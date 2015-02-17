from collections import namedtuple
from ._wrapper import lib, ffi


class Right(namedtuple('Right', 'name value')):
    ALL = set()

    def __new__(cls, *args, **kwargs):
        ret = super(Right, cls).__new__(cls, *args, **kwargs)
        cls.ALL.add(ret)
        return ret

    def __int__(self):
        return self.value

    def __iter__(self):
        raise NotImplementedError


CAP_ACCEPT = Right("CAP_ACCEPT", lib.CAP_ACCEPT)
CAP_ACL_CHECK = Right('CAP_ACL_CHECK', lib.CAP_ACL_CHECK)
CAP_ACL_DELETE = Right('CAP_ACL_DELETE', lib.CAP_ACL_DELETE)
CAP_ACL_GET = Right('CAP_ACL_GET', lib.CAP_ACL_GET)
CAP_ACL_SET = Right('CAP_ACL_SET', lib.CAP_ACL_SET)
CAP_BIND = Right('CAP_BIND', lib.CAP_BIND)
CAP_BINDAT = Right('CAP_BINDAT', lib.CAP_BINDAT)
CAP_CHFLAGSAT = Right('CAP_CHFLAGSAT', lib.CAP_CHFLAGSAT)
CAP_CONNECT = Right('CAP_CONNECT', lib.CAP_CONNECT)
CAP_CONNECTAT = Right('CAP_CONNECTAT', lib.CAP_CONNECTAT)
CAP_CREATE = Right('CAP_CREATE', lib.CAP_CREATE)
CAP_EVENT = Right('CAP_EVENT', lib.CAP_EVENT)
CAP_EXTATTR_DELETE = Right('CAP_EXTATTR_DELETE', lib.CAP_EXTATTR_DELETE)
CAP_EXTATTR_GET = Right('CAP_EXTATTR_GET', lib.CAP_EXTATTR_GET)
CAP_EXTATTR_LIST = Right('CAP_EXTATTR_LIST', lib.CAP_EXTATTR_LIST)
CAP_EXTATTR_SET = Right('CAP_EXTATTR_SET', lib.CAP_EXTATTR_SET)
CAP_FCHDIR = Right('CAP_FCHDIR', lib.CAP_FCHDIR)
CAP_FCHFLAGS = Right('CAP_FCHFLAGS', lib.CAP_FCHFLAGS)
CAP_FCHMOD = Right('CAP_FCHMOD', lib.CAP_FCHMOD)
CAP_FCHMODAT = Right('CAP_FCHMODAT', lib.CAP_FCHMODAT)
CAP_FCHOWN = Right('CAP_FCHOWN', lib.CAP_FCHOWN)
CAP_FCHOWNAT = Right('CAP_FCHOWNAT', lib.CAP_FCHOWNAT)
CAP_FCNTL = Right('CAP_FCNTL', lib.CAP_FCNTL)
CAP_FEXECVE = Right('CAP_FEXECVE', lib.CAP_FEXECVE)
CAP_FLOCK = Right('CAP_FLOCK', lib.CAP_FLOCK)
CAP_FPATHCONF = Right('CAP_FPATHCONF', lib.CAP_FPATHCONF)
CAP_FSCK = Right('CAP_FSCK', lib.CAP_FSCK)
CAP_FSTAT = Right('CAP_FSTAT', lib.CAP_FSTAT)
CAP_FSTATAT = Right('CAP_FSTATAT', lib.CAP_FSTATAT)
CAP_FSTATFS = Right('CAP_FSTATFS', lib.CAP_FSTATFS)
CAP_FSYNC = Right('CAP_FSYNC', lib.CAP_FSYNC)
CAP_FTRUNCATE = Right('CAP_FTRUNCATE', lib.CAP_FTRUNCATE)
CAP_FUTIMES = Right('CAP_FUTIMES', lib.CAP_FUTIMES)
CAP_FUTIMESAT = Right('CAP_FUTIMESAT', lib.CAP_FUTIMESAT)
CAP_GETPEERNAME = Right('CAP_GETPEERNAME', lib.CAP_GETPEERNAME)
CAP_GETSOCKNAME = Right('CAP_GETSOCKNAME', lib.CAP_GETSOCKNAME)
CAP_GETSOCKOPT = Right('CAP_GETSOCKOPT', lib.CAP_GETSOCKOPT)
CAP_IOCTL = Right('CAP_IOCTL', lib.CAP_IOCTL)
CAP_KQUEUE = Right('CAP_KQUEUE', lib.CAP_KQUEUE)
CAP_KQUEUE_CHANGE = Right('CAP_KQUEUE_CHANGE', lib.CAP_KQUEUE_CHANGE)
CAP_KQUEUE_EVENT = Right('CAP_KQUEUE_EVENT', lib.CAP_KQUEUE_EVENT)
CAP_LINKAT = Right('CAP_LINKAT', lib.CAP_LINKAT)
CAP_LISTEN = Right('CAP_LISTEN', lib.CAP_LISTEN)
CAP_LOOKUP = Right('CAP_LOOKUP', lib.CAP_LOOKUP)
CAP_MAC_GET = Right('CAP_MAC_GET', lib.CAP_MAC_GET)
CAP_MAC_SET = Right('CAP_MAC_SET', lib.CAP_MAC_SET)
CAP_MKDIRAT = Right('CAP_MKDIRAT', lib.CAP_MKDIRAT)
CAP_MKFIFOAT = Right('CAP_MKFIFOAT', lib.CAP_MKFIFOAT)
CAP_MKNODAT = Right('CAP_MKNODAT', lib.CAP_MKNODAT)
CAP_MMAP = Right('CAP_MMAP', lib.CAP_MMAP)
CAP_MMAP_R = Right('CAP_MMAP_R', lib.CAP_MMAP_R)
CAP_MMAP_RW = Right('CAP_MMAP_RW', lib.CAP_MMAP_RW)
CAP_MMAP_RWX = Right('CAP_MMAP_RWX', lib.CAP_MMAP_RWX)
CAP_MMAP_RX = Right('CAP_MMAP_RX', lib.CAP_MMAP_RX)
CAP_MMAP_W = Right('CAP_MMAP_W', lib.CAP_MMAP_W)
CAP_MMAP_WX = Right('CAP_MMAP_WX', lib.CAP_MMAP_WX)
CAP_MMAP_X = Right('CAP_MMAP_X', lib.CAP_MMAP_X)
CAP_PDGETPID = Right('CAP_PDGETPID', lib.CAP_PDGETPID)
CAP_PDKILL = Right('CAP_PDKILL', lib.CAP_PDKILL)
CAP_PDWAIT = Right('CAP_PDWAIT', lib.CAP_PDWAIT)
CAP_PEELOFF = Right('CAP_PEELOFF', lib.CAP_PEELOFF)
CAP_PREAD = Right('CAP_PREAD', lib.CAP_PREAD)
CAP_PWRITE = Right('CAP_PWRITE', lib.CAP_PWRITE)
CAP_READ = Right('CAP_READ', lib.CAP_READ)
CAP_RECV = Right('CAP_RECV', lib.CAP_RECV)
CAP_RENAMEAT = Right('CAP_RENAMEAT', lib.CAP_RENAMEAT)
CAP_SEEK = Right('CAP_SEEK', lib.CAP_SEEK)
CAP_SEM_GETVALUE = Right('CAP_SEM_GETVALUE', lib.CAP_SEM_GETVALUE)
CAP_SEM_POST = Right('CAP_SEM_POST', lib.CAP_SEM_POST)
CAP_SEM_WAIT = Right('CAP_SEM_WAIT', lib.CAP_SEM_WAIT)
CAP_SEND = Right('CAP_SEND', lib.CAP_SEND)
CAP_SETSOCKOPT = Right('CAP_SETSOCKOPT', lib.CAP_SETSOCKOPT)
CAP_SHUTDOWN = Right('CAP_SHUTDOWN', lib.CAP_SHUTDOWN)
CAP_SYMLINKAT = Right('CAP_SYMLINKAT', lib.CAP_SYMLINKAT)
CAP_TTYHOOK = Right('CAP_TTYHOOK', lib.CAP_TTYHOOK)
CAP_UNLINKAT = Right('CAP_UNLINKAT', lib.CAP_UNLINKAT)
CAP_WRITE = Right('CAP_WRITE', lib.CAP_WRITE)


class CapabilitiesError(Exception):

    def __init__(self, message, errno=None):
        super(CapabilitiesError, self).__init__(message)
        self.errno = errno


class Rights(object):
    _rights = None

    def __init__(self, *rights):
        bad = set(rights) - Right.ALL
        if bad:
            raise CapabilitiesError('Invalid rights: {}'.format(tuple(bad)))
