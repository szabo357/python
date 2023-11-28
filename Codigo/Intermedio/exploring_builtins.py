# references
# https://www.w3schools.com/python/python_ref_functions.asp
# https://docs.python.org/3/library/functions.html
# https://mathspp.com/blog/pydonts/dunder-methods

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

help('CLASSES')
