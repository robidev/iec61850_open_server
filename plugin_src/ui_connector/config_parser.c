#include "config_parser.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define INITIAL_CAPACITY 8

/* Helper: trim whitespace from both ends */
static char* trim(char *str) {
    char *end;
    
    while(isspace((unsigned char)*str)) str++;
    if(*str == 0) return str;
    
    end = str + strlen(str) - 1;
    while(end > str && isspace((unsigned char)*end)) end--;
    end[1] = '\0';
    
    return str;
}

/* Helper: remove inline comments (# or ;) outside of quotes */
static void remove_inline_comment(char *str) {
    int in_quotes = 0;
    char *ptr = str;
    
    while (*ptr) {
        if (*ptr == '"' && (ptr == str || *(ptr - 1) != '\\')) {
            in_quotes = !in_quotes;
        } else if ((*ptr == '#' || *ptr == ';') && !in_quotes) {
            *ptr = '\0';
            break;
        }
        ptr++;
    }
}

/* Helper: parse quoted string, handles escape sequences */
static char* parse_quoted_string(const char *str) {
    size_t len = strlen(str);
    char *result = malloc(len + 1);
    if (!result) return NULL;
    
    const char *src = str;
    char *dst = result;
    int in_quotes = 0;
    
    while (*src) {
        if (*src == '"') {
            in_quotes = !in_quotes;
            src++;
            continue;
        }
        
        if (*src == '\\' && in_quotes && *(src + 1)) {
            src++;
            switch (*src) {
                case 'n': *dst++ = '\n'; break;
                case 't': *dst++ = '\t'; break;
                case 'r': *dst++ = '\r'; break;
                case '\\': *dst++ = '\\'; break;
                case '"': *dst++ = '"'; break;
                default: *dst++ = *src; break;
            }
            src++;
        } else {
            *dst++ = *src++;
        }
    }
    *dst = '\0';
    return result;
}

/* Helper: parse CSV values, respecting quoted strings */
static char** parse_csv(const char *value, int *count) {
    char **values = NULL;
    int capacity = INITIAL_CAPACITY;
    *count = 0;
    
    values = malloc((size_t)(capacity) * sizeof(char*));
    if (!values) return NULL;
    
    char *value_copy = strdup(value);
    if (!value_copy) {
        free(values);
        return NULL;
    }
    
    char *ptr = value_copy;
    char *start = ptr;
    int in_quotes = 0;
    
    while (*ptr) {
        if (*ptr == '"') {
            in_quotes = !in_quotes;
        } else if (*ptr == ',' && !in_quotes) {
            *ptr = '\0';
            char *trimmed = trim(start);
            
            if (*count >= capacity) {
                capacity *= 2;
                char **new_values = realloc(values, (size_t)capacity * sizeof(char*));
                if (!new_values) {
                    for (int i = 0; i < *count; i++) free(values[i]);
                    free(values);
                    free(value_copy);
                    return NULL;
                }
                values = new_values;
            }
            
            values[*count] = parse_quoted_string(trimmed);
            if (!values[*count]) {
                for (int i = 0; i < *count; i++) free(values[i]);
                free(values);
                free(value_copy);
                return NULL;
            }
            (*count)++;
            start = ptr + 1;
        }
        ptr++;
    }
    
    /* Handle last value */
    char *trimmed = trim(start);
    if (*trimmed) {
        if (*count >= capacity) {
            capacity *= 2;
            char **new_values = realloc(values, (size_t)capacity * sizeof(char*));
            if (!new_values) {
                for (int i = 0; i < *count; i++) free(values[i]);
                free(values);
                free(value_copy);
                return NULL;
            }
            values = new_values;
        }
        
        values[*count] = parse_quoted_string(trimmed);
        if (!values[*count]) {
            for (int i = 0; i < *count; i++) free(values[i]);
            free(values);
            free(value_copy);
            return NULL;
        }
        (*count)++;
    }
    
    free(value_copy);
    return values;
}

/* Initialize config structure */
static void config_init(config_t *config) {
    config->sections = malloc(INITIAL_CAPACITY * sizeof(config_section_t));
    config->section_count = 0;
    config->section_capacity = INITIAL_CAPACITY;
}

/* Add a new section */
static config_section_t* config_add_section(config_t *config, const char *name) {
    if (config->section_count >= config->section_capacity) {
        config->section_capacity *= 2;
        config_section_t *new_sections = realloc(config->sections, 
            (size_t)config->section_capacity * sizeof(config_section_t));
        if (!new_sections) return NULL;
        config->sections = new_sections;
    }
    
    config_section_t *section = &config->sections[config->section_count++];
    section->section = strdup(name);
    section->entries = malloc(INITIAL_CAPACITY * sizeof(config_entry_t));
    section->entry_count = 0;
    section->entry_capacity = INITIAL_CAPACITY;
    
    return section;
}

/* Add an entry to a section */
static int section_add_entry(config_section_t *section, const char *key, const char *value) {
    if (section->entry_count >= section->entry_capacity) {
        section->entry_capacity *= 2;
        config_entry_t *new_entries = realloc(section->entries,
            (size_t)section->entry_capacity * sizeof(config_entry_t));
        if (!new_entries) return -1;
        section->entries = new_entries;
    }
    
    config_entry_t *entry = &section->entries[section->entry_count++];
    entry->key = strdup(key);
    
    /* Parse CSV values */
    entry->values = parse_csv(value, &entry->value_count);
    if (!entry->values) {
        free(entry->key);
        section->entry_count--;
        return -1;
    }
    
    return 0;
}

/* Parse INI-style config file with dynamic allocation and quoted strings */
int config_parse_file(const char *filename, config_t *config) {
    FILE *fp;
    char *line = NULL;
    size_t line_size = 0;
    ssize_t read;
    config_section_t *current_section = NULL;
    
    config_init(config);
    
    fp = fopen(filename, "r");
    if (!fp) {
        perror("Failed to open config file");
        return -1;
    }
    
    while ((read = getline(&line, &line_size, fp)) != -1) {
        /* Remove inline comments first */
        remove_inline_comment(line);
        char *trimmed = trim(line);
        
        /* Skip empty lines and comments */
        if (trimmed[0] == '\0' || trimmed[0] == '#' || trimmed[0] == ';') {
            continue;
        }
        
        /* Section header [device_name] */
        if (trimmed[0] == '[') {
            char *end = strchr(trimmed, ']');
            if (end) {
                *end = '\0';
                char *section_name = trim(trimmed + 1);
                current_section = config_add_section(config, section_name);
                if (!current_section) {
                    fprintf(stderr, "Failed to add section\n");
                    free(line);
                    fclose(fp);
                    return -1;
                }
            }
            continue;
        }
        
        /* Key-value pair: key=value */
        char *equals = strchr(trimmed, '=');
        if (equals && current_section) {
            *equals = '\0';
            char *key = trim(trimmed);
            char *value = trim(equals + 1);
            
            if (section_add_entry(current_section, key, value) != 0) {
                fprintf(stderr, "Failed to add entry %s\n", key);
                free(line);
                fclose(fp);
                return -1;
            }
        }
    }
    
    free(line);
    fclose(fp);
    return 0;
}

/* Find a section by name */
config_section_t* config_find_section(config_t *config, const char *section_name) {
    for (int i = 0; i < config->section_count; i++) {
        if (strcmp(config->sections[i].section, section_name) == 0) {
            return &config->sections[i];
        }
    }
    return NULL;
}

/* Get first value from a key */
const char* config_get_value(config_section_t *section, const char *key) {
    return config_get_value_at(section, key, 0);
}

/* Get value at specific index (for CSV entries) */
const char* config_get_value_at(config_section_t *section, const char *key, int index) {
    if (!section) return NULL;
    
    for (int i = 0; i < section->entry_count; i++) {
        if (strcmp(section->entries[i].key, key) == 0) {
            if (index >= 0 && index < section->entries[i].value_count) {
                return section->entries[i].values[index];
            }
            return NULL;
        }
    }
    return NULL;
}

/* Get number of values for a key */
int config_get_value_count(config_section_t *section, const char *key) {
    if (!section) return 0;
    
    for (int i = 0; i < section->entry_count; i++) {
        if (strcmp(section->entries[i].key, key) == 0) {
            return section->entries[i].value_count;
        }
    }
    return 0;
}

/* Free all resources */
void config_free(config_t *config) {
    for (int i = 0; i < config->section_count; i++) {
        config_section_t *section = &config->sections[i];
        free(section->section);
        
        for (int j = 0; j < section->entry_count; j++) {
            config_entry_t *entry = &section->entries[j];
            free(entry->key);
            for (int k = 0; k < entry->value_count; k++) {
                free(entry->values[k]);
            }
            free(entry->values);
        }
        free(section->entries);
    }
    free(config->sections);
}

/* Debug: print entire config */
void config_print(const config_t *config) {
    for (int i = 0; i < config->section_count; i++) {
        printf("[%s]\n", config->sections[i].section);
        for (int j = 0; j < config->sections[i].entry_count; j++) {
            printf("  %s = ", config->sections[i].entries[j].key);
            
            if (config->sections[i].entries[j].value_count == 1) {
                printf("%s\n", config->sections[i].entries[j].values[0]);
            } else {
                printf("[");
                for (int k = 0; k < config->sections[i].entries[j].value_count; k++) {
                    printf("%s%s", 
                           config->sections[i].entries[j].values[k],
                           k < config->sections[i].entries[j].value_count - 1 ? ", " : "");
                }
                printf("]\n");
            }
        }
    }
}