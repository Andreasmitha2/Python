# encoding: utf-8
# module zmq.backend.cython.constants
# from C:\test.env\lib\site-packages\zmq\backend\cython\constants.pyd
# by generator 1.135
""" 0MQ Constants. """

# imports
import __builtin__ as __builtins__ # <module '__builtin__' (built-in)>

# Variables with simple values

AFFINITY = 4

BACKLOG = 19

CONFLATE = 54

CONNECT_RID = -1

CURVE = 2

CURVE_PUBLICKEY = 48
CURVE_SECRETKEY = 49
CURVE_SERVER = 47
CURVE_SERVERKEY = 50

DEALER = 5

DELAY_ATTACH_ON_CONNECT = 39

DONTWAIT = 1
DOWNSTREAM = -1

EADDRINUSE = 156384717
EADDRNOTAVAIL = 156384718
EAFNOSUPPORT = 156384723
EAGAIN = 11

ECONNABORTED = 156384725
ECONNREFUSED = 156384719
ECONNRESET = 156384726

EFAULT = 14
EFSM = 156384763

EHOSTUNREACH = 156384729

EINPROGRESS = 156384720
EINVAL = 22

EMSGSIZE = 156384722
EMTHREAD = 156384766

ENETDOWN = 156384716
ENETRESET = 156384730
ENETUNREACH = 156384724
ENOBUFS = 156384715
ENOCOMPATPROTO = 156384764
ENODEV = 19
ENOMEM = 12
ENOTCONN = 156384727
ENOTSOCK = 156384721
ENOTSUP = 156384713

EPROTONOSUPPORT = 156384714

ETERM = 156384765
ETIMEDOUT = 156384728

EVENTS = 15

EVENT_ACCEPTED = 32

EVENT_ACCEPT_FAILED = 64

EVENT_ALL = 2047

EVENT_BIND_FAILED = 16

EVENT_CLOSED = 128

EVENT_CLOSE_FAILED = 256

EVENT_CONNECTED = 1

EVENT_CONNECT_DELAYED = 2
EVENT_CONNECT_RETRIED = 4

EVENT_DISCONNECTED = 512
EVENT_LISTENING = 8

EVENT_MONITOR_STOPPED = 1024

FAIL_UNROUTABLE = 33

FD = 14

FORWARDER = 2

HAUSNUMERO = 156384712

HWM = -1

IDENTITY = 5

IMMEDIATE = 39

IO_THREADS = 1

IO_THREADS_DFLT = 1

IPC_FILTER_GID = -1
IPC_FILTER_PID = -1
IPC_FILTER_UID = -1

IPV4ONLY = 31
IPV6 = 42

LAST_ENDPOINT = 32

LINGER = 17

MAXMSGSIZE = 22

MAX_SOCKETS = 2

MAX_SOCKETS_DFLT = 1023

MCAST_LOOP = -1

MECHANISM = 43

MORE = 1

MULTICAST_HOPS = 25

NOBLOCK = 1

NULL = 0

PAIR = 0

PLAIN = 1

PLAIN_PASSWORD = 46
PLAIN_SERVER = 44
PLAIN_USERNAME = 45

POLLERR = 4
POLLIN = 1
POLLOUT = 2

PROBE_ROUTER = 51

PUB = 1
PULL = 7
PUSH = 8

QUEUE = 3

RATE = 8

RCVBUF = 12
RCVHWM = 24
RCVMORE = 13
RCVTIMEO = 27

RECONNECT_IVL = 18

RECONNECT_IVL_MAX = 21

RECOVERY_IVL = 9

RECOVERY_IVL_MSEC = -1

REP = 4
REQ = 3

REQ_CORRELATE = 52
REQ_RELAXED = 53

ROUTER = 6

ROUTER_BEHAVIOR = 33
ROUTER_HANDOVER = -1
ROUTER_MANDATORY = 33
ROUTER_RAW = 41

SNDBUF = 11
SNDHWM = 23
SNDMORE = 2
SNDTIMEO = 28

STREAM = 11
STREAMER = 1

SUB = 2
SUBSCRIBE = 6

SWAP = -1

TCP_ACCEPT_FILTER = 38

TCP_KEEPALIVE = 34

TCP_KEEPALIVE_CNT = 35
TCP_KEEPALIVE_IDLE = 36
TCP_KEEPALIVE_INTVL = 37

TOS = -1

TYPE = 16

UNSUBSCRIBE = 7

UPSTREAM = -1

VERSION = 40004

VERSION_MAJOR = 4
VERSION_MINOR = 0
VERSION_PATCH = 4

XPUB = 9

XPUB_VERBOSE = 40

XSUB = 10

ZAP_DOMAIN = 55

# no functions
# no classes
# variables with complex values

__all__ = [
    'VERSION',
    'VERSION_MAJOR',
    'VERSION_MINOR',
    'VERSION_PATCH',
    'NOBLOCK',
    'DONTWAIT',
    'POLLIN',
    'POLLOUT',
    'POLLERR',
    'SNDMORE',
    'STREAMER',
    'FORWARDER',
    'QUEUE',
    'IO_THREADS_DFLT',
    'MAX_SOCKETS_DFLT',
    'PAIR',
    'PUB',
    'SUB',
    'REQ',
    'REP',
    'DEALER',
    'ROUTER',
    'PULL',
    'PUSH',
    'XPUB',
    'XSUB',
    'UPSTREAM',
    'DOWNSTREAM',
    'STREAM',
    'EVENT_CONNECTED',
    'EVENT_CONNECT_DELAYED',
    'EVENT_CONNECT_RETRIED',
    'EVENT_LISTENING',
    'EVENT_BIND_FAILED',
    'EVENT_ACCEPTED',
    'EVENT_ACCEPT_FAILED',
    'EVENT_CLOSED',
    'EVENT_CLOSE_FAILED',
    'EVENT_DISCONNECTED',
    'EVENT_ALL',
    'EVENT_MONITOR_STOPPED',
    'NULL',
    'PLAIN',
    'CURVE',
    'EAGAIN',
    'EINVAL',
    'EFAULT',
    'ENOMEM',
    'ENODEV',
    'EMSGSIZE',
    'EAFNOSUPPORT',
    'ENETUNREACH',
    'ECONNABORTED',
    'ECONNRESET',
    'ENOTCONN',
    'ETIMEDOUT',
    'EHOSTUNREACH',
    'ENETRESET',
    'HAUSNUMERO',
    'ENOTSUP',
    'EPROTONOSUPPORT',
    'ENOBUFS',
    'ENETDOWN',
    'EADDRINUSE',
    'EADDRNOTAVAIL',
    'ECONNREFUSED',
    'EINPROGRESS',
    'ENOTSOCK',
    'EFSM',
    'ENOCOMPATPROTO',
    'ETERM',
    'EMTHREAD',
    'IO_THREADS',
    'MAX_SOCKETS',
    'MORE',
    'IDENTITY',
    'SUBSCRIBE',
    'UNSUBSCRIBE',
    'LAST_ENDPOINT',
    'TCP_ACCEPT_FILTER',
    'PLAIN_USERNAME',
    'PLAIN_PASSWORD',
    'CURVE_PUBLICKEY',
    'CURVE_SECRETKEY',
    'CURVE_SERVERKEY',
    'ZAP_DOMAIN',
    'CONNECT_RID',
    'RECONNECT_IVL_MAX',
    'SNDTIMEO',
    'RCVTIMEO',
    'SNDHWM',
    'RCVHWM',
    'MULTICAST_HOPS',
    'IPV4ONLY',
    'ROUTER_BEHAVIOR',
    'TCP_KEEPALIVE',
    'TCP_KEEPALIVE_CNT',
    'TCP_KEEPALIVE_IDLE',
    'TCP_KEEPALIVE_INTVL',
    'DELAY_ATTACH_ON_CONNECT',
    'XPUB_VERBOSE',
    'FD',
    'EVENTS',
    'TYPE',
    'LINGER',
    'RECONNECT_IVL',
    'BACKLOG',
    'ROUTER_MANDATORY',
    'FAIL_UNROUTABLE',
    'ROUTER_RAW',
    'IMMEDIATE',
    'IPV6',
    'MECHANISM',
    'PLAIN_SERVER',
    'CURVE_SERVER',
    'PROBE_ROUTER',
    'REQ_RELAXED',
    'REQ_CORRELATE',
    'CONFLATE',
    'ROUTER_HANDOVER',
    'TOS',
    'IPC_FILTER_PID',
    'IPC_FILTER_UID',
    'IPC_FILTER_GID',
    'AFFINITY',
    'MAXMSGSIZE',
    'HWM',
    'SWAP',
    'MCAST_LOOP',
    'RECOVERY_IVL_MSEC',
    'RATE',
    'RECOVERY_IVL',
    'SNDBUF',
    'RCVBUF',
    'RCVMORE',
]

__test__ = {}
