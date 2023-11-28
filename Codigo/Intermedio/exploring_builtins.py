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


help('BASICMETHODS')
help('CLASSES')
