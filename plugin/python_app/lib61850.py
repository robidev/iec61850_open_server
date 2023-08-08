r"""Wrapper for hal_base.h

Generated with:
/home/user/.local/bin/ctypesgen -l /usr/local/lib/libiec61850.so -I /usr/local/include/libiec61850 /usr/local/include/libiec61850/hal_base.h /usr/local/include/libiec61850/hal_time.h /usr/local/include/libiec61850/hal_thread.h /usr/local/include/libiec61850/hal_filesystem.h /usr/local/include/libiec61850/hal_ethernet.h /usr/local/include/libiec61850/hal_socket.h /usr/local/include/libiec61850/tls_config.h /usr/local/include/libiec61850/libiec61850_common_api.h /usr/local/include/libiec61850/linked_list.h /usr/local/include/libiec61850/iec61850_client.h /usr/local/include/libiec61850/iec61850_common.h /usr/local/include/libiec61850/iec61850_server.h /usr/local/include/libiec61850/iec61850_model.h /usr/local/include/libiec61850/iec61850_cdc.h /usr/local/include/libiec61850/iec61850_dynamic_model.h /usr/local/include/libiec61850/iec61850_config_file_parser.h /usr/local/include/libiec61850/mms_value.h /usr/local/include/libiec61850/mms_common.h /usr/local/include/libiec61850/mms_types.h /usr/local/include/libiec61850/mms_type_spec.h /usr/local/include/libiec61850/mms_client_connection.h /usr/local/include/libiec61850/mms_server.h /usr/local/include/libiec61850/iso_connection_parameters.h /usr/local/include/libiec61850/goose_subscriber.h /usr/local/include/libiec61850/goose_receiver.h /usr/local/include/libiec61850/goose_publisher.h /usr/local/include/libiec61850/sv_subscriber.h /usr/local/include/libiec61850/sv_publisher.h /usr/local/include/libiec61850/logging_api.h -o lib61850.py

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
_libs["/usr/local/lib/libiec61850.so"] = load_library("/usr/local/lib/libiec61850.so")

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

nsSinceEpoch = uint64_t# /usr/local/include/libiec61850/hal_time.h: 35

msSinceEpoch = uint64_t# /usr/local/include/libiec61850/hal_time.h: 36

# /usr/local/include/libiec61850/hal_time.h: 47
if _libs["/usr/local/lib/libiec61850.so"].has("Hal_getTimeInMs", "cdecl"):
    Hal_getTimeInMs = _libs["/usr/local/lib/libiec61850.so"].get("Hal_getTimeInMs", "cdecl")
    Hal_getTimeInMs.argtypes = []
    Hal_getTimeInMs.restype = msSinceEpoch

# /usr/local/include/libiec61850/hal_time.h: 58
if _libs["/usr/local/lib/libiec61850.so"].has("Hal_getTimeInNs", "cdecl"):
    Hal_getTimeInNs = _libs["/usr/local/lib/libiec61850.so"].get("Hal_getTimeInNs", "cdecl")
    Hal_getTimeInNs.argtypes = []
    Hal_getTimeInNs.restype = nsSinceEpoch

# /usr/local/include/libiec61850/hal_time.h: 69
if _libs["/usr/local/lib/libiec61850.so"].has("Hal_setTimeInNs", "cdecl"):
    Hal_setTimeInNs = _libs["/usr/local/lib/libiec61850.so"].get("Hal_setTimeInNs", "cdecl")
    Hal_setTimeInNs.argtypes = [nsSinceEpoch]
    Hal_setTimeInNs.restype = c_bool

# /usr/local/include/libiec61850/hal_thread.h: 38
class struct_sThread(Structure):
    pass

Thread = POINTER(struct_sThread)# /usr/local/include/libiec61850/hal_thread.h: 38

Semaphore = POINTER(None)# /usr/local/include/libiec61850/hal_thread.h: 41

ThreadExecutionFunction = CFUNCTYPE(UNCHECKED(POINTER(c_ubyte)), POINTER(None))# /usr/local/include/libiec61850/hal_thread.h: 44

# /usr/local/include/libiec61850/hal_thread.h: 56
if _libs["/usr/local/lib/libiec61850.so"].has("Thread_create", "cdecl"):
    Thread_create = _libs["/usr/local/lib/libiec61850.so"].get("Thread_create", "cdecl")
    Thread_create.argtypes = [ThreadExecutionFunction, POINTER(None), c_bool]
    Thread_create.restype = Thread

# /usr/local/include/libiec61850/hal_thread.h: 67
if _libs["/usr/local/lib/libiec61850.so"].has("Thread_start", "cdecl"):
    Thread_start = _libs["/usr/local/lib/libiec61850.so"].get("Thread_start", "cdecl")
    Thread_start.argtypes = [Thread]
    Thread_start.restype = None

# /usr/local/include/libiec61850/hal_thread.h: 75
if _libs["/usr/local/lib/libiec61850.so"].has("Thread_destroy", "cdecl"):
    Thread_destroy = _libs["/usr/local/lib/libiec61850.so"].get("Thread_destroy", "cdecl")
    Thread_destroy.argtypes = [Thread]
    Thread_destroy.restype = None

# /usr/local/include/libiec61850/hal_thread.h: 81
if _libs["/usr/local/lib/libiec61850.so"].has("Thread_sleep", "cdecl"):
    Thread_sleep = _libs["/usr/local/lib/libiec61850.so"].get("Thread_sleep", "cdecl")
    Thread_sleep.argtypes = [c_int]
    Thread_sleep.restype = None

# /usr/local/include/libiec61850/hal_thread.h: 84
if _libs["/usr/local/lib/libiec61850.so"].has("Semaphore_create", "cdecl"):
    Semaphore_create = _libs["/usr/local/lib/libiec61850.so"].get("Semaphore_create", "cdecl")
    Semaphore_create.argtypes = [c_int]
    Semaphore_create.restype = Semaphore

# /usr/local/include/libiec61850/hal_thread.h: 88
if _libs["/usr/local/lib/libiec61850.so"].has("Semaphore_wait", "cdecl"):
    Semaphore_wait = _libs["/usr/local/lib/libiec61850.so"].get("Semaphore_wait", "cdecl")
    Semaphore_wait.argtypes = [Semaphore]
    Semaphore_wait.restype = None

# /usr/local/include/libiec61850/hal_thread.h: 91
if _libs["/usr/local/lib/libiec61850.so"].has("Semaphore_post", "cdecl"):
    Semaphore_post = _libs["/usr/local/lib/libiec61850.so"].get("Semaphore_post", "cdecl")
    Semaphore_post.argtypes = [Semaphore]
    Semaphore_post.restype = None

# /usr/local/include/libiec61850/hal_thread.h: 94
if _libs["/usr/local/lib/libiec61850.so"].has("Semaphore_destroy", "cdecl"):
    Semaphore_destroy = _libs["/usr/local/lib/libiec61850.so"].get("Semaphore_destroy", "cdecl")
    Semaphore_destroy.argtypes = [Semaphore]
    Semaphore_destroy.restype = None

FileHandle = POINTER(None)# /usr/local/include/libiec61850/hal_filesystem.h: 30

# /usr/local/include/libiec61850/hal_filesystem.h: 31
class struct_sDirectoryHandle(Structure):
    pass

DirectoryHandle = POINTER(struct_sDirectoryHandle)# /usr/local/include/libiec61850/hal_filesystem.h: 31

# /usr/local/include/libiec61850/hal_filesystem.h: 47
if _libs["/usr/local/lib/libiec61850.so"].has("FileSystem_openFile", "cdecl"):
    FileSystem_openFile = _libs["/usr/local/lib/libiec61850.so"].get("FileSystem_openFile", "cdecl")
    FileSystem_openFile.argtypes = [String, c_bool]
    FileSystem_openFile.restype = FileHandle

# /usr/local/include/libiec61850/hal_filesystem.h: 64
if _libs["/usr/local/lib/libiec61850.so"].has("FileSystem_readFile", "cdecl"):
    FileSystem_readFile = _libs["/usr/local/lib/libiec61850.so"].get("FileSystem_readFile", "cdecl")
    FileSystem_readFile.argtypes = [FileHandle, POINTER(uint8_t), c_int]
    FileSystem_readFile.restype = c_int

# /usr/local/include/libiec61850/hal_filesystem.h: 76
if _libs["/usr/local/lib/libiec61850.so"].has("FileSystem_writeFile", "cdecl"):
    FileSystem_writeFile = _libs["/usr/local/lib/libiec61850.so"].get("FileSystem_writeFile", "cdecl")
    FileSystem_writeFile.argtypes = [FileHandle, POINTER(uint8_t), c_int]
    FileSystem_writeFile.restype = c_int

# /usr/local/include/libiec61850/hal_filesystem.h: 84
if _libs["/usr/local/lib/libiec61850.so"].has("FileSystem_closeFile", "cdecl"):
    FileSystem_closeFile = _libs["/usr/local/lib/libiec61850.so"].get("FileSystem_closeFile", "cdecl")
    FileSystem_closeFile.argtypes = [FileHandle]
    FileSystem_closeFile.restype = None

# /usr/local/include/libiec61850/hal_filesystem.h: 100
if _libs["/usr/local/lib/libiec61850.so"].has("FileSystem_getFileInfo", "cdecl"):
    FileSystem_getFileInfo = _libs["/usr/local/lib/libiec61850.so"].get("FileSystem_getFileInfo", "cdecl")
    FileSystem_getFileInfo.argtypes = [String, POINTER(uint32_t), POINTER(uint64_t)]
    FileSystem_getFileInfo.restype = c_bool

# /usr/local/include/libiec61850/hal_filesystem.h: 110
if _libs["/usr/local/lib/libiec61850.so"].has("FileSystem_deleteFile", "cdecl"):
    FileSystem_deleteFile = _libs["/usr/local/lib/libiec61850.so"].get("FileSystem_deleteFile", "cdecl")
    FileSystem_deleteFile.argtypes = [String]
    FileSystem_deleteFile.restype = c_bool

# /usr/local/include/libiec61850/hal_filesystem.h: 121
if _libs["/usr/local/lib/libiec61850.so"].has("FileSystem_renameFile", "cdecl"):
    FileSystem_renameFile = _libs["/usr/local/lib/libiec61850.so"].get("FileSystem_renameFile", "cdecl")
    FileSystem_renameFile.argtypes = [String, String]
    FileSystem_renameFile.restype = c_bool

# /usr/local/include/libiec61850/hal_filesystem.h: 131
if _libs["/usr/local/lib/libiec61850.so"].has("FileSystem_openDirectory", "cdecl"):
    FileSystem_openDirectory = _libs["/usr/local/lib/libiec61850.so"].get("FileSystem_openDirectory", "cdecl")
    FileSystem_openDirectory.argtypes = [String]
    FileSystem_openDirectory.restype = DirectoryHandle

# /usr/local/include/libiec61850/hal_filesystem.h: 145
if _libs["/usr/local/lib/libiec61850.so"].has("FileSystem_readDirectory", "cdecl"):
    FileSystem_readDirectory = _libs["/usr/local/lib/libiec61850.so"].get("FileSystem_readDirectory", "cdecl")
    FileSystem_readDirectory.argtypes = [DirectoryHandle, POINTER(c_bool)]
    if sizeof(c_int) == sizeof(c_void_p):
        FileSystem_readDirectory.restype = ReturnString
    else:
        FileSystem_readDirectory.restype = String
        FileSystem_readDirectory.errcheck = ReturnString

# /usr/local/include/libiec61850/hal_filesystem.h: 155
if _libs["/usr/local/lib/libiec61850.so"].has("FileSystem_closeDirectory", "cdecl"):
    FileSystem_closeDirectory = _libs["/usr/local/lib/libiec61850.so"].get("FileSystem_closeDirectory", "cdecl")
    FileSystem_closeDirectory.argtypes = [DirectoryHandle]
    FileSystem_closeDirectory.restype = None

# /usr/local/include/libiec61850/hal_ethernet.h: 34
class struct_sEthernetSocket(Structure):
    pass

EthernetSocket = POINTER(struct_sEthernetSocket)# /usr/local/include/libiec61850/hal_ethernet.h: 34

# /usr/local/include/libiec61850/hal_ethernet.h: 37
class struct_sEthernetHandleSet(Structure):
    pass

EthernetHandleSet = POINTER(struct_sEthernetHandleSet)# /usr/local/include/libiec61850/hal_ethernet.h: 37

enum_anon_18 = c_int# /usr/local/include/libiec61850/hal_ethernet.h: 44

ETHERNET_SOCKET_MODE_PROMISC = 0# /usr/local/include/libiec61850/hal_ethernet.h: 44

ETHERNET_SOCKET_MODE_ALL_MULTICAST = (ETHERNET_SOCKET_MODE_PROMISC + 1)# /usr/local/include/libiec61850/hal_ethernet.h: 44

ETHERNET_SOCKET_MODE_MULTICAST = (ETHERNET_SOCKET_MODE_ALL_MULTICAST + 1)# /usr/local/include/libiec61850/hal_ethernet.h: 44

ETHERNET_SOCKET_MODE_HOST_ONLY = (ETHERNET_SOCKET_MODE_MULTICAST + 1)# /usr/local/include/libiec61850/hal_ethernet.h: 44

EthernetSocketMode = enum_anon_18# /usr/local/include/libiec61850/hal_ethernet.h: 44

# /usr/local/include/libiec61850/hal_ethernet.h: 52
if _libs["/usr/local/lib/libiec61850.so"].has("EthernetHandleSet_new", "cdecl"):
    EthernetHandleSet_new = _libs["/usr/local/lib/libiec61850.so"].get("EthernetHandleSet_new", "cdecl")
    EthernetHandleSet_new.argtypes = []
    EthernetHandleSet_new.restype = EthernetHandleSet

# /usr/local/include/libiec61850/hal_ethernet.h: 61
if _libs["/usr/local/lib/libiec61850.so"].has("EthernetHandleSet_addSocket", "cdecl"):
    EthernetHandleSet_addSocket = _libs["/usr/local/lib/libiec61850.so"].get("EthernetHandleSet_addSocket", "cdecl")
    EthernetHandleSet_addSocket.argtypes = [EthernetHandleSet, EthernetSocket]
    EthernetHandleSet_addSocket.restype = None

# /usr/local/include/libiec61850/hal_ethernet.h: 70
if _libs["/usr/local/lib/libiec61850.so"].has("EthernetHandleSet_removeSocket", "cdecl"):
    EthernetHandleSet_removeSocket = _libs["/usr/local/lib/libiec61850.so"].get("EthernetHandleSet_removeSocket", "cdecl")
    EthernetHandleSet_removeSocket.argtypes = [EthernetHandleSet, EthernetSocket]
    EthernetHandleSet_removeSocket.restype = None

# /usr/local/include/libiec61850/hal_ethernet.h: 85
if _libs["/usr/local/lib/libiec61850.so"].has("EthernetHandleSet_waitReady", "cdecl"):
    EthernetHandleSet_waitReady = _libs["/usr/local/lib/libiec61850.so"].get("EthernetHandleSet_waitReady", "cdecl")
    EthernetHandleSet_waitReady.argtypes = [EthernetHandleSet, c_uint]
    EthernetHandleSet_waitReady.restype = c_int

# /usr/local/include/libiec61850/hal_ethernet.h: 93
if _libs["/usr/local/lib/libiec61850.so"].has("EthernetHandleSet_destroy", "cdecl"):
    EthernetHandleSet_destroy = _libs["/usr/local/lib/libiec61850.so"].get("EthernetHandleSet_destroy", "cdecl")
    EthernetHandleSet_destroy.argtypes = [EthernetHandleSet]
    EthernetHandleSet_destroy.restype = None

# /usr/local/include/libiec61850/hal_ethernet.h: 104
if _libs["/usr/local/lib/libiec61850.so"].has("Ethernet_getInterfaceMACAddress", "cdecl"):
    Ethernet_getInterfaceMACAddress = _libs["/usr/local/lib/libiec61850.so"].get("Ethernet_getInterfaceMACAddress", "cdecl")
    Ethernet_getInterfaceMACAddress.argtypes = [String, POINTER(uint8_t)]
    Ethernet_getInterfaceMACAddress.restype = None

# /usr/local/include/libiec61850/hal_ethernet.h: 114
if _libs["/usr/local/lib/libiec61850.so"].has("Ethernet_createSocket", "cdecl"):
    Ethernet_createSocket = _libs["/usr/local/lib/libiec61850.so"].get("Ethernet_createSocket", "cdecl")
    Ethernet_createSocket.argtypes = [String, POINTER(uint8_t)]
    Ethernet_createSocket.restype = EthernetSocket

# /usr/local/include/libiec61850/hal_ethernet.h: 122
if _libs["/usr/local/lib/libiec61850.so"].has("Ethernet_destroySocket", "cdecl"):
    Ethernet_destroySocket = _libs["/usr/local/lib/libiec61850.so"].get("Ethernet_destroySocket", "cdecl")
    Ethernet_destroySocket.argtypes = [EthernetSocket]
    Ethernet_destroySocket.restype = None

# /usr/local/include/libiec61850/hal_ethernet.h: 125
if _libs["/usr/local/lib/libiec61850.so"].has("Ethernet_sendPacket", "cdecl"):
    Ethernet_sendPacket = _libs["/usr/local/lib/libiec61850.so"].get("Ethernet_sendPacket", "cdecl")
    Ethernet_sendPacket.argtypes = [EthernetSocket, POINTER(uint8_t), c_int]
    Ethernet_sendPacket.restype = None

# /usr/local/include/libiec61850/hal_ethernet.h: 137
if _libs["/usr/local/lib/libiec61850.so"].has("Ethernet_setMode", "cdecl"):
    Ethernet_setMode = _libs["/usr/local/lib/libiec61850.so"].get("Ethernet_setMode", "cdecl")
    Ethernet_setMode.argtypes = [EthernetSocket, EthernetSocketMode]
    Ethernet_setMode.restype = None

# /usr/local/include/libiec61850/hal_ethernet.h: 148
if _libs["/usr/local/lib/libiec61850.so"].has("Ethernet_addMulticastAddress", "cdecl"):
    Ethernet_addMulticastAddress = _libs["/usr/local/lib/libiec61850.so"].get("Ethernet_addMulticastAddress", "cdecl")
    Ethernet_addMulticastAddress.argtypes = [EthernetSocket, POINTER(uint8_t)]
    Ethernet_addMulticastAddress.restype = None

# /usr/local/include/libiec61850/hal_ethernet.h: 160
if _libs["/usr/local/lib/libiec61850.so"].has("Ethernet_setProtocolFilter", "cdecl"):
    Ethernet_setProtocolFilter = _libs["/usr/local/lib/libiec61850.so"].get("Ethernet_setProtocolFilter", "cdecl")
    Ethernet_setProtocolFilter.argtypes = [EthernetSocket, uint16_t]
    Ethernet_setProtocolFilter.restype = None

# /usr/local/include/libiec61850/hal_ethernet.h: 172
if _libs["/usr/local/lib/libiec61850.so"].has("Ethernet_receivePacket", "cdecl"):
    Ethernet_receivePacket = _libs["/usr/local/lib/libiec61850.so"].get("Ethernet_receivePacket", "cdecl")
    Ethernet_receivePacket.argtypes = [EthernetSocket, POINTER(uint8_t), c_int]
    Ethernet_receivePacket.restype = c_int

# /usr/local/include/libiec61850/hal_ethernet.h: 180
if _libs["/usr/local/lib/libiec61850.so"].has("Ethernet_isSupported", "cdecl"):
    Ethernet_isSupported = _libs["/usr/local/lib/libiec61850.so"].get("Ethernet_isSupported", "cdecl")
    Ethernet_isSupported.argtypes = []
    Ethernet_isSupported.restype = c_bool

# /usr/local/include/libiec61850/hal_socket.h: 44
class struct_sServerSocket(Structure):
    pass

ServerSocket = POINTER(struct_sServerSocket)# /usr/local/include/libiec61850/hal_socket.h: 44

# /usr/local/include/libiec61850/hal_socket.h: 46
class struct_sUdpSocket(Structure):
    pass

UdpSocket = POINTER(struct_sUdpSocket)# /usr/local/include/libiec61850/hal_socket.h: 46

# /usr/local/include/libiec61850/hal_socket.h: 49
class struct_sSocket(Structure):
    pass

Socket = POINTER(struct_sSocket)# /usr/local/include/libiec61850/hal_socket.h: 49

# /usr/local/include/libiec61850/hal_socket.h: 52
class struct_sHandleSet(Structure):
    pass

HandleSet = POINTER(struct_sHandleSet)# /usr/local/include/libiec61850/hal_socket.h: 52

enum_anon_19 = c_int# /usr/local/include/libiec61850/hal_socket.h: 60

SOCKET_STATE_CONNECTING = 0# /usr/local/include/libiec61850/hal_socket.h: 60

SOCKET_STATE_FAILED = 1# /usr/local/include/libiec61850/hal_socket.h: 60

SOCKET_STATE_CONNECTED = 2# /usr/local/include/libiec61850/hal_socket.h: 60

SocketState = enum_anon_19# /usr/local/include/libiec61850/hal_socket.h: 60

# /usr/local/include/libiec61850/hal_socket.h: 69
if _libs["/usr/local/lib/libiec61850.so"].has("Handleset_new", "cdecl"):
    Handleset_new = _libs["/usr/local/lib/libiec61850.so"].get("Handleset_new", "cdecl")
    Handleset_new.argtypes = []
    Handleset_new.restype = HandleSet

# /usr/local/include/libiec61850/hal_socket.h: 75
if _libs["/usr/local/lib/libiec61850.so"].has("Handleset_reset", "cdecl"):
    Handleset_reset = _libs["/usr/local/lib/libiec61850.so"].get("Handleset_reset", "cdecl")
    Handleset_reset.argtypes = [HandleSet]
    Handleset_reset.restype = None

# /usr/local/include/libiec61850/hal_socket.h: 84
if _libs["/usr/local/lib/libiec61850.so"].has("Handleset_addSocket", "cdecl"):
    Handleset_addSocket = _libs["/usr/local/lib/libiec61850.so"].get("Handleset_addSocket", "cdecl")
    Handleset_addSocket.argtypes = [HandleSet, Socket]
    Handleset_addSocket.restype = None

# /usr/local/include/libiec61850/hal_socket.h: 90
if _libs["/usr/local/lib/libiec61850.so"].has("Handleset_removeSocket", "cdecl"):
    Handleset_removeSocket = _libs["/usr/local/lib/libiec61850.so"].get("Handleset_removeSocket", "cdecl")
    Handleset_removeSocket.argtypes = [HandleSet, Socket]
    Handleset_removeSocket.restype = None

# /usr/local/include/libiec61850/hal_socket.h: 108
if _libs["/usr/local/lib/libiec61850.so"].has("Handleset_waitReady", "cdecl"):
    Handleset_waitReady = _libs["/usr/local/lib/libiec61850.so"].get("Handleset_waitReady", "cdecl")
    Handleset_waitReady.argtypes = [HandleSet, c_uint]
    Handleset_waitReady.restype = c_int

# /usr/local/include/libiec61850/hal_socket.h: 116
if _libs["/usr/local/lib/libiec61850.so"].has("Handleset_destroy", "cdecl"):
    Handleset_destroy = _libs["/usr/local/lib/libiec61850.so"].get("Handleset_destroy", "cdecl")
    Handleset_destroy.argtypes = [HandleSet]
    Handleset_destroy.restype = None

# /usr/local/include/libiec61850/hal_socket.h: 129
if _libs["/usr/local/lib/libiec61850.so"].has("TcpServerSocket_create", "cdecl"):
    TcpServerSocket_create = _libs["/usr/local/lib/libiec61850.so"].get("TcpServerSocket_create", "cdecl")
    TcpServerSocket_create.argtypes = [String, c_int]
    TcpServerSocket_create.restype = ServerSocket

# /usr/local/include/libiec61850/hal_socket.h: 132
if _libs["/usr/local/lib/libiec61850.so"].has("UdpSocket_create", "cdecl"):
    UdpSocket_create = _libs["/usr/local/lib/libiec61850.so"].get("UdpSocket_create", "cdecl")
    UdpSocket_create.argtypes = []
    UdpSocket_create.restype = UdpSocket

# /usr/local/include/libiec61850/hal_socket.h: 135
if _libs["/usr/local/lib/libiec61850.so"].has("UdpSocket_bind", "cdecl"):
    UdpSocket_bind = _libs["/usr/local/lib/libiec61850.so"].get("UdpSocket_bind", "cdecl")
    UdpSocket_bind.argtypes = [UdpSocket, String, c_int]
    UdpSocket_bind.restype = c_bool

# /usr/local/include/libiec61850/hal_socket.h: 138
if _libs["/usr/local/lib/libiec61850.so"].has("UdpSocket_sendTo", "cdecl"):
    UdpSocket_sendTo = _libs["/usr/local/lib/libiec61850.so"].get("UdpSocket_sendTo", "cdecl")
    UdpSocket_sendTo.argtypes = [UdpSocket, String, c_int, POINTER(uint8_t), c_int]
    UdpSocket_sendTo.restype = c_bool

# /usr/local/include/libiec61850/hal_socket.h: 152
if _libs["/usr/local/lib/libiec61850.so"].has("UdpSocket_receiveFrom", "cdecl"):
    UdpSocket_receiveFrom = _libs["/usr/local/lib/libiec61850.so"].get("UdpSocket_receiveFrom", "cdecl")
    UdpSocket_receiveFrom.argtypes = [UdpSocket, String, c_int, POINTER(uint8_t), c_int]
    UdpSocket_receiveFrom.restype = c_int

# /usr/local/include/libiec61850/hal_socket.h: 156
if _libs["/usr/local/lib/libiec61850.so"].has("ServerSocket_listen", "cdecl"):
    ServerSocket_listen = _libs["/usr/local/lib/libiec61850.so"].get("ServerSocket_listen", "cdecl")
    ServerSocket_listen.argtypes = [ServerSocket]
    ServerSocket_listen.restype = None

# /usr/local/include/libiec61850/hal_socket.h: 173
if _libs["/usr/local/lib/libiec61850.so"].has("ServerSocket_accept", "cdecl"):
    ServerSocket_accept = _libs["/usr/local/lib/libiec61850.so"].get("ServerSocket_accept", "cdecl")
    ServerSocket_accept.argtypes = [ServerSocket]
    ServerSocket_accept.restype = Socket

# /usr/local/include/libiec61850/hal_socket.h: 186
if _libs["/usr/local/lib/libiec61850.so"].has("Socket_activateTcpKeepAlive", "cdecl"):
    Socket_activateTcpKeepAlive = _libs["/usr/local/lib/libiec61850.so"].get("Socket_activateTcpKeepAlive", "cdecl")
    Socket_activateTcpKeepAlive.argtypes = [Socket, c_int, c_int, c_int]
    Socket_activateTcpKeepAlive.restype = None

# /usr/local/include/libiec61850/hal_socket.h: 198
if _libs["/usr/local/lib/libiec61850.so"].has("ServerSocket_setBacklog", "cdecl"):
    ServerSocket_setBacklog = _libs["/usr/local/lib/libiec61850.so"].get("ServerSocket_setBacklog", "cdecl")
    ServerSocket_setBacklog.argtypes = [ServerSocket, c_int]
    ServerSocket_setBacklog.restype = None

# /usr/local/include/libiec61850/hal_socket.h: 210
if _libs["/usr/local/lib/libiec61850.so"].has("ServerSocket_destroy", "cdecl"):
    ServerSocket_destroy = _libs["/usr/local/lib/libiec61850.so"].get("ServerSocket_destroy", "cdecl")
    ServerSocket_destroy.argtypes = [ServerSocket]
    ServerSocket_destroy.restype = None

# /usr/local/include/libiec61850/hal_socket.h: 220
if _libs["/usr/local/lib/libiec61850.so"].has("TcpSocket_create", "cdecl"):
    TcpSocket_create = _libs["/usr/local/lib/libiec61850.so"].get("TcpSocket_create", "cdecl")
    TcpSocket_create.argtypes = []
    TcpSocket_create.restype = Socket

# /usr/local/include/libiec61850/hal_socket.h: 229
if _libs["/usr/local/lib/libiec61850.so"].has("Socket_setConnectTimeout", "cdecl"):
    Socket_setConnectTimeout = _libs["/usr/local/lib/libiec61850.so"].get("Socket_setConnectTimeout", "cdecl")
    Socket_setConnectTimeout.argtypes = [Socket, uint32_t]
    Socket_setConnectTimeout.restype = None

# /usr/local/include/libiec61850/hal_socket.h: 243
if _libs["/usr/local/lib/libiec61850.so"].has("Socket_bind", "cdecl"):
    Socket_bind = _libs["/usr/local/lib/libiec61850.so"].get("Socket_bind", "cdecl")
    Socket_bind.argtypes = [Socket, String, c_int]
    Socket_bind.restype = c_bool

# /usr/local/include/libiec61850/hal_socket.h: 264
if _libs["/usr/local/lib/libiec61850.so"].has("Socket_connect", "cdecl"):
    Socket_connect = _libs["/usr/local/lib/libiec61850.so"].get("Socket_connect", "cdecl")
    Socket_connect.argtypes = [Socket, String, c_int]
    Socket_connect.restype = c_bool

# /usr/local/include/libiec61850/hal_socket.h: 267
if _libs["/usr/local/lib/libiec61850.so"].has("Socket_connectAsync", "cdecl"):
    Socket_connectAsync = _libs["/usr/local/lib/libiec61850.so"].get("Socket_connectAsync", "cdecl")
    Socket_connectAsync.argtypes = [Socket, String, c_int]
    Socket_connectAsync.restype = c_bool

# /usr/local/include/libiec61850/hal_socket.h: 270
if _libs["/usr/local/lib/libiec61850.so"].has("Socket_checkAsyncConnectState", "cdecl"):
    Socket_checkAsyncConnectState = _libs["/usr/local/lib/libiec61850.so"].get("Socket_checkAsyncConnectState", "cdecl")
    Socket_checkAsyncConnectState.argtypes = [Socket]
    Socket_checkAsyncConnectState.restype = SocketState

# /usr/local/include/libiec61850/hal_socket.h: 289
if _libs["/usr/local/lib/libiec61850.so"].has("Socket_read", "cdecl"):
    Socket_read = _libs["/usr/local/lib/libiec61850.so"].get("Socket_read", "cdecl")
    Socket_read.argtypes = [Socket, POINTER(uint8_t), c_int]
    Socket_read.restype = c_int

# /usr/local/include/libiec61850/hal_socket.h: 301
if _libs["/usr/local/lib/libiec61850.so"].has("Socket_write", "cdecl"):
    Socket_write = _libs["/usr/local/lib/libiec61850.so"].get("Socket_write", "cdecl")
    Socket_write.argtypes = [Socket, POINTER(uint8_t), c_int]
    Socket_write.restype = c_int

# /usr/local/include/libiec61850/hal_socket.h: 303
if _libs["/usr/local/lib/libiec61850.so"].has("Socket_getLocalAddress", "cdecl"):
    Socket_getLocalAddress = _libs["/usr/local/lib/libiec61850.so"].get("Socket_getLocalAddress", "cdecl")
    Socket_getLocalAddress.argtypes = [Socket]
    if sizeof(c_int) == sizeof(c_void_p):
        Socket_getLocalAddress.restype = ReturnString
    else:
        Socket_getLocalAddress.restype = String
        Socket_getLocalAddress.errcheck = ReturnString

# /usr/local/include/libiec61850/hal_socket.h: 317
if _libs["/usr/local/lib/libiec61850.so"].has("Socket_getPeerAddress", "cdecl"):
    Socket_getPeerAddress = _libs["/usr/local/lib/libiec61850.so"].get("Socket_getPeerAddress", "cdecl")
    Socket_getPeerAddress.argtypes = [Socket]
    if sizeof(c_int) == sizeof(c_void_p):
        Socket_getPeerAddress.restype = ReturnString
    else:
        Socket_getPeerAddress.restype = String
        Socket_getPeerAddress.errcheck = ReturnString

# /usr/local/include/libiec61850/hal_socket.h: 334
if _libs["/usr/local/lib/libiec61850.so"].has("Socket_getPeerAddressStatic", "cdecl"):
    Socket_getPeerAddressStatic = _libs["/usr/local/lib/libiec61850.so"].get("Socket_getPeerAddressStatic", "cdecl")
    Socket_getPeerAddressStatic.argtypes = [Socket, String]
    if sizeof(c_int) == sizeof(c_void_p):
        Socket_getPeerAddressStatic.restype = ReturnString
    else:
        Socket_getPeerAddressStatic.restype = String
        Socket_getPeerAddressStatic.errcheck = ReturnString

# /usr/local/include/libiec61850/hal_socket.h: 348
if _libs["/usr/local/lib/libiec61850.so"].has("Socket_destroy", "cdecl"):
    Socket_destroy = _libs["/usr/local/lib/libiec61850.so"].get("Socket_destroy", "cdecl")
    Socket_destroy.argtypes = [Socket]
    Socket_destroy.restype = None

# /usr/local/include/libiec61850/tls_config.h: 37
class struct_sTLSConfiguration(Structure):
    pass

TLSConfiguration = POINTER(struct_sTLSConfiguration)# /usr/local/include/libiec61850/tls_config.h: 37

# /usr/local/include/libiec61850/tls_config.h: 47
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_create", "cdecl"):
        continue
    TLSConfiguration_create = _lib.get("TLSConfiguration_create", "cdecl")
    TLSConfiguration_create.argtypes = []
    TLSConfiguration_create.restype = TLSConfiguration
    break

# /usr/local/include/libiec61850/tls_config.h: 51
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_setClientMode", "cdecl"):
        continue
    TLSConfiguration_setClientMode = _lib.get("TLSConfiguration_setClientMode", "cdecl")
    TLSConfiguration_setClientMode.argtypes = [TLSConfiguration]
    TLSConfiguration_setClientMode.restype = None
    break

enum_anon_20 = c_int# /usr/local/include/libiec61850/tls_config.h: 60

TLS_VERSION_NOT_SELECTED = 0# /usr/local/include/libiec61850/tls_config.h: 60

TLS_VERSION_SSL_3_0 = 3# /usr/local/include/libiec61850/tls_config.h: 60

TLS_VERSION_TLS_1_0 = 4# /usr/local/include/libiec61850/tls_config.h: 60

TLS_VERSION_TLS_1_1 = 5# /usr/local/include/libiec61850/tls_config.h: 60

TLS_VERSION_TLS_1_2 = 6# /usr/local/include/libiec61850/tls_config.h: 60

TLS_VERSION_TLS_1_3 = 7# /usr/local/include/libiec61850/tls_config.h: 60

TLSConfigVersion = enum_anon_20# /usr/local/include/libiec61850/tls_config.h: 60

# /usr/local/include/libiec61850/tls_config.h: 69
for _lib in _libs.values():
    if not _lib.has("TLSConfigVersion_toString", "cdecl"):
        continue
    TLSConfigVersion_toString = _lib.get("TLSConfigVersion_toString", "cdecl")
    TLSConfigVersion_toString.argtypes = [TLSConfigVersion]
    TLSConfigVersion_toString.restype = c_char_p
    break

enum_anon_21 = c_int# /usr/local/include/libiec61850/tls_config.h: 76

TLS_SEC_EVT_INFO = 0# /usr/local/include/libiec61850/tls_config.h: 76

TLS_SEC_EVT_WARNING = 1# /usr/local/include/libiec61850/tls_config.h: 76

TLS_SEC_EVT_INCIDENT = 2# /usr/local/include/libiec61850/tls_config.h: 76

TLSEventLevel = enum_anon_21# /usr/local/include/libiec61850/tls_config.h: 76

# /usr/local/include/libiec61850/tls_config.h: 94
class struct_sTLSConnection(Structure):
    pass

TLSConnection = POINTER(struct_sTLSConnection)# /usr/local/include/libiec61850/tls_config.h: 94

# /usr/local/include/libiec61850/tls_config.h: 104
for _lib in _libs.values():
    if not _lib.has("TLSConnection_getPeerAddress", "cdecl"):
        continue
    TLSConnection_getPeerAddress = _lib.get("TLSConnection_getPeerAddress", "cdecl")
    TLSConnection_getPeerAddress.argtypes = [TLSConnection, String]
    if sizeof(c_int) == sizeof(c_void_p):
        TLSConnection_getPeerAddress.restype = ReturnString
    else:
        TLSConnection_getPeerAddress.restype = String
        TLSConnection_getPeerAddress.errcheck = ReturnString
    break

# /usr/local/include/libiec61850/tls_config.h: 115
for _lib in _libs.values():
    if not _lib.has("TLSConnection_getPeerCertificate", "cdecl"):
        continue
    TLSConnection_getPeerCertificate = _lib.get("TLSConnection_getPeerCertificate", "cdecl")
    TLSConnection_getPeerCertificate.argtypes = [TLSConnection, POINTER(c_int)]
    TLSConnection_getPeerCertificate.restype = POINTER(uint8_t)
    break

# /usr/local/include/libiec61850/tls_config.h: 126
for _lib in _libs.values():
    if not _lib.has("TLSConnection_getTLSVersion", "cdecl"):
        continue
    TLSConnection_getTLSVersion = _lib.get("TLSConnection_getTLSVersion", "cdecl")
    TLSConnection_getTLSVersion.argtypes = [TLSConnection]
    TLSConnection_getTLSVersion.restype = TLSConfigVersion
    break

TLSConfiguration_EventHandler = CFUNCTYPE(UNCHECKED(None), POINTER(None), TLSEventLevel, c_int, String, TLSConnection)# /usr/local/include/libiec61850/tls_config.h: 128

# /usr/local/include/libiec61850/tls_config.h: 137
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_setEventHandler", "cdecl"):
        continue
    TLSConfiguration_setEventHandler = _lib.get("TLSConfiguration_setEventHandler", "cdecl")
    TLSConfiguration_setEventHandler.argtypes = [TLSConfiguration, TLSConfiguration_EventHandler, POINTER(None)]
    TLSConfiguration_setEventHandler.restype = None
    break

# /usr/local/include/libiec61850/tls_config.h: 148
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_enableSessionResumption", "cdecl"):
        continue
    TLSConfiguration_enableSessionResumption = _lib.get("TLSConfiguration_enableSessionResumption", "cdecl")
    TLSConfiguration_enableSessionResumption.argtypes = [TLSConfiguration, c_bool]
    TLSConfiguration_enableSessionResumption.restype = None
    break

# /usr/local/include/libiec61850/tls_config.h: 156
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_setSessionResumptionInterval", "cdecl"):
        continue
    TLSConfiguration_setSessionResumptionInterval = _lib.get("TLSConfiguration_setSessionResumptionInterval", "cdecl")
    TLSConfiguration_setSessionResumptionInterval.argtypes = [TLSConfiguration, c_int]
    TLSConfiguration_setSessionResumptionInterval.restype = None
    break

# /usr/local/include/libiec61850/tls_config.h: 164
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_setChainValidation", "cdecl"):
        continue
    TLSConfiguration_setChainValidation = _lib.get("TLSConfiguration_setChainValidation", "cdecl")
    TLSConfiguration_setChainValidation.argtypes = [TLSConfiguration, c_bool]
    TLSConfiguration_setChainValidation.restype = None
    break

# /usr/local/include/libiec61850/tls_config.h: 175
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_setAllowOnlyKnownCertificates", "cdecl"):
        continue
    TLSConfiguration_setAllowOnlyKnownCertificates = _lib.get("TLSConfiguration_setAllowOnlyKnownCertificates", "cdecl")
    TLSConfiguration_setAllowOnlyKnownCertificates.argtypes = [TLSConfiguration, c_bool]
    TLSConfiguration_setAllowOnlyKnownCertificates.restype = None
    break

# /usr/local/include/libiec61850/tls_config.h: 186
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_setOwnCertificate", "cdecl"):
        continue
    TLSConfiguration_setOwnCertificate = _lib.get("TLSConfiguration_setOwnCertificate", "cdecl")
    TLSConfiguration_setOwnCertificate.argtypes = [TLSConfiguration, POINTER(uint8_t), c_int]
    TLSConfiguration_setOwnCertificate.restype = c_bool
    break

# /usr/local/include/libiec61850/tls_config.h: 196
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_setOwnCertificateFromFile", "cdecl"):
        continue
    TLSConfiguration_setOwnCertificateFromFile = _lib.get("TLSConfiguration_setOwnCertificateFromFile", "cdecl")
    TLSConfiguration_setOwnCertificateFromFile.argtypes = [TLSConfiguration, String]
    TLSConfiguration_setOwnCertificateFromFile.restype = c_bool
    break

# /usr/local/include/libiec61850/tls_config.h: 208
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_setOwnKey", "cdecl"):
        continue
    TLSConfiguration_setOwnKey = _lib.get("TLSConfiguration_setOwnKey", "cdecl")
    TLSConfiguration_setOwnKey.argtypes = [TLSConfiguration, POINTER(uint8_t), c_int, String]
    TLSConfiguration_setOwnKey.restype = c_bool
    break

# /usr/local/include/libiec61850/tls_config.h: 219
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_setOwnKeyFromFile", "cdecl"):
        continue
    TLSConfiguration_setOwnKeyFromFile = _lib.get("TLSConfiguration_setOwnKeyFromFile", "cdecl")
    TLSConfiguration_setOwnKeyFromFile.argtypes = [TLSConfiguration, String, String]
    TLSConfiguration_setOwnKeyFromFile.restype = c_bool
    break

# /usr/local/include/libiec61850/tls_config.h: 229
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_addAllowedCertificate", "cdecl"):
        continue
    TLSConfiguration_addAllowedCertificate = _lib.get("TLSConfiguration_addAllowedCertificate", "cdecl")
    TLSConfiguration_addAllowedCertificate.argtypes = [TLSConfiguration, POINTER(uint8_t), c_int]
    TLSConfiguration_addAllowedCertificate.restype = c_bool
    break

# /usr/local/include/libiec61850/tls_config.h: 238
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_addAllowedCertificateFromFile", "cdecl"):
        continue
    TLSConfiguration_addAllowedCertificateFromFile = _lib.get("TLSConfiguration_addAllowedCertificateFromFile", "cdecl")
    TLSConfiguration_addAllowedCertificateFromFile.argtypes = [TLSConfiguration, String]
    TLSConfiguration_addAllowedCertificateFromFile.restype = c_bool
    break

# /usr/local/include/libiec61850/tls_config.h: 248
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_addCACertificate", "cdecl"):
        continue
    TLSConfiguration_addCACertificate = _lib.get("TLSConfiguration_addCACertificate", "cdecl")
    TLSConfiguration_addCACertificate.argtypes = [TLSConfiguration, POINTER(uint8_t), c_int]
    TLSConfiguration_addCACertificate.restype = c_bool
    break

# /usr/local/include/libiec61850/tls_config.h: 257
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_addCACertificateFromFile", "cdecl"):
        continue
    TLSConfiguration_addCACertificateFromFile = _lib.get("TLSConfiguration_addCACertificateFromFile", "cdecl")
    TLSConfiguration_addCACertificateFromFile.argtypes = [TLSConfiguration, String]
    TLSConfiguration_addCACertificateFromFile.restype = c_bool
    break

# /usr/local/include/libiec61850/tls_config.h: 267
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_setRenegotiationTime", "cdecl"):
        continue
    TLSConfiguration_setRenegotiationTime = _lib.get("TLSConfiguration_setRenegotiationTime", "cdecl")
    TLSConfiguration_setRenegotiationTime.argtypes = [TLSConfiguration, c_int]
    TLSConfiguration_setRenegotiationTime.restype = None
    break

# /usr/local/include/libiec61850/tls_config.h: 273
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_setMinTlsVersion", "cdecl"):
        continue
    TLSConfiguration_setMinTlsVersion = _lib.get("TLSConfiguration_setMinTlsVersion", "cdecl")
    TLSConfiguration_setMinTlsVersion.argtypes = [TLSConfiguration, TLSConfigVersion]
    TLSConfiguration_setMinTlsVersion.restype = None
    break

# /usr/local/include/libiec61850/tls_config.h: 279
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_setMaxTlsVersion", "cdecl"):
        continue
    TLSConfiguration_setMaxTlsVersion = _lib.get("TLSConfiguration_setMaxTlsVersion", "cdecl")
    TLSConfiguration_setMaxTlsVersion.argtypes = [TLSConfiguration, TLSConfigVersion]
    TLSConfiguration_setMaxTlsVersion.restype = None
    break

# /usr/local/include/libiec61850/tls_config.h: 289
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_addCRL", "cdecl"):
        continue
    TLSConfiguration_addCRL = _lib.get("TLSConfiguration_addCRL", "cdecl")
    TLSConfiguration_addCRL.argtypes = [TLSConfiguration, POINTER(uint8_t), c_int]
    TLSConfiguration_addCRL.restype = c_bool
    break

# /usr/local/include/libiec61850/tls_config.h: 298
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_addCRLFromFile", "cdecl"):
        continue
    TLSConfiguration_addCRLFromFile = _lib.get("TLSConfiguration_addCRLFromFile", "cdecl")
    TLSConfiguration_addCRLFromFile.argtypes = [TLSConfiguration, String]
    TLSConfiguration_addCRLFromFile.restype = c_bool
    break

# /usr/local/include/libiec61850/tls_config.h: 304
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_resetCRL", "cdecl"):
        continue
    TLSConfiguration_resetCRL = _lib.get("TLSConfiguration_resetCRL", "cdecl")
    TLSConfiguration_resetCRL.argtypes = [TLSConfiguration]
    TLSConfiguration_resetCRL.restype = None
    break

# /usr/local/include/libiec61850/tls_config.h: 312
for _lib in _libs.values():
    if not _lib.has("TLSConfiguration_destroy", "cdecl"):
        continue
    TLSConfiguration_destroy = _lib.get("TLSConfiguration_destroy", "cdecl")
    TLSConfiguration_destroy.argtypes = [TLSConfiguration]
    TLSConfiguration_destroy.restype = None
    break

enum_anon_22 = c_int# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_NONE = 0# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_CONNECTION_REJECTED = 1# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_CONNECTION_LOST = 2# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_SERVICE_TIMEOUT = 3# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_PARSING_RESPONSE = 4# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_HARDWARE_FAULT = 5# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_CONCLUDE_REJECTED = 6# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_INVALID_ARGUMENTS = 7# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_OUTSTANDING_CALL_LIMIT = 8# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_OTHER = 9# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_VMDSTATE_OTHER = 10# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_APPLICATION_REFERENCE_OTHER = 20# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_DEFINITION_OTHER = 30# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_DEFINITION_INVALID_ADDRESS = 31# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_DEFINITION_TYPE_UNSUPPORTED = 32# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_DEFINITION_TYPE_INCONSISTENT = 33# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_DEFINITION_OBJECT_UNDEFINED = 34# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_DEFINITION_OBJECT_EXISTS = 35# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_DEFINITION_OBJECT_ATTRIBUTE_INCONSISTENT = 36# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_RESOURCE_OTHER = 40# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_RESOURCE_CAPABILITY_UNAVAILABLE = 41# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_SERVICE_OTHER = 50# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_SERVICE_OBJECT_CONSTRAINT_CONFLICT = 55# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_SERVICE_PREEMPT_OTHER = 60# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_TIME_RESOLUTION_OTHER = 70# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_ACCESS_OTHER = 80# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_ACCESS_OBJECT_NON_EXISTENT = 81# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_ACCESS_OBJECT_ACCESS_UNSUPPORTED = 82# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_ACCESS_OBJECT_ACCESS_DENIED = 83# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_ACCESS_OBJECT_INVALIDATED = 84# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_ACCESS_OBJECT_VALUE_INVALID = 85# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_ACCESS_TEMPORARILY_UNAVAILABLE = 86# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_FILE_OTHER = 90# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_FILE_FILENAME_AMBIGUOUS = 91# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_FILE_FILE_BUSY = 92# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_FILE_FILENAME_SYNTAX_ERROR = 93# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_FILE_CONTENT_TYPE_INVALID = 94# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_FILE_POSITION_INVALID = 95# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_FILE_FILE_ACCESS_DENIED = 96# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_FILE_FILE_NON_EXISTENT = 97# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_FILE_DUPLICATE_FILENAME = 98# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_FILE_INSUFFICIENT_SPACE_IN_FILESTORE = 99# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_REJECT_OTHER = 100# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_REJECT_UNKNOWN_PDU_TYPE = 101# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_REJECT_INVALID_PDU = 102# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_REJECT_UNRECOGNIZED_SERVICE = 103# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_REJECT_UNRECOGNIZED_MODIFIER = 104# /usr/local/include/libiec61850/mms_common.h: 103

MMS_ERROR_REJECT_REQUEST_INVALID_ARGUMENT = 105# /usr/local/include/libiec61850/mms_common.h: 103

MmsError = enum_anon_22# /usr/local/include/libiec61850/mms_common.h: 103

enum_anon_23 = c_int# /usr/local/include/libiec61850/mms_common.h: 135

MMS_ARRAY = 0# /usr/local/include/libiec61850/mms_common.h: 135

MMS_STRUCTURE = 1# /usr/local/include/libiec61850/mms_common.h: 135

MMS_BOOLEAN = 2# /usr/local/include/libiec61850/mms_common.h: 135

MMS_BIT_STRING = 3# /usr/local/include/libiec61850/mms_common.h: 135

MMS_INTEGER = 4# /usr/local/include/libiec61850/mms_common.h: 135

MMS_UNSIGNED = 5# /usr/local/include/libiec61850/mms_common.h: 135

MMS_FLOAT = 6# /usr/local/include/libiec61850/mms_common.h: 135

MMS_OCTET_STRING = 7# /usr/local/include/libiec61850/mms_common.h: 135

MMS_VISIBLE_STRING = 8# /usr/local/include/libiec61850/mms_common.h: 135

MMS_GENERALIZED_TIME = 9# /usr/local/include/libiec61850/mms_common.h: 135

MMS_BINARY_TIME = 10# /usr/local/include/libiec61850/mms_common.h: 135

MMS_BCD = 11# /usr/local/include/libiec61850/mms_common.h: 135

MMS_OBJ_ID = 12# /usr/local/include/libiec61850/mms_common.h: 135

MMS_STRING = 13# /usr/local/include/libiec61850/mms_common.h: 135

MMS_UTC_TIME = 14# /usr/local/include/libiec61850/mms_common.h: 135

MMS_DATA_ACCESS_ERROR = 15# /usr/local/include/libiec61850/mms_common.h: 135

MmsType = enum_anon_23# /usr/local/include/libiec61850/mms_common.h: 135

# /usr/local/include/libiec61850/mms_common.h: 137
class struct_sMmsDomain(Structure):
    pass

MmsDomain = struct_sMmsDomain# /usr/local/include/libiec61850/mms_common.h: 137

# /usr/local/include/libiec61850/mms_common.h: 145
class struct_sMmsAccessSpecifier(Structure):
    pass

struct_sMmsAccessSpecifier.__slots__ = [
    'domain',
    'variableName',
    'arrayIndex',
    'componentName',
]
struct_sMmsAccessSpecifier._fields_ = [
    ('domain', POINTER(MmsDomain)),
    ('variableName', String),
    ('arrayIndex', c_int),
    ('componentName', String),
]

MmsAccessSpecifier = struct_sMmsAccessSpecifier# /usr/local/include/libiec61850/mms_common.h: 145

# /usr/local/include/libiec61850/mms_common.h: 153
class struct_anon_24(Structure):
    pass

struct_anon_24.__slots__ = [
    'domainId',
    'itemId',
    'arrayIndex',
    'componentName',
]
struct_anon_24._fields_ = [
    ('domainId', String),
    ('itemId', String),
    ('arrayIndex', c_int32),
    ('componentName', String),
]

MmsVariableAccessSpecification = struct_anon_24# /usr/local/include/libiec61850/mms_common.h: 153

# /usr/local/include/libiec61850/mms_common.h: 155
class struct_sMmsNamedVariableList(Structure):
    pass

MmsNamedVariableList = POINTER(struct_sMmsNamedVariableList)# /usr/local/include/libiec61850/mms_common.h: 155

MmsNamedVariableListEntry = POINTER(struct_sMmsAccessSpecifier)# /usr/local/include/libiec61850/mms_common.h: 156

# /usr/local/include/libiec61850/mms_common.h: 164
class struct_anon_25(Structure):
    pass

struct_anon_25.__slots__ = [
    'arc',
    'arcCount',
]
struct_anon_25._fields_ = [
    ('arc', uint16_t * int(10)),
    ('arcCount', c_int),
]

ItuObjectIdentifier = struct_anon_25# /usr/local/include/libiec61850/mms_common.h: 164

# /usr/local/include/libiec61850/mms_common.h: 172
class struct_anon_26(Structure):
    pass

struct_anon_26.__slots__ = [
    'apTitle',
    'aeQualifier',
]
struct_anon_26._fields_ = [
    ('apTitle', ItuObjectIdentifier),
    ('aeQualifier', c_int),
]

IsoApplicationReference = struct_anon_26# /usr/local/include/libiec61850/mms_common.h: 172

enum_anon_27 = c_int# /usr/local/include/libiec61850/mms_types.h: 36

MMS_VALUE_NO_RESPONSE = 0# /usr/local/include/libiec61850/mms_types.h: 36

MMS_VALUE_OK = (MMS_VALUE_NO_RESPONSE + 1)# /usr/local/include/libiec61850/mms_types.h: 36

MMS_VALUE_ACCESS_DENIED = (MMS_VALUE_OK + 1)# /usr/local/include/libiec61850/mms_types.h: 36

MMS_VALUE_VALUE_INVALID = (MMS_VALUE_ACCESS_DENIED + 1)# /usr/local/include/libiec61850/mms_types.h: 36

MMS_VALUE_TEMPORARILY_UNAVAILABLE = (MMS_VALUE_VALUE_INVALID + 1)# /usr/local/include/libiec61850/mms_types.h: 36

MMS_VALUE_OBJECT_ACCESS_UNSUPPORTED = (MMS_VALUE_TEMPORARILY_UNAVAILABLE + 1)# /usr/local/include/libiec61850/mms_types.h: 36

MmsValueIndication = enum_anon_27# /usr/local/include/libiec61850/mms_types.h: 36

# /usr/local/include/libiec61850/mms_types.h: 50
class struct_sMmsVariableSpecification(Structure):
    pass

MmsVariableSpecification = struct_sMmsVariableSpecification# /usr/local/include/libiec61850/mms_types.h: 46

# /usr/local/include/libiec61850/mms_types.h: 55
class struct_sMmsArray(Structure):
    pass

struct_sMmsArray.__slots__ = [
    'elementCount',
    'elementTypeSpec',
]
struct_sMmsArray._fields_ = [
    ('elementCount', c_int),
    ('elementTypeSpec', POINTER(MmsVariableSpecification)),
]

# /usr/local/include/libiec61850/mms_types.h: 59
class struct_sMmsStructure(Structure):
    pass

struct_sMmsStructure.__slots__ = [
    'elementCount',
    'elements',
]
struct_sMmsStructure._fields_ = [
    ('elementCount', c_int),
    ('elements', POINTER(POINTER(MmsVariableSpecification))),
]

# /usr/local/include/libiec61850/mms_types.h: 66
class struct_sMmsFloat(Structure):
    pass

struct_sMmsFloat.__slots__ = [
    'exponentWidth',
    'formatWidth',
]
struct_sMmsFloat._fields_ = [
    ('exponentWidth', uint8_t),
    ('formatWidth', uint8_t),
]

# /usr/local/include/libiec61850/mms_types.h: 53
class union_uMmsTypeSpecification(Union):
    pass

union_uMmsTypeSpecification.__slots__ = [
    'array',
    'structure',
    'boolean',
    'integer',
    'unsignedInteger',
    'floatingpoint',
    'bitString',
    'octetString',
    'visibleString',
    'mmsString',
    'utctime',
    'binaryTime',
]
union_uMmsTypeSpecification._fields_ = [
    ('array', struct_sMmsArray),
    ('structure', struct_sMmsStructure),
    ('boolean', c_int),
    ('integer', c_int),
    ('unsignedInteger', c_int),
    ('floatingpoint', struct_sMmsFloat),
    ('bitString', c_int),
    ('octetString', c_int),
    ('visibleString', c_int),
    ('mmsString', c_int),
    ('utctime', c_int),
    ('binaryTime', c_int),
]

struct_sMmsVariableSpecification.__slots__ = [
    'type',
    'name',
    'typeSpec',
]
struct_sMmsVariableSpecification._fields_ = [
    ('type', MmsType),
    ('name', String),
    ('typeSpec', union_uMmsTypeSpecification),
]

enum_anon_28 = c_int# /usr/local/include/libiec61850/mms_value.h: 63

DATA_ACCESS_ERROR_SUCCESS_NO_UPDATE = (-3)# /usr/local/include/libiec61850/mms_value.h: 63

DATA_ACCESS_ERROR_NO_RESPONSE = (-2)# /usr/local/include/libiec61850/mms_value.h: 63

DATA_ACCESS_ERROR_SUCCESS = (-1)# /usr/local/include/libiec61850/mms_value.h: 63

DATA_ACCESS_ERROR_OBJECT_INVALIDATED = 0# /usr/local/include/libiec61850/mms_value.h: 63

DATA_ACCESS_ERROR_HARDWARE_FAULT = 1# /usr/local/include/libiec61850/mms_value.h: 63

DATA_ACCESS_ERROR_TEMPORARILY_UNAVAILABLE = 2# /usr/local/include/libiec61850/mms_value.h: 63

DATA_ACCESS_ERROR_OBJECT_ACCESS_DENIED = 3# /usr/local/include/libiec61850/mms_value.h: 63

DATA_ACCESS_ERROR_OBJECT_UNDEFINED = 4# /usr/local/include/libiec61850/mms_value.h: 63

DATA_ACCESS_ERROR_INVALID_ADDRESS = 5# /usr/local/include/libiec61850/mms_value.h: 63

DATA_ACCESS_ERROR_TYPE_UNSUPPORTED = 6# /usr/local/include/libiec61850/mms_value.h: 63

DATA_ACCESS_ERROR_TYPE_INCONSISTENT = 7# /usr/local/include/libiec61850/mms_value.h: 63

DATA_ACCESS_ERROR_OBJECT_ATTRIBUTE_INCONSISTENT = 8# /usr/local/include/libiec61850/mms_value.h: 63

DATA_ACCESS_ERROR_OBJECT_ACCESS_UNSUPPORTED = 9# /usr/local/include/libiec61850/mms_value.h: 63

DATA_ACCESS_ERROR_OBJECT_NONE_EXISTENT = 10# /usr/local/include/libiec61850/mms_value.h: 63

DATA_ACCESS_ERROR_OBJECT_VALUE_INVALID = 11# /usr/local/include/libiec61850/mms_value.h: 63

DATA_ACCESS_ERROR_UNKNOWN = 12# /usr/local/include/libiec61850/mms_value.h: 63

MmsDataAccessError = enum_anon_28# /usr/local/include/libiec61850/mms_value.h: 63

# /usr/local/include/libiec61850/mms_value.h: 68
class struct_sMmsValue(Structure):
    pass

MmsValue = struct_sMmsValue# /usr/local/include/libiec61850/mms_value.h: 68

# /usr/local/include/libiec61850/mms_value.h: 82
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_createArray", "cdecl"):
    MmsValue_createArray = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_createArray", "cdecl")
    MmsValue_createArray.argtypes = [POINTER(MmsVariableSpecification), c_int]
    MmsValue_createArray.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_value.h: 93
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_getArraySize", "cdecl"):
    MmsValue_getArraySize = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_getArraySize", "cdecl")
    MmsValue_getArraySize.argtypes = [POINTER(MmsValue)]
    MmsValue_getArraySize.restype = uint32_t

# /usr/local/include/libiec61850/mms_value.h: 103
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_getElement", "cdecl"):
    MmsValue_getElement = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_getElement", "cdecl")
    MmsValue_getElement.argtypes = [POINTER(MmsValue), c_int]
    MmsValue_getElement.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_value.h: 113
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_createEmptyArray", "cdecl"):
    MmsValue_createEmptyArray = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_createEmptyArray", "cdecl")
    MmsValue_createEmptyArray.argtypes = [c_int]
    MmsValue_createEmptyArray.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_value.h: 127
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_setElement", "cdecl"):
    MmsValue_setElement = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_setElement", "cdecl")
    MmsValue_setElement.argtypes = [POINTER(MmsValue), c_int, POINTER(MmsValue)]
    MmsValue_setElement.restype = None

# /usr/local/include/libiec61850/mms_value.h: 135
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_getDataAccessError", "cdecl"):
    MmsValue_getDataAccessError = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_getDataAccessError", "cdecl")
    MmsValue_getDataAccessError.argtypes = [POINTER(MmsValue)]
    MmsValue_getDataAccessError.restype = MmsDataAccessError

# /usr/local/include/libiec61850/mms_value.h: 145
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_toInt64", "cdecl"):
    MmsValue_toInt64 = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_toInt64", "cdecl")
    MmsValue_toInt64.argtypes = [POINTER(MmsValue)]
    MmsValue_toInt64.restype = c_int64

# /usr/local/include/libiec61850/mms_value.h: 155
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_toInt32", "cdecl"):
    MmsValue_toInt32 = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_toInt32", "cdecl")
    MmsValue_toInt32.argtypes = [POINTER(MmsValue)]
    MmsValue_toInt32.restype = c_int32

# /usr/local/include/libiec61850/mms_value.h: 165
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_toUint32", "cdecl"):
    MmsValue_toUint32 = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_toUint32", "cdecl")
    MmsValue_toUint32.argtypes = [POINTER(MmsValue)]
    MmsValue_toUint32.restype = uint32_t

# /usr/local/include/libiec61850/mms_value.h: 175
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_toDouble", "cdecl"):
    MmsValue_toDouble = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_toDouble", "cdecl")
    MmsValue_toDouble.argtypes = [POINTER(MmsValue)]
    MmsValue_toDouble.restype = c_double

# /usr/local/include/libiec61850/mms_value.h: 185
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_toFloat", "cdecl"):
    MmsValue_toFloat = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_toFloat", "cdecl")
    MmsValue_toFloat.argtypes = [POINTER(MmsValue)]
    MmsValue_toFloat.restype = c_float

# /usr/local/include/libiec61850/mms_value.h: 195
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_toUnixTimestamp", "cdecl"):
    MmsValue_toUnixTimestamp = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_toUnixTimestamp", "cdecl")
    MmsValue_toUnixTimestamp.argtypes = [POINTER(MmsValue)]
    MmsValue_toUnixTimestamp.restype = uint32_t

# /usr/local/include/libiec61850/mms_value.h: 203
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_setFloat", "cdecl"):
    MmsValue_setFloat = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_setFloat", "cdecl")
    MmsValue_setFloat.argtypes = [POINTER(MmsValue), c_float]
    MmsValue_setFloat.restype = None

# /usr/local/include/libiec61850/mms_value.h: 211
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_setDouble", "cdecl"):
    MmsValue_setDouble = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_setDouble", "cdecl")
    MmsValue_setDouble.argtypes = [POINTER(MmsValue), c_double]
    MmsValue_setDouble.restype = None

# /usr/local/include/libiec61850/mms_value.h: 220
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_setInt8", "cdecl"):
    MmsValue_setInt8 = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_setInt8", "cdecl")
    MmsValue_setInt8.argtypes = [POINTER(MmsValue), c_int8]
    MmsValue_setInt8.restype = None

# /usr/local/include/libiec61850/mms_value.h: 229
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_setInt16", "cdecl"):
    MmsValue_setInt16 = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_setInt16", "cdecl")
    MmsValue_setInt16.argtypes = [POINTER(MmsValue), c_int16]
    MmsValue_setInt16.restype = None

# /usr/local/include/libiec61850/mms_value.h: 238
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_setInt32", "cdecl"):
    MmsValue_setInt32 = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_setInt32", "cdecl")
    MmsValue_setInt32.argtypes = [POINTER(MmsValue), c_int32]
    MmsValue_setInt32.restype = None

# /usr/local/include/libiec61850/mms_value.h: 247
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_setInt64", "cdecl"):
    MmsValue_setInt64 = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_setInt64", "cdecl")
    MmsValue_setInt64.argtypes = [POINTER(MmsValue), c_int64]
    MmsValue_setInt64.restype = None

# /usr/local/include/libiec61850/mms_value.h: 256
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_setUint8", "cdecl"):
    MmsValue_setUint8 = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_setUint8", "cdecl")
    MmsValue_setUint8.argtypes = [POINTER(MmsValue), uint8_t]
    MmsValue_setUint8.restype = None

# /usr/local/include/libiec61850/mms_value.h: 265
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_setUint16", "cdecl"):
    MmsValue_setUint16 = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_setUint16", "cdecl")
    MmsValue_setUint16.argtypes = [POINTER(MmsValue), uint16_t]
    MmsValue_setUint16.restype = None

# /usr/local/include/libiec61850/mms_value.h: 274
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_setUint32", "cdecl"):
    MmsValue_setUint32 = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_setUint32", "cdecl")
    MmsValue_setUint32.argtypes = [POINTER(MmsValue), uint32_t]
    MmsValue_setUint32.restype = None

# /usr/local/include/libiec61850/mms_value.h: 284
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_setBoolean", "cdecl"):
    MmsValue_setBoolean = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_setBoolean", "cdecl")
    MmsValue_setBoolean.argtypes = [POINTER(MmsValue), c_bool]
    MmsValue_setBoolean.restype = None

# /usr/local/include/libiec61850/mms_value.h: 293
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_getBoolean", "cdecl"):
    MmsValue_getBoolean = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_getBoolean", "cdecl")
    MmsValue_getBoolean.argtypes = [POINTER(MmsValue)]
    MmsValue_getBoolean.restype = c_bool

# /usr/local/include/libiec61850/mms_value.h: 302
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_toString", "cdecl"):
    MmsValue_toString = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_toString", "cdecl")
    MmsValue_toString.argtypes = [POINTER(MmsValue)]
    MmsValue_toString.restype = c_char_p

# /usr/local/include/libiec61850/mms_value.h: 313
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_getStringSize", "cdecl"):
    MmsValue_getStringSize = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_getStringSize", "cdecl")
    MmsValue_getStringSize.argtypes = [POINTER(MmsValue)]
    MmsValue_getStringSize.restype = c_int

# /usr/local/include/libiec61850/mms_value.h: 316
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_setVisibleString", "cdecl"):
    MmsValue_setVisibleString = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_setVisibleString", "cdecl")
    MmsValue_setVisibleString.argtypes = [POINTER(MmsValue), String]
    MmsValue_setVisibleString.restype = None

# /usr/local/include/libiec61850/mms_value.h: 328
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_setBitStringBit", "cdecl"):
    MmsValue_setBitStringBit = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_setBitStringBit", "cdecl")
    MmsValue_setBitStringBit.argtypes = [POINTER(MmsValue), c_int, c_bool]
    MmsValue_setBitStringBit.restype = None

# /usr/local/include/libiec61850/mms_value.h: 339
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_getBitStringBit", "cdecl"):
    MmsValue_getBitStringBit = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_getBitStringBit", "cdecl")
    MmsValue_getBitStringBit.argtypes = [POINTER(MmsValue), c_int]
    MmsValue_getBitStringBit.restype = c_bool

# /usr/local/include/libiec61850/mms_value.h: 347
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_deleteAllBitStringBits", "cdecl"):
    MmsValue_deleteAllBitStringBits = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_deleteAllBitStringBits", "cdecl")
    MmsValue_deleteAllBitStringBits.argtypes = [POINTER(MmsValue)]
    MmsValue_deleteAllBitStringBits.restype = None

# /usr/local/include/libiec61850/mms_value.h: 356
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_getBitStringSize", "cdecl"):
    MmsValue_getBitStringSize = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_getBitStringSize", "cdecl")
    MmsValue_getBitStringSize.argtypes = [POINTER(MmsValue)]
    MmsValue_getBitStringSize.restype = c_int

# /usr/local/include/libiec61850/mms_value.h: 364
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_getBitStringByteSize", "cdecl"):
    MmsValue_getBitStringByteSize = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_getBitStringByteSize", "cdecl")
    MmsValue_getBitStringByteSize.argtypes = [POINTER(MmsValue)]
    MmsValue_getBitStringByteSize.restype = c_int

# /usr/local/include/libiec61850/mms_value.h: 372
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_getNumberOfSetBits", "cdecl"):
    MmsValue_getNumberOfSetBits = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_getNumberOfSetBits", "cdecl")
    MmsValue_getNumberOfSetBits.argtypes = [POINTER(MmsValue)]
    MmsValue_getNumberOfSetBits.restype = c_int

# /usr/local/include/libiec61850/mms_value.h: 380
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_setAllBitStringBits", "cdecl"):
    MmsValue_setAllBitStringBits = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_setAllBitStringBits", "cdecl")
    MmsValue_setAllBitStringBits.argtypes = [POINTER(MmsValue)]
    MmsValue_setAllBitStringBits.restype = None

# /usr/local/include/libiec61850/mms_value.h: 391
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_getBitStringAsInteger", "cdecl"):
    MmsValue_getBitStringAsInteger = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_getBitStringAsInteger", "cdecl")
    MmsValue_getBitStringAsInteger.argtypes = [POINTER(MmsValue)]
    MmsValue_getBitStringAsInteger.restype = uint32_t

# /usr/local/include/libiec61850/mms_value.h: 403
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_setBitStringFromInteger", "cdecl"):
    MmsValue_setBitStringFromInteger = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_setBitStringFromInteger", "cdecl")
    MmsValue_setBitStringFromInteger.argtypes = [POINTER(MmsValue), uint32_t]
    MmsValue_setBitStringFromInteger.restype = None

# /usr/local/include/libiec61850/mms_value.h: 414
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_getBitStringAsIntegerBigEndian", "cdecl"):
    MmsValue_getBitStringAsIntegerBigEndian = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_getBitStringAsIntegerBigEndian", "cdecl")
    MmsValue_getBitStringAsIntegerBigEndian.argtypes = [POINTER(MmsValue)]
    MmsValue_getBitStringAsIntegerBigEndian.restype = uint32_t

# /usr/local/include/libiec61850/mms_value.h: 426
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_setBitStringFromIntegerBigEndian", "cdecl"):
    MmsValue_setBitStringFromIntegerBigEndian = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_setBitStringFromIntegerBigEndian", "cdecl")
    MmsValue_setBitStringFromIntegerBigEndian.argtypes = [POINTER(MmsValue), uint32_t]
    MmsValue_setBitStringFromIntegerBigEndian.restype = None

# /usr/local/include/libiec61850/mms_value.h: 434
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_setUtcTime", "cdecl"):
    MmsValue_setUtcTime = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_setUtcTime", "cdecl")
    MmsValue_setUtcTime.argtypes = [POINTER(MmsValue), uint32_t]
    MmsValue_setUtcTime.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_value.h: 443
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_setUtcTimeMs", "cdecl"):
    MmsValue_setUtcTimeMs = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_setUtcTimeMs", "cdecl")
    MmsValue_setUtcTimeMs.argtypes = [POINTER(MmsValue), uint64_t]
    MmsValue_setUtcTimeMs.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_value.h: 455
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_setUtcTimeByBuffer", "cdecl"):
    MmsValue_setUtcTimeByBuffer = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_setUtcTimeByBuffer", "cdecl")
    MmsValue_setUtcTimeByBuffer.argtypes = [POINTER(MmsValue), POINTER(uint8_t)]
    MmsValue_setUtcTimeByBuffer.restype = None

# /usr/local/include/libiec61850/mms_value.h: 466
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_getUtcTimeBuffer", "cdecl"):
    MmsValue_getUtcTimeBuffer = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_getUtcTimeBuffer", "cdecl")
    MmsValue_getUtcTimeBuffer.argtypes = [POINTER(MmsValue)]
    MmsValue_getUtcTimeBuffer.restype = POINTER(uint8_t)

# /usr/local/include/libiec61850/mms_value.h: 477
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_getUtcTimeInMs", "cdecl"):
    MmsValue_getUtcTimeInMs = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_getUtcTimeInMs", "cdecl")
    MmsValue_getUtcTimeInMs.argtypes = [POINTER(MmsValue)]
    MmsValue_getUtcTimeInMs.restype = uint64_t

# /usr/local/include/libiec61850/mms_value.h: 488
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_getUtcTimeInMsWithUs", "cdecl"):
    MmsValue_getUtcTimeInMsWithUs = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_getUtcTimeInMsWithUs", "cdecl")
    MmsValue_getUtcTimeInMsWithUs.argtypes = [POINTER(MmsValue), POINTER(uint32_t)]
    MmsValue_getUtcTimeInMsWithUs.restype = uint64_t

# /usr/local/include/libiec61850/mms_value.h: 504
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_setUtcTimeQuality", "cdecl"):
    MmsValue_setUtcTimeQuality = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_setUtcTimeQuality", "cdecl")
    MmsValue_setUtcTimeQuality.argtypes = [POINTER(MmsValue), uint8_t]
    MmsValue_setUtcTimeQuality.restype = None

# /usr/local/include/libiec61850/mms_value.h: 522
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_setUtcTimeMsEx", "cdecl"):
    MmsValue_setUtcTimeMsEx = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_setUtcTimeMsEx", "cdecl")
    MmsValue_setUtcTimeMsEx.argtypes = [POINTER(MmsValue), uint64_t, uint8_t]
    MmsValue_setUtcTimeMsEx.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_value.h: 540
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_getUtcTimeQuality", "cdecl"):
    MmsValue_getUtcTimeQuality = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_getUtcTimeQuality", "cdecl")
    MmsValue_getUtcTimeQuality.argtypes = [POINTER(MmsValue)]
    MmsValue_getUtcTimeQuality.restype = uint8_t

# /usr/local/include/libiec61850/mms_value.h: 549
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_setBinaryTime", "cdecl"):
    MmsValue_setBinaryTime = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_setBinaryTime", "cdecl")
    MmsValue_setBinaryTime.argtypes = [POINTER(MmsValue), uint64_t]
    MmsValue_setBinaryTime.restype = None

# /usr/local/include/libiec61850/mms_value.h: 559
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_getBinaryTimeAsUtcMs", "cdecl"):
    MmsValue_getBinaryTimeAsUtcMs = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_getBinaryTimeAsUtcMs", "cdecl")
    MmsValue_getBinaryTimeAsUtcMs.argtypes = [POINTER(MmsValue)]
    MmsValue_getBinaryTimeAsUtcMs.restype = uint64_t

# /usr/local/include/libiec61850/mms_value.h: 573
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_setOctetString", "cdecl"):
    MmsValue_setOctetString = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_setOctetString", "cdecl")
    MmsValue_setOctetString.argtypes = [POINTER(MmsValue), POINTER(uint8_t), c_int]
    MmsValue_setOctetString.restype = None

# /usr/local/include/libiec61850/mms_value.h: 588
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_setOctetStringOctet", "cdecl"):
    MmsValue_setOctetStringOctet = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_setOctetStringOctet", "cdecl")
    MmsValue_setOctetStringOctet.argtypes = [POINTER(MmsValue), c_int, uint8_t]
    MmsValue_setOctetStringOctet.restype = None

# /usr/local/include/libiec61850/mms_value.h: 601
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_getOctetStringSize", "cdecl"):
    MmsValue_getOctetStringSize = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_getOctetStringSize", "cdecl")
    MmsValue_getOctetStringSize.argtypes = [POINTER(MmsValue)]
    MmsValue_getOctetStringSize.restype = uint16_t

# /usr/local/include/libiec61850/mms_value.h: 614
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_getOctetStringMaxSize", "cdecl"):
    MmsValue_getOctetStringMaxSize = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_getOctetStringMaxSize", "cdecl")
    MmsValue_getOctetStringMaxSize.argtypes = [POINTER(MmsValue)]
    MmsValue_getOctetStringMaxSize.restype = uint16_t

# /usr/local/include/libiec61850/mms_value.h: 625
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_getOctetStringBuffer", "cdecl"):
    MmsValue_getOctetStringBuffer = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_getOctetStringBuffer", "cdecl")
    MmsValue_getOctetStringBuffer.argtypes = [POINTER(MmsValue)]
    MmsValue_getOctetStringBuffer.restype = POINTER(uint8_t)

# /usr/local/include/libiec61850/mms_value.h: 640
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_getOctetStringOctet", "cdecl"):
    MmsValue_getOctetStringOctet = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_getOctetStringOctet", "cdecl")
    MmsValue_getOctetStringOctet.argtypes = [POINTER(MmsValue), c_int]
    MmsValue_getOctetStringOctet.restype = uint8_t

# /usr/local/include/libiec61850/mms_value.h: 654
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_update", "cdecl"):
    MmsValue_update = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_update", "cdecl")
    MmsValue_update.argtypes = [POINTER(MmsValue), POINTER(MmsValue)]
    MmsValue_update.restype = c_bool

# /usr/local/include/libiec61850/mms_value.h: 668
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_equals", "cdecl"):
    MmsValue_equals = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_equals", "cdecl")
    MmsValue_equals.argtypes = [POINTER(MmsValue), POINTER(MmsValue)]
    MmsValue_equals.restype = c_bool

# /usr/local/include/libiec61850/mms_value.h: 683
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_equalTypes", "cdecl"):
    MmsValue_equalTypes = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_equalTypes", "cdecl")
    MmsValue_equalTypes.argtypes = [POINTER(MmsValue), POINTER(MmsValue)]
    MmsValue_equalTypes.restype = c_bool

# /usr/local/include/libiec61850/mms_value.h: 690
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_newDataAccessError", "cdecl"):
    MmsValue_newDataAccessError = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_newDataAccessError", "cdecl")
    MmsValue_newDataAccessError.argtypes = [MmsDataAccessError]
    MmsValue_newDataAccessError.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_value.h: 693
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_newInteger", "cdecl"):
    MmsValue_newInteger = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_newInteger", "cdecl")
    MmsValue_newInteger.argtypes = [c_int]
    MmsValue_newInteger.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_value.h: 696
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_newUnsigned", "cdecl"):
    MmsValue_newUnsigned = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_newUnsigned", "cdecl")
    MmsValue_newUnsigned.argtypes = [c_int]
    MmsValue_newUnsigned.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_value.h: 699
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_newBoolean", "cdecl"):
    MmsValue_newBoolean = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_newBoolean", "cdecl")
    MmsValue_newBoolean.argtypes = [c_bool]
    MmsValue_newBoolean.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_value.h: 709
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_newBitString", "cdecl"):
    MmsValue_newBitString = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_newBitString", "cdecl")
    MmsValue_newBitString.argtypes = [c_int]
    MmsValue_newBitString.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_value.h: 712
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_newOctetString", "cdecl"):
    MmsValue_newOctetString = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_newOctetString", "cdecl")
    MmsValue_newOctetString.argtypes = [c_int, c_int]
    MmsValue_newOctetString.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_value.h: 715
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_newStructure", "cdecl"):
    MmsValue_newStructure = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_newStructure", "cdecl")
    MmsValue_newStructure.argtypes = [POINTER(MmsVariableSpecification)]
    MmsValue_newStructure.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_value.h: 718
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_createEmptyStructure", "cdecl"):
    MmsValue_createEmptyStructure = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_createEmptyStructure", "cdecl")
    MmsValue_createEmptyStructure.argtypes = [c_int]
    MmsValue_createEmptyStructure.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_value.h: 721
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_newDefaultValue", "cdecl"):
    MmsValue_newDefaultValue = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_newDefaultValue", "cdecl")
    MmsValue_newDefaultValue.argtypes = [POINTER(MmsVariableSpecification)]
    MmsValue_newDefaultValue.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_value.h: 724
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_newIntegerFromInt8", "cdecl"):
    MmsValue_newIntegerFromInt8 = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_newIntegerFromInt8", "cdecl")
    MmsValue_newIntegerFromInt8.argtypes = [c_int8]
    MmsValue_newIntegerFromInt8.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_value.h: 727
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_newIntegerFromInt16", "cdecl"):
    MmsValue_newIntegerFromInt16 = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_newIntegerFromInt16", "cdecl")
    MmsValue_newIntegerFromInt16.argtypes = [c_int16]
    MmsValue_newIntegerFromInt16.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_value.h: 730
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_newIntegerFromInt32", "cdecl"):
    MmsValue_newIntegerFromInt32 = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_newIntegerFromInt32", "cdecl")
    MmsValue_newIntegerFromInt32.argtypes = [c_int32]
    MmsValue_newIntegerFromInt32.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_value.h: 733
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_newIntegerFromInt64", "cdecl"):
    MmsValue_newIntegerFromInt64 = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_newIntegerFromInt64", "cdecl")
    MmsValue_newIntegerFromInt64.argtypes = [c_int64]
    MmsValue_newIntegerFromInt64.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_value.h: 736
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_newUnsignedFromUint32", "cdecl"):
    MmsValue_newUnsignedFromUint32 = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_newUnsignedFromUint32", "cdecl")
    MmsValue_newUnsignedFromUint32.argtypes = [uint32_t]
    MmsValue_newUnsignedFromUint32.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_value.h: 746
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_newFloat", "cdecl"):
    MmsValue_newFloat = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_newFloat", "cdecl")
    MmsValue_newFloat.argtypes = [c_float]
    MmsValue_newFloat.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_value.h: 756
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_newDouble", "cdecl"):
    MmsValue_newDouble = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_newDouble", "cdecl")
    MmsValue_newDouble.argtypes = [c_double]
    MmsValue_newDouble.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_value.h: 769
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_clone", "cdecl"):
    MmsValue_clone = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_clone", "cdecl")
    MmsValue_clone.argtypes = [POINTER(MmsValue)]
    MmsValue_clone.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_value.h: 782
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_cloneToBuffer", "cdecl"):
    MmsValue_cloneToBuffer = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_cloneToBuffer", "cdecl")
    MmsValue_cloneToBuffer.argtypes = [POINTER(MmsValue), POINTER(uint8_t)]
    MmsValue_cloneToBuffer.restype = POINTER(uint8_t)

# /usr/local/include/libiec61850/mms_value.h: 796
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_getSizeInMemory", "cdecl"):
    MmsValue_getSizeInMemory = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_getSizeInMemory", "cdecl")
    MmsValue_getSizeInMemory.argtypes = [POINTER(MmsValue)]
    MmsValue_getSizeInMemory.restype = c_int

# /usr/local/include/libiec61850/mms_value.h: 808
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_delete", "cdecl"):
    MmsValue_delete = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_delete", "cdecl")
    MmsValue_delete.argtypes = [POINTER(MmsValue)]
    MmsValue_delete.restype = None

# /usr/local/include/libiec61850/mms_value.h: 823
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_deleteConditional", "cdecl"):
    MmsValue_deleteConditional = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_deleteConditional", "cdecl")
    MmsValue_deleteConditional.argtypes = [POINTER(MmsValue)]
    MmsValue_deleteConditional.restype = None

# /usr/local/include/libiec61850/mms_value.h: 835
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_newVisibleString", "cdecl"):
    MmsValue_newVisibleString = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_newVisibleString", "cdecl")
    MmsValue_newVisibleString.argtypes = [String]
    MmsValue_newVisibleString.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_value.h: 849
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_newVisibleStringWithSize", "cdecl"):
    MmsValue_newVisibleStringWithSize = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_newVisibleStringWithSize", "cdecl")
    MmsValue_newVisibleStringWithSize.argtypes = [c_int]
    MmsValue_newVisibleStringWithSize.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_value.h: 863
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_newMmsStringWithSize", "cdecl"):
    MmsValue_newMmsStringWithSize = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_newMmsStringWithSize", "cdecl")
    MmsValue_newMmsStringWithSize.argtypes = [c_int]
    MmsValue_newMmsStringWithSize.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_value.h: 877
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_newBinaryTime", "cdecl"):
    MmsValue_newBinaryTime = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_newBinaryTime", "cdecl")
    MmsValue_newBinaryTime.argtypes = [c_bool]
    MmsValue_newBinaryTime.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_value.h: 888
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_newVisibleStringFromByteArray", "cdecl"):
    MmsValue_newVisibleStringFromByteArray = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_newVisibleStringFromByteArray", "cdecl")
    MmsValue_newVisibleStringFromByteArray.argtypes = [POINTER(uint8_t), c_int]
    MmsValue_newVisibleStringFromByteArray.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_value.h: 899
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_newMmsStringFromByteArray", "cdecl"):
    MmsValue_newMmsStringFromByteArray = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_newMmsStringFromByteArray", "cdecl")
    MmsValue_newMmsStringFromByteArray.argtypes = [POINTER(uint8_t), c_int]
    MmsValue_newMmsStringFromByteArray.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_value.h: 909
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_newMmsString", "cdecl"):
    MmsValue_newMmsString = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_newMmsString", "cdecl")
    MmsValue_newMmsString.argtypes = [String]
    MmsValue_newMmsString.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_value.h: 918
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_setMmsString", "cdecl"):
    MmsValue_setMmsString = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_setMmsString", "cdecl")
    MmsValue_setMmsString.argtypes = [POINTER(MmsValue), String]
    MmsValue_setMmsString.restype = None

# /usr/local/include/libiec61850/mms_value.h: 927
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_newUtcTime", "cdecl"):
    MmsValue_newUtcTime = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_newUtcTime", "cdecl")
    MmsValue_newUtcTime.argtypes = [uint32_t]
    MmsValue_newUtcTime.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_value.h: 937
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_newUtcTimeByMsTime", "cdecl"):
    MmsValue_newUtcTimeByMsTime = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_newUtcTimeByMsTime", "cdecl")
    MmsValue_newUtcTimeByMsTime.argtypes = [uint64_t]
    MmsValue_newUtcTimeByMsTime.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_value.h: 942
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_setDeletable", "cdecl"):
    MmsValue_setDeletable = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_setDeletable", "cdecl")
    MmsValue_setDeletable.argtypes = [POINTER(MmsValue)]
    MmsValue_setDeletable.restype = None

# /usr/local/include/libiec61850/mms_value.h: 945
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_setDeletableRecursive", "cdecl"):
    MmsValue_setDeletableRecursive = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_setDeletableRecursive", "cdecl")
    MmsValue_setDeletableRecursive.argtypes = [POINTER(MmsValue)]
    MmsValue_setDeletableRecursive.restype = None

# /usr/local/include/libiec61850/mms_value.h: 959
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_isDeletable", "cdecl"):
    MmsValue_isDeletable = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_isDeletable", "cdecl")
    MmsValue_isDeletable.argtypes = [POINTER(MmsValue)]
    MmsValue_isDeletable.restype = c_int

# /usr/local/include/libiec61850/mms_value.h: 967
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_getType", "cdecl"):
    MmsValue_getType = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_getType", "cdecl")
    MmsValue_getType.argtypes = [POINTER(MmsValue)]
    MmsValue_getType.restype = MmsType

# /usr/local/include/libiec61850/mms_value.h: 978
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_getSubElement", "cdecl"):
    MmsValue_getSubElement = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_getSubElement", "cdecl")
    MmsValue_getSubElement.argtypes = [POINTER(MmsValue), POINTER(MmsVariableSpecification), String]
    MmsValue_getSubElement.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_value.h: 988
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_getTypeString", "cdecl"):
    MmsValue_getTypeString = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_getTypeString", "cdecl")
    MmsValue_getTypeString.argtypes = [POINTER(MmsValue)]
    if sizeof(c_int) == sizeof(c_void_p):
        MmsValue_getTypeString.restype = ReturnString
    else:
        MmsValue_getTypeString.restype = String
        MmsValue_getTypeString.errcheck = ReturnString

# /usr/local/include/libiec61850/mms_value.h: 1003
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_printToBuffer", "cdecl"):
    MmsValue_printToBuffer = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_printToBuffer", "cdecl")
    MmsValue_printToBuffer.argtypes = [POINTER(MmsValue), String, c_int]
    MmsValue_printToBuffer.restype = c_char_p

# /usr/local/include/libiec61850/mms_value.h: 1018
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_decodeMmsData", "cdecl"):
    MmsValue_decodeMmsData = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_decodeMmsData", "cdecl")
    MmsValue_decodeMmsData.argtypes = [POINTER(uint8_t), c_int, c_int, POINTER(c_int)]
    MmsValue_decodeMmsData.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_value.h: 1033
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_encodeMmsData", "cdecl"):
    MmsValue_encodeMmsData = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_encodeMmsData", "cdecl")
    MmsValue_encodeMmsData.argtypes = [POINTER(MmsValue), POINTER(uint8_t), c_int, c_bool]
    MmsValue_encodeMmsData.restype = c_int

# /usr/local/include/libiec61850/mms_value.h: 1043
if _libs["/usr/local/lib/libiec61850.so"].has("MmsValue_getMaxEncodedSize", "cdecl"):
    MmsValue_getMaxEncodedSize = _libs["/usr/local/lib/libiec61850.so"].get("MmsValue_getMaxEncodedSize", "cdecl")
    MmsValue_getMaxEncodedSize.argtypes = [POINTER(MmsValue)]
    MmsValue_getMaxEncodedSize.restype = c_int

# /usr/local/include/libiec61850/mms_value.h: 1051
if _libs["/usr/local/lib/libiec61850.so"].has("MmsVariableSpecification_getMaxEncodedSize", "cdecl"):
    MmsVariableSpecification_getMaxEncodedSize = _libs["/usr/local/lib/libiec61850.so"].get("MmsVariableSpecification_getMaxEncodedSize", "cdecl")
    MmsVariableSpecification_getMaxEncodedSize.argtypes = [POINTER(MmsVariableSpecification)]
    MmsVariableSpecification_getMaxEncodedSize.restype = c_int

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

# /usr/local/include/libiec61850/linked_list.h: 60
if _libs["/usr/local/lib/libiec61850.so"].has("LinkedList_create", "cdecl"):
    LinkedList_create = _libs["/usr/local/lib/libiec61850.so"].get("LinkedList_create", "cdecl")
    LinkedList_create.argtypes = []
    LinkedList_create.restype = LinkedList

# /usr/local/include/libiec61850/linked_list.h: 72
if _libs["/usr/local/lib/libiec61850.so"].has("LinkedList_destroy", "cdecl"):
    LinkedList_destroy = _libs["/usr/local/lib/libiec61850.so"].get("LinkedList_destroy", "cdecl")
    LinkedList_destroy.argtypes = [LinkedList]
    LinkedList_destroy.restype = None

LinkedListValueDeleteFunction = CFUNCTYPE(UNCHECKED(None), POINTER(None))# /usr/local/include/libiec61850/linked_list.h: 75

# /usr/local/include/libiec61850/linked_list.h: 89
if _libs["/usr/local/lib/libiec61850.so"].has("LinkedList_destroyDeep", "cdecl"):
    LinkedList_destroyDeep = _libs["/usr/local/lib/libiec61850.so"].get("LinkedList_destroyDeep", "cdecl")
    LinkedList_destroyDeep.argtypes = [LinkedList, LinkedListValueDeleteFunction]
    LinkedList_destroyDeep.restype = None

# /usr/local/include/libiec61850/linked_list.h: 100
if _libs["/usr/local/lib/libiec61850.so"].has("LinkedList_destroyStatic", "cdecl"):
    LinkedList_destroyStatic = _libs["/usr/local/lib/libiec61850.so"].get("LinkedList_destroyStatic", "cdecl")
    LinkedList_destroyStatic.argtypes = [LinkedList]
    LinkedList_destroyStatic.restype = None

# /usr/local/include/libiec61850/linked_list.h: 112
if _libs["/usr/local/lib/libiec61850.so"].has("LinkedList_add", "cdecl"):
    LinkedList_add = _libs["/usr/local/lib/libiec61850.so"].get("LinkedList_add", "cdecl")
    LinkedList_add.argtypes = [LinkedList, POINTER(None)]
    LinkedList_add.restype = None

# /usr/local/include/libiec61850/linked_list.h: 123
if _libs["/usr/local/lib/libiec61850.so"].has("LinkedList_contains", "cdecl"):
    LinkedList_contains = _libs["/usr/local/lib/libiec61850.so"].get("LinkedList_contains", "cdecl")
    LinkedList_contains.argtypes = [LinkedList, POINTER(None)]
    LinkedList_contains.restype = c_bool

# /usr/local/include/libiec61850/linked_list.h: 134
if _libs["/usr/local/lib/libiec61850.so"].has("LinkedList_remove", "cdecl"):
    LinkedList_remove = _libs["/usr/local/lib/libiec61850.so"].get("LinkedList_remove", "cdecl")
    LinkedList_remove.argtypes = [LinkedList, POINTER(None)]
    LinkedList_remove.restype = c_bool

# /usr/local/include/libiec61850/linked_list.h: 143
if _libs["/usr/local/lib/libiec61850.so"].has("LinkedList_get", "cdecl"):
    LinkedList_get = _libs["/usr/local/lib/libiec61850.so"].get("LinkedList_get", "cdecl")
    LinkedList_get.argtypes = [LinkedList, c_int]
    LinkedList_get.restype = LinkedList

# /usr/local/include/libiec61850/linked_list.h: 151
if _libs["/usr/local/lib/libiec61850.so"].has("LinkedList_getNext", "cdecl"):
    LinkedList_getNext = _libs["/usr/local/lib/libiec61850.so"].get("LinkedList_getNext", "cdecl")
    LinkedList_getNext.argtypes = [LinkedList]
    LinkedList_getNext.restype = LinkedList

# /usr/local/include/libiec61850/linked_list.h: 159
if _libs["/usr/local/lib/libiec61850.so"].has("LinkedList_getLastElement", "cdecl"):
    LinkedList_getLastElement = _libs["/usr/local/lib/libiec61850.so"].get("LinkedList_getLastElement", "cdecl")
    LinkedList_getLastElement.argtypes = [LinkedList]
    LinkedList_getLastElement.restype = LinkedList

# /usr/local/include/libiec61850/linked_list.h: 167
if _libs["/usr/local/lib/libiec61850.so"].has("LinkedList_insertAfter", "cdecl"):
    LinkedList_insertAfter = _libs["/usr/local/lib/libiec61850.so"].get("LinkedList_insertAfter", "cdecl")
    LinkedList_insertAfter.argtypes = [LinkedList, POINTER(None)]
    LinkedList_insertAfter.restype = LinkedList

# /usr/local/include/libiec61850/linked_list.h: 177
if _libs["/usr/local/lib/libiec61850.so"].has("LinkedList_size", "cdecl"):
    LinkedList_size = _libs["/usr/local/lib/libiec61850.so"].get("LinkedList_size", "cdecl")
    LinkedList_size.argtypes = [LinkedList]
    LinkedList_size.restype = c_int

# /usr/local/include/libiec61850/linked_list.h: 179
if _libs["/usr/local/lib/libiec61850.so"].has("LinkedList_getData", "cdecl"):
    LinkedList_getData = _libs["/usr/local/lib/libiec61850.so"].get("LinkedList_getData", "cdecl")
    LinkedList_getData.argtypes = [LinkedList]
    LinkedList_getData.restype = POINTER(c_ubyte)
    LinkedList_getData.errcheck = lambda v,*a : cast(v, c_void_p)

# /usr/local/include/libiec61850/linked_list.h: 183
if _libs["/usr/local/lib/libiec61850.so"].has("LinkedList_printStringList", "cdecl"):
    LinkedList_printStringList = _libs["/usr/local/lib/libiec61850.so"].get("LinkedList_printStringList", "cdecl")
    LinkedList_printStringList.argtypes = [LinkedList]
    LinkedList_printStringList.restype = None

# /usr/local/include/libiec61850/logging_api.h: 78
class struct_sLogStorage(Structure):
    pass

LogStorage = POINTER(struct_sLogStorage)# /usr/local/include/libiec61850/logging_api.h: 50

LogEntryCallback = CFUNCTYPE(UNCHECKED(c_bool), POINTER(None), uint64_t, uint64_t, c_bool)# /usr/local/include/libiec61850/logging_api.h: 62

LogEntryDataCallback = CFUNCTYPE(UNCHECKED(c_bool), POINTER(None), String, POINTER(uint8_t), c_int, uint8_t, c_bool)# /usr/local/include/libiec61850/logging_api.h: 76

struct_sLogStorage.__slots__ = [
    'instanceData',
    'maxLogEntries',
    'addEntry',
    'addEntryData',
    'getEntries',
    'getEntriesAfter',
    'getOldestAndNewestEntries',
    'destroy',
]
struct_sLogStorage._fields_ = [
    ('instanceData', POINTER(None)),
    ('maxLogEntries', c_int),
    ('addEntry', CFUNCTYPE(UNCHECKED(uint64_t), LogStorage, uint64_t)),
    ('addEntryData', CFUNCTYPE(UNCHECKED(c_bool), LogStorage, uint64_t, String, POINTER(uint8_t), c_int, uint8_t)),
    ('getEntries', CFUNCTYPE(UNCHECKED(c_bool), LogStorage, uint64_t, uint64_t, LogEntryCallback, LogEntryDataCallback, POINTER(None))),
    ('getEntriesAfter', CFUNCTYPE(UNCHECKED(c_bool), LogStorage, uint64_t, uint64_t, LogEntryCallback, LogEntryDataCallback, POINTER(None))),
    ('getOldestAndNewestEntries', CFUNCTYPE(UNCHECKED(c_bool), LogStorage, POINTER(uint64_t), POINTER(uint64_t), POINTER(uint64_t), POINTER(uint64_t))),
    ('destroy', CFUNCTYPE(UNCHECKED(None), LogStorage)),
]

# /usr/local/include/libiec61850/logging_api.h: 108
if _libs["/usr/local/lib/libiec61850.so"].has("LogStorage_setMaxLogEntries", "cdecl"):
    LogStorage_setMaxLogEntries = _libs["/usr/local/lib/libiec61850.so"].get("LogStorage_setMaxLogEntries", "cdecl")
    LogStorage_setMaxLogEntries.argtypes = [LogStorage, c_int]
    LogStorage_setMaxLogEntries.restype = None

# /usr/local/include/libiec61850/logging_api.h: 118
if _libs["/usr/local/lib/libiec61850.so"].has("LogStorage_getMaxLogEntries", "cdecl"):
    LogStorage_getMaxLogEntries = _libs["/usr/local/lib/libiec61850.so"].get("LogStorage_getMaxLogEntries", "cdecl")
    LogStorage_getMaxLogEntries.argtypes = [LogStorage]
    LogStorage_getMaxLogEntries.restype = c_int

# /usr/local/include/libiec61850/logging_api.h: 129
if _libs["/usr/local/lib/libiec61850.so"].has("LogStorage_addEntry", "cdecl"):
    LogStorage_addEntry = _libs["/usr/local/lib/libiec61850.so"].get("LogStorage_addEntry", "cdecl")
    LogStorage_addEntry.argtypes = [LogStorage, uint64_t]
    LogStorage_addEntry.restype = uint64_t

# /usr/local/include/libiec61850/logging_api.h: 144
if _libs["/usr/local/lib/libiec61850.so"].has("LogStorage_addEntryData", "cdecl"):
    LogStorage_addEntryData = _libs["/usr/local/lib/libiec61850.so"].get("LogStorage_addEntryData", "cdecl")
    LogStorage_addEntryData.argtypes = [LogStorage, uint64_t, String, POINTER(uint8_t), c_int, uint8_t]
    LogStorage_addEntryData.restype = c_bool

# /usr/local/include/libiec61850/logging_api.h: 159
if _libs["/usr/local/lib/libiec61850.so"].has("LogStorage_getEntries", "cdecl"):
    LogStorage_getEntries = _libs["/usr/local/lib/libiec61850.so"].get("LogStorage_getEntries", "cdecl")
    LogStorage_getEntries.argtypes = [LogStorage, uint64_t, uint64_t, LogEntryCallback, LogEntryDataCallback, POINTER(None)]
    LogStorage_getEntries.restype = c_bool

# /usr/local/include/libiec61850/logging_api.h: 178
if _libs["/usr/local/lib/libiec61850.so"].has("LogStorage_getEntriesAfter", "cdecl"):
    LogStorage_getEntriesAfter = _libs["/usr/local/lib/libiec61850.so"].get("LogStorage_getEntriesAfter", "cdecl")
    LogStorage_getEntriesAfter.argtypes = [LogStorage, uint64_t, uint64_t, LogEntryCallback, LogEntryDataCallback, POINTER(None)]
    LogStorage_getEntriesAfter.restype = c_bool

# /usr/local/include/libiec61850/logging_api.h: 194
if _libs["/usr/local/lib/libiec61850.so"].has("LogStorage_getOldestAndNewestEntries", "cdecl"):
    LogStorage_getOldestAndNewestEntries = _libs["/usr/local/lib/libiec61850.so"].get("LogStorage_getOldestAndNewestEntries", "cdecl")
    LogStorage_getOldestAndNewestEntries.argtypes = [LogStorage, POINTER(uint64_t), POINTER(uint64_t), POINTER(uint64_t), POINTER(uint64_t)]
    LogStorage_getOldestAndNewestEntries.restype = c_bool

# /usr/local/include/libiec61850/logging_api.h: 203
if _libs["/usr/local/lib/libiec61850.so"].has("LogStorage_destroy", "cdecl"):
    LogStorage_destroy = _libs["/usr/local/lib/libiec61850.so"].get("LogStorage_destroy", "cdecl")
    LogStorage_destroy.argtypes = [LogStorage]
    LogStorage_destroy.restype = None

# /usr/local/include/libiec61850/iec61850_common.h: 56
class struct_anon_29(Structure):
    pass

struct_anon_29.__slots__ = [
    'vlanPriority',
    'vlanId',
    'appId',
    'dstAddress',
]
struct_anon_29._fields_ = [
    ('vlanPriority', uint8_t),
    ('vlanId', uint16_t),
    ('appId', uint16_t),
    ('dstAddress', uint8_t * int(6)),
]

PhyComAddress = struct_anon_29# /usr/local/include/libiec61850/iec61850_common.h: 56

enum_anon_30 = c_int# /usr/local/include/libiec61850/iec61850_common.h: 88

CONTROL_MODEL_STATUS_ONLY = 0# /usr/local/include/libiec61850/iec61850_common.h: 88

CONTROL_MODEL_DIRECT_NORMAL = 1# /usr/local/include/libiec61850/iec61850_common.h: 88

CONTROL_MODEL_SBO_NORMAL = 2# /usr/local/include/libiec61850/iec61850_common.h: 88

CONTROL_MODEL_DIRECT_ENHANCED = 3# /usr/local/include/libiec61850/iec61850_common.h: 88

CONTROL_MODEL_SBO_ENHANCED = 4# /usr/local/include/libiec61850/iec61850_common.h: 88

ControlModel = enum_anon_30# /usr/local/include/libiec61850/iec61850_common.h: 88

enum_anon_31 = c_int# /usr/local/include/libiec61850/iec61850_common.h: 219

ADD_CAUSE_UNKNOWN = 0# /usr/local/include/libiec61850/iec61850_common.h: 219

ADD_CAUSE_NOT_SUPPORTED = 1# /usr/local/include/libiec61850/iec61850_common.h: 219

ADD_CAUSE_BLOCKED_BY_SWITCHING_HIERARCHY = 2# /usr/local/include/libiec61850/iec61850_common.h: 219

ADD_CAUSE_SELECT_FAILED = 3# /usr/local/include/libiec61850/iec61850_common.h: 219

ADD_CAUSE_INVALID_POSITION = 4# /usr/local/include/libiec61850/iec61850_common.h: 219

ADD_CAUSE_POSITION_REACHED = 5# /usr/local/include/libiec61850/iec61850_common.h: 219

ADD_CAUSE_PARAMETER_CHANGE_IN_EXECUTION = 6# /usr/local/include/libiec61850/iec61850_common.h: 219

ADD_CAUSE_STEP_LIMIT = 7# /usr/local/include/libiec61850/iec61850_common.h: 219

ADD_CAUSE_BLOCKED_BY_MODE = 8# /usr/local/include/libiec61850/iec61850_common.h: 219

ADD_CAUSE_BLOCKED_BY_PROCESS = 9# /usr/local/include/libiec61850/iec61850_common.h: 219

ADD_CAUSE_BLOCKED_BY_INTERLOCKING = 10# /usr/local/include/libiec61850/iec61850_common.h: 219

ADD_CAUSE_BLOCKED_BY_SYNCHROCHECK = 11# /usr/local/include/libiec61850/iec61850_common.h: 219

ADD_CAUSE_COMMAND_ALREADY_IN_EXECUTION = 12# /usr/local/include/libiec61850/iec61850_common.h: 219

ADD_CAUSE_BLOCKED_BY_HEALTH = 13# /usr/local/include/libiec61850/iec61850_common.h: 219

ADD_CAUSE_1_OF_N_CONTROL = 14# /usr/local/include/libiec61850/iec61850_common.h: 219

ADD_CAUSE_ABORTION_BY_CANCEL = 15# /usr/local/include/libiec61850/iec61850_common.h: 219

ADD_CAUSE_TIME_LIMIT_OVER = 16# /usr/local/include/libiec61850/iec61850_common.h: 219

ADD_CAUSE_ABORTION_BY_TRIP = 17# /usr/local/include/libiec61850/iec61850_common.h: 219

ADD_CAUSE_OBJECT_NOT_SELECTED = 18# /usr/local/include/libiec61850/iec61850_common.h: 219

ADD_CAUSE_OBJECT_ALREADY_SELECTED = 19# /usr/local/include/libiec61850/iec61850_common.h: 219

ADD_CAUSE_NO_ACCESS_AUTHORITY = 20# /usr/local/include/libiec61850/iec61850_common.h: 219

ADD_CAUSE_ENDED_WITH_OVERSHOOT = 21# /usr/local/include/libiec61850/iec61850_common.h: 219

ADD_CAUSE_ABORTION_DUE_TO_DEVIATION = 22# /usr/local/include/libiec61850/iec61850_common.h: 219

ADD_CAUSE_ABORTION_BY_COMMUNICATION_LOSS = 23# /usr/local/include/libiec61850/iec61850_common.h: 219

ADD_CAUSE_ABORTION_BY_COMMAND = 24# /usr/local/include/libiec61850/iec61850_common.h: 219

ADD_CAUSE_NONE = 25# /usr/local/include/libiec61850/iec61850_common.h: 219

ADD_CAUSE_INCONSISTENT_PARAMETERS = 26# /usr/local/include/libiec61850/iec61850_common.h: 219

ADD_CAUSE_LOCKED_BY_OTHER_CLIENT = 27# /usr/local/include/libiec61850/iec61850_common.h: 219

ControlAddCause = enum_anon_31# /usr/local/include/libiec61850/iec61850_common.h: 219

enum_anon_32 = c_int# /usr/local/include/libiec61850/iec61850_common.h: 234

CONTROL_ERROR_NO_ERROR = 0# /usr/local/include/libiec61850/iec61850_common.h: 234

CONTROL_ERROR_UNKNOWN = 1# /usr/local/include/libiec61850/iec61850_common.h: 234

CONTROL_ERROR_TIMEOUT_TEST = 2# /usr/local/include/libiec61850/iec61850_common.h: 234

CONTROL_ERROR_OPERATOR_TEST = 3# /usr/local/include/libiec61850/iec61850_common.h: 234

ControlLastApplError = enum_anon_32# /usr/local/include/libiec61850/iec61850_common.h: 234

enum_eFunctionalConstraint = c_int# /usr/local/include/libiec61850/iec61850_common.h: 307

IEC61850_FC_ST = 0# /usr/local/include/libiec61850/iec61850_common.h: 307

IEC61850_FC_MX = 1# /usr/local/include/libiec61850/iec61850_common.h: 307

IEC61850_FC_SP = 2# /usr/local/include/libiec61850/iec61850_common.h: 307

IEC61850_FC_SV = 3# /usr/local/include/libiec61850/iec61850_common.h: 307

IEC61850_FC_CF = 4# /usr/local/include/libiec61850/iec61850_common.h: 307

IEC61850_FC_DC = 5# /usr/local/include/libiec61850/iec61850_common.h: 307

IEC61850_FC_SG = 6# /usr/local/include/libiec61850/iec61850_common.h: 307

IEC61850_FC_SE = 7# /usr/local/include/libiec61850/iec61850_common.h: 307

IEC61850_FC_SR = 8# /usr/local/include/libiec61850/iec61850_common.h: 307

IEC61850_FC_OR = 9# /usr/local/include/libiec61850/iec61850_common.h: 307

IEC61850_FC_BL = 10# /usr/local/include/libiec61850/iec61850_common.h: 307

IEC61850_FC_EX = 11# /usr/local/include/libiec61850/iec61850_common.h: 307

IEC61850_FC_CO = 12# /usr/local/include/libiec61850/iec61850_common.h: 307

IEC61850_FC_US = 13# /usr/local/include/libiec61850/iec61850_common.h: 307

IEC61850_FC_MS = 14# /usr/local/include/libiec61850/iec61850_common.h: 307

IEC61850_FC_RP = 15# /usr/local/include/libiec61850/iec61850_common.h: 307

IEC61850_FC_BR = 16# /usr/local/include/libiec61850/iec61850_common.h: 307

IEC61850_FC_LG = 17# /usr/local/include/libiec61850/iec61850_common.h: 307

IEC61850_FC_GO = 18# /usr/local/include/libiec61850/iec61850_common.h: 307

IEC61850_FC_ALL = 99# /usr/local/include/libiec61850/iec61850_common.h: 307

IEC61850_FC_NONE = (-1)# /usr/local/include/libiec61850/iec61850_common.h: 307

FunctionalConstraint = enum_eFunctionalConstraint# /usr/local/include/libiec61850/iec61850_common.h: 307

# /usr/local/include/libiec61850/iec61850_common.h: 312
if _libs["/usr/local/lib/libiec61850.so"].has("FunctionalConstraint_toString", "cdecl"):
    FunctionalConstraint_toString = _libs["/usr/local/lib/libiec61850.so"].get("FunctionalConstraint_toString", "cdecl")
    FunctionalConstraint_toString.argtypes = [FunctionalConstraint]
    if sizeof(c_int) == sizeof(c_void_p):
        FunctionalConstraint_toString.restype = ReturnString
    else:
        FunctionalConstraint_toString.restype = String
        FunctionalConstraint_toString.errcheck = ReturnString

# /usr/local/include/libiec61850/iec61850_common.h: 319
if _libs["/usr/local/lib/libiec61850.so"].has("FunctionalConstraint_fromString", "cdecl"):
    FunctionalConstraint_fromString = _libs["/usr/local/lib/libiec61850.so"].get("FunctionalConstraint_fromString", "cdecl")
    FunctionalConstraint_fromString.argtypes = [String]
    FunctionalConstraint_fromString.restype = FunctionalConstraint

Quality = uint16_t# /usr/local/include/libiec61850/iec61850_common.h: 330

Validity = uint16_t# /usr/local/include/libiec61850/iec61850_common.h: 331

# /usr/local/include/libiec61850/iec61850_common.h: 356
if _libs["/usr/local/lib/libiec61850.so"].has("Quality_getValidity", "cdecl"):
    Quality_getValidity = _libs["/usr/local/lib/libiec61850.so"].get("Quality_getValidity", "cdecl")
    Quality_getValidity.argtypes = [POINTER(Quality)]
    Quality_getValidity.restype = Validity

# /usr/local/include/libiec61850/iec61850_common.h: 359
if _libs["/usr/local/lib/libiec61850.so"].has("Quality_setValidity", "cdecl"):
    Quality_setValidity = _libs["/usr/local/lib/libiec61850.so"].get("Quality_setValidity", "cdecl")
    Quality_setValidity.argtypes = [POINTER(Quality), Validity]
    Quality_setValidity.restype = None

# /usr/local/include/libiec61850/iec61850_common.h: 362
if _libs["/usr/local/lib/libiec61850.so"].has("Quality_setFlag", "cdecl"):
    Quality_setFlag = _libs["/usr/local/lib/libiec61850.so"].get("Quality_setFlag", "cdecl")
    Quality_setFlag.argtypes = [POINTER(Quality), c_int]
    Quality_setFlag.restype = None

# /usr/local/include/libiec61850/iec61850_common.h: 365
if _libs["/usr/local/lib/libiec61850.so"].has("Quality_unsetFlag", "cdecl"):
    Quality_unsetFlag = _libs["/usr/local/lib/libiec61850.so"].get("Quality_unsetFlag", "cdecl")
    Quality_unsetFlag.argtypes = [POINTER(Quality), c_int]
    Quality_unsetFlag.restype = None

# /usr/local/include/libiec61850/iec61850_common.h: 368
if _libs["/usr/local/lib/libiec61850.so"].has("Quality_isFlagSet", "cdecl"):
    Quality_isFlagSet = _libs["/usr/local/lib/libiec61850.so"].get("Quality_isFlagSet", "cdecl")
    Quality_isFlagSet.argtypes = [POINTER(Quality), c_int]
    Quality_isFlagSet.restype = c_bool

# /usr/local/include/libiec61850/iec61850_common.h: 371
if _libs["/usr/local/lib/libiec61850.so"].has("Quality_fromMmsValue", "cdecl"):
    Quality_fromMmsValue = _libs["/usr/local/lib/libiec61850.so"].get("Quality_fromMmsValue", "cdecl")
    Quality_fromMmsValue.argtypes = [POINTER(MmsValue)]
    Quality_fromMmsValue.restype = Quality

# /usr/local/include/libiec61850/iec61850_common.h: 373
if _libs["/usr/local/lib/libiec61850.so"].has("Quality_toMmsValue", "cdecl"):
    Quality_toMmsValue = _libs["/usr/local/lib/libiec61850.so"].get("Quality_toMmsValue", "cdecl")
    Quality_toMmsValue.argtypes = [POINTER(Quality), POINTER(MmsValue)]
    Quality_toMmsValue.restype = POINTER(MmsValue)

enum_anon_33 = c_int# /usr/local/include/libiec61850/iec61850_common.h: 389

DBPOS_INTERMEDIATE_STATE = 0# /usr/local/include/libiec61850/iec61850_common.h: 389

DBPOS_OFF = 1# /usr/local/include/libiec61850/iec61850_common.h: 389

DBPOS_ON = 2# /usr/local/include/libiec61850/iec61850_common.h: 389

DBPOS_BAD_STATE = 3# /usr/local/include/libiec61850/iec61850_common.h: 389

Dbpos = enum_anon_33# /usr/local/include/libiec61850/iec61850_common.h: 389

# /usr/local/include/libiec61850/iec61850_common.h: 400
if _libs["/usr/local/lib/libiec61850.so"].has("Dbpos_fromMmsValue", "cdecl"):
    Dbpos_fromMmsValue = _libs["/usr/local/lib/libiec61850.so"].get("Dbpos_fromMmsValue", "cdecl")
    Dbpos_fromMmsValue.argtypes = [POINTER(MmsValue)]
    Dbpos_fromMmsValue.restype = Dbpos

# /usr/local/include/libiec61850/iec61850_common.h: 410
if _libs["/usr/local/lib/libiec61850.so"].has("Dbpos_toMmsValue", "cdecl"):
    Dbpos_toMmsValue = _libs["/usr/local/lib/libiec61850.so"].get("Dbpos_toMmsValue", "cdecl")
    Dbpos_toMmsValue.argtypes = [POINTER(MmsValue), Dbpos]
    Dbpos_toMmsValue.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/iec61850_common.h: 423
class union_anon_34(Union):
    pass

union_anon_34.__slots__ = [
    'val',
]
union_anon_34._fields_ = [
    ('val', uint8_t * int(8)),
]

Timestamp = union_anon_34# /usr/local/include/libiec61850/iec61850_common.h: 423

# /usr/local/include/libiec61850/iec61850_common.h: 425
if _libs["/usr/local/lib/libiec61850.so"].has("Timestamp_create", "cdecl"):
    Timestamp_create = _libs["/usr/local/lib/libiec61850.so"].get("Timestamp_create", "cdecl")
    Timestamp_create.argtypes = []
    Timestamp_create.restype = POINTER(Timestamp)

# /usr/local/include/libiec61850/iec61850_common.h: 428
if _libs["/usr/local/lib/libiec61850.so"].has("Timestamp_createFromByteArray", "cdecl"):
    Timestamp_createFromByteArray = _libs["/usr/local/lib/libiec61850.so"].get("Timestamp_createFromByteArray", "cdecl")
    Timestamp_createFromByteArray.argtypes = [POINTER(uint8_t)]
    Timestamp_createFromByteArray.restype = POINTER(Timestamp)

# /usr/local/include/libiec61850/iec61850_common.h: 432
if _libs["/usr/local/lib/libiec61850.so"].has("Timestamp_destroy", "cdecl"):
    Timestamp_destroy = _libs["/usr/local/lib/libiec61850.so"].get("Timestamp_destroy", "cdecl")
    Timestamp_destroy.argtypes = [POINTER(Timestamp)]
    Timestamp_destroy.restype = None

# /usr/local/include/libiec61850/iec61850_common.h: 435
if _libs["/usr/local/lib/libiec61850.so"].has("Timestamp_clearFlags", "cdecl"):
    Timestamp_clearFlags = _libs["/usr/local/lib/libiec61850.so"].get("Timestamp_clearFlags", "cdecl")
    Timestamp_clearFlags.argtypes = [POINTER(Timestamp)]
    Timestamp_clearFlags.restype = None

# /usr/local/include/libiec61850/iec61850_common.h: 438
if _libs["/usr/local/lib/libiec61850.so"].has("Timestamp_getTimeInSeconds", "cdecl"):
    Timestamp_getTimeInSeconds = _libs["/usr/local/lib/libiec61850.so"].get("Timestamp_getTimeInSeconds", "cdecl")
    Timestamp_getTimeInSeconds.argtypes = [POINTER(Timestamp)]
    Timestamp_getTimeInSeconds.restype = uint32_t

# /usr/local/include/libiec61850/iec61850_common.h: 441
if _libs["/usr/local/lib/libiec61850.so"].has("Timestamp_getTimeInMs", "cdecl"):
    Timestamp_getTimeInMs = _libs["/usr/local/lib/libiec61850.so"].get("Timestamp_getTimeInMs", "cdecl")
    Timestamp_getTimeInMs.argtypes = [POINTER(Timestamp)]
    Timestamp_getTimeInMs.restype = msSinceEpoch

# /usr/local/include/libiec61850/iec61850_common.h: 444
if _libs["/usr/local/lib/libiec61850.so"].has("Timestamp_getTimeInNs", "cdecl"):
    Timestamp_getTimeInNs = _libs["/usr/local/lib/libiec61850.so"].get("Timestamp_getTimeInNs", "cdecl")
    Timestamp_getTimeInNs.argtypes = [POINTER(Timestamp)]
    Timestamp_getTimeInNs.restype = nsSinceEpoch

# /usr/local/include/libiec61850/iec61850_common.h: 447
if _libs["/usr/local/lib/libiec61850.so"].has("Timestamp_isLeapSecondKnown", "cdecl"):
    Timestamp_isLeapSecondKnown = _libs["/usr/local/lib/libiec61850.so"].get("Timestamp_isLeapSecondKnown", "cdecl")
    Timestamp_isLeapSecondKnown.argtypes = [POINTER(Timestamp)]
    Timestamp_isLeapSecondKnown.restype = c_bool

# /usr/local/include/libiec61850/iec61850_common.h: 450
if _libs["/usr/local/lib/libiec61850.so"].has("Timestamp_setLeapSecondKnown", "cdecl"):
    Timestamp_setLeapSecondKnown = _libs["/usr/local/lib/libiec61850.so"].get("Timestamp_setLeapSecondKnown", "cdecl")
    Timestamp_setLeapSecondKnown.argtypes = [POINTER(Timestamp), c_bool]
    Timestamp_setLeapSecondKnown.restype = None

# /usr/local/include/libiec61850/iec61850_common.h: 453
if _libs["/usr/local/lib/libiec61850.so"].has("Timestamp_hasClockFailure", "cdecl"):
    Timestamp_hasClockFailure = _libs["/usr/local/lib/libiec61850.so"].get("Timestamp_hasClockFailure", "cdecl")
    Timestamp_hasClockFailure.argtypes = [POINTER(Timestamp)]
    Timestamp_hasClockFailure.restype = c_bool

# /usr/local/include/libiec61850/iec61850_common.h: 456
if _libs["/usr/local/lib/libiec61850.so"].has("Timestamp_setClockFailure", "cdecl"):
    Timestamp_setClockFailure = _libs["/usr/local/lib/libiec61850.so"].get("Timestamp_setClockFailure", "cdecl")
    Timestamp_setClockFailure.argtypes = [POINTER(Timestamp), c_bool]
    Timestamp_setClockFailure.restype = None

# /usr/local/include/libiec61850/iec61850_common.h: 459
if _libs["/usr/local/lib/libiec61850.so"].has("Timestamp_isClockNotSynchronized", "cdecl"):
    Timestamp_isClockNotSynchronized = _libs["/usr/local/lib/libiec61850.so"].get("Timestamp_isClockNotSynchronized", "cdecl")
    Timestamp_isClockNotSynchronized.argtypes = [POINTER(Timestamp)]
    Timestamp_isClockNotSynchronized.restype = c_bool

# /usr/local/include/libiec61850/iec61850_common.h: 462
if _libs["/usr/local/lib/libiec61850.so"].has("Timestamp_setClockNotSynchronized", "cdecl"):
    Timestamp_setClockNotSynchronized = _libs["/usr/local/lib/libiec61850.so"].get("Timestamp_setClockNotSynchronized", "cdecl")
    Timestamp_setClockNotSynchronized.argtypes = [POINTER(Timestamp), c_bool]
    Timestamp_setClockNotSynchronized.restype = None

# /usr/local/include/libiec61850/iec61850_common.h: 465
if _libs["/usr/local/lib/libiec61850.so"].has("Timestamp_getSubsecondPrecision", "cdecl"):
    Timestamp_getSubsecondPrecision = _libs["/usr/local/lib/libiec61850.so"].get("Timestamp_getSubsecondPrecision", "cdecl")
    Timestamp_getSubsecondPrecision.argtypes = [POINTER(Timestamp)]
    Timestamp_getSubsecondPrecision.restype = c_int

# /usr/local/include/libiec61850/iec61850_common.h: 473
if _libs["/usr/local/lib/libiec61850.so"].has("Timestamp_setSubsecondPrecision", "cdecl"):
    Timestamp_setSubsecondPrecision = _libs["/usr/local/lib/libiec61850.so"].get("Timestamp_setSubsecondPrecision", "cdecl")
    Timestamp_setSubsecondPrecision.argtypes = [POINTER(Timestamp), c_int]
    Timestamp_setSubsecondPrecision.restype = None

# /usr/local/include/libiec61850/iec61850_common.h: 485
if _libs["/usr/local/lib/libiec61850.so"].has("Timestamp_setTimeInSeconds", "cdecl"):
    Timestamp_setTimeInSeconds = _libs["/usr/local/lib/libiec61850.so"].get("Timestamp_setTimeInSeconds", "cdecl")
    Timestamp_setTimeInSeconds.argtypes = [POINTER(Timestamp), uint32_t]
    Timestamp_setTimeInSeconds.restype = None

# /usr/local/include/libiec61850/iec61850_common.h: 496
if _libs["/usr/local/lib/libiec61850.so"].has("Timestamp_setTimeInMilliseconds", "cdecl"):
    Timestamp_setTimeInMilliseconds = _libs["/usr/local/lib/libiec61850.so"].get("Timestamp_setTimeInMilliseconds", "cdecl")
    Timestamp_setTimeInMilliseconds.argtypes = [POINTER(Timestamp), msSinceEpoch]
    Timestamp_setTimeInMilliseconds.restype = None

# /usr/local/include/libiec61850/iec61850_common.h: 507
if _libs["/usr/local/lib/libiec61850.so"].has("Timestamp_setTimeInNanoseconds", "cdecl"):
    Timestamp_setTimeInNanoseconds = _libs["/usr/local/lib/libiec61850.so"].get("Timestamp_setTimeInNanoseconds", "cdecl")
    Timestamp_setTimeInNanoseconds.argtypes = [POINTER(Timestamp), nsSinceEpoch]
    Timestamp_setTimeInNanoseconds.restype = None

# /usr/local/include/libiec61850/iec61850_common.h: 510
if _libs["/usr/local/lib/libiec61850.so"].has("Timestamp_setByMmsUtcTime", "cdecl"):
    Timestamp_setByMmsUtcTime = _libs["/usr/local/lib/libiec61850.so"].get("Timestamp_setByMmsUtcTime", "cdecl")
    Timestamp_setByMmsUtcTime.argtypes = [POINTER(Timestamp), POINTER(MmsValue)]
    Timestamp_setByMmsUtcTime.restype = None

# /usr/local/include/libiec61850/iec61850_common.h: 518
if _libs["/usr/local/lib/libiec61850.so"].has("Timestamp_toMmsValue", "cdecl"):
    Timestamp_toMmsValue = _libs["/usr/local/lib/libiec61850.so"].get("Timestamp_toMmsValue", "cdecl")
    Timestamp_toMmsValue.argtypes = [POINTER(Timestamp), POINTER(MmsValue)]
    Timestamp_toMmsValue.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/iec61850_common.h: 529
if _libs["/usr/local/lib/libiec61850.so"].has("Timestamp_fromMmsValue", "cdecl"):
    Timestamp_fromMmsValue = _libs["/usr/local/lib/libiec61850.so"].get("Timestamp_fromMmsValue", "cdecl")
    Timestamp_fromMmsValue.argtypes = [POINTER(Timestamp), POINTER(MmsValue)]
    Timestamp_fromMmsValue.restype = POINTER(Timestamp)

# /usr/local/include/libiec61850/iec61850_common.h: 537
if _libs["/usr/local/lib/libiec61850.so"].has("LibIEC61850_getVersionString", "cdecl"):
    LibIEC61850_getVersionString = _libs["/usr/local/lib/libiec61850.so"].get("LibIEC61850_getVersionString", "cdecl")
    LibIEC61850_getVersionString.argtypes = []
    if sizeof(c_int) == sizeof(c_void_p):
        LibIEC61850_getVersionString.restype = ReturnString
    else:
        LibIEC61850_getVersionString.restype = String
        LibIEC61850_getVersionString.errcheck = ReturnString

# /usr/local/include/libiec61850/mms_type_spec.h: 56
if _libs["/usr/local/lib/libiec61850.so"].has("MmsVariableSpecification_destroy", "cdecl"):
    MmsVariableSpecification_destroy = _libs["/usr/local/lib/libiec61850.so"].get("MmsVariableSpecification_destroy", "cdecl")
    MmsVariableSpecification_destroy.argtypes = [POINTER(MmsVariableSpecification)]
    MmsVariableSpecification_destroy.restype = None

# /usr/local/include/libiec61850/mms_type_spec.h: 71
if _libs["/usr/local/lib/libiec61850.so"].has("MmsVariableSpecification_getChildValue", "cdecl"):
    MmsVariableSpecification_getChildValue = _libs["/usr/local/lib/libiec61850.so"].get("MmsVariableSpecification_getChildValue", "cdecl")
    MmsVariableSpecification_getChildValue.argtypes = [POINTER(MmsVariableSpecification), POINTER(MmsValue), String]
    MmsVariableSpecification_getChildValue.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_type_spec.h: 82
if _libs["/usr/local/lib/libiec61850.so"].has("MmsVariableSpecification_getNamedVariableRecursive", "cdecl"):
    MmsVariableSpecification_getNamedVariableRecursive = _libs["/usr/local/lib/libiec61850.so"].get("MmsVariableSpecification_getNamedVariableRecursive", "cdecl")
    MmsVariableSpecification_getNamedVariableRecursive.argtypes = [POINTER(MmsVariableSpecification), String]
    MmsVariableSpecification_getNamedVariableRecursive.restype = POINTER(MmsVariableSpecification)

# /usr/local/include/libiec61850/mms_type_spec.h: 93
if _libs["/usr/local/lib/libiec61850.so"].has("MmsVariableSpecification_getType", "cdecl"):
    MmsVariableSpecification_getType = _libs["/usr/local/lib/libiec61850.so"].get("MmsVariableSpecification_getType", "cdecl")
    MmsVariableSpecification_getType.argtypes = [POINTER(MmsVariableSpecification)]
    MmsVariableSpecification_getType.restype = MmsType

# /usr/local/include/libiec61850/mms_type_spec.h: 104
if _libs["/usr/local/lib/libiec61850.so"].has("MmsVariableSpecification_isValueOfType", "cdecl"):
    MmsVariableSpecification_isValueOfType = _libs["/usr/local/lib/libiec61850.so"].get("MmsVariableSpecification_isValueOfType", "cdecl")
    MmsVariableSpecification_isValueOfType.argtypes = [POINTER(MmsVariableSpecification), POINTER(MmsValue)]
    MmsVariableSpecification_isValueOfType.restype = c_bool

# /usr/local/include/libiec61850/mms_type_spec.h: 116
if _libs["/usr/local/lib/libiec61850.so"].has("MmsVariableSpecification_getName", "cdecl"):
    MmsVariableSpecification_getName = _libs["/usr/local/lib/libiec61850.so"].get("MmsVariableSpecification_getName", "cdecl")
    MmsVariableSpecification_getName.argtypes = [POINTER(MmsVariableSpecification)]
    MmsVariableSpecification_getName.restype = c_char_p

# /usr/local/include/libiec61850/mms_type_spec.h: 120
if _libs["/usr/local/lib/libiec61850.so"].has("MmsVariableSpecification_getStructureElements", "cdecl"):
    MmsVariableSpecification_getStructureElements = _libs["/usr/local/lib/libiec61850.so"].get("MmsVariableSpecification_getStructureElements", "cdecl")
    MmsVariableSpecification_getStructureElements.argtypes = [POINTER(MmsVariableSpecification)]
    MmsVariableSpecification_getStructureElements.restype = LinkedList

# /usr/local/include/libiec61850/mms_type_spec.h: 133
if _libs["/usr/local/lib/libiec61850.so"].has("MmsVariableSpecification_getSize", "cdecl"):
    MmsVariableSpecification_getSize = _libs["/usr/local/lib/libiec61850.so"].get("MmsVariableSpecification_getSize", "cdecl")
    MmsVariableSpecification_getSize.argtypes = [POINTER(MmsVariableSpecification)]
    MmsVariableSpecification_getSize.restype = c_int

# /usr/local/include/libiec61850/mms_type_spec.h: 135
if _libs["/usr/local/lib/libiec61850.so"].has("MmsVariableSpecification_getChildSpecificationByIndex", "cdecl"):
    MmsVariableSpecification_getChildSpecificationByIndex = _libs["/usr/local/lib/libiec61850.so"].get("MmsVariableSpecification_getChildSpecificationByIndex", "cdecl")
    MmsVariableSpecification_getChildSpecificationByIndex.argtypes = [POINTER(MmsVariableSpecification), c_int]
    MmsVariableSpecification_getChildSpecificationByIndex.restype = POINTER(MmsVariableSpecification)

# /usr/local/include/libiec61850/mms_type_spec.h: 147
if _libs["/usr/local/lib/libiec61850.so"].has("MmsVariableSpecification_getChildSpecificationByName", "cdecl"):
    MmsVariableSpecification_getChildSpecificationByName = _libs["/usr/local/lib/libiec61850.so"].get("MmsVariableSpecification_getChildSpecificationByName", "cdecl")
    MmsVariableSpecification_getChildSpecificationByName.argtypes = [POINTER(MmsVariableSpecification), String, POINTER(c_int)]
    MmsVariableSpecification_getChildSpecificationByName.restype = POINTER(MmsVariableSpecification)

# /usr/local/include/libiec61850/mms_type_spec.h: 150
if _libs["/usr/local/lib/libiec61850.so"].has("MmsVariableSpecification_getArrayElementSpecification", "cdecl"):
    MmsVariableSpecification_getArrayElementSpecification = _libs["/usr/local/lib/libiec61850.so"].get("MmsVariableSpecification_getArrayElementSpecification", "cdecl")
    MmsVariableSpecification_getArrayElementSpecification.argtypes = [POINTER(MmsVariableSpecification)]
    MmsVariableSpecification_getArrayElementSpecification.restype = POINTER(MmsVariableSpecification)

# /usr/local/include/libiec61850/mms_type_spec.h: 154
if _libs["/usr/local/lib/libiec61850.so"].has("MmsVariableSpecification_getExponentWidth", "cdecl"):
    MmsVariableSpecification_getExponentWidth = _libs["/usr/local/lib/libiec61850.so"].get("MmsVariableSpecification_getExponentWidth", "cdecl")
    MmsVariableSpecification_getExponentWidth.argtypes = [POINTER(MmsVariableSpecification)]
    MmsVariableSpecification_getExponentWidth.restype = c_int

enum_anon_35 = c_int# /usr/local/include/libiec61850/iso_connection_parameters.h: 55

ACSE_AUTH_NONE = 0# /usr/local/include/libiec61850/iso_connection_parameters.h: 55

ACSE_AUTH_PASSWORD = 1# /usr/local/include/libiec61850/iso_connection_parameters.h: 55

ACSE_AUTH_CERTIFICATE = 2# /usr/local/include/libiec61850/iso_connection_parameters.h: 55

ACSE_AUTH_TLS = 3# /usr/local/include/libiec61850/iso_connection_parameters.h: 55

AcseAuthenticationMechanism = enum_anon_35# /usr/local/include/libiec61850/iso_connection_parameters.h: 55

# /usr/local/include/libiec61850/iso_connection_parameters.h: 60
class struct_sAcseAuthenticationParameter(Structure):
    pass

AcseAuthenticationParameter = POINTER(struct_sAcseAuthenticationParameter)# /usr/local/include/libiec61850/iso_connection_parameters.h: 58

# /usr/local/include/libiec61850/iso_connection_parameters.h: 66
class struct_anon_36(Structure):
    pass

struct_anon_36.__slots__ = [
    'octetString',
    'passwordLength',
]
struct_anon_36._fields_ = [
    ('octetString', POINTER(uint8_t)),
    ('passwordLength', c_int),
]

# /usr/local/include/libiec61850/iso_connection_parameters.h: 72
class struct_anon_37(Structure):
    pass

struct_anon_37.__slots__ = [
    'buf',
    'length',
]
struct_anon_37._fields_ = [
    ('buf', POINTER(uint8_t)),
    ('length', c_int),
]

# /usr/local/include/libiec61850/iso_connection_parameters.h: 64
class union_anon_38(Union):
    pass

union_anon_38.__slots__ = [
    'password',
    'certificate',
]
union_anon_38._fields_ = [
    ('password', struct_anon_36),
    ('certificate', struct_anon_37),
]

struct_sAcseAuthenticationParameter.__slots__ = [
    'mechanism',
    'value',
]
struct_sAcseAuthenticationParameter._fields_ = [
    ('mechanism', AcseAuthenticationMechanism),
    ('value', union_anon_38),
]

# /usr/local/include/libiec61850/iso_connection_parameters.h: 82
if _libs["/usr/local/lib/libiec61850.so"].has("AcseAuthenticationParameter_create", "cdecl"):
    AcseAuthenticationParameter_create = _libs["/usr/local/lib/libiec61850.so"].get("AcseAuthenticationParameter_create", "cdecl")
    AcseAuthenticationParameter_create.argtypes = []
    AcseAuthenticationParameter_create.restype = AcseAuthenticationParameter

# /usr/local/include/libiec61850/iso_connection_parameters.h: 85
if _libs["/usr/local/lib/libiec61850.so"].has("AcseAuthenticationParameter_destroy", "cdecl"):
    AcseAuthenticationParameter_destroy = _libs["/usr/local/lib/libiec61850.so"].get("AcseAuthenticationParameter_destroy", "cdecl")
    AcseAuthenticationParameter_destroy.argtypes = [AcseAuthenticationParameter]
    AcseAuthenticationParameter_destroy.restype = None

# /usr/local/include/libiec61850/iso_connection_parameters.h: 88
if _libs["/usr/local/lib/libiec61850.so"].has("AcseAuthenticationParameter_setAuthMechanism", "cdecl"):
    AcseAuthenticationParameter_setAuthMechanism = _libs["/usr/local/lib/libiec61850.so"].get("AcseAuthenticationParameter_setAuthMechanism", "cdecl")
    AcseAuthenticationParameter_setAuthMechanism.argtypes = [AcseAuthenticationParameter, AcseAuthenticationMechanism]
    AcseAuthenticationParameter_setAuthMechanism.restype = None

# /usr/local/include/libiec61850/iso_connection_parameters.h: 91
if _libs["/usr/local/lib/libiec61850.so"].has("AcseAuthenticationParameter_setPassword", "cdecl"):
    AcseAuthenticationParameter_setPassword = _libs["/usr/local/lib/libiec61850.so"].get("AcseAuthenticationParameter_setPassword", "cdecl")
    AcseAuthenticationParameter_setPassword.argtypes = [AcseAuthenticationParameter, String]
    AcseAuthenticationParameter_setPassword.restype = None

AcseAuthenticator = CFUNCTYPE(UNCHECKED(c_bool), POINTER(None), AcseAuthenticationParameter, POINTER(POINTER(None)), POINTER(IsoApplicationReference))# /usr/local/include/libiec61850/iso_connection_parameters.h: 105

# /usr/local/include/libiec61850/iso_connection_parameters.h: 115
class struct_anon_39(Structure):
    pass

struct_anon_39.__slots__ = [
    'size',
    'value',
]
struct_anon_39._fields_ = [
    ('size', uint8_t),
    ('value', uint8_t * int(4)),
]

TSelector = struct_anon_39# /usr/local/include/libiec61850/iso_connection_parameters.h: 115

# /usr/local/include/libiec61850/iso_connection_parameters.h: 125
class struct_anon_40(Structure):
    pass

struct_anon_40.__slots__ = [
    'size',
    'value',
]
struct_anon_40._fields_ = [
    ('size', uint8_t),
    ('value', uint8_t * int(16)),
]

SSelector = struct_anon_40# /usr/local/include/libiec61850/iso_connection_parameters.h: 125

# /usr/local/include/libiec61850/iso_connection_parameters.h: 135
class struct_anon_41(Structure):
    pass

struct_anon_41.__slots__ = [
    'size',
    'value',
]
struct_anon_41._fields_ = [
    ('size', uint8_t),
    ('value', uint8_t * int(16)),
]

PSelector = struct_anon_41# /usr/local/include/libiec61850/iso_connection_parameters.h: 135

# /usr/local/include/libiec61850/iso_connection_parameters.h: 137
class struct_sIsoConnectionParameters(Structure):
    pass

struct_sIsoConnectionParameters.__slots__ = [
    'acseAuthParameter',
    'hostname',
    'tcpPort',
    'localIpAddress',
    'localTcpPort',
    'remoteApTitle',
    'remoteApTitleLen',
    'remoteAEQualifier',
    'remotePSelector',
    'remoteSSelector',
    'remoteTSelector',
    'localApTitle',
    'localApTitleLen',
    'localAEQualifier',
    'localPSelector',
    'localSSelector',
    'localTSelector',
]
struct_sIsoConnectionParameters._fields_ = [
    ('acseAuthParameter', AcseAuthenticationParameter),
    ('hostname', String),
    ('tcpPort', c_int),
    ('localIpAddress', String),
    ('localTcpPort', c_int),
    ('remoteApTitle', uint8_t * int(10)),
    ('remoteApTitleLen', c_int),
    ('remoteAEQualifier', c_int),
    ('remotePSelector', PSelector),
    ('remoteSSelector', SSelector),
    ('remoteTSelector', TSelector),
    ('localApTitle', uint8_t * int(10)),
    ('localApTitleLen', c_int),
    ('localAEQualifier', c_int),
    ('localPSelector', PSelector),
    ('localSSelector', SSelector),
    ('localTSelector', TSelector),
]

IsoConnectionParameters = POINTER(struct_sIsoConnectionParameters)# /usr/local/include/libiec61850/iso_connection_parameters.h: 168

# /usr/local/include/libiec61850/iso_connection_parameters.h: 179
if _libs["/usr/local/lib/libiec61850.so"].has("IsoConnectionParameters_create", "cdecl"):
    IsoConnectionParameters_create = _libs["/usr/local/lib/libiec61850.so"].get("IsoConnectionParameters_create", "cdecl")
    IsoConnectionParameters_create.argtypes = []
    IsoConnectionParameters_create.restype = IsoConnectionParameters

# /usr/local/include/libiec61850/iso_connection_parameters.h: 190
if _libs["/usr/local/lib/libiec61850.so"].has("IsoConnectionParameters_destroy", "cdecl"):
    IsoConnectionParameters_destroy = _libs["/usr/local/lib/libiec61850.so"].get("IsoConnectionParameters_destroy", "cdecl")
    IsoConnectionParameters_destroy.argtypes = [IsoConnectionParameters]
    IsoConnectionParameters_destroy.restype = None

# /usr/local/include/libiec61850/iso_connection_parameters.h: 194
if _libs["/usr/local/lib/libiec61850.so"].has("IsoConnectionParameters_setTlsConfiguration", "cdecl"):
    IsoConnectionParameters_setTlsConfiguration = _libs["/usr/local/lib/libiec61850.so"].get("IsoConnectionParameters_setTlsConfiguration", "cdecl")
    IsoConnectionParameters_setTlsConfiguration.argtypes = [IsoConnectionParameters, TLSConfiguration]
    IsoConnectionParameters_setTlsConfiguration.restype = None

# /usr/local/include/libiec61850/iso_connection_parameters.h: 205
if _libs["/usr/local/lib/libiec61850.so"].has("IsoConnectionParameters_setAcseAuthenticationParameter", "cdecl"):
    IsoConnectionParameters_setAcseAuthenticationParameter = _libs["/usr/local/lib/libiec61850.so"].get("IsoConnectionParameters_setAcseAuthenticationParameter", "cdecl")
    IsoConnectionParameters_setAcseAuthenticationParameter.argtypes = [IsoConnectionParameters, AcseAuthenticationParameter]
    IsoConnectionParameters_setAcseAuthenticationParameter.restype = None

# /usr/local/include/libiec61850/iso_connection_parameters.h: 219
if _libs["/usr/local/lib/libiec61850.so"].has("IsoConnectionParameters_setTcpParameters", "cdecl"):
    IsoConnectionParameters_setTcpParameters = _libs["/usr/local/lib/libiec61850.so"].get("IsoConnectionParameters_setTcpParameters", "cdecl")
    IsoConnectionParameters_setTcpParameters.argtypes = [IsoConnectionParameters, String, c_int]
    IsoConnectionParameters_setTcpParameters.restype = None

# /usr/local/include/libiec61850/iso_connection_parameters.h: 232
if _libs["/usr/local/lib/libiec61850.so"].has("IsoConnectionParameters_setLocalTcpParameters", "cdecl"):
    IsoConnectionParameters_setLocalTcpParameters = _libs["/usr/local/lib/libiec61850.so"].get("IsoConnectionParameters_setLocalTcpParameters", "cdecl")
    IsoConnectionParameters_setLocalTcpParameters.argtypes = [IsoConnectionParameters, String, c_int]
    IsoConnectionParameters_setLocalTcpParameters.restype = None

# /usr/local/include/libiec61850/iso_connection_parameters.h: 248
if _libs["/usr/local/lib/libiec61850.so"].has("IsoConnectionParameters_setRemoteApTitle", "cdecl"):
    IsoConnectionParameters_setRemoteApTitle = _libs["/usr/local/lib/libiec61850.so"].get("IsoConnectionParameters_setRemoteApTitle", "cdecl")
    IsoConnectionParameters_setRemoteApTitle.argtypes = [IsoConnectionParameters, String, c_int]
    IsoConnectionParameters_setRemoteApTitle.restype = None

# /usr/local/include/libiec61850/iso_connection_parameters.h: 263
if _libs["/usr/local/lib/libiec61850.so"].has("IsoConnectionParameters_setRemoteAddresses", "cdecl"):
    IsoConnectionParameters_setRemoteAddresses = _libs["/usr/local/lib/libiec61850.so"].get("IsoConnectionParameters_setRemoteAddresses", "cdecl")
    IsoConnectionParameters_setRemoteAddresses.argtypes = [IsoConnectionParameters, PSelector, SSelector, TSelector]
    IsoConnectionParameters_setRemoteAddresses.restype = None

# /usr/local/include/libiec61850/iso_connection_parameters.h: 278
if _libs["/usr/local/lib/libiec61850.so"].has("IsoConnectionParameters_setLocalApTitle", "cdecl"):
    IsoConnectionParameters_setLocalApTitle = _libs["/usr/local/lib/libiec61850.so"].get("IsoConnectionParameters_setLocalApTitle", "cdecl")
    IsoConnectionParameters_setLocalApTitle.argtypes = [IsoConnectionParameters, String, c_int]
    IsoConnectionParameters_setLocalApTitle.restype = None

# /usr/local/include/libiec61850/iso_connection_parameters.h: 293
if _libs["/usr/local/lib/libiec61850.so"].has("IsoConnectionParameters_setLocalAddresses", "cdecl"):
    IsoConnectionParameters_setLocalAddresses = _libs["/usr/local/lib/libiec61850.so"].get("IsoConnectionParameters_setLocalAddresses", "cdecl")
    IsoConnectionParameters_setLocalAddresses.argtypes = [IsoConnectionParameters, PSelector, SSelector, TSelector]
    IsoConnectionParameters_setLocalAddresses.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 54
class struct_sMmsConnectionParameters(Structure):
    pass

struct_sMmsConnectionParameters.__slots__ = [
    'maxServOutstandingCalling',
    'maxServOutstandingCalled',
    'dataStructureNestingLevel',
    'maxPduSize',
    'servicesSupported',
]
struct_sMmsConnectionParameters._fields_ = [
    ('maxServOutstandingCalling', c_int),
    ('maxServOutstandingCalled', c_int),
    ('dataStructureNestingLevel', c_int),
    ('maxPduSize', c_int),
    ('servicesSupported', uint8_t * int(11)),
]

MmsConnectionParameters = struct_sMmsConnectionParameters# /usr/local/include/libiec61850/mms_client_connection.h: 54

# /usr/local/include/libiec61850/mms_client_connection.h: 60
class struct_anon_42(Structure):
    pass

struct_anon_42.__slots__ = [
    'vendorName',
    'modelName',
    'revision',
]
struct_anon_42._fields_ = [
    ('vendorName', String),
    ('modelName', String),
    ('revision', String),
]

MmsServerIdentity = struct_anon_42# /usr/local/include/libiec61850/mms_client_connection.h: 60

enum_anon_43 = c_int# /usr/local/include/libiec61850/mms_client_connection.h: 67

MMS_CONNECTION_STATE_CLOSED = 0# /usr/local/include/libiec61850/mms_client_connection.h: 67

MMS_CONNECTION_STATE_CONNECTING = (MMS_CONNECTION_STATE_CLOSED + 1)# /usr/local/include/libiec61850/mms_client_connection.h: 67

MMS_CONNECTION_STATE_CONNECTED = (MMS_CONNECTION_STATE_CONNECTING + 1)# /usr/local/include/libiec61850/mms_client_connection.h: 67

MMS_CONNECTION_STATE_CLOSING = (MMS_CONNECTION_STATE_CONNECTED + 1)# /usr/local/include/libiec61850/mms_client_connection.h: 67

MmsConnectionState = enum_anon_43# /usr/local/include/libiec61850/mms_client_connection.h: 67

MmsInformationReportHandler = CFUNCTYPE(UNCHECKED(None), POINTER(None), String, String, POINTER(MmsValue), c_bool)# /usr/local/include/libiec61850/mms_client_connection.h: 69

# /usr/local/include/libiec61850/mms_client_connection.h: 75
class struct_sMmsConnection(Structure):
    pass

MmsConnection = POINTER(struct_sMmsConnection)# /usr/local/include/libiec61850/mms_client_connection.h: 75

# /usr/local/include/libiec61850/mms_client_connection.h: 88
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_create", "cdecl"):
    MmsConnection_create = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_create", "cdecl")
    MmsConnection_create.argtypes = []
    MmsConnection_create.restype = MmsConnection

# /usr/local/include/libiec61850/mms_client_connection.h: 98
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_createSecure", "cdecl"):
    MmsConnection_createSecure = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_createSecure", "cdecl")
    MmsConnection_createSecure.argtypes = [TLSConfiguration]
    MmsConnection_createSecure.restype = MmsConnection

# /usr/local/include/libiec61850/mms_client_connection.h: 112
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_createNonThreaded", "cdecl"):
    MmsConnection_createNonThreaded = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_createNonThreaded", "cdecl")
    MmsConnection_createNonThreaded.argtypes = [TLSConfiguration]
    MmsConnection_createNonThreaded.restype = MmsConnection

MmsRawMessageHandler = CFUNCTYPE(UNCHECKED(None), POINTER(None), POINTER(uint8_t), c_int, c_bool)# /usr/local/include/libiec61850/mms_client_connection.h: 125

# /usr/local/include/libiec61850/mms_client_connection.h: 139
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_setRawMessageHandler", "cdecl"):
    MmsConnection_setRawMessageHandler = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_setRawMessageHandler", "cdecl")
    MmsConnection_setRawMessageHandler.argtypes = [MmsConnection, MmsRawMessageHandler, POINTER(None)]
    MmsConnection_setRawMessageHandler.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 152
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_setFilestoreBasepath", "cdecl"):
    MmsConnection_setFilestoreBasepath = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_setFilestoreBasepath", "cdecl")
    MmsConnection_setFilestoreBasepath.argtypes = [MmsConnection, String]
    MmsConnection_setFilestoreBasepath.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 161
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_setRequestTimeout", "cdecl"):
    MmsConnection_setRequestTimeout = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_setRequestTimeout", "cdecl")
    MmsConnection_setRequestTimeout.argtypes = [MmsConnection, uint32_t]
    MmsConnection_setRequestTimeout.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 171
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_getRequestTimeout", "cdecl"):
    MmsConnection_getRequestTimeout = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_getRequestTimeout", "cdecl")
    MmsConnection_getRequestTimeout.argtypes = [MmsConnection]
    MmsConnection_getRequestTimeout.restype = uint32_t

# /usr/local/include/libiec61850/mms_client_connection.h: 180
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_setConnectTimeout", "cdecl"):
    MmsConnection_setConnectTimeout = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_setConnectTimeout", "cdecl")
    MmsConnection_setConnectTimeout.argtypes = [MmsConnection, uint32_t]
    MmsConnection_setConnectTimeout.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 194
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_setInformationReportHandler", "cdecl"):
    MmsConnection_setInformationReportHandler = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_setInformationReportHandler", "cdecl")
    MmsConnection_setInformationReportHandler.argtypes = [MmsConnection, MmsInformationReportHandler, POINTER(None)]
    MmsConnection_setInformationReportHandler.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 204
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_getIsoConnectionParameters", "cdecl"):
    MmsConnection_getIsoConnectionParameters = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_getIsoConnectionParameters", "cdecl")
    MmsConnection_getIsoConnectionParameters.argtypes = [MmsConnection]
    MmsConnection_getIsoConnectionParameters.restype = IsoConnectionParameters

# /usr/local/include/libiec61850/mms_client_connection.h: 213
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_getMmsConnectionParameters", "cdecl"):
    MmsConnection_getMmsConnectionParameters = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_getMmsConnectionParameters", "cdecl")
    MmsConnection_getMmsConnectionParameters.argtypes = [MmsConnection]
    MmsConnection_getMmsConnectionParameters.restype = MmsConnectionParameters

MmsConnectionStateChangedHandler = CFUNCTYPE(UNCHECKED(None), MmsConnection, POINTER(None), MmsConnectionState)# /usr/local/include/libiec61850/mms_client_connection.h: 215

# /usr/local/include/libiec61850/mms_client_connection.h: 218
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_setConnectionStateChangedHandler", "cdecl"):
    MmsConnection_setConnectionStateChangedHandler = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_setConnectionStateChangedHandler", "cdecl")
    MmsConnection_setConnectionStateChangedHandler.argtypes = [MmsConnection, MmsConnectionStateChangedHandler, POINTER(None)]
    MmsConnection_setConnectionStateChangedHandler.restype = None

MmsConnectionLostHandler = CFUNCTYPE(UNCHECKED(None), MmsConnection, POINTER(None))# /usr/local/include/libiec61850/mms_client_connection.h: 226

# /usr/local/include/libiec61850/mms_client_connection.h: 235
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_setConnectionLostHandler", "cdecl"):
    MmsConnection_setConnectionLostHandler = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_setConnectionLostHandler", "cdecl")
    MmsConnection_setConnectionLostHandler.argtypes = [MmsConnection, MmsConnectionLostHandler, POINTER(None)]
    MmsConnection_setConnectionLostHandler.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 244
for _lib in _libs.values():
    if not _lib.has("MmsConnection_setIsoConnectionParameters", "cdecl"):
        continue
    MmsConnection_setIsoConnectionParameters = _lib.get("MmsConnection_setIsoConnectionParameters", "cdecl")
    MmsConnection_setIsoConnectionParameters.argtypes = [MmsConnection, POINTER(IsoConnectionParameters)]
    MmsConnection_setIsoConnectionParameters.restype = None
    break

# /usr/local/include/libiec61850/mms_client_connection.h: 252
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_destroy", "cdecl"):
    MmsConnection_destroy = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_destroy", "cdecl")
    MmsConnection_destroy.argtypes = [MmsConnection]
    MmsConnection_destroy.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 272
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_connect", "cdecl"):
    MmsConnection_connect = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_connect", "cdecl")
    MmsConnection_connect.argtypes = [MmsConnection, POINTER(MmsError), String, c_int]
    MmsConnection_connect.restype = c_bool

# /usr/local/include/libiec61850/mms_client_connection.h: 275
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_connectAsync", "cdecl"):
    MmsConnection_connectAsync = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_connectAsync", "cdecl")
    MmsConnection_connectAsync.argtypes = [MmsConnection, POINTER(MmsError), String, c_int]
    MmsConnection_connectAsync.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 286
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_tick", "cdecl"):
    MmsConnection_tick = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_tick", "cdecl")
    MmsConnection_tick.argtypes = [MmsConnection]
    MmsConnection_tick.restype = c_bool

# /usr/local/include/libiec61850/mms_client_connection.h: 290
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_sendRawData", "cdecl"):
    MmsConnection_sendRawData = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_sendRawData", "cdecl")
    MmsConnection_sendRawData.argtypes = [MmsConnection, POINTER(MmsError), POINTER(uint8_t), c_int]
    MmsConnection_sendRawData.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 301
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_close", "cdecl"):
    MmsConnection_close = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_close", "cdecl")
    MmsConnection_close.argtypes = [MmsConnection]
    MmsConnection_close.restype = None

MmsConnection_ConcludeAbortHandler = CFUNCTYPE(UNCHECKED(None), POINTER(None), MmsError, c_bool)# /usr/local/include/libiec61850/mms_client_connection.h: 304

# /usr/local/include/libiec61850/mms_client_connection.h: 318
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_abort", "cdecl"):
    MmsConnection_abort = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_abort", "cdecl")
    MmsConnection_abort.argtypes = [MmsConnection, POINTER(MmsError)]
    MmsConnection_abort.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 321
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_abortAsync", "cdecl"):
    MmsConnection_abortAsync = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_abortAsync", "cdecl")
    MmsConnection_abortAsync.argtypes = [MmsConnection, POINTER(MmsError)]
    MmsConnection_abortAsync.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 335
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_conclude", "cdecl"):
    MmsConnection_conclude = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_conclude", "cdecl")
    MmsConnection_conclude.argtypes = [MmsConnection, POINTER(MmsError)]
    MmsConnection_conclude.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 338
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_concludeAsync", "cdecl"):
    MmsConnection_concludeAsync = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_concludeAsync", "cdecl")
    MmsConnection_concludeAsync.argtypes = [MmsConnection, POINTER(MmsError), MmsConnection_ConcludeAbortHandler, POINTER(None)]
    MmsConnection_concludeAsync.restype = None

MmsConnection_GenericServiceHandler = CFUNCTYPE(UNCHECKED(None), uint32_t, POINTER(None), MmsError, c_bool)# /usr/local/include/libiec61850/mms_client_connection.h: 341

MmsConnection_GetNameListHandler = CFUNCTYPE(UNCHECKED(None), uint32_t, POINTER(None), MmsError, LinkedList, c_bool)# /usr/local/include/libiec61850/mms_client_connection.h: 344

# /usr/local/include/libiec61850/mms_client_connection.h: 357
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_getVMDVariableNames", "cdecl"):
    MmsConnection_getVMDVariableNames = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_getVMDVariableNames", "cdecl")
    MmsConnection_getVMDVariableNames.argtypes = [MmsConnection, POINTER(MmsError)]
    MmsConnection_getVMDVariableNames.restype = LinkedList

# /usr/local/include/libiec61850/mms_client_connection.h: 360
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_getVMDVariableNamesAsync", "cdecl"):
    MmsConnection_getVMDVariableNamesAsync = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_getVMDVariableNamesAsync", "cdecl")
    MmsConnection_getVMDVariableNamesAsync.argtypes = [MmsConnection, POINTER(uint32_t), POINTER(MmsError), String, MmsConnection_GetNameListHandler, POINTER(None)]
    MmsConnection_getVMDVariableNamesAsync.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 375
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_getDomainNames", "cdecl"):
    MmsConnection_getDomainNames = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_getDomainNames", "cdecl")
    MmsConnection_getDomainNames.argtypes = [MmsConnection, POINTER(MmsError)]
    MmsConnection_getDomainNames.restype = LinkedList

# /usr/local/include/libiec61850/mms_client_connection.h: 389
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_getDomainNamesAsync", "cdecl"):
    MmsConnection_getDomainNamesAsync = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_getDomainNamesAsync", "cdecl")
    MmsConnection_getDomainNamesAsync.argtypes = [MmsConnection, POINTER(uint32_t), POINTER(MmsError), String, LinkedList, MmsConnection_GetNameListHandler, POINTER(None)]
    MmsConnection_getDomainNamesAsync.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 404
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_getDomainVariableNames", "cdecl"):
    MmsConnection_getDomainVariableNames = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_getDomainVariableNames", "cdecl")
    MmsConnection_getDomainVariableNames.argtypes = [MmsConnection, POINTER(MmsError), String]
    MmsConnection_getDomainVariableNames.restype = LinkedList

# /usr/local/include/libiec61850/mms_client_connection.h: 421
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_getDomainVariableNamesAsync", "cdecl"):
    MmsConnection_getDomainVariableNamesAsync = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_getDomainVariableNamesAsync", "cdecl")
    MmsConnection_getDomainVariableNamesAsync.argtypes = [MmsConnection, POINTER(uint32_t), POINTER(MmsError), String, String, LinkedList, MmsConnection_GetNameListHandler, POINTER(None)]
    MmsConnection_getDomainVariableNamesAsync.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 436
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_getDomainVariableListNames", "cdecl"):
    MmsConnection_getDomainVariableListNames = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_getDomainVariableListNames", "cdecl")
    MmsConnection_getDomainVariableListNames.argtypes = [MmsConnection, POINTER(MmsError), String]
    MmsConnection_getDomainVariableListNames.restype = LinkedList

# /usr/local/include/libiec61850/mms_client_connection.h: 439
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_getDomainVariableListNamesAsync", "cdecl"):
    MmsConnection_getDomainVariableListNamesAsync = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_getDomainVariableListNamesAsync", "cdecl")
    MmsConnection_getDomainVariableListNamesAsync.argtypes = [MmsConnection, POINTER(uint32_t), POINTER(MmsError), String, String, LinkedList, MmsConnection_GetNameListHandler, POINTER(None)]
    MmsConnection_getDomainVariableListNamesAsync.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 454
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_getDomainJournals", "cdecl"):
    MmsConnection_getDomainJournals = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_getDomainJournals", "cdecl")
    MmsConnection_getDomainJournals.argtypes = [MmsConnection, POINTER(MmsError), String]
    MmsConnection_getDomainJournals.restype = LinkedList

# /usr/local/include/libiec61850/mms_client_connection.h: 457
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_getDomainJournalsAsync", "cdecl"):
    MmsConnection_getDomainJournalsAsync = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_getDomainJournalsAsync", "cdecl")
    MmsConnection_getDomainJournalsAsync.argtypes = [MmsConnection, POINTER(uint32_t), POINTER(MmsError), String, String, MmsConnection_GetNameListHandler, POINTER(None)]
    MmsConnection_getDomainJournalsAsync.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 471
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_getVariableListNamesAssociationSpecific", "cdecl"):
    MmsConnection_getVariableListNamesAssociationSpecific = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_getVariableListNamesAssociationSpecific", "cdecl")
    MmsConnection_getVariableListNamesAssociationSpecific.argtypes = [MmsConnection, POINTER(MmsError)]
    MmsConnection_getVariableListNamesAssociationSpecific.restype = LinkedList

# /usr/local/include/libiec61850/mms_client_connection.h: 474
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_getVariableListNamesAssociationSpecificAsync", "cdecl"):
    MmsConnection_getVariableListNamesAssociationSpecificAsync = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_getVariableListNamesAssociationSpecificAsync", "cdecl")
    MmsConnection_getVariableListNamesAssociationSpecificAsync.argtypes = [MmsConnection, POINTER(uint32_t), POINTER(MmsError), String, MmsConnection_GetNameListHandler, POINTER(None)]
    MmsConnection_getVariableListNamesAssociationSpecificAsync.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 490
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_readVariable", "cdecl"):
    MmsConnection_readVariable = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_readVariable", "cdecl")
    MmsConnection_readVariable.argtypes = [MmsConnection, POINTER(MmsError), String, String]
    MmsConnection_readVariable.restype = POINTER(MmsValue)

MmsConnection_ReadVariableHandler = CFUNCTYPE(UNCHECKED(None), uint32_t, POINTER(None), MmsError, POINTER(MmsValue))# /usr/local/include/libiec61850/mms_client_connection.h: 495

# /usr/local/include/libiec61850/mms_client_connection.h: 507
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_readVariableAsync", "cdecl"):
    MmsConnection_readVariableAsync = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_readVariableAsync", "cdecl")
    MmsConnection_readVariableAsync.argtypes = [MmsConnection, POINTER(uint32_t), POINTER(MmsError), String, String, MmsConnection_ReadVariableHandler, POINTER(None)]
    MmsConnection_readVariableAsync.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 523
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_readVariableComponent", "cdecl"):
    MmsConnection_readVariableComponent = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_readVariableComponent", "cdecl")
    MmsConnection_readVariableComponent.argtypes = [MmsConnection, POINTER(MmsError), String, String, String]
    MmsConnection_readVariableComponent.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_client_connection.h: 540
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_readVariableComponentAsync", "cdecl"):
    MmsConnection_readVariableComponentAsync = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_readVariableComponentAsync", "cdecl")
    MmsConnection_readVariableComponentAsync.argtypes = [MmsConnection, POINTER(uint32_t), POINTER(MmsError), String, String, String, MmsConnection_ReadVariableHandler, POINTER(None)]
    MmsConnection_readVariableComponentAsync.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 558
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_readArrayElements", "cdecl"):
    MmsConnection_readArrayElements = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_readArrayElements", "cdecl")
    MmsConnection_readArrayElements.argtypes = [MmsConnection, POINTER(MmsError), String, String, uint32_t, uint32_t]
    MmsConnection_readArrayElements.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_client_connection.h: 577
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_readArrayElementsAsync", "cdecl"):
    MmsConnection_readArrayElementsAsync = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_readArrayElementsAsync", "cdecl")
    MmsConnection_readArrayElementsAsync.argtypes = [MmsConnection, POINTER(uint32_t), POINTER(MmsError), String, String, uint32_t, uint32_t, MmsConnection_ReadVariableHandler, POINTER(None)]
    MmsConnection_readArrayElementsAsync.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 594
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_readSingleArrayElementWithComponent", "cdecl"):
    MmsConnection_readSingleArrayElementWithComponent = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_readSingleArrayElementWithComponent", "cdecl")
    MmsConnection_readSingleArrayElementWithComponent.argtypes = [MmsConnection, POINTER(MmsError), String, String, uint32_t, String]
    MmsConnection_readSingleArrayElementWithComponent.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_client_connection.h: 599
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_readSingleArrayElementWithComponentAsync", "cdecl"):
    MmsConnection_readSingleArrayElementWithComponentAsync = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_readSingleArrayElementWithComponentAsync", "cdecl")
    MmsConnection_readSingleArrayElementWithComponentAsync.argtypes = [MmsConnection, POINTER(uint32_t), POINTER(MmsError), String, String, uint32_t, String, MmsConnection_ReadVariableHandler, POINTER(None)]
    MmsConnection_readSingleArrayElementWithComponentAsync.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 616
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_readMultipleVariables", "cdecl"):
    MmsConnection_readMultipleVariables = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_readMultipleVariables", "cdecl")
    MmsConnection_readMultipleVariables.argtypes = [MmsConnection, POINTER(MmsError), String, LinkedList]
    MmsConnection_readMultipleVariables.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_client_connection.h: 621
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_readMultipleVariablesAsync", "cdecl"):
    MmsConnection_readMultipleVariablesAsync = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_readMultipleVariablesAsync", "cdecl")
    MmsConnection_readMultipleVariablesAsync.argtypes = [MmsConnection, POINTER(uint32_t), POINTER(MmsError), String, LinkedList, MmsConnection_ReadVariableHandler, POINTER(None)]
    MmsConnection_readMultipleVariablesAsync.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 639
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_writeVariable", "cdecl"):
    MmsConnection_writeVariable = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_writeVariable", "cdecl")
    MmsConnection_writeVariable.argtypes = [MmsConnection, POINTER(MmsError), String, String, POINTER(MmsValue)]
    MmsConnection_writeVariable.restype = MmsDataAccessError

MmsConnection_WriteVariableHandler = CFUNCTYPE(UNCHECKED(None), uint32_t, POINTER(None), MmsError, MmsDataAccessError)# /usr/local/include/libiec61850/mms_client_connection.h: 643

# /usr/local/include/libiec61850/mms_client_connection.h: 646
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_writeVariableAsync", "cdecl"):
    MmsConnection_writeVariableAsync = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_writeVariableAsync", "cdecl")
    MmsConnection_writeVariableAsync.argtypes = [MmsConnection, POINTER(uint32_t), POINTER(MmsError), String, String, POINTER(MmsValue), MmsConnection_WriteVariableHandler, POINTER(None)]
    MmsConnection_writeVariableAsync.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 664
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_writeVariableComponent", "cdecl"):
    MmsConnection_writeVariableComponent = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_writeVariableComponent", "cdecl")
    MmsConnection_writeVariableComponent.argtypes = [MmsConnection, POINTER(MmsError), String, String, String, POINTER(MmsValue)]
    MmsConnection_writeVariableComponent.restype = MmsDataAccessError

# /usr/local/include/libiec61850/mms_client_connection.h: 682
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_writeSingleArrayElementWithComponent", "cdecl"):
    MmsConnection_writeSingleArrayElementWithComponent = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_writeSingleArrayElementWithComponent", "cdecl")
    MmsConnection_writeSingleArrayElementWithComponent.argtypes = [MmsConnection, POINTER(MmsError), String, String, uint32_t, String, POINTER(MmsValue)]
    MmsConnection_writeSingleArrayElementWithComponent.restype = MmsDataAccessError

# /usr/local/include/libiec61850/mms_client_connection.h: 687
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_writeSingleArrayElementWithComponentAsync", "cdecl"):
    MmsConnection_writeSingleArrayElementWithComponentAsync = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_writeSingleArrayElementWithComponentAsync", "cdecl")
    MmsConnection_writeSingleArrayElementWithComponentAsync.argtypes = [MmsConnection, POINTER(uint32_t), POINTER(MmsError), String, String, uint32_t, String, POINTER(MmsValue), MmsConnection_WriteVariableHandler, POINTER(None)]
    MmsConnection_writeSingleArrayElementWithComponentAsync.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 693
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_writeVariableComponentAsync", "cdecl"):
    MmsConnection_writeVariableComponentAsync = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_writeVariableComponentAsync", "cdecl")
    MmsConnection_writeVariableComponentAsync.argtypes = [MmsConnection, POINTER(uint32_t), POINTER(MmsError), String, String, String, POINTER(MmsValue), MmsConnection_WriteVariableHandler, POINTER(None)]
    MmsConnection_writeVariableComponentAsync.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 716
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_writeArrayElements", "cdecl"):
    MmsConnection_writeArrayElements = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_writeArrayElements", "cdecl")
    MmsConnection_writeArrayElements.argtypes = [MmsConnection, POINTER(MmsError), String, String, c_int, c_int, POINTER(MmsValue)]
    MmsConnection_writeArrayElements.restype = MmsDataAccessError

# /usr/local/include/libiec61850/mms_client_connection.h: 721
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_writeArrayElementsAsync", "cdecl"):
    MmsConnection_writeArrayElementsAsync = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_writeArrayElementsAsync", "cdecl")
    MmsConnection_writeArrayElementsAsync.argtypes = [MmsConnection, POINTER(uint32_t), POINTER(MmsError), String, String, c_int, c_int, POINTER(MmsValue), MmsConnection_WriteVariableHandler, POINTER(None)]
    MmsConnection_writeArrayElementsAsync.restype = None

MmsConnection_WriteMultipleVariablesHandler = CFUNCTYPE(UNCHECKED(None), uint32_t, POINTER(None), MmsError, LinkedList)# /usr/local/include/libiec61850/mms_client_connection.h: 728

# /usr/local/include/libiec61850/mms_client_connection.h: 749
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_writeMultipleVariables", "cdecl"):
    MmsConnection_writeMultipleVariables = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_writeMultipleVariables", "cdecl")
    MmsConnection_writeMultipleVariables.argtypes = [MmsConnection, POINTER(MmsError), String, LinkedList, LinkedList, POINTER(LinkedList)]
    MmsConnection_writeMultipleVariables.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 754
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_writeMultipleVariablesAsync", "cdecl"):
    MmsConnection_writeMultipleVariablesAsync = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_writeMultipleVariablesAsync", "cdecl")
    MmsConnection_writeMultipleVariablesAsync.argtypes = [MmsConnection, POINTER(uint32_t), POINTER(MmsError), String, LinkedList, LinkedList, MmsConnection_WriteMultipleVariablesHandler, POINTER(None)]
    MmsConnection_writeMultipleVariablesAsync.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 775
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_writeNamedVariableList", "cdecl"):
    MmsConnection_writeNamedVariableList = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_writeNamedVariableList", "cdecl")
    MmsConnection_writeNamedVariableList.argtypes = [MmsConnection, POINTER(MmsError), c_bool, String, String, LinkedList, POINTER(LinkedList)]
    MmsConnection_writeNamedVariableList.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 781
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_writeNamedVariableListAsync", "cdecl"):
    MmsConnection_writeNamedVariableListAsync = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_writeNamedVariableListAsync", "cdecl")
    MmsConnection_writeNamedVariableListAsync.argtypes = [MmsConnection, POINTER(uint32_t), POINTER(MmsError), c_bool, String, String, LinkedList, MmsConnection_WriteMultipleVariablesHandler, POINTER(None)]
    MmsConnection_writeNamedVariableListAsync.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 795
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_getVariableAccessAttributes", "cdecl"):
    MmsConnection_getVariableAccessAttributes = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_getVariableAccessAttributes", "cdecl")
    MmsConnection_getVariableAccessAttributes.argtypes = [MmsConnection, POINTER(MmsError), String, String]
    MmsConnection_getVariableAccessAttributes.restype = POINTER(MmsVariableSpecification)

MmsConnection_GetVariableAccessAttributesHandler = CFUNCTYPE(UNCHECKED(None), uint32_t, POINTER(None), MmsError, POINTER(MmsVariableSpecification))# /usr/local/include/libiec61850/mms_client_connection.h: 800

# /usr/local/include/libiec61850/mms_client_connection.h: 804
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_getVariableAccessAttributesAsync", "cdecl"):
    MmsConnection_getVariableAccessAttributesAsync = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_getVariableAccessAttributesAsync", "cdecl")
    MmsConnection_getVariableAccessAttributesAsync.argtypes = [MmsConnection, POINTER(uint32_t), POINTER(MmsError), String, String, MmsConnection_GetVariableAccessAttributesHandler, POINTER(None)]
    MmsConnection_getVariableAccessAttributesAsync.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 824
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_readNamedVariableListValues", "cdecl"):
    MmsConnection_readNamedVariableListValues = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_readNamedVariableListValues", "cdecl")
    MmsConnection_readNamedVariableListValues.argtypes = [MmsConnection, POINTER(MmsError), String, String, c_bool]
    MmsConnection_readNamedVariableListValues.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_client_connection.h: 829
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_readNamedVariableListValuesAsync", "cdecl"):
    MmsConnection_readNamedVariableListValuesAsync = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_readNamedVariableListValuesAsync", "cdecl")
    MmsConnection_readNamedVariableListValuesAsync.argtypes = [MmsConnection, POINTER(uint32_t), POINTER(MmsError), String, String, c_bool, MmsConnection_ReadVariableHandler, POINTER(None)]
    MmsConnection_readNamedVariableListValuesAsync.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 846
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_readNamedVariableListValuesAssociationSpecific", "cdecl"):
    MmsConnection_readNamedVariableListValuesAssociationSpecific = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_readNamedVariableListValuesAssociationSpecific", "cdecl")
    MmsConnection_readNamedVariableListValuesAssociationSpecific.argtypes = [MmsConnection, POINTER(MmsError), String, c_bool]
    MmsConnection_readNamedVariableListValuesAssociationSpecific.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_client_connection.h: 851
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_readNamedVariableListValuesAssociationSpecificAsync", "cdecl"):
    MmsConnection_readNamedVariableListValuesAssociationSpecificAsync = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_readNamedVariableListValuesAssociationSpecificAsync", "cdecl")
    MmsConnection_readNamedVariableListValuesAssociationSpecificAsync.argtypes = [MmsConnection, POINTER(uint32_t), POINTER(MmsError), String, c_bool, MmsConnection_ReadVariableHandler, POINTER(None)]
    MmsConnection_readNamedVariableListValuesAssociationSpecificAsync.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 869
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_defineNamedVariableList", "cdecl"):
    MmsConnection_defineNamedVariableList = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_defineNamedVariableList", "cdecl")
    MmsConnection_defineNamedVariableList.argtypes = [MmsConnection, POINTER(MmsError), String, String, LinkedList]
    MmsConnection_defineNamedVariableList.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 873
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_defineNamedVariableListAsync", "cdecl"):
    MmsConnection_defineNamedVariableListAsync = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_defineNamedVariableListAsync", "cdecl")
    MmsConnection_defineNamedVariableListAsync.argtypes = [MmsConnection, POINTER(uint32_t), POINTER(MmsError), String, String, LinkedList, MmsConnection_GenericServiceHandler, POINTER(None)]
    MmsConnection_defineNamedVariableListAsync.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 889
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_defineNamedVariableListAssociationSpecific", "cdecl"):
    MmsConnection_defineNamedVariableListAssociationSpecific = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_defineNamedVariableListAssociationSpecific", "cdecl")
    MmsConnection_defineNamedVariableListAssociationSpecific.argtypes = [MmsConnection, POINTER(MmsError), String, LinkedList]
    MmsConnection_defineNamedVariableListAssociationSpecific.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 893
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_defineNamedVariableListAssociationSpecificAsync", "cdecl"):
    MmsConnection_defineNamedVariableListAssociationSpecificAsync = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_defineNamedVariableListAssociationSpecificAsync", "cdecl")
    MmsConnection_defineNamedVariableListAssociationSpecificAsync.argtypes = [MmsConnection, POINTER(uint32_t), POINTER(MmsError), String, LinkedList, MmsConnection_GenericServiceHandler, POINTER(None)]
    MmsConnection_defineNamedVariableListAssociationSpecificAsync.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 913
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_readNamedVariableListDirectory", "cdecl"):
    MmsConnection_readNamedVariableListDirectory = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_readNamedVariableListDirectory", "cdecl")
    MmsConnection_readNamedVariableListDirectory.argtypes = [MmsConnection, POINTER(MmsError), String, String, POINTER(c_bool)]
    MmsConnection_readNamedVariableListDirectory.restype = LinkedList

MmsConnection_ReadNVLDirectoryHandler = CFUNCTYPE(UNCHECKED(None), uint32_t, POINTER(None), MmsError, LinkedList, c_bool)# /usr/local/include/libiec61850/mms_client_connection.h: 918

# /usr/local/include/libiec61850/mms_client_connection.h: 922
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_readNamedVariableListDirectoryAsync", "cdecl"):
    MmsConnection_readNamedVariableListDirectoryAsync = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_readNamedVariableListDirectoryAsync", "cdecl")
    MmsConnection_readNamedVariableListDirectoryAsync.argtypes = [MmsConnection, POINTER(uint32_t), POINTER(MmsError), String, String, MmsConnection_ReadNVLDirectoryHandler, POINTER(None)]
    MmsConnection_readNamedVariableListDirectoryAsync.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 937
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_readNamedVariableListDirectoryAssociationSpecific", "cdecl"):
    MmsConnection_readNamedVariableListDirectoryAssociationSpecific = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_readNamedVariableListDirectoryAssociationSpecific", "cdecl")
    MmsConnection_readNamedVariableListDirectoryAssociationSpecific.argtypes = [MmsConnection, POINTER(MmsError), String, POINTER(c_bool)]
    MmsConnection_readNamedVariableListDirectoryAssociationSpecific.restype = LinkedList

# /usr/local/include/libiec61850/mms_client_connection.h: 941
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_readNamedVariableListDirectoryAssociationSpecificAsync", "cdecl"):
    MmsConnection_readNamedVariableListDirectoryAssociationSpecificAsync = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_readNamedVariableListDirectoryAssociationSpecificAsync", "cdecl")
    MmsConnection_readNamedVariableListDirectoryAssociationSpecificAsync.argtypes = [MmsConnection, POINTER(uint32_t), POINTER(MmsError), String, MmsConnection_ReadNVLDirectoryHandler, POINTER(None)]
    MmsConnection_readNamedVariableListDirectoryAssociationSpecificAsync.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 959
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_deleteNamedVariableList", "cdecl"):
    MmsConnection_deleteNamedVariableList = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_deleteNamedVariableList", "cdecl")
    MmsConnection_deleteNamedVariableList.argtypes = [MmsConnection, POINTER(MmsError), String, String]
    MmsConnection_deleteNamedVariableList.restype = c_bool

# /usr/local/include/libiec61850/mms_client_connection.h: 963
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_deleteNamedVariableListAsync", "cdecl"):
    MmsConnection_deleteNamedVariableListAsync = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_deleteNamedVariableListAsync", "cdecl")
    MmsConnection_deleteNamedVariableListAsync.argtypes = [MmsConnection, POINTER(uint32_t), POINTER(MmsError), String, String, MmsConnection_GenericServiceHandler, POINTER(None)]
    MmsConnection_deleteNamedVariableListAsync.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 976
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_deleteAssociationSpecificNamedVariableList", "cdecl"):
    MmsConnection_deleteAssociationSpecificNamedVariableList = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_deleteAssociationSpecificNamedVariableList", "cdecl")
    MmsConnection_deleteAssociationSpecificNamedVariableList.argtypes = [MmsConnection, POINTER(MmsError), String]
    MmsConnection_deleteAssociationSpecificNamedVariableList.restype = c_bool

# /usr/local/include/libiec61850/mms_client_connection.h: 981
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_deleteAssociationSpecificNamedVariableListAsync", "cdecl"):
    MmsConnection_deleteAssociationSpecificNamedVariableListAsync = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_deleteAssociationSpecificNamedVariableListAsync", "cdecl")
    MmsConnection_deleteAssociationSpecificNamedVariableListAsync.argtypes = [MmsConnection, POINTER(uint32_t), POINTER(MmsError), String, MmsConnection_GenericServiceHandler, POINTER(None)]
    MmsConnection_deleteAssociationSpecificNamedVariableListAsync.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 995
if _libs["/usr/local/lib/libiec61850.so"].has("MmsVariableAccessSpecification_create", "cdecl"):
    MmsVariableAccessSpecification_create = _libs["/usr/local/lib/libiec61850.so"].get("MmsVariableAccessSpecification_create", "cdecl")
    MmsVariableAccessSpecification_create.argtypes = [String, String]
    MmsVariableAccessSpecification_create.restype = POINTER(MmsVariableAccessSpecification)

# /usr/local/include/libiec61850/mms_client_connection.h: 1014
if _libs["/usr/local/lib/libiec61850.so"].has("MmsVariableAccessSpecification_createAlternateAccess", "cdecl"):
    MmsVariableAccessSpecification_createAlternateAccess = _libs["/usr/local/lib/libiec61850.so"].get("MmsVariableAccessSpecification_createAlternateAccess", "cdecl")
    MmsVariableAccessSpecification_createAlternateAccess.argtypes = [String, String, c_int32, String]
    MmsVariableAccessSpecification_createAlternateAccess.restype = POINTER(MmsVariableAccessSpecification)

# /usr/local/include/libiec61850/mms_client_connection.h: 1024
if _libs["/usr/local/lib/libiec61850.so"].has("MmsVariableAccessSpecification_destroy", "cdecl"):
    MmsVariableAccessSpecification_destroy = _libs["/usr/local/lib/libiec61850.so"].get("MmsVariableAccessSpecification_destroy", "cdecl")
    MmsVariableAccessSpecification_destroy.argtypes = [POINTER(MmsVariableAccessSpecification)]
    MmsVariableAccessSpecification_destroy.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 1036
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_setLocalDetail", "cdecl"):
    MmsConnection_setLocalDetail = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_setLocalDetail", "cdecl")
    MmsConnection_setLocalDetail.argtypes = [MmsConnection, c_int32]
    MmsConnection_setLocalDetail.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 1039
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_getLocalDetail", "cdecl"):
    MmsConnection_getLocalDetail = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_getLocalDetail", "cdecl")
    MmsConnection_getLocalDetail.argtypes = [MmsConnection]
    MmsConnection_getLocalDetail.restype = c_int32

# /usr/local/include/libiec61850/mms_client_connection.h: 1050
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_identify", "cdecl"):
    MmsConnection_identify = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_identify", "cdecl")
    MmsConnection_identify.argtypes = [MmsConnection, POINTER(MmsError)]
    MmsConnection_identify.restype = POINTER(MmsServerIdentity)

MmsConnection_IdentifyHandler = CFUNCTYPE(UNCHECKED(None), uint32_t, POINTER(None), MmsError, String, String, String)# /usr/local/include/libiec61850/mms_client_connection.h: 1054

# /usr/local/include/libiec61850/mms_client_connection.h: 1058
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_identifyAsync", "cdecl"):
    MmsConnection_identifyAsync = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_identifyAsync", "cdecl")
    MmsConnection_identifyAsync.argtypes = [MmsConnection, POINTER(uint32_t), POINTER(MmsError), MmsConnection_IdentifyHandler, POINTER(None)]
    MmsConnection_identifyAsync.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 1067
if _libs["/usr/local/lib/libiec61850.so"].has("MmsServerIdentity_destroy", "cdecl"):
    MmsServerIdentity_destroy = _libs["/usr/local/lib/libiec61850.so"].get("MmsServerIdentity_destroy", "cdecl")
    MmsServerIdentity_destroy.argtypes = [POINTER(MmsServerIdentity)]
    MmsServerIdentity_destroy.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 1082
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_getServerStatus", "cdecl"):
    MmsConnection_getServerStatus = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_getServerStatus", "cdecl")
    MmsConnection_getServerStatus.argtypes = [MmsConnection, POINTER(MmsError), POINTER(c_int), POINTER(c_int), c_bool]
    MmsConnection_getServerStatus.restype = None

MmsConnection_GetServerStatusHandler = CFUNCTYPE(UNCHECKED(None), uint32_t, POINTER(None), MmsError, c_int, c_int)# /usr/local/include/libiec61850/mms_client_connection.h: 1086

# /usr/local/include/libiec61850/mms_client_connection.h: 1089
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_getServerStatusAsync", "cdecl"):
    MmsConnection_getServerStatusAsync = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_getServerStatusAsync", "cdecl")
    MmsConnection_getServerStatusAsync.argtypes = [MmsConnection, POINTER(uint32_t), POINTER(MmsError), c_bool, MmsConnection_GetServerStatusHandler, POINTER(None)]
    MmsConnection_getServerStatusAsync.restype = None

MmsFileDirectoryHandler = CFUNCTYPE(UNCHECKED(None), POINTER(None), String, uint32_t, uint64_t)# /usr/local/include/libiec61850/mms_client_connection.h: 1097

MmsConnection_FileDirectoryHandler = CFUNCTYPE(UNCHECKED(None), uint32_t, POINTER(None), MmsError, String, uint32_t, uint64_t, c_bool)# /usr/local/include/libiec61850/mms_client_connection.h: 1107

MmsFileReadHandler = CFUNCTYPE(UNCHECKED(None), POINTER(None), c_int32, POINTER(uint8_t), uint32_t)# /usr/local/include/libiec61850/mms_client_connection.h: 1111

MmsConnection_FileReadHandler = CFUNCTYPE(UNCHECKED(None), uint32_t, POINTER(None), MmsError, c_int32, POINTER(uint8_t), uint32_t, c_bool)# /usr/local/include/libiec61850/mms_client_connection.h: 1127

# /usr/local/include/libiec61850/mms_client_connection.h: 1140
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_fileOpen", "cdecl"):
    MmsConnection_fileOpen = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_fileOpen", "cdecl")
    MmsConnection_fileOpen.argtypes = [MmsConnection, POINTER(MmsError), String, uint32_t, POINTER(uint32_t), POINTER(uint64_t)]
    MmsConnection_fileOpen.restype = c_int32

MmsConnection_FileOpenHandler = CFUNCTYPE(UNCHECKED(None), uint32_t, POINTER(None), MmsError, c_int32, uint32_t, uint64_t)# /usr/local/include/libiec61850/mms_client_connection.h: 1144

# /usr/local/include/libiec61850/mms_client_connection.h: 1147
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_fileOpenAsync", "cdecl"):
    MmsConnection_fileOpenAsync = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_fileOpenAsync", "cdecl")
    MmsConnection_fileOpenAsync.argtypes = [MmsConnection, POINTER(uint32_t), POINTER(MmsError), String, uint32_t, MmsConnection_FileOpenHandler, POINTER(None)]
    MmsConnection_fileOpenAsync.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 1163
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_fileRead", "cdecl"):
    MmsConnection_fileRead = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_fileRead", "cdecl")
    MmsConnection_fileRead.argtypes = [MmsConnection, POINTER(MmsError), c_int32, MmsFileReadHandler, POINTER(None)]
    MmsConnection_fileRead.restype = c_bool

# /usr/local/include/libiec61850/mms_client_connection.h: 1166
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_fileReadAsync", "cdecl"):
    MmsConnection_fileReadAsync = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_fileReadAsync", "cdecl")
    MmsConnection_fileReadAsync.argtypes = [MmsConnection, POINTER(uint32_t), POINTER(MmsError), c_int32, MmsConnection_FileReadHandler, POINTER(None)]
    MmsConnection_fileReadAsync.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 1176
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_fileClose", "cdecl"):
    MmsConnection_fileClose = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_fileClose", "cdecl")
    MmsConnection_fileClose.argtypes = [MmsConnection, POINTER(MmsError), c_int32]
    MmsConnection_fileClose.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 1179
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_fileCloseAsync", "cdecl"):
    MmsConnection_fileCloseAsync = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_fileCloseAsync", "cdecl")
    MmsConnection_fileCloseAsync.argtypes = [MmsConnection, POINTER(uint32_t), POINTER(MmsError), uint32_t, MmsConnection_GenericServiceHandler, POINTER(None)]
    MmsConnection_fileCloseAsync.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 1189
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_fileDelete", "cdecl"):
    MmsConnection_fileDelete = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_fileDelete", "cdecl")
    MmsConnection_fileDelete.argtypes = [MmsConnection, POINTER(MmsError), String]
    MmsConnection_fileDelete.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 1192
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_fileDeleteAsync", "cdecl"):
    MmsConnection_fileDeleteAsync = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_fileDeleteAsync", "cdecl")
    MmsConnection_fileDeleteAsync.argtypes = [MmsConnection, POINTER(uint32_t), POINTER(MmsError), String, MmsConnection_GenericServiceHandler, POINTER(None)]
    MmsConnection_fileDeleteAsync.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 1204
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_fileRename", "cdecl"):
    MmsConnection_fileRename = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_fileRename", "cdecl")
    MmsConnection_fileRename.argtypes = [MmsConnection, POINTER(MmsError), String, String]
    MmsConnection_fileRename.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 1207
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_fileRenameAsync", "cdecl"):
    MmsConnection_fileRenameAsync = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_fileRenameAsync", "cdecl")
    MmsConnection_fileRenameAsync.argtypes = [MmsConnection, POINTER(uint32_t), POINTER(MmsError), String, String, MmsConnection_GenericServiceHandler, POINTER(None)]
    MmsConnection_fileRenameAsync.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 1219
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_obtainFile", "cdecl"):
    MmsConnection_obtainFile = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_obtainFile", "cdecl")
    MmsConnection_obtainFile.argtypes = [MmsConnection, POINTER(MmsError), String, String]
    MmsConnection_obtainFile.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 1222
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_obtainFileAsync", "cdecl"):
    MmsConnection_obtainFileAsync = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_obtainFileAsync", "cdecl")
    MmsConnection_obtainFileAsync.argtypes = [MmsConnection, POINTER(uint32_t), POINTER(MmsError), String, String, MmsConnection_GenericServiceHandler, POINTER(None)]
    MmsConnection_obtainFileAsync.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 1242
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_getFileDirectory", "cdecl"):
    MmsConnection_getFileDirectory = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_getFileDirectory", "cdecl")
    MmsConnection_getFileDirectory.argtypes = [MmsConnection, POINTER(MmsError), String, String, MmsFileDirectoryHandler, POINTER(None)]
    MmsConnection_getFileDirectory.restype = c_bool

# /usr/local/include/libiec61850/mms_client_connection.h: 1246
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_getFileDirectoryAsync", "cdecl"):
    MmsConnection_getFileDirectoryAsync = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_getFileDirectoryAsync", "cdecl")
    MmsConnection_getFileDirectoryAsync.argtypes = [MmsConnection, POINTER(uint32_t), POINTER(MmsError), String, String, MmsConnection_FileDirectoryHandler, POINTER(None)]
    MmsConnection_getFileDirectoryAsync.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 1253
class struct_sMmsJournalEntry(Structure):
    pass

MmsJournalEntry = POINTER(struct_sMmsJournalEntry)# /usr/local/include/libiec61850/mms_client_connection.h: 1249

# /usr/local/include/libiec61850/mms_client_connection.h: 1259
class struct_sMmsJournalVariable(Structure):
    pass

MmsJournalVariable = POINTER(struct_sMmsJournalVariable)# /usr/local/include/libiec61850/mms_client_connection.h: 1251

struct_sMmsJournalEntry.__slots__ = [
    'entryID',
    'occurenceTime',
    'journalVariables',
]
struct_sMmsJournalEntry._fields_ = [
    ('entryID', POINTER(MmsValue)),
    ('occurenceTime', POINTER(MmsValue)),
    ('journalVariables', LinkedList),
]

struct_sMmsJournalVariable.__slots__ = [
    'tag',
    'value',
]
struct_sMmsJournalVariable._fields_ = [
    ('tag', String),
    ('value', POINTER(MmsValue)),
]

# /usr/local/include/libiec61850/mms_client_connection.h: 1278
if _libs["/usr/local/lib/libiec61850.so"].has("MmsJournalEntry_destroy", "cdecl"):
    MmsJournalEntry_destroy = _libs["/usr/local/lib/libiec61850.so"].get("MmsJournalEntry_destroy", "cdecl")
    MmsJournalEntry_destroy.argtypes = [MmsJournalEntry]
    MmsJournalEntry_destroy.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 1280
if _libs["/usr/local/lib/libiec61850.so"].has("MmsJournalEntry_getEntryID", "cdecl"):
    MmsJournalEntry_getEntryID = _libs["/usr/local/lib/libiec61850.so"].get("MmsJournalEntry_getEntryID", "cdecl")
    MmsJournalEntry_getEntryID.argtypes = [MmsJournalEntry]
    MmsJournalEntry_getEntryID.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_client_connection.h: 1283
if _libs["/usr/local/lib/libiec61850.so"].has("MmsJournalEntry_getOccurenceTime", "cdecl"):
    MmsJournalEntry_getOccurenceTime = _libs["/usr/local/lib/libiec61850.so"].get("MmsJournalEntry_getOccurenceTime", "cdecl")
    MmsJournalEntry_getOccurenceTime.argtypes = [MmsJournalEntry]
    MmsJournalEntry_getOccurenceTime.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/mms_client_connection.h: 1287
if _libs["/usr/local/lib/libiec61850.so"].has("MmsJournalEntry_getJournalVariables", "cdecl"):
    MmsJournalEntry_getJournalVariables = _libs["/usr/local/lib/libiec61850.so"].get("MmsJournalEntry_getJournalVariables", "cdecl")
    MmsJournalEntry_getJournalVariables.argtypes = [MmsJournalEntry]
    MmsJournalEntry_getJournalVariables.restype = LinkedList

# /usr/local/include/libiec61850/mms_client_connection.h: 1289
if _libs["/usr/local/lib/libiec61850.so"].has("MmsJournalVariable_getTag", "cdecl"):
    MmsJournalVariable_getTag = _libs["/usr/local/lib/libiec61850.so"].get("MmsJournalVariable_getTag", "cdecl")
    MmsJournalVariable_getTag.argtypes = [MmsJournalVariable]
    MmsJournalVariable_getTag.restype = c_char_p

# /usr/local/include/libiec61850/mms_client_connection.h: 1292
if _libs["/usr/local/lib/libiec61850.so"].has("MmsJournalVariable_getValue", "cdecl"):
    MmsJournalVariable_getValue = _libs["/usr/local/lib/libiec61850.so"].get("MmsJournalVariable_getValue", "cdecl")
    MmsJournalVariable_getValue.argtypes = [MmsJournalVariable]
    MmsJournalVariable_getValue.restype = POINTER(MmsValue)

MmsConnection_ReadJournalHandler = CFUNCTYPE(UNCHECKED(None), uint32_t, POINTER(None), MmsError, LinkedList, c_bool)# /usr/local/include/libiec61850/mms_client_connection.h: 1296

# /usr/local/include/libiec61850/mms_client_connection.h: 1300
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_readJournalTimeRange", "cdecl"):
    MmsConnection_readJournalTimeRange = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_readJournalTimeRange", "cdecl")
    MmsConnection_readJournalTimeRange.argtypes = [MmsConnection, POINTER(MmsError), String, String, POINTER(MmsValue), POINTER(MmsValue), POINTER(c_bool)]
    MmsConnection_readJournalTimeRange.restype = LinkedList

# /usr/local/include/libiec61850/mms_client_connection.h: 1304
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_readJournalTimeRangeAsync", "cdecl"):
    MmsConnection_readJournalTimeRangeAsync = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_readJournalTimeRangeAsync", "cdecl")
    MmsConnection_readJournalTimeRangeAsync.argtypes = [MmsConnection, POINTER(uint32_t), POINTER(MmsError), String, String, POINTER(MmsValue), POINTER(MmsValue), MmsConnection_ReadJournalHandler, POINTER(None)]
    MmsConnection_readJournalTimeRangeAsync.restype = None

# /usr/local/include/libiec61850/mms_client_connection.h: 1308
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_readJournalStartAfter", "cdecl"):
    MmsConnection_readJournalStartAfter = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_readJournalStartAfter", "cdecl")
    MmsConnection_readJournalStartAfter.argtypes = [MmsConnection, POINTER(MmsError), String, String, POINTER(MmsValue), POINTER(MmsValue), POINTER(c_bool)]
    MmsConnection_readJournalStartAfter.restype = LinkedList

# /usr/local/include/libiec61850/mms_client_connection.h: 1312
if _libs["/usr/local/lib/libiec61850.so"].has("MmsConnection_readJournalStartAfterAsync", "cdecl"):
    MmsConnection_readJournalStartAfterAsync = _libs["/usr/local/lib/libiec61850.so"].get("MmsConnection_readJournalStartAfterAsync", "cdecl")
    MmsConnection_readJournalStartAfterAsync.argtypes = [MmsConnection, POINTER(uint32_t), POINTER(MmsError), String, String, POINTER(MmsValue), POINTER(MmsValue), MmsConnection_ReadJournalHandler, POINTER(None)]
    MmsConnection_readJournalStartAfterAsync.restype = None

# /usr/local/include/libiec61850/iec61850_client.h: 43
class struct_sClientDataSet(Structure):
    pass

ClientDataSet = POINTER(struct_sClientDataSet)# /usr/local/include/libiec61850/iec61850_client.h: 43

# /usr/local/include/libiec61850/iec61850_client.h: 46
class struct_sClientReport(Structure):
    pass

ClientReport = POINTER(struct_sClientReport)# /usr/local/include/libiec61850/iec61850_client.h: 46

# /usr/local/include/libiec61850/iec61850_client.h: 49
class struct_sClientReportControlBlock(Structure):
    pass

ClientReportControlBlock = POINTER(struct_sClientReportControlBlock)# /usr/local/include/libiec61850/iec61850_client.h: 49

# /usr/local/include/libiec61850/iec61850_client.h: 52
class struct_sClientGooseControlBlock(Structure):
    pass

ClientGooseControlBlock = POINTER(struct_sClientGooseControlBlock)# /usr/local/include/libiec61850/iec61850_client.h: 52

# /usr/local/include/libiec61850/iec61850_client.h: 61
class struct_sIedConnection(Structure):
    pass

IedConnection = POINTER(struct_sIedConnection)# /usr/local/include/libiec61850/iec61850_client.h: 61

# /usr/local/include/libiec61850/iec61850_client.h: 69
class struct_anon_44(Structure):
    pass

struct_anon_44.__slots__ = [
    'ctlNum',
    'error',
    'addCause',
]
struct_anon_44._fields_ = [
    ('ctlNum', c_int),
    ('error', ControlLastApplError),
    ('addCause', ControlAddCause),
]

LastApplError = struct_anon_44# /usr/local/include/libiec61850/iec61850_client.h: 69

enum_anon_45 = c_int# /usr/local/include/libiec61850/iec61850_client.h: 78

IED_STATE_CLOSED = 0# /usr/local/include/libiec61850/iec61850_client.h: 78

IED_STATE_CONNECTING = (IED_STATE_CLOSED + 1)# /usr/local/include/libiec61850/iec61850_client.h: 78

IED_STATE_CONNECTED = (IED_STATE_CONNECTING + 1)# /usr/local/include/libiec61850/iec61850_client.h: 78

IED_STATE_CLOSING = (IED_STATE_CONNECTED + 1)# /usr/local/include/libiec61850/iec61850_client.h: 78

IedConnectionState = enum_anon_45# /usr/local/include/libiec61850/iec61850_client.h: 78

enum_anon_46 = c_int# /usr/local/include/libiec61850/iec61850_client.h: 170

IED_ERROR_OK = 0# /usr/local/include/libiec61850/iec61850_client.h: 170

IED_ERROR_NOT_CONNECTED = 1# /usr/local/include/libiec61850/iec61850_client.h: 170

IED_ERROR_ALREADY_CONNECTED = 2# /usr/local/include/libiec61850/iec61850_client.h: 170

IED_ERROR_CONNECTION_LOST = 3# /usr/local/include/libiec61850/iec61850_client.h: 170

IED_ERROR_SERVICE_NOT_SUPPORTED = 4# /usr/local/include/libiec61850/iec61850_client.h: 170

IED_ERROR_CONNECTION_REJECTED = 5# /usr/local/include/libiec61850/iec61850_client.h: 170

IED_ERROR_OUTSTANDING_CALL_LIMIT_REACHED = 6# /usr/local/include/libiec61850/iec61850_client.h: 170

IED_ERROR_USER_PROVIDED_INVALID_ARGUMENT = 10# /usr/local/include/libiec61850/iec61850_client.h: 170

IED_ERROR_ENABLE_REPORT_FAILED_DATASET_MISMATCH = 11# /usr/local/include/libiec61850/iec61850_client.h: 170

IED_ERROR_OBJECT_REFERENCE_INVALID = 12# /usr/local/include/libiec61850/iec61850_client.h: 170

IED_ERROR_UNEXPECTED_VALUE_RECEIVED = 13# /usr/local/include/libiec61850/iec61850_client.h: 170

IED_ERROR_TIMEOUT = 20# /usr/local/include/libiec61850/iec61850_client.h: 170

IED_ERROR_ACCESS_DENIED = 21# /usr/local/include/libiec61850/iec61850_client.h: 170

IED_ERROR_OBJECT_DOES_NOT_EXIST = 22# /usr/local/include/libiec61850/iec61850_client.h: 170

IED_ERROR_OBJECT_EXISTS = 23# /usr/local/include/libiec61850/iec61850_client.h: 170

IED_ERROR_OBJECT_ACCESS_UNSUPPORTED = 24# /usr/local/include/libiec61850/iec61850_client.h: 170

IED_ERROR_TYPE_INCONSISTENT = 25# /usr/local/include/libiec61850/iec61850_client.h: 170

IED_ERROR_TEMPORARILY_UNAVAILABLE = 26# /usr/local/include/libiec61850/iec61850_client.h: 170

IED_ERROR_OBJECT_UNDEFINED = 27# /usr/local/include/libiec61850/iec61850_client.h: 170

IED_ERROR_INVALID_ADDRESS = 28# /usr/local/include/libiec61850/iec61850_client.h: 170

IED_ERROR_HARDWARE_FAULT = 29# /usr/local/include/libiec61850/iec61850_client.h: 170

IED_ERROR_TYPE_UNSUPPORTED = 30# /usr/local/include/libiec61850/iec61850_client.h: 170

IED_ERROR_OBJECT_ATTRIBUTE_INCONSISTENT = 31# /usr/local/include/libiec61850/iec61850_client.h: 170

IED_ERROR_OBJECT_VALUE_INVALID = 32# /usr/local/include/libiec61850/iec61850_client.h: 170

IED_ERROR_OBJECT_INVALIDATED = 33# /usr/local/include/libiec61850/iec61850_client.h: 170

IED_ERROR_MALFORMED_MESSAGE = 34# /usr/local/include/libiec61850/iec61850_client.h: 170

IED_ERROR_SERVICE_NOT_IMPLEMENTED = 98# /usr/local/include/libiec61850/iec61850_client.h: 170

IED_ERROR_UNKNOWN = 99# /usr/local/include/libiec61850/iec61850_client.h: 170

IedClientError = enum_anon_46# /usr/local/include/libiec61850/iec61850_client.h: 170

# /usr/local/include/libiec61850/iec61850_client.h: 186
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_create", "cdecl"):
    IedConnection_create = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_create", "cdecl")
    IedConnection_create.argtypes = []
    IedConnection_create.restype = IedConnection

# /usr/local/include/libiec61850/iec61850_client.h: 204
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_createEx", "cdecl"):
    IedConnection_createEx = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_createEx", "cdecl")
    IedConnection_createEx.argtypes = [TLSConfiguration, c_bool]
    IedConnection_createEx.restype = IedConnection

# /usr/local/include/libiec61850/iec61850_client.h: 221
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_createWithTlsSupport", "cdecl"):
    IedConnection_createWithTlsSupport = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_createWithTlsSupport", "cdecl")
    IedConnection_createWithTlsSupport.argtypes = [TLSConfiguration]
    IedConnection_createWithTlsSupport.restype = IedConnection

# /usr/local/include/libiec61850/iec61850_client.h: 232
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_destroy", "cdecl"):
    IedConnection_destroy = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_destroy", "cdecl")
    IedConnection_destroy.argtypes = [IedConnection]
    IedConnection_destroy.restype = None

# /usr/local/include/libiec61850/iec61850_client.h: 244
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_setLocalAddress", "cdecl"):
    IedConnection_setLocalAddress = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_setLocalAddress", "cdecl")
    IedConnection_setLocalAddress.argtypes = [IedConnection, String, c_int]
    IedConnection_setLocalAddress.restype = None

# /usr/local/include/libiec61850/iec61850_client.h: 256
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_setConnectTimeout", "cdecl"):
    IedConnection_setConnectTimeout = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_setConnectTimeout", "cdecl")
    IedConnection_setConnectTimeout.argtypes = [IedConnection, uint32_t]
    IedConnection_setConnectTimeout.restype = None

# /usr/local/include/libiec61850/iec61850_client.h: 268
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_setRequestTimeout", "cdecl"):
    IedConnection_setRequestTimeout = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_setRequestTimeout", "cdecl")
    IedConnection_setRequestTimeout.argtypes = [IedConnection, uint32_t]
    IedConnection_setRequestTimeout.restype = None

# /usr/local/include/libiec61850/iec61850_client.h: 278
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_getRequestTimeout", "cdecl"):
    IedConnection_getRequestTimeout = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_getRequestTimeout", "cdecl")
    IedConnection_getRequestTimeout.argtypes = [IedConnection]
    IedConnection_getRequestTimeout.restype = uint32_t

# /usr/local/include/libiec61850/iec61850_client.h: 290
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_setTimeQuality", "cdecl"):
    IedConnection_setTimeQuality = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_setTimeQuality", "cdecl")
    IedConnection_setTimeQuality.argtypes = [IedConnection, c_bool, c_bool, c_bool, c_int]
    IedConnection_setTimeQuality.restype = None

# /usr/local/include/libiec61850/iec61850_client.h: 305
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_tick", "cdecl"):
    IedConnection_tick = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_tick", "cdecl")
    IedConnection_tick.argtypes = [IedConnection]
    IedConnection_tick.restype = c_bool

IedConnection_GenericServiceHandler = CFUNCTYPE(UNCHECKED(None), uint32_t, POINTER(None), IedClientError)# /usr/local/include/libiec61850/iec61850_client.h: 318

# /usr/local/include/libiec61850/iec61850_client.h: 335
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_connect", "cdecl"):
    IedConnection_connect = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_connect", "cdecl")
    IedConnection_connect.argtypes = [IedConnection, POINTER(IedClientError), String, c_int]
    IedConnection_connect.restype = None

# /usr/local/include/libiec61850/iec61850_client.h: 351
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_connectAsync", "cdecl"):
    IedConnection_connectAsync = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_connectAsync", "cdecl")
    IedConnection_connectAsync.argtypes = [IedConnection, POINTER(IedClientError), String, c_int]
    IedConnection_connectAsync.restype = None

# /usr/local/include/libiec61850/iec61850_client.h: 366
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_abort", "cdecl"):
    IedConnection_abort = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_abort", "cdecl")
    IedConnection_abort.argtypes = [IedConnection, POINTER(IedClientError)]
    IedConnection_abort.restype = None

# /usr/local/include/libiec61850/iec61850_client.h: 382
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_abortAsync", "cdecl"):
    IedConnection_abortAsync = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_abortAsync", "cdecl")
    IedConnection_abortAsync.argtypes = [IedConnection, POINTER(IedClientError)]
    IedConnection_abortAsync.restype = None

# /usr/local/include/libiec61850/iec61850_client.h: 397
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_release", "cdecl"):
    IedConnection_release = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_release", "cdecl")
    IedConnection_release.argtypes = [IedConnection, POINTER(IedClientError)]
    IedConnection_release.restype = None

# /usr/local/include/libiec61850/iec61850_client.h: 412
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_releaseAsync", "cdecl"):
    IedConnection_releaseAsync = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_releaseAsync", "cdecl")
    IedConnection_releaseAsync.argtypes = [IedConnection, POINTER(IedClientError)]
    IedConnection_releaseAsync.restype = None

# /usr/local/include/libiec61850/iec61850_client.h: 422
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_close", "cdecl"):
    IedConnection_close = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_close", "cdecl")
    IedConnection_close.argtypes = [IedConnection]
    IedConnection_close.restype = None

# /usr/local/include/libiec61850/iec61850_client.h: 434
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_getState", "cdecl"):
    IedConnection_getState = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_getState", "cdecl")
    IedConnection_getState.argtypes = [IedConnection]
    IedConnection_getState.restype = IedConnectionState

# /usr/local/include/libiec61850/iec61850_client.h: 444
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_getLastApplError", "cdecl"):
    IedConnection_getLastApplError = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_getLastApplError", "cdecl")
    IedConnection_getLastApplError.argtypes = [IedConnection]
    IedConnection_getLastApplError.restype = LastApplError

IedConnectionClosedHandler = CFUNCTYPE(UNCHECKED(None), POINTER(None), IedConnection)# /usr/local/include/libiec61850/iec61850_client.h: 455

# /usr/local/include/libiec61850/iec61850_client.h: 467
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_installConnectionClosedHandler", "cdecl"):
    IedConnection_installConnectionClosedHandler = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_installConnectionClosedHandler", "cdecl")
    IedConnection_installConnectionClosedHandler.argtypes = [IedConnection, IedConnectionClosedHandler, POINTER(None)]
    IedConnection_installConnectionClosedHandler.restype = None

IedConnection_StateChangedHandler = CFUNCTYPE(UNCHECKED(None), POINTER(None), IedConnection, IedConnectionState)# /usr/local/include/libiec61850/iec61850_client.h: 478

# /usr/local/include/libiec61850/iec61850_client.h: 488
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_installStateChangedHandler", "cdecl"):
    IedConnection_installStateChangedHandler = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_installStateChangedHandler", "cdecl")
    IedConnection_installStateChangedHandler.argtypes = [IedConnection, IedConnection_StateChangedHandler, POINTER(None)]
    IedConnection_installStateChangedHandler.restype = None

# /usr/local/include/libiec61850/iec61850_client.h: 501
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_getMmsConnection", "cdecl"):
    IedConnection_getMmsConnection = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_getMmsConnection", "cdecl")
    IedConnection_getMmsConnection.argtypes = [IedConnection]
    IedConnection_getMmsConnection.restype = MmsConnection

# /usr/local/include/libiec61850/iec61850_client.h: 534
class struct_sClientSVControlBlock(Structure):
    pass

ClientSVControlBlock = POINTER(struct_sClientSVControlBlock)# /usr/local/include/libiec61850/iec61850_client.h: 534

# /usr/local/include/libiec61850/iec61850_client.h: 552
if _libs["/usr/local/lib/libiec61850.so"].has("ClientSVControlBlock_create", "cdecl"):
    ClientSVControlBlock_create = _libs["/usr/local/lib/libiec61850.so"].get("ClientSVControlBlock_create", "cdecl")
    ClientSVControlBlock_create.argtypes = [IedConnection, String]
    ClientSVControlBlock_create.restype = ClientSVControlBlock

# /usr/local/include/libiec61850/iec61850_client.h: 560
if _libs["/usr/local/lib/libiec61850.so"].has("ClientSVControlBlock_destroy", "cdecl"):
    ClientSVControlBlock_destroy = _libs["/usr/local/lib/libiec61850.so"].get("ClientSVControlBlock_destroy", "cdecl")
    ClientSVControlBlock_destroy.argtypes = [ClientSVControlBlock]
    ClientSVControlBlock_destroy.restype = None

# /usr/local/include/libiec61850/iec61850_client.h: 570
if _libs["/usr/local/lib/libiec61850.so"].has("ClientSVControlBlock_isMulticast", "cdecl"):
    ClientSVControlBlock_isMulticast = _libs["/usr/local/lib/libiec61850.so"].get("ClientSVControlBlock_isMulticast", "cdecl")
    ClientSVControlBlock_isMulticast.argtypes = [ClientSVControlBlock]
    ClientSVControlBlock_isMulticast.restype = c_bool

# /usr/local/include/libiec61850/iec61850_client.h: 580
if _libs["/usr/local/lib/libiec61850.so"].has("ClientSVControlBlock_getLastComError", "cdecl"):
    ClientSVControlBlock_getLastComError = _libs["/usr/local/lib/libiec61850.so"].get("ClientSVControlBlock_getLastComError", "cdecl")
    ClientSVControlBlock_getLastComError.argtypes = [ClientSVControlBlock]
    ClientSVControlBlock_getLastComError.restype = IedClientError

# /usr/local/include/libiec61850/iec61850_client.h: 584
if _libs["/usr/local/lib/libiec61850.so"].has("ClientSVControlBlock_setSvEna", "cdecl"):
    ClientSVControlBlock_setSvEna = _libs["/usr/local/lib/libiec61850.so"].get("ClientSVControlBlock_setSvEna", "cdecl")
    ClientSVControlBlock_setSvEna.argtypes = [ClientSVControlBlock, c_bool]
    ClientSVControlBlock_setSvEna.restype = c_bool

# /usr/local/include/libiec61850/iec61850_client.h: 587
if _libs["/usr/local/lib/libiec61850.so"].has("ClientSVControlBlock_getSvEna", "cdecl"):
    ClientSVControlBlock_getSvEna = _libs["/usr/local/lib/libiec61850.so"].get("ClientSVControlBlock_getSvEna", "cdecl")
    ClientSVControlBlock_getSvEna.argtypes = [ClientSVControlBlock]
    ClientSVControlBlock_getSvEna.restype = c_bool

# /usr/local/include/libiec61850/iec61850_client.h: 590
if _libs["/usr/local/lib/libiec61850.so"].has("ClientSVControlBlock_setResv", "cdecl"):
    ClientSVControlBlock_setResv = _libs["/usr/local/lib/libiec61850.so"].get("ClientSVControlBlock_setResv", "cdecl")
    ClientSVControlBlock_setResv.argtypes = [ClientSVControlBlock, c_bool]
    ClientSVControlBlock_setResv.restype = c_bool

# /usr/local/include/libiec61850/iec61850_client.h: 593
if _libs["/usr/local/lib/libiec61850.so"].has("ClientSVControlBlock_getResv", "cdecl"):
    ClientSVControlBlock_getResv = _libs["/usr/local/lib/libiec61850.so"].get("ClientSVControlBlock_getResv", "cdecl")
    ClientSVControlBlock_getResv.argtypes = [ClientSVControlBlock]
    ClientSVControlBlock_getResv.restype = c_bool

# /usr/local/include/libiec61850/iec61850_client.h: 595
if _libs["/usr/local/lib/libiec61850.so"].has("ClientSVControlBlock_getMsvID", "cdecl"):
    ClientSVControlBlock_getMsvID = _libs["/usr/local/lib/libiec61850.so"].get("ClientSVControlBlock_getMsvID", "cdecl")
    ClientSVControlBlock_getMsvID.argtypes = [ClientSVControlBlock]
    if sizeof(c_int) == sizeof(c_void_p):
        ClientSVControlBlock_getMsvID.restype = ReturnString
    else:
        ClientSVControlBlock_getMsvID.restype = String
        ClientSVControlBlock_getMsvID.errcheck = ReturnString

# /usr/local/include/libiec61850/iec61850_client.h: 609
if _libs["/usr/local/lib/libiec61850.so"].has("ClientSVControlBlock_getDatSet", "cdecl"):
    ClientSVControlBlock_getDatSet = _libs["/usr/local/lib/libiec61850.so"].get("ClientSVControlBlock_getDatSet", "cdecl")
    ClientSVControlBlock_getDatSet.argtypes = [ClientSVControlBlock]
    if sizeof(c_int) == sizeof(c_void_p):
        ClientSVControlBlock_getDatSet.restype = ReturnString
    else:
        ClientSVControlBlock_getDatSet.restype = String
        ClientSVControlBlock_getDatSet.errcheck = ReturnString

# /usr/local/include/libiec61850/iec61850_client.h: 613
if _libs["/usr/local/lib/libiec61850.so"].has("ClientSVControlBlock_getConfRev", "cdecl"):
    ClientSVControlBlock_getConfRev = _libs["/usr/local/lib/libiec61850.so"].get("ClientSVControlBlock_getConfRev", "cdecl")
    ClientSVControlBlock_getConfRev.argtypes = [ClientSVControlBlock]
    ClientSVControlBlock_getConfRev.restype = uint32_t

# /usr/local/include/libiec61850/iec61850_client.h: 616
if _libs["/usr/local/lib/libiec61850.so"].has("ClientSVControlBlock_getSmpRate", "cdecl"):
    ClientSVControlBlock_getSmpRate = _libs["/usr/local/lib/libiec61850.so"].get("ClientSVControlBlock_getSmpRate", "cdecl")
    ClientSVControlBlock_getSmpRate.argtypes = [ClientSVControlBlock]
    ClientSVControlBlock_getSmpRate.restype = uint16_t

# /usr/local/include/libiec61850/iec61850_client.h: 625
if _libs["/usr/local/lib/libiec61850.so"].has("ClientSVControlBlock_getDstAddress", "cdecl"):
    ClientSVControlBlock_getDstAddress = _libs["/usr/local/lib/libiec61850.so"].get("ClientSVControlBlock_getDstAddress", "cdecl")
    ClientSVControlBlock_getDstAddress.argtypes = [ClientSVControlBlock]
    ClientSVControlBlock_getDstAddress.restype = PhyComAddress

# /usr/local/include/libiec61850/iec61850_client.h: 634
if _libs["/usr/local/lib/libiec61850.so"].has("ClientSVControlBlock_getOptFlds", "cdecl"):
    ClientSVControlBlock_getOptFlds = _libs["/usr/local/lib/libiec61850.so"].get("ClientSVControlBlock_getOptFlds", "cdecl")
    ClientSVControlBlock_getOptFlds.argtypes = [ClientSVControlBlock]
    ClientSVControlBlock_getOptFlds.restype = c_int

# /usr/local/include/libiec61850/iec61850_client.h: 642
if _libs["/usr/local/lib/libiec61850.so"].has("ClientSVControlBlock_getSmpMod", "cdecl"):
    ClientSVControlBlock_getSmpMod = _libs["/usr/local/lib/libiec61850.so"].get("ClientSVControlBlock_getSmpMod", "cdecl")
    ClientSVControlBlock_getSmpMod.argtypes = [ClientSVControlBlock]
    ClientSVControlBlock_getSmpMod.restype = uint8_t

# /usr/local/include/libiec61850/iec61850_client.h: 652
if _libs["/usr/local/lib/libiec61850.so"].has("ClientSVControlBlock_getNoASDU", "cdecl"):
    ClientSVControlBlock_getNoASDU = _libs["/usr/local/lib/libiec61850.so"].get("ClientSVControlBlock_getNoASDU", "cdecl")
    ClientSVControlBlock_getNoASDU.argtypes = [ClientSVControlBlock]
    ClientSVControlBlock_getNoASDU.restype = c_int

# /usr/local/include/libiec61850/iec61850_client.h: 703
if _libs["/usr/local/lib/libiec61850.so"].has("ClientGooseControlBlock_create", "cdecl"):
    ClientGooseControlBlock_create = _libs["/usr/local/lib/libiec61850.so"].get("ClientGooseControlBlock_create", "cdecl")
    ClientGooseControlBlock_create.argtypes = [String]
    ClientGooseControlBlock_create.restype = ClientGooseControlBlock

# /usr/local/include/libiec61850/iec61850_client.h: 706
if _libs["/usr/local/lib/libiec61850.so"].has("ClientGooseControlBlock_destroy", "cdecl"):
    ClientGooseControlBlock_destroy = _libs["/usr/local/lib/libiec61850.so"].get("ClientGooseControlBlock_destroy", "cdecl")
    ClientGooseControlBlock_destroy.argtypes = [ClientGooseControlBlock]
    ClientGooseControlBlock_destroy.restype = None

# /usr/local/include/libiec61850/iec61850_client.h: 709
if _libs["/usr/local/lib/libiec61850.so"].has("ClientGooseControlBlock_getGoEna", "cdecl"):
    ClientGooseControlBlock_getGoEna = _libs["/usr/local/lib/libiec61850.so"].get("ClientGooseControlBlock_getGoEna", "cdecl")
    ClientGooseControlBlock_getGoEna.argtypes = [ClientGooseControlBlock]
    ClientGooseControlBlock_getGoEna.restype = c_bool

# /usr/local/include/libiec61850/iec61850_client.h: 712
if _libs["/usr/local/lib/libiec61850.so"].has("ClientGooseControlBlock_setGoEna", "cdecl"):
    ClientGooseControlBlock_setGoEna = _libs["/usr/local/lib/libiec61850.so"].get("ClientGooseControlBlock_setGoEna", "cdecl")
    ClientGooseControlBlock_setGoEna.argtypes = [ClientGooseControlBlock, c_bool]
    ClientGooseControlBlock_setGoEna.restype = None

# /usr/local/include/libiec61850/iec61850_client.h: 714
if _libs["/usr/local/lib/libiec61850.so"].has("ClientGooseControlBlock_getGoID", "cdecl"):
    ClientGooseControlBlock_getGoID = _libs["/usr/local/lib/libiec61850.so"].get("ClientGooseControlBlock_getGoID", "cdecl")
    ClientGooseControlBlock_getGoID.argtypes = [ClientGooseControlBlock]
    ClientGooseControlBlock_getGoID.restype = c_char_p

# /usr/local/include/libiec61850/iec61850_client.h: 718
if _libs["/usr/local/lib/libiec61850.so"].has("ClientGooseControlBlock_setGoID", "cdecl"):
    ClientGooseControlBlock_setGoID = _libs["/usr/local/lib/libiec61850.so"].get("ClientGooseControlBlock_setGoID", "cdecl")
    ClientGooseControlBlock_setGoID.argtypes = [ClientGooseControlBlock, String]
    ClientGooseControlBlock_setGoID.restype = None

# /usr/local/include/libiec61850/iec61850_client.h: 720
if _libs["/usr/local/lib/libiec61850.so"].has("ClientGooseControlBlock_getDatSet", "cdecl"):
    ClientGooseControlBlock_getDatSet = _libs["/usr/local/lib/libiec61850.so"].get("ClientGooseControlBlock_getDatSet", "cdecl")
    ClientGooseControlBlock_getDatSet.argtypes = [ClientGooseControlBlock]
    ClientGooseControlBlock_getDatSet.restype = c_char_p

# /usr/local/include/libiec61850/iec61850_client.h: 724
if _libs["/usr/local/lib/libiec61850.so"].has("ClientGooseControlBlock_setDatSet", "cdecl"):
    ClientGooseControlBlock_setDatSet = _libs["/usr/local/lib/libiec61850.so"].get("ClientGooseControlBlock_setDatSet", "cdecl")
    ClientGooseControlBlock_setDatSet.argtypes = [ClientGooseControlBlock, String]
    ClientGooseControlBlock_setDatSet.restype = None

# /usr/local/include/libiec61850/iec61850_client.h: 727
if _libs["/usr/local/lib/libiec61850.so"].has("ClientGooseControlBlock_getConfRev", "cdecl"):
    ClientGooseControlBlock_getConfRev = _libs["/usr/local/lib/libiec61850.so"].get("ClientGooseControlBlock_getConfRev", "cdecl")
    ClientGooseControlBlock_getConfRev.argtypes = [ClientGooseControlBlock]
    ClientGooseControlBlock_getConfRev.restype = uint32_t

# /usr/local/include/libiec61850/iec61850_client.h: 730
if _libs["/usr/local/lib/libiec61850.so"].has("ClientGooseControlBlock_getNdsComm", "cdecl"):
    ClientGooseControlBlock_getNdsComm = _libs["/usr/local/lib/libiec61850.so"].get("ClientGooseControlBlock_getNdsComm", "cdecl")
    ClientGooseControlBlock_getNdsComm.argtypes = [ClientGooseControlBlock]
    ClientGooseControlBlock_getNdsComm.restype = c_bool

# /usr/local/include/libiec61850/iec61850_client.h: 733
if _libs["/usr/local/lib/libiec61850.so"].has("ClientGooseControlBlock_getMinTime", "cdecl"):
    ClientGooseControlBlock_getMinTime = _libs["/usr/local/lib/libiec61850.so"].get("ClientGooseControlBlock_getMinTime", "cdecl")
    ClientGooseControlBlock_getMinTime.argtypes = [ClientGooseControlBlock]
    ClientGooseControlBlock_getMinTime.restype = uint32_t

# /usr/local/include/libiec61850/iec61850_client.h: 736
if _libs["/usr/local/lib/libiec61850.so"].has("ClientGooseControlBlock_getMaxTime", "cdecl"):
    ClientGooseControlBlock_getMaxTime = _libs["/usr/local/lib/libiec61850.so"].get("ClientGooseControlBlock_getMaxTime", "cdecl")
    ClientGooseControlBlock_getMaxTime.argtypes = [ClientGooseControlBlock]
    ClientGooseControlBlock_getMaxTime.restype = uint32_t

# /usr/local/include/libiec61850/iec61850_client.h: 739
if _libs["/usr/local/lib/libiec61850.so"].has("ClientGooseControlBlock_getFixedOffs", "cdecl"):
    ClientGooseControlBlock_getFixedOffs = _libs["/usr/local/lib/libiec61850.so"].get("ClientGooseControlBlock_getFixedOffs", "cdecl")
    ClientGooseControlBlock_getFixedOffs.argtypes = [ClientGooseControlBlock]
    ClientGooseControlBlock_getFixedOffs.restype = c_bool

# /usr/local/include/libiec61850/iec61850_client.h: 742
if _libs["/usr/local/lib/libiec61850.so"].has("ClientGooseControlBlock_getDstAddress", "cdecl"):
    ClientGooseControlBlock_getDstAddress = _libs["/usr/local/lib/libiec61850.so"].get("ClientGooseControlBlock_getDstAddress", "cdecl")
    ClientGooseControlBlock_getDstAddress.argtypes = [ClientGooseControlBlock]
    ClientGooseControlBlock_getDstAddress.restype = PhyComAddress

# /usr/local/include/libiec61850/iec61850_client.h: 745
if _libs["/usr/local/lib/libiec61850.so"].has("ClientGooseControlBlock_setDstAddress", "cdecl"):
    ClientGooseControlBlock_setDstAddress = _libs["/usr/local/lib/libiec61850.so"].get("ClientGooseControlBlock_setDstAddress", "cdecl")
    ClientGooseControlBlock_setDstAddress.argtypes = [ClientGooseControlBlock, PhyComAddress]
    ClientGooseControlBlock_setDstAddress.restype = None

# /usr/local/include/libiec61850/iec61850_client.h: 747
if _libs["/usr/local/lib/libiec61850.so"].has("ClientGooseControlBlock_getDstAddress_addr", "cdecl"):
    ClientGooseControlBlock_getDstAddress_addr = _libs["/usr/local/lib/libiec61850.so"].get("ClientGooseControlBlock_getDstAddress_addr", "cdecl")
    ClientGooseControlBlock_getDstAddress_addr.argtypes = [ClientGooseControlBlock]
    ClientGooseControlBlock_getDstAddress_addr.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/iec61850_client.h: 751
if _libs["/usr/local/lib/libiec61850.so"].has("ClientGooseControlBlock_setDstAddress_addr", "cdecl"):
    ClientGooseControlBlock_setDstAddress_addr = _libs["/usr/local/lib/libiec61850.so"].get("ClientGooseControlBlock_setDstAddress_addr", "cdecl")
    ClientGooseControlBlock_setDstAddress_addr.argtypes = [ClientGooseControlBlock, POINTER(MmsValue)]
    ClientGooseControlBlock_setDstAddress_addr.restype = None

# /usr/local/include/libiec61850/iec61850_client.h: 754
if _libs["/usr/local/lib/libiec61850.so"].has("ClientGooseControlBlock_getDstAddress_priority", "cdecl"):
    ClientGooseControlBlock_getDstAddress_priority = _libs["/usr/local/lib/libiec61850.so"].get("ClientGooseControlBlock_getDstAddress_priority", "cdecl")
    ClientGooseControlBlock_getDstAddress_priority.argtypes = [ClientGooseControlBlock]
    ClientGooseControlBlock_getDstAddress_priority.restype = uint8_t

# /usr/local/include/libiec61850/iec61850_client.h: 757
if _libs["/usr/local/lib/libiec61850.so"].has("ClientGooseControlBlock_setDstAddress_priority", "cdecl"):
    ClientGooseControlBlock_setDstAddress_priority = _libs["/usr/local/lib/libiec61850.so"].get("ClientGooseControlBlock_setDstAddress_priority", "cdecl")
    ClientGooseControlBlock_setDstAddress_priority.argtypes = [ClientGooseControlBlock, uint8_t]
    ClientGooseControlBlock_setDstAddress_priority.restype = None

# /usr/local/include/libiec61850/iec61850_client.h: 760
if _libs["/usr/local/lib/libiec61850.so"].has("ClientGooseControlBlock_getDstAddress_vid", "cdecl"):
    ClientGooseControlBlock_getDstAddress_vid = _libs["/usr/local/lib/libiec61850.so"].get("ClientGooseControlBlock_getDstAddress_vid", "cdecl")
    ClientGooseControlBlock_getDstAddress_vid.argtypes = [ClientGooseControlBlock]
    ClientGooseControlBlock_getDstAddress_vid.restype = uint16_t

# /usr/local/include/libiec61850/iec61850_client.h: 763
if _libs["/usr/local/lib/libiec61850.so"].has("ClientGooseControlBlock_setDstAddress_vid", "cdecl"):
    ClientGooseControlBlock_setDstAddress_vid = _libs["/usr/local/lib/libiec61850.so"].get("ClientGooseControlBlock_setDstAddress_vid", "cdecl")
    ClientGooseControlBlock_setDstAddress_vid.argtypes = [ClientGooseControlBlock, uint16_t]
    ClientGooseControlBlock_setDstAddress_vid.restype = None

# /usr/local/include/libiec61850/iec61850_client.h: 766
if _libs["/usr/local/lib/libiec61850.so"].has("ClientGooseControlBlock_getDstAddress_appid", "cdecl"):
    ClientGooseControlBlock_getDstAddress_appid = _libs["/usr/local/lib/libiec61850.so"].get("ClientGooseControlBlock_getDstAddress_appid", "cdecl")
    ClientGooseControlBlock_getDstAddress_appid.argtypes = [ClientGooseControlBlock]
    ClientGooseControlBlock_getDstAddress_appid.restype = uint16_t

# /usr/local/include/libiec61850/iec61850_client.h: 769
if _libs["/usr/local/lib/libiec61850.so"].has("ClientGooseControlBlock_setDstAddress_appid", "cdecl"):
    ClientGooseControlBlock_setDstAddress_appid = _libs["/usr/local/lib/libiec61850.so"].get("ClientGooseControlBlock_setDstAddress_appid", "cdecl")
    ClientGooseControlBlock_setDstAddress_appid.argtypes = [ClientGooseControlBlock, uint16_t]
    ClientGooseControlBlock_setDstAddress_appid.restype = None

# /usr/local/include/libiec61850/iec61850_client.h: 804
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_getGoCBValues", "cdecl"):
    IedConnection_getGoCBValues = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_getGoCBValues", "cdecl")
    IedConnection_getGoCBValues.argtypes = [IedConnection, POINTER(IedClientError), String, ClientGooseControlBlock]
    IedConnection_getGoCBValues.restype = ClientGooseControlBlock

# /usr/local/include/libiec61850/iec61850_client.h: 828
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_setGoCBValues", "cdecl"):
    IedConnection_setGoCBValues = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_setGoCBValues", "cdecl")
    IedConnection_setGoCBValues.argtypes = [IedConnection, POINTER(IedClientError), ClientGooseControlBlock, uint32_t, c_bool]
    IedConnection_setGoCBValues.restype = None

# /usr/local/include/libiec61850/iec61850_client.h: 854
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_readObject", "cdecl"):
    IedConnection_readObject = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_readObject", "cdecl")
    IedConnection_readObject.argtypes = [IedConnection, POINTER(IedClientError), String, FunctionalConstraint]
    IedConnection_readObject.restype = POINTER(MmsValue)

IedConnection_ReadObjectHandler = CFUNCTYPE(UNCHECKED(None), uint32_t, POINTER(None), IedClientError, POINTER(MmsValue))# /usr/local/include/libiec61850/iec61850_client.h: 858

# /usr/local/include/libiec61850/iec61850_client.h: 873
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_readObjectAsync", "cdecl"):
    IedConnection_readObjectAsync = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_readObjectAsync", "cdecl")
    IedConnection_readObjectAsync.argtypes = [IedConnection, POINTER(IedClientError), String, FunctionalConstraint, IedConnection_ReadObjectHandler, POINTER(None)]
    IedConnection_readObjectAsync.restype = uint32_t

# /usr/local/include/libiec61850/iec61850_client.h: 886
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_writeObject", "cdecl"):
    IedConnection_writeObject = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_writeObject", "cdecl")
    IedConnection_writeObject.argtypes = [IedConnection, POINTER(IedClientError), String, FunctionalConstraint, POINTER(MmsValue)]
    IedConnection_writeObject.restype = None

# /usr/local/include/libiec61850/iec61850_client.h: 903
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_writeObjectAsync", "cdecl"):
    IedConnection_writeObjectAsync = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_writeObjectAsync", "cdecl")
    IedConnection_writeObjectAsync.argtypes = [IedConnection, POINTER(IedClientError), String, FunctionalConstraint, POINTER(MmsValue), IedConnection_GenericServiceHandler, POINTER(None)]
    IedConnection_writeObjectAsync.restype = uint32_t

# /usr/local/include/libiec61850/iec61850_client.h: 915
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_readBooleanValue", "cdecl"):
    IedConnection_readBooleanValue = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_readBooleanValue", "cdecl")
    IedConnection_readBooleanValue.argtypes = [IedConnection, POINTER(IedClientError), String, FunctionalConstraint]
    IedConnection_readBooleanValue.restype = c_bool

# /usr/local/include/libiec61850/iec61850_client.h: 926
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_readFloatValue", "cdecl"):
    IedConnection_readFloatValue = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_readFloatValue", "cdecl")
    IedConnection_readFloatValue.argtypes = [IedConnection, POINTER(IedClientError), String, FunctionalConstraint]
    IedConnection_readFloatValue.restype = c_float

# /usr/local/include/libiec61850/iec61850_client.h: 940
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_readStringValue", "cdecl"):
    IedConnection_readStringValue = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_readStringValue", "cdecl")
    IedConnection_readStringValue.argtypes = [IedConnection, POINTER(IedClientError), String, FunctionalConstraint]
    if sizeof(c_int) == sizeof(c_void_p):
        IedConnection_readStringValue.restype = ReturnString
    else:
        IedConnection_readStringValue.restype = String
        IedConnection_readStringValue.errcheck = ReturnString

# /usr/local/include/libiec61850/iec61850_client.h: 954
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_readInt32Value", "cdecl"):
    IedConnection_readInt32Value = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_readInt32Value", "cdecl")
    IedConnection_readInt32Value.argtypes = [IedConnection, POINTER(IedClientError), String, FunctionalConstraint]
    IedConnection_readInt32Value.restype = c_int32

# /usr/local/include/libiec61850/iec61850_client.h: 967
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_readInt64Value", "cdecl"):
    IedConnection_readInt64Value = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_readInt64Value", "cdecl")
    IedConnection_readInt64Value.argtypes = [IedConnection, POINTER(IedClientError), String, FunctionalConstraint]
    IedConnection_readInt64Value.restype = c_int64

# /usr/local/include/libiec61850/iec61850_client.h: 980
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_readUnsigned32Value", "cdecl"):
    IedConnection_readUnsigned32Value = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_readUnsigned32Value", "cdecl")
    IedConnection_readUnsigned32Value.argtypes = [IedConnection, POINTER(IedClientError), String, FunctionalConstraint]
    IedConnection_readUnsigned32Value.restype = uint32_t

# /usr/local/include/libiec61850/iec61850_client.h: 997
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_readTimestampValue", "cdecl"):
    IedConnection_readTimestampValue = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_readTimestampValue", "cdecl")
    IedConnection_readTimestampValue.argtypes = [IedConnection, POINTER(IedClientError), String, FunctionalConstraint, POINTER(Timestamp)]
    IedConnection_readTimestampValue.restype = POINTER(Timestamp)

# /usr/local/include/libiec61850/iec61850_client.h: 1012
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_readQualityValue", "cdecl"):
    IedConnection_readQualityValue = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_readQualityValue", "cdecl")
    IedConnection_readQualityValue.argtypes = [IedConnection, POINTER(IedClientError), String, FunctionalConstraint]
    IedConnection_readQualityValue.restype = Quality

# /usr/local/include/libiec61850/iec61850_client.h: 1024
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_writeBooleanValue", "cdecl"):
    IedConnection_writeBooleanValue = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_writeBooleanValue", "cdecl")
    IedConnection_writeBooleanValue.argtypes = [IedConnection, POINTER(IedClientError), String, FunctionalConstraint, c_bool]
    IedConnection_writeBooleanValue.restype = None

# /usr/local/include/libiec61850/iec61850_client.h: 1037
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_writeInt32Value", "cdecl"):
    IedConnection_writeInt32Value = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_writeInt32Value", "cdecl")
    IedConnection_writeInt32Value.argtypes = [IedConnection, POINTER(IedClientError), String, FunctionalConstraint, c_int32]
    IedConnection_writeInt32Value.restype = None

# /usr/local/include/libiec61850/iec61850_client.h: 1050
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_writeUnsigned32Value", "cdecl"):
    IedConnection_writeUnsigned32Value = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_writeUnsigned32Value", "cdecl")
    IedConnection_writeUnsigned32Value.argtypes = [IedConnection, POINTER(IedClientError), String, FunctionalConstraint, uint32_t]
    IedConnection_writeUnsigned32Value.restype = None

# /usr/local/include/libiec61850/iec61850_client.h: 1063
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_writeFloatValue", "cdecl"):
    IedConnection_writeFloatValue = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_writeFloatValue", "cdecl")
    IedConnection_writeFloatValue.argtypes = [IedConnection, POINTER(IedClientError), String, FunctionalConstraint, c_float]
    IedConnection_writeFloatValue.restype = None

# /usr/local/include/libiec61850/iec61850_client.h: 1067
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_writeVisibleStringValue", "cdecl"):
    IedConnection_writeVisibleStringValue = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_writeVisibleStringValue", "cdecl")
    IedConnection_writeVisibleStringValue.argtypes = [IedConnection, POINTER(IedClientError), String, FunctionalConstraint, String]
    IedConnection_writeVisibleStringValue.restype = None

# /usr/local/include/libiec61850/iec61850_client.h: 1071
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_writeOctetString", "cdecl"):
    IedConnection_writeOctetString = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_writeOctetString", "cdecl")
    IedConnection_writeOctetString.argtypes = [IedConnection, POINTER(IedClientError), String, FunctionalConstraint, POINTER(uint8_t), c_int]
    IedConnection_writeOctetString.restype = None

# /usr/local/include/libiec61850/iec61850_client.h: 1120
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_getRCBValues", "cdecl"):
    IedConnection_getRCBValues = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_getRCBValues", "cdecl")
    IedConnection_getRCBValues.argtypes = [IedConnection, POINTER(IedClientError), String, ClientReportControlBlock]
    IedConnection_getRCBValues.restype = ClientReportControlBlock

IedConnection_GetRCBValuesHandler = CFUNCTYPE(UNCHECKED(None), uint32_t, POINTER(None), IedClientError, ClientReportControlBlock)# /usr/local/include/libiec61850/iec61850_client.h: 1124

# /usr/local/include/libiec61850/iec61850_client.h: 1127
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_getRCBValuesAsync", "cdecl"):
    IedConnection_getRCBValuesAsync = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_getRCBValuesAsync", "cdecl")
    IedConnection_getRCBValuesAsync.argtypes = [IedConnection, POINTER(IedClientError), String, ClientReportControlBlock, IedConnection_GetRCBValuesHandler, POINTER(None)]
    IedConnection_getRCBValuesAsync.restype = uint32_t

ReasonForInclusion = c_int# /usr/local/include/libiec61850/iec61850_client.h: 1131

# /usr/local/include/libiec61850/iec61850_client.h: 1235
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_setRCBValues", "cdecl"):
    IedConnection_setRCBValues = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_setRCBValues", "cdecl")
    IedConnection_setRCBValues.argtypes = [IedConnection, POINTER(IedClientError), ClientReportControlBlock, uint32_t, c_bool]
    IedConnection_setRCBValues.restype = None

# /usr/local/include/libiec61850/iec61850_client.h: 1239
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_setRCBValuesAsync", "cdecl"):
    IedConnection_setRCBValuesAsync = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_setRCBValuesAsync", "cdecl")
    IedConnection_setRCBValuesAsync.argtypes = [IedConnection, POINTER(IedClientError), ClientReportControlBlock, uint32_t, c_bool, IedConnection_GenericServiceHandler, POINTER(None)]
    IedConnection_setRCBValuesAsync.restype = uint32_t

ReportCallbackFunction = CFUNCTYPE(UNCHECKED(None), POINTER(None), ClientReport)# /usr/local/include/libiec61850/iec61850_client.h: 1248

# /usr/local/include/libiec61850/iec61850_client.h: 1270
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_installReportHandler", "cdecl"):
    IedConnection_installReportHandler = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_installReportHandler", "cdecl")
    IedConnection_installReportHandler.argtypes = [IedConnection, String, String, ReportCallbackFunction, POINTER(None)]
    IedConnection_installReportHandler.restype = None

# /usr/local/include/libiec61850/iec61850_client.h: 1280
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_uninstallReportHandler", "cdecl"):
    IedConnection_uninstallReportHandler = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_uninstallReportHandler", "cdecl")
    IedConnection_uninstallReportHandler.argtypes = [IedConnection, String]
    IedConnection_uninstallReportHandler.restype = None

# /usr/local/include/libiec61850/iec61850_client.h: 1294
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_triggerGIReport", "cdecl"):
    IedConnection_triggerGIReport = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_triggerGIReport", "cdecl")
    IedConnection_triggerGIReport.argtypes = [IedConnection, POINTER(IedClientError), String]
    IedConnection_triggerGIReport.restype = None

# /usr/local/include/libiec61850/iec61850_client.h: 1308
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReport_getDataSetName", "cdecl"):
    ClientReport_getDataSetName = _libs["/usr/local/lib/libiec61850.so"].get("ClientReport_getDataSetName", "cdecl")
    ClientReport_getDataSetName.argtypes = [ClientReport]
    ClientReport_getDataSetName.restype = c_char_p

# /usr/local/include/libiec61850/iec61850_client.h: 1321
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReport_getDataSetValues", "cdecl"):
    ClientReport_getDataSetValues = _libs["/usr/local/lib/libiec61850.so"].get("ClientReport_getDataSetValues", "cdecl")
    ClientReport_getDataSetValues.argtypes = [ClientReport]
    ClientReport_getDataSetValues.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/iec61850_client.h: 1330
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReport_getRcbReference", "cdecl"):
    ClientReport_getRcbReference = _libs["/usr/local/lib/libiec61850.so"].get("ClientReport_getRcbReference", "cdecl")
    ClientReport_getRcbReference.argtypes = [ClientReport]
    if sizeof(c_int) == sizeof(c_void_p):
        ClientReport_getRcbReference.restype = ReturnString
    else:
        ClientReport_getRcbReference.restype = String
        ClientReport_getRcbReference.errcheck = ReturnString

# /usr/local/include/libiec61850/iec61850_client.h: 1339
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReport_getRptId", "cdecl"):
    ClientReport_getRptId = _libs["/usr/local/lib/libiec61850.so"].get("ClientReport_getRptId", "cdecl")
    ClientReport_getRptId.argtypes = [ClientReport]
    if sizeof(c_int) == sizeof(c_void_p):
        ClientReport_getRptId.restype = ReturnString
    else:
        ClientReport_getRptId.restype = String
        ClientReport_getRptId.errcheck = ReturnString

# /usr/local/include/libiec61850/iec61850_client.h: 1351
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReport_getReasonForInclusion", "cdecl"):
    ClientReport_getReasonForInclusion = _libs["/usr/local/lib/libiec61850.so"].get("ClientReport_getReasonForInclusion", "cdecl")
    ClientReport_getReasonForInclusion.argtypes = [ClientReport, c_int]
    ClientReport_getReasonForInclusion.restype = ReasonForInclusion

# /usr/local/include/libiec61850/iec61850_client.h: 1362
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReport_getEntryId", "cdecl"):
    ClientReport_getEntryId = _libs["/usr/local/lib/libiec61850.so"].get("ClientReport_getEntryId", "cdecl")
    ClientReport_getEntryId.argtypes = [ClientReport]
    ClientReport_getEntryId.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/iec61850_client.h: 1373
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReport_hasTimestamp", "cdecl"):
    ClientReport_hasTimestamp = _libs["/usr/local/lib/libiec61850.so"].get("ClientReport_hasTimestamp", "cdecl")
    ClientReport_hasTimestamp.argtypes = [ClientReport]
    ClientReport_hasTimestamp.restype = c_bool

# /usr/local/include/libiec61850/iec61850_client.h: 1383
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReport_hasSeqNum", "cdecl"):
    ClientReport_hasSeqNum = _libs["/usr/local/lib/libiec61850.so"].get("ClientReport_hasSeqNum", "cdecl")
    ClientReport_hasSeqNum.argtypes = [ClientReport]
    ClientReport_hasSeqNum.restype = c_bool

# /usr/local/include/libiec61850/iec61850_client.h: 1395
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReport_getSeqNum", "cdecl"):
    ClientReport_getSeqNum = _libs["/usr/local/lib/libiec61850.so"].get("ClientReport_getSeqNum", "cdecl")
    ClientReport_getSeqNum.argtypes = [ClientReport]
    ClientReport_getSeqNum.restype = uint16_t

# /usr/local/include/libiec61850/iec61850_client.h: 1405
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReport_hasDataSetName", "cdecl"):
    ClientReport_hasDataSetName = _libs["/usr/local/lib/libiec61850.so"].get("ClientReport_hasDataSetName", "cdecl")
    ClientReport_hasDataSetName.argtypes = [ClientReport]
    ClientReport_hasDataSetName.restype = c_bool

# /usr/local/include/libiec61850/iec61850_client.h: 1415
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReport_hasReasonForInclusion", "cdecl"):
    ClientReport_hasReasonForInclusion = _libs["/usr/local/lib/libiec61850.so"].get("ClientReport_hasReasonForInclusion", "cdecl")
    ClientReport_hasReasonForInclusion.argtypes = [ClientReport]
    ClientReport_hasReasonForInclusion.restype = c_bool

# /usr/local/include/libiec61850/iec61850_client.h: 1425
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReport_hasConfRev", "cdecl"):
    ClientReport_hasConfRev = _libs["/usr/local/lib/libiec61850.so"].get("ClientReport_hasConfRev", "cdecl")
    ClientReport_hasConfRev.argtypes = [ClientReport]
    ClientReport_hasConfRev.restype = c_bool

# /usr/local/include/libiec61850/iec61850_client.h: 1437
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReport_getConfRev", "cdecl"):
    ClientReport_getConfRev = _libs["/usr/local/lib/libiec61850.so"].get("ClientReport_getConfRev", "cdecl")
    ClientReport_getConfRev.argtypes = [ClientReport]
    ClientReport_getConfRev.restype = uint32_t

# /usr/local/include/libiec61850/iec61850_client.h: 1447
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReport_hasBufOvfl", "cdecl"):
    ClientReport_hasBufOvfl = _libs["/usr/local/lib/libiec61850.so"].get("ClientReport_hasBufOvfl", "cdecl")
    ClientReport_hasBufOvfl.argtypes = [ClientReport]
    ClientReport_hasBufOvfl.restype = c_bool

# /usr/local/include/libiec61850/iec61850_client.h: 1457
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReport_getBufOvfl", "cdecl"):
    ClientReport_getBufOvfl = _libs["/usr/local/lib/libiec61850.so"].get("ClientReport_getBufOvfl", "cdecl")
    ClientReport_getBufOvfl.argtypes = [ClientReport]
    ClientReport_getBufOvfl.restype = c_bool

# /usr/local/include/libiec61850/iec61850_client.h: 1467
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReport_hasDataReference", "cdecl"):
    ClientReport_hasDataReference = _libs["/usr/local/lib/libiec61850.so"].get("ClientReport_hasDataReference", "cdecl")
    ClientReport_hasDataReference.argtypes = [ClientReport]
    ClientReport_hasDataReference.restype = c_bool

# /usr/local/include/libiec61850/iec61850_client.h: 1482
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReport_getDataReference", "cdecl"):
    ClientReport_getDataReference = _libs["/usr/local/lib/libiec61850.so"].get("ClientReport_getDataReference", "cdecl")
    ClientReport_getDataReference.argtypes = [ClientReport, c_int]
    ClientReport_getDataReference.restype = c_char_p

# /usr/local/include/libiec61850/iec61850_client.h: 1497
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReport_getTimestamp", "cdecl"):
    ClientReport_getTimestamp = _libs["/usr/local/lib/libiec61850.so"].get("ClientReport_getTimestamp", "cdecl")
    ClientReport_getTimestamp.argtypes = [ClientReport]
    ClientReport_getTimestamp.restype = uint64_t

# /usr/local/include/libiec61850/iec61850_client.h: 1507
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReport_hasSubSeqNum", "cdecl"):
    ClientReport_hasSubSeqNum = _libs["/usr/local/lib/libiec61850.so"].get("ClientReport_hasSubSeqNum", "cdecl")
    ClientReport_hasSubSeqNum.argtypes = [ClientReport]
    ClientReport_hasSubSeqNum.restype = c_bool

# /usr/local/include/libiec61850/iec61850_client.h: 1520
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReport_getSubSeqNum", "cdecl"):
    ClientReport_getSubSeqNum = _libs["/usr/local/lib/libiec61850.so"].get("ClientReport_getSubSeqNum", "cdecl")
    ClientReport_getSubSeqNum.argtypes = [ClientReport]
    ClientReport_getSubSeqNum.restype = uint16_t

# /usr/local/include/libiec61850/iec61850_client.h: 1533
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReport_getMoreSeqmentsFollow", "cdecl"):
    ClientReport_getMoreSeqmentsFollow = _libs["/usr/local/lib/libiec61850.so"].get("ClientReport_getMoreSeqmentsFollow", "cdecl")
    ClientReport_getMoreSeqmentsFollow.argtypes = [ClientReport]
    ClientReport_getMoreSeqmentsFollow.restype = c_bool

# /usr/local/include/libiec61850/iec61850_client.h: 1542
if _libs["/usr/local/lib/libiec61850.so"].has("ReasonForInclusion_getValueAsString", "cdecl"):
    ReasonForInclusion_getValueAsString = _libs["/usr/local/lib/libiec61850.so"].get("ReasonForInclusion_getValueAsString", "cdecl")
    ReasonForInclusion_getValueAsString.argtypes = [ReasonForInclusion]
    if sizeof(c_int) == sizeof(c_void_p):
        ReasonForInclusion_getValueAsString.restype = ReturnString
    else:
        ReasonForInclusion_getValueAsString.restype = String
        ReasonForInclusion_getValueAsString.errcheck = ReturnString

# /usr/local/include/libiec61850/iec61850_client.h: 1550
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReportControlBlock_create", "cdecl"):
    ClientReportControlBlock_create = _libs["/usr/local/lib/libiec61850.so"].get("ClientReportControlBlock_create", "cdecl")
    ClientReportControlBlock_create.argtypes = [String]
    ClientReportControlBlock_create.restype = ClientReportControlBlock

# /usr/local/include/libiec61850/iec61850_client.h: 1553
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReportControlBlock_destroy", "cdecl"):
    ClientReportControlBlock_destroy = _libs["/usr/local/lib/libiec61850.so"].get("ClientReportControlBlock_destroy", "cdecl")
    ClientReportControlBlock_destroy.argtypes = [ClientReportControlBlock]
    ClientReportControlBlock_destroy.restype = None

# /usr/local/include/libiec61850/iec61850_client.h: 1555
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReportControlBlock_getObjectReference", "cdecl"):
    ClientReportControlBlock_getObjectReference = _libs["/usr/local/lib/libiec61850.so"].get("ClientReportControlBlock_getObjectReference", "cdecl")
    ClientReportControlBlock_getObjectReference.argtypes = [ClientReportControlBlock]
    if sizeof(c_int) == sizeof(c_void_p):
        ClientReportControlBlock_getObjectReference.restype = ReturnString
    else:
        ClientReportControlBlock_getObjectReference.restype = String
        ClientReportControlBlock_getObjectReference.errcheck = ReturnString

# /usr/local/include/libiec61850/iec61850_client.h: 1559
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReportControlBlock_isBuffered", "cdecl"):
    ClientReportControlBlock_isBuffered = _libs["/usr/local/lib/libiec61850.so"].get("ClientReportControlBlock_isBuffered", "cdecl")
    ClientReportControlBlock_isBuffered.argtypes = [ClientReportControlBlock]
    ClientReportControlBlock_isBuffered.restype = c_bool

# /usr/local/include/libiec61850/iec61850_client.h: 1561
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReportControlBlock_getRptId", "cdecl"):
    ClientReportControlBlock_getRptId = _libs["/usr/local/lib/libiec61850.so"].get("ClientReportControlBlock_getRptId", "cdecl")
    ClientReportControlBlock_getRptId.argtypes = [ClientReportControlBlock]
    ClientReportControlBlock_getRptId.restype = c_char_p

# /usr/local/include/libiec61850/iec61850_client.h: 1565
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReportControlBlock_setRptId", "cdecl"):
    ClientReportControlBlock_setRptId = _libs["/usr/local/lib/libiec61850.so"].get("ClientReportControlBlock_setRptId", "cdecl")
    ClientReportControlBlock_setRptId.argtypes = [ClientReportControlBlock, String]
    ClientReportControlBlock_setRptId.restype = None

# /usr/local/include/libiec61850/iec61850_client.h: 1568
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReportControlBlock_getRptEna", "cdecl"):
    ClientReportControlBlock_getRptEna = _libs["/usr/local/lib/libiec61850.so"].get("ClientReportControlBlock_getRptEna", "cdecl")
    ClientReportControlBlock_getRptEna.argtypes = [ClientReportControlBlock]
    ClientReportControlBlock_getRptEna.restype = c_bool

# /usr/local/include/libiec61850/iec61850_client.h: 1571
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReportControlBlock_setRptEna", "cdecl"):
    ClientReportControlBlock_setRptEna = _libs["/usr/local/lib/libiec61850.so"].get("ClientReportControlBlock_setRptEna", "cdecl")
    ClientReportControlBlock_setRptEna.argtypes = [ClientReportControlBlock, c_bool]
    ClientReportControlBlock_setRptEna.restype = None

# /usr/local/include/libiec61850/iec61850_client.h: 1574
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReportControlBlock_getResv", "cdecl"):
    ClientReportControlBlock_getResv = _libs["/usr/local/lib/libiec61850.so"].get("ClientReportControlBlock_getResv", "cdecl")
    ClientReportControlBlock_getResv.argtypes = [ClientReportControlBlock]
    ClientReportControlBlock_getResv.restype = c_bool

# /usr/local/include/libiec61850/iec61850_client.h: 1577
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReportControlBlock_setResv", "cdecl"):
    ClientReportControlBlock_setResv = _libs["/usr/local/lib/libiec61850.so"].get("ClientReportControlBlock_setResv", "cdecl")
    ClientReportControlBlock_setResv.argtypes = [ClientReportControlBlock, c_bool]
    ClientReportControlBlock_setResv.restype = None

# /usr/local/include/libiec61850/iec61850_client.h: 1579
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReportControlBlock_getDataSetReference", "cdecl"):
    ClientReportControlBlock_getDataSetReference = _libs["/usr/local/lib/libiec61850.so"].get("ClientReportControlBlock_getDataSetReference", "cdecl")
    ClientReportControlBlock_getDataSetReference.argtypes = [ClientReportControlBlock]
    ClientReportControlBlock_getDataSetReference.restype = c_char_p

# /usr/local/include/libiec61850/iec61850_client.h: 1599
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReportControlBlock_setDataSetReference", "cdecl"):
    ClientReportControlBlock_setDataSetReference = _libs["/usr/local/lib/libiec61850.so"].get("ClientReportControlBlock_setDataSetReference", "cdecl")
    ClientReportControlBlock_setDataSetReference.argtypes = [ClientReportControlBlock, String]
    ClientReportControlBlock_setDataSetReference.restype = None

# /usr/local/include/libiec61850/iec61850_client.h: 1602
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReportControlBlock_getConfRev", "cdecl"):
    ClientReportControlBlock_getConfRev = _libs["/usr/local/lib/libiec61850.so"].get("ClientReportControlBlock_getConfRev", "cdecl")
    ClientReportControlBlock_getConfRev.argtypes = [ClientReportControlBlock]
    ClientReportControlBlock_getConfRev.restype = uint32_t

# /usr/local/include/libiec61850/iec61850_client.h: 1612
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReportControlBlock_getOptFlds", "cdecl"):
    ClientReportControlBlock_getOptFlds = _libs["/usr/local/lib/libiec61850.so"].get("ClientReportControlBlock_getOptFlds", "cdecl")
    ClientReportControlBlock_getOptFlds.argtypes = [ClientReportControlBlock]
    ClientReportControlBlock_getOptFlds.restype = c_int

# /usr/local/include/libiec61850/iec61850_client.h: 1621
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReportControlBlock_setOptFlds", "cdecl"):
    ClientReportControlBlock_setOptFlds = _libs["/usr/local/lib/libiec61850.so"].get("ClientReportControlBlock_setOptFlds", "cdecl")
    ClientReportControlBlock_setOptFlds.argtypes = [ClientReportControlBlock, c_int]
    ClientReportControlBlock_setOptFlds.restype = None

# /usr/local/include/libiec61850/iec61850_client.h: 1632
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReportControlBlock_getBufTm", "cdecl"):
    ClientReportControlBlock_getBufTm = _libs["/usr/local/lib/libiec61850.so"].get("ClientReportControlBlock_getBufTm", "cdecl")
    ClientReportControlBlock_getBufTm.argtypes = [ClientReportControlBlock]
    ClientReportControlBlock_getBufTm.restype = uint32_t

# /usr/local/include/libiec61850/iec61850_client.h: 1644
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReportControlBlock_setBufTm", "cdecl"):
    ClientReportControlBlock_setBufTm = _libs["/usr/local/lib/libiec61850.so"].get("ClientReportControlBlock_setBufTm", "cdecl")
    ClientReportControlBlock_setBufTm.argtypes = [ClientReportControlBlock, uint32_t]
    ClientReportControlBlock_setBufTm.restype = None

# /usr/local/include/libiec61850/iec61850_client.h: 1647
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReportControlBlock_getSqNum", "cdecl"):
    ClientReportControlBlock_getSqNum = _libs["/usr/local/lib/libiec61850.so"].get("ClientReportControlBlock_getSqNum", "cdecl")
    ClientReportControlBlock_getSqNum.argtypes = [ClientReportControlBlock]
    ClientReportControlBlock_getSqNum.restype = uint16_t

# /usr/local/include/libiec61850/iec61850_client.h: 1650
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReportControlBlock_getTrgOps", "cdecl"):
    ClientReportControlBlock_getTrgOps = _libs["/usr/local/lib/libiec61850.so"].get("ClientReportControlBlock_getTrgOps", "cdecl")
    ClientReportControlBlock_getTrgOps.argtypes = [ClientReportControlBlock]
    ClientReportControlBlock_getTrgOps.restype = c_int

# /usr/local/include/libiec61850/iec61850_client.h: 1653
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReportControlBlock_setTrgOps", "cdecl"):
    ClientReportControlBlock_setTrgOps = _libs["/usr/local/lib/libiec61850.so"].get("ClientReportControlBlock_setTrgOps", "cdecl")
    ClientReportControlBlock_setTrgOps.argtypes = [ClientReportControlBlock, c_int]
    ClientReportControlBlock_setTrgOps.restype = None

# /usr/local/include/libiec61850/iec61850_client.h: 1656
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReportControlBlock_getIntgPd", "cdecl"):
    ClientReportControlBlock_getIntgPd = _libs["/usr/local/lib/libiec61850.so"].get("ClientReportControlBlock_getIntgPd", "cdecl")
    ClientReportControlBlock_getIntgPd.argtypes = [ClientReportControlBlock]
    ClientReportControlBlock_getIntgPd.restype = uint32_t

# /usr/local/include/libiec61850/iec61850_client.h: 1659
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReportControlBlock_setIntgPd", "cdecl"):
    ClientReportControlBlock_setIntgPd = _libs["/usr/local/lib/libiec61850.so"].get("ClientReportControlBlock_setIntgPd", "cdecl")
    ClientReportControlBlock_setIntgPd.argtypes = [ClientReportControlBlock, uint32_t]
    ClientReportControlBlock_setIntgPd.restype = None

# /usr/local/include/libiec61850/iec61850_client.h: 1662
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReportControlBlock_getGI", "cdecl"):
    ClientReportControlBlock_getGI = _libs["/usr/local/lib/libiec61850.so"].get("ClientReportControlBlock_getGI", "cdecl")
    ClientReportControlBlock_getGI.argtypes = [ClientReportControlBlock]
    ClientReportControlBlock_getGI.restype = c_bool

# /usr/local/include/libiec61850/iec61850_client.h: 1665
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReportControlBlock_setGI", "cdecl"):
    ClientReportControlBlock_setGI = _libs["/usr/local/lib/libiec61850.so"].get("ClientReportControlBlock_setGI", "cdecl")
    ClientReportControlBlock_setGI.argtypes = [ClientReportControlBlock, c_bool]
    ClientReportControlBlock_setGI.restype = None

# /usr/local/include/libiec61850/iec61850_client.h: 1668
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReportControlBlock_getPurgeBuf", "cdecl"):
    ClientReportControlBlock_getPurgeBuf = _libs["/usr/local/lib/libiec61850.so"].get("ClientReportControlBlock_getPurgeBuf", "cdecl")
    ClientReportControlBlock_getPurgeBuf.argtypes = [ClientReportControlBlock]
    ClientReportControlBlock_getPurgeBuf.restype = c_bool

# /usr/local/include/libiec61850/iec61850_client.h: 1678
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReportControlBlock_setPurgeBuf", "cdecl"):
    ClientReportControlBlock_setPurgeBuf = _libs["/usr/local/lib/libiec61850.so"].get("ClientReportControlBlock_setPurgeBuf", "cdecl")
    ClientReportControlBlock_setPurgeBuf.argtypes = [ClientReportControlBlock, c_bool]
    ClientReportControlBlock_setPurgeBuf.restype = None

# /usr/local/include/libiec61850/iec61850_client.h: 1686
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReportControlBlock_hasResvTms", "cdecl"):
    ClientReportControlBlock_hasResvTms = _libs["/usr/local/lib/libiec61850.so"].get("ClientReportControlBlock_hasResvTms", "cdecl")
    ClientReportControlBlock_hasResvTms.argtypes = [ClientReportControlBlock]
    ClientReportControlBlock_hasResvTms.restype = c_bool

# /usr/local/include/libiec61850/iec61850_client.h: 1689
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReportControlBlock_getResvTms", "cdecl"):
    ClientReportControlBlock_getResvTms = _libs["/usr/local/lib/libiec61850.so"].get("ClientReportControlBlock_getResvTms", "cdecl")
    ClientReportControlBlock_getResvTms.argtypes = [ClientReportControlBlock]
    ClientReportControlBlock_getResvTms.restype = c_int16

# /usr/local/include/libiec61850/iec61850_client.h: 1692
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReportControlBlock_setResvTms", "cdecl"):
    ClientReportControlBlock_setResvTms = _libs["/usr/local/lib/libiec61850.so"].get("ClientReportControlBlock_setResvTms", "cdecl")
    ClientReportControlBlock_setResvTms.argtypes = [ClientReportControlBlock, c_int16]
    ClientReportControlBlock_setResvTms.restype = None

# /usr/local/include/libiec61850/iec61850_client.h: 1694
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReportControlBlock_getEntryId", "cdecl"):
    ClientReportControlBlock_getEntryId = _libs["/usr/local/lib/libiec61850.so"].get("ClientReportControlBlock_getEntryId", "cdecl")
    ClientReportControlBlock_getEntryId.argtypes = [ClientReportControlBlock]
    ClientReportControlBlock_getEntryId.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/iec61850_client.h: 1698
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReportControlBlock_setEntryId", "cdecl"):
    ClientReportControlBlock_setEntryId = _libs["/usr/local/lib/libiec61850.so"].get("ClientReportControlBlock_setEntryId", "cdecl")
    ClientReportControlBlock_setEntryId.argtypes = [ClientReportControlBlock, POINTER(MmsValue)]
    ClientReportControlBlock_setEntryId.restype = None

# /usr/local/include/libiec61850/iec61850_client.h: 1701
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReportControlBlock_getEntryTime", "cdecl"):
    ClientReportControlBlock_getEntryTime = _libs["/usr/local/lib/libiec61850.so"].get("ClientReportControlBlock_getEntryTime", "cdecl")
    ClientReportControlBlock_getEntryTime.argtypes = [ClientReportControlBlock]
    ClientReportControlBlock_getEntryTime.restype = uint64_t

# /usr/local/include/libiec61850/iec61850_client.h: 1703
if _libs["/usr/local/lib/libiec61850.so"].has("ClientReportControlBlock_getOwner", "cdecl"):
    ClientReportControlBlock_getOwner = _libs["/usr/local/lib/libiec61850.so"].get("ClientReportControlBlock_getOwner", "cdecl")
    ClientReportControlBlock_getOwner.argtypes = [ClientReportControlBlock]
    ClientReportControlBlock_getOwner.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/iec61850_client.h: 1737
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_readDataSetValues", "cdecl"):
    IedConnection_readDataSetValues = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_readDataSetValues", "cdecl")
    IedConnection_readDataSetValues.argtypes = [IedConnection, POINTER(IedClientError), String, ClientDataSet]
    IedConnection_readDataSetValues.restype = ClientDataSet

IedConnection_ReadDataSetHandler = CFUNCTYPE(UNCHECKED(None), uint32_t, POINTER(None), IedClientError, ClientDataSet)# /usr/local/include/libiec61850/iec61850_client.h: 1740

# /usr/local/include/libiec61850/iec61850_client.h: 1762
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_readDataSetValuesAsync", "cdecl"):
    IedConnection_readDataSetValuesAsync = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_readDataSetValuesAsync", "cdecl")
    IedConnection_readDataSetValuesAsync.argtypes = [IedConnection, POINTER(IedClientError), String, ClientDataSet, IedConnection_ReadDataSetHandler, POINTER(None)]
    IedConnection_readDataSetValuesAsync.restype = uint32_t

# /usr/local/include/libiec61850/iec61850_client.h: 1783
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_createDataSet", "cdecl"):
    IedConnection_createDataSet = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_createDataSet", "cdecl")
    IedConnection_createDataSet.argtypes = [IedConnection, POINTER(IedClientError), String, LinkedList]
    IedConnection_createDataSet.restype = None

# /usr/local/include/libiec61850/iec61850_client.h: 1807
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_createDataSetAsync", "cdecl"):
    IedConnection_createDataSetAsync = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_createDataSetAsync", "cdecl")
    IedConnection_createDataSetAsync.argtypes = [IedConnection, POINTER(IedClientError), String, LinkedList, IedConnection_GenericServiceHandler, POINTER(None)]
    IedConnection_createDataSetAsync.restype = uint32_t

# /usr/local/include/libiec61850/iec61850_client.h: 1824
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_deleteDataSet", "cdecl"):
    IedConnection_deleteDataSet = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_deleteDataSet", "cdecl")
    IedConnection_deleteDataSet.argtypes = [IedConnection, POINTER(IedClientError), String]
    IedConnection_deleteDataSet.restype = c_bool

# /usr/local/include/libiec61850/iec61850_client.h: 1844
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_deleteDataSetAsync", "cdecl"):
    IedConnection_deleteDataSetAsync = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_deleteDataSetAsync", "cdecl")
    IedConnection_deleteDataSetAsync.argtypes = [IedConnection, POINTER(IedClientError), String, IedConnection_GenericServiceHandler, POINTER(None)]
    IedConnection_deleteDataSetAsync.restype = uint32_t

# /usr/local/include/libiec61850/iec61850_client.h: 1862
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_getDataSetDirectory", "cdecl"):
    IedConnection_getDataSetDirectory = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_getDataSetDirectory", "cdecl")
    IedConnection_getDataSetDirectory.argtypes = [IedConnection, POINTER(IedClientError), String, POINTER(c_bool)]
    IedConnection_getDataSetDirectory.restype = LinkedList

IedConnection_GetDataSetDirectoryHandler = CFUNCTYPE(UNCHECKED(None), uint32_t, POINTER(None), IedClientError, LinkedList, c_bool)# /usr/local/include/libiec61850/iec61850_client.h: 1872

# /usr/local/include/libiec61850/iec61850_client.h: 1889
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_getDataSetDirectoryAsync", "cdecl"):
    IedConnection_getDataSetDirectoryAsync = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_getDataSetDirectoryAsync", "cdecl")
    IedConnection_getDataSetDirectoryAsync.argtypes = [IedConnection, POINTER(IedClientError), String, IedConnection_GetDataSetDirectoryHandler, POINTER(None)]
    IedConnection_getDataSetDirectoryAsync.restype = uint32_t

# /usr/local/include/libiec61850/iec61850_client.h: 1908
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_writeDataSetValues", "cdecl"):
    IedConnection_writeDataSetValues = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_writeDataSetValues", "cdecl")
    IedConnection_writeDataSetValues.argtypes = [IedConnection, POINTER(IedClientError), String, LinkedList, POINTER(LinkedList)]
    IedConnection_writeDataSetValues.restype = None

IedConnection_WriteDataSetHandler = CFUNCTYPE(UNCHECKED(None), uint32_t, POINTER(None), IedClientError, LinkedList)# /usr/local/include/libiec61850/iec61850_client.h: 1920

# /usr/local/include/libiec61850/iec61850_client.h: 1944
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_writeDataSetValuesAsync", "cdecl"):
    IedConnection_writeDataSetValuesAsync = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_writeDataSetValuesAsync", "cdecl")
    IedConnection_writeDataSetValuesAsync.argtypes = [IedConnection, POINTER(IedClientError), String, LinkedList, IedConnection_WriteDataSetHandler, POINTER(None)]
    IedConnection_writeDataSetValuesAsync.restype = uint32_t

# /usr/local/include/libiec61850/iec61850_client.h: 1961
if _libs["/usr/local/lib/libiec61850.so"].has("ClientDataSet_destroy", "cdecl"):
    ClientDataSet_destroy = _libs["/usr/local/lib/libiec61850.so"].get("ClientDataSet_destroy", "cdecl")
    ClientDataSet_destroy.argtypes = [ClientDataSet]
    ClientDataSet_destroy.restype = None

# /usr/local/include/libiec61850/iec61850_client.h: 1977
if _libs["/usr/local/lib/libiec61850.so"].has("ClientDataSet_getValues", "cdecl"):
    ClientDataSet_getValues = _libs["/usr/local/lib/libiec61850.so"].get("ClientDataSet_getValues", "cdecl")
    ClientDataSet_getValues.argtypes = [ClientDataSet]
    ClientDataSet_getValues.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/iec61850_client.h: 1987
if _libs["/usr/local/lib/libiec61850.so"].has("ClientDataSet_getReference", "cdecl"):
    ClientDataSet_getReference = _libs["/usr/local/lib/libiec61850.so"].get("ClientDataSet_getReference", "cdecl")
    ClientDataSet_getReference.argtypes = [ClientDataSet]
    if sizeof(c_int) == sizeof(c_void_p):
        ClientDataSet_getReference.restype = ReturnString
    else:
        ClientDataSet_getReference.restype = String
        ClientDataSet_getReference.errcheck = ReturnString

# /usr/local/include/libiec61850/iec61850_client.h: 1998
if _libs["/usr/local/lib/libiec61850.so"].has("ClientDataSet_getDataSetSize", "cdecl"):
    ClientDataSet_getDataSetSize = _libs["/usr/local/lib/libiec61850.so"].get("ClientDataSet_getDataSetSize", "cdecl")
    ClientDataSet_getDataSetSize.argtypes = [ClientDataSet]
    ClientDataSet_getDataSetSize.restype = c_int

# /usr/local/include/libiec61850/iec61850_client.h: 2012
class struct_sControlObjectClient(Structure):
    pass

ControlObjectClient = POINTER(struct_sControlObjectClient)# /usr/local/include/libiec61850/iec61850_client.h: 2012

# /usr/local/include/libiec61850/iec61850_client.h: 2031
if _libs["/usr/local/lib/libiec61850.so"].has("ControlObjectClient_create", "cdecl"):
    ControlObjectClient_create = _libs["/usr/local/lib/libiec61850.so"].get("ControlObjectClient_create", "cdecl")
    ControlObjectClient_create.argtypes = [String, IedConnection]
    ControlObjectClient_create.restype = ControlObjectClient

# /usr/local/include/libiec61850/iec61850_client.h: 2046
if _libs["/usr/local/lib/libiec61850.so"].has("ControlObjectClient_createEx", "cdecl"):
    ControlObjectClient_createEx = _libs["/usr/local/lib/libiec61850.so"].get("ControlObjectClient_createEx", "cdecl")
    ControlObjectClient_createEx.argtypes = [String, IedConnection, ControlModel, POINTER(MmsVariableSpecification)]
    ControlObjectClient_createEx.restype = ControlObjectClient

# /usr/local/include/libiec61850/iec61850_client.h: 2054
if _libs["/usr/local/lib/libiec61850.so"].has("ControlObjectClient_destroy", "cdecl"):
    ControlObjectClient_destroy = _libs["/usr/local/lib/libiec61850.so"].get("ControlObjectClient_destroy", "cdecl")
    ControlObjectClient_destroy.argtypes = [ControlObjectClient]
    ControlObjectClient_destroy.restype = None

enum_anon_47 = c_int# /usr/local/include/libiec61850/iec61850_client.h: 2064

CONTROL_ACTION_TYPE_SELECT = 0# /usr/local/include/libiec61850/iec61850_client.h: 2064

CONTROL_ACTION_TYPE_OPERATE = 1# /usr/local/include/libiec61850/iec61850_client.h: 2064

CONTROL_ACTION_TYPE_CANCEL = 2# /usr/local/include/libiec61850/iec61850_client.h: 2064

ControlActionType = enum_anon_47# /usr/local/include/libiec61850/iec61850_client.h: 2064

ControlObjectClient_ControlActionHandler = CFUNCTYPE(UNCHECKED(None), uint32_t, POINTER(None), IedClientError, ControlActionType, c_bool)# /usr/local/include/libiec61850/iec61850_client.h: 2083

# /usr/local/include/libiec61850/iec61850_client.h: 2092
if _libs["/usr/local/lib/libiec61850.so"].has("ControlObjectClient_getObjectReference", "cdecl"):
    ControlObjectClient_getObjectReference = _libs["/usr/local/lib/libiec61850.so"].get("ControlObjectClient_getObjectReference", "cdecl")
    ControlObjectClient_getObjectReference.argtypes = [ControlObjectClient]
    ControlObjectClient_getObjectReference.restype = c_char_p

# /usr/local/include/libiec61850/iec61850_client.h: 2103
if _libs["/usr/local/lib/libiec61850.so"].has("ControlObjectClient_getControlModel", "cdecl"):
    ControlObjectClient_getControlModel = _libs["/usr/local/lib/libiec61850.so"].get("ControlObjectClient_getControlModel", "cdecl")
    ControlObjectClient_getControlModel.argtypes = [ControlObjectClient]
    ControlObjectClient_getControlModel.restype = ControlModel

# /usr/local/include/libiec61850/iec61850_client.h: 2114
if _libs["/usr/local/lib/libiec61850.so"].has("ControlObjectClient_setControlModel", "cdecl"):
    ControlObjectClient_setControlModel = _libs["/usr/local/lib/libiec61850.so"].get("ControlObjectClient_setControlModel", "cdecl")
    ControlObjectClient_setControlModel.argtypes = [ControlObjectClient, ControlModel]
    ControlObjectClient_setControlModel.restype = None

# /usr/local/include/libiec61850/iec61850_client.h: 2126
if _libs["/usr/local/lib/libiec61850.so"].has("ControlObjectClient_changeServerControlModel", "cdecl"):
    ControlObjectClient_changeServerControlModel = _libs["/usr/local/lib/libiec61850.so"].get("ControlObjectClient_changeServerControlModel", "cdecl")
    ControlObjectClient_changeServerControlModel.argtypes = [ControlObjectClient, ControlModel]
    ControlObjectClient_changeServerControlModel.restype = None

# /usr/local/include/libiec61850/iec61850_client.h: 2139
if _libs["/usr/local/lib/libiec61850.so"].has("ControlObjectClient_getCtlValType", "cdecl"):
    ControlObjectClient_getCtlValType = _libs["/usr/local/lib/libiec61850.so"].get("ControlObjectClient_getCtlValType", "cdecl")
    ControlObjectClient_getCtlValType.argtypes = [ControlObjectClient]
    ControlObjectClient_getCtlValType.restype = MmsType

# /usr/local/include/libiec61850/iec61850_client.h: 2149
if _libs["/usr/local/lib/libiec61850.so"].has("ControlObjectClient_getLastError", "cdecl"):
    ControlObjectClient_getLastError = _libs["/usr/local/lib/libiec61850.so"].get("ControlObjectClient_getLastError", "cdecl")
    ControlObjectClient_getLastError.argtypes = [ControlObjectClient]
    ControlObjectClient_getLastError.restype = IedClientError

# /usr/local/include/libiec61850/iec61850_client.h: 2162
if _libs["/usr/local/lib/libiec61850.so"].has("ControlObjectClient_operate", "cdecl"):
    ControlObjectClient_operate = _libs["/usr/local/lib/libiec61850.so"].get("ControlObjectClient_operate", "cdecl")
    ControlObjectClient_operate.argtypes = [ControlObjectClient, POINTER(MmsValue), uint64_t]
    ControlObjectClient_operate.restype = c_bool

# /usr/local/include/libiec61850/iec61850_client.h: 2175
if _libs["/usr/local/lib/libiec61850.so"].has("ControlObjectClient_select", "cdecl"):
    ControlObjectClient_select = _libs["/usr/local/lib/libiec61850.so"].get("ControlObjectClient_select", "cdecl")
    ControlObjectClient_select.argtypes = [ControlObjectClient]
    ControlObjectClient_select.restype = c_bool

# /usr/local/include/libiec61850/iec61850_client.h: 2189
if _libs["/usr/local/lib/libiec61850.so"].has("ControlObjectClient_selectWithValue", "cdecl"):
    ControlObjectClient_selectWithValue = _libs["/usr/local/lib/libiec61850.so"].get("ControlObjectClient_selectWithValue", "cdecl")
    ControlObjectClient_selectWithValue.argtypes = [ControlObjectClient, POINTER(MmsValue)]
    ControlObjectClient_selectWithValue.restype = c_bool

# /usr/local/include/libiec61850/iec61850_client.h: 2202
if _libs["/usr/local/lib/libiec61850.so"].has("ControlObjectClient_cancel", "cdecl"):
    ControlObjectClient_cancel = _libs["/usr/local/lib/libiec61850.so"].get("ControlObjectClient_cancel", "cdecl")
    ControlObjectClient_cancel.argtypes = [ControlObjectClient]
    ControlObjectClient_cancel.restype = c_bool

# /usr/local/include/libiec61850/iec61850_client.h: 2219
if _libs["/usr/local/lib/libiec61850.so"].has("ControlObjectClient_operateAsync", "cdecl"):
    ControlObjectClient_operateAsync = _libs["/usr/local/lib/libiec61850.so"].get("ControlObjectClient_operateAsync", "cdecl")
    ControlObjectClient_operateAsync.argtypes = [ControlObjectClient, POINTER(IedClientError), POINTER(MmsValue), uint64_t, ControlObjectClient_ControlActionHandler, POINTER(None)]
    ControlObjectClient_operateAsync.restype = uint32_t

# /usr/local/include/libiec61850/iec61850_client.h: 2236
if _libs["/usr/local/lib/libiec61850.so"].has("ControlObjectClient_selectAsync", "cdecl"):
    ControlObjectClient_selectAsync = _libs["/usr/local/lib/libiec61850.so"].get("ControlObjectClient_selectAsync", "cdecl")
    ControlObjectClient_selectAsync.argtypes = [ControlObjectClient, POINTER(IedClientError), ControlObjectClient_ControlActionHandler, POINTER(None)]
    ControlObjectClient_selectAsync.restype = uint32_t

# /usr/local/include/libiec61850/iec61850_client.h: 2253
if _libs["/usr/local/lib/libiec61850.so"].has("ControlObjectClient_selectWithValueAsync", "cdecl"):
    ControlObjectClient_selectWithValueAsync = _libs["/usr/local/lib/libiec61850.so"].get("ControlObjectClient_selectWithValueAsync", "cdecl")
    ControlObjectClient_selectWithValueAsync.argtypes = [ControlObjectClient, POINTER(IedClientError), POINTER(MmsValue), ControlObjectClient_ControlActionHandler, POINTER(None)]
    ControlObjectClient_selectWithValueAsync.restype = uint32_t

# /usr/local/include/libiec61850/iec61850_client.h: 2270
if _libs["/usr/local/lib/libiec61850.so"].has("ControlObjectClient_cancelAsync", "cdecl"):
    ControlObjectClient_cancelAsync = _libs["/usr/local/lib/libiec61850.so"].get("ControlObjectClient_cancelAsync", "cdecl")
    ControlObjectClient_cancelAsync.argtypes = [ControlObjectClient, POINTER(IedClientError), ControlObjectClient_ControlActionHandler, POINTER(None)]
    ControlObjectClient_cancelAsync.restype = uint32_t

# /usr/local/include/libiec61850/iec61850_client.h: 2280
if _libs["/usr/local/lib/libiec61850.so"].has("ControlObjectClient_getLastApplError", "cdecl"):
    ControlObjectClient_getLastApplError = _libs["/usr/local/lib/libiec61850.so"].get("ControlObjectClient_getLastApplError", "cdecl")
    ControlObjectClient_getLastApplError.argtypes = [ControlObjectClient]
    ControlObjectClient_getLastApplError.restype = LastApplError

# /usr/local/include/libiec61850/iec61850_client.h: 2292
if _libs["/usr/local/lib/libiec61850.so"].has("ControlObjectClient_setTestMode", "cdecl"):
    ControlObjectClient_setTestMode = _libs["/usr/local/lib/libiec61850.so"].get("ControlObjectClient_setTestMode", "cdecl")
    ControlObjectClient_setTestMode.argtypes = [ControlObjectClient, c_bool]
    ControlObjectClient_setTestMode.restype = None

# /usr/local/include/libiec61850/iec61850_client.h: 2305
if _libs["/usr/local/lib/libiec61850.so"].has("ControlObjectClient_setOrigin", "cdecl"):
    ControlObjectClient_setOrigin = _libs["/usr/local/lib/libiec61850.so"].get("ControlObjectClient_setOrigin", "cdecl")
    ControlObjectClient_setOrigin.argtypes = [ControlObjectClient, String, c_int]
    ControlObjectClient_setOrigin.restype = None

# /usr/local/include/libiec61850/iec61850_client.h: 2316
if _libs["/usr/local/lib/libiec61850.so"].has("ControlObjectClient_useConstantT", "cdecl"):
    ControlObjectClient_useConstantT = _libs["/usr/local/lib/libiec61850.so"].get("ControlObjectClient_useConstantT", "cdecl")
    ControlObjectClient_useConstantT.argtypes = [ControlObjectClient, c_bool]
    ControlObjectClient_useConstantT.restype = None

# /usr/local/include/libiec61850/iec61850_client.h: 2322
if _libs["/usr/local/lib/libiec61850.so"].has("ControlObjectClient_enableInterlockCheck", "cdecl"):
    ControlObjectClient_enableInterlockCheck = _libs["/usr/local/lib/libiec61850.so"].get("ControlObjectClient_enableInterlockCheck", "cdecl")
    ControlObjectClient_enableInterlockCheck.argtypes = [ControlObjectClient]
    ControlObjectClient_enableInterlockCheck.restype = None

# /usr/local/include/libiec61850/iec61850_client.h: 2328
if _libs["/usr/local/lib/libiec61850.so"].has("ControlObjectClient_enableSynchroCheck", "cdecl"):
    ControlObjectClient_enableSynchroCheck = _libs["/usr/local/lib/libiec61850.so"].get("ControlObjectClient_enableSynchroCheck", "cdecl")
    ControlObjectClient_enableSynchroCheck.argtypes = [ControlObjectClient]
    ControlObjectClient_enableSynchroCheck.restype = None

# /usr/local/include/libiec61850/iec61850_client.h: 2334
if _libs["/usr/local/lib/libiec61850.so"].has("ControlObjectClient_setCtlNum", "cdecl"):
    ControlObjectClient_setCtlNum = _libs["/usr/local/lib/libiec61850.so"].get("ControlObjectClient_setCtlNum", "cdecl")
    ControlObjectClient_setCtlNum.argtypes = [ControlObjectClient, uint8_t]
    ControlObjectClient_setCtlNum.restype = None

# /usr/local/include/libiec61850/iec61850_client.h: 2343
if _libs["/usr/local/lib/libiec61850.so"].has("ControlObjectClient_setInterlockCheck", "cdecl"):
    ControlObjectClient_setInterlockCheck = _libs["/usr/local/lib/libiec61850.so"].get("ControlObjectClient_setInterlockCheck", "cdecl")
    ControlObjectClient_setInterlockCheck.argtypes = [ControlObjectClient, c_bool]
    ControlObjectClient_setInterlockCheck.restype = None

# /usr/local/include/libiec61850/iec61850_client.h: 2352
if _libs["/usr/local/lib/libiec61850.so"].has("ControlObjectClient_setSynchroCheck", "cdecl"):
    ControlObjectClient_setSynchroCheck = _libs["/usr/local/lib/libiec61850.so"].get("ControlObjectClient_setSynchroCheck", "cdecl")
    ControlObjectClient_setSynchroCheck.argtypes = [ControlObjectClient, c_bool]
    ControlObjectClient_setSynchroCheck.restype = None

CommandTerminationHandler = CFUNCTYPE(UNCHECKED(None), POINTER(None), ControlObjectClient)# /usr/local/include/libiec61850/iec61850_client.h: 2372

# /usr/local/include/libiec61850/iec61850_client.h: 2389
if _libs["/usr/local/lib/libiec61850.so"].has("ControlObjectClient_setCommandTerminationHandler", "cdecl"):
    ControlObjectClient_setCommandTerminationHandler = _libs["/usr/local/lib/libiec61850.so"].get("ControlObjectClient_setCommandTerminationHandler", "cdecl")
    ControlObjectClient_setCommandTerminationHandler.argtypes = [ControlObjectClient, CommandTerminationHandler, POINTER(None)]
    ControlObjectClient_setCommandTerminationHandler.restype = None

# /usr/local/include/libiec61850/iec61850_client.h: 2415
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_getDeviceModelFromServer", "cdecl"):
    IedConnection_getDeviceModelFromServer = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_getDeviceModelFromServer", "cdecl")
    IedConnection_getDeviceModelFromServer.argtypes = [IedConnection, POINTER(IedClientError)]
    IedConnection_getDeviceModelFromServer.restype = None

# /usr/local/include/libiec61850/iec61850_client.h: 2431
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_getLogicalDeviceList", "cdecl"):
    IedConnection_getLogicalDeviceList = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_getLogicalDeviceList", "cdecl")
    IedConnection_getLogicalDeviceList.argtypes = [IedConnection, POINTER(IedClientError)]
    IedConnection_getLogicalDeviceList.restype = LinkedList

# /usr/local/include/libiec61850/iec61850_client.h: 2450
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_getServerDirectory", "cdecl"):
    IedConnection_getServerDirectory = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_getServerDirectory", "cdecl")
    IedConnection_getServerDirectory.argtypes = [IedConnection, POINTER(IedClientError), c_bool]
    IedConnection_getServerDirectory.restype = LinkedList

# /usr/local/include/libiec61850/iec61850_client.h: 2468
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_getLogicalDeviceDirectory", "cdecl"):
    IedConnection_getLogicalDeviceDirectory = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_getLogicalDeviceDirectory", "cdecl")
    IedConnection_getLogicalDeviceDirectory.argtypes = [IedConnection, POINTER(IedClientError), String]
    IedConnection_getLogicalDeviceDirectory.restype = LinkedList

enum_anon_48 = c_int# /usr/local/include/libiec61850/iec61850_client.h: 2482

ACSI_CLASS_DATA_OBJECT = 0# /usr/local/include/libiec61850/iec61850_client.h: 2482

ACSI_CLASS_DATA_SET = (ACSI_CLASS_DATA_OBJECT + 1)# /usr/local/include/libiec61850/iec61850_client.h: 2482

ACSI_CLASS_BRCB = (ACSI_CLASS_DATA_SET + 1)# /usr/local/include/libiec61850/iec61850_client.h: 2482

ACSI_CLASS_URCB = (ACSI_CLASS_BRCB + 1)# /usr/local/include/libiec61850/iec61850_client.h: 2482

ACSI_CLASS_LCB = (ACSI_CLASS_URCB + 1)# /usr/local/include/libiec61850/iec61850_client.h: 2482

ACSI_CLASS_LOG = (ACSI_CLASS_LCB + 1)# /usr/local/include/libiec61850/iec61850_client.h: 2482

ACSI_CLASS_SGCB = (ACSI_CLASS_LOG + 1)# /usr/local/include/libiec61850/iec61850_client.h: 2482

ACSI_CLASS_GoCB = (ACSI_CLASS_SGCB + 1)# /usr/local/include/libiec61850/iec61850_client.h: 2482

ACSI_CLASS_GsCB = (ACSI_CLASS_GoCB + 1)# /usr/local/include/libiec61850/iec61850_client.h: 2482

ACSI_CLASS_MSVCB = (ACSI_CLASS_GsCB + 1)# /usr/local/include/libiec61850/iec61850_client.h: 2482

ACSI_CLASS_USVCB = (ACSI_CLASS_MSVCB + 1)# /usr/local/include/libiec61850/iec61850_client.h: 2482

ACSIClass = enum_anon_48# /usr/local/include/libiec61850/iec61850_client.h: 2482

# /usr/local/include/libiec61850/iec61850_client.h: 2500
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_getLogicalNodeVariables", "cdecl"):
    IedConnection_getLogicalNodeVariables = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_getLogicalNodeVariables", "cdecl")
    IedConnection_getLogicalNodeVariables.argtypes = [IedConnection, POINTER(IedClientError), String]
    IedConnection_getLogicalNodeVariables.restype = LinkedList

# /usr/local/include/libiec61850/iec61850_client.h: 2520
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_getLogicalNodeDirectory", "cdecl"):
    IedConnection_getLogicalNodeDirectory = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_getLogicalNodeDirectory", "cdecl")
    IedConnection_getLogicalNodeDirectory.argtypes = [IedConnection, POINTER(IedClientError), String, ACSIClass]
    IedConnection_getLogicalNodeDirectory.restype = LinkedList

# /usr/local/include/libiec61850/iec61850_client.h: 2539
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_getDataDirectory", "cdecl"):
    IedConnection_getDataDirectory = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_getDataDirectory", "cdecl")
    IedConnection_getDataDirectory.argtypes = [IedConnection, POINTER(IedClientError), String]
    IedConnection_getDataDirectory.restype = LinkedList

# /usr/local/include/libiec61850/iec61850_client.h: 2558
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_getDataDirectoryFC", "cdecl"):
    IedConnection_getDataDirectoryFC = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_getDataDirectoryFC", "cdecl")
    IedConnection_getDataDirectoryFC.argtypes = [IedConnection, POINTER(IedClientError), String]
    IedConnection_getDataDirectoryFC.restype = LinkedList

# /usr/local/include/libiec61850/iec61850_client.h: 2580
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_getDataDirectoryByFC", "cdecl"):
    IedConnection_getDataDirectoryByFC = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_getDataDirectoryByFC", "cdecl")
    IedConnection_getDataDirectoryByFC.argtypes = [IedConnection, POINTER(IedClientError), String, FunctionalConstraint]
    IedConnection_getDataDirectoryByFC.restype = LinkedList

# /usr/local/include/libiec61850/iec61850_client.h: 2597
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_getVariableSpecification", "cdecl"):
    IedConnection_getVariableSpecification = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_getVariableSpecification", "cdecl")
    IedConnection_getVariableSpecification.argtypes = [IedConnection, POINTER(IedClientError), String, FunctionalConstraint]
    IedConnection_getVariableSpecification.restype = POINTER(MmsVariableSpecification)

# /usr/local/include/libiec61850/iec61850_client.h: 2614
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_getLogicalDeviceVariables", "cdecl"):
    IedConnection_getLogicalDeviceVariables = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_getLogicalDeviceVariables", "cdecl")
    IedConnection_getLogicalDeviceVariables.argtypes = [IedConnection, POINTER(IedClientError), String]
    IedConnection_getLogicalDeviceVariables.restype = LinkedList

# /usr/local/include/libiec61850/iec61850_client.h: 2629
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_getLogicalDeviceDataSets", "cdecl"):
    IedConnection_getLogicalDeviceDataSets = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_getLogicalDeviceDataSets", "cdecl")
    IedConnection_getLogicalDeviceDataSets.argtypes = [IedConnection, POINTER(IedClientError), String]
    IedConnection_getLogicalDeviceDataSets.restype = LinkedList

IedConnection_GetNameListHandler = CFUNCTYPE(UNCHECKED(None), uint32_t, POINTER(None), IedClientError, LinkedList, c_bool)# /usr/local/include/libiec61850/iec61850_client.h: 2636

# /usr/local/include/libiec61850/iec61850_client.h: 2651
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_getServerDirectoryAsync", "cdecl"):
    IedConnection_getServerDirectoryAsync = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_getServerDirectoryAsync", "cdecl")
    IedConnection_getServerDirectoryAsync.argtypes = [IedConnection, POINTER(IedClientError), String, LinkedList, IedConnection_GetNameListHandler, POINTER(None)]
    IedConnection_getServerDirectoryAsync.restype = uint32_t

# /usr/local/include/libiec61850/iec61850_client.h: 2671
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_getLogicalDeviceVariablesAsync", "cdecl"):
    IedConnection_getLogicalDeviceVariablesAsync = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_getLogicalDeviceVariablesAsync", "cdecl")
    IedConnection_getLogicalDeviceVariablesAsync.argtypes = [IedConnection, POINTER(IedClientError), String, String, LinkedList, IedConnection_GetNameListHandler, POINTER(None)]
    IedConnection_getLogicalDeviceVariablesAsync.restype = uint32_t

# /usr/local/include/libiec61850/iec61850_client.h: 2691
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_getLogicalDeviceDataSetsAsync", "cdecl"):
    IedConnection_getLogicalDeviceDataSetsAsync = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_getLogicalDeviceDataSetsAsync", "cdecl")
    IedConnection_getLogicalDeviceDataSetsAsync.argtypes = [IedConnection, POINTER(IedClientError), String, String, LinkedList, IedConnection_GetNameListHandler, POINTER(None)]
    IedConnection_getLogicalDeviceDataSetsAsync.restype = uint32_t

IedConnection_GetVariableSpecificationHandler = CFUNCTYPE(UNCHECKED(None), uint32_t, POINTER(None), IedClientError, POINTER(MmsVariableSpecification))# /usr/local/include/libiec61850/iec61850_client.h: 2696

# /usr/local/include/libiec61850/iec61850_client.h: 2710
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_getVariableSpecificationAsync", "cdecl"):
    IedConnection_getVariableSpecificationAsync = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_getVariableSpecificationAsync", "cdecl")
    IedConnection_getVariableSpecificationAsync.argtypes = [IedConnection, POINTER(IedClientError), String, FunctionalConstraint, IedConnection_GetVariableSpecificationHandler, POINTER(None)]
    IedConnection_getVariableSpecificationAsync.restype = uint32_t

# /usr/local/include/libiec61850/iec61850_client.h: 2739
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_queryLogByTime", "cdecl"):
    IedConnection_queryLogByTime = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_queryLogByTime", "cdecl")
    IedConnection_queryLogByTime.argtypes = [IedConnection, POINTER(IedClientError), String, uint64_t, uint64_t, POINTER(c_bool)]
    IedConnection_queryLogByTime.restype = LinkedList

# /usr/local/include/libiec61850/iec61850_client.h: 2760
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_queryLogAfter", "cdecl"):
    IedConnection_queryLogAfter = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_queryLogAfter", "cdecl")
    IedConnection_queryLogAfter.argtypes = [IedConnection, POINTER(IedClientError), String, POINTER(MmsValue), uint64_t, POINTER(c_bool)]
    IedConnection_queryLogAfter.restype = LinkedList

IedConnection_QueryLogHandler = CFUNCTYPE(UNCHECKED(None), uint32_t, POINTER(None), IedClientError, LinkedList, c_bool)# /usr/local/include/libiec61850/iec61850_client.h: 2765

# /usr/local/include/libiec61850/iec61850_client.h: 2768
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_queryLogByTimeAsync", "cdecl"):
    IedConnection_queryLogByTimeAsync = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_queryLogByTimeAsync", "cdecl")
    IedConnection_queryLogByTimeAsync.argtypes = [IedConnection, POINTER(IedClientError), String, uint64_t, uint64_t, IedConnection_QueryLogHandler, POINTER(None)]
    IedConnection_queryLogByTimeAsync.restype = uint32_t

# /usr/local/include/libiec61850/iec61850_client.h: 2772
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_queryLogAfterAsync", "cdecl"):
    IedConnection_queryLogAfterAsync = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_queryLogAfterAsync", "cdecl")
    IedConnection_queryLogAfterAsync.argtypes = [IedConnection, POINTER(IedClientError), String, POINTER(MmsValue), uint64_t, IedConnection_QueryLogHandler, POINTER(None)]
    IedConnection_queryLogAfterAsync.restype = uint32_t

# /usr/local/include/libiec61850/iec61850_client.h: 2783
class struct_sFileDirectoryEntry(Structure):
    pass

FileDirectoryEntry = POINTER(struct_sFileDirectoryEntry)# /usr/local/include/libiec61850/iec61850_client.h: 2783

# /usr/local/include/libiec61850/iec61850_client.h: 2789
if _libs["/usr/local/lib/libiec61850.so"].has("FileDirectoryEntry_create", "cdecl"):
    FileDirectoryEntry_create = _libs["/usr/local/lib/libiec61850.so"].get("FileDirectoryEntry_create", "cdecl")
    FileDirectoryEntry_create.argtypes = [String, uint32_t, uint64_t]
    FileDirectoryEntry_create.restype = FileDirectoryEntry

# /usr/local/include/libiec61850/iec61850_client.h: 2799
if _libs["/usr/local/lib/libiec61850.so"].has("FileDirectoryEntry_destroy", "cdecl"):
    FileDirectoryEntry_destroy = _libs["/usr/local/lib/libiec61850.so"].get("FileDirectoryEntry_destroy", "cdecl")
    FileDirectoryEntry_destroy.argtypes = [FileDirectoryEntry]
    FileDirectoryEntry_destroy.restype = None

# /usr/local/include/libiec61850/iec61850_client.h: 2808
if _libs["/usr/local/lib/libiec61850.so"].has("FileDirectoryEntry_getFileName", "cdecl"):
    FileDirectoryEntry_getFileName = _libs["/usr/local/lib/libiec61850.so"].get("FileDirectoryEntry_getFileName", "cdecl")
    FileDirectoryEntry_getFileName.argtypes = [FileDirectoryEntry]
    FileDirectoryEntry_getFileName.restype = c_char_p

# /usr/local/include/libiec61850/iec61850_client.h: 2819
if _libs["/usr/local/lib/libiec61850.so"].has("FileDirectoryEntry_getFileSize", "cdecl"):
    FileDirectoryEntry_getFileSize = _libs["/usr/local/lib/libiec61850.so"].get("FileDirectoryEntry_getFileSize", "cdecl")
    FileDirectoryEntry_getFileSize.argtypes = [FileDirectoryEntry]
    FileDirectoryEntry_getFileSize.restype = uint32_t

# /usr/local/include/libiec61850/iec61850_client.h: 2829
if _libs["/usr/local/lib/libiec61850.so"].has("FileDirectoryEntry_getLastModified", "cdecl"):
    FileDirectoryEntry_getLastModified = _libs["/usr/local/lib/libiec61850.so"].get("FileDirectoryEntry_getLastModified", "cdecl")
    FileDirectoryEntry_getLastModified.argtypes = [FileDirectoryEntry]
    FileDirectoryEntry_getLastModified.restype = uint64_t

# /usr/local/include/libiec61850/iec61850_client.h: 2851
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_getFileDirectory", "cdecl"):
    IedConnection_getFileDirectory = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_getFileDirectory", "cdecl")
    IedConnection_getFileDirectory.argtypes = [IedConnection, POINTER(IedClientError), String]
    IedConnection_getFileDirectory.restype = LinkedList

# /usr/local/include/libiec61850/iec61850_client.h: 2882
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_getFileDirectoryEx", "cdecl"):
    IedConnection_getFileDirectoryEx = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_getFileDirectoryEx", "cdecl")
    IedConnection_getFileDirectoryEx.argtypes = [IedConnection, POINTER(IedClientError), String, String, POINTER(c_bool)]
    IedConnection_getFileDirectoryEx.restype = LinkedList

IedConnection_FileDirectoryEntryHandler = CFUNCTYPE(UNCHECKED(c_bool), uint32_t, POINTER(None), IedClientError, String, uint32_t, uint64_t, c_bool)# /usr/local/include/libiec61850/iec61850_client.h: 2910

# /usr/local/include/libiec61850/iec61850_client.h: 2932
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_getFileDirectoryAsyncEx", "cdecl"):
    IedConnection_getFileDirectoryAsyncEx = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_getFileDirectoryAsyncEx", "cdecl")
    IedConnection_getFileDirectoryAsyncEx.argtypes = [IedConnection, POINTER(IedClientError), String, String, IedConnection_FileDirectoryEntryHandler, POINTER(None)]
    IedConnection_getFileDirectoryAsyncEx.restype = uint32_t

IedClientGetFileHandler = CFUNCTYPE(UNCHECKED(c_bool), POINTER(None), POINTER(uint8_t), uint32_t)# /usr/local/include/libiec61850/iec61850_client.h: 2950

# /usr/local/include/libiec61850/iec61850_client.h: 2964
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_getFile", "cdecl"):
    IedConnection_getFile = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_getFile", "cdecl")
    IedConnection_getFile.argtypes = [IedConnection, POINTER(IedClientError), String, IedClientGetFileHandler, POINTER(None)]
    IedConnection_getFile.restype = uint32_t

IedConnection_GetFileAsyncHandler = CFUNCTYPE(UNCHECKED(c_bool), uint32_t, POINTER(None), IedClientError, uint32_t, POINTER(uint8_t), uint32_t, c_bool)# /usr/local/include/libiec61850/iec61850_client.h: 2987

# /usr/local/include/libiec61850/iec61850_client.h: 3008
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_getFileAsync", "cdecl"):
    IedConnection_getFileAsync = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_getFileAsync", "cdecl")
    IedConnection_getFileAsync.argtypes = [IedConnection, POINTER(IedClientError), String, IedConnection_GetFileAsyncHandler, POINTER(None)]
    IedConnection_getFileAsync.restype = uint32_t

# /usr/local/include/libiec61850/iec61850_client.h: 3022
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_setFilestoreBasepath", "cdecl"):
    IedConnection_setFilestoreBasepath = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_setFilestoreBasepath", "cdecl")
    IedConnection_setFilestoreBasepath.argtypes = [IedConnection, String]
    IedConnection_setFilestoreBasepath.restype = None

# /usr/local/include/libiec61850/iec61850_client.h: 3035
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_setFile", "cdecl"):
    IedConnection_setFile = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_setFile", "cdecl")
    IedConnection_setFile.argtypes = [IedConnection, POINTER(IedClientError), String, String]
    IedConnection_setFile.restype = None

# /usr/local/include/libiec61850/iec61850_client.h: 3050
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_setFileAsync", "cdecl"):
    IedConnection_setFileAsync = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_setFileAsync", "cdecl")
    IedConnection_setFileAsync.argtypes = [IedConnection, POINTER(IedClientError), String, String, IedConnection_GenericServiceHandler, POINTER(None)]
    IedConnection_setFileAsync.restype = uint32_t

# /usr/local/include/libiec61850/iec61850_client.h: 3063
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_deleteFile", "cdecl"):
    IedConnection_deleteFile = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_deleteFile", "cdecl")
    IedConnection_deleteFile.argtypes = [IedConnection, POINTER(IedClientError), String]
    IedConnection_deleteFile.restype = None

# /usr/local/include/libiec61850/iec61850_client.h: 3077
if _libs["/usr/local/lib/libiec61850.so"].has("IedConnection_deleteFileAsync", "cdecl"):
    IedConnection_deleteFileAsync = _libs["/usr/local/lib/libiec61850.so"].get("IedConnection_deleteFileAsync", "cdecl")
    IedConnection_deleteFileAsync.argtypes = [IedConnection, POINTER(IedClientError), String, IedConnection_GenericServiceHandler, POINTER(None)]
    IedConnection_deleteFileAsync.restype = uint32_t

enum_anon_49 = c_int# /usr/local/include/libiec61850/mms_server.h: 42

MMS_SERVER_NEW_CONNECTION = 0# /usr/local/include/libiec61850/mms_server.h: 42

MMS_SERVER_CONNECTION_CLOSED = (MMS_SERVER_NEW_CONNECTION + 1)# /usr/local/include/libiec61850/mms_server.h: 42

MMS_SERVER_CONNECTION_TICK = (MMS_SERVER_CONNECTION_CLOSED + 1)# /usr/local/include/libiec61850/mms_server.h: 42

MmsServerEvent = enum_anon_49# /usr/local/include/libiec61850/mms_server.h: 42

# /usr/local/include/libiec61850/mms_server.h: 44
class struct_sMmsServer(Structure):
    pass

MmsServer = POINTER(struct_sMmsServer)# /usr/local/include/libiec61850/mms_server.h: 44

# /usr/local/include/libiec61850/mms_server.h: 46
class struct_sMmsServerConnection(Structure):
    pass

MmsServerConnection = POINTER(struct_sMmsServerConnection)# /usr/local/include/libiec61850/mms_server.h: 46

enum_anon_50 = c_int# /usr/local/include/libiec61850/mms_server.h: 52

MMS_DOMAIN_SPECIFIC = 0# /usr/local/include/libiec61850/mms_server.h: 52

MMS_ASSOCIATION_SPECIFIC = (MMS_DOMAIN_SPECIFIC + 1)# /usr/local/include/libiec61850/mms_server.h: 52

MMS_VMD_SPECIFIC = (MMS_ASSOCIATION_SPECIFIC + 1)# /usr/local/include/libiec61850/mms_server.h: 52

MmsVariableListType = enum_anon_50# /usr/local/include/libiec61850/mms_server.h: 52

# /usr/local/include/libiec61850/mms_server.h: 55
for _lib in _libs.values():
    if not _lib.has("MmsServer_setLocalIpAddress", "cdecl"):
        continue
    MmsServer_setLocalIpAddress = _lib.get("MmsServer_setLocalIpAddress", "cdecl")
    MmsServer_setLocalIpAddress.argtypes = [MmsServer, String]
    MmsServer_setLocalIpAddress.restype = None
    break

# /usr/local/include/libiec61850/mms_server.h: 58
for _lib in _libs.values():
    if not _lib.has("MmsServer_isRunning", "cdecl"):
        continue
    MmsServer_isRunning = _lib.get("MmsServer_isRunning", "cdecl")
    MmsServer_isRunning.argtypes = [MmsServer]
    MmsServer_isRunning.restype = c_bool
    break

MmsNamedVariableListChangedHandler = CFUNCTYPE(UNCHECKED(MmsError), POINTER(None), c_bool, MmsVariableListType, POINTER(MmsDomain), String, MmsServerConnection)# /usr/local/include/libiec61850/mms_server.h: 72

# /usr/local/include/libiec61850/mms_server.h: 83
for _lib in _libs.values():
    if not _lib.has("MmsServer_installVariableListChangedHandler", "cdecl"):
        continue
    MmsServer_installVariableListChangedHandler = _lib.get("MmsServer_installVariableListChangedHandler", "cdecl")
    MmsServer_installVariableListChangedHandler.argtypes = [MmsServer, MmsNamedVariableListChangedHandler, POINTER(None)]
    MmsServer_installVariableListChangedHandler.restype = None
    break

MmsObtainFileHandler = CFUNCTYPE(UNCHECKED(c_bool), POINTER(None), MmsServerConnection, String, String)# /usr/local/include/libiec61850/mms_server.h: 96

# /usr/local/include/libiec61850/mms_server.h: 108
for _lib in _libs.values():
    if not _lib.has("MmsServer_installObtainFileHandler", "cdecl"):
        continue
    MmsServer_installObtainFileHandler = _lib.get("MmsServer_installObtainFileHandler", "cdecl")
    MmsServer_installObtainFileHandler.argtypes = [MmsServer, MmsObtainFileHandler, POINTER(None)]
    MmsServer_installObtainFileHandler.restype = None
    break

MmsGetFileCompleteHandler = CFUNCTYPE(UNCHECKED(None), POINTER(None), MmsServerConnection, String)# /usr/local/include/libiec61850/mms_server.h: 119

# /usr/local/include/libiec61850/mms_server.h: 130
for _lib in _libs.values():
    if not _lib.has("MmsServer_installGetFileCompleteHandler", "cdecl"):
        continue
    MmsServer_installGetFileCompleteHandler = _lib.get("MmsServer_installGetFileCompleteHandler", "cdecl")
    MmsServer_installGetFileCompleteHandler.argtypes = [MmsServer, MmsGetFileCompleteHandler, POINTER(None)]
    MmsServer_installGetFileCompleteHandler.restype = None
    break

enum_anon_51 = c_int# /usr/local/include/libiec61850/mms_server.h: 139

MMS_FILE_ACCESS_TYPE_READ_DIRECTORY = 0# /usr/local/include/libiec61850/mms_server.h: 139

MMS_FILE_ACCESS_TYPE_OPEN = (MMS_FILE_ACCESS_TYPE_READ_DIRECTORY + 1)# /usr/local/include/libiec61850/mms_server.h: 139

MMS_FILE_ACCESS_TYPE_OBTAIN = (MMS_FILE_ACCESS_TYPE_OPEN + 1)# /usr/local/include/libiec61850/mms_server.h: 139

MMS_FILE_ACCESS_TYPE_DELETE = (MMS_FILE_ACCESS_TYPE_OBTAIN + 1)# /usr/local/include/libiec61850/mms_server.h: 139

MMS_FILE_ACCESS_TYPE_RENAME = (MMS_FILE_ACCESS_TYPE_DELETE + 1)# /usr/local/include/libiec61850/mms_server.h: 139

MmsFileServiceType = enum_anon_51# /usr/local/include/libiec61850/mms_server.h: 139

MmsFileAccessHandler = CFUNCTYPE(UNCHECKED(MmsError), POINTER(None), MmsServerConnection, MmsFileServiceType, String, String)# /usr/local/include/libiec61850/mms_server.h: 152

# /usr/local/include/libiec61850/mms_server.h: 165
if _libs["/usr/local/lib/libiec61850.so"].has("MmsServer_installFileAccessHandler", "cdecl"):
    MmsServer_installFileAccessHandler = _libs["/usr/local/lib/libiec61850.so"].get("MmsServer_installFileAccessHandler", "cdecl")
    MmsServer_installFileAccessHandler.argtypes = [MmsServer, MmsFileAccessHandler, POINTER(None)]
    MmsServer_installFileAccessHandler.restype = None

# /usr/local/include/libiec61850/mms_server.h: 178
for _lib in _libs.values():
    if not _lib.has("MmsServer_setFilestoreBasepath", "cdecl"):
        continue
    MmsServer_setFilestoreBasepath = _lib.get("MmsServer_setFilestoreBasepath", "cdecl")
    MmsServer_setFilestoreBasepath.argtypes = [MmsServer, String]
    MmsServer_setFilestoreBasepath.restype = None
    break

# /usr/local/include/libiec61850/mms_server.h: 186
for _lib in _libs.values():
    if not _lib.has("MmsServer_setMaxConnections", "cdecl"):
        continue
    MmsServer_setMaxConnections = _lib.get("MmsServer_setMaxConnections", "cdecl")
    MmsServer_setMaxConnections.argtypes = [MmsServer, c_int]
    MmsServer_setMaxConnections.restype = None
    break

# /usr/local/include/libiec61850/mms_server.h: 197
for _lib in _libs.values():
    if not _lib.has("MmsServer_enableFileService", "cdecl"):
        continue
    MmsServer_enableFileService = _lib.get("MmsServer_enableFileService", "cdecl")
    MmsServer_enableFileService.argtypes = [MmsServer, c_bool]
    MmsServer_enableFileService.restype = None
    break

# /usr/local/include/libiec61850/mms_server.h: 208
for _lib in _libs.values():
    if not _lib.has("MmsServer_enableDynamicNamedVariableListService", "cdecl"):
        continue
    MmsServer_enableDynamicNamedVariableListService = _lib.get("MmsServer_enableDynamicNamedVariableListService", "cdecl")
    MmsServer_enableDynamicNamedVariableListService.argtypes = [MmsServer, c_bool]
    MmsServer_enableDynamicNamedVariableListService.restype = None
    break

# /usr/local/include/libiec61850/mms_server.h: 217
for _lib in _libs.values():
    if not _lib.has("MmsServer_setMaxAssociationSpecificDataSets", "cdecl"):
        continue
    MmsServer_setMaxAssociationSpecificDataSets = _lib.get("MmsServer_setMaxAssociationSpecificDataSets", "cdecl")
    MmsServer_setMaxAssociationSpecificDataSets.argtypes = [MmsServer, c_int]
    MmsServer_setMaxAssociationSpecificDataSets.restype = None
    break

# /usr/local/include/libiec61850/mms_server.h: 226
for _lib in _libs.values():
    if not _lib.has("MmsServer_setMaxDomainSpecificDataSets", "cdecl"):
        continue
    MmsServer_setMaxDomainSpecificDataSets = _lib.get("MmsServer_setMaxDomainSpecificDataSets", "cdecl")
    MmsServer_setMaxDomainSpecificDataSets.argtypes = [MmsServer, c_int]
    MmsServer_setMaxDomainSpecificDataSets.restype = None
    break

# /usr/local/include/libiec61850/mms_server.h: 235
for _lib in _libs.values():
    if not _lib.has("MmsServer_setMaxDataSetEntries", "cdecl"):
        continue
    MmsServer_setMaxDataSetEntries = _lib.get("MmsServer_setMaxDataSetEntries", "cdecl")
    MmsServer_setMaxDataSetEntries.argtypes = [MmsServer, c_int]
    MmsServer_setMaxDataSetEntries.restype = None
    break

# /usr/local/include/libiec61850/mms_server.h: 246
for _lib in _libs.values():
    if not _lib.has("MmsServer_enableJournalService", "cdecl"):
        continue
    MmsServer_enableJournalService = _lib.get("MmsServer_enableJournalService", "cdecl")
    MmsServer_enableJournalService.argtypes = [MmsServer, c_bool]
    MmsServer_enableJournalService.restype = None
    break

# /usr/local/include/libiec61850/mms_server.h: 268
for _lib in _libs.values():
    if not _lib.has("MmsServer_setServerIdentity", "cdecl"):
        continue
    MmsServer_setServerIdentity = _lib.get("MmsServer_setServerIdentity", "cdecl")
    MmsServer_setServerIdentity.argtypes = [MmsServer, String, String, String]
    MmsServer_setServerIdentity.restype = None
    break

# /usr/local/include/libiec61850/mms_server.h: 276
for _lib in _libs.values():
    if not _lib.has("MmsServer_getVendorName", "cdecl"):
        continue
    MmsServer_getVendorName = _lib.get("MmsServer_getVendorName", "cdecl")
    MmsServer_getVendorName.argtypes = [MmsServer]
    if sizeof(c_int) == sizeof(c_void_p):
        MmsServer_getVendorName.restype = ReturnString
    else:
        MmsServer_getVendorName.restype = String
        MmsServer_getVendorName.errcheck = ReturnString
    break

# /usr/local/include/libiec61850/mms_server.h: 285
for _lib in _libs.values():
    if not _lib.has("MmsServer_getModelName", "cdecl"):
        continue
    MmsServer_getModelName = _lib.get("MmsServer_getModelName", "cdecl")
    MmsServer_getModelName.argtypes = [MmsServer]
    if sizeof(c_int) == sizeof(c_void_p):
        MmsServer_getModelName.restype = ReturnString
    else:
        MmsServer_getModelName.restype = String
        MmsServer_getModelName.errcheck = ReturnString
    break

# /usr/local/include/libiec61850/mms_server.h: 294
for _lib in _libs.values():
    if not _lib.has("MmsServer_getRevision", "cdecl"):
        continue
    MmsServer_getRevision = _lib.get("MmsServer_getRevision", "cdecl")
    MmsServer_getRevision.argtypes = [MmsServer]
    if sizeof(c_int) == sizeof(c_void_p):
        MmsServer_getRevision.restype = ReturnString
    else:
        MmsServer_getRevision.restype = String
        MmsServer_getRevision.errcheck = ReturnString
    break

MmsStatusRequestListener = CFUNCTYPE(UNCHECKED(None), POINTER(None), MmsServer, MmsServerConnection, c_bool)# /usr/local/include/libiec61850/mms_server.h: 322

# /usr/local/include/libiec61850/mms_server.h: 332
for _lib in _libs.values():
    if not _lib.has("MmsServer_setVMDStatus", "cdecl"):
        continue
    MmsServer_setVMDStatus = _lib.get("MmsServer_setVMDStatus", "cdecl")
    MmsServer_setVMDStatus.argtypes = [MmsServer, c_int, c_int]
    MmsServer_setVMDStatus.restype = None
    break

# /usr/local/include/libiec61850/mms_server.h: 340
for _lib in _libs.values():
    if not _lib.has("MmsServer_getVMDLogicalStatus", "cdecl"):
        continue
    MmsServer_getVMDLogicalStatus = _lib.get("MmsServer_getVMDLogicalStatus", "cdecl")
    MmsServer_getVMDLogicalStatus.argtypes = [MmsServer]
    MmsServer_getVMDLogicalStatus.restype = c_int
    break

# /usr/local/include/libiec61850/mms_server.h: 348
for _lib in _libs.values():
    if not _lib.has("MmsServer_getVMDPhysicalStatus", "cdecl"):
        continue
    MmsServer_getVMDPhysicalStatus = _lib.get("MmsServer_getVMDPhysicalStatus", "cdecl")
    MmsServer_getVMDPhysicalStatus.argtypes = [MmsServer]
    MmsServer_getVMDPhysicalStatus.restype = c_int
    break

# /usr/local/include/libiec61850/mms_server.h: 362
for _lib in _libs.values():
    if not _lib.has("MmsServer_setStatusRequestListener", "cdecl"):
        continue
    MmsServer_setStatusRequestListener = _lib.get("MmsServer_setStatusRequestListener", "cdecl")
    MmsServer_setStatusRequestListener.argtypes = [MmsServer, MmsStatusRequestListener, POINTER(None)]
    MmsServer_setStatusRequestListener.restype = None
    break

# /usr/local/include/libiec61850/mms_server.h: 364
for _lib in _libs.values():
    if not _lib.has("MmsServerConnection_getClientAddress", "cdecl"):
        continue
    MmsServerConnection_getClientAddress = _lib.get("MmsServerConnection_getClientAddress", "cdecl")
    MmsServerConnection_getClientAddress.argtypes = [MmsServerConnection]
    if sizeof(c_int) == sizeof(c_void_p):
        MmsServerConnection_getClientAddress.restype = ReturnString
    else:
        MmsServerConnection_getClientAddress.restype = String
        MmsServerConnection_getClientAddress.errcheck = ReturnString
    break

# /usr/local/include/libiec61850/mms_server.h: 367
for _lib in _libs.values():
    if not _lib.has("MmsServerConnection_getLocalAddress", "cdecl"):
        continue
    MmsServerConnection_getLocalAddress = _lib.get("MmsServerConnection_getLocalAddress", "cdecl")
    MmsServerConnection_getLocalAddress.argtypes = [MmsServerConnection]
    if sizeof(c_int) == sizeof(c_void_p):
        MmsServerConnection_getLocalAddress.restype = ReturnString
    else:
        MmsServerConnection_getLocalAddress.restype = String
        MmsServerConnection_getLocalAddress.errcheck = ReturnString
    break

# /usr/local/include/libiec61850/mms_server.h: 370
for _lib in _libs.values():
    if not _lib.has("MmsServerConnection_getSecurityToken", "cdecl"):
        continue
    MmsServerConnection_getSecurityToken = _lib.get("MmsServerConnection_getSecurityToken", "cdecl")
    MmsServerConnection_getSecurityToken.argtypes = [MmsServerConnection]
    MmsServerConnection_getSecurityToken.restype = POINTER(c_ubyte)
    MmsServerConnection_getSecurityToken.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# /usr/local/include/libiec61850/iec61850_model.h: 192
class struct_sModelNode(Structure):
    pass

ModelNode = struct_sModelNode# /usr/local/include/libiec61850/iec61850_model.h: 46

# /usr/local/include/libiec61850/iec61850_model.h: 218
class struct_sDataAttribute(Structure):
    pass

DataAttribute = struct_sDataAttribute# /usr/local/include/libiec61850/iec61850_model.h: 51

# /usr/local/include/libiec61850/iec61850_model.h: 208
class struct_sDataObject(Structure):
    pass

DataObject = struct_sDataObject# /usr/local/include/libiec61850/iec61850_model.h: 56

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

enum_anon_52 = c_int# /usr/local/include/libiec61850/iec61850_model.h: 162

IEC61850_UNKNOWN_TYPE = (-1)# /usr/local/include/libiec61850/iec61850_model.h: 162

IEC61850_BOOLEAN = 0# /usr/local/include/libiec61850/iec61850_model.h: 162

IEC61850_INT8 = 1# /usr/local/include/libiec61850/iec61850_model.h: 162

IEC61850_INT16 = 2# /usr/local/include/libiec61850/iec61850_model.h: 162

IEC61850_INT32 = 3# /usr/local/include/libiec61850/iec61850_model.h: 162

IEC61850_INT64 = 4# /usr/local/include/libiec61850/iec61850_model.h: 162

IEC61850_INT128 = 5# /usr/local/include/libiec61850/iec61850_model.h: 162

IEC61850_INT8U = 6# /usr/local/include/libiec61850/iec61850_model.h: 162

IEC61850_INT16U = 7# /usr/local/include/libiec61850/iec61850_model.h: 162

IEC61850_INT24U = 8# /usr/local/include/libiec61850/iec61850_model.h: 162

IEC61850_INT32U = 9# /usr/local/include/libiec61850/iec61850_model.h: 162

IEC61850_FLOAT32 = 10# /usr/local/include/libiec61850/iec61850_model.h: 162

IEC61850_FLOAT64 = 11# /usr/local/include/libiec61850/iec61850_model.h: 162

IEC61850_ENUMERATED = 12# /usr/local/include/libiec61850/iec61850_model.h: 162

IEC61850_OCTET_STRING_64 = 13# /usr/local/include/libiec61850/iec61850_model.h: 162

IEC61850_OCTET_STRING_6 = 14# /usr/local/include/libiec61850/iec61850_model.h: 162

IEC61850_OCTET_STRING_8 = 15# /usr/local/include/libiec61850/iec61850_model.h: 162

IEC61850_VISIBLE_STRING_32 = 16# /usr/local/include/libiec61850/iec61850_model.h: 162

IEC61850_VISIBLE_STRING_64 = 17# /usr/local/include/libiec61850/iec61850_model.h: 162

IEC61850_VISIBLE_STRING_65 = 18# /usr/local/include/libiec61850/iec61850_model.h: 162

IEC61850_VISIBLE_STRING_129 = 19# /usr/local/include/libiec61850/iec61850_model.h: 162

IEC61850_VISIBLE_STRING_255 = 20# /usr/local/include/libiec61850/iec61850_model.h: 162

IEC61850_UNICODE_STRING_255 = 21# /usr/local/include/libiec61850/iec61850_model.h: 162

IEC61850_TIMESTAMP = 22# /usr/local/include/libiec61850/iec61850_model.h: 162

IEC61850_QUALITY = 23# /usr/local/include/libiec61850/iec61850_model.h: 162

IEC61850_CHECK = 24# /usr/local/include/libiec61850/iec61850_model.h: 162

IEC61850_CODEDENUM = 25# /usr/local/include/libiec61850/iec61850_model.h: 162

IEC61850_GENERIC_BITSTRING = 26# /usr/local/include/libiec61850/iec61850_model.h: 162

IEC61850_CONSTRUCTED = 27# /usr/local/include/libiec61850/iec61850_model.h: 162

IEC61850_ENTRY_TIME = 28# /usr/local/include/libiec61850/iec61850_model.h: 162

IEC61850_PHYCOMADDR = 29# /usr/local/include/libiec61850/iec61850_model.h: 162

IEC61850_CURRENCY = 30# /usr/local/include/libiec61850/iec61850_model.h: 162

IEC61850_OPTFLDS = 31# /usr/local/include/libiec61850/iec61850_model.h: 162

IEC61850_TRGOPS = 32# /usr/local/include/libiec61850/iec61850_model.h: 162

DataAttributeType = enum_anon_52# /usr/local/include/libiec61850/iec61850_model.h: 162

enum_anon_53 = c_int# /usr/local/include/libiec61850/iec61850_model.h: 169

LogicalDeviceModelType = 0# /usr/local/include/libiec61850/iec61850_model.h: 169

LogicalNodeModelType = (LogicalDeviceModelType + 1)# /usr/local/include/libiec61850/iec61850_model.h: 169

DataObjectModelType = (LogicalNodeModelType + 1)# /usr/local/include/libiec61850/iec61850_model.h: 169

DataAttributeModelType = (DataObjectModelType + 1)# /usr/local/include/libiec61850/iec61850_model.h: 169

ModelNodeType = enum_anon_53# /usr/local/include/libiec61850/iec61850_model.h: 169

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

struct_sDataObject.__slots__ = [
    'modelType',
    'name',
    'parent',
    'sibling',
    'firstChild',
    'elementCount',
]
struct_sDataObject._fields_ = [
    ('modelType', ModelNodeType),
    ('name', String),
    ('parent', POINTER(ModelNode)),
    ('sibling', POINTER(ModelNode)),
    ('firstChild', POINTER(ModelNode)),
    ('elementCount', c_int),
]

struct_sDataAttribute.__slots__ = [
    'modelType',
    'name',
    'parent',
    'sibling',
    'firstChild',
    'elementCount',
    'fc',
    'type',
    'triggerOptions',
    'mmsValue',
    'sAddr',
]
struct_sDataAttribute._fields_ = [
    ('modelType', ModelNodeType),
    ('name', String),
    ('parent', POINTER(ModelNode)),
    ('sibling', POINTER(ModelNode)),
    ('firstChild', POINTER(ModelNode)),
    ('elementCount', c_int),
    ('fc', FunctionalConstraint),
    ('type', DataAttributeType),
    ('triggerOptions', uint8_t),
    ('mmsValue', POINTER(MmsValue)),
    ('sAddr', uint32_t),
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

# /usr/local/include/libiec61850/iec61850_model.h: 361
if _libs["/usr/local/lib/libiec61850.so"].has("ModelNode_getChildCount", "cdecl"):
    ModelNode_getChildCount = _libs["/usr/local/lib/libiec61850.so"].get("ModelNode_getChildCount", "cdecl")
    ModelNode_getChildCount.argtypes = [POINTER(ModelNode)]
    ModelNode_getChildCount.restype = c_int

# /usr/local/include/libiec61850/iec61850_model.h: 371
if _libs["/usr/local/lib/libiec61850.so"].has("ModelNode_getChild", "cdecl"):
    ModelNode_getChild = _libs["/usr/local/lib/libiec61850.so"].get("ModelNode_getChild", "cdecl")
    ModelNode_getChild.argtypes = [POINTER(ModelNode), String]
    ModelNode_getChild.restype = POINTER(ModelNode)

# /usr/local/include/libiec61850/iec61850_model.h: 387
if _libs["/usr/local/lib/libiec61850.so"].has("ModelNode_getChildWithFc", "cdecl"):
    ModelNode_getChildWithFc = _libs["/usr/local/lib/libiec61850.so"].get("ModelNode_getChildWithFc", "cdecl")
    ModelNode_getChildWithFc.argtypes = [POINTER(ModelNode), String, FunctionalConstraint]
    ModelNode_getChildWithFc.restype = POINTER(ModelNode)

# /usr/local/include/libiec61850/iec61850_model.h: 399
if _libs["/usr/local/lib/libiec61850.so"].has("ModelNode_getObjectReference", "cdecl"):
    ModelNode_getObjectReference = _libs["/usr/local/lib/libiec61850.so"].get("ModelNode_getObjectReference", "cdecl")
    ModelNode_getObjectReference.argtypes = [POINTER(ModelNode), String]
    if sizeof(c_int) == sizeof(c_void_p):
        ModelNode_getObjectReference.restype = ReturnString
    else:
        ModelNode_getObjectReference.restype = String
        ModelNode_getObjectReference.errcheck = ReturnString

# /usr/local/include/libiec61850/iec61850_model.h: 412
if _libs["/usr/local/lib/libiec61850.so"].has("ModelNode_getObjectReferenceEx", "cdecl"):
    ModelNode_getObjectReferenceEx = _libs["/usr/local/lib/libiec61850.so"].get("ModelNode_getObjectReferenceEx", "cdecl")
    ModelNode_getObjectReferenceEx.argtypes = [POINTER(ModelNode), String, c_bool]
    if sizeof(c_int) == sizeof(c_void_p):
        ModelNode_getObjectReferenceEx.restype = ReturnString
    else:
        ModelNode_getObjectReferenceEx.restype = String
        ModelNode_getObjectReferenceEx.errcheck = ReturnString

# /usr/local/include/libiec61850/iec61850_model.h: 423
if _libs["/usr/local/lib/libiec61850.so"].has("ModelNode_getType", "cdecl"):
    ModelNode_getType = _libs["/usr/local/lib/libiec61850.so"].get("ModelNode_getType", "cdecl")
    ModelNode_getType.argtypes = [POINTER(ModelNode)]
    ModelNode_getType.restype = ModelNodeType

# /usr/local/include/libiec61850/iec61850_model.h: 432
if _libs["/usr/local/lib/libiec61850.so"].has("ModelNode_getName", "cdecl"):
    ModelNode_getName = _libs["/usr/local/lib/libiec61850.so"].get("ModelNode_getName", "cdecl")
    ModelNode_getName.argtypes = [POINTER(ModelNode)]
    ModelNode_getName.restype = c_char_p

# /usr/local/include/libiec61850/iec61850_model.h: 442
if _libs["/usr/local/lib/libiec61850.so"].has("ModelNode_getParent", "cdecl"):
    ModelNode_getParent = _libs["/usr/local/lib/libiec61850.so"].get("ModelNode_getParent", "cdecl")
    ModelNode_getParent.argtypes = [POINTER(ModelNode)]
    ModelNode_getParent.restype = POINTER(ModelNode)

# /usr/local/include/libiec61850/iec61850_model.h: 453
if _libs["/usr/local/lib/libiec61850.so"].has("ModelNode_getChildren", "cdecl"):
    ModelNode_getChildren = _libs["/usr/local/lib/libiec61850.so"].get("ModelNode_getChildren", "cdecl")
    ModelNode_getChildren.argtypes = [POINTER(ModelNode)]
    ModelNode_getChildren.restype = LinkedList

# /usr/local/include/libiec61850/iec61850_model.h: 465
if _libs["/usr/local/lib/libiec61850.so"].has("IedModel_setIedName", "cdecl"):
    IedModel_setIedName = _libs["/usr/local/lib/libiec61850.so"].get("IedModel_setIedName", "cdecl")
    IedModel_setIedName.argtypes = [POINTER(IedModel), String]
    IedModel_setIedName.restype = None

# /usr/local/include/libiec61850/iec61850_model.h: 479
if _libs["/usr/local/lib/libiec61850.so"].has("IedModel_getModelNodeByObjectReference", "cdecl"):
    IedModel_getModelNodeByObjectReference = _libs["/usr/local/lib/libiec61850.so"].get("IedModel_getModelNodeByObjectReference", "cdecl")
    IedModel_getModelNodeByObjectReference.argtypes = [POINTER(IedModel), String]
    IedModel_getModelNodeByObjectReference.restype = POINTER(ModelNode)

# /usr/local/include/libiec61850/iec61850_model.h: 482
if _libs["/usr/local/lib/libiec61850.so"].has("IedModel_getSVControlBlock", "cdecl"):
    IedModel_getSVControlBlock = _libs["/usr/local/lib/libiec61850.so"].get("IedModel_getSVControlBlock", "cdecl")
    IedModel_getSVControlBlock.argtypes = [POINTER(IedModel), POINTER(LogicalNode), String]
    IedModel_getSVControlBlock.restype = POINTER(SVControlBlock)

# /usr/local/include/libiec61850/iec61850_model.h: 497
if _libs["/usr/local/lib/libiec61850.so"].has("IedModel_getModelNodeByShortObjectReference", "cdecl"):
    IedModel_getModelNodeByShortObjectReference = _libs["/usr/local/lib/libiec61850.so"].get("IedModel_getModelNodeByShortObjectReference", "cdecl")
    IedModel_getModelNodeByShortObjectReference.argtypes = [POINTER(IedModel), String]
    IedModel_getModelNodeByShortObjectReference.restype = POINTER(ModelNode)

# /usr/local/include/libiec61850/iec61850_model.h: 511
if _libs["/usr/local/lib/libiec61850.so"].has("IedModel_getModelNodeByShortAddress", "cdecl"):
    IedModel_getModelNodeByShortAddress = _libs["/usr/local/lib/libiec61850.so"].get("IedModel_getModelNodeByShortAddress", "cdecl")
    IedModel_getModelNodeByShortAddress.argtypes = [POINTER(IedModel), uint32_t]
    IedModel_getModelNodeByShortAddress.restype = POINTER(ModelNode)

# /usr/local/include/libiec61850/iec61850_model.h: 522
if _libs["/usr/local/lib/libiec61850.so"].has("IedModel_getDeviceByInst", "cdecl"):
    IedModel_getDeviceByInst = _libs["/usr/local/lib/libiec61850.so"].get("IedModel_getDeviceByInst", "cdecl")
    IedModel_getDeviceByInst.argtypes = [POINTER(IedModel), String]
    IedModel_getDeviceByInst.restype = POINTER(LogicalDevice)

# /usr/local/include/libiec61850/iec61850_model.h: 533
if _libs["/usr/local/lib/libiec61850.so"].has("IedModel_getDeviceByIndex", "cdecl"):
    IedModel_getDeviceByIndex = _libs["/usr/local/lib/libiec61850.so"].get("IedModel_getDeviceByIndex", "cdecl")
    IedModel_getDeviceByIndex.argtypes = [POINTER(IedModel), c_int]
    IedModel_getDeviceByIndex.restype = POINTER(LogicalDevice)

# /usr/local/include/libiec61850/iec61850_model.h: 545
if _libs["/usr/local/lib/libiec61850.so"].has("LogicalDevice_getLogicalNode", "cdecl"):
    LogicalDevice_getLogicalNode = _libs["/usr/local/lib/libiec61850.so"].get("LogicalDevice_getLogicalNode", "cdecl")
    LogicalDevice_getLogicalNode.argtypes = [POINTER(LogicalDevice), String]
    LogicalDevice_getLogicalNode.restype = POINTER(LogicalNode)

# /usr/local/include/libiec61850/iec61850_model.h: 555
if _libs["/usr/local/lib/libiec61850.so"].has("LogicalDevice_getSettingGroupControlBlock", "cdecl"):
    LogicalDevice_getSettingGroupControlBlock = _libs["/usr/local/lib/libiec61850.so"].get("LogicalDevice_getSettingGroupControlBlock", "cdecl")
    LogicalDevice_getSettingGroupControlBlock.argtypes = [POINTER(LogicalDevice)]
    LogicalDevice_getSettingGroupControlBlock.restype = POINTER(SettingGroupControlBlock)

# /usr/local/include/libiec61850/iec61850_model.h: 569
if _libs["/usr/local/lib/libiec61850.so"].has("IedModel_setAttributeValuesToNull", "cdecl"):
    IedModel_setAttributeValuesToNull = _libs["/usr/local/lib/libiec61850.so"].get("IedModel_setAttributeValuesToNull", "cdecl")
    IedModel_setAttributeValuesToNull.argtypes = [POINTER(IedModel)]
    IedModel_setAttributeValuesToNull.restype = None

# /usr/local/include/libiec61850/iec61850_model.h: 579
if _libs["/usr/local/lib/libiec61850.so"].has("IedModel_getDevice", "cdecl"):
    IedModel_getDevice = _libs["/usr/local/lib/libiec61850.so"].get("IedModel_getDevice", "cdecl")
    IedModel_getDevice.argtypes = [POINTER(IedModel), String]
    IedModel_getDevice.restype = POINTER(LogicalDevice)

# /usr/local/include/libiec61850/iec61850_model.h: 590
if _libs["/usr/local/lib/libiec61850.so"].has("IedModel_lookupDataSet", "cdecl"):
    IedModel_lookupDataSet = _libs["/usr/local/lib/libiec61850.so"].get("IedModel_lookupDataSet", "cdecl")
    IedModel_lookupDataSet.argtypes = [POINTER(IedModel), String]
    IedModel_lookupDataSet.restype = POINTER(DataSet)

# /usr/local/include/libiec61850/iec61850_model.h: 601
if _libs["/usr/local/lib/libiec61850.so"].has("IedModel_lookupDataAttributeByMmsValue", "cdecl"):
    IedModel_lookupDataAttributeByMmsValue = _libs["/usr/local/lib/libiec61850.so"].get("IedModel_lookupDataAttributeByMmsValue", "cdecl")
    IedModel_lookupDataAttributeByMmsValue.argtypes = [POINTER(IedModel), POINTER(MmsValue)]
    IedModel_lookupDataAttributeByMmsValue.restype = POINTER(DataAttribute)

# /usr/local/include/libiec61850/iec61850_model.h: 613
if _libs["/usr/local/lib/libiec61850.so"].has("IedModel_getLogicalDeviceCount", "cdecl"):
    IedModel_getLogicalDeviceCount = _libs["/usr/local/lib/libiec61850.so"].get("IedModel_getLogicalDeviceCount", "cdecl")
    IedModel_getLogicalDeviceCount.argtypes = [POINTER(IedModel)]
    IedModel_getLogicalDeviceCount.restype = c_int

# /usr/local/include/libiec61850/iec61850_model.h: 616
if _libs["/usr/local/lib/libiec61850.so"].has("LogicalDevice_getLogicalNodeCount", "cdecl"):
    LogicalDevice_getLogicalNodeCount = _libs["/usr/local/lib/libiec61850.so"].get("LogicalDevice_getLogicalNodeCount", "cdecl")
    LogicalDevice_getLogicalNodeCount.argtypes = [POINTER(LogicalDevice)]
    LogicalDevice_getLogicalNodeCount.restype = c_int

# /usr/local/include/libiec61850/iec61850_model.h: 618
if _libs["/usr/local/lib/libiec61850.so"].has("LogicalDevice_getChildByMmsVariableName", "cdecl"):
    LogicalDevice_getChildByMmsVariableName = _libs["/usr/local/lib/libiec61850.so"].get("LogicalDevice_getChildByMmsVariableName", "cdecl")
    LogicalDevice_getChildByMmsVariableName.argtypes = [POINTER(LogicalDevice), String]
    LogicalDevice_getChildByMmsVariableName.restype = POINTER(ModelNode)

# /usr/local/include/libiec61850/iec61850_model.h: 622
if _libs["/usr/local/lib/libiec61850.so"].has("LogicalNode_hasFCData", "cdecl"):
    LogicalNode_hasFCData = _libs["/usr/local/lib/libiec61850.so"].get("LogicalNode_hasFCData", "cdecl")
    LogicalNode_hasFCData.argtypes = [POINTER(LogicalNode), FunctionalConstraint]
    LogicalNode_hasFCData.restype = c_bool

# /usr/local/include/libiec61850/iec61850_model.h: 625
for _lib in _libs.values():
    if not _lib.has("LogicalNode_hasBufferedReports", "cdecl"):
        continue
    LogicalNode_hasBufferedReports = _lib.get("LogicalNode_hasBufferedReports", "cdecl")
    LogicalNode_hasBufferedReports.argtypes = [POINTER(LogicalNode)]
    LogicalNode_hasBufferedReports.restype = c_bool
    break

# /usr/local/include/libiec61850/iec61850_model.h: 628
for _lib in _libs.values():
    if not _lib.has("LogicalNode_hasUnbufferedReports", "cdecl"):
        continue
    LogicalNode_hasUnbufferedReports = _lib.get("LogicalNode_hasUnbufferedReports", "cdecl")
    LogicalNode_hasUnbufferedReports.argtypes = [POINTER(LogicalNode)]
    LogicalNode_hasUnbufferedReports.restype = c_bool
    break

# /usr/local/include/libiec61850/iec61850_model.h: 638
if _libs["/usr/local/lib/libiec61850.so"].has("LogicalNode_getDataSet", "cdecl"):
    LogicalNode_getDataSet = _libs["/usr/local/lib/libiec61850.so"].get("LogicalNode_getDataSet", "cdecl")
    LogicalNode_getDataSet.argtypes = [POINTER(LogicalNode), String]
    LogicalNode_getDataSet.restype = POINTER(DataSet)

# /usr/local/include/libiec61850/iec61850_model.h: 642
if _libs["/usr/local/lib/libiec61850.so"].has("DataObject_hasFCData", "cdecl"):
    DataObject_hasFCData = _libs["/usr/local/lib/libiec61850.so"].get("DataObject_hasFCData", "cdecl")
    DataObject_hasFCData.argtypes = [POINTER(DataObject), FunctionalConstraint]
    DataObject_hasFCData.restype = c_bool

# /usr/local/include/libiec61850/iec61850_cdc.h: 136
if _libs["/usr/local/lib/libiec61850.so"].has("CAC_AnalogueValue_create", "cdecl"):
    CAC_AnalogueValue_create = _libs["/usr/local/lib/libiec61850.so"].get("CAC_AnalogueValue_create", "cdecl")
    CAC_AnalogueValue_create.argtypes = [String, POINTER(ModelNode), FunctionalConstraint, uint8_t, c_bool]
    CAC_AnalogueValue_create.restype = POINTER(DataAttribute)

# /usr/local/include/libiec61850/iec61850_cdc.h: 146
if _libs["/usr/local/lib/libiec61850.so"].has("CAC_ValWithTrans_create", "cdecl"):
    CAC_ValWithTrans_create = _libs["/usr/local/lib/libiec61850.so"].get("CAC_ValWithTrans_create", "cdecl")
    CAC_ValWithTrans_create.argtypes = [String, POINTER(ModelNode), FunctionalConstraint, uint8_t, c_bool]
    CAC_ValWithTrans_create.restype = POINTER(DataAttribute)

# /usr/local/include/libiec61850/iec61850_cdc.h: 153
if _libs["/usr/local/lib/libiec61850.so"].has("CAC_Vector_create", "cdecl"):
    CAC_Vector_create = _libs["/usr/local/lib/libiec61850.so"].get("CAC_Vector_create", "cdecl")
    CAC_Vector_create.argtypes = [String, POINTER(ModelNode), uint32_t, FunctionalConstraint, uint8_t]
    CAC_Vector_create.restype = POINTER(DataAttribute)

# /usr/local/include/libiec61850/iec61850_cdc.h: 156
if _libs["/usr/local/lib/libiec61850.so"].has("CAC_Point_create", "cdecl"):
    CAC_Point_create = _libs["/usr/local/lib/libiec61850.so"].get("CAC_Point_create", "cdecl")
    CAC_Point_create.argtypes = [String, POINTER(ModelNode), FunctionalConstraint, uint8_t, c_bool]
    CAC_Point_create.restype = POINTER(DataAttribute)

# /usr/local/include/libiec61850/iec61850_cdc.h: 159
if _libs["/usr/local/lib/libiec61850.so"].has("CAC_ScaledValueConfig_create", "cdecl"):
    CAC_ScaledValueConfig_create = _libs["/usr/local/lib/libiec61850.so"].get("CAC_ScaledValueConfig_create", "cdecl")
    CAC_ScaledValueConfig_create.argtypes = [String, POINTER(ModelNode)]
    CAC_ScaledValueConfig_create.restype = POINTER(DataAttribute)

# /usr/local/include/libiec61850/iec61850_cdc.h: 162
if _libs["/usr/local/lib/libiec61850.so"].has("CAC_Unit_create", "cdecl"):
    CAC_Unit_create = _libs["/usr/local/lib/libiec61850.so"].get("CAC_Unit_create", "cdecl")
    CAC_Unit_create.argtypes = [String, POINTER(ModelNode), c_bool]
    CAC_Unit_create.restype = POINTER(DataAttribute)

# /usr/local/include/libiec61850/iec61850_cdc.h: 165
for _lib in _libs.values():
    if not _lib.has("CDA_OperBoolean", "cdecl"):
        continue
    CDA_OperBoolean = _lib.get("CDA_OperBoolean", "cdecl")
    CDA_OperBoolean.argtypes = [POINTER(ModelNode), c_bool]
    CDA_OperBoolean.restype = POINTER(DataAttribute)
    break

# /usr/local/include/libiec61850/iec61850_cdc.h: 172
if _libs["/usr/local/lib/libiec61850.so"].has("CDC_SPS_create", "cdecl"):
    CDC_SPS_create = _libs["/usr/local/lib/libiec61850.so"].get("CDC_SPS_create", "cdecl")
    CDC_SPS_create.argtypes = [String, POINTER(ModelNode), uint32_t]
    CDC_SPS_create.restype = POINTER(DataObject)

# /usr/local/include/libiec61850/iec61850_cdc.h: 175
if _libs["/usr/local/lib/libiec61850.so"].has("CDC_DPS_create", "cdecl"):
    CDC_DPS_create = _libs["/usr/local/lib/libiec61850.so"].get("CDC_DPS_create", "cdecl")
    CDC_DPS_create.argtypes = [String, POINTER(ModelNode), uint32_t]
    CDC_DPS_create.restype = POINTER(DataObject)

# /usr/local/include/libiec61850/iec61850_cdc.h: 178
if _libs["/usr/local/lib/libiec61850.so"].has("CDC_INS_create", "cdecl"):
    CDC_INS_create = _libs["/usr/local/lib/libiec61850.so"].get("CDC_INS_create", "cdecl")
    CDC_INS_create.argtypes = [String, POINTER(ModelNode), uint32_t]
    CDC_INS_create.restype = POINTER(DataObject)

# /usr/local/include/libiec61850/iec61850_cdc.h: 181
if _libs["/usr/local/lib/libiec61850.so"].has("CDC_ENS_create", "cdecl"):
    CDC_ENS_create = _libs["/usr/local/lib/libiec61850.so"].get("CDC_ENS_create", "cdecl")
    CDC_ENS_create.argtypes = [String, POINTER(ModelNode), uint32_t]
    CDC_ENS_create.restype = POINTER(DataObject)

# /usr/local/include/libiec61850/iec61850_cdc.h: 184
if _libs["/usr/local/lib/libiec61850.so"].has("CDC_BCR_create", "cdecl"):
    CDC_BCR_create = _libs["/usr/local/lib/libiec61850.so"].get("CDC_BCR_create", "cdecl")
    CDC_BCR_create.argtypes = [String, POINTER(ModelNode), uint32_t]
    CDC_BCR_create.restype = POINTER(DataObject)

# /usr/local/include/libiec61850/iec61850_cdc.h: 187
if _libs["/usr/local/lib/libiec61850.so"].has("CDC_VSS_create", "cdecl"):
    CDC_VSS_create = _libs["/usr/local/lib/libiec61850.so"].get("CDC_VSS_create", "cdecl")
    CDC_VSS_create.argtypes = [String, POINTER(ModelNode), uint32_t]
    CDC_VSS_create.restype = POINTER(DataObject)

# /usr/local/include/libiec61850/iec61850_cdc.h: 205
if _libs["/usr/local/lib/libiec61850.so"].has("CDC_SEC_create", "cdecl"):
    CDC_SEC_create = _libs["/usr/local/lib/libiec61850.so"].get("CDC_SEC_create", "cdecl")
    CDC_SEC_create.argtypes = [String, POINTER(ModelNode), uint32_t]
    CDC_SEC_create.restype = POINTER(DataObject)

# /usr/local/include/libiec61850/iec61850_cdc.h: 225
if _libs["/usr/local/lib/libiec61850.so"].has("CDC_MV_create", "cdecl"):
    CDC_MV_create = _libs["/usr/local/lib/libiec61850.so"].get("CDC_MV_create", "cdecl")
    CDC_MV_create.argtypes = [String, POINTER(ModelNode), uint32_t, c_bool]
    CDC_MV_create.restype = POINTER(DataObject)

# /usr/local/include/libiec61850/iec61850_cdc.h: 232
if _libs["/usr/local/lib/libiec61850.so"].has("CDC_CMV_create", "cdecl"):
    CDC_CMV_create = _libs["/usr/local/lib/libiec61850.so"].get("CDC_CMV_create", "cdecl")
    CDC_CMV_create.argtypes = [String, POINTER(ModelNode), uint32_t]
    CDC_CMV_create.restype = POINTER(DataObject)

# /usr/local/include/libiec61850/iec61850_cdc.h: 253
if _libs["/usr/local/lib/libiec61850.so"].has("CDC_SAV_create", "cdecl"):
    CDC_SAV_create = _libs["/usr/local/lib/libiec61850.so"].get("CDC_SAV_create", "cdecl")
    CDC_SAV_create.argtypes = [String, POINTER(ModelNode), uint32_t, c_bool]
    CDC_SAV_create.restype = POINTER(DataObject)

# /usr/local/include/libiec61850/iec61850_cdc.h: 277
if _libs["/usr/local/lib/libiec61850.so"].has("CDC_LPL_create", "cdecl"):
    CDC_LPL_create = _libs["/usr/local/lib/libiec61850.so"].get("CDC_LPL_create", "cdecl")
    CDC_LPL_create.argtypes = [String, POINTER(ModelNode), uint32_t]
    CDC_LPL_create.restype = POINTER(DataObject)

# /usr/local/include/libiec61850/iec61850_cdc.h: 301
if _libs["/usr/local/lib/libiec61850.so"].has("CDC_DPL_create", "cdecl"):
    CDC_DPL_create = _libs["/usr/local/lib/libiec61850.so"].get("CDC_DPL_create", "cdecl")
    CDC_DPL_create.argtypes = [String, POINTER(ModelNode), uint32_t]
    CDC_DPL_create.restype = POINTER(DataObject)

# /usr/local/include/libiec61850/iec61850_cdc.h: 304
if _libs["/usr/local/lib/libiec61850.so"].has("CDC_HST_create", "cdecl"):
    CDC_HST_create = _libs["/usr/local/lib/libiec61850.so"].get("CDC_HST_create", "cdecl")
    CDC_HST_create.argtypes = [String, POINTER(ModelNode), uint32_t, uint16_t]
    CDC_HST_create.restype = POINTER(DataObject)

# /usr/local/include/libiec61850/iec61850_cdc.h: 325
if _libs["/usr/local/lib/libiec61850.so"].has("CDC_ACD_create", "cdecl"):
    CDC_ACD_create = _libs["/usr/local/lib/libiec61850.so"].get("CDC_ACD_create", "cdecl")
    CDC_ACD_create.argtypes = [String, POINTER(ModelNode), uint32_t]
    CDC_ACD_create.restype = POINTER(DataObject)

# /usr/local/include/libiec61850/iec61850_cdc.h: 331
if _libs["/usr/local/lib/libiec61850.so"].has("CDC_ACT_create", "cdecl"):
    CDC_ACT_create = _libs["/usr/local/lib/libiec61850.so"].get("CDC_ACT_create", "cdecl")
    CDC_ACT_create.argtypes = [String, POINTER(ModelNode), uint32_t]
    CDC_ACT_create.restype = POINTER(DataObject)

# /usr/local/include/libiec61850/iec61850_cdc.h: 341
if _libs["/usr/local/lib/libiec61850.so"].has("CDC_SPG_create", "cdecl"):
    CDC_SPG_create = _libs["/usr/local/lib/libiec61850.so"].get("CDC_SPG_create", "cdecl")
    CDC_SPG_create.argtypes = [String, POINTER(ModelNode), uint32_t]
    CDC_SPG_create.restype = POINTER(DataObject)

# /usr/local/include/libiec61850/iec61850_cdc.h: 351
if _libs["/usr/local/lib/libiec61850.so"].has("CDC_VSG_create", "cdecl"):
    CDC_VSG_create = _libs["/usr/local/lib/libiec61850.so"].get("CDC_VSG_create", "cdecl")
    CDC_VSG_create.argtypes = [String, POINTER(ModelNode), uint32_t]
    CDC_VSG_create.restype = POINTER(DataObject)

# /usr/local/include/libiec61850/iec61850_cdc.h: 361
if _libs["/usr/local/lib/libiec61850.so"].has("CDC_ENG_create", "cdecl"):
    CDC_ENG_create = _libs["/usr/local/lib/libiec61850.so"].get("CDC_ENG_create", "cdecl")
    CDC_ENG_create.argtypes = [String, POINTER(ModelNode), uint32_t]
    CDC_ENG_create.restype = POINTER(DataObject)

# /usr/local/include/libiec61850/iec61850_cdc.h: 375
if _libs["/usr/local/lib/libiec61850.so"].has("CDC_ING_create", "cdecl"):
    CDC_ING_create = _libs["/usr/local/lib/libiec61850.so"].get("CDC_ING_create", "cdecl")
    CDC_ING_create.argtypes = [String, POINTER(ModelNode), uint32_t]
    CDC_ING_create.restype = POINTER(DataObject)

# /usr/local/include/libiec61850/iec61850_cdc.h: 389
if _libs["/usr/local/lib/libiec61850.so"].has("CDC_ASG_create", "cdecl"):
    CDC_ASG_create = _libs["/usr/local/lib/libiec61850.so"].get("CDC_ASG_create", "cdecl")
    CDC_ASG_create.argtypes = [String, POINTER(ModelNode), uint32_t, c_bool]
    CDC_ASG_create.restype = POINTER(DataObject)

# /usr/local/include/libiec61850/iec61850_cdc.h: 398
if _libs["/usr/local/lib/libiec61850.so"].has("CDC_WYE_create", "cdecl"):
    CDC_WYE_create = _libs["/usr/local/lib/libiec61850.so"].get("CDC_WYE_create", "cdecl")
    CDC_WYE_create.argtypes = [String, POINTER(ModelNode), uint32_t]
    CDC_WYE_create.restype = POINTER(DataObject)

# /usr/local/include/libiec61850/iec61850_cdc.h: 407
if _libs["/usr/local/lib/libiec61850.so"].has("CDC_DEL_create", "cdecl"):
    CDC_DEL_create = _libs["/usr/local/lib/libiec61850.so"].get("CDC_DEL_create", "cdecl")
    CDC_DEL_create.argtypes = [String, POINTER(ModelNode), uint32_t]
    CDC_DEL_create.restype = POINTER(DataObject)

# /usr/local/include/libiec61850/iec61850_cdc.h: 419
if _libs["/usr/local/lib/libiec61850.so"].has("CDC_SPC_create", "cdecl"):
    CDC_SPC_create = _libs["/usr/local/lib/libiec61850.so"].get("CDC_SPC_create", "cdecl")
    CDC_SPC_create.argtypes = [String, POINTER(ModelNode), uint32_t, uint32_t]
    CDC_SPC_create.restype = POINTER(DataObject)

# /usr/local/include/libiec61850/iec61850_cdc.h: 437
if _libs["/usr/local/lib/libiec61850.so"].has("CDC_DPC_create", "cdecl"):
    CDC_DPC_create = _libs["/usr/local/lib/libiec61850.so"].get("CDC_DPC_create", "cdecl")
    CDC_DPC_create.argtypes = [String, POINTER(ModelNode), uint32_t, uint32_t]
    CDC_DPC_create.restype = POINTER(DataObject)

# /usr/local/include/libiec61850/iec61850_cdc.h: 459
if _libs["/usr/local/lib/libiec61850.so"].has("CDC_INC_create", "cdecl"):
    CDC_INC_create = _libs["/usr/local/lib/libiec61850.so"].get("CDC_INC_create", "cdecl")
    CDC_INC_create.argtypes = [String, POINTER(ModelNode), uint32_t, uint32_t]
    CDC_INC_create.restype = POINTER(DataObject)

# /usr/local/include/libiec61850/iec61850_cdc.h: 477
if _libs["/usr/local/lib/libiec61850.so"].has("CDC_ENC_create", "cdecl"):
    CDC_ENC_create = _libs["/usr/local/lib/libiec61850.so"].get("CDC_ENC_create", "cdecl")
    CDC_ENC_create.argtypes = [String, POINTER(ModelNode), uint32_t, uint32_t]
    CDC_ENC_create.restype = POINTER(DataObject)

# /usr/local/include/libiec61850/iec61850_cdc.h: 496
if _libs["/usr/local/lib/libiec61850.so"].has("CDC_BSC_create", "cdecl"):
    CDC_BSC_create = _libs["/usr/local/lib/libiec61850.so"].get("CDC_BSC_create", "cdecl")
    CDC_BSC_create.argtypes = [String, POINTER(ModelNode), uint32_t, uint32_t, c_bool]
    CDC_BSC_create.restype = POINTER(DataObject)

# /usr/local/include/libiec61850/iec61850_cdc.h: 515
if _libs["/usr/local/lib/libiec61850.so"].has("CDC_ISC_create", "cdecl"):
    CDC_ISC_create = _libs["/usr/local/lib/libiec61850.so"].get("CDC_ISC_create", "cdecl")
    CDC_ISC_create.argtypes = [String, POINTER(ModelNode), uint32_t, uint32_t, c_bool]
    CDC_ISC_create.restype = POINTER(DataObject)

# /usr/local/include/libiec61850/iec61850_cdc.h: 536
if _libs["/usr/local/lib/libiec61850.so"].has("CDC_APC_create", "cdecl"):
    CDC_APC_create = _libs["/usr/local/lib/libiec61850.so"].get("CDC_APC_create", "cdecl")
    CDC_APC_create.argtypes = [String, POINTER(ModelNode), uint32_t, uint32_t, c_bool]
    CDC_APC_create.restype = POINTER(DataObject)

# /usr/local/include/libiec61850/iec61850_cdc.h: 558
if _libs["/usr/local/lib/libiec61850.so"].has("CDC_BAC_create", "cdecl"):
    CDC_BAC_create = _libs["/usr/local/lib/libiec61850.so"].get("CDC_BAC_create", "cdecl")
    CDC_BAC_create.argtypes = [String, POINTER(ModelNode), uint32_t, uint32_t, c_bool]
    CDC_BAC_create.restype = POINTER(DataObject)

# /usr/local/include/libiec61850/iec61850_cdc.h: 606
if _libs["/usr/local/lib/libiec61850.so"].has("CDC_SPV_create", "cdecl"):
    CDC_SPV_create = _libs["/usr/local/lib/libiec61850.so"].get("CDC_SPV_create", "cdecl")
    CDC_SPV_create.argtypes = [String, POINTER(ModelNode), uint32_t, uint32_t, uint32_t, c_bool]
    CDC_SPV_create.restype = POINTER(DataObject)

# /usr/local/include/libiec61850/iec61850_cdc.h: 613
if _libs["/usr/local/lib/libiec61850.so"].has("CDC_STV_create", "cdecl"):
    CDC_STV_create = _libs["/usr/local/lib/libiec61850.so"].get("CDC_STV_create", "cdecl")
    CDC_STV_create.argtypes = [String, POINTER(ModelNode), uint32_t, uint32_t, uint32_t, c_bool]
    CDC_STV_create.restype = POINTER(DataObject)

# /usr/local/include/libiec61850/iec61850_cdc.h: 620
if _libs["/usr/local/lib/libiec61850.so"].has("CDC_CMD_create", "cdecl"):
    CDC_CMD_create = _libs["/usr/local/lib/libiec61850.so"].get("CDC_CMD_create", "cdecl")
    CDC_CMD_create.argtypes = [String, POINTER(ModelNode), uint32_t, uint32_t, uint32_t, c_bool, c_bool, c_bool]
    CDC_CMD_create.restype = POINTER(DataObject)

# /usr/local/include/libiec61850/iec61850_cdc.h: 629
if _libs["/usr/local/lib/libiec61850.so"].has("CDC_ALM_create", "cdecl"):
    CDC_ALM_create = _libs["/usr/local/lib/libiec61850.so"].get("CDC_ALM_create", "cdecl")
    CDC_ALM_create.argtypes = [String, POINTER(ModelNode), uint32_t, uint32_t, uint32_t, c_bool]
    CDC_ALM_create.restype = POINTER(DataObject)

# /usr/local/include/libiec61850/iec61850_cdc.h: 636
if _libs["/usr/local/lib/libiec61850.so"].has("CDC_CTE_create", "cdecl"):
    CDC_CTE_create = _libs["/usr/local/lib/libiec61850.so"].get("CDC_CTE_create", "cdecl")
    CDC_CTE_create.argtypes = [String, POINTER(ModelNode), uint32_t, uint32_t, uint32_t, c_bool]
    CDC_CTE_create.restype = POINTER(DataObject)

# /usr/local/include/libiec61850/iec61850_cdc.h: 643
if _libs["/usr/local/lib/libiec61850.so"].has("CDC_TMS_create", "cdecl"):
    CDC_TMS_create = _libs["/usr/local/lib/libiec61850.so"].get("CDC_TMS_create", "cdecl")
    CDC_TMS_create.argtypes = [String, POINTER(ModelNode), uint32_t, uint32_t, uint32_t, c_bool]
    CDC_TMS_create.restype = POINTER(DataObject)

# /usr/local/include/libiec61850/iec61850_dynamic_model.h: 55
if _libs["/usr/local/lib/libiec61850.so"].has("IedModel_create", "cdecl"):
    IedModel_create = _libs["/usr/local/lib/libiec61850.so"].get("IedModel_create", "cdecl")
    IedModel_create.argtypes = [String]
    IedModel_create.restype = POINTER(IedModel)

# /usr/local/include/libiec61850/iec61850_dynamic_model.h: 70
if _libs["/usr/local/lib/libiec61850.so"].has("IedModel_setIedNameForDynamicModel", "cdecl"):
    IedModel_setIedNameForDynamicModel = _libs["/usr/local/lib/libiec61850.so"].get("IedModel_setIedNameForDynamicModel", "cdecl")
    IedModel_setIedNameForDynamicModel.argtypes = [POINTER(IedModel), String]
    IedModel_setIedNameForDynamicModel.restype = None

# /usr/local/include/libiec61850/iec61850_dynamic_model.h: 82
if _libs["/usr/local/lib/libiec61850.so"].has("IedModel_destroy", "cdecl"):
    IedModel_destroy = _libs["/usr/local/lib/libiec61850.so"].get("IedModel_destroy", "cdecl")
    IedModel_destroy.argtypes = [POINTER(IedModel)]
    IedModel_destroy.restype = None

# /usr/local/include/libiec61850/iec61850_dynamic_model.h: 92
if _libs["/usr/local/lib/libiec61850.so"].has("LogicalDevice_create", "cdecl"):
    LogicalDevice_create = _libs["/usr/local/lib/libiec61850.so"].get("LogicalDevice_create", "cdecl")
    LogicalDevice_create.argtypes = [String, POINTER(IedModel)]
    LogicalDevice_create.restype = POINTER(LogicalDevice)

# /usr/local/include/libiec61850/iec61850_dynamic_model.h: 104
if _libs["/usr/local/lib/libiec61850.so"].has("LogicalNode_create", "cdecl"):
    LogicalNode_create = _libs["/usr/local/lib/libiec61850.so"].get("LogicalNode_create", "cdecl")
    LogicalNode_create.argtypes = [String, POINTER(LogicalDevice)]
    LogicalNode_create.restype = POINTER(LogicalNode)

# /usr/local/include/libiec61850/iec61850_dynamic_model.h: 118
if _libs["/usr/local/lib/libiec61850.so"].has("DataObject_create", "cdecl"):
    DataObject_create = _libs["/usr/local/lib/libiec61850.so"].get("DataObject_create", "cdecl")
    DataObject_create.argtypes = [String, POINTER(ModelNode), c_int]
    DataObject_create.restype = POINTER(DataObject)

# /usr/local/include/libiec61850/iec61850_dynamic_model.h: 136
if _libs["/usr/local/lib/libiec61850.so"].has("DataAttribute_create", "cdecl"):
    DataAttribute_create = _libs["/usr/local/lib/libiec61850.so"].get("DataAttribute_create", "cdecl")
    DataAttribute_create.argtypes = [String, POINTER(ModelNode), DataAttributeType, FunctionalConstraint, uint8_t, c_int, uint32_t]
    DataAttribute_create.restype = POINTER(DataAttribute)

# /usr/local/include/libiec61850/iec61850_dynamic_model.h: 148
if _libs["/usr/local/lib/libiec61850.so"].has("DataAttribute_getType", "cdecl"):
    DataAttribute_getType = _libs["/usr/local/lib/libiec61850.so"].get("DataAttribute_getType", "cdecl")
    DataAttribute_getType.argtypes = [POINTER(DataAttribute)]
    DataAttribute_getType.restype = DataAttributeType

# /usr/local/include/libiec61850/iec61850_dynamic_model.h: 158
if _libs["/usr/local/lib/libiec61850.so"].has("DataAttribute_getFC", "cdecl"):
    DataAttribute_getFC = _libs["/usr/local/lib/libiec61850.so"].get("DataAttribute_getFC", "cdecl")
    DataAttribute_getFC.argtypes = [POINTER(DataAttribute)]
    DataAttribute_getFC.restype = FunctionalConstraint

# /usr/local/include/libiec61850/iec61850_dynamic_model.h: 168
if _libs["/usr/local/lib/libiec61850.so"].has("DataAttribute_getTrgOps", "cdecl"):
    DataAttribute_getTrgOps = _libs["/usr/local/lib/libiec61850.so"].get("DataAttribute_getTrgOps", "cdecl")
    DataAttribute_getTrgOps.argtypes = [POINTER(DataAttribute)]
    DataAttribute_getTrgOps.restype = uint8_t

# /usr/local/include/libiec61850/iec61850_dynamic_model.h: 177
if _libs["/usr/local/lib/libiec61850.so"].has("DataAttribute_setValue", "cdecl"):
    DataAttribute_setValue = _libs["/usr/local/lib/libiec61850.so"].get("DataAttribute_setValue", "cdecl")
    DataAttribute_setValue.argtypes = [POINTER(DataAttribute), POINTER(MmsValue)]
    DataAttribute_setValue.restype = None

# /usr/local/include/libiec61850/iec61850_dynamic_model.h: 198
if _libs["/usr/local/lib/libiec61850.so"].has("ReportControlBlock_create", "cdecl"):
    ReportControlBlock_create = _libs["/usr/local/lib/libiec61850.so"].get("ReportControlBlock_create", "cdecl")
    ReportControlBlock_create.argtypes = [String, POINTER(LogicalNode), String, c_bool, String, uint32_t, uint8_t, uint8_t, uint32_t, uint32_t]
    ReportControlBlock_create.restype = POINTER(ReportControlBlock)

# /usr/local/include/libiec61850/iec61850_dynamic_model.h: 212
if _libs["/usr/local/lib/libiec61850.so"].has("ReportControlBlock_setPreconfiguredClient", "cdecl"):
    ReportControlBlock_setPreconfiguredClient = _libs["/usr/local/lib/libiec61850.so"].get("ReportControlBlock_setPreconfiguredClient", "cdecl")
    ReportControlBlock_setPreconfiguredClient.argtypes = [POINTER(ReportControlBlock), uint8_t, POINTER(uint8_t)]
    ReportControlBlock_setPreconfiguredClient.restype = None

# /usr/local/include/libiec61850/iec61850_dynamic_model.h: 223
if _libs["/usr/local/lib/libiec61850.so"].has("ReportControlBlock_getName", "cdecl"):
    ReportControlBlock_getName = _libs["/usr/local/lib/libiec61850.so"].get("ReportControlBlock_getName", "cdecl")
    ReportControlBlock_getName.argtypes = [POINTER(ReportControlBlock)]
    ReportControlBlock_getName.restype = c_char_p

# /usr/local/include/libiec61850/iec61850_dynamic_model.h: 234
if _libs["/usr/local/lib/libiec61850.so"].has("ReportControlBlock_isBuffered", "cdecl"):
    ReportControlBlock_isBuffered = _libs["/usr/local/lib/libiec61850.so"].get("ReportControlBlock_isBuffered", "cdecl")
    ReportControlBlock_isBuffered.argtypes = [POINTER(ReportControlBlock)]
    ReportControlBlock_isBuffered.restype = c_bool

# /usr/local/include/libiec61850/iec61850_dynamic_model.h: 243
if _libs["/usr/local/lib/libiec61850.so"].has("ReportControlBlock_getParent", "cdecl"):
    ReportControlBlock_getParent = _libs["/usr/local/lib/libiec61850.so"].get("ReportControlBlock_getParent", "cdecl")
    ReportControlBlock_getParent.argtypes = [POINTER(ReportControlBlock)]
    ReportControlBlock_getParent.restype = POINTER(LogicalNode)

# /usr/local/include/libiec61850/iec61850_dynamic_model.h: 253
if _libs["/usr/local/lib/libiec61850.so"].has("ReportControlBlock_getRptID", "cdecl"):
    ReportControlBlock_getRptID = _libs["/usr/local/lib/libiec61850.so"].get("ReportControlBlock_getRptID", "cdecl")
    ReportControlBlock_getRptID.argtypes = [POINTER(ReportControlBlock)]
    if sizeof(c_int) == sizeof(c_void_p):
        ReportControlBlock_getRptID.restype = ReturnString
    else:
        ReportControlBlock_getRptID.restype = String
        ReportControlBlock_getRptID.errcheck = ReturnString

# /usr/local/include/libiec61850/iec61850_dynamic_model.h: 264
if _libs["/usr/local/lib/libiec61850.so"].has("ReportControlBlock_getRptEna", "cdecl"):
    ReportControlBlock_getRptEna = _libs["/usr/local/lib/libiec61850.so"].get("ReportControlBlock_getRptEna", "cdecl")
    ReportControlBlock_getRptEna.argtypes = [POINTER(ReportControlBlock)]
    ReportControlBlock_getRptEna.restype = c_bool

# /usr/local/include/libiec61850/iec61850_dynamic_model.h: 273
if _libs["/usr/local/lib/libiec61850.so"].has("ReportControlBlock_getDataSet", "cdecl"):
    ReportControlBlock_getDataSet = _libs["/usr/local/lib/libiec61850.so"].get("ReportControlBlock_getDataSet", "cdecl")
    ReportControlBlock_getDataSet.argtypes = [POINTER(ReportControlBlock)]
    if sizeof(c_int) == sizeof(c_void_p):
        ReportControlBlock_getDataSet.restype = ReturnString
    else:
        ReportControlBlock_getDataSet.restype = String
        ReportControlBlock_getDataSet.errcheck = ReturnString

# /usr/local/include/libiec61850/iec61850_dynamic_model.h: 284
if _libs["/usr/local/lib/libiec61850.so"].has("ReportControlBlock_getConfRev", "cdecl"):
    ReportControlBlock_getConfRev = _libs["/usr/local/lib/libiec61850.so"].get("ReportControlBlock_getConfRev", "cdecl")
    ReportControlBlock_getConfRev.argtypes = [POINTER(ReportControlBlock)]
    ReportControlBlock_getConfRev.restype = uint32_t

# /usr/local/include/libiec61850/iec61850_dynamic_model.h: 304
if _libs["/usr/local/lib/libiec61850.so"].has("ReportControlBlock_getOptFlds", "cdecl"):
    ReportControlBlock_getOptFlds = _libs["/usr/local/lib/libiec61850.so"].get("ReportControlBlock_getOptFlds", "cdecl")
    ReportControlBlock_getOptFlds.argtypes = [POINTER(ReportControlBlock)]
    ReportControlBlock_getOptFlds.restype = uint32_t

# /usr/local/include/libiec61850/iec61850_dynamic_model.h: 317
if _libs["/usr/local/lib/libiec61850.so"].has("ReportControlBlock_getBufTm", "cdecl"):
    ReportControlBlock_getBufTm = _libs["/usr/local/lib/libiec61850.so"].get("ReportControlBlock_getBufTm", "cdecl")
    ReportControlBlock_getBufTm.argtypes = [POINTER(ReportControlBlock)]
    ReportControlBlock_getBufTm.restype = uint32_t

# /usr/local/include/libiec61850/iec61850_dynamic_model.h: 320
if _libs["/usr/local/lib/libiec61850.so"].has("ReportControlBlock_getSqNum", "cdecl"):
    ReportControlBlock_getSqNum = _libs["/usr/local/lib/libiec61850.so"].get("ReportControlBlock_getSqNum", "cdecl")
    ReportControlBlock_getSqNum.argtypes = [POINTER(ReportControlBlock)]
    ReportControlBlock_getSqNum.restype = uint16_t

# /usr/local/include/libiec61850/iec61850_dynamic_model.h: 337
if _libs["/usr/local/lib/libiec61850.so"].has("ReportControlBlock_getTrgOps", "cdecl"):
    ReportControlBlock_getTrgOps = _libs["/usr/local/lib/libiec61850.so"].get("ReportControlBlock_getTrgOps", "cdecl")
    ReportControlBlock_getTrgOps.argtypes = [POINTER(ReportControlBlock)]
    ReportControlBlock_getTrgOps.restype = uint32_t

# /usr/local/include/libiec61850/iec61850_dynamic_model.h: 340
if _libs["/usr/local/lib/libiec61850.so"].has("ReportControlBlock_getIntgPd", "cdecl"):
    ReportControlBlock_getIntgPd = _libs["/usr/local/lib/libiec61850.so"].get("ReportControlBlock_getIntgPd", "cdecl")
    ReportControlBlock_getIntgPd.argtypes = [POINTER(ReportControlBlock)]
    ReportControlBlock_getIntgPd.restype = uint32_t

# /usr/local/include/libiec61850/iec61850_dynamic_model.h: 343
if _libs["/usr/local/lib/libiec61850.so"].has("ReportControlBlock_getGI", "cdecl"):
    ReportControlBlock_getGI = _libs["/usr/local/lib/libiec61850.so"].get("ReportControlBlock_getGI", "cdecl")
    ReportControlBlock_getGI.argtypes = [POINTER(ReportControlBlock)]
    ReportControlBlock_getGI.restype = c_bool

# /usr/local/include/libiec61850/iec61850_dynamic_model.h: 346
if _libs["/usr/local/lib/libiec61850.so"].has("ReportControlBlock_getPurgeBuf", "cdecl"):
    ReportControlBlock_getPurgeBuf = _libs["/usr/local/lib/libiec61850.so"].get("ReportControlBlock_getPurgeBuf", "cdecl")
    ReportControlBlock_getPurgeBuf.argtypes = [POINTER(ReportControlBlock)]
    ReportControlBlock_getPurgeBuf.restype = c_bool

# /usr/local/include/libiec61850/iec61850_dynamic_model.h: 348
if _libs["/usr/local/lib/libiec61850.so"].has("ReportControlBlock_getEntryId", "cdecl"):
    ReportControlBlock_getEntryId = _libs["/usr/local/lib/libiec61850.so"].get("ReportControlBlock_getEntryId", "cdecl")
    ReportControlBlock_getEntryId.argtypes = [POINTER(ReportControlBlock)]
    ReportControlBlock_getEntryId.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/iec61850_dynamic_model.h: 352
if _libs["/usr/local/lib/libiec61850.so"].has("ReportControlBlock_getTimeofEntry", "cdecl"):
    ReportControlBlock_getTimeofEntry = _libs["/usr/local/lib/libiec61850.so"].get("ReportControlBlock_getTimeofEntry", "cdecl")
    ReportControlBlock_getTimeofEntry.argtypes = [POINTER(ReportControlBlock)]
    ReportControlBlock_getTimeofEntry.restype = uint64_t

# /usr/local/include/libiec61850/iec61850_dynamic_model.h: 355
if _libs["/usr/local/lib/libiec61850.so"].has("ReportControlBlock_getResvTms", "cdecl"):
    ReportControlBlock_getResvTms = _libs["/usr/local/lib/libiec61850.so"].get("ReportControlBlock_getResvTms", "cdecl")
    ReportControlBlock_getResvTms.argtypes = [POINTER(ReportControlBlock)]
    ReportControlBlock_getResvTms.restype = c_int16

# /usr/local/include/libiec61850/iec61850_dynamic_model.h: 358
if _libs["/usr/local/lib/libiec61850.so"].has("ReportControlBlock_getResv", "cdecl"):
    ReportControlBlock_getResv = _libs["/usr/local/lib/libiec61850.so"].get("ReportControlBlock_getResv", "cdecl")
    ReportControlBlock_getResv.argtypes = [POINTER(ReportControlBlock)]
    ReportControlBlock_getResv.restype = c_bool

# /usr/local/include/libiec61850/iec61850_dynamic_model.h: 360
if _libs["/usr/local/lib/libiec61850.so"].has("ReportControlBlock_getOwner", "cdecl"):
    ReportControlBlock_getOwner = _libs["/usr/local/lib/libiec61850.so"].get("ReportControlBlock_getOwner", "cdecl")
    ReportControlBlock_getOwner.argtypes = [POINTER(ReportControlBlock)]
    ReportControlBlock_getOwner.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/iec61850_dynamic_model.h: 380
if _libs["/usr/local/lib/libiec61850.so"].has("LogControlBlock_create", "cdecl"):
    LogControlBlock_create = _libs["/usr/local/lib/libiec61850.so"].get("LogControlBlock_create", "cdecl")
    LogControlBlock_create.argtypes = [String, POINTER(LogicalNode), String, String, uint8_t, uint32_t, c_bool, c_bool]
    LogControlBlock_create.restype = POINTER(LogControlBlock)

# /usr/local/include/libiec61850/iec61850_dynamic_model.h: 392
if _libs["/usr/local/lib/libiec61850.so"].has("Log_create", "cdecl"):
    Log_create = _libs["/usr/local/lib/libiec61850.so"].get("Log_create", "cdecl")
    Log_create.argtypes = [String, POINTER(LogicalNode)]
    Log_create.restype = POINTER(Log)

# /usr/local/include/libiec61850/iec61850_dynamic_model.h: 406
if _libs["/usr/local/lib/libiec61850.so"].has("SettingGroupControlBlock_create", "cdecl"):
    SettingGroupControlBlock_create = _libs["/usr/local/lib/libiec61850.so"].get("SettingGroupControlBlock_create", "cdecl")
    SettingGroupControlBlock_create.argtypes = [POINTER(LogicalNode), uint8_t, uint8_t]
    SettingGroupControlBlock_create.restype = POINTER(SettingGroupControlBlock)

# /usr/local/include/libiec61850/iec61850_dynamic_model.h: 425
if _libs["/usr/local/lib/libiec61850.so"].has("GSEControlBlock_create", "cdecl"):
    GSEControlBlock_create = _libs["/usr/local/lib/libiec61850.so"].get("GSEControlBlock_create", "cdecl")
    GSEControlBlock_create.argtypes = [String, POINTER(LogicalNode), String, String, uint32_t, c_bool, c_int, c_int]
    GSEControlBlock_create.restype = POINTER(GSEControlBlock)

# /usr/local/include/libiec61850/iec61850_dynamic_model.h: 445
if _libs["/usr/local/lib/libiec61850.so"].has("SVControlBlock_create", "cdecl"):
    SVControlBlock_create = _libs["/usr/local/lib/libiec61850.so"].get("SVControlBlock_create", "cdecl")
    SVControlBlock_create.argtypes = [String, POINTER(LogicalNode), String, String, uint32_t, uint8_t, uint16_t, uint8_t, c_bool]
    SVControlBlock_create.restype = POINTER(SVControlBlock)

# /usr/local/include/libiec61850/iec61850_dynamic_model.h: 450
if _libs["/usr/local/lib/libiec61850.so"].has("SVControlBlock_addPhyComAddress", "cdecl"):
    SVControlBlock_addPhyComAddress = _libs["/usr/local/lib/libiec61850.so"].get("SVControlBlock_addPhyComAddress", "cdecl")
    SVControlBlock_addPhyComAddress.argtypes = [POINTER(SVControlBlock), POINTER(PhyComAddress)]
    SVControlBlock_addPhyComAddress.restype = None

# /usr/local/include/libiec61850/iec61850_dynamic_model.h: 453
if _libs["/usr/local/lib/libiec61850.so"].has("GSEControlBlock_addPhyComAddress", "cdecl"):
    GSEControlBlock_addPhyComAddress = _libs["/usr/local/lib/libiec61850.so"].get("GSEControlBlock_addPhyComAddress", "cdecl")
    GSEControlBlock_addPhyComAddress.argtypes = [POINTER(GSEControlBlock), POINTER(PhyComAddress)]
    GSEControlBlock_addPhyComAddress.restype = None

# /usr/local/include/libiec61850/iec61850_dynamic_model.h: 467
if _libs["/usr/local/lib/libiec61850.so"].has("PhyComAddress_create", "cdecl"):
    PhyComAddress_create = _libs["/usr/local/lib/libiec61850.so"].get("PhyComAddress_create", "cdecl")
    PhyComAddress_create.argtypes = [uint8_t, uint16_t, uint16_t, POINTER(uint8_t)]
    PhyComAddress_create.restype = POINTER(PhyComAddress)

# /usr/local/include/libiec61850/iec61850_dynamic_model.h: 478
if _libs["/usr/local/lib/libiec61850.so"].has("DataSet_create", "cdecl"):
    DataSet_create = _libs["/usr/local/lib/libiec61850.so"].get("DataSet_create", "cdecl")
    DataSet_create.argtypes = [String, POINTER(LogicalNode)]
    DataSet_create.restype = POINTER(DataSet)

# /usr/local/include/libiec61850/iec61850_dynamic_model.h: 488
if _libs["/usr/local/lib/libiec61850.so"].has("DataSet_getName", "cdecl"):
    DataSet_getName = _libs["/usr/local/lib/libiec61850.so"].get("DataSet_getName", "cdecl")
    DataSet_getName.argtypes = [POINTER(DataSet)]
    DataSet_getName.restype = c_char_p

# /usr/local/include/libiec61850/iec61850_dynamic_model.h: 499
if _libs["/usr/local/lib/libiec61850.so"].has("DataSet_getSize", "cdecl"):
    DataSet_getSize = _libs["/usr/local/lib/libiec61850.so"].get("DataSet_getSize", "cdecl")
    DataSet_getSize.argtypes = [POINTER(DataSet)]
    DataSet_getSize.restype = c_int

# /usr/local/include/libiec61850/iec61850_dynamic_model.h: 501
if _libs["/usr/local/lib/libiec61850.so"].has("DataSet_getFirstEntry", "cdecl"):
    DataSet_getFirstEntry = _libs["/usr/local/lib/libiec61850.so"].get("DataSet_getFirstEntry", "cdecl")
    DataSet_getFirstEntry.argtypes = [POINTER(DataSet)]
    DataSet_getFirstEntry.restype = POINTER(DataSetEntry)

# /usr/local/include/libiec61850/iec61850_dynamic_model.h: 504
if _libs["/usr/local/lib/libiec61850.so"].has("DataSetEntry_getNext", "cdecl"):
    DataSetEntry_getNext = _libs["/usr/local/lib/libiec61850.so"].get("DataSetEntry_getNext", "cdecl")
    DataSetEntry_getNext.argtypes = [POINTER(DataSetEntry)]
    DataSetEntry_getNext.restype = POINTER(DataSetEntry)

# /usr/local/include/libiec61850/iec61850_dynamic_model.h: 527
if _libs["/usr/local/lib/libiec61850.so"].has("DataSetEntry_create", "cdecl"):
    DataSetEntry_create = _libs["/usr/local/lib/libiec61850.so"].get("DataSetEntry_create", "cdecl")
    DataSetEntry_create.argtypes = [POINTER(DataSet), String, c_int, String]
    DataSetEntry_create.restype = POINTER(DataSetEntry)

# /usr/local/include/libiec61850/iec61850_config_file_parser.h: 50
if _libs["/usr/local/lib/libiec61850.so"].has("ConfigFileParser_createModelFromConfigFileEx", "cdecl"):
    ConfigFileParser_createModelFromConfigFileEx = _libs["/usr/local/lib/libiec61850.so"].get("ConfigFileParser_createModelFromConfigFileEx", "cdecl")
    ConfigFileParser_createModelFromConfigFileEx.argtypes = [String]
    ConfigFileParser_createModelFromConfigFileEx.restype = POINTER(IedModel)

# /usr/local/include/libiec61850/iec61850_config_file_parser.h: 53
if _libs["/usr/local/lib/libiec61850.so"].has("ConfigFileParser_createModelFromConfigFile", "cdecl"):
    ConfigFileParser_createModelFromConfigFile = _libs["/usr/local/lib/libiec61850.so"].get("ConfigFileParser_createModelFromConfigFile", "cdecl")
    ConfigFileParser_createModelFromConfigFile.argtypes = [FileHandle]
    ConfigFileParser_createModelFromConfigFile.restype = POINTER(IedModel)

# /usr/local/include/libiec61850/iec61850_server.h: 57
class struct_sIedServerConfig(Structure):
    pass

IedServerConfig = POINTER(struct_sIedServerConfig)# /usr/local/include/libiec61850/iec61850_server.h: 55

struct_sIedServerConfig.__slots__ = [
    'reportBufferSize',
    'reportBufferSizeURCBs',
    'fileServiceBasepath',
    'enableFileService',
    'enableDynamicDataSetService',
    'maxAssociationSpecificDataSets',
    'maxDomainSpecificDataSets',
    'maxDataSetEntries',
    'enableLogService',
    'useIntegratedGoosePublisher',
    'edition',
    'maxMmsConnections',
    'enableEditSG',
    'enableResvTmsForSGCB',
    'enableResvTmsForBRCB',
    'enableOwnerForRCB',
    'syncIntegrityReportTimes',
    'reportSettingsWritable',
]
struct_sIedServerConfig._fields_ = [
    ('reportBufferSize', c_int),
    ('reportBufferSizeURCBs', c_int),
    ('fileServiceBasepath', String),
    ('enableFileService', c_bool),
    ('enableDynamicDataSetService', c_bool),
    ('maxAssociationSpecificDataSets', c_int),
    ('maxDomainSpecificDataSets', c_int),
    ('maxDataSetEntries', c_int),
    ('enableLogService', c_bool),
    ('useIntegratedGoosePublisher', c_bool),
    ('edition', uint8_t),
    ('maxMmsConnections', c_int),
    ('enableEditSG', c_bool),
    ('enableResvTmsForSGCB', c_bool),
    ('enableResvTmsForBRCB', c_bool),
    ('enableOwnerForRCB', c_bool),
    ('syncIntegrityReportTimes', c_bool),
    ('reportSettingsWritable', uint8_t),
]

# /usr/local/include/libiec61850/iec61850_server.h: 120
if _libs["/usr/local/lib/libiec61850.so"].has("IedServerConfig_create", "cdecl"):
    IedServerConfig_create = _libs["/usr/local/lib/libiec61850.so"].get("IedServerConfig_create", "cdecl")
    IedServerConfig_create.argtypes = []
    IedServerConfig_create.restype = IedServerConfig

# /usr/local/include/libiec61850/iec61850_server.h: 126
if _libs["/usr/local/lib/libiec61850.so"].has("IedServerConfig_destroy", "cdecl"):
    IedServerConfig_destroy = _libs["/usr/local/lib/libiec61850.so"].get("IedServerConfig_destroy", "cdecl")
    IedServerConfig_destroy.argtypes = [IedServerConfig]
    IedServerConfig_destroy.restype = None

# /usr/local/include/libiec61850/iec61850_server.h: 134
if _libs["/usr/local/lib/libiec61850.so"].has("IedServerConfig_setEdition", "cdecl"):
    IedServerConfig_setEdition = _libs["/usr/local/lib/libiec61850.so"].get("IedServerConfig_setEdition", "cdecl")
    IedServerConfig_setEdition.argtypes = [IedServerConfig, uint8_t]
    IedServerConfig_setEdition.restype = None

# /usr/local/include/libiec61850/iec61850_server.h: 142
if _libs["/usr/local/lib/libiec61850.so"].has("IedServerConfig_getEdition", "cdecl"):
    IedServerConfig_getEdition = _libs["/usr/local/lib/libiec61850.so"].get("IedServerConfig_getEdition", "cdecl")
    IedServerConfig_getEdition.argtypes = [IedServerConfig]
    IedServerConfig_getEdition.restype = uint8_t

# /usr/local/include/libiec61850/iec61850_server.h: 150
if _libs["/usr/local/lib/libiec61850.so"].has("IedServerConfig_setReportBufferSize", "cdecl"):
    IedServerConfig_setReportBufferSize = _libs["/usr/local/lib/libiec61850.so"].get("IedServerConfig_setReportBufferSize", "cdecl")
    IedServerConfig_setReportBufferSize.argtypes = [IedServerConfig, c_int]
    IedServerConfig_setReportBufferSize.restype = None

# /usr/local/include/libiec61850/iec61850_server.h: 158
if _libs["/usr/local/lib/libiec61850.so"].has("IedServerConfig_getReportBufferSize", "cdecl"):
    IedServerConfig_getReportBufferSize = _libs["/usr/local/lib/libiec61850.so"].get("IedServerConfig_getReportBufferSize", "cdecl")
    IedServerConfig_getReportBufferSize.argtypes = [IedServerConfig]
    IedServerConfig_getReportBufferSize.restype = c_int

# /usr/local/include/libiec61850/iec61850_server.h: 166
if _libs["/usr/local/lib/libiec61850.so"].has("IedServerConfig_setReportBufferSizeForURCBs", "cdecl"):
    IedServerConfig_setReportBufferSizeForURCBs = _libs["/usr/local/lib/libiec61850.so"].get("IedServerConfig_setReportBufferSizeForURCBs", "cdecl")
    IedServerConfig_setReportBufferSizeForURCBs.argtypes = [IedServerConfig, c_int]
    IedServerConfig_setReportBufferSizeForURCBs.restype = None

# /usr/local/include/libiec61850/iec61850_server.h: 174
if _libs["/usr/local/lib/libiec61850.so"].has("IedServerConfig_getReportBufferSizeForURCBs", "cdecl"):
    IedServerConfig_getReportBufferSizeForURCBs = _libs["/usr/local/lib/libiec61850.so"].get("IedServerConfig_getReportBufferSizeForURCBs", "cdecl")
    IedServerConfig_getReportBufferSizeForURCBs.argtypes = [IedServerConfig]
    IedServerConfig_getReportBufferSizeForURCBs.restype = c_int

# /usr/local/include/libiec61850/iec61850_server.h: 185
if _libs["/usr/local/lib/libiec61850.so"].has("IedServerConfig_setMaxMmsConnections", "cdecl"):
    IedServerConfig_setMaxMmsConnections = _libs["/usr/local/lib/libiec61850.so"].get("IedServerConfig_setMaxMmsConnections", "cdecl")
    IedServerConfig_setMaxMmsConnections.argtypes = [IedServerConfig, c_int]
    IedServerConfig_setMaxMmsConnections.restype = None

# /usr/local/include/libiec61850/iec61850_server.h: 193
if _libs["/usr/local/lib/libiec61850.so"].has("IedServerConfig_getMaxMmsConnections", "cdecl"):
    IedServerConfig_getMaxMmsConnections = _libs["/usr/local/lib/libiec61850.so"].get("IedServerConfig_getMaxMmsConnections", "cdecl")
    IedServerConfig_getMaxMmsConnections.argtypes = [IedServerConfig]
    IedServerConfig_getMaxMmsConnections.restype = c_int

# /usr/local/include/libiec61850/iec61850_server.h: 205
if _libs["/usr/local/lib/libiec61850.so"].has("IedServerConfig_setSyncIntegrityReportTimes", "cdecl"):
    IedServerConfig_setSyncIntegrityReportTimes = _libs["/usr/local/lib/libiec61850.so"].get("IedServerConfig_setSyncIntegrityReportTimes", "cdecl")
    IedServerConfig_setSyncIntegrityReportTimes.argtypes = [IedServerConfig, c_bool]
    IedServerConfig_setSyncIntegrityReportTimes.restype = None

# /usr/local/include/libiec61850/iec61850_server.h: 217
if _libs["/usr/local/lib/libiec61850.so"].has("IedServerConfig_getSyncIntegrityReportTimes", "cdecl"):
    IedServerConfig_getSyncIntegrityReportTimes = _libs["/usr/local/lib/libiec61850.so"].get("IedServerConfig_getSyncIntegrityReportTimes", "cdecl")
    IedServerConfig_getSyncIntegrityReportTimes.argtypes = [IedServerConfig]
    IedServerConfig_getSyncIntegrityReportTimes.restype = c_bool

# /usr/local/include/libiec61850/iec61850_server.h: 227
if _libs["/usr/local/lib/libiec61850.so"].has("IedServerConfig_setFileServiceBasePath", "cdecl"):
    IedServerConfig_setFileServiceBasePath = _libs["/usr/local/lib/libiec61850.so"].get("IedServerConfig_setFileServiceBasePath", "cdecl")
    IedServerConfig_setFileServiceBasePath.argtypes = [IedServerConfig, String]
    IedServerConfig_setFileServiceBasePath.restype = None

# /usr/local/include/libiec61850/iec61850_server.h: 232
if _libs["/usr/local/lib/libiec61850.so"].has("IedServerConfig_getFileServiceBasePath", "cdecl"):
    IedServerConfig_getFileServiceBasePath = _libs["/usr/local/lib/libiec61850.so"].get("IedServerConfig_getFileServiceBasePath", "cdecl")
    IedServerConfig_getFileServiceBasePath.argtypes = [IedServerConfig]
    IedServerConfig_getFileServiceBasePath.restype = c_char_p

# /usr/local/include/libiec61850/iec61850_server.h: 241
if _libs["/usr/local/lib/libiec61850.so"].has("IedServerConfig_enableFileService", "cdecl"):
    IedServerConfig_enableFileService = _libs["/usr/local/lib/libiec61850.so"].get("IedServerConfig_enableFileService", "cdecl")
    IedServerConfig_enableFileService.argtypes = [IedServerConfig, c_bool]
    IedServerConfig_enableFileService.restype = None

# /usr/local/include/libiec61850/iec61850_server.h: 249
if _libs["/usr/local/lib/libiec61850.so"].has("IedServerConfig_isFileServiceEnabled", "cdecl"):
    IedServerConfig_isFileServiceEnabled = _libs["/usr/local/lib/libiec61850.so"].get("IedServerConfig_isFileServiceEnabled", "cdecl")
    IedServerConfig_isFileServiceEnabled.argtypes = [IedServerConfig]
    IedServerConfig_isFileServiceEnabled.restype = c_bool

# /usr/local/include/libiec61850/iec61850_server.h: 257
if _libs["/usr/local/lib/libiec61850.so"].has("IedServerConfig_enableDynamicDataSetService", "cdecl"):
    IedServerConfig_enableDynamicDataSetService = _libs["/usr/local/lib/libiec61850.so"].get("IedServerConfig_enableDynamicDataSetService", "cdecl")
    IedServerConfig_enableDynamicDataSetService.argtypes = [IedServerConfig, c_bool]
    IedServerConfig_enableDynamicDataSetService.restype = None

# /usr/local/include/libiec61850/iec61850_server.h: 265
if _libs["/usr/local/lib/libiec61850.so"].has("IedServerConfig_isDynamicDataSetServiceEnabled", "cdecl"):
    IedServerConfig_isDynamicDataSetServiceEnabled = _libs["/usr/local/lib/libiec61850.so"].get("IedServerConfig_isDynamicDataSetServiceEnabled", "cdecl")
    IedServerConfig_isDynamicDataSetServiceEnabled.argtypes = [IedServerConfig]
    IedServerConfig_isDynamicDataSetServiceEnabled.restype = c_bool

# /usr/local/include/libiec61850/iec61850_server.h: 276
if _libs["/usr/local/lib/libiec61850.so"].has("IedServerConfig_setMaxAssociationSpecificDataSets", "cdecl"):
    IedServerConfig_setMaxAssociationSpecificDataSets = _libs["/usr/local/lib/libiec61850.so"].get("IedServerConfig_setMaxAssociationSpecificDataSets", "cdecl")
    IedServerConfig_setMaxAssociationSpecificDataSets.argtypes = [IedServerConfig, c_int]
    IedServerConfig_setMaxAssociationSpecificDataSets.restype = None

# /usr/local/include/libiec61850/iec61850_server.h: 284
if _libs["/usr/local/lib/libiec61850.so"].has("IedServerConfig_getMaxAssociationSpecificDataSets", "cdecl"):
    IedServerConfig_getMaxAssociationSpecificDataSets = _libs["/usr/local/lib/libiec61850.so"].get("IedServerConfig_getMaxAssociationSpecificDataSets", "cdecl")
    IedServerConfig_getMaxAssociationSpecificDataSets.argtypes = [IedServerConfig]
    IedServerConfig_getMaxAssociationSpecificDataSets.restype = c_int

# /usr/local/include/libiec61850/iec61850_server.h: 292
if _libs["/usr/local/lib/libiec61850.so"].has("IedServerConfig_setMaxDomainSpecificDataSets", "cdecl"):
    IedServerConfig_setMaxDomainSpecificDataSets = _libs["/usr/local/lib/libiec61850.so"].get("IedServerConfig_setMaxDomainSpecificDataSets", "cdecl")
    IedServerConfig_setMaxDomainSpecificDataSets.argtypes = [IedServerConfig, c_int]
    IedServerConfig_setMaxDomainSpecificDataSets.restype = None

# /usr/local/include/libiec61850/iec61850_server.h: 300
if _libs["/usr/local/lib/libiec61850.so"].has("IedServerConfig_getMaxDomainSpecificDataSets", "cdecl"):
    IedServerConfig_getMaxDomainSpecificDataSets = _libs["/usr/local/lib/libiec61850.so"].get("IedServerConfig_getMaxDomainSpecificDataSets", "cdecl")
    IedServerConfig_getMaxDomainSpecificDataSets.argtypes = [IedServerConfig]
    IedServerConfig_getMaxDomainSpecificDataSets.restype = c_int

# /usr/local/include/libiec61850/iec61850_server.h: 312
if _libs["/usr/local/lib/libiec61850.so"].has("IedServerConfig_setMaxDataSetEntries", "cdecl"):
    IedServerConfig_setMaxDataSetEntries = _libs["/usr/local/lib/libiec61850.so"].get("IedServerConfig_setMaxDataSetEntries", "cdecl")
    IedServerConfig_setMaxDataSetEntries.argtypes = [IedServerConfig, c_int]
    IedServerConfig_setMaxDataSetEntries.restype = None

# /usr/local/include/libiec61850/iec61850_server.h: 320
if _libs["/usr/local/lib/libiec61850.so"].has("IedServerConfig_getMaxDatasSetEntries", "cdecl"):
    IedServerConfig_getMaxDatasSetEntries = _libs["/usr/local/lib/libiec61850.so"].get("IedServerConfig_getMaxDatasSetEntries", "cdecl")
    IedServerConfig_getMaxDatasSetEntries.argtypes = [IedServerConfig]
    IedServerConfig_getMaxDatasSetEntries.restype = c_int

# /usr/local/include/libiec61850/iec61850_server.h: 328
if _libs["/usr/local/lib/libiec61850.so"].has("IedServerConfig_enableLogService", "cdecl"):
    IedServerConfig_enableLogService = _libs["/usr/local/lib/libiec61850.so"].get("IedServerConfig_enableLogService", "cdecl")
    IedServerConfig_enableLogService.argtypes = [IedServerConfig, c_bool]
    IedServerConfig_enableLogService.restype = None

# /usr/local/include/libiec61850/iec61850_server.h: 339
if _libs["/usr/local/lib/libiec61850.so"].has("IedServerConfig_enableEditSG", "cdecl"):
    IedServerConfig_enableEditSG = _libs["/usr/local/lib/libiec61850.so"].get("IedServerConfig_enableEditSG", "cdecl")
    IedServerConfig_enableEditSG.argtypes = [IedServerConfig, c_bool]
    IedServerConfig_enableEditSG.restype = None

# /usr/local/include/libiec61850/iec61850_server.h: 349
if _libs["/usr/local/lib/libiec61850.so"].has("IedServerConfig_enableResvTmsForSGCB", "cdecl"):
    IedServerConfig_enableResvTmsForSGCB = _libs["/usr/local/lib/libiec61850.so"].get("IedServerConfig_enableResvTmsForSGCB", "cdecl")
    IedServerConfig_enableResvTmsForSGCB.argtypes = [IedServerConfig, c_bool]
    IedServerConfig_enableResvTmsForSGCB.restype = None

# /usr/local/include/libiec61850/iec61850_server.h: 357
if _libs["/usr/local/lib/libiec61850.so"].has("IedServerConfig_enableResvTmsForBRCB", "cdecl"):
    IedServerConfig_enableResvTmsForBRCB = _libs["/usr/local/lib/libiec61850.so"].get("IedServerConfig_enableResvTmsForBRCB", "cdecl")
    IedServerConfig_enableResvTmsForBRCB.argtypes = [IedServerConfig, c_bool]
    IedServerConfig_enableResvTmsForBRCB.restype = None

# /usr/local/include/libiec61850/iec61850_server.h: 365
if _libs["/usr/local/lib/libiec61850.so"].has("IedServerConfig_isResvTmsForBRCBEnabled", "cdecl"):
    IedServerConfig_isResvTmsForBRCBEnabled = _libs["/usr/local/lib/libiec61850.so"].get("IedServerConfig_isResvTmsForBRCBEnabled", "cdecl")
    IedServerConfig_isResvTmsForBRCBEnabled.argtypes = [IedServerConfig]
    IedServerConfig_isResvTmsForBRCBEnabled.restype = c_bool

# /usr/local/include/libiec61850/iec61850_server.h: 373
if _libs["/usr/local/lib/libiec61850.so"].has("IedServerConfig_enableOwnerForRCB", "cdecl"):
    IedServerConfig_enableOwnerForRCB = _libs["/usr/local/lib/libiec61850.so"].get("IedServerConfig_enableOwnerForRCB", "cdecl")
    IedServerConfig_enableOwnerForRCB.argtypes = [IedServerConfig, c_bool]
    IedServerConfig_enableOwnerForRCB.restype = None

# /usr/local/include/libiec61850/iec61850_server.h: 381
if _libs["/usr/local/lib/libiec61850.so"].has("IedServerConfig_isOwnerForRCBEnabled", "cdecl"):
    IedServerConfig_isOwnerForRCBEnabled = _libs["/usr/local/lib/libiec61850.so"].get("IedServerConfig_isOwnerForRCBEnabled", "cdecl")
    IedServerConfig_isOwnerForRCBEnabled.argtypes = [IedServerConfig]
    IedServerConfig_isOwnerForRCBEnabled.restype = c_bool

# /usr/local/include/libiec61850/iec61850_server.h: 391
if _libs["/usr/local/lib/libiec61850.so"].has("IedServerConfig_useIntegratedGoosePublisher", "cdecl"):
    IedServerConfig_useIntegratedGoosePublisher = _libs["/usr/local/lib/libiec61850.so"].get("IedServerConfig_useIntegratedGoosePublisher", "cdecl")
    IedServerConfig_useIntegratedGoosePublisher.argtypes = [IedServerConfig, c_bool]
    IedServerConfig_useIntegratedGoosePublisher.restype = None

# /usr/local/include/libiec61850/iec61850_server.h: 399
if _libs["/usr/local/lib/libiec61850.so"].has("IedServerConfig_isLogServiceEnabled", "cdecl"):
    IedServerConfig_isLogServiceEnabled = _libs["/usr/local/lib/libiec61850.so"].get("IedServerConfig_isLogServiceEnabled", "cdecl")
    IedServerConfig_isLogServiceEnabled.argtypes = [IedServerConfig]
    IedServerConfig_isLogServiceEnabled.restype = c_bool

# /usr/local/include/libiec61850/iec61850_server.h: 410
if _libs["/usr/local/lib/libiec61850.so"].has("IedServerConfig_setReportSetting", "cdecl"):
    IedServerConfig_setReportSetting = _libs["/usr/local/lib/libiec61850.so"].get("IedServerConfig_setReportSetting", "cdecl")
    IedServerConfig_setReportSetting.argtypes = [IedServerConfig, uint8_t, c_bool]
    IedServerConfig_setReportSetting.restype = None

# /usr/local/include/libiec61850/iec61850_server.h: 420
if _libs["/usr/local/lib/libiec61850.so"].has("IedServerConfig_getReportSetting", "cdecl"):
    IedServerConfig_getReportSetting = _libs["/usr/local/lib/libiec61850.so"].get("IedServerConfig_getReportSetting", "cdecl")
    IedServerConfig_getReportSetting.argtypes = [IedServerConfig, uint8_t]
    IedServerConfig_getReportSetting.restype = c_bool

# /usr/local/include/libiec61850/iec61850_server.h: 425
class struct_sIedServer(Structure):
    pass

IedServer = POINTER(struct_sIedServer)# /usr/local/include/libiec61850/iec61850_server.h: 425

# /usr/local/include/libiec61850/iec61850_server.h: 430
class struct_sClientConnection(Structure):
    pass

ClientConnection = POINTER(struct_sClientConnection)# /usr/local/include/libiec61850/iec61850_server.h: 430

# /usr/local/include/libiec61850/iec61850_server.h: 447
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_create", "cdecl"):
    IedServer_create = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_create", "cdecl")
    IedServer_create.argtypes = [POINTER(IedModel)]
    IedServer_create.restype = IedServer

# /usr/local/include/libiec61850/iec61850_server.h: 458
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_createWithTlsSupport", "cdecl"):
    IedServer_createWithTlsSupport = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_createWithTlsSupport", "cdecl")
    IedServer_createWithTlsSupport.argtypes = [POINTER(IedModel), TLSConfiguration]
    IedServer_createWithTlsSupport.restype = IedServer

# /usr/local/include/libiec61850/iec61850_server.h: 468
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_createWithConfig", "cdecl"):
    IedServer_createWithConfig = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_createWithConfig", "cdecl")
    IedServer_createWithConfig.argtypes = [POINTER(IedModel), TLSConfiguration, IedServerConfig]
    IedServer_createWithConfig.restype = IedServer

# /usr/local/include/libiec61850/iec61850_server.h: 476
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_destroy", "cdecl"):
    IedServer_destroy = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_destroy", "cdecl")
    IedServer_destroy.argtypes = [IedServer]
    IedServer_destroy.restype = None

# /usr/local/include/libiec61850/iec61850_server.h: 489
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_addAccessPoint", "cdecl"):
    IedServer_addAccessPoint = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_addAccessPoint", "cdecl")
    IedServer_addAccessPoint.argtypes = [IedServer, String, c_int, TLSConfiguration]
    IedServer_addAccessPoint.restype = c_bool

# /usr/local/include/libiec61850/iec61850_server.h: 498
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_setLocalIpAddress", "cdecl"):
    IedServer_setLocalIpAddress = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_setLocalIpAddress", "cdecl")
    IedServer_setLocalIpAddress.argtypes = [IedServer, String]
    IedServer_setLocalIpAddress.restype = None

# /usr/local/include/libiec61850/iec61850_server.h: 511
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_setServerIdentity", "cdecl"):
    IedServer_setServerIdentity = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_setServerIdentity", "cdecl")
    IedServer_setServerIdentity.argtypes = [IedServer, String, String, String]
    IedServer_setServerIdentity.restype = None

# /usr/local/include/libiec61850/iec61850_server.h: 524
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_setFilestoreBasepath", "cdecl"):
    IedServer_setFilestoreBasepath = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_setFilestoreBasepath", "cdecl")
    IedServer_setFilestoreBasepath.argtypes = [IedServer, String]
    IedServer_setFilestoreBasepath.restype = None

# /usr/local/include/libiec61850/iec61850_server.h: 533
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_start", "cdecl"):
    IedServer_start = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_start", "cdecl")
    IedServer_start.argtypes = [IedServer, c_int]
    IedServer_start.restype = None

# /usr/local/include/libiec61850/iec61850_server.h: 541
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_stop", "cdecl"):
    IedServer_stop = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_stop", "cdecl")
    IedServer_stop.argtypes = [IedServer]
    IedServer_stop.restype = None

# /usr/local/include/libiec61850/iec61850_server.h: 554
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_startThreadless", "cdecl"):
    IedServer_startThreadless = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_startThreadless", "cdecl")
    IedServer_startThreadless.argtypes = [IedServer, c_int]
    IedServer_startThreadless.restype = None

# /usr/local/include/libiec61850/iec61850_server.h: 570
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_waitReady", "cdecl"):
    IedServer_waitReady = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_waitReady", "cdecl")
    IedServer_waitReady.argtypes = [IedServer, c_uint]
    IedServer_waitReady.restype = c_int

# /usr/local/include/libiec61850/iec61850_server.h: 582
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_processIncomingData", "cdecl"):
    IedServer_processIncomingData = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_processIncomingData", "cdecl")
    IedServer_processIncomingData.argtypes = [IedServer]
    IedServer_processIncomingData.restype = None

# /usr/local/include/libiec61850/iec61850_server.h: 593
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_performPeriodicTasks", "cdecl"):
    IedServer_performPeriodicTasks = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_performPeriodicTasks", "cdecl")
    IedServer_performPeriodicTasks.argtypes = [IedServer]
    IedServer_performPeriodicTasks.restype = None

# /usr/local/include/libiec61850/iec61850_server.h: 601
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_stopThreadless", "cdecl"):
    IedServer_stopThreadless = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_stopThreadless", "cdecl")
    IedServer_stopThreadless.argtypes = [IedServer]
    IedServer_stopThreadless.restype = None

# /usr/local/include/libiec61850/iec61850_server.h: 610
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_getDataModel", "cdecl"):
    IedServer_getDataModel = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_getDataModel", "cdecl")
    IedServer_getDataModel.argtypes = [IedServer]
    IedServer_getDataModel.restype = POINTER(IedModel)

# /usr/local/include/libiec61850/iec61850_server.h: 621
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_isRunning", "cdecl"):
    IedServer_isRunning = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_isRunning", "cdecl")
    IedServer_isRunning.argtypes = [IedServer]
    IedServer_isRunning.restype = c_bool

# /usr/local/include/libiec61850/iec61850_server.h: 631
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_getNumberOfOpenConnections", "cdecl"):
    IedServer_getNumberOfOpenConnections = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_getNumberOfOpenConnections", "cdecl")
    IedServer_getNumberOfOpenConnections.argtypes = [IedServer]
    IedServer_getNumberOfOpenConnections.restype = c_int

# /usr/local/include/libiec61850/iec61850_server.h: 644
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_getMmsServer", "cdecl"):
    IedServer_getMmsServer = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_getMmsServer", "cdecl")
    IedServer_getMmsServer.argtypes = [IedServer]
    IedServer_getMmsServer.restype = MmsServer

# /usr/local/include/libiec61850/iec61850_server.h: 659
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_enableGoosePublishing", "cdecl"):
    IedServer_enableGoosePublishing = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_enableGoosePublishing", "cdecl")
    IedServer_enableGoosePublishing.argtypes = [IedServer]
    IedServer_enableGoosePublishing.restype = None

# /usr/local/include/libiec61850/iec61850_server.h: 672
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_disableGoosePublishing", "cdecl"):
    IedServer_disableGoosePublishing = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_disableGoosePublishing", "cdecl")
    IedServer_disableGoosePublishing.argtypes = [IedServer]
    IedServer_disableGoosePublishing.restype = None

# /usr/local/include/libiec61850/iec61850_server.h: 687
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_setGooseInterfaceId", "cdecl"):
    IedServer_setGooseInterfaceId = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_setGooseInterfaceId", "cdecl")
    IedServer_setGooseInterfaceId.argtypes = [IedServer, String]
    IedServer_setGooseInterfaceId.restype = None

# /usr/local/include/libiec61850/iec61850_server.h: 703
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_setGooseInterfaceIdEx", "cdecl"):
    IedServer_setGooseInterfaceIdEx = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_setGooseInterfaceIdEx", "cdecl")
    IedServer_setGooseInterfaceIdEx.argtypes = [IedServer, POINTER(LogicalNode), String, String]
    IedServer_setGooseInterfaceIdEx.restype = None

# /usr/local/include/libiec61850/iec61850_server.h: 719
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_useGooseVlanTag", "cdecl"):
    IedServer_useGooseVlanTag = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_useGooseVlanTag", "cdecl")
    IedServer_useGooseVlanTag.argtypes = [IedServer, POINTER(LogicalNode), String, c_bool]
    IedServer_useGooseVlanTag.restype = None

# /usr/local/include/libiec61850/iec61850_server.h: 734
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_setTimeQuality", "cdecl"):
    IedServer_setTimeQuality = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_setTimeQuality", "cdecl")
    IedServer_setTimeQuality.argtypes = [IedServer, c_bool, c_bool, c_bool, c_int]
    IedServer_setTimeQuality.restype = None

# /usr/local/include/libiec61850/iec61850_server.h: 757
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_setAuthenticator", "cdecl"):
    IedServer_setAuthenticator = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_setAuthenticator", "cdecl")
    IedServer_setAuthenticator.argtypes = [IedServer, AcseAuthenticator, POINTER(None)]
    IedServer_setAuthenticator.restype = None

# /usr/local/include/libiec61850/iec61850_server.h: 768
if _libs["/usr/local/lib/libiec61850.so"].has("ClientConnection_getPeerAddress", "cdecl"):
    ClientConnection_getPeerAddress = _libs["/usr/local/lib/libiec61850.so"].get("ClientConnection_getPeerAddress", "cdecl")
    ClientConnection_getPeerAddress.argtypes = [ClientConnection]
    ClientConnection_getPeerAddress.restype = c_char_p

# /usr/local/include/libiec61850/iec61850_server.h: 780
if _libs["/usr/local/lib/libiec61850.so"].has("ClientConnection_getLocalAddress", "cdecl"):
    ClientConnection_getLocalAddress = _libs["/usr/local/lib/libiec61850.so"].get("ClientConnection_getLocalAddress", "cdecl")
    ClientConnection_getLocalAddress.argtypes = [ClientConnection]
    ClientConnection_getLocalAddress.restype = c_char_p

# /usr/local/include/libiec61850/iec61850_server.h: 793
if _libs["/usr/local/lib/libiec61850.so"].has("ClientConnection_getSecurityToken", "cdecl"):
    ClientConnection_getSecurityToken = _libs["/usr/local/lib/libiec61850.so"].get("ClientConnection_getSecurityToken", "cdecl")
    ClientConnection_getSecurityToken.argtypes = [ClientConnection]
    ClientConnection_getSecurityToken.restype = POINTER(c_ubyte)
    ClientConnection_getSecurityToken.errcheck = lambda v,*a : cast(v, c_void_p)

IedConnectionIndicationHandler = CFUNCTYPE(UNCHECKED(None), IedServer, ClientConnection, c_bool, POINTER(None))# /usr/local/include/libiec61850/iec61850_server.h: 805

# /usr/local/include/libiec61850/iec61850_server.h: 815
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_setConnectionIndicationHandler", "cdecl"):
    IedServer_setConnectionIndicationHandler = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_setConnectionIndicationHandler", "cdecl")
    IedServer_setConnectionIndicationHandler.argtypes = [IedServer, IedConnectionIndicationHandler, POINTER(None)]
    IedServer_setConnectionIndicationHandler.restype = None

# /usr/local/include/libiec61850/iec61850_server.h: 841
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_lockDataModel", "cdecl"):
    IedServer_lockDataModel = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_lockDataModel", "cdecl")
    IedServer_lockDataModel.argtypes = [IedServer]
    IedServer_lockDataModel.restype = None

# /usr/local/include/libiec61850/iec61850_server.h: 852
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_unlockDataModel", "cdecl"):
    IedServer_unlockDataModel = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_unlockDataModel", "cdecl")
    IedServer_unlockDataModel.argtypes = [IedServer]
    IedServer_unlockDataModel.restype = None

# /usr/local/include/libiec61850/iec61850_server.h: 866
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_getAttributeValue", "cdecl"):
    IedServer_getAttributeValue = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_getAttributeValue", "cdecl")
    IedServer_getAttributeValue.argtypes = [IedServer, POINTER(DataAttribute)]
    IedServer_getAttributeValue.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/iec61850_server.h: 881
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_getBooleanAttributeValue", "cdecl"):
    IedServer_getBooleanAttributeValue = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_getBooleanAttributeValue", "cdecl")
    IedServer_getBooleanAttributeValue.argtypes = [IedServer, POINTER(DataAttribute)]
    IedServer_getBooleanAttributeValue.restype = c_bool

# /usr/local/include/libiec61850/iec61850_server.h: 895
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_getInt32AttributeValue", "cdecl"):
    IedServer_getInt32AttributeValue = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_getInt32AttributeValue", "cdecl")
    IedServer_getInt32AttributeValue.argtypes = [IedServer, POINTER(DataAttribute)]
    IedServer_getInt32AttributeValue.restype = c_int32

# /usr/local/include/libiec61850/iec61850_server.h: 909
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_getInt64AttributeValue", "cdecl"):
    IedServer_getInt64AttributeValue = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_getInt64AttributeValue", "cdecl")
    IedServer_getInt64AttributeValue.argtypes = [IedServer, POINTER(DataAttribute)]
    IedServer_getInt64AttributeValue.restype = c_int64

# /usr/local/include/libiec61850/iec61850_server.h: 923
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_getUInt32AttributeValue", "cdecl"):
    IedServer_getUInt32AttributeValue = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_getUInt32AttributeValue", "cdecl")
    IedServer_getUInt32AttributeValue.argtypes = [IedServer, POINTER(DataAttribute)]
    IedServer_getUInt32AttributeValue.restype = uint32_t

# /usr/local/include/libiec61850/iec61850_server.h: 937
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_getFloatAttributeValue", "cdecl"):
    IedServer_getFloatAttributeValue = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_getFloatAttributeValue", "cdecl")
    IedServer_getFloatAttributeValue.argtypes = [IedServer, POINTER(DataAttribute)]
    IedServer_getFloatAttributeValue.restype = c_float

# /usr/local/include/libiec61850/iec61850_server.h: 951
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_getUTCTimeAttributeValue", "cdecl"):
    IedServer_getUTCTimeAttributeValue = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_getUTCTimeAttributeValue", "cdecl")
    IedServer_getUTCTimeAttributeValue.argtypes = [IedServer, POINTER(DataAttribute)]
    IedServer_getUTCTimeAttributeValue.restype = uint64_t

# /usr/local/include/libiec61850/iec61850_server.h: 969
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_getBitStringAttributeValue", "cdecl"):
    IedServer_getBitStringAttributeValue = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_getBitStringAttributeValue", "cdecl")
    IedServer_getBitStringAttributeValue.argtypes = [IedServer, POINTER(DataAttribute)]
    IedServer_getBitStringAttributeValue.restype = uint32_t

# /usr/local/include/libiec61850/iec61850_server.h: 982
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_getStringAttributeValue", "cdecl"):
    IedServer_getStringAttributeValue = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_getStringAttributeValue", "cdecl")
    IedServer_getStringAttributeValue.argtypes = [IedServer, POINTER(DataAttribute)]
    IedServer_getStringAttributeValue.restype = c_char_p

# /usr/local/include/libiec61850/iec61850_server.h: 1000
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_getFunctionalConstrainedData", "cdecl"):
    IedServer_getFunctionalConstrainedData = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_getFunctionalConstrainedData", "cdecl")
    IedServer_getFunctionalConstrainedData.argtypes = [IedServer, POINTER(DataObject), FunctionalConstraint]
    IedServer_getFunctionalConstrainedData.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/iec61850_server.h: 1020
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_updateAttributeValue", "cdecl"):
    IedServer_updateAttributeValue = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_updateAttributeValue", "cdecl")
    IedServer_updateAttributeValue.argtypes = [IedServer, POINTER(DataAttribute), POINTER(MmsValue)]
    IedServer_updateAttributeValue.restype = None

# /usr/local/include/libiec61850/iec61850_server.h: 1035
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_updateFloatAttributeValue", "cdecl"):
    IedServer_updateFloatAttributeValue = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_updateFloatAttributeValue", "cdecl")
    IedServer_updateFloatAttributeValue.argtypes = [IedServer, POINTER(DataAttribute), c_float]
    IedServer_updateFloatAttributeValue.restype = None

# /usr/local/include/libiec61850/iec61850_server.h: 1050
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_updateInt32AttributeValue", "cdecl"):
    IedServer_updateInt32AttributeValue = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_updateInt32AttributeValue", "cdecl")
    IedServer_updateInt32AttributeValue.argtypes = [IedServer, POINTER(DataAttribute), c_int32]
    IedServer_updateInt32AttributeValue.restype = None

# /usr/local/include/libiec61850/iec61850_server.h: 1065
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_updateDbposValue", "cdecl"):
    IedServer_updateDbposValue = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_updateDbposValue", "cdecl")
    IedServer_updateDbposValue.argtypes = [IedServer, POINTER(DataAttribute), Dbpos]
    IedServer_updateDbposValue.restype = None

# /usr/local/include/libiec61850/iec61850_server.h: 1080
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_updateInt64AttributeValue", "cdecl"):
    IedServer_updateInt64AttributeValue = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_updateInt64AttributeValue", "cdecl")
    IedServer_updateInt64AttributeValue.argtypes = [IedServer, POINTER(DataAttribute), c_int64]
    IedServer_updateInt64AttributeValue.restype = None

# /usr/local/include/libiec61850/iec61850_server.h: 1095
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_updateUnsignedAttributeValue", "cdecl"):
    IedServer_updateUnsignedAttributeValue = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_updateUnsignedAttributeValue", "cdecl")
    IedServer_updateUnsignedAttributeValue.argtypes = [IedServer, POINTER(DataAttribute), uint32_t]
    IedServer_updateUnsignedAttributeValue.restype = None

# /usr/local/include/libiec61850/iec61850_server.h: 1110
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_updateBitStringAttributeValue", "cdecl"):
    IedServer_updateBitStringAttributeValue = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_updateBitStringAttributeValue", "cdecl")
    IedServer_updateBitStringAttributeValue.argtypes = [IedServer, POINTER(DataAttribute), uint32_t]
    IedServer_updateBitStringAttributeValue.restype = None

# /usr/local/include/libiec61850/iec61850_server.h: 1125
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_updateBooleanAttributeValue", "cdecl"):
    IedServer_updateBooleanAttributeValue = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_updateBooleanAttributeValue", "cdecl")
    IedServer_updateBooleanAttributeValue.argtypes = [IedServer, POINTER(DataAttribute), c_bool]
    IedServer_updateBooleanAttributeValue.restype = None

# /usr/local/include/libiec61850/iec61850_server.h: 1140
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_updateVisibleStringAttributeValue", "cdecl"):
    IedServer_updateVisibleStringAttributeValue = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_updateVisibleStringAttributeValue", "cdecl")
    IedServer_updateVisibleStringAttributeValue.argtypes = [IedServer, POINTER(DataAttribute), String]
    IedServer_updateVisibleStringAttributeValue.restype = None

# /usr/local/include/libiec61850/iec61850_server.h: 1155
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_updateUTCTimeAttributeValue", "cdecl"):
    IedServer_updateUTCTimeAttributeValue = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_updateUTCTimeAttributeValue", "cdecl")
    IedServer_updateUTCTimeAttributeValue.argtypes = [IedServer, POINTER(DataAttribute), uint64_t]
    IedServer_updateUTCTimeAttributeValue.restype = None

# /usr/local/include/libiec61850/iec61850_server.h: 1170
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_updateTimestampAttributeValue", "cdecl"):
    IedServer_updateTimestampAttributeValue = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_updateTimestampAttributeValue", "cdecl")
    IedServer_updateTimestampAttributeValue.argtypes = [IedServer, POINTER(DataAttribute), POINTER(Timestamp)]
    IedServer_updateTimestampAttributeValue.restype = None

# /usr/local/include/libiec61850/iec61850_server.h: 1187
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_updateQuality", "cdecl"):
    IedServer_updateQuality = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_updateQuality", "cdecl")
    IedServer_updateQuality.argtypes = [IedServer, POINTER(DataAttribute), Quality]
    IedServer_updateQuality.restype = None

# /usr/local/include/libiec61850/iec61850_server.h: 1193
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_setLogStorage", "cdecl"):
    IedServer_setLogStorage = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_setLogStorage", "cdecl")
    IedServer_setLogStorage.argtypes = [IedServer, String, LogStorage]
    IedServer_setLogStorage.restype = None

# /usr/local/include/libiec61850/iec61850_server.h: 1212
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_changeActiveSettingGroup", "cdecl"):
    IedServer_changeActiveSettingGroup = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_changeActiveSettingGroup", "cdecl")
    IedServer_changeActiveSettingGroup.argtypes = [IedServer, POINTER(SettingGroupControlBlock), uint8_t]
    IedServer_changeActiveSettingGroup.restype = None

# /usr/local/include/libiec61850/iec61850_server.h: 1223
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_getActiveSettingGroup", "cdecl"):
    IedServer_getActiveSettingGroup = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_getActiveSettingGroup", "cdecl")
    IedServer_getActiveSettingGroup.argtypes = [IedServer, POINTER(SettingGroupControlBlock)]
    IedServer_getActiveSettingGroup.restype = uint8_t

ActiveSettingGroupChangedHandler = CFUNCTYPE(UNCHECKED(c_bool), POINTER(None), POINTER(SettingGroupControlBlock), uint8_t, ClientConnection)# /usr/local/include/libiec61850/iec61850_server.h: 1240

# /usr/local/include/libiec61850/iec61850_server.h: 1252
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_setActiveSettingGroupChangedHandler", "cdecl"):
    IedServer_setActiveSettingGroupChangedHandler = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_setActiveSettingGroupChangedHandler", "cdecl")
    IedServer_setActiveSettingGroupChangedHandler.argtypes = [IedServer, POINTER(SettingGroupControlBlock), ActiveSettingGroupChangedHandler, POINTER(None)]
    IedServer_setActiveSettingGroupChangedHandler.restype = None

EditSettingGroupChangedHandler = CFUNCTYPE(UNCHECKED(c_bool), POINTER(None), POINTER(SettingGroupControlBlock), uint8_t, ClientConnection)# /usr/local/include/libiec61850/iec61850_server.h: 1272

# /usr/local/include/libiec61850/iec61850_server.h: 1284
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_setEditSettingGroupChangedHandler", "cdecl"):
    IedServer_setEditSettingGroupChangedHandler = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_setEditSettingGroupChangedHandler", "cdecl")
    IedServer_setEditSettingGroupChangedHandler.argtypes = [IedServer, POINTER(SettingGroupControlBlock), EditSettingGroupChangedHandler, POINTER(None)]
    IedServer_setEditSettingGroupChangedHandler.restype = None

EditSettingGroupConfirmationHandler = CFUNCTYPE(UNCHECKED(None), POINTER(None), POINTER(SettingGroupControlBlock), uint8_t)# /usr/local/include/libiec61850/iec61850_server.h: 1296

# /usr/local/include/libiec61850/iec61850_server.h: 1308
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_setEditSettingGroupConfirmationHandler", "cdecl"):
    IedServer_setEditSettingGroupConfirmationHandler = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_setEditSettingGroupConfirmationHandler", "cdecl")
    IedServer_setEditSettingGroupConfirmationHandler.argtypes = [IedServer, POINTER(SettingGroupControlBlock), EditSettingGroupConfirmationHandler, POINTER(None)]
    IedServer_setEditSettingGroupConfirmationHandler.restype = None

enum_anon_54 = c_int# /usr/local/include/libiec61850/iec61850_server.h: 1330

CONTROL_ACCEPTED = (-1)# /usr/local/include/libiec61850/iec61850_server.h: 1330

CONTROL_WAITING_FOR_SELECT = 0# /usr/local/include/libiec61850/iec61850_server.h: 1330

CONTROL_HARDWARE_FAULT = 1# /usr/local/include/libiec61850/iec61850_server.h: 1330

CONTROL_TEMPORARILY_UNAVAILABLE = 2# /usr/local/include/libiec61850/iec61850_server.h: 1330

CONTROL_OBJECT_ACCESS_DENIED = 3# /usr/local/include/libiec61850/iec61850_server.h: 1330

CONTROL_OBJECT_UNDEFINED = 4# /usr/local/include/libiec61850/iec61850_server.h: 1330

CONTROL_VALUE_INVALID = 11# /usr/local/include/libiec61850/iec61850_server.h: 1330

CheckHandlerResult = enum_anon_54# /usr/local/include/libiec61850/iec61850_server.h: 1330

enum_anon_55 = c_int# /usr/local/include/libiec61850/iec61850_server.h: 1339

CONTROL_RESULT_FAILED = 0# /usr/local/include/libiec61850/iec61850_server.h: 1339

CONTROL_RESULT_OK = 1# /usr/local/include/libiec61850/iec61850_server.h: 1339

CONTROL_RESULT_WAITING = 2# /usr/local/include/libiec61850/iec61850_server.h: 1339

ControlHandlerResult = enum_anon_55# /usr/local/include/libiec61850/iec61850_server.h: 1339

ControlAction = POINTER(None)# /usr/local/include/libiec61850/iec61850_server.h: 1341

# /usr/local/include/libiec61850/iec61850_server.h: 1350
if _libs["/usr/local/lib/libiec61850.so"].has("ControlAction_setError", "cdecl"):
    ControlAction_setError = _libs["/usr/local/lib/libiec61850.so"].get("ControlAction_setError", "cdecl")
    ControlAction_setError.argtypes = [ControlAction, ControlLastApplError]
    ControlAction_setError.restype = None

# /usr/local/include/libiec61850/iec61850_server.h: 1359
if _libs["/usr/local/lib/libiec61850.so"].has("ControlAction_setAddCause", "cdecl"):
    ControlAction_setAddCause = _libs["/usr/local/lib/libiec61850.so"].get("ControlAction_setAddCause", "cdecl")
    ControlAction_setAddCause.argtypes = [ControlAction, ControlAddCause]
    ControlAction_setAddCause.restype = None

# /usr/local/include/libiec61850/iec61850_server.h: 1369
if _libs["/usr/local/lib/libiec61850.so"].has("ControlAction_getOrCat", "cdecl"):
    ControlAction_getOrCat = _libs["/usr/local/lib/libiec61850.so"].get("ControlAction_getOrCat", "cdecl")
    ControlAction_getOrCat.argtypes = [ControlAction]
    ControlAction_getOrCat.restype = c_int

# /usr/local/include/libiec61850/iec61850_server.h: 1378
if _libs["/usr/local/lib/libiec61850.so"].has("ControlAction_getOrIdent", "cdecl"):
    ControlAction_getOrIdent = _libs["/usr/local/lib/libiec61850.so"].get("ControlAction_getOrIdent", "cdecl")
    ControlAction_getOrIdent.argtypes = [ControlAction, POINTER(c_int)]
    ControlAction_getOrIdent.restype = POINTER(uint8_t)

# /usr/local/include/libiec61850/iec61850_server.h: 1389
if _libs["/usr/local/lib/libiec61850.so"].has("ControlAction_getCtlNum", "cdecl"):
    ControlAction_getCtlNum = _libs["/usr/local/lib/libiec61850.so"].get("ControlAction_getCtlNum", "cdecl")
    ControlAction_getCtlNum.argtypes = [ControlAction]
    ControlAction_getCtlNum.restype = c_int

# /usr/local/include/libiec61850/iec61850_server.h: 1399
if _libs["/usr/local/lib/libiec61850.so"].has("ControlAction_getSynchroCheck", "cdecl"):
    ControlAction_getSynchroCheck = _libs["/usr/local/lib/libiec61850.so"].get("ControlAction_getSynchroCheck", "cdecl")
    ControlAction_getSynchroCheck.argtypes = [ControlAction]
    ControlAction_getSynchroCheck.restype = c_bool

# /usr/local/include/libiec61850/iec61850_server.h: 1409
if _libs["/usr/local/lib/libiec61850.so"].has("ControlAction_getInterlockCheck", "cdecl"):
    ControlAction_getInterlockCheck = _libs["/usr/local/lib/libiec61850.so"].get("ControlAction_getInterlockCheck", "cdecl")
    ControlAction_getInterlockCheck.argtypes = [ControlAction]
    ControlAction_getInterlockCheck.restype = c_bool

# /usr/local/include/libiec61850/iec61850_server.h: 1419
if _libs["/usr/local/lib/libiec61850.so"].has("ControlAction_isSelect", "cdecl"):
    ControlAction_isSelect = _libs["/usr/local/lib/libiec61850.so"].get("ControlAction_isSelect", "cdecl")
    ControlAction_isSelect.argtypes = [ControlAction]
    ControlAction_isSelect.restype = c_bool

# /usr/local/include/libiec61850/iec61850_server.h: 1429
if _libs["/usr/local/lib/libiec61850.so"].has("ControlAction_getClientConnection", "cdecl"):
    ControlAction_getClientConnection = _libs["/usr/local/lib/libiec61850.so"].get("ControlAction_getClientConnection", "cdecl")
    ControlAction_getClientConnection.argtypes = [ControlAction]
    ControlAction_getClientConnection.restype = ClientConnection

# /usr/local/include/libiec61850/iec61850_server.h: 1438
if _libs["/usr/local/lib/libiec61850.so"].has("ControlAction_getControlObject", "cdecl"):
    ControlAction_getControlObject = _libs["/usr/local/lib/libiec61850.so"].get("ControlAction_getControlObject", "cdecl")
    ControlAction_getControlObject.argtypes = [ControlAction]
    ControlAction_getControlObject.restype = POINTER(DataObject)

# /usr/local/include/libiec61850/iec61850_server.h: 1449
if _libs["/usr/local/lib/libiec61850.so"].has("ControlAction_getControlTime", "cdecl"):
    ControlAction_getControlTime = _libs["/usr/local/lib/libiec61850.so"].get("ControlAction_getControlTime", "cdecl")
    ControlAction_getControlTime.argtypes = [ControlAction]
    ControlAction_getControlTime.restype = uint64_t

ControlPerformCheckHandler = CFUNCTYPE(UNCHECKED(CheckHandlerResult), ControlAction, POINTER(None), POINTER(MmsValue), c_bool, c_bool)# /usr/local/include/libiec61850/iec61850_server.h: 1471

ControlWaitForExecutionHandler = CFUNCTYPE(UNCHECKED(ControlHandlerResult), ControlAction, POINTER(None), POINTER(MmsValue), c_bool, c_bool)# /usr/local/include/libiec61850/iec61850_server.h: 1495

ControlHandler = CFUNCTYPE(UNCHECKED(ControlHandlerResult), ControlAction, POINTER(None), POINTER(MmsValue), c_bool)# /usr/local/include/libiec61850/iec61850_server.h: 1517

enum_anon_56 = c_int# /usr/local/include/libiec61850/iec61850_server.h: 1529

SELECT_STATE_REASON_SELECTED = 0# /usr/local/include/libiec61850/iec61850_server.h: 1529

SELECT_STATE_REASON_CANCELED = (SELECT_STATE_REASON_SELECTED + 1)# /usr/local/include/libiec61850/iec61850_server.h: 1529

SELECT_STATE_REASON_TIMEOUT = (SELECT_STATE_REASON_CANCELED + 1)# /usr/local/include/libiec61850/iec61850_server.h: 1529

SELECT_STATE_REASON_OPERATED = (SELECT_STATE_REASON_TIMEOUT + 1)# /usr/local/include/libiec61850/iec61850_server.h: 1529

SELECT_STATE_REASON_OPERATE_FAILED = (SELECT_STATE_REASON_OPERATED + 1)# /usr/local/include/libiec61850/iec61850_server.h: 1529

SELECT_STATE_REASON_DISCONNECTED = (SELECT_STATE_REASON_OPERATE_FAILED + 1)# /usr/local/include/libiec61850/iec61850_server.h: 1529

SelectStateChangedReason = enum_anon_56# /usr/local/include/libiec61850/iec61850_server.h: 1529

ControlSelectStateChangedHandler = CFUNCTYPE(UNCHECKED(None), ControlAction, POINTER(None), c_bool, SelectStateChangedReason)# /usr/local/include/libiec61850/iec61850_server.h: 1541

# /usr/local/include/libiec61850/iec61850_server.h: 1557
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_setControlHandler", "cdecl"):
    IedServer_setControlHandler = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_setControlHandler", "cdecl")
    IedServer_setControlHandler.argtypes = [IedServer, POINTER(DataObject), ControlHandler, POINTER(None)]
    IedServer_setControlHandler.restype = None

# /usr/local/include/libiec61850/iec61850_server.h: 1574
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_setPerformCheckHandler", "cdecl"):
    IedServer_setPerformCheckHandler = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_setPerformCheckHandler", "cdecl")
    IedServer_setPerformCheckHandler.argtypes = [IedServer, POINTER(DataObject), ControlPerformCheckHandler, POINTER(None)]
    IedServer_setPerformCheckHandler.restype = None

# /usr/local/include/libiec61850/iec61850_server.h: 1591
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_setWaitForExecutionHandler", "cdecl"):
    IedServer_setWaitForExecutionHandler = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_setWaitForExecutionHandler", "cdecl")
    IedServer_setWaitForExecutionHandler.argtypes = [IedServer, POINTER(DataObject), ControlWaitForExecutionHandler, POINTER(None)]
    IedServer_setWaitForExecutionHandler.restype = None

# /usr/local/include/libiec61850/iec61850_server.h: 1610
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_setSelectStateChangedHandler", "cdecl"):
    IedServer_setSelectStateChangedHandler = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_setSelectStateChangedHandler", "cdecl")
    IedServer_setSelectStateChangedHandler.argtypes = [IedServer, POINTER(DataObject), ControlSelectStateChangedHandler, POINTER(None)]
    IedServer_setSelectStateChangedHandler.restype = None

# /usr/local/include/libiec61850/iec61850_server.h: 1623
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_updateCtlModel", "cdecl"):
    IedServer_updateCtlModel = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_updateCtlModel", "cdecl")
    IedServer_updateCtlModel.argtypes = [IedServer, POINTER(DataObject), ControlModel]
    IedServer_updateCtlModel.restype = None

enum_anon_57 = c_int# /usr/local/include/libiec61850/iec61850_server.h: 1644

RCB_EVENT_GET_PARAMETER = 0# /usr/local/include/libiec61850/iec61850_server.h: 1644

RCB_EVENT_SET_PARAMETER = (RCB_EVENT_GET_PARAMETER + 1)# /usr/local/include/libiec61850/iec61850_server.h: 1644

RCB_EVENT_UNRESERVED = (RCB_EVENT_SET_PARAMETER + 1)# /usr/local/include/libiec61850/iec61850_server.h: 1644

RCB_EVENT_RESERVED = (RCB_EVENT_UNRESERVED + 1)# /usr/local/include/libiec61850/iec61850_server.h: 1644

RCB_EVENT_ENABLE = (RCB_EVENT_RESERVED + 1)# /usr/local/include/libiec61850/iec61850_server.h: 1644

RCB_EVENT_DISABLE = (RCB_EVENT_ENABLE + 1)# /usr/local/include/libiec61850/iec61850_server.h: 1644

RCB_EVENT_GI = (RCB_EVENT_DISABLE + 1)# /usr/local/include/libiec61850/iec61850_server.h: 1644

RCB_EVENT_PURGEBUF = (RCB_EVENT_GI + 1)# /usr/local/include/libiec61850/iec61850_server.h: 1644

RCB_EVENT_OVERFLOW = (RCB_EVENT_PURGEBUF + 1)# /usr/local/include/libiec61850/iec61850_server.h: 1644

RCB_EVENT_REPORT_CREATED = (RCB_EVENT_OVERFLOW + 1)# /usr/local/include/libiec61850/iec61850_server.h: 1644

IedServer_RCBEventType = enum_anon_57# /usr/local/include/libiec61850/iec61850_server.h: 1644

IedServer_RCBEventHandler = CFUNCTYPE(UNCHECKED(None), POINTER(None), POINTER(ReportControlBlock), ClientConnection, IedServer_RCBEventType, String, MmsDataAccessError)# /usr/local/include/libiec61850/iec61850_server.h: 1656

# /usr/local/include/libiec61850/iec61850_server.h: 1666
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_setRCBEventHandler", "cdecl"):
    IedServer_setRCBEventHandler = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_setRCBEventHandler", "cdecl")
    IedServer_setRCBEventHandler.argtypes = [IedServer, IedServer_RCBEventHandler, POINTER(None)]
    IedServer_setRCBEventHandler.restype = None

SVCBEventHandler = CFUNCTYPE(UNCHECKED(None), POINTER(SVControlBlock), c_int, POINTER(None))# /usr/local/include/libiec61850/iec61850_server.h: 1689

# /usr/local/include/libiec61850/iec61850_server.h: 1700
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_setSVCBHandler", "cdecl"):
    IedServer_setSVCBHandler = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_setSVCBHandler", "cdecl")
    IedServer_setSVCBHandler.argtypes = [IedServer, POINTER(SVControlBlock), SVCBEventHandler, POINTER(None)]
    IedServer_setSVCBHandler.restype = None

# /usr/local/include/libiec61850/iec61850_server.h: 1710
class struct_sMmsGooseControlBlock(Structure):
    pass

MmsGooseControlBlock = POINTER(struct_sMmsGooseControlBlock)# /usr/local/include/libiec61850/iec61850_server.h: 1710

GoCBEventHandler = CFUNCTYPE(UNCHECKED(None), MmsGooseControlBlock, c_int, POINTER(None))# /usr/local/include/libiec61850/iec61850_server.h: 1718

# /usr/local/include/libiec61850/iec61850_server.h: 1731
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_setGoCBHandler", "cdecl"):
    IedServer_setGoCBHandler = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_setGoCBHandler", "cdecl")
    IedServer_setGoCBHandler.argtypes = [IedServer, GoCBEventHandler, POINTER(None)]
    IedServer_setGoCBHandler.restype = None

# /usr/local/include/libiec61850/iec61850_server.h: 1733
if _libs["/usr/local/lib/libiec61850.so"].has("MmsGooseControlBlock_getName", "cdecl"):
    MmsGooseControlBlock_getName = _libs["/usr/local/lib/libiec61850.so"].get("MmsGooseControlBlock_getName", "cdecl")
    MmsGooseControlBlock_getName.argtypes = [MmsGooseControlBlock]
    if sizeof(c_int) == sizeof(c_void_p):
        MmsGooseControlBlock_getName.restype = ReturnString
    else:
        MmsGooseControlBlock_getName.restype = String
        MmsGooseControlBlock_getName.errcheck = ReturnString

# /usr/local/include/libiec61850/iec61850_server.h: 1736
if _libs["/usr/local/lib/libiec61850.so"].has("MmsGooseControlBlock_getLogicalNode", "cdecl"):
    MmsGooseControlBlock_getLogicalNode = _libs["/usr/local/lib/libiec61850.so"].get("MmsGooseControlBlock_getLogicalNode", "cdecl")
    MmsGooseControlBlock_getLogicalNode.argtypes = [MmsGooseControlBlock]
    MmsGooseControlBlock_getLogicalNode.restype = POINTER(LogicalNode)

# /usr/local/include/libiec61850/iec61850_server.h: 1739
if _libs["/usr/local/lib/libiec61850.so"].has("MmsGooseControlBlock_getDataSet", "cdecl"):
    MmsGooseControlBlock_getDataSet = _libs["/usr/local/lib/libiec61850.so"].get("MmsGooseControlBlock_getDataSet", "cdecl")
    MmsGooseControlBlock_getDataSet.argtypes = [MmsGooseControlBlock]
    MmsGooseControlBlock_getDataSet.restype = POINTER(DataSet)

# /usr/local/include/libiec61850/iec61850_server.h: 1743
if _libs["/usr/local/lib/libiec61850.so"].has("MmsGooseControlBlock_getGoEna", "cdecl"):
    MmsGooseControlBlock_getGoEna = _libs["/usr/local/lib/libiec61850.so"].get("MmsGooseControlBlock_getGoEna", "cdecl")
    MmsGooseControlBlock_getGoEna.argtypes = [MmsGooseControlBlock]
    MmsGooseControlBlock_getGoEna.restype = c_bool

# /usr/local/include/libiec61850/iec61850_server.h: 1746
if _libs["/usr/local/lib/libiec61850.so"].has("MmsGooseControlBlock_getMinTime", "cdecl"):
    MmsGooseControlBlock_getMinTime = _libs["/usr/local/lib/libiec61850.so"].get("MmsGooseControlBlock_getMinTime", "cdecl")
    MmsGooseControlBlock_getMinTime.argtypes = [MmsGooseControlBlock]
    MmsGooseControlBlock_getMinTime.restype = c_int

# /usr/local/include/libiec61850/iec61850_server.h: 1749
if _libs["/usr/local/lib/libiec61850.so"].has("MmsGooseControlBlock_getMaxTime", "cdecl"):
    MmsGooseControlBlock_getMaxTime = _libs["/usr/local/lib/libiec61850.so"].get("MmsGooseControlBlock_getMaxTime", "cdecl")
    MmsGooseControlBlock_getMaxTime.argtypes = [MmsGooseControlBlock]
    MmsGooseControlBlock_getMaxTime.restype = c_int

# /usr/local/include/libiec61850/iec61850_server.h: 1752
if _libs["/usr/local/lib/libiec61850.so"].has("MmsGooseControlBlock_getFixedOffs", "cdecl"):
    MmsGooseControlBlock_getFixedOffs = _libs["/usr/local/lib/libiec61850.so"].get("MmsGooseControlBlock_getFixedOffs", "cdecl")
    MmsGooseControlBlock_getFixedOffs.argtypes = [MmsGooseControlBlock]
    MmsGooseControlBlock_getFixedOffs.restype = c_bool

# /usr/local/include/libiec61850/iec61850_server.h: 1755
if _libs["/usr/local/lib/libiec61850.so"].has("MmsGooseControlBlock_getNdsCom", "cdecl"):
    MmsGooseControlBlock_getNdsCom = _libs["/usr/local/lib/libiec61850.so"].get("MmsGooseControlBlock_getNdsCom", "cdecl")
    MmsGooseControlBlock_getNdsCom.argtypes = [MmsGooseControlBlock]
    MmsGooseControlBlock_getNdsCom.restype = c_bool

WriteAccessHandler = CFUNCTYPE(UNCHECKED(MmsDataAccessError), POINTER(DataAttribute), POINTER(MmsValue), ClientConnection, POINTER(None))# /usr/local/include/libiec61850/iec61850_server.h: 1792

# /usr/local/include/libiec61850/iec61850_server.h: 1814
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_handleWriteAccess", "cdecl"):
    IedServer_handleWriteAccess = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_handleWriteAccess", "cdecl")
    IedServer_handleWriteAccess.argtypes = [IedServer, POINTER(DataAttribute), WriteAccessHandler, POINTER(None)]
    IedServer_handleWriteAccess.restype = None

# /usr/local/include/libiec61850/iec61850_server.h: 1837
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_handleWriteAccessForComplexAttribute", "cdecl"):
    IedServer_handleWriteAccessForComplexAttribute = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_handleWriteAccessForComplexAttribute", "cdecl")
    IedServer_handleWriteAccessForComplexAttribute.argtypes = [IedServer, POINTER(DataAttribute), WriteAccessHandler, POINTER(None)]
    IedServer_handleWriteAccessForComplexAttribute.restype = None

enum_anon_58 = c_int# /usr/local/include/libiec61850/iec61850_server.h: 1843

ACCESS_POLICY_ALLOW = 0# /usr/local/include/libiec61850/iec61850_server.h: 1843

ACCESS_POLICY_DENY = (ACCESS_POLICY_ALLOW + 1)# /usr/local/include/libiec61850/iec61850_server.h: 1843

AccessPolicy = enum_anon_58# /usr/local/include/libiec61850/iec61850_server.h: 1843

# /usr/local/include/libiec61850/iec61850_server.h: 1854
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_setWriteAccessPolicy", "cdecl"):
    IedServer_setWriteAccessPolicy = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_setWriteAccessPolicy", "cdecl")
    IedServer_setWriteAccessPolicy.argtypes = [IedServer, FunctionalConstraint, AccessPolicy]
    IedServer_setWriteAccessPolicy.restype = None

ReadAccessHandler = CFUNCTYPE(UNCHECKED(MmsDataAccessError), POINTER(LogicalDevice), POINTER(LogicalNode), POINTER(DataObject), FunctionalConstraint, ClientConnection, POINTER(None))# /usr/local/include/libiec61850/iec61850_server.h: 1873

# /usr/local/include/libiec61850/iec61850_server.h: 1885
if _libs["/usr/local/lib/libiec61850.so"].has("IedServer_setReadAccessHandler", "cdecl"):
    IedServer_setReadAccessHandler = _libs["/usr/local/lib/libiec61850.so"].get("IedServer_setReadAccessHandler", "cdecl")
    IedServer_setReadAccessHandler.argtypes = [IedServer, ReadAccessHandler, POINTER(None)]
    IedServer_setReadAccessHandler.restype = None

enum_anon_59 = c_int# /usr/local/include/libiec61850/goose_subscriber.h: 51

GOOSE_PARSE_ERROR_NO_ERROR = 0# /usr/local/include/libiec61850/goose_subscriber.h: 51

GOOSE_PARSE_ERROR_UNKNOWN_TAG = (GOOSE_PARSE_ERROR_NO_ERROR + 1)# /usr/local/include/libiec61850/goose_subscriber.h: 51

GOOSE_PARSE_ERROR_TAGDECODE = (GOOSE_PARSE_ERROR_UNKNOWN_TAG + 1)# /usr/local/include/libiec61850/goose_subscriber.h: 51

GOOSE_PARSE_ERROR_SUBLEVEL = (GOOSE_PARSE_ERROR_TAGDECODE + 1)# /usr/local/include/libiec61850/goose_subscriber.h: 51

GOOSE_PARSE_ERROR_OVERFLOW = (GOOSE_PARSE_ERROR_SUBLEVEL + 1)# /usr/local/include/libiec61850/goose_subscriber.h: 51

GOOSE_PARSE_ERROR_UNDERFLOW = (GOOSE_PARSE_ERROR_OVERFLOW + 1)# /usr/local/include/libiec61850/goose_subscriber.h: 51

GOOSE_PARSE_ERROR_TYPE_MISMATCH = (GOOSE_PARSE_ERROR_UNDERFLOW + 1)# /usr/local/include/libiec61850/goose_subscriber.h: 51

GOOSE_PARSE_ERROR_LENGTH_MISMATCH = (GOOSE_PARSE_ERROR_TYPE_MISMATCH + 1)# /usr/local/include/libiec61850/goose_subscriber.h: 51

GOOSE_PARSE_ERROR_INVALID_PADDING = (GOOSE_PARSE_ERROR_LENGTH_MISMATCH + 1)# /usr/local/include/libiec61850/goose_subscriber.h: 51

GooseParseError = enum_anon_59# /usr/local/include/libiec61850/goose_subscriber.h: 51

# /usr/local/include/libiec61850/goose_subscriber.h: 53
class struct_sGooseSubscriber(Structure):
    pass

GooseSubscriber = POINTER(struct_sGooseSubscriber)# /usr/local/include/libiec61850/goose_subscriber.h: 53

GooseListener = CFUNCTYPE(UNCHECKED(None), GooseSubscriber, POINTER(None))# /usr/local/include/libiec61850/goose_subscriber.h: 61

# /usr/local/include/libiec61850/goose_subscriber.h: 84
if _libs["/usr/local/lib/libiec61850.so"].has("GooseSubscriber_create", "cdecl"):
    GooseSubscriber_create = _libs["/usr/local/lib/libiec61850.so"].get("GooseSubscriber_create", "cdecl")
    GooseSubscriber_create.argtypes = [String, POINTER(MmsValue)]
    GooseSubscriber_create.restype = GooseSubscriber

# /usr/local/include/libiec61850/goose_subscriber.h: 91
if _libs["/usr/local/lib/libiec61850.so"].has("GooseSubscriber_getGoId", "cdecl"):
    GooseSubscriber_getGoId = _libs["/usr/local/lib/libiec61850.so"].get("GooseSubscriber_getGoId", "cdecl")
    GooseSubscriber_getGoId.argtypes = [GooseSubscriber]
    if sizeof(c_int) == sizeof(c_void_p):
        GooseSubscriber_getGoId.restype = ReturnString
    else:
        GooseSubscriber_getGoId.restype = String
        GooseSubscriber_getGoId.errcheck = ReturnString

# /usr/local/include/libiec61850/goose_subscriber.h: 99
if _libs["/usr/local/lib/libiec61850.so"].has("GooseSubscriber_getGoCbRef", "cdecl"):
    GooseSubscriber_getGoCbRef = _libs["/usr/local/lib/libiec61850.so"].get("GooseSubscriber_getGoCbRef", "cdecl")
    GooseSubscriber_getGoCbRef.argtypes = [GooseSubscriber]
    if sizeof(c_int) == sizeof(c_void_p):
        GooseSubscriber_getGoCbRef.restype = ReturnString
    else:
        GooseSubscriber_getGoCbRef.restype = String
        GooseSubscriber_getGoCbRef.errcheck = ReturnString

# /usr/local/include/libiec61850/goose_subscriber.h: 107
if _libs["/usr/local/lib/libiec61850.so"].has("GooseSubscriber_getDataSet", "cdecl"):
    GooseSubscriber_getDataSet = _libs["/usr/local/lib/libiec61850.so"].get("GooseSubscriber_getDataSet", "cdecl")
    GooseSubscriber_getDataSet.argtypes = [GooseSubscriber]
    if sizeof(c_int) == sizeof(c_void_p):
        GooseSubscriber_getDataSet.restype = ReturnString
    else:
        GooseSubscriber_getDataSet.restype = String
        GooseSubscriber_getDataSet.errcheck = ReturnString

# /usr/local/include/libiec61850/goose_subscriber.h: 119
if _libs["/usr/local/lib/libiec61850.so"].has("GooseSubscriber_setDstMac", "cdecl"):
    GooseSubscriber_setDstMac = _libs["/usr/local/lib/libiec61850.so"].get("GooseSubscriber_setDstMac", "cdecl")
    GooseSubscriber_setDstMac.argtypes = [GooseSubscriber, uint8_t * int(6)]
    GooseSubscriber_setDstMac.restype = None

# /usr/local/include/libiec61850/goose_subscriber.h: 130
if _libs["/usr/local/lib/libiec61850.so"].has("GooseSubscriber_setAppId", "cdecl"):
    GooseSubscriber_setAppId = _libs["/usr/local/lib/libiec61850.so"].get("GooseSubscriber_setAppId", "cdecl")
    GooseSubscriber_setAppId.argtypes = [GooseSubscriber, uint16_t]
    GooseSubscriber_setAppId.restype = None

# /usr/local/include/libiec61850/goose_subscriber.h: 140
if _libs["/usr/local/lib/libiec61850.so"].has("GooseSubscriber_isValid", "cdecl"):
    GooseSubscriber_isValid = _libs["/usr/local/lib/libiec61850.so"].get("GooseSubscriber_isValid", "cdecl")
    GooseSubscriber_isValid.argtypes = [GooseSubscriber]
    GooseSubscriber_isValid.restype = c_bool

# /usr/local/include/libiec61850/goose_subscriber.h: 150
if _libs["/usr/local/lib/libiec61850.so"].has("GooseSubscriber_getParseError", "cdecl"):
    GooseSubscriber_getParseError = _libs["/usr/local/lib/libiec61850.so"].get("GooseSubscriber_getParseError", "cdecl")
    GooseSubscriber_getParseError.argtypes = [GooseSubscriber]
    GooseSubscriber_getParseError.restype = GooseParseError

# /usr/local/include/libiec61850/goose_subscriber.h: 161
if _libs["/usr/local/lib/libiec61850.so"].has("GooseSubscriber_destroy", "cdecl"):
    GooseSubscriber_destroy = _libs["/usr/local/lib/libiec61850.so"].get("GooseSubscriber_destroy", "cdecl")
    GooseSubscriber_destroy.argtypes = [GooseSubscriber]
    GooseSubscriber_destroy.restype = None

# /usr/local/include/libiec61850/goose_subscriber.h: 171
if _libs["/usr/local/lib/libiec61850.so"].has("GooseSubscriber_setListener", "cdecl"):
    GooseSubscriber_setListener = _libs["/usr/local/lib/libiec61850.so"].get("GooseSubscriber_setListener", "cdecl")
    GooseSubscriber_setListener.argtypes = [GooseSubscriber, GooseListener, POINTER(None)]
    GooseSubscriber_setListener.restype = None

# /usr/local/include/libiec61850/goose_subscriber.h: 179
if _libs["/usr/local/lib/libiec61850.so"].has("GooseSubscriber_getAppId", "cdecl"):
    GooseSubscriber_getAppId = _libs["/usr/local/lib/libiec61850.so"].get("GooseSubscriber_getAppId", "cdecl")
    GooseSubscriber_getAppId.argtypes = [GooseSubscriber]
    GooseSubscriber_getAppId.restype = c_int32

# /usr/local/include/libiec61850/goose_subscriber.h: 188
if _libs["/usr/local/lib/libiec61850.so"].has("GooseSubscriber_getSrcMac", "cdecl"):
    GooseSubscriber_getSrcMac = _libs["/usr/local/lib/libiec61850.so"].get("GooseSubscriber_getSrcMac", "cdecl")
    GooseSubscriber_getSrcMac.argtypes = [GooseSubscriber, POINTER(uint8_t)]
    GooseSubscriber_getSrcMac.restype = None

# /usr/local/include/libiec61850/goose_subscriber.h: 197
if _libs["/usr/local/lib/libiec61850.so"].has("GooseSubscriber_getDstMac", "cdecl"):
    GooseSubscriber_getDstMac = _libs["/usr/local/lib/libiec61850.so"].get("GooseSubscriber_getDstMac", "cdecl")
    GooseSubscriber_getDstMac.argtypes = [GooseSubscriber, POINTER(uint8_t)]
    GooseSubscriber_getDstMac.restype = None

# /usr/local/include/libiec61850/goose_subscriber.h: 209
if _libs["/usr/local/lib/libiec61850.so"].has("GooseSubscriber_getStNum", "cdecl"):
    GooseSubscriber_getStNum = _libs["/usr/local/lib/libiec61850.so"].get("GooseSubscriber_getStNum", "cdecl")
    GooseSubscriber_getStNum.argtypes = [GooseSubscriber]
    GooseSubscriber_getStNum.restype = uint32_t

# /usr/local/include/libiec61850/goose_subscriber.h: 222
if _libs["/usr/local/lib/libiec61850.so"].has("GooseSubscriber_getSqNum", "cdecl"):
    GooseSubscriber_getSqNum = _libs["/usr/local/lib/libiec61850.so"].get("GooseSubscriber_getSqNum", "cdecl")
    GooseSubscriber_getSqNum.argtypes = [GooseSubscriber]
    GooseSubscriber_getSqNum.restype = uint32_t

# /usr/local/include/libiec61850/goose_subscriber.h: 234
if _libs["/usr/local/lib/libiec61850.so"].has("GooseSubscriber_isTest", "cdecl"):
    GooseSubscriber_isTest = _libs["/usr/local/lib/libiec61850.so"].get("GooseSubscriber_isTest", "cdecl")
    GooseSubscriber_isTest.argtypes = [GooseSubscriber]
    GooseSubscriber_isTest.restype = c_bool

# /usr/local/include/libiec61850/goose_subscriber.h: 245
if _libs["/usr/local/lib/libiec61850.so"].has("GooseSubscriber_getConfRev", "cdecl"):
    GooseSubscriber_getConfRev = _libs["/usr/local/lib/libiec61850.so"].get("GooseSubscriber_getConfRev", "cdecl")
    GooseSubscriber_getConfRev.argtypes = [GooseSubscriber]
    GooseSubscriber_getConfRev.restype = uint32_t

# /usr/local/include/libiec61850/goose_subscriber.h: 258
if _libs["/usr/local/lib/libiec61850.so"].has("GooseSubscriber_needsCommission", "cdecl"):
    GooseSubscriber_needsCommission = _libs["/usr/local/lib/libiec61850.so"].get("GooseSubscriber_needsCommission", "cdecl")
    GooseSubscriber_needsCommission.argtypes = [GooseSubscriber]
    GooseSubscriber_needsCommission.restype = c_bool

# /usr/local/include/libiec61850/goose_subscriber.h: 268
if _libs["/usr/local/lib/libiec61850.so"].has("GooseSubscriber_getTimeAllowedToLive", "cdecl"):
    GooseSubscriber_getTimeAllowedToLive = _libs["/usr/local/lib/libiec61850.so"].get("GooseSubscriber_getTimeAllowedToLive", "cdecl")
    GooseSubscriber_getTimeAllowedToLive.argtypes = [GooseSubscriber]
    GooseSubscriber_getTimeAllowedToLive.restype = uint32_t

# /usr/local/include/libiec61850/goose_subscriber.h: 278
if _libs["/usr/local/lib/libiec61850.so"].has("GooseSubscriber_getTimestamp", "cdecl"):
    GooseSubscriber_getTimestamp = _libs["/usr/local/lib/libiec61850.so"].get("GooseSubscriber_getTimestamp", "cdecl")
    GooseSubscriber_getTimestamp.argtypes = [GooseSubscriber]
    GooseSubscriber_getTimestamp.restype = uint64_t

# /usr/local/include/libiec61850/goose_subscriber.h: 291
if _libs["/usr/local/lib/libiec61850.so"].has("GooseSubscriber_getDataSetValues", "cdecl"):
    GooseSubscriber_getDataSetValues = _libs["/usr/local/lib/libiec61850.so"].get("GooseSubscriber_getDataSetValues", "cdecl")
    GooseSubscriber_getDataSetValues.argtypes = [GooseSubscriber]
    GooseSubscriber_getDataSetValues.restype = POINTER(MmsValue)

# /usr/local/include/libiec61850/goose_subscriber.h: 295
if _libs["/usr/local/lib/libiec61850.so"].has("GooseSubscriber_isVlanSet", "cdecl"):
    GooseSubscriber_isVlanSet = _libs["/usr/local/lib/libiec61850.so"].get("GooseSubscriber_isVlanSet", "cdecl")
    GooseSubscriber_isVlanSet.argtypes = [GooseSubscriber]
    GooseSubscriber_isVlanSet.restype = c_bool

# /usr/local/include/libiec61850/goose_subscriber.h: 298
if _libs["/usr/local/lib/libiec61850.so"].has("GooseSubscriber_getVlanId", "cdecl"):
    GooseSubscriber_getVlanId = _libs["/usr/local/lib/libiec61850.so"].get("GooseSubscriber_getVlanId", "cdecl")
    GooseSubscriber_getVlanId.argtypes = [GooseSubscriber]
    GooseSubscriber_getVlanId.restype = uint16_t

# /usr/local/include/libiec61850/goose_subscriber.h: 301
if _libs["/usr/local/lib/libiec61850.so"].has("GooseSubscriber_getVlanPrio", "cdecl"):
    GooseSubscriber_getVlanPrio = _libs["/usr/local/lib/libiec61850.so"].get("GooseSubscriber_getVlanPrio", "cdecl")
    GooseSubscriber_getVlanPrio.argtypes = [GooseSubscriber]
    GooseSubscriber_getVlanPrio.restype = uint8_t

# /usr/local/include/libiec61850/goose_subscriber.h: 310
if _libs["/usr/local/lib/libiec61850.so"].has("GooseSubscriber_setObserver", "cdecl"):
    GooseSubscriber_setObserver = _libs["/usr/local/lib/libiec61850.so"].get("GooseSubscriber_setObserver", "cdecl")
    GooseSubscriber_setObserver.argtypes = [GooseSubscriber]
    GooseSubscriber_setObserver.restype = None

# /usr/local/include/libiec61850/goose_receiver.h: 41
class struct_sGooseReceiver(Structure):
    pass

GooseReceiver = POINTER(struct_sGooseReceiver)# /usr/local/include/libiec61850/goose_receiver.h: 41

# /usr/local/include/libiec61850/goose_receiver.h: 52
if _libs["/usr/local/lib/libiec61850.so"].has("GooseReceiver_create", "cdecl"):
    GooseReceiver_create = _libs["/usr/local/lib/libiec61850.so"].get("GooseReceiver_create", "cdecl")
    GooseReceiver_create.argtypes = []
    GooseReceiver_create.restype = GooseReceiver

# /usr/local/include/libiec61850/goose_receiver.h: 65
if _libs["/usr/local/lib/libiec61850.so"].has("GooseReceiver_createEx", "cdecl"):
    GooseReceiver_createEx = _libs["/usr/local/lib/libiec61850.so"].get("GooseReceiver_createEx", "cdecl")
    GooseReceiver_createEx.argtypes = [POINTER(uint8_t)]
    GooseReceiver_createEx.restype = GooseReceiver

# /usr/local/include/libiec61850/goose_receiver.h: 74
if _libs["/usr/local/lib/libiec61850.so"].has("GooseReceiver_setInterfaceId", "cdecl"):
    GooseReceiver_setInterfaceId = _libs["/usr/local/lib/libiec61850.so"].get("GooseReceiver_setInterfaceId", "cdecl")
    GooseReceiver_setInterfaceId.argtypes = [GooseReceiver, String]
    GooseReceiver_setInterfaceId.restype = None

# /usr/local/include/libiec61850/goose_receiver.h: 83
if _libs["/usr/local/lib/libiec61850.so"].has("GooseReceiver_getInterfaceId", "cdecl"):
    GooseReceiver_getInterfaceId = _libs["/usr/local/lib/libiec61850.so"].get("GooseReceiver_getInterfaceId", "cdecl")
    GooseReceiver_getInterfaceId.argtypes = [GooseReceiver]
    GooseReceiver_getInterfaceId.restype = c_char_p

# /usr/local/include/libiec61850/goose_receiver.h: 96
if _libs["/usr/local/lib/libiec61850.so"].has("GooseReceiver_addSubscriber", "cdecl"):
    GooseReceiver_addSubscriber = _libs["/usr/local/lib/libiec61850.so"].get("GooseReceiver_addSubscriber", "cdecl")
    GooseReceiver_addSubscriber.argtypes = [GooseReceiver, GooseSubscriber]
    GooseReceiver_addSubscriber.restype = None

# /usr/local/include/libiec61850/goose_receiver.h: 108
if _libs["/usr/local/lib/libiec61850.so"].has("GooseReceiver_removeSubscriber", "cdecl"):
    GooseReceiver_removeSubscriber = _libs["/usr/local/lib/libiec61850.so"].get("GooseReceiver_removeSubscriber", "cdecl")
    GooseReceiver_removeSubscriber.argtypes = [GooseReceiver, GooseSubscriber]
    GooseReceiver_removeSubscriber.restype = None

# /usr/local/include/libiec61850/goose_receiver.h: 116
if _libs["/usr/local/lib/libiec61850.so"].has("GooseReceiver_start", "cdecl"):
    GooseReceiver_start = _libs["/usr/local/lib/libiec61850.so"].get("GooseReceiver_start", "cdecl")
    GooseReceiver_start.argtypes = [GooseReceiver]
    GooseReceiver_start.restype = None

# /usr/local/include/libiec61850/goose_receiver.h: 126
if _libs["/usr/local/lib/libiec61850.so"].has("GooseReceiver_stop", "cdecl"):
    GooseReceiver_stop = _libs["/usr/local/lib/libiec61850.so"].get("GooseReceiver_stop", "cdecl")
    GooseReceiver_stop.argtypes = [GooseReceiver]
    GooseReceiver_stop.restype = None

# /usr/local/include/libiec61850/goose_receiver.h: 138
if _libs["/usr/local/lib/libiec61850.so"].has("GooseReceiver_isRunning", "cdecl"):
    GooseReceiver_isRunning = _libs["/usr/local/lib/libiec61850.so"].get("GooseReceiver_isRunning", "cdecl")
    GooseReceiver_isRunning.argtypes = [GooseReceiver]
    GooseReceiver_isRunning.restype = c_bool

# /usr/local/include/libiec61850/goose_receiver.h: 146
if _libs["/usr/local/lib/libiec61850.so"].has("GooseReceiver_destroy", "cdecl"):
    GooseReceiver_destroy = _libs["/usr/local/lib/libiec61850.so"].get("GooseReceiver_destroy", "cdecl")
    GooseReceiver_destroy.argtypes = [GooseReceiver]
    GooseReceiver_destroy.restype = None

# /usr/local/include/libiec61850/goose_receiver.h: 152
if _libs["/usr/local/lib/libiec61850.so"].has("GooseReceiver_startThreadless", "cdecl"):
    GooseReceiver_startThreadless = _libs["/usr/local/lib/libiec61850.so"].get("GooseReceiver_startThreadless", "cdecl")
    GooseReceiver_startThreadless.argtypes = [GooseReceiver]
    GooseReceiver_startThreadless.restype = EthernetSocket

# /usr/local/include/libiec61850/goose_receiver.h: 155
if _libs["/usr/local/lib/libiec61850.so"].has("GooseReceiver_stopThreadless", "cdecl"):
    GooseReceiver_stopThreadless = _libs["/usr/local/lib/libiec61850.so"].get("GooseReceiver_stopThreadless", "cdecl")
    GooseReceiver_stopThreadless.argtypes = [GooseReceiver]
    GooseReceiver_stopThreadless.restype = None

# /usr/local/include/libiec61850/goose_receiver.h: 167
if _libs["/usr/local/lib/libiec61850.so"].has("GooseReceiver_tick", "cdecl"):
    GooseReceiver_tick = _libs["/usr/local/lib/libiec61850.so"].get("GooseReceiver_tick", "cdecl")
    GooseReceiver_tick.argtypes = [GooseReceiver]
    GooseReceiver_tick.restype = c_bool

# /usr/local/include/libiec61850/goose_receiver.h: 180
if _libs["/usr/local/lib/libiec61850.so"].has("GooseReceiver_handleMessage", "cdecl"):
    GooseReceiver_handleMessage = _libs["/usr/local/lib/libiec61850.so"].get("GooseReceiver_handleMessage", "cdecl")
    GooseReceiver_handleMessage.argtypes = [GooseReceiver, POINTER(uint8_t), c_int]
    GooseReceiver_handleMessage.restype = None

# /usr/local/include/libiec61850/goose_publisher.h: 43
class struct_sCommParameters(Structure):
    pass

struct_sCommParameters.__slots__ = [
    'vlanPriority',
    'vlanId',
    'appId',
    'dstAddress',
]
struct_sCommParameters._fields_ = [
    ('vlanPriority', uint8_t),
    ('vlanId', uint16_t),
    ('appId', uint16_t),
    ('dstAddress', uint8_t * int(6)),
]

CommParameters = struct_sCommParameters# /usr/local/include/libiec61850/goose_publisher.h: 43

# /usr/local/include/libiec61850/goose_publisher.h: 47
class struct_sGoosePublisher(Structure):
    pass

GoosePublisher = POINTER(struct_sGoosePublisher)# /usr/local/include/libiec61850/goose_publisher.h: 47

# /usr/local/include/libiec61850/goose_publisher.h: 58
if _libs["/usr/local/lib/libiec61850.so"].has("GoosePublisher_create", "cdecl"):
    GoosePublisher_create = _libs["/usr/local/lib/libiec61850.so"].get("GoosePublisher_create", "cdecl")
    GoosePublisher_create.argtypes = [POINTER(CommParameters), String]
    GoosePublisher_create.restype = GoosePublisher

# /usr/local/include/libiec61850/goose_publisher.h: 68
if _libs["/usr/local/lib/libiec61850.so"].has("GoosePublisher_createEx", "cdecl"):
    GoosePublisher_createEx = _libs["/usr/local/lib/libiec61850.so"].get("GoosePublisher_createEx", "cdecl")
    GoosePublisher_createEx.argtypes = [POINTER(CommParameters), String, c_bool]
    GoosePublisher_createEx.restype = GoosePublisher

# /usr/local/include/libiec61850/goose_publisher.h: 76
if _libs["/usr/local/lib/libiec61850.so"].has("GoosePublisher_destroy", "cdecl"):
    GoosePublisher_destroy = _libs["/usr/local/lib/libiec61850.so"].get("GoosePublisher_destroy", "cdecl")
    GoosePublisher_destroy.argtypes = [GoosePublisher]
    GoosePublisher_destroy.restype = None

# /usr/local/include/libiec61850/goose_publisher.h: 87
if _libs["/usr/local/lib/libiec61850.so"].has("GoosePublisher_publish", "cdecl"):
    GoosePublisher_publish = _libs["/usr/local/lib/libiec61850.so"].get("GoosePublisher_publish", "cdecl")
    GoosePublisher_publish.argtypes = [GoosePublisher, LinkedList]
    GoosePublisher_publish.restype = c_int

# /usr/local/include/libiec61850/goose_publisher.h: 99
if _libs["/usr/local/lib/libiec61850.so"].has("GoosePublisher_publishAndDump", "cdecl"):
    GoosePublisher_publishAndDump = _libs["/usr/local/lib/libiec61850.so"].get("GoosePublisher_publishAndDump", "cdecl")
    GoosePublisher_publishAndDump.argtypes = [GoosePublisher, LinkedList, String, POINTER(c_int32), c_int32]
    GoosePublisher_publishAndDump.restype = c_int

# /usr/local/include/libiec61850/goose_publisher.h: 108
if _libs["/usr/local/lib/libiec61850.so"].has("GoosePublisher_setGoID", "cdecl"):
    GoosePublisher_setGoID = _libs["/usr/local/lib/libiec61850.so"].get("GoosePublisher_setGoID", "cdecl")
    GoosePublisher_setGoID.argtypes = [GoosePublisher, String]
    GoosePublisher_setGoID.restype = None

# /usr/local/include/libiec61850/goose_publisher.h: 117
if _libs["/usr/local/lib/libiec61850.so"].has("GoosePublisher_setGoCbRef", "cdecl"):
    GoosePublisher_setGoCbRef = _libs["/usr/local/lib/libiec61850.so"].get("GoosePublisher_setGoCbRef", "cdecl")
    GoosePublisher_setGoCbRef.argtypes = [GoosePublisher, String]
    GoosePublisher_setGoCbRef.restype = None

# /usr/local/include/libiec61850/goose_publisher.h: 126
if _libs["/usr/local/lib/libiec61850.so"].has("GoosePublisher_setTimeAllowedToLive", "cdecl"):
    GoosePublisher_setTimeAllowedToLive = _libs["/usr/local/lib/libiec61850.so"].get("GoosePublisher_setTimeAllowedToLive", "cdecl")
    GoosePublisher_setTimeAllowedToLive.argtypes = [GoosePublisher, uint32_t]
    GoosePublisher_setTimeAllowedToLive.restype = None

# /usr/local/include/libiec61850/goose_publisher.h: 135
if _libs["/usr/local/lib/libiec61850.so"].has("GoosePublisher_setDataSetRef", "cdecl"):
    GoosePublisher_setDataSetRef = _libs["/usr/local/lib/libiec61850.so"].get("GoosePublisher_setDataSetRef", "cdecl")
    GoosePublisher_setDataSetRef.argtypes = [GoosePublisher, String]
    GoosePublisher_setDataSetRef.restype = None

# /usr/local/include/libiec61850/goose_publisher.h: 144
if _libs["/usr/local/lib/libiec61850.so"].has("GoosePublisher_setConfRev", "cdecl"):
    GoosePublisher_setConfRev = _libs["/usr/local/lib/libiec61850.so"].get("GoosePublisher_setConfRev", "cdecl")
    GoosePublisher_setConfRev.argtypes = [GoosePublisher, uint32_t]
    GoosePublisher_setConfRev.restype = None

# /usr/local/include/libiec61850/goose_publisher.h: 153
if _libs["/usr/local/lib/libiec61850.so"].has("GoosePublisher_setSimulation", "cdecl"):
    GoosePublisher_setSimulation = _libs["/usr/local/lib/libiec61850.so"].get("GoosePublisher_setSimulation", "cdecl")
    GoosePublisher_setSimulation.argtypes = [GoosePublisher, c_bool]
    GoosePublisher_setSimulation.restype = None

# /usr/local/include/libiec61850/goose_publisher.h: 165
if _libs["/usr/local/lib/libiec61850.so"].has("GoosePublisher_setStNum", "cdecl"):
    GoosePublisher_setStNum = _libs["/usr/local/lib/libiec61850.so"].get("GoosePublisher_setStNum", "cdecl")
    GoosePublisher_setStNum.argtypes = [GoosePublisher, uint32_t]
    GoosePublisher_setStNum.restype = None

# /usr/local/include/libiec61850/goose_publisher.h: 176
if _libs["/usr/local/lib/libiec61850.so"].has("GoosePublisher_setSqNum", "cdecl"):
    GoosePublisher_setSqNum = _libs["/usr/local/lib/libiec61850.so"].get("GoosePublisher_setSqNum", "cdecl")
    GoosePublisher_setSqNum.argtypes = [GoosePublisher, uint32_t]
    GoosePublisher_setSqNum.restype = None

# /usr/local/include/libiec61850/goose_publisher.h: 185
if _libs["/usr/local/lib/libiec61850.so"].has("GoosePublisher_setNeedsCommission", "cdecl"):
    GoosePublisher_setNeedsCommission = _libs["/usr/local/lib/libiec61850.so"].get("GoosePublisher_setNeedsCommission", "cdecl")
    GoosePublisher_setNeedsCommission.argtypes = [GoosePublisher, c_bool]
    GoosePublisher_setNeedsCommission.restype = None

# /usr/local/include/libiec61850/goose_publisher.h: 197
if _libs["/usr/local/lib/libiec61850.so"].has("GoosePublisher_increaseStNum", "cdecl"):
    GoosePublisher_increaseStNum = _libs["/usr/local/lib/libiec61850.so"].get("GoosePublisher_increaseStNum", "cdecl")
    GoosePublisher_increaseStNum.argtypes = [GoosePublisher]
    GoosePublisher_increaseStNum.restype = uint64_t

# /usr/local/include/libiec61850/goose_publisher.h: 207
if _libs["/usr/local/lib/libiec61850.so"].has("GoosePublisher_reset", "cdecl"):
    GoosePublisher_reset = _libs["/usr/local/lib/libiec61850.so"].get("GoosePublisher_reset", "cdecl")
    GoosePublisher_reset.argtypes = [GoosePublisher]
    GoosePublisher_reset.restype = None

# /usr/local/include/libiec61850/sv_subscriber.h: 96
class struct_sSVSubscriber_ASDU(Structure):
    pass

SVSubscriber_ASDU = POINTER(struct_sSVSubscriber_ASDU)# /usr/local/include/libiec61850/sv_subscriber.h: 96

# /usr/local/include/libiec61850/sv_subscriber.h: 105
class struct_sSVSubscriber(Structure):
    pass

SVSubscriber = POINTER(struct_sSVSubscriber)# /usr/local/include/libiec61850/sv_subscriber.h: 105

SVUpdateListener = CFUNCTYPE(UNCHECKED(None), SVSubscriber, POINTER(None), SVSubscriber_ASDU)# /usr/local/include/libiec61850/sv_subscriber.h: 116

# /usr/local/include/libiec61850/sv_subscriber.h: 121
class struct_sSVReceiver(Structure):
    pass

SVReceiver = POINTER(struct_sSVReceiver)# /usr/local/include/libiec61850/sv_subscriber.h: 121

# /usr/local/include/libiec61850/sv_subscriber.h: 133
if _libs["/usr/local/lib/libiec61850.so"].has("SVReceiver_create", "cdecl"):
    SVReceiver_create = _libs["/usr/local/lib/libiec61850.so"].get("SVReceiver_create", "cdecl")
    SVReceiver_create.argtypes = []
    SVReceiver_create.restype = SVReceiver

# /usr/local/include/libiec61850/sv_subscriber.h: 141
if _libs["/usr/local/lib/libiec61850.so"].has("SVReceiver_disableDestAddrCheck", "cdecl"):
    SVReceiver_disableDestAddrCheck = _libs["/usr/local/lib/libiec61850.so"].get("SVReceiver_disableDestAddrCheck", "cdecl")
    SVReceiver_disableDestAddrCheck.argtypes = [SVReceiver]
    SVReceiver_disableDestAddrCheck.restype = None

# /usr/local/include/libiec61850/sv_subscriber.h: 154
if _libs["/usr/local/lib/libiec61850.so"].has("SVReceiver_enableDestAddrCheck", "cdecl"):
    SVReceiver_enableDestAddrCheck = _libs["/usr/local/lib/libiec61850.so"].get("SVReceiver_enableDestAddrCheck", "cdecl")
    SVReceiver_enableDestAddrCheck.argtypes = [SVReceiver]
    SVReceiver_enableDestAddrCheck.restype = None

# /usr/local/include/libiec61850/sv_subscriber.h: 167
if _libs["/usr/local/lib/libiec61850.so"].has("SVReceiver_setInterfaceId", "cdecl"):
    SVReceiver_setInterfaceId = _libs["/usr/local/lib/libiec61850.so"].get("SVReceiver_setInterfaceId", "cdecl")
    SVReceiver_setInterfaceId.argtypes = [SVReceiver, String]
    SVReceiver_setInterfaceId.restype = None

# /usr/local/include/libiec61850/sv_subscriber.h: 178
if _libs["/usr/local/lib/libiec61850.so"].has("SVReceiver_addSubscriber", "cdecl"):
    SVReceiver_addSubscriber = _libs["/usr/local/lib/libiec61850.so"].get("SVReceiver_addSubscriber", "cdecl")
    SVReceiver_addSubscriber.argtypes = [SVReceiver, SVSubscriber]
    SVReceiver_addSubscriber.restype = None

# /usr/local/include/libiec61850/sv_subscriber.h: 187
if _libs["/usr/local/lib/libiec61850.so"].has("SVReceiver_removeSubscriber", "cdecl"):
    SVReceiver_removeSubscriber = _libs["/usr/local/lib/libiec61850.so"].get("SVReceiver_removeSubscriber", "cdecl")
    SVReceiver_removeSubscriber.argtypes = [SVReceiver, SVSubscriber]
    SVReceiver_removeSubscriber.restype = None

# /usr/local/include/libiec61850/sv_subscriber.h: 197
if _libs["/usr/local/lib/libiec61850.so"].has("SVReceiver_start", "cdecl"):
    SVReceiver_start = _libs["/usr/local/lib/libiec61850.so"].get("SVReceiver_start", "cdecl")
    SVReceiver_start.argtypes = [SVReceiver]
    SVReceiver_start.restype = None

# /usr/local/include/libiec61850/sv_subscriber.h: 205
if _libs["/usr/local/lib/libiec61850.so"].has("SVReceiver_stop", "cdecl"):
    SVReceiver_stop = _libs["/usr/local/lib/libiec61850.so"].get("SVReceiver_stop", "cdecl")
    SVReceiver_stop.argtypes = [SVReceiver]
    SVReceiver_stop.restype = None

# /usr/local/include/libiec61850/sv_subscriber.h: 217
if _libs["/usr/local/lib/libiec61850.so"].has("SVReceiver_isRunning", "cdecl"):
    SVReceiver_isRunning = _libs["/usr/local/lib/libiec61850.so"].get("SVReceiver_isRunning", "cdecl")
    SVReceiver_isRunning.argtypes = [SVReceiver]
    SVReceiver_isRunning.restype = c_bool

# /usr/local/include/libiec61850/sv_subscriber.h: 225
if _libs["/usr/local/lib/libiec61850.so"].has("SVReceiver_destroy", "cdecl"):
    SVReceiver_destroy = _libs["/usr/local/lib/libiec61850.so"].get("SVReceiver_destroy", "cdecl")
    SVReceiver_destroy.argtypes = [SVReceiver]
    SVReceiver_destroy.restype = None

# /usr/local/include/libiec61850/sv_subscriber.h: 232
if _libs["/usr/local/lib/libiec61850.so"].has("SVReceiver_startThreadless", "cdecl"):
    SVReceiver_startThreadless = _libs["/usr/local/lib/libiec61850.so"].get("SVReceiver_startThreadless", "cdecl")
    SVReceiver_startThreadless.argtypes = [SVReceiver]
    SVReceiver_startThreadless.restype = EthernetSocket

# /usr/local/include/libiec61850/sv_subscriber.h: 235
if _libs["/usr/local/lib/libiec61850.so"].has("SVReceiver_stopThreadless", "cdecl"):
    SVReceiver_stopThreadless = _libs["/usr/local/lib/libiec61850.so"].get("SVReceiver_stopThreadless", "cdecl")
    SVReceiver_stopThreadless.argtypes = [SVReceiver]
    SVReceiver_stopThreadless.restype = None

# /usr/local/include/libiec61850/sv_subscriber.h: 247
if _libs["/usr/local/lib/libiec61850.so"].has("SVReceiver_tick", "cdecl"):
    SVReceiver_tick = _libs["/usr/local/lib/libiec61850.so"].get("SVReceiver_tick", "cdecl")
    SVReceiver_tick.argtypes = [SVReceiver]
    SVReceiver_tick.restype = c_bool

# /usr/local/include/libiec61850/sv_subscriber.h: 259
if _libs["/usr/local/lib/libiec61850.so"].has("SVSubscriber_create", "cdecl"):
    SVSubscriber_create = _libs["/usr/local/lib/libiec61850.so"].get("SVSubscriber_create", "cdecl")
    SVSubscriber_create.argtypes = [POINTER(uint8_t), uint16_t]
    SVSubscriber_create.restype = SVSubscriber

# /usr/local/include/libiec61850/sv_subscriber.h: 273
if _libs["/usr/local/lib/libiec61850.so"].has("SVSubscriber_setListener", "cdecl"):
    SVSubscriber_setListener = _libs["/usr/local/lib/libiec61850.so"].get("SVSubscriber_setListener", "cdecl")
    SVSubscriber_setListener.argtypes = [SVSubscriber, SVUpdateListener, POINTER(None)]
    SVSubscriber_setListener.restype = None

# /usr/local/include/libiec61850/sv_subscriber.h: 276
if _libs["/usr/local/lib/libiec61850.so"].has("SVSubscriber_destroy", "cdecl"):
    SVSubscriber_destroy = _libs["/usr/local/lib/libiec61850.so"].get("SVSubscriber_destroy", "cdecl")
    SVSubscriber_destroy.argtypes = [SVSubscriber]
    SVSubscriber_destroy.restype = None

# /usr/local/include/libiec61850/sv_subscriber.h: 296
if _libs["/usr/local/lib/libiec61850.so"].has("SVSubscriber_ASDU_getSmpCnt", "cdecl"):
    SVSubscriber_ASDU_getSmpCnt = _libs["/usr/local/lib/libiec61850.so"].get("SVSubscriber_ASDU_getSmpCnt", "cdecl")
    SVSubscriber_ASDU_getSmpCnt.argtypes = [SVSubscriber_ASDU]
    SVSubscriber_ASDU_getSmpCnt.restype = uint16_t

# /usr/local/include/libiec61850/sv_subscriber.h: 303
if _libs["/usr/local/lib/libiec61850.so"].has("SVSubscriber_ASDU_getSvId", "cdecl"):
    SVSubscriber_ASDU_getSvId = _libs["/usr/local/lib/libiec61850.so"].get("SVSubscriber_ASDU_getSvId", "cdecl")
    SVSubscriber_ASDU_getSvId.argtypes = [SVSubscriber_ASDU]
    SVSubscriber_ASDU_getSvId.restype = c_char_p

# /usr/local/include/libiec61850/sv_subscriber.h: 311
if _libs["/usr/local/lib/libiec61850.so"].has("SVSubscriber_ASDU_getDatSet", "cdecl"):
    SVSubscriber_ASDU_getDatSet = _libs["/usr/local/lib/libiec61850.so"].get("SVSubscriber_ASDU_getDatSet", "cdecl")
    SVSubscriber_ASDU_getDatSet.argtypes = [SVSubscriber_ASDU]
    SVSubscriber_ASDU_getDatSet.restype = c_char_p

# /usr/local/include/libiec61850/sv_subscriber.h: 320
if _libs["/usr/local/lib/libiec61850.so"].has("SVSubscriber_ASDU_getConfRev", "cdecl"):
    SVSubscriber_ASDU_getConfRev = _libs["/usr/local/lib/libiec61850.so"].get("SVSubscriber_ASDU_getConfRev", "cdecl")
    SVSubscriber_ASDU_getConfRev.argtypes = [SVSubscriber_ASDU]
    SVSubscriber_ASDU_getConfRev.restype = uint32_t

# /usr/local/include/libiec61850/sv_subscriber.h: 328
if _libs["/usr/local/lib/libiec61850.so"].has("SVSubscriber_ASDU_getSmpMod", "cdecl"):
    SVSubscriber_ASDU_getSmpMod = _libs["/usr/local/lib/libiec61850.so"].get("SVSubscriber_ASDU_getSmpMod", "cdecl")
    SVSubscriber_ASDU_getSmpMod.argtypes = [SVSubscriber_ASDU]
    SVSubscriber_ASDU_getSmpMod.restype = uint8_t

# /usr/local/include/libiec61850/sv_subscriber.h: 336
if _libs["/usr/local/lib/libiec61850.so"].has("SVSubscriber_ASDU_getSmpRate", "cdecl"):
    SVSubscriber_ASDU_getSmpRate = _libs["/usr/local/lib/libiec61850.so"].get("SVSubscriber_ASDU_getSmpRate", "cdecl")
    SVSubscriber_ASDU_getSmpRate.argtypes = [SVSubscriber_ASDU]
    SVSubscriber_ASDU_getSmpRate.restype = uint16_t

# /usr/local/include/libiec61850/sv_subscriber.h: 346
if _libs["/usr/local/lib/libiec61850.so"].has("SVSubscriber_ASDU_hasDatSet", "cdecl"):
    SVSubscriber_ASDU_hasDatSet = _libs["/usr/local/lib/libiec61850.so"].get("SVSubscriber_ASDU_hasDatSet", "cdecl")
    SVSubscriber_ASDU_hasDatSet.argtypes = [SVSubscriber_ASDU]
    SVSubscriber_ASDU_hasDatSet.restype = c_bool

# /usr/local/include/libiec61850/sv_subscriber.h: 356
if _libs["/usr/local/lib/libiec61850.so"].has("SVSubscriber_ASDU_hasRefrTm", "cdecl"):
    SVSubscriber_ASDU_hasRefrTm = _libs["/usr/local/lib/libiec61850.so"].get("SVSubscriber_ASDU_hasRefrTm", "cdecl")
    SVSubscriber_ASDU_hasRefrTm.argtypes = [SVSubscriber_ASDU]
    SVSubscriber_ASDU_hasRefrTm.restype = c_bool

# /usr/local/include/libiec61850/sv_subscriber.h: 366
if _libs["/usr/local/lib/libiec61850.so"].has("SVSubscriber_ASDU_hasSmpMod", "cdecl"):
    SVSubscriber_ASDU_hasSmpMod = _libs["/usr/local/lib/libiec61850.so"].get("SVSubscriber_ASDU_hasSmpMod", "cdecl")
    SVSubscriber_ASDU_hasSmpMod.argtypes = [SVSubscriber_ASDU]
    SVSubscriber_ASDU_hasSmpMod.restype = c_bool

# /usr/local/include/libiec61850/sv_subscriber.h: 376
if _libs["/usr/local/lib/libiec61850.so"].has("SVSubscriber_ASDU_hasSmpRate", "cdecl"):
    SVSubscriber_ASDU_hasSmpRate = _libs["/usr/local/lib/libiec61850.so"].get("SVSubscriber_ASDU_hasSmpRate", "cdecl")
    SVSubscriber_ASDU_hasSmpRate.argtypes = [SVSubscriber_ASDU]
    SVSubscriber_ASDU_hasSmpRate.restype = c_bool

# /usr/local/include/libiec61850/sv_subscriber.h: 386
if _libs["/usr/local/lib/libiec61850.so"].has("SVSubscriber_ASDU_getRefrTmAsMs", "cdecl"):
    SVSubscriber_ASDU_getRefrTmAsMs = _libs["/usr/local/lib/libiec61850.so"].get("SVSubscriber_ASDU_getRefrTmAsMs", "cdecl")
    SVSubscriber_ASDU_getRefrTmAsMs.argtypes = [SVSubscriber_ASDU]
    SVSubscriber_ASDU_getRefrTmAsMs.restype = uint64_t

# /usr/local/include/libiec61850/sv_subscriber.h: 396
if _libs["/usr/local/lib/libiec61850.so"].has("SVSubscriber_ASDU_getRefrTmAsNs", "cdecl"):
    SVSubscriber_ASDU_getRefrTmAsNs = _libs["/usr/local/lib/libiec61850.so"].get("SVSubscriber_ASDU_getRefrTmAsNs", "cdecl")
    SVSubscriber_ASDU_getRefrTmAsNs.argtypes = [SVSubscriber_ASDU]
    SVSubscriber_ASDU_getRefrTmAsNs.restype = nsSinceEpoch

# /usr/local/include/libiec61850/sv_subscriber.h: 407
if _libs["/usr/local/lib/libiec61850.so"].has("SVSubscriber_ASDU_getINT8", "cdecl"):
    SVSubscriber_ASDU_getINT8 = _libs["/usr/local/lib/libiec61850.so"].get("SVSubscriber_ASDU_getINT8", "cdecl")
    SVSubscriber_ASDU_getINT8.argtypes = [SVSubscriber_ASDU, c_int]
    SVSubscriber_ASDU_getINT8.restype = c_int8

# /usr/local/include/libiec61850/sv_subscriber.h: 418
if _libs["/usr/local/lib/libiec61850.so"].has("SVSubscriber_ASDU_getINT16", "cdecl"):
    SVSubscriber_ASDU_getINT16 = _libs["/usr/local/lib/libiec61850.so"].get("SVSubscriber_ASDU_getINT16", "cdecl")
    SVSubscriber_ASDU_getINT16.argtypes = [SVSubscriber_ASDU, c_int]
    SVSubscriber_ASDU_getINT16.restype = c_int16

# /usr/local/include/libiec61850/sv_subscriber.h: 429
if _libs["/usr/local/lib/libiec61850.so"].has("SVSubscriber_ASDU_getINT32", "cdecl"):
    SVSubscriber_ASDU_getINT32 = _libs["/usr/local/lib/libiec61850.so"].get("SVSubscriber_ASDU_getINT32", "cdecl")
    SVSubscriber_ASDU_getINT32.argtypes = [SVSubscriber_ASDU, c_int]
    SVSubscriber_ASDU_getINT32.restype = c_int32

# /usr/local/include/libiec61850/sv_subscriber.h: 440
if _libs["/usr/local/lib/libiec61850.so"].has("SVSubscriber_ASDU_getINT64", "cdecl"):
    SVSubscriber_ASDU_getINT64 = _libs["/usr/local/lib/libiec61850.so"].get("SVSubscriber_ASDU_getINT64", "cdecl")
    SVSubscriber_ASDU_getINT64.argtypes = [SVSubscriber_ASDU, c_int]
    SVSubscriber_ASDU_getINT64.restype = c_int64

# /usr/local/include/libiec61850/sv_subscriber.h: 451
if _libs["/usr/local/lib/libiec61850.so"].has("SVSubscriber_ASDU_getINT8U", "cdecl"):
    SVSubscriber_ASDU_getINT8U = _libs["/usr/local/lib/libiec61850.so"].get("SVSubscriber_ASDU_getINT8U", "cdecl")
    SVSubscriber_ASDU_getINT8U.argtypes = [SVSubscriber_ASDU, c_int]
    SVSubscriber_ASDU_getINT8U.restype = uint8_t

# /usr/local/include/libiec61850/sv_subscriber.h: 462
if _libs["/usr/local/lib/libiec61850.so"].has("SVSubscriber_ASDU_getINT16U", "cdecl"):
    SVSubscriber_ASDU_getINT16U = _libs["/usr/local/lib/libiec61850.so"].get("SVSubscriber_ASDU_getINT16U", "cdecl")
    SVSubscriber_ASDU_getINT16U.argtypes = [SVSubscriber_ASDU, c_int]
    SVSubscriber_ASDU_getINT16U.restype = uint16_t

# /usr/local/include/libiec61850/sv_subscriber.h: 473
if _libs["/usr/local/lib/libiec61850.so"].has("SVSubscriber_ASDU_getINT32U", "cdecl"):
    SVSubscriber_ASDU_getINT32U = _libs["/usr/local/lib/libiec61850.so"].get("SVSubscriber_ASDU_getINT32U", "cdecl")
    SVSubscriber_ASDU_getINT32U.argtypes = [SVSubscriber_ASDU, c_int]
    SVSubscriber_ASDU_getINT32U.restype = uint32_t

# /usr/local/include/libiec61850/sv_subscriber.h: 484
if _libs["/usr/local/lib/libiec61850.so"].has("SVSubscriber_ASDU_getINT64U", "cdecl"):
    SVSubscriber_ASDU_getINT64U = _libs["/usr/local/lib/libiec61850.so"].get("SVSubscriber_ASDU_getINT64U", "cdecl")
    SVSubscriber_ASDU_getINT64U.argtypes = [SVSubscriber_ASDU, c_int]
    SVSubscriber_ASDU_getINT64U.restype = uint64_t

# /usr/local/include/libiec61850/sv_subscriber.h: 495
if _libs["/usr/local/lib/libiec61850.so"].has("SVSubscriber_ASDU_getFLOAT32", "cdecl"):
    SVSubscriber_ASDU_getFLOAT32 = _libs["/usr/local/lib/libiec61850.so"].get("SVSubscriber_ASDU_getFLOAT32", "cdecl")
    SVSubscriber_ASDU_getFLOAT32.argtypes = [SVSubscriber_ASDU, c_int]
    SVSubscriber_ASDU_getFLOAT32.restype = c_float

# /usr/local/include/libiec61850/sv_subscriber.h: 506
if _libs["/usr/local/lib/libiec61850.so"].has("SVSubscriber_ASDU_getFLOAT64", "cdecl"):
    SVSubscriber_ASDU_getFLOAT64 = _libs["/usr/local/lib/libiec61850.so"].get("SVSubscriber_ASDU_getFLOAT64", "cdecl")
    SVSubscriber_ASDU_getFLOAT64.argtypes = [SVSubscriber_ASDU, c_int]
    SVSubscriber_ASDU_getFLOAT64.restype = c_double

# /usr/local/include/libiec61850/sv_subscriber.h: 517
if _libs["/usr/local/lib/libiec61850.so"].has("SVSubscriber_ASDU_getTimestamp", "cdecl"):
    SVSubscriber_ASDU_getTimestamp = _libs["/usr/local/lib/libiec61850.so"].get("SVSubscriber_ASDU_getTimestamp", "cdecl")
    SVSubscriber_ASDU_getTimestamp.argtypes = [SVSubscriber_ASDU, c_int]
    SVSubscriber_ASDU_getTimestamp.restype = Timestamp

# /usr/local/include/libiec61850/sv_subscriber.h: 530
if _libs["/usr/local/lib/libiec61850.so"].has("SVSubscriber_ASDU_getQuality", "cdecl"):
    SVSubscriber_ASDU_getQuality = _libs["/usr/local/lib/libiec61850.so"].get("SVSubscriber_ASDU_getQuality", "cdecl")
    SVSubscriber_ASDU_getQuality.argtypes = [SVSubscriber_ASDU, c_int]
    SVSubscriber_ASDU_getQuality.restype = Quality

# /usr/local/include/libiec61850/sv_subscriber.h: 540
if _libs["/usr/local/lib/libiec61850.so"].has("SVSubscriber_ASDU_getDataSize", "cdecl"):
    SVSubscriber_ASDU_getDataSize = _libs["/usr/local/lib/libiec61850.so"].get("SVSubscriber_ASDU_getDataSize", "cdecl")
    SVSubscriber_ASDU_getDataSize.argtypes = [SVSubscriber_ASDU]
    SVSubscriber_ASDU_getDataSize.restype = c_int

# /usr/local/include/libiec61850/sv_subscriber.h: 550
if _libs["/usr/local/lib/libiec61850.so"].has("SVSubscriber_ASDU_getSmpSynch", "cdecl"):
    SVSubscriber_ASDU_getSmpSynch = _libs["/usr/local/lib/libiec61850.so"].get("SVSubscriber_ASDU_getSmpSynch", "cdecl")
    SVSubscriber_ASDU_getSmpSynch.argtypes = [SVSubscriber_ASDU]
    SVSubscriber_ASDU_getSmpSynch.restype = uint8_t

# /usr/local/include/libiec61850/sv_subscriber.h: 567
class struct_sSVSubscriberASDU(Structure):
    pass

SVClientASDU = POINTER(struct_sSVSubscriberASDU)# /usr/local/include/libiec61850/sv_subscriber.h: 567

# /usr/local/include/libiec61850/sv_subscriber.h: 570
if _libs["/usr/local/lib/libiec61850.so"].has("SVClientASDU_getSmpCnt", "cdecl"):
    SVClientASDU_getSmpCnt = _libs["/usr/local/lib/libiec61850.so"].get("SVClientASDU_getSmpCnt", "cdecl")
    SVClientASDU_getSmpCnt.argtypes = [SVSubscriber_ASDU]
    SVClientASDU_getSmpCnt.restype = uint16_t

# /usr/local/include/libiec61850/sv_subscriber.h: 572
if _libs["/usr/local/lib/libiec61850.so"].has("SVClientASDU_getSvId", "cdecl"):
    SVClientASDU_getSvId = _libs["/usr/local/lib/libiec61850.so"].get("SVClientASDU_getSvId", "cdecl")
    SVClientASDU_getSvId.argtypes = [SVSubscriber_ASDU]
    SVClientASDU_getSvId.restype = c_char_p

# /usr/local/include/libiec61850/sv_subscriber.h: 576
if _libs["/usr/local/lib/libiec61850.so"].has("SVClientASDU_getConfRev", "cdecl"):
    SVClientASDU_getConfRev = _libs["/usr/local/lib/libiec61850.so"].get("SVClientASDU_getConfRev", "cdecl")
    SVClientASDU_getConfRev.argtypes = [SVSubscriber_ASDU]
    SVClientASDU_getConfRev.restype = uint32_t

# /usr/local/include/libiec61850/sv_subscriber.h: 579
if _libs["/usr/local/lib/libiec61850.so"].has("SVClientASDU_hasRefrTm", "cdecl"):
    SVClientASDU_hasRefrTm = _libs["/usr/local/lib/libiec61850.so"].get("SVClientASDU_hasRefrTm", "cdecl")
    SVClientASDU_hasRefrTm.argtypes = [SVSubscriber_ASDU]
    SVClientASDU_hasRefrTm.restype = c_bool

# /usr/local/include/libiec61850/sv_subscriber.h: 582
if _libs["/usr/local/lib/libiec61850.so"].has("SVClientASDU_getRefrTmAsMs", "cdecl"):
    SVClientASDU_getRefrTmAsMs = _libs["/usr/local/lib/libiec61850.so"].get("SVClientASDU_getRefrTmAsMs", "cdecl")
    SVClientASDU_getRefrTmAsMs.argtypes = [SVSubscriber_ASDU]
    SVClientASDU_getRefrTmAsMs.restype = uint64_t

# /usr/local/include/libiec61850/sv_subscriber.h: 585
if _libs["/usr/local/lib/libiec61850.so"].has("SVClientASDU_getINT8", "cdecl"):
    SVClientASDU_getINT8 = _libs["/usr/local/lib/libiec61850.so"].get("SVClientASDU_getINT8", "cdecl")
    SVClientASDU_getINT8.argtypes = [SVSubscriber_ASDU, c_int]
    SVClientASDU_getINT8.restype = c_int8

# /usr/local/include/libiec61850/sv_subscriber.h: 588
if _libs["/usr/local/lib/libiec61850.so"].has("SVClientASDU_getINT16", "cdecl"):
    SVClientASDU_getINT16 = _libs["/usr/local/lib/libiec61850.so"].get("SVClientASDU_getINT16", "cdecl")
    SVClientASDU_getINT16.argtypes = [SVSubscriber_ASDU, c_int]
    SVClientASDU_getINT16.restype = c_int16

# /usr/local/include/libiec61850/sv_subscriber.h: 591
if _libs["/usr/local/lib/libiec61850.so"].has("SVClientASDU_getINT32", "cdecl"):
    SVClientASDU_getINT32 = _libs["/usr/local/lib/libiec61850.so"].get("SVClientASDU_getINT32", "cdecl")
    SVClientASDU_getINT32.argtypes = [SVSubscriber_ASDU, c_int]
    SVClientASDU_getINT32.restype = c_int32

# /usr/local/include/libiec61850/sv_subscriber.h: 594
if _libs["/usr/local/lib/libiec61850.so"].has("SVClientASDU_getINT64", "cdecl"):
    SVClientASDU_getINT64 = _libs["/usr/local/lib/libiec61850.so"].get("SVClientASDU_getINT64", "cdecl")
    SVClientASDU_getINT64.argtypes = [SVSubscriber_ASDU, c_int]
    SVClientASDU_getINT64.restype = c_int64

# /usr/local/include/libiec61850/sv_subscriber.h: 597
if _libs["/usr/local/lib/libiec61850.so"].has("SVClientASDU_getINT8U", "cdecl"):
    SVClientASDU_getINT8U = _libs["/usr/local/lib/libiec61850.so"].get("SVClientASDU_getINT8U", "cdecl")
    SVClientASDU_getINT8U.argtypes = [SVSubscriber_ASDU, c_int]
    SVClientASDU_getINT8U.restype = uint8_t

# /usr/local/include/libiec61850/sv_subscriber.h: 600
if _libs["/usr/local/lib/libiec61850.so"].has("SVClientASDU_getINT16U", "cdecl"):
    SVClientASDU_getINT16U = _libs["/usr/local/lib/libiec61850.so"].get("SVClientASDU_getINT16U", "cdecl")
    SVClientASDU_getINT16U.argtypes = [SVSubscriber_ASDU, c_int]
    SVClientASDU_getINT16U.restype = uint16_t

# /usr/local/include/libiec61850/sv_subscriber.h: 603
if _libs["/usr/local/lib/libiec61850.so"].has("SVClientASDU_getINT32U", "cdecl"):
    SVClientASDU_getINT32U = _libs["/usr/local/lib/libiec61850.so"].get("SVClientASDU_getINT32U", "cdecl")
    SVClientASDU_getINT32U.argtypes = [SVSubscriber_ASDU, c_int]
    SVClientASDU_getINT32U.restype = uint32_t

# /usr/local/include/libiec61850/sv_subscriber.h: 606
if _libs["/usr/local/lib/libiec61850.so"].has("SVClientASDU_getINT64U", "cdecl"):
    SVClientASDU_getINT64U = _libs["/usr/local/lib/libiec61850.so"].get("SVClientASDU_getINT64U", "cdecl")
    SVClientASDU_getINT64U.argtypes = [SVSubscriber_ASDU, c_int]
    SVClientASDU_getINT64U.restype = uint64_t

# /usr/local/include/libiec61850/sv_subscriber.h: 609
if _libs["/usr/local/lib/libiec61850.so"].has("SVClientASDU_getFLOAT32", "cdecl"):
    SVClientASDU_getFLOAT32 = _libs["/usr/local/lib/libiec61850.so"].get("SVClientASDU_getFLOAT32", "cdecl")
    SVClientASDU_getFLOAT32.argtypes = [SVSubscriber_ASDU, c_int]
    SVClientASDU_getFLOAT32.restype = c_float

# /usr/local/include/libiec61850/sv_subscriber.h: 612
if _libs["/usr/local/lib/libiec61850.so"].has("SVClientASDU_getFLOAT64", "cdecl"):
    SVClientASDU_getFLOAT64 = _libs["/usr/local/lib/libiec61850.so"].get("SVClientASDU_getFLOAT64", "cdecl")
    SVClientASDU_getFLOAT64.argtypes = [SVSubscriber_ASDU, c_int]
    SVClientASDU_getFLOAT64.restype = c_double

# /usr/local/include/libiec61850/sv_subscriber.h: 615
if _libs["/usr/local/lib/libiec61850.so"].has("SVClientASDU_getDataSize", "cdecl"):
    SVClientASDU_getDataSize = _libs["/usr/local/lib/libiec61850.so"].get("SVClientASDU_getDataSize", "cdecl")
    SVClientASDU_getDataSize.argtypes = [SVSubscriber_ASDU]
    SVClientASDU_getDataSize.restype = c_int

# /usr/local/include/libiec61850/sv_publisher.h: 62
class struct_sSVPublisher(Structure):
    pass

SVPublisher = POINTER(struct_sSVPublisher)# /usr/local/include/libiec61850/sv_publisher.h: 62

# /usr/local/include/libiec61850/sv_publisher.h: 67
class struct_sSVPublisher_ASDU(Structure):
    pass

SVPublisher_ASDU = POINTER(struct_sSVPublisher_ASDU)# /usr/local/include/libiec61850/sv_publisher.h: 67

# /usr/local/include/libiec61850/sv_publisher.h: 80
if _libs["/usr/local/lib/libiec61850.so"].has("SVPublisher_create", "cdecl"):
    SVPublisher_create = _libs["/usr/local/lib/libiec61850.so"].get("SVPublisher_create", "cdecl")
    SVPublisher_create.argtypes = [POINTER(CommParameters), String]
    SVPublisher_create.restype = SVPublisher

# /usr/local/include/libiec61850/sv_publisher.h: 91
if _libs["/usr/local/lib/libiec61850.so"].has("SVPublisher_createEx", "cdecl"):
    SVPublisher_createEx = _libs["/usr/local/lib/libiec61850.so"].get("SVPublisher_createEx", "cdecl")
    SVPublisher_createEx.argtypes = [POINTER(CommParameters), String, c_bool]
    SVPublisher_createEx.restype = SVPublisher

# /usr/local/include/libiec61850/sv_publisher.h: 102
if _libs["/usr/local/lib/libiec61850.so"].has("SVPublisher_addASDU", "cdecl"):
    SVPublisher_addASDU = _libs["/usr/local/lib/libiec61850.so"].get("SVPublisher_addASDU", "cdecl")
    SVPublisher_addASDU.argtypes = [SVPublisher, String, String, uint32_t]
    SVPublisher_addASDU.restype = SVPublisher_ASDU

# /usr/local/include/libiec61850/sv_publisher.h: 112
if _libs["/usr/local/lib/libiec61850.so"].has("SVPublisher_setupComplete", "cdecl"):
    SVPublisher_setupComplete = _libs["/usr/local/lib/libiec61850.so"].get("SVPublisher_setupComplete", "cdecl")
    SVPublisher_setupComplete.argtypes = [SVPublisher]
    SVPublisher_setupComplete.restype = None

# /usr/local/include/libiec61850/sv_publisher.h: 120
if _libs["/usr/local/lib/libiec61850.so"].has("SVPublisher_publish", "cdecl"):
    SVPublisher_publish = _libs["/usr/local/lib/libiec61850.so"].get("SVPublisher_publish", "cdecl")
    SVPublisher_publish.argtypes = [SVPublisher]
    SVPublisher_publish.restype = None

# /usr/local/include/libiec61850/sv_publisher.h: 128
if _libs["/usr/local/lib/libiec61850.so"].has("SVPublisher_destroy", "cdecl"):
    SVPublisher_destroy = _libs["/usr/local/lib/libiec61850.so"].get("SVPublisher_destroy", "cdecl")
    SVPublisher_destroy.argtypes = [SVPublisher]
    SVPublisher_destroy.restype = None

# /usr/local/include/libiec61850/sv_publisher.h: 144
if _libs["/usr/local/lib/libiec61850.so"].has("SVPublisher_ASDU_resetBuffer", "cdecl"):
    SVPublisher_ASDU_resetBuffer = _libs["/usr/local/lib/libiec61850.so"].get("SVPublisher_ASDU_resetBuffer", "cdecl")
    SVPublisher_ASDU_resetBuffer.argtypes = [SVPublisher_ASDU]
    SVPublisher_ASDU_resetBuffer.restype = None

# /usr/local/include/libiec61850/sv_publisher.h: 153
if _libs["/usr/local/lib/libiec61850.so"].has("SVPublisher_ASDU_addINT8", "cdecl"):
    SVPublisher_ASDU_addINT8 = _libs["/usr/local/lib/libiec61850.so"].get("SVPublisher_ASDU_addINT8", "cdecl")
    SVPublisher_ASDU_addINT8.argtypes = [SVPublisher_ASDU]
    SVPublisher_ASDU_addINT8.restype = c_int

# /usr/local/include/libiec61850/sv_publisher.h: 163
if _libs["/usr/local/lib/libiec61850.so"].has("SVPublisher_ASDU_setINT8", "cdecl"):
    SVPublisher_ASDU_setINT8 = _libs["/usr/local/lib/libiec61850.so"].get("SVPublisher_ASDU_setINT8", "cdecl")
    SVPublisher_ASDU_setINT8.argtypes = [SVPublisher_ASDU, c_int, c_int8]
    SVPublisher_ASDU_setINT8.restype = None

# /usr/local/include/libiec61850/sv_publisher.h: 172
if _libs["/usr/local/lib/libiec61850.so"].has("SVPublisher_ASDU_addINT32", "cdecl"):
    SVPublisher_ASDU_addINT32 = _libs["/usr/local/lib/libiec61850.so"].get("SVPublisher_ASDU_addINT32", "cdecl")
    SVPublisher_ASDU_addINT32.argtypes = [SVPublisher_ASDU]
    SVPublisher_ASDU_addINT32.restype = c_int

# /usr/local/include/libiec61850/sv_publisher.h: 182
if _libs["/usr/local/lib/libiec61850.so"].has("SVPublisher_ASDU_setINT32", "cdecl"):
    SVPublisher_ASDU_setINT32 = _libs["/usr/local/lib/libiec61850.so"].get("SVPublisher_ASDU_setINT32", "cdecl")
    SVPublisher_ASDU_setINT32.argtypes = [SVPublisher_ASDU, c_int, c_int32]
    SVPublisher_ASDU_setINT32.restype = None

# /usr/local/include/libiec61850/sv_publisher.h: 191
if _libs["/usr/local/lib/libiec61850.so"].has("SVPublisher_ASDU_addINT64", "cdecl"):
    SVPublisher_ASDU_addINT64 = _libs["/usr/local/lib/libiec61850.so"].get("SVPublisher_ASDU_addINT64", "cdecl")
    SVPublisher_ASDU_addINT64.argtypes = [SVPublisher_ASDU]
    SVPublisher_ASDU_addINT64.restype = c_int

# /usr/local/include/libiec61850/sv_publisher.h: 201
if _libs["/usr/local/lib/libiec61850.so"].has("SVPublisher_ASDU_setINT64", "cdecl"):
    SVPublisher_ASDU_setINT64 = _libs["/usr/local/lib/libiec61850.so"].get("SVPublisher_ASDU_setINT64", "cdecl")
    SVPublisher_ASDU_setINT64.argtypes = [SVPublisher_ASDU, c_int, c_int64]
    SVPublisher_ASDU_setINT64.restype = None

# /usr/local/include/libiec61850/sv_publisher.h: 210
if _libs["/usr/local/lib/libiec61850.so"].has("SVPublisher_ASDU_addFLOAT", "cdecl"):
    SVPublisher_ASDU_addFLOAT = _libs["/usr/local/lib/libiec61850.so"].get("SVPublisher_ASDU_addFLOAT", "cdecl")
    SVPublisher_ASDU_addFLOAT.argtypes = [SVPublisher_ASDU]
    SVPublisher_ASDU_addFLOAT.restype = c_int

# /usr/local/include/libiec61850/sv_publisher.h: 220
if _libs["/usr/local/lib/libiec61850.so"].has("SVPublisher_ASDU_setFLOAT", "cdecl"):
    SVPublisher_ASDU_setFLOAT = _libs["/usr/local/lib/libiec61850.so"].get("SVPublisher_ASDU_setFLOAT", "cdecl")
    SVPublisher_ASDU_setFLOAT.argtypes = [SVPublisher_ASDU, c_int, c_float]
    SVPublisher_ASDU_setFLOAT.restype = None

# /usr/local/include/libiec61850/sv_publisher.h: 229
if _libs["/usr/local/lib/libiec61850.so"].has("SVPublisher_ASDU_addFLOAT64", "cdecl"):
    SVPublisher_ASDU_addFLOAT64 = _libs["/usr/local/lib/libiec61850.so"].get("SVPublisher_ASDU_addFLOAT64", "cdecl")
    SVPublisher_ASDU_addFLOAT64.argtypes = [SVPublisher_ASDU]
    SVPublisher_ASDU_addFLOAT64.restype = c_int

# /usr/local/include/libiec61850/sv_publisher.h: 239
if _libs["/usr/local/lib/libiec61850.so"].has("SVPublisher_ASDU_setFLOAT64", "cdecl"):
    SVPublisher_ASDU_setFLOAT64 = _libs["/usr/local/lib/libiec61850.so"].get("SVPublisher_ASDU_setFLOAT64", "cdecl")
    SVPublisher_ASDU_setFLOAT64.argtypes = [SVPublisher_ASDU, c_int, c_double]
    SVPublisher_ASDU_setFLOAT64.restype = None

# /usr/local/include/libiec61850/sv_publisher.h: 248
if _libs["/usr/local/lib/libiec61850.so"].has("SVPublisher_ASDU_addTimestamp", "cdecl"):
    SVPublisher_ASDU_addTimestamp = _libs["/usr/local/lib/libiec61850.so"].get("SVPublisher_ASDU_addTimestamp", "cdecl")
    SVPublisher_ASDU_addTimestamp.argtypes = [SVPublisher_ASDU]
    SVPublisher_ASDU_addTimestamp.restype = c_int

# /usr/local/include/libiec61850/sv_publisher.h: 258
if _libs["/usr/local/lib/libiec61850.so"].has("SVPublisher_ASDU_setTimestamp", "cdecl"):
    SVPublisher_ASDU_setTimestamp = _libs["/usr/local/lib/libiec61850.so"].get("SVPublisher_ASDU_setTimestamp", "cdecl")
    SVPublisher_ASDU_setTimestamp.argtypes = [SVPublisher_ASDU, c_int, Timestamp]
    SVPublisher_ASDU_setTimestamp.restype = None

# /usr/local/include/libiec61850/sv_publisher.h: 269
if _libs["/usr/local/lib/libiec61850.so"].has("SVPublisher_ASDU_addQuality", "cdecl"):
    SVPublisher_ASDU_addQuality = _libs["/usr/local/lib/libiec61850.so"].get("SVPublisher_ASDU_addQuality", "cdecl")
    SVPublisher_ASDU_addQuality.argtypes = [SVPublisher_ASDU]
    SVPublisher_ASDU_addQuality.restype = c_int

# /usr/local/include/libiec61850/sv_publisher.h: 279
if _libs["/usr/local/lib/libiec61850.so"].has("SVPublisher_ASDU_setQuality", "cdecl"):
    SVPublisher_ASDU_setQuality = _libs["/usr/local/lib/libiec61850.so"].get("SVPublisher_ASDU_setQuality", "cdecl")
    SVPublisher_ASDU_setQuality.argtypes = [SVPublisher_ASDU, c_int, Quality]
    SVPublisher_ASDU_setQuality.restype = None

# /usr/local/include/libiec61850/sv_publisher.h: 288
if _libs["/usr/local/lib/libiec61850.so"].has("SVPublisher_ASDU_setSmpCnt", "cdecl"):
    SVPublisher_ASDU_setSmpCnt = _libs["/usr/local/lib/libiec61850.so"].get("SVPublisher_ASDU_setSmpCnt", "cdecl")
    SVPublisher_ASDU_setSmpCnt.argtypes = [SVPublisher_ASDU, uint16_t]
    SVPublisher_ASDU_setSmpCnt.restype = None

# /usr/local/include/libiec61850/sv_publisher.h: 296
if _libs["/usr/local/lib/libiec61850.so"].has("SVPublisher_ASDU_getSmpCnt", "cdecl"):
    SVPublisher_ASDU_getSmpCnt = _libs["/usr/local/lib/libiec61850.so"].get("SVPublisher_ASDU_getSmpCnt", "cdecl")
    SVPublisher_ASDU_getSmpCnt.argtypes = [SVPublisher_ASDU]
    SVPublisher_ASDU_getSmpCnt.restype = uint16_t

# /usr/local/include/libiec61850/sv_publisher.h: 308
if _libs["/usr/local/lib/libiec61850.so"].has("SVPublisher_ASDU_increaseSmpCnt", "cdecl"):
    SVPublisher_ASDU_increaseSmpCnt = _libs["/usr/local/lib/libiec61850.so"].get("SVPublisher_ASDU_increaseSmpCnt", "cdecl")
    SVPublisher_ASDU_increaseSmpCnt.argtypes = [SVPublisher_ASDU]
    SVPublisher_ASDU_increaseSmpCnt.restype = None

# /usr/local/include/libiec61850/sv_publisher.h: 318
if _libs["/usr/local/lib/libiec61850.so"].has("SVPublisher_ASDU_setSmpCntWrap", "cdecl"):
    SVPublisher_ASDU_setSmpCntWrap = _libs["/usr/local/lib/libiec61850.so"].get("SVPublisher_ASDU_setSmpCntWrap", "cdecl")
    SVPublisher_ASDU_setSmpCntWrap.argtypes = [SVPublisher_ASDU, uint16_t]
    SVPublisher_ASDU_setSmpCntWrap.restype = None

# /usr/local/include/libiec61850/sv_publisher.h: 328
if _libs["/usr/local/lib/libiec61850.so"].has("SVPublisher_ASDU_enableRefrTm", "cdecl"):
    SVPublisher_ASDU_enableRefrTm = _libs["/usr/local/lib/libiec61850.so"].get("SVPublisher_ASDU_enableRefrTm", "cdecl")
    SVPublisher_ASDU_enableRefrTm.argtypes = [SVPublisher_ASDU]
    SVPublisher_ASDU_enableRefrTm.restype = None

# /usr/local/include/libiec61850/sv_publisher.h: 337
if _libs["/usr/local/lib/libiec61850.so"].has("SVPublisher_ASDU_setRefrTmNs", "cdecl"):
    SVPublisher_ASDU_setRefrTmNs = _libs["/usr/local/lib/libiec61850.so"].get("SVPublisher_ASDU_setRefrTmNs", "cdecl")
    SVPublisher_ASDU_setRefrTmNs.argtypes = [SVPublisher_ASDU, nsSinceEpoch]
    SVPublisher_ASDU_setRefrTmNs.restype = None

# /usr/local/include/libiec61850/sv_publisher.h: 346
if _libs["/usr/local/lib/libiec61850.so"].has("SVPublisher_ASDU_setRefrTm", "cdecl"):
    SVPublisher_ASDU_setRefrTm = _libs["/usr/local/lib/libiec61850.so"].get("SVPublisher_ASDU_setRefrTm", "cdecl")
    SVPublisher_ASDU_setRefrTm.argtypes = [SVPublisher_ASDU, msSinceEpoch]
    SVPublisher_ASDU_setRefrTm.restype = None

# /usr/local/include/libiec61850/sv_publisher.h: 358
if _libs["/usr/local/lib/libiec61850.so"].has("SVPublisher_ASDU_setRefrTmByTimestamp", "cdecl"):
    SVPublisher_ASDU_setRefrTmByTimestamp = _libs["/usr/local/lib/libiec61850.so"].get("SVPublisher_ASDU_setRefrTmByTimestamp", "cdecl")
    SVPublisher_ASDU_setRefrTmByTimestamp.argtypes = [SVPublisher_ASDU, POINTER(Timestamp)]
    SVPublisher_ASDU_setRefrTmByTimestamp.restype = None

# /usr/local/include/libiec61850/sv_publisher.h: 372
if _libs["/usr/local/lib/libiec61850.so"].has("SVPublisher_ASDU_setSmpMod", "cdecl"):
    SVPublisher_ASDU_setSmpMod = _libs["/usr/local/lib/libiec61850.so"].get("SVPublisher_ASDU_setSmpMod", "cdecl")
    SVPublisher_ASDU_setSmpMod.argtypes = [SVPublisher_ASDU, uint8_t]
    SVPublisher_ASDU_setSmpMod.restype = None

# /usr/local/include/libiec61850/sv_publisher.h: 386
if _libs["/usr/local/lib/libiec61850.so"].has("SVPublisher_ASDU_setSmpRate", "cdecl"):
    SVPublisher_ASDU_setSmpRate = _libs["/usr/local/lib/libiec61850.so"].get("SVPublisher_ASDU_setSmpRate", "cdecl")
    SVPublisher_ASDU_setSmpRate.argtypes = [SVPublisher_ASDU, uint16_t]
    SVPublisher_ASDU_setSmpRate.restype = None

# /usr/local/include/libiec61850/sv_publisher.h: 403
if _libs["/usr/local/lib/libiec61850.so"].has("SVPublisher_ASDU_setSmpSynch", "cdecl"):
    SVPublisher_ASDU_setSmpSynch = _libs["/usr/local/lib/libiec61850.so"].get("SVPublisher_ASDU_setSmpSynch", "cdecl")
    SVPublisher_ASDU_setSmpSynch.argtypes = [SVPublisher_ASDU, uint16_t]
    SVPublisher_ASDU_setSmpSynch.restype = None

SampledValuesPublisher = POINTER(struct_sSVPublisher)# /usr/local/include/libiec61850/sv_publisher.h: 422

# /usr/local/include/libiec61850/sv_publisher.h: 424
class struct_sSV_ASDU(Structure):
    pass

SV_ASDU = POINTER(struct_sSV_ASDU)# /usr/local/include/libiec61850/sv_publisher.h: 424

# /usr/local/include/libiec61850/sv_publisher.h: 427
if _libs["/usr/local/lib/libiec61850.so"].has("SampledValuesPublisher_create", "cdecl"):
    SampledValuesPublisher_create = _libs["/usr/local/lib/libiec61850.so"].get("SampledValuesPublisher_create", "cdecl")
    SampledValuesPublisher_create.argtypes = [POINTER(CommParameters), String]
    SampledValuesPublisher_create.restype = SVPublisher

# /usr/local/include/libiec61850/sv_publisher.h: 430
if _libs["/usr/local/lib/libiec61850.so"].has("SampledValuesPublisher_addASDU", "cdecl"):
    SampledValuesPublisher_addASDU = _libs["/usr/local/lib/libiec61850.so"].get("SampledValuesPublisher_addASDU", "cdecl")
    SampledValuesPublisher_addASDU.argtypes = [SVPublisher, String, String, uint32_t]
    SampledValuesPublisher_addASDU.restype = SVPublisher_ASDU

# /usr/local/include/libiec61850/sv_publisher.h: 433
if _libs["/usr/local/lib/libiec61850.so"].has("SampledValuesPublisher_setupComplete", "cdecl"):
    SampledValuesPublisher_setupComplete = _libs["/usr/local/lib/libiec61850.so"].get("SampledValuesPublisher_setupComplete", "cdecl")
    SampledValuesPublisher_setupComplete.argtypes = [SVPublisher]
    SampledValuesPublisher_setupComplete.restype = None

# /usr/local/include/libiec61850/sv_publisher.h: 436
if _libs["/usr/local/lib/libiec61850.so"].has("SampledValuesPublisher_publish", "cdecl"):
    SampledValuesPublisher_publish = _libs["/usr/local/lib/libiec61850.so"].get("SampledValuesPublisher_publish", "cdecl")
    SampledValuesPublisher_publish.argtypes = [SVPublisher]
    SampledValuesPublisher_publish.restype = None

# /usr/local/include/libiec61850/sv_publisher.h: 439
if _libs["/usr/local/lib/libiec61850.so"].has("SampledValuesPublisher_destroy", "cdecl"):
    SampledValuesPublisher_destroy = _libs["/usr/local/lib/libiec61850.so"].get("SampledValuesPublisher_destroy", "cdecl")
    SampledValuesPublisher_destroy.argtypes = [SVPublisher]
    SampledValuesPublisher_destroy.restype = None

# /usr/local/include/libiec61850/sv_publisher.h: 442
if _libs["/usr/local/lib/libiec61850.so"].has("SV_ASDU_resetBuffer", "cdecl"):
    SV_ASDU_resetBuffer = _libs["/usr/local/lib/libiec61850.so"].get("SV_ASDU_resetBuffer", "cdecl")
    SV_ASDU_resetBuffer.argtypes = [SVPublisher_ASDU]
    SV_ASDU_resetBuffer.restype = None

# /usr/local/include/libiec61850/sv_publisher.h: 445
if _libs["/usr/local/lib/libiec61850.so"].has("SV_ASDU_addINT8", "cdecl"):
    SV_ASDU_addINT8 = _libs["/usr/local/lib/libiec61850.so"].get("SV_ASDU_addINT8", "cdecl")
    SV_ASDU_addINT8.argtypes = [SVPublisher_ASDU]
    SV_ASDU_addINT8.restype = c_int

# /usr/local/include/libiec61850/sv_publisher.h: 448
if _libs["/usr/local/lib/libiec61850.so"].has("SV_ASDU_setINT8", "cdecl"):
    SV_ASDU_setINT8 = _libs["/usr/local/lib/libiec61850.so"].get("SV_ASDU_setINT8", "cdecl")
    SV_ASDU_setINT8.argtypes = [SVPublisher_ASDU, c_int, c_int8]
    SV_ASDU_setINT8.restype = None

# /usr/local/include/libiec61850/sv_publisher.h: 451
if _libs["/usr/local/lib/libiec61850.so"].has("SV_ASDU_addINT32", "cdecl"):
    SV_ASDU_addINT32 = _libs["/usr/local/lib/libiec61850.so"].get("SV_ASDU_addINT32", "cdecl")
    SV_ASDU_addINT32.argtypes = [SVPublisher_ASDU]
    SV_ASDU_addINT32.restype = c_int

# /usr/local/include/libiec61850/sv_publisher.h: 454
if _libs["/usr/local/lib/libiec61850.so"].has("SV_ASDU_setINT32", "cdecl"):
    SV_ASDU_setINT32 = _libs["/usr/local/lib/libiec61850.so"].get("SV_ASDU_setINT32", "cdecl")
    SV_ASDU_setINT32.argtypes = [SVPublisher_ASDU, c_int, c_int32]
    SV_ASDU_setINT32.restype = None

# /usr/local/include/libiec61850/sv_publisher.h: 457
if _libs["/usr/local/lib/libiec61850.so"].has("SV_ASDU_addINT64", "cdecl"):
    SV_ASDU_addINT64 = _libs["/usr/local/lib/libiec61850.so"].get("SV_ASDU_addINT64", "cdecl")
    SV_ASDU_addINT64.argtypes = [SVPublisher_ASDU]
    SV_ASDU_addINT64.restype = c_int

# /usr/local/include/libiec61850/sv_publisher.h: 460
if _libs["/usr/local/lib/libiec61850.so"].has("SV_ASDU_setINT64", "cdecl"):
    SV_ASDU_setINT64 = _libs["/usr/local/lib/libiec61850.so"].get("SV_ASDU_setINT64", "cdecl")
    SV_ASDU_setINT64.argtypes = [SVPublisher_ASDU, c_int, c_int64]
    SV_ASDU_setINT64.restype = None

# /usr/local/include/libiec61850/sv_publisher.h: 463
if _libs["/usr/local/lib/libiec61850.so"].has("SV_ASDU_addFLOAT", "cdecl"):
    SV_ASDU_addFLOAT = _libs["/usr/local/lib/libiec61850.so"].get("SV_ASDU_addFLOAT", "cdecl")
    SV_ASDU_addFLOAT.argtypes = [SVPublisher_ASDU]
    SV_ASDU_addFLOAT.restype = c_int

# /usr/local/include/libiec61850/sv_publisher.h: 466
if _libs["/usr/local/lib/libiec61850.so"].has("SV_ASDU_setFLOAT", "cdecl"):
    SV_ASDU_setFLOAT = _libs["/usr/local/lib/libiec61850.so"].get("SV_ASDU_setFLOAT", "cdecl")
    SV_ASDU_setFLOAT.argtypes = [SVPublisher_ASDU, c_int, c_float]
    SV_ASDU_setFLOAT.restype = None

# /usr/local/include/libiec61850/sv_publisher.h: 469
if _libs["/usr/local/lib/libiec61850.so"].has("SV_ASDU_addFLOAT64", "cdecl"):
    SV_ASDU_addFLOAT64 = _libs["/usr/local/lib/libiec61850.so"].get("SV_ASDU_addFLOAT64", "cdecl")
    SV_ASDU_addFLOAT64.argtypes = [SVPublisher_ASDU]
    SV_ASDU_addFLOAT64.restype = c_int

# /usr/local/include/libiec61850/sv_publisher.h: 472
if _libs["/usr/local/lib/libiec61850.so"].has("SV_ASDU_setFLOAT64", "cdecl"):
    SV_ASDU_setFLOAT64 = _libs["/usr/local/lib/libiec61850.so"].get("SV_ASDU_setFLOAT64", "cdecl")
    SV_ASDU_setFLOAT64.argtypes = [SVPublisher_ASDU, c_int, c_double]
    SV_ASDU_setFLOAT64.restype = None

# /usr/local/include/libiec61850/sv_publisher.h: 475
if _libs["/usr/local/lib/libiec61850.so"].has("SV_ASDU_setSmpCnt", "cdecl"):
    SV_ASDU_setSmpCnt = _libs["/usr/local/lib/libiec61850.so"].get("SV_ASDU_setSmpCnt", "cdecl")
    SV_ASDU_setSmpCnt.argtypes = [SVPublisher_ASDU, uint16_t]
    SV_ASDU_setSmpCnt.restype = None

# /usr/local/include/libiec61850/sv_publisher.h: 478
if _libs["/usr/local/lib/libiec61850.so"].has("SV_ASDU_getSmpCnt", "cdecl"):
    SV_ASDU_getSmpCnt = _libs["/usr/local/lib/libiec61850.so"].get("SV_ASDU_getSmpCnt", "cdecl")
    SV_ASDU_getSmpCnt.argtypes = [SVPublisher_ASDU]
    SV_ASDU_getSmpCnt.restype = uint16_t

# /usr/local/include/libiec61850/sv_publisher.h: 481
if _libs["/usr/local/lib/libiec61850.so"].has("SV_ASDU_increaseSmpCnt", "cdecl"):
    SV_ASDU_increaseSmpCnt = _libs["/usr/local/lib/libiec61850.so"].get("SV_ASDU_increaseSmpCnt", "cdecl")
    SV_ASDU_increaseSmpCnt.argtypes = [SVPublisher_ASDU]
    SV_ASDU_increaseSmpCnt.restype = None

# /usr/local/include/libiec61850/sv_publisher.h: 484
if _libs["/usr/local/lib/libiec61850.so"].has("SV_ASDU_setRefrTm", "cdecl"):
    SV_ASDU_setRefrTm = _libs["/usr/local/lib/libiec61850.so"].get("SV_ASDU_setRefrTm", "cdecl")
    SV_ASDU_setRefrTm.argtypes = [SVPublisher_ASDU, uint64_t]
    SV_ASDU_setRefrTm.restype = None

# /usr/local/include/libiec61850/sv_publisher.h: 487
if _libs["/usr/local/lib/libiec61850.so"].has("SV_ASDU_setSmpMod", "cdecl"):
    SV_ASDU_setSmpMod = _libs["/usr/local/lib/libiec61850.so"].get("SV_ASDU_setSmpMod", "cdecl")
    SV_ASDU_setSmpMod.argtypes = [SVPublisher_ASDU, uint8_t]
    SV_ASDU_setSmpMod.restype = None

# /usr/local/include/libiec61850/sv_publisher.h: 490
if _libs["/usr/local/lib/libiec61850.so"].has("SV_ASDU_setSmpRate", "cdecl"):
    SV_ASDU_setSmpRate = _libs["/usr/local/lib/libiec61850.so"].get("SV_ASDU_setSmpRate", "cdecl")
    SV_ASDU_setSmpRate.argtypes = [SVPublisher_ASDU, uint16_t]
    SV_ASDU_setSmpRate.restype = None

# /usr/local/include/libiec61850/hal_filesystem.h: 34
try:
    CONFIG_SYSTEM_FILE_SEPARATOR = '/'
except:
    pass

# /usr/local/include/libiec61850/tls_config.h: 78
try:
    TLS_EVENT_CODE_ALM_ALGO_NOT_SUPPORTED = 1
except:
    pass

# /usr/local/include/libiec61850/tls_config.h: 79
try:
    TLS_EVENT_CODE_ALM_UNSECURE_COMMUNICATION = 2
except:
    pass

# /usr/local/include/libiec61850/tls_config.h: 80
try:
    TLS_EVENT_CODE_ALM_CERT_UNAVAILABLE = 3
except:
    pass

# /usr/local/include/libiec61850/tls_config.h: 81
try:
    TLS_EVENT_CODE_ALM_BAD_CERT = 4
except:
    pass

# /usr/local/include/libiec61850/tls_config.h: 82
try:
    TLS_EVENT_CODE_ALM_CERT_SIZE_EXCEEDED = 5
except:
    pass

# /usr/local/include/libiec61850/tls_config.h: 83
try:
    TLS_EVENT_CODE_ALM_CERT_VALIDATION_FAILED = 6
except:
    pass

# /usr/local/include/libiec61850/tls_config.h: 84
try:
    TLS_EVENT_CODE_ALM_CERT_REQUIRED = 7
except:
    pass

# /usr/local/include/libiec61850/tls_config.h: 85
try:
    TLS_EVENT_CODE_ALM_HANDSHAKE_FAILED_UNKNOWN_REASON = 8
except:
    pass

# /usr/local/include/libiec61850/tls_config.h: 86
try:
    TLS_EVENT_CODE_WRN_INSECURE_TLS_VERSION = 9
except:
    pass

# /usr/local/include/libiec61850/tls_config.h: 87
try:
    TLS_EVENT_CODE_INF_SESSION_RENEGOTIATION = 10
except:
    pass

# /usr/local/include/libiec61850/tls_config.h: 88
try:
    TLS_EVENT_CODE_ALM_CERT_EXPIRED = 11
except:
    pass

# /usr/local/include/libiec61850/tls_config.h: 89
try:
    TLS_EVENT_CODE_ALM_CERT_REVOKED = 12
except:
    pass

# /usr/local/include/libiec61850/tls_config.h: 90
try:
    TLS_EVENT_CODE_ALM_CERT_NOT_CONFIGURED = 13
except:
    pass

# /usr/local/include/libiec61850/tls_config.h: 91
try:
    TLS_EVENT_CODE_ALM_CERT_NOT_TRUSTED = 14
except:
    pass

# /usr/local/include/libiec61850/tls_config.h: 92
try:
    TLS_EVENT_CODE_ALM_NO_CIPHER = 15
except:
    pass

# /usr/local/include/libiec61850/iec61850_common.h: 42
try:
    IEC_61850_EDITION_1 = 0
except:
    pass

# /usr/local/include/libiec61850/iec61850_common.h: 45
try:
    IEC_61850_EDITION_2 = 1
except:
    pass

# /usr/local/include/libiec61850/iec61850_common.h: 48
try:
    IEC_61850_EDITION_2_1 = 2
except:
    pass

# /usr/local/include/libiec61850/iec61850_common.h: 97
try:
    TRG_OPT_DATA_CHANGED = 1
except:
    pass

# /usr/local/include/libiec61850/iec61850_common.h: 100
try:
    TRG_OPT_QUALITY_CHANGED = 2
except:
    pass

# /usr/local/include/libiec61850/iec61850_common.h: 103
try:
    TRG_OPT_DATA_UPDATE = 4
except:
    pass

# /usr/local/include/libiec61850/iec61850_common.h: 106
try:
    TRG_OPT_INTEGRITY = 8
except:
    pass

# /usr/local/include/libiec61850/iec61850_common.h: 109
try:
    TRG_OPT_GI = 16
except:
    pass

# /usr/local/include/libiec61850/iec61850_common.h: 112
try:
    TRG_OPT_TRANSIENT = 128
except:
    pass

# /usr/local/include/libiec61850/iec61850_common.h: 124
try:
    RPT_OPT_SEQ_NUM = 1
except:
    pass

# /usr/local/include/libiec61850/iec61850_common.h: 127
try:
    RPT_OPT_TIME_STAMP = 2
except:
    pass

# /usr/local/include/libiec61850/iec61850_common.h: 130
try:
    RPT_OPT_REASON_FOR_INCLUSION = 4
except:
    pass

# /usr/local/include/libiec61850/iec61850_common.h: 133
try:
    RPT_OPT_DATA_SET = 8
except:
    pass

# /usr/local/include/libiec61850/iec61850_common.h: 136
try:
    RPT_OPT_DATA_REFERENCE = 16
except:
    pass

# /usr/local/include/libiec61850/iec61850_common.h: 139
try:
    RPT_OPT_BUFFER_OVERFLOW = 32
except:
    pass

# /usr/local/include/libiec61850/iec61850_common.h: 142
try:
    RPT_OPT_ENTRY_ID = 64
except:
    pass

# /usr/local/include/libiec61850/iec61850_common.h: 145
try:
    RPT_OPT_CONF_REV = 128
except:
    pass

# /usr/local/include/libiec61850/iec61850_common.h: 155
try:
    CONTROL_ORCAT_NOT_SUPPORTED = 0
except:
    pass

# /usr/local/include/libiec61850/iec61850_common.h: 158
try:
    CONTROL_ORCAT_BAY_CONTROL = 1
except:
    pass

# /usr/local/include/libiec61850/iec61850_common.h: 161
try:
    CONTROL_ORCAT_STATION_CONTROL = 2
except:
    pass

# /usr/local/include/libiec61850/iec61850_common.h: 164
try:
    CONTROL_ORCAT_REMOTE_CONTROL = 3
except:
    pass

# /usr/local/include/libiec61850/iec61850_common.h: 167
try:
    CONTROL_ORCAT_AUTOMATIC_BAY = 4
except:
    pass

# /usr/local/include/libiec61850/iec61850_common.h: 170
try:
    CONTROL_ORCAT_AUTOMATIC_STATION = 5
except:
    pass

# /usr/local/include/libiec61850/iec61850_common.h: 173
try:
    CONTROL_ORCAT_AUTOMATIC_REMOTE = 6
except:
    pass

# /usr/local/include/libiec61850/iec61850_common.h: 176
try:
    CONTROL_ORCAT_MAINTENANCE = 7
except:
    pass

# /usr/local/include/libiec61850/iec61850_common.h: 179
try:
    CONTROL_ORCAT_PROCESS = 8
except:
    pass

# /usr/local/include/libiec61850/iec61850_common.h: 333
try:
    QUALITY_VALIDITY_GOOD = 0
except:
    pass

# /usr/local/include/libiec61850/iec61850_common.h: 334
try:
    QUALITY_VALIDITY_INVALID = 2
except:
    pass

# /usr/local/include/libiec61850/iec61850_common.h: 335
try:
    QUALITY_VALIDITY_RESERVED = 1
except:
    pass

# /usr/local/include/libiec61850/iec61850_common.h: 336
try:
    QUALITY_VALIDITY_QUESTIONABLE = 3
except:
    pass

# /usr/local/include/libiec61850/iec61850_common.h: 338
try:
    QUALITY_DETAIL_OVERFLOW = 4
except:
    pass

# /usr/local/include/libiec61850/iec61850_common.h: 339
try:
    QUALITY_DETAIL_OUT_OF_RANGE = 8
except:
    pass

# /usr/local/include/libiec61850/iec61850_common.h: 340
try:
    QUALITY_DETAIL_BAD_REFERENCE = 16
except:
    pass

# /usr/local/include/libiec61850/iec61850_common.h: 341
try:
    QUALITY_DETAIL_OSCILLATORY = 32
except:
    pass

# /usr/local/include/libiec61850/iec61850_common.h: 342
try:
    QUALITY_DETAIL_FAILURE = 64
except:
    pass

# /usr/local/include/libiec61850/iec61850_common.h: 343
try:
    QUALITY_DETAIL_OLD_DATA = 128
except:
    pass

# /usr/local/include/libiec61850/iec61850_common.h: 344
try:
    QUALITY_DETAIL_INCONSISTENT = 256
except:
    pass

# /usr/local/include/libiec61850/iec61850_common.h: 345
try:
    QUALITY_DETAIL_INACCURATE = 512
except:
    pass

# /usr/local/include/libiec61850/iec61850_common.h: 347
try:
    QUALITY_SOURCE_SUBSTITUTED = 1024
except:
    pass

# /usr/local/include/libiec61850/iec61850_common.h: 349
try:
    QUALITY_TEST = 2048
except:
    pass

# /usr/local/include/libiec61850/iec61850_common.h: 351
try:
    QUALITY_OPERATOR_BLOCKED = 4096
except:
    pass

# /usr/local/include/libiec61850/iec61850_common.h: 353
try:
    QUALITY_DERIVED = 8192
except:
    pass

# /usr/local/include/libiec61850/iec61850_client.h: 512
try:
    IEC61850_SV_OPT_REFRESH_TIME = 1
except:
    pass

# /usr/local/include/libiec61850/iec61850_client.h: 515
try:
    IEC61850_SV_OPT_SAMPLE_SYNC = 2
except:
    pass

# /usr/local/include/libiec61850/iec61850_client.h: 518
try:
    IEC61850_SV_OPT_SAMPLE_RATE = 4
except:
    pass

# /usr/local/include/libiec61850/iec61850_client.h: 521
try:
    IEC61850_SV_OPT_DATA_SET = 8
except:
    pass

# /usr/local/include/libiec61850/iec61850_client.h: 524
try:
    IEC61850_SV_OPT_SECURITY = 16
except:
    pass

# /usr/local/include/libiec61850/iec61850_client.h: 526
try:
    IEC61850_SV_SMPMOD_SAMPLES_PER_PERIOD = 0
except:
    pass

# /usr/local/include/libiec61850/iec61850_client.h: 528
try:
    IEC61850_SV_SMPMOD_SAMPLES_PER_SECOND = 1
except:
    pass

# /usr/local/include/libiec61850/iec61850_client.h: 530
try:
    IEC61850_SV_SMPMOD_SECONDS_PER_SAMPLE = 2
except:
    pass

# /usr/local/include/libiec61850/iec61850_client.h: 668
try:
    GOCB_ELEMENT_GO_ENA = 1
except:
    pass

# /usr/local/include/libiec61850/iec61850_client.h: 671
try:
    GOCB_ELEMENT_GO_ID = 2
except:
    pass

# /usr/local/include/libiec61850/iec61850_client.h: 674
try:
    GOCB_ELEMENT_DATSET = 4
except:
    pass

# /usr/local/include/libiec61850/iec61850_client.h: 677
try:
    GOCB_ELEMENT_CONF_REV = 8
except:
    pass

# /usr/local/include/libiec61850/iec61850_client.h: 680
try:
    GOCB_ELEMENT_NDS_COMM = 16
except:
    pass

# /usr/local/include/libiec61850/iec61850_client.h: 683
try:
    GOCB_ELEMENT_DST_ADDRESS = 32
except:
    pass

# /usr/local/include/libiec61850/iec61850_client.h: 686
try:
    GOCB_ELEMENT_MIN_TIME = 64
except:
    pass

# /usr/local/include/libiec61850/iec61850_client.h: 689
try:
    GOCB_ELEMENT_MAX_TIME = 128
except:
    pass

# /usr/local/include/libiec61850/iec61850_client.h: 692
try:
    GOCB_ELEMENT_FIXED_OFFS = 256
except:
    pass

# /usr/local/include/libiec61850/iec61850_client.h: 695
try:
    GOCB_ELEMENT_ALL = 511
except:
    pass

# /usr/local/include/libiec61850/iec61850_client.h: 1134
try:
    IEC61850_REASON_NOT_INCLUDED = 0
except:
    pass

# /usr/local/include/libiec61850/iec61850_client.h: 1137
try:
    IEC61850_REASON_DATA_CHANGE = 1
except:
    pass

# /usr/local/include/libiec61850/iec61850_client.h: 1140
try:
    IEC61850_REASON_QUALITY_CHANGE = 2
except:
    pass

# /usr/local/include/libiec61850/iec61850_client.h: 1143
try:
    IEC61850_REASON_DATA_UPDATE = 4
except:
    pass

# /usr/local/include/libiec61850/iec61850_client.h: 1146
try:
    IEC61850_REASON_INTEGRITY = 8
except:
    pass

# /usr/local/include/libiec61850/iec61850_client.h: 1149
try:
    IEC61850_REASON_GI = 16
except:
    pass

# /usr/local/include/libiec61850/iec61850_client.h: 1152
try:
    IEC61850_REASON_UNKNOWN = 32
except:
    pass

# /usr/local/include/libiec61850/iec61850_client.h: 1154
try:
    REASON_NOT_INCLUDED = IEC61850_REASON_NOT_INCLUDED
except:
    pass

# /usr/local/include/libiec61850/iec61850_client.h: 1155
try:
    REASON_DATA_CHANGE = IEC61850_REASON_DATA_CHANGE
except:
    pass

# /usr/local/include/libiec61850/iec61850_client.h: 1156
try:
    REASON_QUALITY_CHANGE = IEC61850_REASON_QUALITY_CHANGE
except:
    pass

# /usr/local/include/libiec61850/iec61850_client.h: 1157
try:
    REASON_DATA_UPDATE = IEC61850_REASON_DATA_UPDATE
except:
    pass

# /usr/local/include/libiec61850/iec61850_client.h: 1158
try:
    REASON_INTEGRITY = IEC61850_REASON_INTEGRITY
except:
    pass

# /usr/local/include/libiec61850/iec61850_client.h: 1159
try:
    REASON_GI = IEC61850_REASON_GI
except:
    pass

# /usr/local/include/libiec61850/iec61850_client.h: 1160
try:
    REASON_UNKNOWN = IEC61850_REASON_UNKNOWN
except:
    pass

# /usr/local/include/libiec61850/iec61850_client.h: 1166
try:
    RCB_ELEMENT_RPT_ID = 1
except:
    pass

# /usr/local/include/libiec61850/iec61850_client.h: 1169
try:
    RCB_ELEMENT_RPT_ENA = 2
except:
    pass

# /usr/local/include/libiec61850/iec61850_client.h: 1172
try:
    RCB_ELEMENT_RESV = 4
except:
    pass

# /usr/local/include/libiec61850/iec61850_client.h: 1175
try:
    RCB_ELEMENT_DATSET = 8
except:
    pass

# /usr/local/include/libiec61850/iec61850_client.h: 1178
try:
    RCB_ELEMENT_CONF_REV = 16
except:
    pass

# /usr/local/include/libiec61850/iec61850_client.h: 1181
try:
    RCB_ELEMENT_OPT_FLDS = 32
except:
    pass

# /usr/local/include/libiec61850/iec61850_client.h: 1184
try:
    RCB_ELEMENT_BUF_TM = 64
except:
    pass

# /usr/local/include/libiec61850/iec61850_client.h: 1187
try:
    RCB_ELEMENT_SQ_NUM = 128
except:
    pass

# /usr/local/include/libiec61850/iec61850_client.h: 1190
try:
    RCB_ELEMENT_TRG_OPS = 256
except:
    pass

# /usr/local/include/libiec61850/iec61850_client.h: 1193
try:
    RCB_ELEMENT_INTG_PD = 512
except:
    pass

# /usr/local/include/libiec61850/iec61850_client.h: 1196
try:
    RCB_ELEMENT_GI = 1024
except:
    pass

# /usr/local/include/libiec61850/iec61850_client.h: 1199
try:
    RCB_ELEMENT_PURGE_BUF = 2048
except:
    pass

# /usr/local/include/libiec61850/iec61850_client.h: 1202
try:
    RCB_ELEMENT_ENTRY_ID = 4096
except:
    pass

# /usr/local/include/libiec61850/iec61850_client.h: 1205
try:
    RCB_ELEMENT_TIME_OF_ENTRY = 8192
except:
    pass

# /usr/local/include/libiec61850/iec61850_client.h: 1208
try:
    RCB_ELEMENT_RESV_TMS = 16384
except:
    pass

# /usr/local/include/libiec61850/iec61850_client.h: 1211
try:
    RCB_ELEMENT_OWNER = 32768
except:
    pass

# /usr/local/include/libiec61850/mms_server.h: 301
try:
    MMS_LOGICAL_STATE_STATE_CHANGES_ALLOWED = 0
except:
    pass

# /usr/local/include/libiec61850/mms_server.h: 302
try:
    MMS_LOGICAL_STATE_NO_STATE_CHANGES_ALLOWED = 1
except:
    pass

# /usr/local/include/libiec61850/mms_server.h: 303
try:
    MMS_LOGICAL_STATE_LIMITED_SERVICES_PERMITTED = 2
except:
    pass

# /usr/local/include/libiec61850/mms_server.h: 304
try:
    MMS_LOGICAL_STATE_SUPPORT_SERVICES_ALLOWED = 3
except:
    pass

# /usr/local/include/libiec61850/mms_server.h: 306
try:
    MMS_PHYSICAL_STATE_OPERATIONAL = 0
except:
    pass

# /usr/local/include/libiec61850/mms_server.h: 307
try:
    MMS_PHYSICAL_STATE_PARTIALLY_OPERATIONAL = 1
except:
    pass

# /usr/local/include/libiec61850/mms_server.h: 308
try:
    MMS_PHYSICAL_STATE_INOPERATIONAL = 2
except:
    pass

# /usr/local/include/libiec61850/mms_server.h: 309
try:
    MMS_PHYSICAL_STATE_NEEDS_COMMISSIONING = 3
except:
    pass

# /usr/local/include/libiec61850/iec61850_cdc.h: 47
try:
    CDC_OPTION_PICS_SUBST = (1 << 0)
except:
    pass

# /usr/local/include/libiec61850/iec61850_cdc.h: 48
try:
    CDC_OPTION_BLK_ENA = (1 << 1)
except:
    pass

# /usr/local/include/libiec61850/iec61850_cdc.h: 51
try:
    CDC_OPTION_DESC = (1 << 2)
except:
    pass

# /usr/local/include/libiec61850/iec61850_cdc.h: 54
try:
    CDC_OPTION_DESC_UNICODE = (1 << 3)
except:
    pass

# /usr/local/include/libiec61850/iec61850_cdc.h: 57
try:
    CDC_OPTION_AC_DLNDA = (1 << 4)
except:
    pass

# /usr/local/include/libiec61850/iec61850_cdc.h: 60
try:
    CDC_OPTION_AC_DLN = (1 << 5)
except:
    pass

# /usr/local/include/libiec61850/iec61850_cdc.h: 63
try:
    CDC_OPTION_UNIT = (1 << 6)
except:
    pass

# /usr/local/include/libiec61850/iec61850_cdc.h: 65
try:
    CDC_OPTION_FROZEN_VALUE = (1 << 7)
except:
    pass

# /usr/local/include/libiec61850/iec61850_cdc.h: 67
try:
    CDC_OPTION_ADDR = (1 << 8)
except:
    pass

# /usr/local/include/libiec61850/iec61850_cdc.h: 68
try:
    CDC_OPTION_ADDINFO = (1 << 9)
except:
    pass

# /usr/local/include/libiec61850/iec61850_cdc.h: 70
try:
    CDC_OPTION_INST_MAG = (1 << 10)
except:
    pass

# /usr/local/include/libiec61850/iec61850_cdc.h: 71
try:
    CDC_OPTION_RANGE = (1 << 11)
except:
    pass

# /usr/local/include/libiec61850/iec61850_cdc.h: 73
try:
    CDC_OPTION_UNIT_MULTIPLIER = (1 << 12)
except:
    pass

# /usr/local/include/libiec61850/iec61850_cdc.h: 75
try:
    CDC_OPTION_AC_SCAV = (1 << 13)
except:
    pass

# /usr/local/include/libiec61850/iec61850_cdc.h: 77
try:
    CDC_OPTION_MIN = (1 << 14)
except:
    pass

# /usr/local/include/libiec61850/iec61850_cdc.h: 78
try:
    CDC_OPTION_MAX = (1 << 15)
except:
    pass

# /usr/local/include/libiec61850/iec61850_cdc.h: 80
try:
    CDC_OPTION_AC_CLC_O = (1 << 16)
except:
    pass

# /usr/local/include/libiec61850/iec61850_cdc.h: 82
try:
    CDC_OPTION_RANGE_ANG = (1 << 17)
except:
    pass

# /usr/local/include/libiec61850/iec61850_cdc.h: 84
try:
    CDC_OPTION_PHASE_A = (1 << 18)
except:
    pass

# /usr/local/include/libiec61850/iec61850_cdc.h: 85
try:
    CDC_OPTION_PHASE_B = (1 << 19)
except:
    pass

# /usr/local/include/libiec61850/iec61850_cdc.h: 86
try:
    CDC_OPTION_PHASE_C = (1 << 20)
except:
    pass

# /usr/local/include/libiec61850/iec61850_cdc.h: 88
try:
    CDC_OPTION_PHASE_NEUT = (1 << 21)
except:
    pass

# /usr/local/include/libiec61850/iec61850_cdc.h: 90
try:
    CDC_OPTION_PHASES_ABC = ((CDC_OPTION_PHASE_A | CDC_OPTION_PHASE_B) | CDC_OPTION_PHASE_C)
except:
    pass

# /usr/local/include/libiec61850/iec61850_cdc.h: 92
try:
    CDC_OPTION_PHASES_ALL = (((CDC_OPTION_PHASE_A | CDC_OPTION_PHASE_B) | CDC_OPTION_PHASE_C) | CDC_OPTION_PHASE_NEUT)
except:
    pass

# /usr/local/include/libiec61850/iec61850_cdc.h: 94
try:
    CDC_OPTION_STEP_SIZE = (1 << 22)
except:
    pass

# /usr/local/include/libiec61850/iec61850_cdc.h: 96
try:
    CDC_OPTION_ANGLE_REF = (1 << 23)
except:
    pass

# /usr/local/include/libiec61850/iec61850_cdc.h: 99
try:
    CDC_OPTION_DPL_HWREV = (1 << 17)
except:
    pass

# /usr/local/include/libiec61850/iec61850_cdc.h: 100
try:
    CDC_OPTION_DPL_SWREV = (1 << 18)
except:
    pass

# /usr/local/include/libiec61850/iec61850_cdc.h: 101
try:
    CDC_OPTION_DPL_SERNUM = (1 << 19)
except:
    pass

# /usr/local/include/libiec61850/iec61850_cdc.h: 102
try:
    CDC_OPTION_DPL_MODEL = (1 << 20)
except:
    pass

# /usr/local/include/libiec61850/iec61850_cdc.h: 103
try:
    CDC_OPTION_DPL_LOCATION = (1 << 21)
except:
    pass

# /usr/local/include/libiec61850/iec61850_cdc.h: 106
try:
    CDC_OPTION_AC_LN0_M = (1 << 24)
except:
    pass

# /usr/local/include/libiec61850/iec61850_cdc.h: 107
try:
    CDC_OPTION_AC_LN0_EX = (1 << 25)
except:
    pass

# /usr/local/include/libiec61850/iec61850_cdc.h: 108
try:
    CDC_OPTION_AC_DLD_M = (1 << 26)
except:
    pass

# /usr/local/include/libiec61850/iec61850_cdc.h: 113
try:
    CDC_CTL_MODEL_NONE = 0
except:
    pass

# /usr/local/include/libiec61850/iec61850_cdc.h: 114
try:
    CDC_CTL_MODEL_DIRECT_NORMAL = 1
except:
    pass

# /usr/local/include/libiec61850/iec61850_cdc.h: 115
try:
    CDC_CTL_MODEL_SBO_NORMAL = 2
except:
    pass

# /usr/local/include/libiec61850/iec61850_cdc.h: 116
try:
    CDC_CTL_MODEL_DIRECT_ENHANCED = 3
except:
    pass

# /usr/local/include/libiec61850/iec61850_cdc.h: 117
try:
    CDC_CTL_MODEL_SBO_ENHANCED = 4
except:
    pass

# /usr/local/include/libiec61850/iec61850_cdc.h: 119
try:
    CDC_CTL_MODEL_HAS_CANCEL = (1 << 4)
except:
    pass

# /usr/local/include/libiec61850/iec61850_cdc.h: 120
try:
    CDC_CTL_MODEL_IS_TIME_ACTIVATED = (1 << 5)
except:
    pass

# /usr/local/include/libiec61850/iec61850_cdc.h: 122
try:
    CDC_CTL_OPTION_ORIGIN = (1 << 6)
except:
    pass

# /usr/local/include/libiec61850/iec61850_cdc.h: 123
try:
    CDC_CTL_OPTION_CTL_NUM = (1 << 7)
except:
    pass

# /usr/local/include/libiec61850/iec61850_cdc.h: 124
try:
    CDC_CTL_OPTION_ST_SELD = (1 << 8)
except:
    pass

# /usr/local/include/libiec61850/iec61850_cdc.h: 125
try:
    CDC_CTL_OPTION_OP_RCVD = (1 << 9)
except:
    pass

# /usr/local/include/libiec61850/iec61850_cdc.h: 126
try:
    CDC_CTL_OPTION_OP_OK = (1 << 10)
except:
    pass

# /usr/local/include/libiec61850/iec61850_cdc.h: 127
try:
    CDC_CTL_OPTION_T_OP_OK = (1 << 11)
except:
    pass

# /usr/local/include/libiec61850/iec61850_cdc.h: 128
try:
    CDC_CTL_OPTION_SBO_TIMEOUT = (1 << 12)
except:
    pass

# /usr/local/include/libiec61850/iec61850_cdc.h: 129
try:
    CDC_CTL_OPTION_SBO_CLASS = (1 << 13)
except:
    pass

# /usr/local/include/libiec61850/iec61850_cdc.h: 130
try:
    CDC_CTL_OPTION_OPER_TIMEOUT = (1 << 14)
except:
    pass

# /usr/local/include/libiec61850/iec61850_cdc.h: 562
try:
    CDC_OPTION_61400_MIN_MX_VAL = (1 << 10)
except:
    pass

# /usr/local/include/libiec61850/iec61850_cdc.h: 565
try:
    CDC_OPTION_61400_MAX_MX_VAL = (1 << 11)
except:
    pass

# /usr/local/include/libiec61850/iec61850_cdc.h: 568
try:
    CDC_OPTION_61400_TOT_AV_VAL = (1 << 12)
except:
    pass

# /usr/local/include/libiec61850/iec61850_cdc.h: 571
try:
    CDC_OPTION_61400_SDV_VAL = (1 << 13)
except:
    pass

# /usr/local/include/libiec61850/iec61850_cdc.h: 574
try:
    CDC_OPTION_61400_INC_RATE = (1 << 14)
except:
    pass

# /usr/local/include/libiec61850/iec61850_cdc.h: 577
try:
    CDC_OPTION_61400_DEC_RATE = (1 << 15)
except:
    pass

# /usr/local/include/libiec61850/iec61850_cdc.h: 580
try:
    CDC_OPTION_61400_SP_ACS = (1 << 16)
except:
    pass

# /usr/local/include/libiec61850/iec61850_cdc.h: 583
try:
    CDC_OPTION_61400_CHA_PER_RS = (1 << 17)
except:
    pass

# /usr/local/include/libiec61850/iec61850_cdc.h: 586
try:
    CDC_OPTION_61400_CM_ACS = (1 << 18)
except:
    pass

# /usr/local/include/libiec61850/iec61850_cdc.h: 589
try:
    CDC_OPTION_61400_TM_TOT = (1 << 19)
except:
    pass

# /usr/local/include/libiec61850/iec61850_cdc.h: 592
try:
    CDC_OPTION_61400_COUNTING_DAILY = (1 << 20)
except:
    pass

# /usr/local/include/libiec61850/iec61850_cdc.h: 595
try:
    CDC_OPTION_61400_COUNTING_MONTHLY = (1 << 21)
except:
    pass

# /usr/local/include/libiec61850/iec61850_cdc.h: 598
try:
    CDC_OPTION_61400_COUNTING_YEARLY = (1 << 22)
except:
    pass

# /usr/local/include/libiec61850/iec61850_cdc.h: 601
try:
    CDC_OPTION_61400_COUNTING_TOTAL = (1 << 23)
except:
    pass

# /usr/local/include/libiec61850/iec61850_cdc.h: 604
try:
    CDC_OPTION_61400_COUNTING_ALL = (((CDC_OPTION_61400_COUNTING_DAILY | CDC_OPTION_61400_COUNTING_MONTHLY) | CDC_OPTION_61400_COUNTING_YEARLY) | CDC_OPTION_61400_COUNTING_TOTAL)
except:
    pass

# /usr/local/include/libiec61850/iec61850_server.h: 45
try:
    IEC61850_REPORTSETTINGS_RPT_ID = 1
except:
    pass

# /usr/local/include/libiec61850/iec61850_server.h: 46
try:
    IEC61850_REPORTSETTINGS_BUF_TIME = 2
except:
    pass

# /usr/local/include/libiec61850/iec61850_server.h: 47
try:
    IEC61850_REPORTSETTINGS_DATSET = 4
except:
    pass

# /usr/local/include/libiec61850/iec61850_server.h: 48
try:
    IEC61850_REPORTSETTINGS_TRG_OPS = 8
except:
    pass

# /usr/local/include/libiec61850/iec61850_server.h: 49
try:
    IEC61850_REPORTSETTINGS_OPT_FIELDS = 16
except:
    pass

# /usr/local/include/libiec61850/iec61850_server.h: 50
try:
    IEC61850_REPORTSETTINGS_INTG_PD = 32
except:
    pass

# /usr/local/include/libiec61850/iec61850_server.h: 1677
try:
    IEC61850_SVCB_EVENT_ENABLE = 1
except:
    pass

# /usr/local/include/libiec61850/iec61850_server.h: 1680
try:
    IEC61850_SVCB_EVENT_DISABLE = 0
except:
    pass

# /usr/local/include/libiec61850/iec61850_server.h: 1713
try:
    IEC61850_GOCB_EVENT_ENABLE = 1
except:
    pass

# /usr/local/include/libiec61850/iec61850_server.h: 1716
try:
    IEC61850_GOCB_EVENT_DISABLE = 0
except:
    pass

# /usr/local/include/libiec61850/sv_publisher.h: 51
try:
    IEC61850_SV_SMPSYNC_NOT_SYNCHRONIZED = 0
except:
    pass

# /usr/local/include/libiec61850/sv_publisher.h: 52
try:
    IEC61850_SV_SMPSYNC_SYNCED_UNSPEC_LOCAL_CLOCK = 1
except:
    pass

# /usr/local/include/libiec61850/sv_publisher.h: 53
try:
    IEC61850_SV_SMPSYNC_SYNCED_GLOBAL_CLOCK = 2
except:
    pass

# /usr/local/include/libiec61850/sv_publisher.h: 55
try:
    IEC61850_SV_SMPMOD_PER_NOMINAL_PERIOD = 0
except:
    pass

# /usr/local/include/libiec61850/sv_publisher.h: 56
try:
    IEC61850_SV_SMPMOD_SAMPLES_PER_SECOND = 1
except:
    pass

# /usr/local/include/libiec61850/sv_publisher.h: 57
try:
    IEC61850_SV_SMPMOD_SECONDS_PER_SAMPLE = 2
except:
    pass

sThread = struct_sThread# /usr/local/include/libiec61850/hal_thread.h: 38

sDirectoryHandle = struct_sDirectoryHandle# /usr/local/include/libiec61850/hal_filesystem.h: 31

sEthernetSocket = struct_sEthernetSocket# /usr/local/include/libiec61850/hal_ethernet.h: 34

sEthernetHandleSet = struct_sEthernetHandleSet# /usr/local/include/libiec61850/hal_ethernet.h: 37

sServerSocket = struct_sServerSocket# /usr/local/include/libiec61850/hal_socket.h: 44

sUdpSocket = struct_sUdpSocket# /usr/local/include/libiec61850/hal_socket.h: 46

sSocket = struct_sSocket# /usr/local/include/libiec61850/hal_socket.h: 49

sHandleSet = struct_sHandleSet# /usr/local/include/libiec61850/hal_socket.h: 52

sTLSConfiguration = struct_sTLSConfiguration# /usr/local/include/libiec61850/tls_config.h: 37

sTLSConnection = struct_sTLSConnection# /usr/local/include/libiec61850/tls_config.h: 94

sMmsDomain = struct_sMmsDomain# /usr/local/include/libiec61850/mms_common.h: 137

sMmsAccessSpecifier = struct_sMmsAccessSpecifier# /usr/local/include/libiec61850/mms_common.h: 145

sMmsNamedVariableList = struct_sMmsNamedVariableList# /usr/local/include/libiec61850/mms_common.h: 155

sMmsVariableSpecification = struct_sMmsVariableSpecification# /usr/local/include/libiec61850/mms_types.h: 50

sMmsArray = struct_sMmsArray# /usr/local/include/libiec61850/mms_types.h: 55

sMmsStructure = struct_sMmsStructure# /usr/local/include/libiec61850/mms_types.h: 59

sMmsFloat = struct_sMmsFloat# /usr/local/include/libiec61850/mms_types.h: 66

uMmsTypeSpecification = union_uMmsTypeSpecification# /usr/local/include/libiec61850/mms_types.h: 53

sMmsValue = struct_sMmsValue# /usr/local/include/libiec61850/mms_value.h: 68

sLinkedList = struct_sLinkedList# /usr/local/include/libiec61850/linked_list.h: 44

sLogStorage = struct_sLogStorage# /usr/local/include/libiec61850/logging_api.h: 78

sAcseAuthenticationParameter = struct_sAcseAuthenticationParameter# /usr/local/include/libiec61850/iso_connection_parameters.h: 60

sIsoConnectionParameters = struct_sIsoConnectionParameters# /usr/local/include/libiec61850/iso_connection_parameters.h: 137

sMmsConnectionParameters = struct_sMmsConnectionParameters# /usr/local/include/libiec61850/mms_client_connection.h: 54

sMmsConnection = struct_sMmsConnection# /usr/local/include/libiec61850/mms_client_connection.h: 75

sMmsJournalEntry = struct_sMmsJournalEntry# /usr/local/include/libiec61850/mms_client_connection.h: 1253

sMmsJournalVariable = struct_sMmsJournalVariable# /usr/local/include/libiec61850/mms_client_connection.h: 1259

sClientDataSet = struct_sClientDataSet# /usr/local/include/libiec61850/iec61850_client.h: 43

sClientReport = struct_sClientReport# /usr/local/include/libiec61850/iec61850_client.h: 46

sClientReportControlBlock = struct_sClientReportControlBlock# /usr/local/include/libiec61850/iec61850_client.h: 49

sClientGooseControlBlock = struct_sClientGooseControlBlock# /usr/local/include/libiec61850/iec61850_client.h: 52

sIedConnection = struct_sIedConnection# /usr/local/include/libiec61850/iec61850_client.h: 61

sClientSVControlBlock = struct_sClientSVControlBlock# /usr/local/include/libiec61850/iec61850_client.h: 534

sControlObjectClient = struct_sControlObjectClient# /usr/local/include/libiec61850/iec61850_client.h: 2012

sFileDirectoryEntry = struct_sFileDirectoryEntry# /usr/local/include/libiec61850/iec61850_client.h: 2783

sMmsServer = struct_sMmsServer# /usr/local/include/libiec61850/mms_server.h: 44

sMmsServerConnection = struct_sMmsServerConnection# /usr/local/include/libiec61850/mms_server.h: 46

sModelNode = struct_sModelNode# /usr/local/include/libiec61850/iec61850_model.h: 192

sDataAttribute = struct_sDataAttribute# /usr/local/include/libiec61850/iec61850_model.h: 218

sDataObject = struct_sDataObject# /usr/local/include/libiec61850/iec61850_model.h: 208

sLogicalNode = struct_sLogicalNode# /usr/local/include/libiec61850/iec61850_model.h: 200

sLogicalDevice = struct_sLogicalDevice# /usr/local/include/libiec61850/iec61850_model.h: 184

sIedModel = struct_sIedModel# /usr/local/include/libiec61850/iec61850_model.h: 171

sDataSet = struct_sDataSet# /usr/local/include/libiec61850/iec61850_model.h: 247

sReportControlBlock = struct_sReportControlBlock# /usr/local/include/libiec61850/iec61850_model.h: 255

sSettingGroupControlBlock = struct_sSettingGroupControlBlock# /usr/local/include/libiec61850/iec61850_model.h: 302

sGSEControlBlock = struct_sGSEControlBlock# /usr/local/include/libiec61850/iec61850_model.h: 316

sSVControlBlock = struct_sSVControlBlock# /usr/local/include/libiec61850/iec61850_model.h: 329

sLogControlBlock = struct_sLogControlBlock# /usr/local/include/libiec61850/iec61850_model.h: 277

sLog = struct_sLog# /usr/local/include/libiec61850/iec61850_model.h: 294

sDataSetEntry = struct_sDataSetEntry# /usr/local/include/libiec61850/iec61850_model.h: 237

sIedServerConfig = struct_sIedServerConfig# /usr/local/include/libiec61850/iec61850_server.h: 57

sIedServer = struct_sIedServer# /usr/local/include/libiec61850/iec61850_server.h: 425

sClientConnection = struct_sClientConnection# /usr/local/include/libiec61850/iec61850_server.h: 430

sMmsGooseControlBlock = struct_sMmsGooseControlBlock# /usr/local/include/libiec61850/iec61850_server.h: 1710

sGooseSubscriber = struct_sGooseSubscriber# /usr/local/include/libiec61850/goose_subscriber.h: 53

sGooseReceiver = struct_sGooseReceiver# /usr/local/include/libiec61850/goose_receiver.h: 41

sCommParameters = struct_sCommParameters# /usr/local/include/libiec61850/goose_publisher.h: 43

sGoosePublisher = struct_sGoosePublisher# /usr/local/include/libiec61850/goose_publisher.h: 47

sSVSubscriber_ASDU = struct_sSVSubscriber_ASDU# /usr/local/include/libiec61850/sv_subscriber.h: 96

sSVSubscriber = struct_sSVSubscriber# /usr/local/include/libiec61850/sv_subscriber.h: 105

sSVReceiver = struct_sSVReceiver# /usr/local/include/libiec61850/sv_subscriber.h: 121

sSVSubscriberASDU = struct_sSVSubscriberASDU# /usr/local/include/libiec61850/sv_subscriber.h: 567

sSVPublisher = struct_sSVPublisher# /usr/local/include/libiec61850/sv_publisher.h: 62

sSVPublisher_ASDU = struct_sSVPublisher_ASDU# /usr/local/include/libiec61850/sv_publisher.h: 67

sSV_ASDU = struct_sSV_ASDU# /usr/local/include/libiec61850/sv_publisher.h: 424

# No inserted files

# No prefix-stripping

