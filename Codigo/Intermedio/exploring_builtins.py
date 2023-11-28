# references
# https://www.w3schools.com/python/python_ref_keywords.asp
# https://www.w3schools.com/python/python_ref_functions.asp
# https://docs.python.org/3/library/functions.html
# https://mathspp.com/blog/pydonts/dunder-methods
 
#**PEP 3107** - Function Annotations
#     The original specification for function annotations.


#import _03lambdas
#import os

def test():
    """
    This is a short description of the functionality in this method
    it doesn't do anything.
    >>> test()

    """
    pass

# 40 - 16 = 24
funclist:[str] = ['__bool__', 
                  '__class__', 
                  '__delattr__', 
                  '__dir__', 
                  '__doc__', 
                  '__eq__', 
                  '__format__', 
                  '__ge__', 
                  '__getattribute__', 
                  '__getstate__', 
                  '__gt__', 
                  '__hash__', 
                  '__init__', 
                  '__init_subclass__', 
                  '__le__', 
                  '__lt__', 
                  '__ne__', 
                  '__new__', 
                  '__reduce__', 
                  '__reduce_ex__', 
                  '__repr__', 
                  '__setattr__', 
                  '__sizeof__', 
                  '__str__', 
                  '__subclasshook__']


class Animal:
    pass

# 72 - 46 = 26
classlist:[str] = ['__class__', 
                   '__delattr__', 
                   '__dict__', 
                   '__dir__', 
                   '__doc__', 
                   '__eq__', 
                   '__format__', 
                   '__ge__', 
                   '__getattribute__', 
                   '__getstate__', 
                   '__gt__', 
                   '__hash__', 
                   '__init__', 
                   '__init_subclass__', 
                   '__le__', 
                   '__lt__', 
                   '__module__', 
                   '__ne__', 
                   '__new__', 
                   '__reduce__', 
                   '__reduce_ex__', 
                   '__repr__', 
                   '__setattr__', 
                   '__sizeof__', 
                   '__str__', 
                   '__subclasshook__', 
                   '__weakref__']

# 84 -74 = 10
modulelist:[str] = ['__builtins__', 
                    '__cached__', 
                    '__doc__', 
                    '__file__', 
                    '__loader__', 
                    '__name__', 
                    '__package__', 
                    '__spec__', 
                    'multiply_values', 
                    'sum_three_values', 
                    'sum_two_values']
#245-86 = 159
listOs:[str] = ['DirEntry', 
                'EX_OK', 
                'F_OK', 
                'GenericAlias', 
                'Mapping', 
                'MutableMapping', 
                'O_APPEND', 
                'O_BINARY', 
                'O_CREAT', 
                'O_EXCL', 
                'O_NOINHERIT', 
                'O_RANDOM', 
                'O_RDONLY', 
                'O_RDWR', 
                'O_SEQUENTIAL', 
                'O_SHORT_LIVED', 
                'O_TEMPORARY', 
                'O_TEXT', 
                'O_TRUNC', 
                'O_WRONLY', 
                'P_DETACH', 
                'P_NOWAIT', 
                'P_NOWAITO', 
                'P_OVERLAY', 
                'P_WAIT', 
                'PathLike', 
                'R_OK', 
                'SEEK_CUR', 
                'SEEK_END', 
                'SEEK_SET', 
                'TMP_MAX', 
                'W_OK', 
                'X_OK', 
                '_AddedDllDirectory', 
                '_Environ', 
                '__all__', 
                '__builtins__', 
                '__doc__', 
                '__file__', 
                '__loader__', 
                '__name__', 
                '__package__', 
                '__spec__', 
                '_check_methods', 
                '_execvpe', 
                '_exists', 
                '_exit', 
                '_fspath', 
                '_get_exports_list', 
                '_wrap_close', 
                'abc', 
                'abort', 
                'access', 
                'add_dll_directory', 
                'altsep', 
                'chdir', 
                'chmod', 
                'close', 
                'closerange', 
                'cpu_count', 
                'curdir', 
                'defpath', 
                'device_encoding', 
                'devnull', 
                'dup', 
                'dup2', 
                'environ', 
                'error', 
                'execl', 
                'execle', 
                'execlp', 
                'execlpe', 
                'execv', 
                'execve', 
                'execvp', 
                'execvpe', 
                'extsep', 
                'fdopen', 
                'fsdecode', 
                'fsencode', 
                'fspath', 
                'fstat', 
                'fsync', 
                'ftruncate', 
                'get_blocking', 
                'get_exec_path', 
                'get_handle_inheritable', 
                'get_inheritable', 
                'get_terminal_size', 
                'getcwd', 
                'getcwdb', 
                'getenv', 
                'getlogin', 
                'getpid', 
                'getppid', 
                'isatty', 
                'kill', 
                'linesep', 
                'link', 
                'listdir', 
                'listdrives', 
                'listmounts', 
                'listvolumes', 
                'lseek', 
                'lstat', 
                'makedirs', 
                'mkdir', 
                'name', 
                'open', 
                'pardir', 
                'path', 
                'pathsep', 
                'pipe', 
                'popen', 
                'putenv', 
                'read', 
                'readlink', 
                'remove', 
                'removedirs', 
                'rename', 
                'renames', 
                'replace', 
                'rmdir', 
                'scandir', 
                'sep', 
                'set_blocking', 
                'set_handle_inheritable', 
                'set_inheritable', 
                'spawnl', 
                'spawnle', 
                'spawnv', 
                'spawnve', 
                'st', 
                'startfile', 
                'stat', 
                'stat_result', 
                'statvfs_result', 
                'strerror', 
                'supports_bytes_environ', 
                'supports_dir_fd', 
                'supports_effective_ids', 
                'supports_fd', 
                'supports_follow_symlinks', 
                'symlink', 
                'sys', 
                'system', 
                'terminal_size', 
                'times', 
                'times_result', 
                'truncate', 
                'umask', 
                'uname_result', 
                'unlink', 
                'unsetenv', 
                'urandom', 
                'utime', 
                'waitpid', 
                'waitstatus_to_exitcode', 
                'walk', 
                'write']
#print(dir(test()))
#print(test.__doc__)

#print(dir(Animal()))
#print(dir(_03lambdas))
#print(dir(os))

# using the help function to get more information.

#help('modules')
"""
Please wait a moment while I gather a list of all available modules...

test_sqlite3: testing with SQLite version 3.42.0
00dates             _typing             gettext             runpy
01list_comprenhension _uuid               glob                sched
02challenges        _warnings           graphlib            secrets
_03lambdas          _weakref            gzip                select
__future__          _weakrefset         h11                 selectors
__hello__           _winapi             hashlib             shelve
__phello__          _wmi                heapq               shlex
_abc                _xxinterpchannels   hmac                shutil
_aix_support        _xxsubinterpreters  html                signal
_ast                _yaml               http                site
_asyncio            _zoneinfo           httpcore            six
_bisect             abc                 httpx               slugify
_blake2             aifc                idlelib             smtplib
_bz2                antigravity         idna                sndhdr
_codecs             anyio               imaplib             sniffio
_codecs_cn          argparse            imghdr              socket
_codecs_hk          array               importlib           socketserver
_codecs_iso2022     arrow               inspect             sqlite3
_codecs_jp          ast                 io                  sre_compile
_codecs_kr          asyncio             ipaddress           sre_constants
_codecs_tw          atexit              itertools           sre_parse
_collections        audioop             jinja2              ssl
_collections_abc    base64              json                stat
_compat_pickle      bdb                 keyword             statistics
_compression        binaryornot         lib2to3             string
_contextvars        binascii            linecache           stringprep
_csv                bisect              locale              struct
_ctypes             builtins            logging             subprocess
_ctypes_test        bz2                 lzma                sunau
_datetime           cProfile            mailbox             symtable
_decimal            calendar            mailcap             sys
_elementtree        certifi             markdown_it         sysconfig
_functools          cgi                 markupsafe          tabnanny
_hashlib            cgitb               marshal             tarfile
_heapq              chardet             math                telnetlib
_imp                charset_normalizer  mdurl               tempfile
_io                 chunk               mimetypes           test
_json               click               mmap                text_unidecode
_locale             cmath               modulefinder        textwrap
_lsprof             cmd                 msilib              this
_lzma               code                msvcrt              threading
_markupbase         codecs              multiprocessing     time
_md5                codeop              netrc               timeit
_msi                collections         nntplib             tkinter
_multibytecodec     colorama            nt                  token
_multiprocessing    colorsys            ntpath              tokenize
_opcode             compileall          nturl2path          tomllib
_operator           concurrent          numbers             trace
_osx_support        configparser        oauthlib            traceback
_overlapped         contextlib          opcode              tracemalloc
_pickle             contextvars         operator            tty
_py_abc             cookiecutter        optparse            turtle
_pydatetime         copy                os                  turtledemo
_pydecimal          copyreg             packaging           types
_pyio               crypt               pathlib             typing
_pylong             csv                 pdb                 typing_extensions
_queue              ctypes              pickle              unicodedata
_random             curses              pickletools         unittest
_sha1               dataclasses         pip                 urllib
_sha2               datetime            pipes               urllib3
_sha3               dateutil            pkgutil             uu
_signal             dbm                 platform            uuid
_sitebuiltins       decimal             plistlib            venv
_socket             difflib             png                 warnings
_sqlite3            dis                 poplib              watchdog
_sre                doctest             posixpath           wave
_ssl                email               pprint              weakref
_stat               encodings           profile             webbrowser
_statistics         ensurepip           pstats              websocket
_string             enum                pty                 websockets
_strptime           errno               py_compile          winreg
_struct             exploring_builtins  pyclbr              winsound
_symtable           faulthandler        pydoc               wsgiref
_testbuffer         filecmp             pydoc_data          xdrlib
_testcapi           fileinput           pyexpat             xml
_testclinic         flet                pygments            xmlrpc
_testconsole        flet_core           qrcode              xxsubtype
_testimportmultiple flet_runtime        queue               yaml
_testinternalcapi   fnmatch             quopri              zipapp
_testmultiphase     fractions           random              zipfile
_testsinglephase    ftplib              re                  zipimport
_thread             functools           repath              zlib
_threading_local    gc                  reprlib             zoneinfo
_tkinter            genericpath         requests
_tokenize           getopt              rich
_tracemalloc        getpass             rlcompleter
"""
#help('keywords')
#help('yield')
#help('class')
"""
Here is a list of the Python keywords.  Enter any keyword to get more help.

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not
"""

#help('symbols')

#Here is a list of the punctuation symbols which Python assigns special meaning
#to. Enter any symbol to get more help.

# !=                  +                   <=                  __
# "                   +=                  <>                  `
# """                 ,                   ==                  b"
# %                   -                   >                   b'
# %=                  -=                  >=                  f"
# &                   .                   >>                  f'
# &=                  ...                 >>=                 j
# '                   /                   @                   r"
# '''                 //                  J                   r'
# (                   //=                 [                   u"
# )                   /=                  \                   u'
# *                   :                   ]                   |
# **                  <                   ^                   |=
# **=                 <<                  ^=                  ~
# *=                  <<=                 _

#help('topics')
"""
Here is a list of available topics.  Enter any topic name to get more help.

ASSERTION           DELETION            LOOPING             SHIFTING
ASSIGNMENT          DICTIONARIES        MAPPINGMETHODS      SLICINGS
ATTRIBUTEMETHODS    DICTIONARYLITERALS  MAPPINGS            SPECIALATTRIBUTES
ATTRIBUTES          DYNAMICFEATURES     METHODS             SPECIALIDENTIFIERS
AUGMENTEDASSIGNMENT ELLIPSIS            MODULES             SPECIALMETHODS
BASICMETHODS        EXCEPTIONS          NAMESPACES          STRINGMETHODS
BINARY              EXECUTION           NONE                STRINGS
BITWISE             EXPRESSIONS         NUMBERMETHODS       SUBSCRIPTS
BOOLEAN             FLOAT               NUMBERS             TRACEBACKS
CALLABLEMETHODS     FORMATTING          OBJECTS             TRUTHVALUE
CALLS               FRAMEOBJECTS        OPERATORS           TUPLELITERALS
CLASSES             FRAMES              PACKAGES            TUPLES
CODEOBJECTS         FUNCTIONS           POWER               TYPEOBJECTS
COMPARISON          IDENTIFIERS         PRECEDENCE          TYPES
COMPLEX             IMPORTING           PRIVATENAMES        UNARY
CONDITIONAL         INTEGER             RETURNING           UNICODE
CONTEXTMANAGERS     LISTLITERALS        SCOPING
CONVERSIONS         LISTS               SEQUENCEMETHODS
DEBUGGING           LITERALS            SEQUENCES
"""

#help('modules spam')
"""
Here is a list of modules whose name or summary contains 'spam'.
If there are any, enter a module name to get more help.

__phello__.spam 
test_sqlite3: testing with SQLite version 3.42.0
"""

#help('BASICMETHODS')

"""
Basic customization
*******************

object.__new__(cls[, ...])

   Called to create a new instance of class *cls*.  "__new__()" is a
   static method (special-cased so you need not declare it as such)
   that takes the class of which an instance was requested as its
   first argument.  The remaining arguments are those passed to the
   object constructor expression (the call to the class).  The return
   value of "__new__()" should be the new object instance (usually an
   instance of *cls*).

   Typical implementations create a new instance of the class by
   invoking the superclass\u2019s "__new__()" method using
   "super().__new__(cls[, ...])" with appropriate arguments and then
   modifying the newly created instance as necessary before returning
   it.

   If "__new__()" is invoked during object construction and it returns
   an instance of *cls*, then the new instance\u2019s "__init__()" method
   will be invoked like "__init__(self[, ...])", where *self* is the
   new instance and the remaining arguments are the same as were
   passed to the object constructor.

   If "__new__()" does not return an instance of *cls*, then the new
   instance\u2019s "__init__()" method will not be invoked.

   "__new__()" is intended mainly to allow subclasses of immutable
   types (like int, str, or tuple) to customize instance creation.  It
   is also commonly overridden in custom metaclasses in order to
   customize class creation.

object.__init__(self[, ...])

   Called after the instance has been created (by "__new__()"), but
   before it is returned to the caller.  The arguments are those
   passed to the class constructor expression.  If a base class has an
   "__init__()" method, the derived class\u2019s "__init__()" method, if
   any, must explicitly call it to ensure proper initialization of the
   base class part of the instance; for example:
   "super().__init__([args...])".

   Because "__new__()" and "__init__()" work together in constructing
   objects ("__new__()" to create it, and "__init__()" to customize
   it), no non-"None" value may be returned by "__init__()"; doing so
   will cause a "TypeError" to be raised at runtime.

object.__del__(self)

   Called when the instance is about to be destroyed.  This is also
   called a finalizer or (improperly) a destructor.  If a base class
   has a "__del__()" method, the derived class\u2019s "__del__()" method,
   if any, must explicitly call it to ensure proper deletion of the
   base class part of the instance.

   It is possible (though not recommended!) for the "__del__()" method
   to postpone destruction of the instance by creating a new reference
   to it.  This is called object *resurrection*.  It is
   implementation-dependent whether "__del__()" is called a second
   time when a resurrected object is about to be destroyed; the
   current *CPython* implementation only calls it once.

   It is not guaranteed that "__del__()" methods are called for
   objects that still exist when the interpreter exits.

   Note:

     "del x" doesn\u2019t directly call "x.__del__()" \u2014 the former
     decrements the reference count for "x" by one, and the latter is
     only called when "x"\u2019s reference count reaches zero.

   **CPython implementation detail:** It is possible for a reference
   cycle to prevent the reference count of an object from going to
   zero.  In this case, the cycle will be later detected and deleted
   by the *cyclic garbage collector*.  A common cause of reference
   cycles is when an exception has been caught in a local variable.
   The frame\u2019s locals then reference the exception, which references
   its own traceback, which references the locals of all frames caught
   in the traceback.

   See also: Documentation for the "gc" module.

   Warning:

     Due to the precarious circumstances under which "__del__()"
     methods are invoked, exceptions that occur during their execution
     are ignored, and a warning is printed to "sys.stderr" instead.
     In particular:

     * "__del__()" can be invoked when arbitrary code is being
       executed, including from any arbitrary thread.  If "__del__()"
       needs to take a lock or invoke any other blocking resource, it
       may deadlock as the resource may already be taken by the code
       that gets interrupted to execute "__del__()".

     * "__del__()" can be executed during interpreter shutdown.  As a
       consequence, the global variables it needs to access (including
       other modules) may already have been deleted or set to "None".
       Python guarantees that globals whose name begins with a single
       underscore are deleted from their module before other globals
       are deleted; if no other references to such globals exist, this
       may help in assuring that imported modules are still available
       at the time when the "__del__()" method is called.

object.__repr__(self)

   Called by the "repr()" built-in function to compute the \u201cofficial\u201d
   string representation of an object.  If at all possible, this
   should look like a valid Python expression that could be used to
   recreate an object with the same value (given an appropriate
   environment).  If this is not possible, a string of the form
   "<...some useful description...>" should be returned. The return
   value must be a string object. If a class defines "__repr__()" but
   not "__str__()", then "__repr__()" is also used when an \u201cinformal\u201d
   string representation of instances of that class is required.

   This is typically used for debugging, so it is important that the
   representation is information-rich and unambiguous.

object.__str__(self)

   Called by "str(object)" and the built-in functions "format()" and
   "print()" to compute the \u201cinformal\u201d or nicely printable string
   representation of an object.  The return value must be a string
   object.

   This method differs from "object.__repr__()" in that there is no
   expectation that "__str__()" return a valid Python expression: a
   more convenient or concise representation can be used.

   The default implementation defined by the built-in type "object"
   calls "object.__repr__()".

object.__bytes__(self)

   Called by bytes to compute a byte-string representation of an
   object. This should return a "bytes" object.

object.__format__(self, format_spec)

   Called by the "format()" built-in function, and by extension,
   evaluation of formatted string literals and the "str.format()"
   method, to produce a \u201cformatted\u201d string representation of an
   object. The *format_spec* argument is a string that contains a
   description of the formatting options desired. The interpretation
   of the *format_spec* argument is up to the type implementing
   "__format__()", however most classes will either delegate
   formatting to one of the built-in types, or use a similar
   formatting option syntax.

   See Format Specification Mini-Language for a description of the
   standard formatting syntax.

   The return value must be a string object.

   Changed in version 3.4: The __format__ method of "object" itself
   raises a "TypeError" if passed any non-empty string.

   Changed in version 3.7: "object.__format__(x, '')" is now
   equivalent to "str(x)" rather than "format(str(x), '')".

object.__lt__(self, other)
object.__le__(self, other)
object.__eq__(self, other)
object.__ne__(self, other)
object.__gt__(self, other)
object.__ge__(self, other)

   These are the so-called \u201crich comparison\u201d methods. The
   correspondence between operator symbols and method names is as
   follows: "x<y" calls "x.__lt__(y)", "x<=y" calls "x.__le__(y)",
   "x==y" calls "x.__eq__(y)", "x!=y" calls "x.__ne__(y)", "x>y" calls
   "x.__gt__(y)", and "x>=y" calls "x.__ge__(y)".

   A rich comparison method may return the singleton "NotImplemented"
   if it does not implement the operation for a given pair of
   arguments. By convention, "False" and "True" are returned for a
   successful comparison. However, these methods can return any value,
   so if the comparison operator is used in a Boolean context (e.g.,
   in the condition of an "if" statement), Python will call "bool()"
   on the value to determine if the result is true or false.

   By default, "object" implements "__eq__()" by using "is", returning
   "NotImplemented" in the case of a false comparison: "True if x is y
   else NotImplemented". For "__ne__()", by default it delegates to
   "__eq__()" and inverts the result unless it is "NotImplemented".
   There are no other implied relationships among the comparison
   operators or default implementations; for example, the truth of
   "(x<y or x==y)" does not imply "x<=y". To automatically generate
   ordering operations from a single root operation, see
   "functools.total_ordering()".

   See the paragraph on "__hash__()" for some important notes on
   creating *hashable* objects which support custom comparison
   operations and are usable as dictionary keys.

   There are no swapped-argument versions of these methods (to be used
   when the left argument does not support the operation but the right
   argument does); rather, "__lt__()" and "__gt__()" are each other\u2019s
   reflection, "__le__()" and "__ge__()" are each other\u2019s reflection,
   and "__eq__()" and "__ne__()" are their own reflection. If the
   operands are of different types, and right operand\u2019s type is a
   direct or indirect subclass of the left operand\u2019s type, the
   reflected method of the right operand has priority, otherwise the
   left operand\u2019s method has priority.  Virtual subclassing is not
   considered.

object.__hash__(self)

   Called by built-in function "hash()" and for operations on members
   of hashed collections including "set", "frozenset", and "dict".
   The "__hash__()" method should return an integer. The only required
   property is that objects which compare equal have the same hash
   value; it is advised to mix together the hash values of the
   components of the object that also play a part in comparison of
   objects by packing them into a tuple and hashing the tuple.
   Example:

      def __hash__(self):
          return hash((self.name, self.nick, self.color))

   Note:

     "hash()" truncates the value returned from an object\u2019s custom
     "__hash__()" method to the size of a "Py_ssize_t".  This is
     typically 8 bytes on 64-bit builds and 4 bytes on 32-bit builds.
     If an object\u2019s   "__hash__()" must interoperate on builds of
     different bit sizes, be sure to check the width on all supported
     builds.  An easy way to do this is with "python -c "import sys;
     print(sys.hash_info.width)"".

   If a class does not define an "__eq__()" method it should not
   define a "__hash__()" operation either; if it defines "__eq__()"
   but not "__hash__()", its instances will not be usable as items in
   hashable collections.  If a class defines mutable objects and
   implements an "__eq__()" method, it should not implement
   "__hash__()", since the implementation of *hashable* collections
   requires that a key\u2019s hash value is immutable (if the object\u2019s hash
   value changes, it will be in the wrong hash bucket).

   User-defined classes have "__eq__()" and "__hash__()" methods by
   default; with them, all objects compare unequal (except with
   themselves) and "x.__hash__()" returns an appropriate value such
   that "x == y" implies both that "x is y" and "hash(x) == hash(y)".

   A class that overrides "__eq__()" and does not define "__hash__()"
   will have its "__hash__()" implicitly set to "None".  When the
   "__hash__()" method of a class is "None", instances of the class
   will raise an appropriate "TypeError" when a program attempts to
   retrieve their hash value, and will also be correctly identified as
   unhashable when checking "isinstance(obj,
   collections.abc.Hashable)".

   If a class that overrides "__eq__()" needs to retain the
   implementation of "__hash__()" from a parent class, the interpreter
   must be told this explicitly by setting "__hash__ =
   <ParentClass>.__hash__".

   If a class that does not override "__eq__()" wishes to suppress
   hash support, it should include "__hash__ = None" in the class
   definition. A class which defines its own "__hash__()" that
   explicitly raises a "TypeError" would be incorrectly identified as
   hashable by an "isinstance(obj, collections.abc.Hashable)" call.

   Note:

     By default, the "__hash__()" values of str and bytes objects are
     \u201csalted\u201d with an unpredictable random value.  Although they
     remain constant within an individual Python process, they are not
     predictable between repeated invocations of Python.This is
     intended to provide protection against a denial-of-service caused
     by carefully chosen inputs that exploit the worst case
     performance of a dict insertion, O(n^2) complexity.  See
     http://ocert.org/advisories/ocert-2011-003.html for
     details.Changing hash values affects the iteration order of sets.
     Python has never made guarantees about this ordering (and it
     typically varies between 32-bit and 64-bit builds).See also
     "PYTHONHASHSEED".

   Changed in version 3.3: Hash randomization is enabled by default.

object.__bool__(self)

   Called to implement truth value testing and the built-in operation
   "bool()"; should return "False" or "True".  When this method is not
   defined, "__len__()" is called, if it is defined, and the object is
   considered true if its result is nonzero.  If a class defines
   neither "__len__()" nor "__bool__()", all its instances are
   considered true.

Related help topics: hash, repr, str, SPECIALMETHODS
"""

#help('CLASSES') 

"""
The standard type hierarchy
***************************

Below is a list of the types that are built into Python.  Extension
modules (written in C, Java, or other languages, depending on the
implementation) can define additional types.  Future versions of
Python may add types to the type hierarchy (e.g., rational numbers,
efficiently stored arrays of integers, etc.), although such additions
will often be provided via the standard library instead.

Some of the type descriptions below contain a paragraph listing
\u2018special attributes.\u2019  These are attributes that provide access to the
implementation and are not intended for general use.  Their definition
may change in the future.


None
====

This type has a single value.  There is a single object with this
value. This object is accessed through the built-in name "None". It is
used to signify the absence of a value in many situations, e.g., it is
returned from functions that don\u2019t explicitly return anything. Its
truth value is false.


NotImplemented
==============

This type has a single value.  There is a single object with this
value. This object is accessed through the built-in name
"NotImplemented". Numeric methods and rich comparison methods should
return this value if they do not implement the operation for the
operands provided.  (The interpreter will then try the reflected
operation, or some other fallback, depending on the operator.)  It
should not be evaluated in a boolean context.

See Implementing the arithmetic operations for more details.

Changed in version 3.9: Evaluating "NotImplemented" in a boolean
context is deprecated. While it currently evaluates as true, it will
emit a "DeprecationWarning". It will raise a "TypeError" in a future
version of Python.


Ellipsis
========

This type has a single value.  There is a single object with this
value. This object is accessed through the literal "..." or the built-
in name "Ellipsis".  Its truth value is true.


"numbers.Number"
================

These are created by numeric literals and returned as results by
arithmetic operators and arithmetic built-in functions.  Numeric
objects are immutable; once created their value never changes.  Python
numbers are of course strongly related to mathematical numbers, but
subject to the limitations of numerical representation in computers.

The string representations of the numeric classes, computed by
"__repr__()" and "__str__()", have the following properties:

* They are valid numeric literals which, when passed to their class
  constructor, produce an object having the value of the original
  numeric.

* The representation is in base 10, when possible.

* Leading zeros, possibly excepting a single zero before a decimal
  point, are not shown.

* Trailing zeros, possibly excepting a single zero after a decimal
  point, are not shown.

* A sign is shown only when the number is negative.

Python distinguishes between integers, floating point numbers, and
complex numbers:


"numbers.Integral"
------------------

These represent elements from the mathematical set of integers
(positive and negative).

Note:

  The rules for integer representation are intended to give the most
  meaningful interpretation of shift and mask operations involving
  negative integers.

There are two types of integers:

Integers ("int")
   These represent numbers in an unlimited range, subject to available
   (virtual) memory only.  For the purpose of shift and mask
   operations, a binary representation is assumed, and negative
   numbers are represented in a variant of 2\u2019s complement which gives
   the illusion of an infinite string of sign bits extending to the
   left.

Booleans ("bool")
   These represent the truth values False and True.  The two objects
   representing the values "False" and "True" are the only Boolean
   objects. The Boolean type is a subtype of the integer type, and
   Boolean values behave like the values 0 and 1, respectively, in
   almost all contexts, the exception being that when converted to a
   string, the strings ""False"" or ""True"" are returned,
   respectively.


"numbers.Real" ("float")
------------------------

These represent machine-level double precision floating point numbers.
You are at the mercy of the underlying machine architecture (and C or
Java implementation) for the accepted range and handling of overflow.
Python does not support single-precision floating point numbers; the
savings in processor and memory usage that are usually the reason for
using these are dwarfed by the overhead of using objects in Python, so
there is no reason to complicate the language with two kinds of
floating point numbers.


"numbers.Complex" ("complex")
-----------------------------

These represent complex numbers as a pair of machine-level double
precision floating point numbers.  The same caveats apply as for
floating point numbers. The real and imaginary parts of a complex
number "z" can be retrieved through the read-only attributes "z.real"
and "z.imag".


Sequences
=========

These represent finite ordered sets indexed by non-negative numbers.
The built-in function "len()" returns the number of items of a
sequence. When the length of a sequence is *n*, the index set contains
the numbers 0, 1, \u2026, *n*-1.  Item *i* of sequence *a* is selected by
"a[i]".

Sequences also support slicing: "a[i:j]" selects all items with index
*k* such that *i* "<=" *k* "<" *j*.  When used as an expression, a
slice is a sequence of the same type.  This implies that the index set
is renumbered so that it starts at 0.

Some sequences also support \u201cextended slicing\u201d with a third \u201cstep\u201d
parameter: "a[i:j:k]" selects all items of *a* with index *x* where "x
= i + n*k", *n* ">=" "0" and *i* "<=" *x* "<" *j*.

Sequences are distinguished according to their mutability:


Immutable sequences
-------------------

An object of an immutable sequence type cannot change once it is
created.  (If the object contains references to other objects, these
other objects may be mutable and may be changed; however, the
collection of objects directly referenced by an immutable object
cannot change.)

The following types are immutable sequences:

Strings
   A string is a sequence of values that represent Unicode code
   points. All the code points in the range "U+0000 - U+10FFFF" can be
   represented in a string.  Python doesn\u2019t have a char type; instead,
   every code point in the string is represented as a string object
   with length "1".  The built-in function "ord()" converts a code
   point from its string form to an integer in the range "0 - 10FFFF";
   "chr()" converts an integer in the range "0 - 10FFFF" to the
   corresponding length "1" string object. "str.encode()" can be used
   to convert a "str" to "bytes" using the given text encoding, and
   "bytes.decode()" can be used to achieve the opposite.

Tuples
   The items of a tuple are arbitrary Python objects. Tuples of two or
   more items are formed by comma-separated lists of expressions.  A
   tuple of one item (a \u2018singleton\u2019) can be formed by affixing a comma
   to an expression (an expression by itself does not create a tuple,
   since parentheses must be usable for grouping of expressions).  An
   empty tuple can be formed by an empty pair of parentheses.

Bytes
   A bytes object is an immutable array.  The items are 8-bit bytes,
   represented by integers in the range 0 <= x < 256.  Bytes literals
   (like "b'abc'") and the built-in "bytes()" constructor can be used
   to create bytes objects.  Also, bytes objects can be decoded to
   strings via the "decode()" method.


Mutable sequences
-----------------

Mutable sequences can be changed after they are created.  The
subscription and slicing notations can be used as the target of
assignment and "del" (delete) statements.

Note:

  The "collections" and "array" module provide additional examples of
  mutable sequence types.

There are currently two intrinsic mutable sequence types:

Lists
   The items of a list are arbitrary Python objects.  Lists are formed
   by placing a comma-separated list of expressions in square
   brackets. (Note that there are no special cases needed to form
   lists of length 0 or 1.)

Byte Arrays
   A bytearray object is a mutable array. They are created by the
   built-in "bytearray()" constructor.  Aside from being mutable (and
   hence unhashable), byte arrays otherwise provide the same interface
   and functionality as immutable "bytes" objects.


Set types
=========

These represent unordered, finite sets of unique, immutable objects.
As such, they cannot be indexed by any subscript. However, they can be
iterated over, and the built-in function "len()" returns the number of
items in a set. Common uses for sets are fast membership testing,
removing duplicates from a sequence, and computing mathematical
operations such as intersection, union, difference, and symmetric
difference.

For set elements, the same immutability rules apply as for dictionary
keys. Note that numeric types obey the normal rules for numeric
comparison: if two numbers compare equal (e.g., "1" and "1.0"), only
one of them can be contained in a set.

There are currently two intrinsic set types:

Sets
   These represent a mutable set. They are created by the built-in
   "set()" constructor and can be modified afterwards by several
   methods, such as "add()".

Frozen sets
   These represent an immutable set.  They are created by the built-in
   "frozenset()" constructor.  As a frozenset is immutable and
   *hashable*, it can be used again as an element of another set, or
   as a dictionary key.


Mappings
========

These represent finite sets of objects indexed by arbitrary index
sets. The subscript notation "a[k]" selects the item indexed by "k"
from the mapping "a"; this can be used in expressions and as the
target of assignments or "del" statements. The built-in function
"len()" returns the number of items in a mapping.

There is currently a single intrinsic mapping type:


Dictionaries
------------

These represent finite sets of objects indexed by nearly arbitrary
values.  The only types of values not acceptable as keys are values
containing lists or dictionaries or other mutable types that are
compared by value rather than by object identity, the reason being
that the efficient implementation of dictionaries requires a key\u2019s
hash value to remain constant. Numeric types used for keys obey the
normal rules for numeric comparison: if two numbers compare equal
(e.g., "1" and "1.0") then they can be used interchangeably to index
the same dictionary entry.

Dictionaries preserve insertion order, meaning that keys will be
produced in the same order they were added sequentially over the
dictionary. Replacing an existing key does not change the order,
however removing a key and re-inserting it will add it to the end
instead of keeping its old place.

Dictionaries are mutable; they can be created by the "{...}" notation
(see section Dictionary displays).

The extension modules "dbm.ndbm" and "dbm.gnu" provide additional
examples of mapping types, as does the "collections" module.

Changed in version 3.7: Dictionaries did not preserve insertion order
in versions of Python before 3.6. In CPython 3.6, insertion order was
preserved, but it was considered an implementation detail at that time
rather than a language guarantee.


Callable types
==============

These are the types to which the function call operation (see section
Calls) can be applied:


User-defined functions
----------------------

A user-defined function object is created by a function definition
(see section Function definitions).  It should be called with an
argument list containing the same number of items as the function\u2019s
formal parameter list.

Special attributes:

+---------------------------+---------------------------------+-------------+
| Attribute                 | Meaning                         |             |
|===========================|=================================|=============|
| "__doc__"                 | The function\u2019s documentation    | Writable    |
|                           | string, or "None" if            |             |
|                           | unavailable; not inherited by   |             |
|                           | subclasses.                     |             |
+---------------------------+---------------------------------+-------------+
| "__name__"                | The function\u2019s name.            | Writable    |
+---------------------------+---------------------------------+-------------+
| "__qualname__"            | The function\u2019s *qualified       | Writable    |
|                           | name*.  New in version 3.3.     |             |
+---------------------------+---------------------------------+-------------+
| "__module__"              | The name of the module the      | Writable    |
|                           | function was defined in, or     |             |
|                           | "None" if unavailable.          |             |
+---------------------------+---------------------------------+-------------+
| "__defaults__"            | A tuple containing default      | Writable    |
|                           | argument values for those       |             |
|                           | arguments that have defaults,   |             |
|                           | or "None" if no arguments have  |             |
|                           | a default value.                |             |
+---------------------------+---------------------------------+-------------+
| "__code__"                | The code object representing    | Writable    |
|                           | the compiled function body.     |             |
+---------------------------+---------------------------------+-------------+
| "__globals__"             | A reference to the dictionary   | Read-only   |
|                           | that holds the function\u2019s       |             |
|                           | global variables \u2014 the global   |             |
|                           | namespace of the module in      |             |
|                           | which the function was defined. |             |
+---------------------------+---------------------------------+-------------+
| "__dict__"                | The namespace supporting        | Writable    |
|                           | arbitrary function attributes.  |             |
+---------------------------+---------------------------------+-------------+
| "__closure__"             | "None" or a tuple of cells that | Read-only   |
|                           | contain bindings for the        |             |
|                           | function\u2019s free variables. See  |             |
|                           | below for information on the    |             |
|                           | "cell_contents" attribute.      |             |
+---------------------------+---------------------------------+-------------+
| "__annotations__"         | A dict containing annotations   | Writable    |
|                           | of parameters.  The keys of the |             |
|                           | dict are the parameter names,   |             |
|                           | and "'return'" for the return   |             |
|                           | annotation, if provided.  For   |             |
|                           | more information on working     |             |
|                           | with this attribute, see        |             |
|                           | Annotations Best Practices.     |             |
+---------------------------+---------------------------------+-------------+
| "__kwdefaults__"          | A dict containing defaults for  | Writable    |
|                           | keyword-only parameters.        |             |
+---------------------------+---------------------------------+-------------+
| "__type_params__"         | A tuple containing the type     | Writable    |
|                           | parameters of a generic         |             |
|                           | function.                       |             |
+---------------------------+---------------------------------+-------------+

Most of the attributes labelled \u201cWritable\u201d check the type of the
assigned value.

Function objects also support getting and setting arbitrary
attributes, which can be used, for example, to attach metadata to
functions.  Regular attribute dot-notation is used to get and set such
attributes. *Note that the current implementation only supports
function attributes on user-defined functions. Function attributes on
built-in functions may be supported in the future.*

A cell object has the attribute "cell_contents". This can be used to
get the value of the cell, as well as set the value.

Additional information about a function\u2019s definition can be retrieved
from its code object; see the description of internal types below. The
"cell" type can be accessed in the "types" module.


Instance methods
----------------

An instance method object combines a class, a class instance and any
callable object (normally a user-defined function).

Special read-only attributes: "__self__" is the class instance object,
"__func__" is the function object; "__doc__" is the method\u2019s
documentation (same as "__func__.__doc__"); "__name__" is the method
name (same as "__func__.__name__"); "__module__" is the name of the
module the method was defined in, or "None" if unavailable.

Methods also support accessing (but not setting) the arbitrary
function attributes on the underlying function object.

User-defined method objects may be created when getting an attribute
of a class (perhaps via an instance of that class), if that attribute
is a user-defined function object or a class method object.

When an instance method object is created by retrieving a user-defined
function object from a class via one of its instances, its "__self__"
attribute is the instance, and the method object is said to be bound.
The new method\u2019s "__func__" attribute is the original function object.

When an instance method object is created by retrieving a class method
object from a class or instance, its "__self__" attribute is the class
itself, and its "__func__" attribute is the function object underlying
the class method.

When an instance method object is called, the underlying function
("__func__") is called, inserting the class instance ("__self__") in
front of the argument list.  For instance, when "C" is a class which
contains a definition for a function "f()", and "x" is an instance of
"C", calling "x.f(1)" is equivalent to calling "C.f(x, 1)".

When an instance method object is derived from a class method object,
the \u201cclass instance\u201d stored in "__self__" will actually be the class
itself, so that calling either "x.f(1)" or "C.f(1)" is equivalent to
calling "f(C,1)" where "f" is the underlying function.

Note that the transformation from function object to instance method
object happens each time the attribute is retrieved from the instance.
In some cases, a fruitful optimization is to assign the attribute to a
local variable and call that local variable. Also notice that this
transformation only happens for user-defined functions; other callable
objects (and all non-callable objects) are retrieved without
transformation.  It is also important to note that user-defined
functions which are attributes of a class instance are not converted
to bound methods; this *only* happens when the function is an
attribute of the class.


Generator functions
-------------------

A function or method which uses the "yield" statement (see section The
yield statement) is called a *generator function*.  Such a function,
when called, always returns an *iterator* object which can be used to
execute the body of the function:  calling the iterator\u2019s
"iterator.__next__()" method will cause the function to execute until
it provides a value using the "yield" statement.  When the function
executes a "return" statement or falls off the end, a "StopIteration"
exception is raised and the iterator will have reached the end of the
set of values to be returned.


Coroutine functions
-------------------

A function or method which is defined using "async def" is called a
*coroutine function*.  Such a function, when called, returns a
*coroutine* object.  It may contain "await" expressions, as well as
"async with" and "async for" statements. See also the Coroutine
Objects section.


Asynchronous generator functions
--------------------------------

A function or method which is defined using "async def" and which uses
the "yield" statement is called a *asynchronous generator function*.
Such a function, when called, returns an *asynchronous iterator*
object which can be used in an "async for" statement to execute the
body of the function.

Calling the asynchronous iterator\u2019s "aiterator.__anext__" method will
return an *awaitable* which when awaited will execute until it
provides a value using the "yield" expression.  When the function
executes an empty "return" statement or falls off the end, a
"StopAsyncIteration" exception is raised and the asynchronous iterator
will have reached the end of the set of values to be yielded.


Built-in functions
------------------

A built-in function object is a wrapper around a C function.  Examples
of built-in functions are "len()" and "math.sin()" ("math" is a
standard built-in module). The number and type of the arguments are
determined by the C function. Special read-only attributes: "__doc__"
is the function\u2019s documentation string, or "None" if unavailable;
"__name__" is the function\u2019s name; "__self__" is set to "None" (but
see the next item); "__module__" is the name of the module the
function was defined in or "None" if unavailable.


Built-in methods
----------------

This is really a different disguise of a built-in function, this time
containing an object passed to the C function as an implicit extra
argument.  An example of a built-in method is "alist.append()",
assuming *alist* is a list object. In this case, the special read-only
attribute "__self__" is set to the object denoted by *alist*.


Classes
-------

Classes are callable.  These objects normally act as factories for new
instances of themselves, but variations are possible for class types
that override "__new__()".  The arguments of the call are passed to
"__new__()" and, in the typical case, to "__init__()" to initialize
the new instance.


Class Instances
---------------

Instances of arbitrary classes can be made callable by defining a
"__call__()" method in their class.


Modules
=======

Modules are a basic organizational unit of Python code, and are
created by the import system as invoked either by the "import"
statement, or by calling functions such as "importlib.import_module()"
and built-in "__import__()".  A module object has a namespace
implemented by a dictionary object (this is the dictionary referenced
by the "__globals__" attribute of functions defined in the module).
Attribute references are translated to lookups in this dictionary,
e.g., "m.x" is equivalent to "m.__dict__["x"]". A module object does
not contain the code object used to initialize the module (since it
isn\u2019t needed once the initialization is done).

Attribute assignment updates the module\u2019s namespace dictionary, e.g.,
"m.x = 1" is equivalent to "m.__dict__["x"] = 1".

Predefined (writable) attributes:

   "__name__"
      The module\u2019s name.

   "__doc__"
      The module\u2019s documentation string, or "None" if unavailable.

   "__file__"
      The pathname of the file from which the module was loaded, if it
      was loaded from a file. The "__file__" attribute may be missing
      for certain types of modules, such as C modules that are
      statically linked into the interpreter.  For extension modules
      loaded dynamically from a shared library, it\u2019s the pathname of
      the shared library file.

   "__annotations__"
      A dictionary containing *variable annotations* collected during
      module body execution.  For best practices on working with
      "__annotations__", please see Annotations Best Practices.

Special read-only attribute: "__dict__" is the module\u2019s namespace as a
dictionary object.

**CPython implementation detail:** Because of the way CPython clears
module dictionaries, the module dictionary will be cleared when the
module falls out of scope even if the dictionary still has live
references.  To avoid this, copy the dictionary or keep the module
around while using its dictionary directly.


Custom classes
==============

Custom class types are typically created by class definitions (see
section Class definitions).  A class has a namespace implemented by a
dictionary object. Class attribute references are translated to
lookups in this dictionary, e.g., "C.x" is translated to
"C.__dict__["x"]" (although there are a number of hooks which allow
for other means of locating attributes). When the attribute name is
not found there, the attribute search continues in the base classes.
This search of the base classes uses the C3 method resolution order
which behaves correctly even in the presence of \u2018diamond\u2019 inheritance
structures where there are multiple inheritance paths leading back to
a common ancestor. Additional details on the C3 MRO used by Python can
be found in the documentation accompanying the 2.3 release at
https://www.python.org/download/releases/2.3/mro/.

When a class attribute reference (for class "C", say) would yield a
class method object, it is transformed into an instance method object
whose "__self__" attribute is "C".  When it would yield a static
method object, it is transformed into the object wrapped by the static
method object. See section Implementing Descriptors for another way in
which attributes retrieved from a class may differ from those actually
contained in its "__dict__".

Class attribute assignments update the class\u2019s dictionary, never the
dictionary of a base class.

A class object can be called (see above) to yield a class instance
(see below).

Special attributes:

   "__name__"
      The class name.

   "__module__"
      The name of the module in which the class was defined.

   "__dict__"
      The dictionary containing the class\u2019s namespace.

   "__bases__"
      A tuple containing the base classes, in the order of their
      occurrence in the base class list.

   "__doc__"
      The class\u2019s documentation string, or "None" if undefined.

   "__annotations__"
      A dictionary containing *variable annotations* collected during
      class body execution.  For best practices on working with
      "__annotations__", please see Annotations Best Practices.

   "__type_params__"
      A tuple containing the type parameters of a generic class.


Class instances
===============

A class instance is created by calling a class object (see above).  A
class instance has a namespace implemented as a dictionary which is
the first place in which attribute references are searched.  When an
attribute is not found there, and the instance\u2019s class has an
attribute by that name, the search continues with the class
attributes.  If a class attribute is found that is a user-defined
function object, it is transformed into an instance method object
whose "__self__" attribute is the instance.  Static method and class
method objects are also transformed; see above under \u201cClasses\u201d.  See
section Implementing Descriptors for another way in which attributes
of a class retrieved via its instances may differ from the objects
actually stored in the class\u2019s "__dict__".  If no class attribute is
found, and the object\u2019s class has a "__getattr__()" method, that is
called to satisfy the lookup.

Attribute assignments and deletions update the instance\u2019s dictionary,
never a class\u2019s dictionary.  If the class has a "__setattr__()" or
"__delattr__()" method, this is called instead of updating the
instance dictionary directly.

Class instances can pretend to be numbers, sequences, or mappings if
they have methods with certain special names.  See section Special
method names.

Special attributes: "__dict__" is the attribute dictionary;
"__class__" is the instance\u2019s class.


I/O objects (also known as file objects)
========================================

A *file object* represents an open file.  Various shortcuts are
available to create file objects: the "open()" built-in function, and
also "os.popen()", "os.fdopen()", and the "makefile()" method of
socket objects (and perhaps by other functions or methods provided by
extension modules).

The objects "sys.stdin", "sys.stdout" and "sys.stderr" are initialized
to file objects corresponding to the interpreter\u2019s standard input,
output and error streams; they are all open in text mode and therefore
follow the interface defined by the "io.TextIOBase" abstract class.


Internal types
==============

A few types used internally by the interpreter are exposed to the
user. Their definitions may change with future versions of the
interpreter, but they are mentioned here for completeness.


Code objects
------------

Code objects represent *byte-compiled* executable Python code, or
*bytecode*. The difference between a code object and a function object
is that the function object contains an explicit reference to the
function\u2019s globals (the module in which it was defined), while a code
object contains no context; also the default argument values are
stored in the function object, not in the code object (because they
represent values calculated at run-time).  Unlike function objects,
code objects are immutable and contain no references (directly or
indirectly) to mutable objects.

Special read-only attributes: "co_name" gives the function name;
"co_qualname" gives the fully qualified function name; "co_argcount"
is the total number of positional arguments (including positional-only
arguments and arguments with default values); "co_posonlyargcount" is
the number of positional-only arguments (including arguments with
default values); "co_kwonlyargcount" is the number of keyword-only
arguments (including arguments with default values); "co_nlocals" is
the number of local variables used by the function (including
arguments); "co_varnames" is a tuple containing the names of the local
variables (starting with the argument names); "co_cellvars" is a tuple
containing the names of local variables that are referenced by nested
functions; "co_freevars" is a tuple containing the names of free
variables; "co_code" is a string representing the sequence of bytecode
instructions; "co_consts" is a tuple containing the literals used by
the bytecode; "co_names" is a tuple containing the names used by the
bytecode; "co_filename" is the filename from which the code was
compiled; "co_firstlineno" is the first line number of the function;
"co_lnotab" is a string encoding the mapping from bytecode offsets to
line numbers (for details see the source code of the interpreter, is
deprecated since 3.12 and may be removed in 3.14); "co_stacksize" is
the required stack size; "co_flags" is an integer encoding a number of
flags for the interpreter.

The following flag bits are defined for "co_flags": bit "0x04" is set
if the function uses the "*arguments" syntax to accept an arbitrary
number of positional arguments; bit "0x08" is set if the function uses
the "**keywords" syntax to accept arbitrary keyword arguments; bit
"0x20" is set if the function is a generator.

Future feature declarations ("from __future__ import division") also
use bits in "co_flags" to indicate whether a code object was compiled
with a particular feature enabled: bit "0x2000" is set if the function
was compiled with future division enabled; bits "0x10" and "0x1000"
were used in earlier versions of Python.

Other bits in "co_flags" are reserved for internal use.

If a code object represents a function, the first item in "co_consts"
is the documentation string of the function, or "None" if undefined.

codeobject.co_positions()

   Returns an iterable over the source code positions of each bytecode
   instruction in the code object.

   The iterator returns tuples containing the "(start_line, end_line,
   start_column, end_column)". The *i-th* tuple corresponds to the
   position of the source code that compiled to the *i-th*
   instruction. Column information is 0-indexed utf-8 byte offsets on
   the given source line.

   This positional information can be missing. A non-exhaustive lists
   of cases where this may happen:

   * Running the interpreter with "-X" "no_debug_ranges".

   * Loading a pyc file compiled while using "-X" "no_debug_ranges".

   * Position tuples corresponding to artificial instructions.

   * Line and column numbers that can\u2019t be represented due to
     implementation specific limitations.

   When this occurs, some or all of the tuple elements can be "None".

   New in version 3.11.

   Note:

     This feature requires storing column positions in code objects
     which may result in a small increase of disk usage of compiled
     Python files or interpreter memory usage. To avoid storing the
     extra information and/or deactivate printing the extra traceback
     information, the "-X" "no_debug_ranges" command line flag or the
     "PYTHONNODEBUGRANGES" environment variable can be used.


Frame objects
-------------

Frame objects represent execution frames.  They may occur in traceback
objects (see below), and are also passed to registered trace
functions.

Special read-only attributes: "f_back" is to the previous stack frame
(towards the caller), or "None" if this is the bottom stack frame;
"f_code" is the code object being executed in this frame; "f_locals"
is the dictionary used to look up local variables; "f_globals" is used
for global variables; "f_builtins" is used for built-in (intrinsic)
names; "f_lasti" gives the precise instruction (this is an index into
the bytecode string of the code object).

Accessing "f_code" raises an auditing event "object.__getattr__" with
arguments "obj" and ""f_code"".

Special writable attributes: "f_trace", if not "None", is a function
called for various events during code execution (this is used by the
debugger). Normally an event is triggered for each new source line -
this can be disabled by setting "f_trace_lines" to "False".

Implementations *may* allow per-opcode events to be requested by
setting "f_trace_opcodes" to "True". Note that this may lead to
undefined interpreter behaviour if exceptions raised by the trace
function escape to the function being traced.

"f_lineno" is the current line number of the frame \u2014 writing to this
from within a trace function jumps to the given line (only for the
bottom-most frame).  A debugger can implement a Jump command (aka Set
Next Statement) by writing to f_lineno.

Frame objects support one method:

frame.clear()

   This method clears all references to local variables held by the
   frame.  Also, if the frame belonged to a generator, the generator
   is finalized.  This helps break reference cycles involving frame
   objects (for example when catching an exception and storing its
   traceback for later use).

   "RuntimeError" is raised if the frame is currently executing.

   New in version 3.4.


Traceback objects
-----------------

Traceback objects represent a stack trace of an exception.  A
traceback object is implicitly created when an exception occurs, and
may also be explicitly created by calling "types.TracebackType".

For implicitly created tracebacks, when the search for an exception
handler unwinds the execution stack, at each unwound level a traceback
object is inserted in front of the current traceback.  When an
exception handler is entered, the stack trace is made available to the
program. (See section The try statement.) It is accessible as the
third item of the tuple returned by "sys.exc_info()", and as the
"__traceback__" attribute of the caught exception.

When the program contains no suitable handler, the stack trace is
written (nicely formatted) to the standard error stream; if the
interpreter is interactive, it is also made available to the user as
"sys.last_traceback".

For explicitly created tracebacks, it is up to the creator of the
traceback to determine how the "tb_next" attributes should be linked
to form a full stack trace.

Special read-only attributes: "tb_frame" points to the execution frame
of the current level; "tb_lineno" gives the line number where the
exception occurred; "tb_lasti" indicates the precise instruction. The
line number and last instruction in the traceback may differ from the
line number of its frame object if the exception occurred in a "try"
statement with no matching except clause or with a finally clause.

Accessing "tb_frame" raises an auditing event "object.__getattr__"
with arguments "obj" and ""tb_frame"".

Special writable attribute: "tb_next" is the next level in the stack
trace (towards the frame where the exception occurred), or "None" if
there is no next level.

Changed in version 3.7: Traceback objects can now be explicitly
instantiated from Python code, and the "tb_next" attribute of existing
instances can be updated.


Slice objects
-------------

Slice objects are used to represent slices for "__getitem__()"
methods.  They are also created by the built-in "slice()" function.

Special read-only attributes: "start" is the lower bound; "stop" is
the upper bound; "step" is the step value; each is "None" if omitted.
These attributes can have any type.

Slice objects support one method:

slice.indices(self, length)

   This method takes a single integer argument *length* and computes
   information about the slice that the slice object would describe if
   applied to a sequence of *length* items.  It returns a tuple of
   three integers; respectively these are the *start* and *stop*
   indices and the *step* or stride length of the slice. Missing or
   out-of-bounds indices are handled in a manner consistent with
   regular slices.


Static method objects
---------------------

Static method objects provide a way of defeating the transformation of
function objects to method objects described above. A static method
object is a wrapper around any other object, usually a user-defined
method object. When a static method object is retrieved from a class
or a class instance, the object actually returned is the wrapped
object, which is not subject to any further transformation. Static
method objects are also callable. Static method objects are created by
the built-in "staticmethod()" constructor.


Class method objects
--------------------

A class method object, like a static method object, is a wrapper
around another object that alters the way in which that object is
retrieved from classes and class instances. The behaviour of class
method objects upon such retrieval is described above, under \u201cUser-
defined methods\u201d. Class method objects are created by the built-in
"classmethod()" constructor.

Related help topics: class, SPECIALMETHODS, PRIVATENAMES
"""
#help('class')

"""
Class definitions
*****************

A class definition defines a class object (see section The standard
type hierarchy):

   classdef    ::= [decorators] "class" classname [type_params] [inheritance] ":" suite
   inheritance ::= "(" [argument_list] ")"
   classname   ::= identifier

A class definition is an executable statement.  The inheritance list
usually gives a list of base classes (see Metaclasses for more
advanced uses), so each item in the list should evaluate to a class
object which allows subclassing.  Classes without an inheritance list
inherit, by default, from the base class "object"; hence,

   class Foo:
       pass

is equivalent to

   class Foo(object):
       pass

The class\u2019s suite is then executed in a new execution frame (see
Naming and binding), using a newly created local namespace and the
original global namespace. (Usually, the suite contains mostly
function definitions.)  When the class\u2019s suite finishes execution, its
execution frame is discarded but its local namespace is saved. [5] A
class object is then created using the inheritance list for the base
classes and the saved local namespace for the attribute dictionary.
The class name is bound to this class object in the original local
namespace.

The order in which attributes are defined in the class body is
preserved in the new class\u2019s "__dict__".  Note that this is reliable
only right after the class is created and only for classes that were
defined using the definition syntax.

Class creation can be customized heavily using metaclasses.

Classes can also be decorated: just like when decorating functions,

   @f1(arg)
   @f2
   class Foo: pass

is roughly equivalent to

   class Foo: pass
   Foo = f1(arg)(f2(Foo))

The evaluation rules for the decorator expressions are the same as for
function decorators.  The result is then bound to the class name.

Changed in version 3.9: Classes may be decorated with any valid
"assignment_expression". Previously, the grammar was much more
restrictive; see **PEP 614** for details.

A list of type parameters may be given in square brackets immediately
after the class\u2019s name. This indicates to static type checkers that
the class is generic. At runtime, the type parameters can be retrieved
from the class\u2019s "__type_params__" attribute. See Generic classes for
more.

Changed in version 3.12: Type parameter lists are new in Python 3.12.

**Programmer\u2019s note:** Variables defined in the class definition are
class attributes; they are shared by instances.  Instance attributes
can be set in a method with "self.name = value".  Both class and
instance attributes are accessible through the notation \u201c"self.name"\u201d,
and an instance attribute hides a class attribute with the same name
when accessed in this way.  Class attributes can be used as defaults
for instance attributes, but using mutable values there can lead to
unexpected results.  Descriptors can be used to create instance
variables with different implementation details.

See also:

  **PEP 3115** - Metaclasses in Python 3000
     The proposal that changed the declaration of metaclasses to the
     current syntax, and the semantics for how classes with
     metaclasses are constructed.

  **PEP 3129** - Class Decorators
     The proposal that added class decorators.  Function and method
     decorators were introduced in **PEP 318**.

Related help topics: CLASSES, SPECIALMETHODS
"""