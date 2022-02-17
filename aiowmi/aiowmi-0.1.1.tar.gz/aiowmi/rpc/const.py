# MS/RPC Constants
MSRPC_REQUEST = 0x00
MSRPC_PING = 0x01
MSRPC_RESPONSE = 0x02
MSRPC_FAULT = 0x03
MSRPC_WORKING = 0x04
MSRPC_NOCALL = 0x05
MSRPC_REJECT = 0x06
MSRPC_ACK = 0x07
MSRPC_CL_CANCEL = 0x08
MSRPC_FACK = 0x09
MSRPC_CANCELACK = 0x0A
MSRPC_BIND = 0x0B
MSRPC_BINDACK = 0x0C
MSRPC_BINDNAK = 0x0D
MSRPC_ALTERCTX = 0x0E
MSRPC_ALTERCTX_R = 0x0F
MSRPC_AUTH3 = 0x10
MSRPC_SHUTDOWN = 0x11
MSRPC_CO_CANCEL = 0x12
MSRPC_ORPHANED = 0x13
MSRPC_RTS = 0x14

# MS/RPC Packet Flags
PFC_FIRST_FRAG = 0x01
PFC_LAST_FRAG = 0x02

# For PDU types bind, bind_ack, alter_context, and
# alter_context_resp, this flag MUST be interpreted as PFC_SUPPORT_HEADER_SIGN
MSRPC_SUPPORT_SIGN = 0x04

# For the
# remaining PDU types, this flag MUST be interpreted as PFC_PENDING_CANCEL.
MSRPC_PENDING_CANCEL = 0x04

PFC_RESERVED_1 = 0x08
PFC_CONC_MPX = 0x10
PFC_DID_NOT_EXECUTE = 0x20
PFC_MAYBE = 0x40
PFC_OBJECT_UUID = 0x80

# Auth Types - Security Providers
RPC_C_AUTHN_NONE = 0x00
RPC_C_AUTHN_GSS_NEGOTIATE = 0x09
RPC_C_AUTHN_WINNT = 0x0A
RPC_C_AUTHN_GSS_SCHANNEL = 0x0E
RPC_C_AUTHN_GSS_KERBEROS = 0x10
RPC_C_AUTHN_NETLOGON = 0x44
RPC_C_AUTHN_DEFAULT = 0xFF

# Auth Levels
RPC_C_AUTHN_LEVEL_NONE = 1
RPC_C_AUTHN_LEVEL_CONNECT = 2
RPC_C_AUTHN_LEVEL_CALL = 3
RPC_C_AUTHN_LEVEL_PKT = 4
RPC_C_AUTHN_LEVEL_PKT_INTEGRITY = 5
RPC_C_AUTHN_LEVEL_PKT_PRIVACY = 6

# Reasons for rejection of a context element,
# included in bind_ack result reason
rpc_provider_reason = {
    0: 'reason_not_specified',
    1: 'abstract_syntax_not_supported',
    2: 'proposed_transfer_syntaxes_not_supported',
    3: 'local_limit_exceeded',
    4: 'protocol_version_not_specified',
    8: 'authentication_type_not_recognized',
    9: 'invalid_checksum'
}

MSRPC_CONT_RESULT_ACCEPT = 0
MSRPC_CONT_RESULT_USER_REJECT = 1
MSRPC_CONT_RESULT_PROV_REJECT = 2

# Results of a presentation context negotiation
rpc_cont_def_result = {
    0: 'acceptance',
    1: 'user_rejection',
    2: 'provider_rejection'
}

# status codes, references:
# https://docs.microsoft.com/windows/desktop/Rpc/rpc-return-values
# https://msdn.microsoft.com/library/default.asp?url=/library/en-us/randz/
#    protocol/common_return_values.asp
# winerror.h
# https://www.opengroup.org/onlinepubs/9629399/apdxn.htm

ACCESS_DENIED = 0X00000005
AUTHENTICATION_TYPE_NOT_RECOGNIZED = 0X00000008
EPT_S_CANT_PERFORM_OP = 0X000006D8
RPC_S_INVALID_BOUND = 0X000006C6
RPC_S_CANNOT_SUPPORT = 0X000006E4
RPC_X_BAD_STUB_DATA = 0X000006F7
NCA_S_COMM_FAILURE = 0X1C010001
NCA_S_OP_RNG_ERROR = 0X1C010002
NCA_S_UNK_IF = 0X1C010003
NCA_S_WRONG_BOOT_TIME = 0X1C010006
NCA_S_YOU_CRASHED = 0X1C010009
NCA_S_PROTO_ERROR = 0X1C01000B
NCA_S_OUT_ARGS_TOO_BIG = 0X1C010013
NCA_S_SERVER_TOO_BUSY = 0X1C010014
NCA_S_FAULT_STRING_TOO_LONG = 0X1C010015
NCA_S_UNSUPPORTED_TYPE = 0X1C010017
NCA_S_FAULT_INT_DIV_BY_ZERO = 0X1C000001
NCA_S_FAULT_ADDR_ERROR = 0X1C000002
NCA_S_FAULT_FP_DIV_ZERO = 0X1C000003
NCA_S_FAULT_FP_UNDERFLOW = 0X1C000004
NCA_S_FAULT_FP_OVERFLOW = 0X1C000005
NCA_S_FAULT_INVALID_TAG = 0X1C000006
NCA_S_FAULT_INVALID_BOUND = 0X1C000007
NCA_S_RPC_VERSION_MISMATCH = 0X1C000008
NCA_S_UNSPEC_REJECT = 0X1C000009
NCA_S_BAD_ACTID = 0X1C00000A
NCA_S_WHO_ARE_YOU_FAILED = 0X1C00000B
NCA_S_MANAGER_NOT_ENTERED = 0X1C00000C
NCA_S_FAULT_CANCEL = 0X1C00000D
NCA_S_FAULT_ILL_INST = 0X1C00000E
NCA_S_FAULT_FP_ERROR = 0X1C00000F
NCA_S_FAULT_INT_OVERFLOW = 0X1C000010
NCA_S_FAULT_UNSPEC = 0X1C000012
NCA_S_FAULT_REMOTE_COMM_FAILURE = 0X1C000013
NCA_S_FAULT_PIPE_EMPTY = 0X1C000014
NCA_S_FAULT_PIPE_CLOSED = 0X1C000015
NCA_S_FAULT_PIPE_ORDER = 0X1C000016
NCA_S_FAULT_PIPE_DISCIPLINE = 0X1C000017
NCA_S_FAULT_PIPE_COMM_ERROR = 0X1C000018
NCA_S_FAULT_PIPE_MEMORY = 0X1C000019
NCA_S_FAULT_CONTEXT_MISMATCH = 0X1C00001A
NCA_S_FAULT_REMOTE_NO_MEMORY = 0X1C00001B
NCA_S_INVALID_PRES_CONTEXT_ID = 0X1C00001C
NCA_S_UNSUPPORTED_AUTHN_LEVEL = 0X1C00001D
NCA_S_INVALID_CHECKSUM = 0X1C00001F
NCA_S_INVALID_CRC = 0X1C000020
NCA_S_FAULT_USER_DEFINED = 0X1C000021
NCA_S_FAULT_TX_OPEN_FAILED = 0X1C000022
NCA_S_FAULT_CODESET_CONV_ERROR = 0X1C000023
NCA_S_FAULT_OBJECT_NOT_FOUND = 0X1C000024
NCA_S_FAULT_NO_CLIENT_STUB = 0X1C000025
RPC_S_MOD = 0X16C9A000
RPC_S_OP_RNG_ERROR = 0X16C9A001
RPC_S_CANT_CREATE_SOCKET = 0X16C9A002
RPC_S_CANT_BIND_SOCKET = 0X16C9A003
RPC_S_NOT_IN_CALL = 0X16C9A004
RPC_S_NO_PORT = 0X16C9A005
RPC_S_WRONG_BOOT_TIME = 0X16C9A006
RPC_S_TOO_MANY_SOCKETS = 0X16C9A007
RPC_S_ILLEGAL_REGISTER = 0X16C9A008
RPC_S_CANT_RECV = 0X16C9A009
RPC_S_BAD_PKT = 0X16C9A00A
RPC_S_UNBOUND_HANDLE = 0X16C9A00B
RPC_S_ADDR_IN_USE = 0X16C9A00C
RPC_S_IN_ARGS_TOO_BIG = 0X16C9A00D
RPC_S_STRING_TOO_LONG = 0X16C9A00E
RPC_S_TOO_MANY_OBJECTS = 0X16C9A00F
RPC_S_BINDING_HAS_NO_AUTH = 0X16C9A010
RPC_S_UNKNOWN_AUTHN_SERVICE = 0X16C9A011
RPC_S_NO_MEMORY = 0X16C9A012
RPC_S_CANT_NMALLOC = 0X16C9A013
RPC_S_CALL_FAULTED = 0X16C9A014
RPC_S_CALL_FAILED = 0X16C9A015
RPC_S_COMM_FAILURE = 0X16C9A016
RPC_S_RPCD_COMM_FAILURE = 0X16C9A017
RPC_S_ILLEGAL_FAMILY_REBIND = 0X16C9A018
RPC_S_INVALID_HANDLE = 0X16C9A019
RPC_S_CODING_ERROR = 0X16C9A01A
RPC_S_OBJECT_NOT_FOUND = 0X16C9A01B
RPC_S_CTHREAD_NOT_FOUND = 0X16C9A01C
RPC_S_INVALID_BINDING = 0X16C9A01D
RPC_S_ALREADY_REGISTERED = 0X16C9A01E
RPC_S_ENDPOINT_NOT_FOUND = 0X16C9A01F
RPC_S_INVALID_RPC_PROTSEQ = 0X16C9A020
RPC_S_DESC_NOT_REGISTERED = 0X16C9A021
RPC_S_ALREADY_LISTENING = 0X16C9A022
RPC_S_NO_PROTSEQS = 0X16C9A023
RPC_S_NO_PROTSEQS_REGISTERED = 0X16C9A024
RPC_S_NO_BINDINGS = 0X16C9A025
RPC_S_MAX_DESCS_EXCEEDED = 0X16C9A026
RPC_S_NO_INTERFACES = 0X16C9A027
RPC_S_INVALID_TIMEOUT = 0X16C9A028
RPC_S_CANT_INQ_SOCKET = 0X16C9A029
RPC_S_INVALID_NAF_ID = 0X16C9A02A
RPC_S_INVAL_NET_ADDR = 0X16C9A02B
RPC_S_UNKNOWN_IF = 0X16C9A02C
RPC_S_UNSUPPORTED_TYPE = 0X16C9A02D
RPC_S_INVALID_CALL_OPT = 0X16C9A02E
RPC_S_NO_FAULT = 0X16C9A02F
RPC_S_CANCEL_TIMEOUT = 0X16C9A030
RPC_S_CALL_CANCELLED = 0X16C9A031
RPC_S_INVALID_CALL_HANDLE = 0X16C9A032
RPC_S_CANNOT_ALLOC_ASSOC = 0X16C9A033
RPC_S_CANNOT_CONNECT = 0X16C9A034
RPC_S_CONNECTION_ABORTED = 0X16C9A035
RPC_S_CONNECTION_CLOSED = 0X16C9A036
RPC_S_CANNOT_ACCEPT = 0X16C9A037
RPC_S_ASSOC_GRP_NOT_FOUND = 0X16C9A038
RPC_S_STUB_INTERFACE_ERROR = 0X16C9A039
RPC_S_INVALID_OBJECT = 0X16C9A03A
RPC_S_INVALID_TYPE = 0X16C9A03B
RPC_S_INVALID_IF_OPNUM = 0X16C9A03C
RPC_S_DIFFERENT_SERVER_INSTANCE = 0X16C9A03D
RPC_S_PROTOCOL_ERROR = 0X16C9A03E
RPC_S_CANT_RECVMSG = 0X16C9A03F
RPC_S_INVALID_STRING_BINDING = 0X16C9A040
RPC_S_CONNECT_TIMED_OUT = 0X16C9A041
RPC_S_CONNECT_REJECTED = 0X16C9A042
RPC_S_NETWORK_UNREACHABLE = 0X16C9A043
RPC_S_CONNECT_NO_RESOURCES = 0X16C9A044
RPC_S_REM_NETWORK_SHUTDOWN = 0X16C9A045
RPC_S_TOO_MANY_REM_CONNECTS = 0X16C9A046
RPC_S_NO_REM_ENDPOINT = 0X16C9A047
RPC_S_REM_HOST_DOWN = 0X16C9A048
RPC_S_HOST_UNREACHABLE = 0X16C9A049
RPC_S_ACCESS_CONTROL_INFO_INV = 0X16C9A04A
RPC_S_LOC_CONNECT_ABORTED = 0X16C9A04B
RPC_S_CONNECT_CLOSED_BY_REM = 0X16C9A04C
RPC_S_REM_HOST_CRASHED = 0X16C9A04D
RPC_S_INVALID_ENDPOINT_FORMAT = 0X16C9A04E
RPC_S_UNKNOWN_STATUS_CODE = 0X16C9A04F
RPC_S_UNKNOWN_MGR_TYPE = 0X16C9A050
RPC_S_ASSOC_CREATION_FAILED = 0X16C9A051
RPC_S_ASSOC_GRP_MAX_EXCEEDED = 0X16C9A052
RPC_S_ASSOC_GRP_ALLOC_FAILED = 0X16C9A053
RPC_S_SM_INVALID_STATE = 0X16C9A054
RPC_S_ASSOC_REQ_REJECTED = 0X16C9A055
RPC_S_ASSOC_SHUTDOWN = 0X16C9A056
RPC_S_TSYNTAXES_UNSUPPORTED = 0X16C9A057
RPC_S_CONTEXT_ID_NOT_FOUND = 0X16C9A058
RPC_S_CANT_LISTEN_SOCKET = 0X16C9A059
RPC_S_NO_ADDRS = 0X16C9A05A
RPC_S_CANT_GETPEERNAME = 0X16C9A05B
RPC_S_CANT_GET_IF_ID = 0X16C9A05C
RPC_S_PROTSEQ_NOT_SUPPORTED = 0X16C9A05D
RPC_S_CALL_ORPHANED = 0X16C9A05E
RPC_S_WHO_ARE_YOU_FAILED = 0X16C9A05F
RPC_S_UNKNOWN_REJECT = 0X16C9A060
RPC_S_TYPE_ALREADY_REGISTERED = 0X16C9A061
RPC_S_STOP_LISTENING_DISABLED = 0X16C9A062
RPC_S_INVALID_ARG = 0X16C9A063
RPC_S_NOT_SUPPORTED = 0X16C9A064
RPC_S_WRONG_KIND_OF_BINDING = 0X16C9A065
RPC_S_AUTHN_AUTHZ_MISMATCH = 0X16C9A066
RPC_S_CALL_QUEUED = 0X16C9A067
RPC_S_CANNOT_SET_NODELAY = 0X16C9A068
RPC_S_NOT_RPC_TOWER = 0X16C9A069
RPC_S_INVALID_RPC_PROTID = 0X16C9A06A
RPC_S_INVALID_RPC_FLOOR = 0X16C9A06B
RPC_S_CALL_TIMEOUT = 0X16C9A06C
RPC_S_MGMT_OP_DISALLOWED = 0X16C9A06D
RPC_S_MANAGER_NOT_ENTERED = 0X16C9A06E
RPC_S_CALLS_TOO_LARGE_FOR_WK_EP = 0X16C9A06F
RPC_S_SERVER_TOO_BUSY = 0X16C9A070
RPC_S_PROT_VERSION_MISMATCH = 0X16C9A071
RPC_S_RPC_PROT_VERSION_MISMATCH = 0X16C9A072
RPC_S_SS_NO_IMPORT_CURSOR = 0X16C9A073
RPC_S_FAULT_ADDR_ERROR = 0X16C9A074
RPC_S_FAULT_CONTEXT_MISMATCH = 0X16C9A075
RPC_S_FAULT_FP_DIV_BY_ZERO = 0X16C9A076
RPC_S_FAULT_FP_ERROR = 0X16C9A077
RPC_S_FAULT_FP_OVERFLOW = 0X16C9A078
RPC_S_FAULT_FP_UNDERFLOW = 0X16C9A079
RPC_S_FAULT_ILL_INST = 0X16C9A07A
RPC_S_FAULT_INT_DIV_BY_ZERO = 0X16C9A07B
RPC_S_FAULT_INT_OVERFLOW = 0X16C9A07C
RPC_S_FAULT_INVALID_BOUND = 0X16C9A07D
RPC_S_FAULT_INVALID_TAG = 0X16C9A07E
RPC_S_FAULT_PIPE_CLOSED = 0X16C9A07F
RPC_S_FAULT_PIPE_COMM_ERROR = 0X16C9A080
RPC_S_FAULT_PIPE_DISCIPLINE = 0X16C9A081
RPC_S_FAULT_PIPE_EMPTY = 0X16C9A082
RPC_S_FAULT_PIPE_MEMORY = 0X16C9A083
RPC_S_FAULT_PIPE_ORDER = 0X16C9A084
RPC_S_FAULT_REMOTE_COMM_FAILURE = 0X16C9A085
RPC_S_FAULT_REMOTE_NO_MEMORY = 0X16C9A086
RPC_S_FAULT_UNSPEC = 0X16C9A087
UUID_S_BAD_VERSION = 0X16C9A088
UUID_S_SOCKET_FAILURE = 0X16C9A089
UUID_S_GETCONF_FAILURE = 0X16C9A08A
UUID_S_NO_ADDRESS = 0X16C9A08B
UUID_S_OVERRUN = 0X16C9A08C
UUID_S_INTERNAL_ERROR = 0X16C9A08D
UUID_S_CODING_ERROR = 0X16C9A08E
UUID_S_INVALID_STRING_UUID = 0X16C9A08F
UUID_S_NO_MEMORY = 0X16C9A090
RPC_S_NO_MORE_ENTRIES = 0X16C9A091
RPC_S_UNKNOWN_NS_ERROR = 0X16C9A092
RPC_S_NAME_SERVICE_UNAVAILABLE = 0X16C9A093
RPC_S_INCOMPLETE_NAME = 0X16C9A094
RPC_S_GROUP_NOT_FOUND = 0X16C9A095
RPC_S_INVALID_NAME_SYNTAX = 0X16C9A096
RPC_S_NO_MORE_MEMBERS = 0X16C9A097
RPC_S_NO_MORE_INTERFACES = 0X16C9A098
RPC_S_INVALID_NAME_SERVICE = 0X16C9A099
RPC_S_NO_NAME_MAPPING = 0X16C9A09A
RPC_S_PROFILE_NOT_FOUND = 0X16C9A09B
RPC_S_NOT_FOUND = 0X16C9A09C
RPC_S_NO_UPDATES = 0X16C9A09D
RPC_S_UPDATE_FAILED = 0X16C9A09E
RPC_S_NO_MATCH_EXPORTED = 0X16C9A09F
RPC_S_ENTRY_NOT_FOUND = 0X16C9A0A0
RPC_S_INVALID_INQUIRY_CONTEXT = 0X16C9A0A1
RPC_S_INTERFACE_NOT_FOUND = 0X16C9A0A2
RPC_S_GROUP_MEMBER_NOT_FOUND = 0X16C9A0A3
RPC_S_ENTRY_ALREADY_EXISTS = 0X16C9A0A4
RPC_S_NSINIT_FAILURE = 0X16C9A0A5
RPC_S_UNSUPPORTED_NAME_SYNTAX = 0X16C9A0A6
RPC_S_NO_MORE_ELEMENTS = 0X16C9A0A7
RPC_S_NO_NS_PERMISSION = 0X16C9A0A8
RPC_S_INVALID_INQUIRY_TYPE = 0X16C9A0A9
RPC_S_PROFILE_ELEMENT_NOT_FOUND = 0X16C9A0AA
RPC_S_PROFILE_ELEMENT_REPLACED = 0X16C9A0AB
RPC_S_IMPORT_ALREADY_DONE = 0X16C9A0AC
RPC_S_DATABASE_BUSY = 0X16C9A0AD
RPC_S_INVALID_IMPORT_CONTEXT = 0X16C9A0AE
RPC_S_UUID_SET_NOT_FOUND = 0X16C9A0AF
RPC_S_UUID_MEMBER_NOT_FOUND = 0X16C9A0B0
RPC_S_NO_INTERFACES_EXPORTED = 0X16C9A0B1
RPC_S_TOWER_SET_NOT_FOUND = 0X16C9A0B2
RPC_S_TOWER_MEMBER_NOT_FOUND = 0X16C9A0B3
RPC_S_OBJ_UUID_NOT_FOUND = 0X16C9A0B4
RPC_S_NO_MORE_BINDINGS = 0X16C9A0B5
RPC_S_INVALID_PRIORITY = 0X16C9A0B6
RPC_S_NOT_RPC_ENTRY = 0X16C9A0B7
RPC_S_INVALID_LOOKUP_CONTEXT = 0X16C9A0B8
RPC_S_BINDING_VECTOR_FULL = 0X16C9A0B9
RPC_S_CYCLE_DETECTED = 0X16C9A0BA
RPC_S_NOTHING_TO_EXPORT = 0X16C9A0BB
RPC_S_NOTHING_TO_UNEXPORT = 0X16C9A0BC
RPC_S_INVALID_VERS_OPTION = 0X16C9A0BD
RPC_S_NO_RPC_DATA = 0X16C9A0BE
RPC_S_MBR_PICKED = 0X16C9A0BF
RPC_S_NOT_ALL_OBJS_UNEXPORTED = 0X16C9A0C0
RPC_S_NO_ENTRY_NAME = 0X16C9A0C1
RPC_S_PRIORITY_GROUP_DONE = 0X16C9A0C2
RPC_S_PARTIAL_RESULTS = 0X16C9A0C3
RPC_S_NO_ENV_SETUP = 0X16C9A0C4
TWR_S_UNKNOWN_SA = 0X16C9A0C5
TWR_S_UNKNOWN_TOWER = 0X16C9A0C6
TWR_S_NOT_IMPLEMENTED = 0X16C9A0C7
RPC_S_MAX_CALLS_TOO_SMALL = 0X16C9A0C8
RPC_S_CTHREAD_CREATE_FAILED = 0X16C9A0C9
RPC_S_CTHREAD_POOL_EXISTS = 0X16C9A0CA
RPC_S_CTHREAD_NO_SUCH_POOL = 0X16C9A0CB
RPC_S_CTHREAD_INVOKE_DISABLED = 0X16C9A0CC
EPT_S_CANT_PERFORM_OP = 0X16C9A0CD
EPT_S_NO_MEMORY = 0X16C9A0CE
EPT_S_DATABASE_INVALID = 0X16C9A0CF
EPT_S_CANT_CREATE = 0X16C9A0D0
EPT_S_CANT_ACCESS = 0X16C9A0D1
EPT_S_DATABASE_ALREADY_OPEN = 0X16C9A0D2
EPT_S_INVALID_ENTRY = 0X16C9A0D3
EPT_S_UPDATE_FAILED = 0X16C9A0D4
EPT_S_INVALID_CONTEXT = 0X16C9A0D5
EPT_S_NOT_REGISTERED = 0X16C9A0D6
EPT_S_SERVER_UNAVAILABLE = 0X16C9A0D7
RPC_S_UNDERSPECIFIED_NAME = 0X16C9A0D8
RPC_S_INVALID_NS_HANDLE = 0X16C9A0D9
RPC_S_UNKNOWN_ERROR = 0X16C9A0DA
RPC_S_SS_CHAR_TRANS_OPEN_FAIL = 0X16C9A0DB
RPC_S_SS_CHAR_TRANS_SHORT_FILE = 0X16C9A0DC
RPC_S_SS_CONTEXT_DAMAGED = 0X16C9A0DD
RPC_S_SS_IN_NULL_CONTEXT = 0X16C9A0DE
RPC_S_SOCKET_FAILURE = 0X16C9A0DF
RPC_S_UNSUPPORTED_PROTECT_LEVEL = 0X16C9A0E0
RPC_S_INVALID_CHECKSUM = 0X16C9A0E1
RPC_S_INVALID_CREDENTIALS = 0X16C9A0E2
RPC_S_CREDENTIALS_TOO_LARGE = 0X16C9A0E3
RPC_S_CALL_ID_NOT_FOUND = 0X16C9A0E4
RPC_S_KEY_ID_NOT_FOUND = 0X16C9A0E5
RPC_S_AUTH_BAD_INTEGRITY = 0X16C9A0E6
RPC_S_AUTH_TKT_EXPIRED = 0X16C9A0E7
RPC_S_AUTH_TKT_NYV = 0X16C9A0E8
RPC_S_AUTH_REPEAT = 0X16C9A0E9
RPC_S_AUTH_NOT_US = 0X16C9A0EA
RPC_S_AUTH_BADMATCH = 0X16C9A0EB
RPC_S_AUTH_SKEW = 0X16C9A0EC
RPC_S_AUTH_BADADDR = 0X16C9A0ED
RPC_S_AUTH_BADVERSION = 0X16C9A0EE
RPC_S_AUTH_MSG_TYPE = 0X16C9A0EF
RPC_S_AUTH_MODIFIED = 0X16C9A0F0
RPC_S_AUTH_BADORDER = 0X16C9A0F1
RPC_S_AUTH_BADKEYVER = 0X16C9A0F2
RPC_S_AUTH_NOKEY = 0X16C9A0F3
RPC_S_AUTH_MUT_FAIL = 0X16C9A0F4
RPC_S_AUTH_BADDIRECTION = 0X16C9A0F5
RPC_S_AUTH_METHOD = 0X16C9A0F6
RPC_S_AUTH_BADSEQ = 0X16C9A0F7
RPC_S_AUTH_INAPP_CKSUM = 0X16C9A0F8
RPC_S_AUTH_FIELD_TOOLONG = 0X16C9A0F9
RPC_S_INVALID_CRC = 0X16C9A0FA
RPC_S_BINDING_INCOMPLETE = 0X16C9A0FB
RPC_S_KEY_FUNC_NOT_ALLOWED = 0X16C9A0FC
RPC_S_UNKNOWN_STUB_RTL_IF_VERS = 0X16C9A0FD
RPC_S_UNKNOWN_IFSPEC_VERS = 0X16C9A0FE
RPC_S_PROTO_UNSUPP_BY_AUTH = 0X16C9A0FF
RPC_S_AUTHN_CHALLENGE_MALFORMED = 0X16C9A100
RPC_S_PROTECT_LEVEL_MISMATCH = 0X16C9A101
RPC_S_NO_MEPV = 0X16C9A102
RPC_S_STUB_PROTOCOL_ERROR = 0X16C9A103
RPC_S_CLASS_VERSION_MISMATCH = 0X16C9A104
RPC_S_HELPER_NOT_RUNNING = 0X16C9A105
RPC_S_HELPER_SHORT_READ = 0X16C9A106
RPC_S_HELPER_CATATONIC = 0X16C9A107
RPC_S_HELPER_ABORTED = 0X16C9A108
RPC_S_NOT_IN_KERNEL = 0X16C9A109
RPC_S_HELPER_WRONG_USER = 0X16C9A10A
RPC_S_HELPER_OVERFLOW = 0X16C9A10B
RPC_S_DG_NEED_WAY_AUTH = 0X16C9A10C
RPC_S_UNSUPPORTED_AUTH_SUBTYPE = 0X16C9A10D
RPC_S_WRONG_PICKLE_TYPE = 0X16C9A10E
RPC_S_NOT_LISTENING = 0X16C9A10F
RPC_S_SS_BAD_BUFFER = 0X16C9A110
RPC_S_SS_BAD_ES_ACTION = 0X16C9A111
RPC_S_SS_WRONG_ES_VERSION = 0X16C9A112
RPC_S_FAULT_USER_DEFINED = 0X16C9A113
RPC_S_SS_INCOMPATIBLE_CODESETS = 0X16C9A114
RPC_S_TX_NOT_IN_TRANSACTION = 0X16C9A115
RPC_S_TX_OPEN_FAILED = 0X16C9A116
RPC_S_PARTIAL_CREDENTIALS = 0X16C9A117
RPC_S_SS_INVALID_CODESET_TAG = 0X16C9A118
RPC_S_MGMT_BAD_TYPE = 0X16C9A119
RPC_S_SS_INVALID_CHAR_INPUT = 0X16C9A11A
RPC_S_SS_SHORT_CONV_BUFFER = 0X16C9A11B
RPC_S_SS_ICONV_ERROR = 0X16C9A11C
RPC_S_SS_NO_COMPAT_CODESET = 0X16C9A11D
RPC_S_SS_NO_COMPAT_CHARSETS = 0X16C9A11E
DCE_CS_C_OK = 0X16C9A11F
DCE_CS_C_UNKNOWN = 0X16C9A120
DCE_CS_C_NOTFOUND = 0X16C9A121
DCE_CS_C_CANNOT_OPEN_FILE = 0X16C9A122
DCE_CS_C_CANNOT_READ_FILE = 0X16C9A123
DCE_CS_C_CANNOT_ALLOCATE_MEMORY = 0X16C9A124
RPC_S_SS_CLEANUP_FAILED = 0X16C9A125
RPC_SVC_DESC_GENERAL = 0X16C9A126
RPC_SVC_DESC_MUTEX = 0X16C9A127
RPC_SVC_DESC_XMIT = 0X16C9A128
RPC_SVC_DESC_RECV = 0X16C9A129
RPC_SVC_DESC_DG_STATE = 0X16C9A12A
RPC_SVC_DESC_CANCEL = 0X16C9A12B
RPC_SVC_DESC_ORPHAN = 0X16C9A12C
RPC_SVC_DESC_CN_STATE = 0X16C9A12D
RPC_SVC_DESC_CN_PKT = 0X16C9A12E
RPC_SVC_DESC_PKT_QUOTAS = 0X16C9A12F
RPC_SVC_DESC_AUTH = 0X16C9A130
RPC_SVC_DESC_SOURCE = 0X16C9A131
RPC_SVC_DESC_STATS = 0X16C9A132
RPC_SVC_DESC_MEM = 0X16C9A133
RPC_SVC_DESC_MEM_TYPE = 0X16C9A134
RPC_SVC_DESC_DG_PKTLOG = 0X16C9A135
RPC_SVC_DESC_THREAD_ID = 0X16C9A136
RPC_SVC_DESC_TIMESTAMP = 0X16C9A137
RPC_SVC_DESC_CN_ERRORS = 0X16C9A138
RPC_SVC_DESC_CONV_THREAD = 0X16C9A139
RPC_SVC_DESC_PID = 0X16C9A13A
RPC_SVC_DESC_ATFORK = 0X16C9A13B
RPC_SVC_DESC_CMA_THREAD = 0X16C9A13C
RPC_SVC_DESC_INHERIT = 0X16C9A13D
RPC_SVC_DESC_DG_SOCKETS = 0X16C9A13E
RPC_SVC_DESC_TIMER = 0X16C9A13F
RPC_SVC_DESC_THREADS = 0X16C9A140
RPC_SVC_DESC_SERVER_CALL = 0X16C9A141
RPC_SVC_DESC_NSI = 0X16C9A142
RPC_SVC_DESC_DG_PKT = 0X16C9A143
RPC_M_CN_ILL_STATE_TRANS_SA = 0X16C9A144
RPC_M_CN_ILL_STATE_TRANS_CA = 0X16C9A145
RPC_M_CN_ILL_STATE_TRANS_SG = 0X16C9A146
RPC_M_CN_ILL_STATE_TRANS_CG = 0X16C9A147
RPC_M_CN_ILL_STATE_TRANS_SR = 0X16C9A148
RPC_M_CN_ILL_STATE_TRANS_CR = 0X16C9A149
RPC_M_BAD_PKT_TYPE = 0X16C9A14A
RPC_M_PROT_MISMATCH = 0X16C9A14B
RPC_M_FRAG_TOOBIG = 0X16C9A14C
RPC_M_UNSUPP_STUB_RTL_IF = 0X16C9A14D
RPC_M_UNHANDLED_CALLSTATE = 0X16C9A14E
RPC_M_CALL_FAILED = 0X16C9A14F
RPC_M_CALL_FAILED_NO_STATUS = 0X16C9A150
RPC_M_CALL_FAILED_ERRNO = 0X16C9A151
RPC_M_CALL_FAILED_S = 0X16C9A152
RPC_M_CALL_FAILED_C = 0X16C9A153
RPC_M_ERRMSG_TOOBIG = 0X16C9A154
RPC_M_INVALID_SRCHATTR = 0X16C9A155
RPC_M_NTS_NOT_FOUND = 0X16C9A156
RPC_M_INVALID_ACCBYTCNT = 0X16C9A157
RPC_M_PRE_V2_IFSPEC = 0X16C9A158
RPC_M_UNK_IFSPEC = 0X16C9A159
RPC_M_RECVBUF_TOOSMALL = 0X16C9A15A
RPC_M_UNALIGN_AUTHTRL = 0X16C9A15B
RPC_M_UNEXPECTED_EXC = 0X16C9A15C
RPC_M_NO_STUB_DATA = 0X16C9A15D
RPC_M_EVENTLIST_FULL = 0X16C9A15E
RPC_M_UNK_SOCK_TYPE = 0X16C9A15F
RPC_M_UNIMP_CALL = 0X16C9A160
RPC_M_INVALID_SEQNUM = 0X16C9A161
RPC_M_CANT_CREATE_UUID = 0X16C9A162
RPC_M_PRE_V2_SS = 0X16C9A163
RPC_M_DGPKT_POOL_CORRUPT = 0X16C9A164
RPC_M_DGPKT_BAD_FREE = 0X16C9A165
RPC_M_LOOKASIDE_CORRUPT = 0X16C9A166
RPC_M_ALLOC_FAIL = 0X16C9A167
RPC_M_REALLOC_FAIL = 0X16C9A168
RPC_M_CANT_OPEN_FILE = 0X16C9A169
RPC_M_CANT_READ_ADDR = 0X16C9A16A
RPC_SVC_DESC_LIBIDL = 0X16C9A16B
RPC_M_CTXRUNDOWN_NOMEM = 0X16C9A16C
RPC_M_CTXRUNDOWN_EXC = 0X16C9A16D
RPC_S_FAULT_CODESET_CONV_ERROR = 0X16C9A16E
RPC_S_NO_CALL_ACTIVE = 0X16C9A16F
RPC_S_CANNOT_SUPPORT = 0X16C9A170
RPC_S_NO_CONTEXT_AVAILABLE = 0X16C9A171
