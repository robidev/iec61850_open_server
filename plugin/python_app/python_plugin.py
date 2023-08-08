r"""Wrapper for python_plugin.h

Generated with:
/home/user/.local/bin/ctypesgen -l ../libpython.so -I ../../inc ../../plugin_src/python/python_plugin.h ../../inc/open_server.h -o python_plugin.py

Do not modify this file.
"""

__docformat__ = "restructuredtext"

# Begin preamble for Python

import ctypes
import sys
from ctypes import *  # noqa: F401, F403

_int_types = (ctypes.c_int16, ctypes.c_int32)
if hasattr(ctypes, "c_int64"):
    # Some builds of ctypes apparently do not have ctypes.c_int64
    # defined; it's a pretty good bet that these builds do not
    # have 64-bit pointers.
    _int_types += (ctypes.c_int64,)
for t in _int_types:
    if ctypes.sizeof(t) == ctypes.sizeof(ctypes.c_size_t):
        c_ptrdiff_t = t
del t
del _int_types



class UserString:
    def __init__(self, seq):
        if isinstance(seq, bytes):
            self.data = seq
        elif isinstance(seq, UserString):
            self.data = seq.data[:]
        else:
            self.data = str(seq).encode()

    def __bytes__(self):
        return self.data

    def __str__(self):
        return self.data.decode()

    def __repr__(self):
        return repr(self.data)

    def __int__(self):
        return int(self.data.decode())

    def __long__(self):
        return int(self.data.decode())

    def __float__(self):
        return float(self.data.decode())

    def __complex__(self):
        return complex(self.data.decode())

    def __hash__(self):
        return hash(self.data)

    def __le__(self, string):
        if isinstance(string, UserString):
            return self.data <= string.data
        else:
            return self.data <= string

    def __lt__(self, string):
        if isinstance(string, UserString):
            return self.data < string.data
        else:
            return self.data < string

    def __ge__(self, string):
        if isinstance(string, UserString):
            return self.data >= string.data
        else:
            return self.data >= string

    def __gt__(self, string):
        if isinstance(string, UserString):
            return self.data > string.data
        else:
            return self.data > string

    def __eq__(self, string):
        if isinstance(string, UserString):
            return self.data == string.data
        else:
            return self.data == string

    def __ne__(self, string):
        if isinstance(string, UserString):
            return self.data != string.data
        else:
            return self.data != string

    def __contains__(self, char):
        return char in self.data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.__class__(self.data[index])

    def __getslice__(self, start, end):
        start = max(start, 0)
        end = max(end, 0)
        return self.__class__(self.data[start:end])

    def __add__(self, other):
        if isinstance(other, UserString):
            return self.__class__(self.data + other.data)
        elif isinstance(other, bytes):
            return self.__class__(self.data + other)
        else:
            return self.__class__(self.data + str(other).encode())

    def __radd__(self, other):
        if isinstance(other, bytes):
            return self.__class__(other + self.data)
        else:
            return self.__class__(str(other).encode() + self.data)

    def __mul__(self, n):
        return self.__class__(self.data * n)

    __rmul__ = __mul__

    def __mod__(self, args):
        return self.__class__(self.data % args)

    # the following methods are defined in alphabetical order:
    def capitalize(self):
        return self.__class__(self.data.capitalize())

    def center(self, width, *args):
        return self.__class__(self.data.center(width, *args))

    def count(self, sub, start=0, end=sys.maxsize):
        return self.data.count(sub, start, end)

    def decode(self, encoding=None, errors=None):  # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.decode(encoding, errors))
            else:
                return self.__class__(self.data.decode(encoding))
        else:
            return self.__class__(self.data.decode())

    def encode(self, encoding=None, errors=None):  # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.encode(encoding, errors))
            else:
                return self.__class__(self.data.encode(encoding))
        else:
            return self.__class__(self.data.encode())

    def endswith(self, suffix, start=0, end=sys.maxsize):
        return self.data.endswith(suffix, start, end)

    def expandtabs(self, tabsize=8):
        return self.__class__(self.data.expandtabs(tabsize))

    def find(self, sub, start=0, end=sys.maxsize):
        return self.data.find(sub, start, end)

    def index(self, sub, start=0, end=sys.maxsize):
        return self.data.index(sub, start, end)

    def isalpha(self):
        return self.data.isalpha()

    def isalnum(self):
        return self.data.isalnum()

    def isdecimal(self):
        return self.data.isdecimal()

    def isdigit(self):
        return self.data.isdigit()

    def islower(self):
        return self.data.islower()

    def isnumeric(self):
        return self.data.isnumeric()

    def isspace(self):
        return self.data.isspace()

    def istitle(self):
        return self.data.istitle()

    def isupper(self):
        return self.data.isupper()

    def join(self, seq):
        return self.data.join(seq)

    def ljust(self, width, *args):
        return self.__class__(self.data.ljust(width, *args))

    def lower(self):
        return self.__class__(self.data.lower())

    def lstrip(self, chars=None):
        return self.__class__(self.data.lstrip(chars))

    def partition(self, sep):
        return self.data.partition(sep)

    def replace(self, old, new, maxsplit=-1):
        return self.__class__(self.data.replace(old, new, maxsplit))

    def rfind(self, sub, start=0, end=sys.maxsize):
        return self.data.rfind(sub, start, end)

    def rindex(self, sub, start=0, end=sys.maxsize):
        return self.data.rindex(sub, start, end)

    def rjust(self, width, *args):
        return self.__class__(self.data.rjust(width, *args))

    def rpartition(self, sep):
        return self.data.rpartition(sep)

    def rstrip(self, chars=None):
        return self.__class__(self.data.rstrip(chars))

    def split(self, sep=None, maxsplit=-1):
        return self.data.split(sep, maxsplit)

    def rsplit(self, sep=None, maxsplit=-1):
        return self.data.rsplit(sep, maxsplit)

    def splitlines(self, keepends=0):
        return self.data.splitlines(keepends)

    def startswith(self, prefix, start=0, end=sys.maxsize):
        return self.data.startswith(prefix, start, end)

    def strip(self, chars=None):
        return self.__class__(self.data.strip(chars))

    def swapcase(self):
        return self.__class__(self.data.swapcase())

    def title(self):
        return self.__class__(self.data.title())

    def translate(self, *args):
        return self.__class__(self.data.translate(*args))

    def upper(self):
        return self.__class__(self.data.upper())

    def zfill(self, width):
        return self.__class__(self.data.zfill(width))


class MutableString(UserString):
    """mutable string objects

    Python strings are immutable objects.  This has the advantage, that
    strings may be used as dictionary keys.  If this property isn't needed
    and you insist on changing string values in place instead, you may cheat
    and use MutableString.

    But the purpose of this class is an educational one: to prevent
    people from inventing their own mutable string class derived
    from UserString and than forget thereby to remove (override) the
    __hash__ method inherited from UserString.  This would lead to
    errors that would be very hard to track down.

    A faster and better solution is to rewrite your program using lists."""

    def __init__(self, string=""):
        self.data = string

    def __hash__(self):
        raise TypeError("unhashable type (it is mutable)")

    def __setitem__(self, index, sub):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data):
            raise IndexError
        self.data = self.data[:index] + sub + self.data[index + 1 :]

    def __delitem__(self, index):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data):
            raise IndexError
        self.data = self.data[:index] + self.data[index + 1 :]

    def __setslice__(self, start, end, sub):
        start = max(start, 0)
        end = max(end, 0)
        if isinstance(sub, UserString):
            self.data = self.data[:start] + sub.data + self.data[end:]
        elif isinstance(sub, bytes):
            self.data = self.data[:start] + sub + self.data[end:]
        else:
            self.data = self.data[:start] + str(sub).encode() + self.data[end:]

    def __delslice__(self, start, end):
        start = max(start, 0)
        end = max(end, 0)
        self.data = self.data[:start] + self.data[end:]

    def immutable(self):
        return UserString(self.data)

    def __iadd__(self, other):
        if isinstance(other, UserString):
            self.data += other.data
        elif isinstance(other, bytes):
            self.data += other
        else:
            self.data += str(other).encode()
        return self

    def __imul__(self, n):
        self.data *= n
        return self


class String(MutableString, ctypes.Union):

    _fields_ = [("raw", ctypes.POINTER(ctypes.c_char)), ("data", ctypes.c_char_p)]

    def __init__(self, obj=b""):
        if isinstance(obj, (bytes, UserString)):
            self.data = bytes(obj)
        else:
            self.raw = obj

    def __len__(self):
        return self.data and len(self.data) or 0

    def from_param(cls, obj):
        # Convert None or 0
        if obj is None or obj == 0:
            return cls(ctypes.POINTER(ctypes.c_char)())

        # Convert from String
        elif isinstance(obj, String):
            return obj

        # Convert from bytes
        elif isinstance(obj, bytes):
            return cls(obj)

        # Convert from str
        elif isinstance(obj, str):
            return cls(obj.encode())

        # Convert from c_char_p
        elif isinstance(obj, ctypes.c_char_p):
            return obj

        # Convert from POINTER(ctypes.c_char)
        elif isinstance(obj, ctypes.POINTER(ctypes.c_char)):
            return obj

        # Convert from raw pointer
        elif isinstance(obj, int):
            return cls(ctypes.cast(obj, ctypes.POINTER(ctypes.c_char)))

        # Convert from ctypes.c_char array
        elif isinstance(obj, ctypes.c_char * len(obj)):
            return obj

        # Convert from object
        else:
            return String.from_param(obj._as_parameter_)

    from_param = classmethod(from_param)


def ReturnString(obj, func=None, arguments=None):
    return String.from_param(obj)


# As of ctypes 1.0, ctypes does not support custom error-checking
# functions on callbacks, nor does it support custom datatypes on
# callbacks, so we must ensure that all callbacks return
# primitive datatypes.
#
# Non-primitive return values wrapped with UNCHECKED won't be
# typechecked, and will be converted to ctypes.c_void_p.
def UNCHECKED(type):
    if hasattr(type, "_type_") and isinstance(type._type_, str) and type._type_ != "P":
        return type
    else:
        return ctypes.c_void_p


# ctypes doesn't have direct support for variadic functions, so we have to write
# our own wrapper class
class _variadic_function(object):
    def __init__(self, func, restype, argtypes, errcheck):
        self.func = func
        self.func.restype = restype
        self.argtypes = argtypes
        if errcheck:
            self.func.errcheck = errcheck

    def _as_parameter_(self):
        # So we can pass this variadic function as a function pointer
        return self.func

    def __call__(self, *args):
        fixed_args = []
        i = 0
        for argtype in self.argtypes:
            # Typecheck what we can
            fixed_args.append(argtype.from_param(args[i]))
            i += 1
        return self.func(*fixed_args + list(args[i:]))


def ord_if_char(value):
    """
    Simple helper used for casts to simple builtin types:  if the argument is a
    string type, it will be converted to it's ordinal value.

    This function will raise an exception if the argument is string with more
    than one characters.
    """
    return ord(value) if (isinstance(value, bytes) or isinstance(value, str)) else value

# End preamble

_libs = {}
_libdirs = []

# Begin loader

"""
Load libraries - appropriately for all our supported platforms
"""
# ----------------------------------------------------------------------------
# Copyright (c) 2008 David James
# Copyright (c) 2006-2008 Alex Holkner
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

import ctypes
import ctypes.util
import glob
import os.path
import platform
import re
import sys


def _environ_path(name):
    """Split an environment variable into a path-like list elements"""
    if name in os.environ:
        return os.environ[name].split(":")
    return []


class LibraryLoader:
    """
    A base class For loading of libraries ;-)
    Subclasses load libraries for specific platforms.
    """

    # library names formatted specifically for platforms
    name_formats = ["%s"]

    class Lookup:
        """Looking up calling conventions for a platform"""

        mode = ctypes.DEFAULT_MODE

        def __init__(self, path):
            super(LibraryLoader.Lookup, self).__init__()
            self.access = dict(cdecl=ctypes.CDLL(path, self.mode))

        def get(self, name, calling_convention="cdecl"):
            """Return the given name according to the selected calling convention"""
            if calling_convention not in self.access:
                raise LookupError(
                    "Unknown calling convention '{}' for function '{}'".format(
                        calling_convention, name
                    )
                )
            return getattr(self.access[calling_convention], name)

        def has(self, name, calling_convention="cdecl"):
            """Return True if this given calling convention finds the given 'name'"""
            if calling_convention not in self.access:
                return False
            return hasattr(self.access[calling_convention], name)

        def __getattr__(self, name):
            return getattr(self.access["cdecl"], name)

    def __init__(self):
        self.other_dirs = []

    def __call__(self, libname):
        """Given the name of a library, load it."""
        paths = self.getpaths(libname)

        for path in paths:
            # noinspection PyBroadException
            try:
                return self.Lookup(path)
            except Exception:  # pylint: disable=broad-except
                pass

        raise ImportError("Could not load %s." % libname)

    def getpaths(self, libname):
        """Return a list of paths where the library might be found."""
        if os.path.isabs(libname):
            yield libname
        else:
            # search through a prioritized series of locations for the library

            # we first search any specific directories identified by user
            for dir_i in self.other_dirs:
                for fmt in self.name_formats:
                    # dir_i should be absolute already
                    yield os.path.join(dir_i, fmt % libname)

            # check if this code is even stored in a physical file
            try:
                this_file = __file__
            except NameError:
                this_file = None

            # then we search the directory where the generated python interface is stored
            if this_file is not None:
                for fmt in self.name_formats:
                    yield os.path.abspath(os.path.join(os.path.dirname(__file__), fmt % libname))

            # now, use the ctypes tools to try to find the library
            for fmt in self.name_formats:
                path = ctypes.util.find_library(fmt % libname)
                if path:
                    yield path

            # then we search all paths identified as platform-specific lib paths
            for path in self.getplatformpaths(libname):
                yield path

            # Finally, we'll try the users current working directory
            for fmt in self.name_formats:
                yield os.path.abspath(os.path.join(os.path.curdir, fmt % libname))

    def getplatformpaths(self, _libname):  # pylint: disable=no-self-use
        """Return all the library paths available in this platform"""
        return []


# Darwin (Mac OS X)


class DarwinLibraryLoader(LibraryLoader):
    """Library loader for MacOS"""

    name_formats = [
        "lib%s.dylib",
        "lib%s.so",
        "lib%s.bundle",
        "%s.dylib",
        "%s.so",
        "%s.bundle",
        "%s",
    ]

    class Lookup(LibraryLoader.Lookup):
        """
        Looking up library files for this platform (Darwin aka MacOS)
        """

        # Darwin requires dlopen to be called with mode RTLD_GLOBAL instead
        # of the default RTLD_LOCAL.  Without this, you end up with
        # libraries not being loadable, resulting in "Symbol not found"
        # errors
        mode = ctypes.RTLD_GLOBAL

    def getplatformpaths(self, libname):
        if os.path.pathsep in libname:
            names = [libname]
        else:
            names = [fmt % libname for fmt in self.name_formats]

        for directory in self.getdirs(libname):
            for name in names:
                yield os.path.join(directory, name)

    @staticmethod
    def getdirs(libname):
        """Implements the dylib search as specified in Apple documentation:

        http://developer.apple.com/documentation/DeveloperTools/Conceptual/
            DynamicLibraries/Articles/DynamicLibraryUsageGuidelines.html

        Before commencing the standard search, the method first checks
        the bundle's ``Frameworks`` directory if the application is running
        within a bundle (OS X .app).
        """

        dyld_fallback_library_path = _environ_path("DYLD_FALLBACK_LIBRARY_PATH")
        if not dyld_fallback_library_path:
            dyld_fallback_library_path = [
                os.path.expanduser("~/lib"),
                "/usr/local/lib",
                "/usr/lib",
            ]

        dirs = []

        if "/" in libname:
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
        else:
            dirs.extend(_environ_path("LD_LIBRARY_PATH"))
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
            dirs.extend(_environ_path("LD_RUN_PATH"))

        if hasattr(sys, "frozen") and getattr(sys, "frozen") == "macosx_app":
            dirs.append(os.path.join(os.environ["RESOURCEPATH"], "..", "Frameworks"))

        dirs.extend(dyld_fallback_library_path)

        return dirs


# Posix


class PosixLibraryLoader(LibraryLoader):
    """Library loader for POSIX-like systems (including Linux)"""

    _ld_so_cache = None

    _include = re.compile(r"^\s*include\s+(?P<pattern>.*)")

    name_formats = ["lib%s.so", "%s.so", "%s"]

    class _Directories(dict):
        """Deal with directories"""

        def __init__(self):
            dict.__init__(self)
            self.order = 0

        def add(self, directory):
            """Add a directory to our current set of directories"""
            if len(directory) > 1:
                directory = directory.rstrip(os.path.sep)
            # only adds and updates order if exists and not already in set
            if not os.path.exists(directory):
                return
            order = self.setdefault(directory, self.order)
            if order == self.order:
                self.order += 1

        def extend(self, directories):
            """Add a list of directories to our set"""
            for a_dir in directories:
                self.add(a_dir)

        def ordered(self):
            """Sort the list of directories"""
            return (i[0] for i in sorted(self.items(), key=lambda d: d[1]))

    def _get_ld_so_conf_dirs(self, conf, dirs):
        """
        Recursive function to help parse all ld.so.conf files, including proper
        handling of the `include` directive.
        """

        try:
            with open(conf) as fileobj:
                for dirname in fileobj:
                    dirname = dirname.strip()
                    if not dirname:
                        continue

                    match = self._include.match(dirname)
                    if not match:
                        dirs.add(dirname)
                    else:
                        for dir2 in glob.glob(match.group("pattern")):
                            self._get_ld_so_conf_dirs(dir2, dirs)
        except IOError:
            pass

    def _create_ld_so_cache(self):
        # Recreate search path followed by ld.so.  This is going to be
        # slow to build, and incorrect (ld.so uses ld.so.cache, which may
        # not be up-to-date).  Used only as fallback for distros without
        # /sbin/ldconfig.
        #
        # We assume the DT_RPATH and DT_RUNPATH binary sections are omitted.

        directories = self._Directories()
        for name in (
            "LD_LIBRARY_PATH",
            "SHLIB_PATH",  # HP-UX
            "LIBPATH",  # OS/2, AIX
            "LIBRARY_PATH",  # BE/OS
        ):
            if name in os.environ:
                directories.extend(os.environ[name].split(os.pathsep))

        self._get_ld_so_conf_dirs("/etc/ld.so.conf", directories)

        bitage = platform.architecture()[0]

        unix_lib_dirs_list = []
        if bitage.startswith("64"):
            # prefer 64 bit if that is our arch
            unix_lib_dirs_list += ["/lib64", "/usr/lib64"]

        # must include standard libs, since those paths are also used by 64 bit
        # installs
        unix_lib_dirs_list += ["/lib", "/usr/lib"]
        if sys.platform.startswith("linux"):
            # Try and support multiarch work in Ubuntu
            # https://wiki.ubuntu.com/MultiarchSpec
            if bitage.startswith("32"):
                # Assume Intel/AMD x86 compat
                unix_lib_dirs_list += ["/lib/i386-linux-gnu", "/usr/lib/i386-linux-gnu"]
            elif bitage.startswith("64"):
                # Assume Intel/AMD x86 compatible
                unix_lib_dirs_list += [
                    "/lib/x86_64-linux-gnu",
                    "/usr/lib/x86_64-linux-gnu",
                ]
            else:
                # guess...
                unix_lib_dirs_list += glob.glob("/lib/*linux-gnu")
        directories.extend(unix_lib_dirs_list)

        cache = {}
        lib_re = re.compile(r"lib(.*)\.s[ol]")
        # ext_re = re.compile(r"\.s[ol]$")
        for our_dir in directories.ordered():
            try:
                for path in glob.glob("%s/*.s[ol]*" % our_dir):
                    file = os.path.basename(path)

                    # Index by filename
                    cache_i = cache.setdefault(file, set())
                    cache_i.add(path)

                    # Index by library name
                    match = lib_re.match(file)
                    if match:
                        library = match.group(1)
                        cache_i = cache.setdefault(library, set())
                        cache_i.add(path)
            except OSError:
                pass

        self._ld_so_cache = cache

    def getplatformpaths(self, libname):
        if self._ld_so_cache is None:
            self._create_ld_so_cache()

        result = self._ld_so_cache.get(libname, set())
        for i in result:
            # we iterate through all found paths for library, since we may have
            # actually found multiple architectures or other library types that
            # may not load
            yield i


# Windows


class WindowsLibraryLoader(LibraryLoader):
    """Library loader for Microsoft Windows"""

    name_formats = ["%s.dll", "lib%s.dll", "%slib.dll", "%s"]

    class Lookup(LibraryLoader.Lookup):
        """Lookup class for Windows libraries..."""

        def __init__(self, path):
            super(WindowsLibraryLoader.Lookup, self).__init__(path)
            self.access["stdcall"] = ctypes.windll.LoadLibrary(path)


# Platform switching

# If your value of sys.platform does not appear in this dict, please contact
# the Ctypesgen maintainers.

loaderclass = {
    "darwin": DarwinLibraryLoader,
    "cygwin": WindowsLibraryLoader,
    "win32": WindowsLibraryLoader,
    "msys": WindowsLibraryLoader,
}

load_library = loaderclass.get(sys.platform, PosixLibraryLoader)()


def add_library_search_dirs(other_dirs):
    """
    Add libraries to search paths.
    If library paths are relative, convert them to absolute with respect to this
    file's directory
    """
    for path in other_dirs:
        if not os.path.isabs(path):
            path = os.path.abspath(path)
        load_library.other_dirs.append(path)


del loaderclass

# End loader

add_library_search_dirs([])

# Begin libraries
_libs["../libpython.so"] = load_library("../libpython.so")

# 1 libraries
# End libraries

# No modules

__uint8_t = c_ubyte# /usr/include/x86_64-linux-gnu/bits/types.h: 38

__uint16_t = c_ushort# /usr/include/x86_64-linux-gnu/bits/types.h: 40

__uint32_t = c_uint# /usr/include/x86_64-linux-gnu/bits/types.h: 42

__uint64_t = c_ulong# /usr/include/x86_64-linux-gnu/bits/types.h: 45

uint8_t = __uint8_t# /usr/include/x86_64-linux-gnu/bits/stdint-uintn.h: 24

uint16_t = __uint16_t# /usr/include/x86_64-linux-gnu/bits/stdint-uintn.h: 25

uint32_t = __uint32_t# /usr/include/x86_64-linux-gnu/bits/stdint-uintn.h: 26

uint64_t = __uint64_t# /usr/include/x86_64-linux-gnu/bits/stdint-uintn.h: 27

# /usr/local/include/libiec61850/mms_value.h: 68
class struct_sMmsValue(Structure):
    pass

MmsValue = struct_sMmsValue# /usr/local/include/libiec61850/mms_value.h: 68

# /usr/local/include/libiec61850/linked_list.h: 44
class struct_sLinkedList(Structure):
    pass

struct_sLinkedList.__slots__ = [
    'data',
    'next',
]
struct_sLinkedList._fields_ = [
    ('data', POINTER(None)),
    ('next', POINTER(struct_sLinkedList)),
]

LinkedList = POINTER(struct_sLinkedList)# /usr/local/include/libiec61850/linked_list.h: 52

# /usr/local/include/libiec61850/iec61850_common.h: 56
class struct_anon_25(Structure):
    pass

struct_anon_25.__slots__ = [
    'vlanPriority',
    'vlanId',
    'appId',
    'dstAddress',
]
struct_anon_25._fields_ = [
    ('vlanPriority', uint8_t),
    ('vlanId', uint16_t),
    ('appId', uint16_t),
    ('dstAddress', uint8_t * int(6)),
]

PhyComAddress = struct_anon_25# /usr/local/include/libiec61850/iec61850_common.h: 56

# /usr/local/include/libiec61850/iec61850_model.h: 192
class struct_sModelNode(Structure):
    pass

ModelNode = struct_sModelNode# /usr/local/include/libiec61850/iec61850_model.h: 46

# /usr/local/include/libiec61850/iec61850_model.h: 200
class struct_sLogicalNode(Structure):
    pass

LogicalNode = struct_sLogicalNode# /usr/local/include/libiec61850/iec61850_model.h: 61

# /usr/local/include/libiec61850/iec61850_model.h: 184
class struct_sLogicalDevice(Structure):
    pass

LogicalDevice = struct_sLogicalDevice# /usr/local/include/libiec61850/iec61850_model.h: 66

# /usr/local/include/libiec61850/iec61850_model.h: 171
class struct_sIedModel(Structure):
    pass

IedModel = struct_sIedModel# /usr/local/include/libiec61850/iec61850_model.h: 71

# /usr/local/include/libiec61850/iec61850_model.h: 247
class struct_sDataSet(Structure):
    pass

DataSet = struct_sDataSet# /usr/local/include/libiec61850/iec61850_model.h: 73

# /usr/local/include/libiec61850/iec61850_model.h: 255
class struct_sReportControlBlock(Structure):
    pass

ReportControlBlock = struct_sReportControlBlock# /usr/local/include/libiec61850/iec61850_model.h: 74

# /usr/local/include/libiec61850/iec61850_model.h: 302
class struct_sSettingGroupControlBlock(Structure):
    pass

SettingGroupControlBlock = struct_sSettingGroupControlBlock# /usr/local/include/libiec61850/iec61850_model.h: 79

# /usr/local/include/libiec61850/iec61850_model.h: 316
class struct_sGSEControlBlock(Structure):
    pass

GSEControlBlock = struct_sGSEControlBlock# /usr/local/include/libiec61850/iec61850_model.h: 81

# /usr/local/include/libiec61850/iec61850_model.h: 329
class struct_sSVControlBlock(Structure):
    pass

SVControlBlock = struct_sSVControlBlock# /usr/local/include/libiec61850/iec61850_model.h: 83

# /usr/local/include/libiec61850/iec61850_model.h: 277
class struct_sLogControlBlock(Structure):
    pass

LogControlBlock = struct_sLogControlBlock# /usr/local/include/libiec61850/iec61850_model.h: 85

# /usr/local/include/libiec61850/iec61850_model.h: 294
class struct_sLog(Structure):
    pass

Log = struct_sLog# /usr/local/include/libiec61850/iec61850_model.h: 87

enum_anon_32 = c_int# /usr/local/include/libiec61850/iec61850_model.h: 169

ModelNodeType = enum_anon_32# /usr/local/include/libiec61850/iec61850_model.h: 169

struct_sIedModel.__slots__ = [
    'name',
    'firstChild',
    'dataSets',
    'rcbs',
    'gseCBs',
    'svCBs',
    'sgcbs',
    'lcbs',
    'logs',
    'initializer',
]
struct_sIedModel._fields_ = [
    ('name', String),
    ('firstChild', POINTER(LogicalDevice)),
    ('dataSets', POINTER(DataSet)),
    ('rcbs', POINTER(ReportControlBlock)),
    ('gseCBs', POINTER(GSEControlBlock)),
    ('svCBs', POINTER(SVControlBlock)),
    ('sgcbs', POINTER(SettingGroupControlBlock)),
    ('lcbs', POINTER(LogControlBlock)),
    ('logs', POINTER(Log)),
    ('initializer', CFUNCTYPE(UNCHECKED(None), )),
]

struct_sLogicalDevice.__slots__ = [
    'modelType',
    'name',
    'parent',
    'sibling',
    'firstChild',
]
struct_sLogicalDevice._fields_ = [
    ('modelType', ModelNodeType),
    ('name', String),
    ('parent', POINTER(ModelNode)),
    ('sibling', POINTER(ModelNode)),
    ('firstChild', POINTER(ModelNode)),
]

struct_sModelNode.__slots__ = [
    'modelType',
    'name',
    'parent',
    'sibling',
    'firstChild',
]
struct_sModelNode._fields_ = [
    ('modelType', ModelNodeType),
    ('name', String),
    ('parent', POINTER(ModelNode)),
    ('sibling', POINTER(ModelNode)),
    ('firstChild', POINTER(ModelNode)),
]

struct_sLogicalNode.__slots__ = [
    'modelType',
    'name',
    'parent',
    'sibling',
    'firstChild',
]
struct_sLogicalNode._fields_ = [
    ('modelType', ModelNodeType),
    ('name', String),
    ('parent', POINTER(ModelNode)),
    ('sibling', POINTER(ModelNode)),
    ('firstChild', POINTER(ModelNode)),
]

# /usr/local/include/libiec61850/iec61850_model.h: 237
class struct_sDataSetEntry(Structure):
    pass

struct_sDataSetEntry.__slots__ = [
    'logicalDeviceName',
    'isLDNameDynamicallyAllocated',
    'variableName',
    'index',
    'componentName',
    'value',
    'sibling',
]
struct_sDataSetEntry._fields_ = [
    ('logicalDeviceName', String),
    ('isLDNameDynamicallyAllocated', c_bool),
    ('variableName', String),
    ('index', c_int),
    ('componentName', String),
    ('value', POINTER(MmsValue)),
    ('sibling', POINTER(struct_sDataSetEntry)),
]

DataSetEntry = struct_sDataSetEntry# /usr/local/include/libiec61850/iec61850_model.h: 245

struct_sDataSet.__slots__ = [
    'logicalDeviceName',
    'name',
    'elementCount',
    'fcdas',
    'sibling',
]
struct_sDataSet._fields_ = [
    ('logicalDeviceName', String),
    ('name', String),
    ('elementCount', c_int),
    ('fcdas', POINTER(DataSetEntry)),
    ('sibling', POINTER(DataSet)),
]

struct_sReportControlBlock.__slots__ = [
    'parent',
    'name',
    'rptId',
    'buffered',
    'dataSetName',
    'confRef',
    'trgOps',
    'options',
    'bufferTime',
    'intPeriod',
    'clientReservation',
    'sibling',
]
struct_sReportControlBlock._fields_ = [
    ('parent', POINTER(LogicalNode)),
    ('name', String),
    ('rptId', String),
    ('buffered', c_bool),
    ('dataSetName', String),
    ('confRef', uint32_t),
    ('trgOps', uint8_t),
    ('options', uint8_t),
    ('bufferTime', uint32_t),
    ('intPeriod', uint32_t),
    ('clientReservation', uint8_t * int(17)),
    ('sibling', POINTER(ReportControlBlock)),
]

struct_sLogControlBlock.__slots__ = [
    'parent',
    'name',
    'dataSetName',
    'logRef',
    'trgOps',
    'intPeriod',
    'logEna',
    'reasonCode',
    'sibling',
]
struct_sLogControlBlock._fields_ = [
    ('parent', POINTER(LogicalNode)),
    ('name', String),
    ('dataSetName', String),
    ('logRef', String),
    ('trgOps', uint8_t),
    ('intPeriod', uint32_t),
    ('logEna', c_bool),
    ('reasonCode', c_bool),
    ('sibling', POINTER(LogControlBlock)),
]

struct_sLog.__slots__ = [
    'parent',
    'name',
    'sibling',
]
struct_sLog._fields_ = [
    ('parent', POINTER(LogicalNode)),
    ('name', String),
    ('sibling', POINTER(Log)),
]

struct_sSettingGroupControlBlock.__slots__ = [
    'parent',
    'actSG',
    'numOfSGs',
    'editSG',
    'cnfEdit',
    'timestamp',
    'resvTms',
    'sibling',
]
struct_sSettingGroupControlBlock._fields_ = [
    ('parent', POINTER(LogicalNode)),
    ('actSG', uint8_t),
    ('numOfSGs', uint8_t),
    ('editSG', uint8_t),
    ('cnfEdit', c_bool),
    ('timestamp', uint64_t),
    ('resvTms', uint16_t),
    ('sibling', POINTER(SettingGroupControlBlock)),
]

struct_sGSEControlBlock.__slots__ = [
    'parent',
    'name',
    'appId',
    'dataSetName',
    'confRev',
    'fixedOffs',
    'address',
    'minTime',
    'maxTime',
    'sibling',
]
struct_sGSEControlBlock._fields_ = [
    ('parent', POINTER(LogicalNode)),
    ('name', String),
    ('appId', String),
    ('dataSetName', String),
    ('confRev', uint32_t),
    ('fixedOffs', c_bool),
    ('address', POINTER(PhyComAddress)),
    ('minTime', c_int),
    ('maxTime', c_int),
    ('sibling', POINTER(GSEControlBlock)),
]

struct_sSVControlBlock.__slots__ = [
    'parent',
    'name',
    'svId',
    'dataSetName',
    'optFlds',
    'smpMod',
    'smpRate',
    'confRev',
    'dstAddress',
    'isUnicast',
    'noASDU',
    'sibling',
]
struct_sSVControlBlock._fields_ = [
    ('parent', POINTER(LogicalNode)),
    ('name', String),
    ('svId', String),
    ('dataSetName', String),
    ('optFlds', uint8_t),
    ('smpMod', uint8_t),
    ('smpRate', uint16_t),
    ('confRev', uint32_t),
    ('dstAddress', POINTER(PhyComAddress)),
    ('isUnicast', c_bool),
    ('noASDU', c_int),
    ('sibling', POINTER(SVControlBlock)),
]

# /usr/local/include/libiec61850/iec61850_server.h: 425
class struct_sIedServer(Structure):
    pass

IedServer = POINTER(struct_sIedServer)# /usr/local/include/libiec61850/iec61850_server.h: 425

# ../../inc/iec61850_model_extensions.h: 38
class struct_sIedModel_extensions(Structure):
    pass

IedModel_extensions = struct_sIedModel_extensions# ../../inc/iec61850_model_extensions.h: 30

# ../../inc/iec61850_model_extensions.h: 79
class struct_sLogicalNodeClass(Structure):
    pass

LogicalNodeClass = struct_sLogicalNodeClass# ../../inc/iec61850_model_extensions.h: 31

# ../../inc/iec61850_model_extensions.h: 60
class struct_sInput(Structure):
    pass

Input = struct_sInput# ../../inc/iec61850_model_extensions.h: 32

# ../../inc/iec61850_model_extensions.h: 68
class struct_sSubscriberEntry(Structure):
    pass

SubscriberEntry = struct_sSubscriberEntry# ../../inc/iec61850_model_extensions.h: 33

callBackFunction = CFUNCTYPE(UNCHECKED(None), POINTER(None))# ../../inc/iec61850_model_extensions.h: 34

struct_sIedModel_extensions.__slots__ = [
    'inputs',
    'subRefs',
    'logicalNodes',
]
struct_sIedModel_extensions._fields_ = [
    ('inputs', POINTER(Input)),
    ('subRefs', POINTER(SubscriberEntry)),
    ('logicalNodes', POINTER(LogicalNodeClass)),
]

# ../../inc/iec61850_model_extensions.h: 45
class struct_sInputEntry(Structure):
    pass

struct_sInputEntry.__slots__ = [
    'desc',
    'Ref',
    'intAddr',
    'serviceType',
    'srcRef',
    'value',
    'callBack',
    'callBackParam',
    'sibling',
]
struct_sInputEntry._fields_ = [
    ('desc', String),
    ('Ref', String),
    ('intAddr', String),
    ('serviceType', String),
    ('srcRef', String),
    ('value', POINTER(MmsValue)),
    ('callBack', callBackFunction),
    ('callBackParam', POINTER(None)),
    ('sibling', POINTER(struct_sInputEntry)),
]

InputEntry = struct_sInputEntry# ../../inc/iec61850_model_extensions.h: 57

struct_sInput.__slots__ = [
    'parent',
    'elementCount',
    'extRefs',
    'sibling',
]
struct_sInput._fields_ = [
    ('parent', POINTER(LogicalNode)),
    ('elementCount', c_int),
    ('extRefs', POINTER(InputEntry)),
    ('sibling', POINTER(Input)),
]

struct_sSubscriberEntry.__slots__ = [
    'variableName',
    'Dataset',
    'APPID',
    'cbRef',
    'ID',
    'ethAddr',
    'sibling',
]
struct_sSubscriberEntry._fields_ = [
    ('variableName', String),
    ('Dataset', String),
    ('APPID', uint16_t),
    ('cbRef', String),
    ('ID', String),
    ('ethAddr', uint8_t * int(6)),
    ('sibling', POINTER(struct_sSubscriberEntry)),
]

struct_sLogicalNodeClass.__slots__ = [
    'parent',
    'lnClass',
    'instance',
    'sibling',
]
struct_sLogicalNodeClass._fields_ = [
    ('parent', POINTER(LogicalNode)),
    ('lnClass', String),
    ('instance', POINTER(None)),
    ('sibling', POINTER(LogicalNodeClass)),
]

# ../../inc/LNParse.h: 15
class struct_sSMVcB(Structure):
    pass

SMVcB = struct_sSMVcB# ../../inc/LNParse.h: 13

struct_sSMVcB.__slots__ = [
    'svCBs',
    'instance',
    'sibling',
]
struct_sSMVcB._fields_ = [
    ('svCBs', POINTER(SVControlBlock)),
    ('instance', POINTER(None)),
    ('sibling', POINTER(SMVcB)),
]

# ../../inc/open_server.h: 18
class struct_sOpenServerInstance(Structure):
    pass

struct_sOpenServerInstance.__slots__ = [
    'server',
    'Model',
    'Model_ex',
    'SMVControlInstances',
    'allInputValues',
]
struct_sOpenServerInstance._fields_ = [
    ('server', IedServer),
    ('Model', POINTER(IedModel)),
    ('Model_ex', POINTER(IedModel_extensions)),
    ('SMVControlInstances', POINTER(SMVcB)),
    ('allInputValues', LinkedList),
]

OpenServerInstance = struct_sOpenServerInstance# ../../inc/open_server.h: 18

lib_init_func = CFUNCTYPE(UNCHECKED(c_int), POINTER(OpenServerInstance))# ../../inc/open_server.h: 20

# ../../inc/open_server.h: 23
for _lib in _libs.values():
    if not _lib.has("open_server_running", "cdecl"):
        continue
    open_server_running = _lib.get("open_server_running", "cdecl")
    open_server_running.argtypes = []
    open_server_running.restype = c_int
    break

# /home/user/Desktop/scada/iec61850_open_server/plugin_src/python/python_plugin.h: 14
for _lib in _libs.values():
    if not _lib.has("getDataRefFromModel", "cdecl"):
        continue
    getDataRefFromModel = _lib.get("getDataRefFromModel", "cdecl")
    getDataRefFromModel.argtypes = [POINTER(OpenServerInstance), String]
    getDataRefFromModel.restype = POINTER(MmsValue)
    break

# /home/user/Desktop/scada/iec61850_open_server/plugin_src/python/python_plugin.h: 15
for _lib in _libs.values():
    if not _lib.has("updateDataRef", "cdecl"):
        continue
    updateDataRef = _lib.get("updateDataRef", "cdecl")
    updateDataRef.argtypes = [POINTER(OpenServerInstance), String, c_int]
    updateDataRef.restype = None
    break

# /home/user/Desktop/scada/iec61850_open_server/plugin_src/python/python_plugin.h: 16
for _lib in _libs.values():
    if not _lib.has("castOpenServerInstance", "cdecl"):
        continue
    castOpenServerInstance = _lib.get("castOpenServerInstance", "cdecl")
    castOpenServerInstance.argtypes = [POINTER(None)]
    castOpenServerInstance.restype = POINTER(OpenServerInstance)
    break

sOpenServerInstance = struct_sOpenServerInstance# ../../inc/open_server.h: 18

# No inserted files

# No prefix-stripping

