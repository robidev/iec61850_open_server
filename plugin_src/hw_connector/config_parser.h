#ifndef CONFIG_PARSER_H
#define CONFIG_PARSER_H

#include <stddef.h>

/* Key-value pair with support for multiple values (CSV) */
typedef struct {
    char *key;
    char **values;      /* Array of values for CSV support */
    int value_count;    /* Number of values (1 for single value) */
} config_entry_t;

/* Configuration section (matches a device) */
typedef struct {
    char *section;
    config_entry_t *entries;
    int entry_count;
    int entry_capacity;
} config_section_t;

/* Main config structure */
typedef struct {
    config_section_t *sections;
    int section_count;
    int section_capacity;
} config_t;

/* Function prototypes */
int config_parse_file(const char *filename, config_t *config);
config_section_t* config_find_section(config_t *config, const char *section_name);
const char* config_get_value(config_section_t *section, const char *key);
const char* config_get_value_at(config_section_t *section, const char *key, int index);
int config_get_value_count(config_section_t *section, const char *key);
void config_free(config_t *config);
void config_print(const config_t *config);

#endif /* CONFIG_PARSER_H */