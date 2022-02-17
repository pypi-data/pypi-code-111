#! /usr/bin/env python
########################################################################
# SimpleFIX
# Copyright (C) 2017-2022, David Arnold.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
########################################################################

"""FIX protocol constants."""

import sys


if sys.version_info[0] == 2:
    EQUALS_BYTE = b'='
    SOH_BYTE = b'\x01'
    SOH_STR = SOH_BYTE
else:
    EQUALS_BYTE = 61
    SOH_BYTE = 1
    SOH_STR = b'\x01'

# Tag 1
TAG_ACCOUNT = b'1'

# Tag 2
TAG_ADVID = b'2'

# Tag 3
TAG_ADVREFID = b'3'

# Tag 4
TAG_ADVSIDE = b'4'
ADVSIDE_BUY = b'B'
ADVSIDE_CROSS = b'X'
ADVSIDE_SELL = b'S'
ADVSIDE_TRADE = b'T'

# Tag 5
TAG_ADVTRANSTYPE = b'5'
ADVTRANSTYPE_CANCEL = b'C'
ADVTRANSTYPE_NEW = b'N'
ADVTRANSTYPE_REPLACE = b'R'

# Tag 6
TAG_AVGPX = b'6'

# Tag 7
TAG_BEGINSEQNO = b'7'

# Tag 8
TAG_BEGINSTRING = b'8'

# Tag 9
TAG_BODYLENGTH = b'9'

# Tag 10
TAG_CHECKSUM = b'10'

# Tag 11
TAG_CLORDID = b'11'

# Tag 12
TAG_COMMISSION = b'12'

# Tag 13
TAG_COMMTYPE = b'13'
COMMTYPE_PER_UNIT = b'1'
COMMTYPE_PERCENT = b'2'
COMMTYPE_ABSOLUTE = b'3'
COMMTYPE_PERCENT_WAIVED_CASH = b'4'
COMMTYPE_PERCENT_WAIVED_ENHANCED = b'5'
COMMTYPE_POINTS = b'6'

# Tag 14
TAG_CUMQTY = b'14'

# Tag 15
TAG_CURRENCY = b'15'
CURRENCY_AFGHANI = b'AFA'
CURRENCY_ALGERIAN_DINAR = b'DZD'
CURRENCY_ANDORRAN_PESETA = b'ADP'
CURRENCY_ARGENTINE_PESO = b'ARS'
CURRENCY_ARMENIAN_DRAM = b'AMD'
CURRENCY_ARUBAN_GUILDER = b'AWG'
CURRENCY_AUSTRALIAN_DOLLAR = b'AUD'
CURRENCY_AZERBAIJANIAN_MANAT = b'AZM'
CURRENCY_BAHAMIAN_DOLLAR = b'BSD'
# FIXME: many, many, more.

# Tag 16
TAG_ENDSEQNO = b'16'

# Tag 17
TAG_EXECID = b'17'

# Tag 18
TAG_EXECINST = b'18'
EXECINST_NOT_HELD = b'1'
EXECINST_WORK = b'2'
EXECINST_GO_ALONG = b'3'
EXECINST_OVER_THE_DAY = b'4'
EXECINST_HELD = b'5'
EXECINST_PARTICIPATE_DONT_INITIATE = b'6'
EXECINST_STRICT_SCALE = b'7'
EXECINST_TRY_TO_SCALE = b'8'
EXECINST_STAY_ON_BID_SIDE = b'9'
EXECINST_STAY_ON_OFFER_SIDE = b'0'
EXECINST_NO_CROSS = b'A'
EXECINST_OK_TO_CROSS = b'B'
EXECINST_CALL_FIRST = b'C'
EXECINST_PERCENT_OF_VOLUME = b'D'
EXECINST_DO_NOT_INCREASE = b'E'
EXECINST_DO_NOT_REDUCE = b'F'
EXECINST_ALL_OR_NONE = b'G'
EXECINST_REINSTATE_ON_SYSTEM_FAILURE = b'H'
EXECINST_INSTITUTIONS_ONLY = b'I'
EXECINST_REINSTATE_ON_TRADING_HALT = b'J'
EXECINST_CANCEL_ON_TRADING_HALT = b'K'
EXECINST_LAST_PEG = b'L'
EXECINST_MID_PRICE_PEG = b'M'
EXECINST_NON_NEGOTIABLE = b'N'
EXECINST_OPENING_PEG = b'O'
EXECINST_MARKET_PEG = b'P'
EXECINST_CANCEL_ON_SYSTEM_FAILURE = b'Q'
EXECINST_PRIMARY_PEG = b'R'
EXECINST_SUSPEND = b'S'
EXECINST_CUSTOMER_DISPLAY_INSTRUCTION = b'U'
EXECINST_NETTING = b'V'
EXECINST_PEG_TO_VWAP = b'W'
EXECINST_TRADE_ALONG = b'X'
EXECINST_TRY_TO_STOP = b'Y'
EXECINST_CANCEL_IF_NOT_BEST = b'Z'
EXECINST_TRAILING_STOP_PEG = b'a'
EXECINST_STRICT_LIMIT = b'b'
EXECINST_IGNORE_PRICE_VALIDITY_CHECKS = b'c'
EXECINST_PEG_TO_LIMIT_PRICE = b'd'
EXECINST_WORK_TO_TARGET_STRATEGY = b'e'

# Tag 19
TAG_EXECREFID = b'19'

# Tag 20
TAG_EXECTRANSTYPE = b'20'
EXECTRANSTYPE_NEW = b'0'
EXECTRANSTYPE_CANCEL = b'1'
EXECTRANSTYPE_CORRECT = b'2'
EXECTRANSTYPE_STATUS = b'3'

# Tag 21
TAG_HANDLINST = b'21'
HANDLINST_AUTO_PRIVATE = b'1'
HANDLINST_AUTO_PUBLIC = b'2'
HANDLINST_MANUAL = b'3'

# Tag 22
TAG_SECURITYIDSOURCE = b'22'
SECURITYIDSOURCE_CUSIP = b'1'
SECURITYIDSOURCE_SEDOL = b'2'
SECURITYIDSOURCE_QUIK = b'3'
SECURITYIDSOURCE_ISIN = b'4'
SECURITYIDSOURCE_RIC = b'5'
SECURITYIDSOURCE_ISO_CURRENCY = b'6'
SECURITYIDSOURCE_ISO_COUNTRY = b'7'
SECURITYIDSOURCE_EXCHANGE = b'8'
SECURITYIDSOURCE_CTA = b'9'
SECURITYIDSOURCE_BLOOMBERG = b'A'
SECURITYIDSOURCE_WERTPAPIER = b'B'
SECURITYIDSOURCE_BUTCH = b'C'
SECURITYIDSOURCE_VALOREN = b'D'
SECURITYIDSOURCE_SICOVAM = b'E'
SECURITYIDSOURCE_BELGIAN = b'F'
SECURITYIDSOURCE_COMMON = b'G'
SECURITYIDSOURCE_CLEARING = b'H'
SECURITYIDSOURCE_IDSA = b'I'
SECURITYIDSOURCE_OPRA = b'J'
SECURITYIDSOURCE_IDSA_URL = b'K'
SECURITYIDSOURCE_LETTER_OF_CREDIT = b'L'
SECURITYIDSOURCE_MARKETPLACE = b'M'
SECURITYIDSOURCE_MARKIT_RED_ENTITY_CLIP = b'N'
SECURITYIDSOURCE_MARKIT_RED_PAIR_CLIP = b'P'
SECURITYIDSOURCE_CFTC = b'Q'
SECURITYIDSOURCE_IDSA_COMMODITY_REFERENCE_PRICE = b'R'
SECURITYIDSOURCE_FINANCIAL_INSTRUMENT_GLOBAL_IDENTIFIER = b'S'
SECURITYIDSOURCE_LEGAL_ENTITY_IDENTIFIER = b'T'
SECURITYIDSOURCE_SYNTHETIC = b'U'
SECURITYIDSOURCE_FIM = b'V'
SECURITYIDSOURCE_INDEX_NAME = b'W'

# Tag 23
TAG_IOIID = b'23'

# Tag 24
TAG_IOIOTHSVC = b'24'
IOIOTHSVC_AUTEX = b'A'
IOIOTHSVC_BRIDGE = b'B'
IOIOTHSVC_AUTEX_AND_BRIDGE = b'AB'
IOIOTHSVC_BRIDGE_AND_AUTEX = b'BA'

# Tag 25
TAG_IOIQLTYIND = b'25'
# this is to avoid breaking code using the old typo
TAG_IOIQlTYIND = TAG_IOIQLTYIND
IOIQLTYIND_HIGH = b'H'
IOIQLTYIND_MEDIUM = b'M'
IOIQLTYIND_LOW = b'L'

# Tag 26
TAG_IOIREFID = b'26'

# Tag 27
TAG_IOIQTY = b'27'
IOIQTY_SMALL = b'S'
IOIQTY_MEDIUM = b'M'
IOIQTY_LARGE = b'L'
IOIQTY_UNDISCLOSED = b'U'

# Tag 28
TAG_IOITRANSTYPE = b'28'
IOITRANSTYPE_NEW = b'N'
IOITRANSTYPE_CANCEL = b'C'
IOITRANSTYPE_REPLACE = b'R'

# Tag 29
TAG_LASTCAPACITY = b'29'
LASTCAPACITY_AGENT = b'1'
LASTCAPACITY_CROSS_AS_AGENT = b'2'
LASTCAPACITY_CROSS_AS_PRINCIPAL = b'3'
LASTCAPACITY_PRINCIPAL = b'4'
LASTCAPACITY_RISKLESS_PRINCIPAL = b'5'

# Tag 30
TAG_LASTMKT = b'30'
LASTMKT_BLOOMBERG_TRADEBOOK = b'31'
LASTMKT_BONDBOOK = b'32'
LASTMKT_BONDCLICK = b'35'
LASTMKT_BONDHUB = b'36'
LASTMKT_LIMITRADER = b'37'
LASTMKT_MARKETAXESS = b'33'
LASTMKT_MUNICENTER = b'34'
LASTMKT_NONE = b'0'
LASTMKT_OTC = b'11'
LASTMKT_NYFIX_MILLENIUM = b'13'
LASTMKT_NYSE_BBSS = b'10'
LASTMKT_POSIT = b'4'
LASTMKT_STOCKHOLM_OPTIONS_MARKET = b'17'
LASTMKT_VANCOUVER_OPTIONS_EXCHANGE = b'9'
LASTMKT_VISIBLE_MARKETS = b'38'
LASTMKT_TRADEWEB = b'30'
LASTMKT_ARCHIPELAGO = b'39'
LASTMKT_ATTAIN = b'40'
LASTMKT_BRUT = b'41'
LASTMKT_GLOBENET = b'42'
LASTMKT_INSTINET = b'43'
LASTMKT_ISLAND = b'44'
LASTMKT_MARKETXT = b'45'
LASTMKT_NEXTRADE = b'46'
LASTMKT_REDIBOOK = b'47'
LASTMKT_NQLX = b'49'
LASTMKT_ONECHICAGO = b'50'
LASTMKT_TRACK_DATA = b'51'
LASTMKT_TRACK_TRAC = b'52'
LASTMKT_PIPELINE = b'53'
LASTMKT_BATS = b'54'
LASTMKT_BIDS = b'55'
LASTMKT_DIRECT_EDGE_X = b'56'
LASTMKT_DIRECT_EDGE = b'57'
LASTMKT_LEVELATS = b'58'
LASTMKT_LAVA_TRADING = b'59'
LASTMKT_BOSTON_OPTIONS_EXCHANGE = b'60'
LASTMKT_NATIONAL_STOCK_EXCHANGE = b'61'
LASTMKT_LIQUIDNET = b'62'
LASTMKT_NYFIX_EURO_MILLENIUM = b'63'
LASTMKT_NASDAQ_OPTIONS_MARKET = b'64'
LASTMKT_BLOCKCROSS_ATS = b'66'
LASTMKT_MATCH_ATS = b'67'
LASTMKT_ATHENS_STOCK_EXCHANGE_REUTERS = b'AT'
LASTMKT_ATHENS_STOCK_EXCHANGE_MARKET = b'ASE'
LASTMKT_LATIBEX = b'LA'
LASTMKT_MADRID_STOCK_EXCHANGE = b'MC'
LASTMKT_OCCIDENTS_STOCK_EXCHANGE = b'OD'
LASTMKT_SBI_STOCK_EXCHANGE = b'SBI'
LASTMKT_DOHA_SECURITIES_MARKET = b'DSMD'
LASTMKT_INTERCONTINENTAL_EXCHANGE = b'IEPA'
LASTMKT_PINKSHEETS = b'PINX'
LASTMKT_THE_THIRD_MARKET_CORPORATION = b'THRD'
LASTMKT_TRADEWEB_LLC = b'TRWB'

# Tag 31
TAG_LASTPX = b'31'

# Tag 32
TAG_LASTQTY = b'32'

# Tag 33
TAG_NOLINESOFTEXT = b'33'

# Tag 34
TAG_MSGSEQNUM = b'34'

# Tag 35
TAG_MSGTYPE = b'35'
MSGTYPE_HEARTBEAT = b'0'
MSGTYPE_TEST_REQUEST = b'1'
MSGTYPE_RESEND_REQUEST = b'2'
MSGTYPE_REJECT = b'3'
MSGTYPE_SEQUENCE_RESET = b'4'
MSGTYPE_LOGOUT = b'5'
MSGTYPE_INDICATION_OF_INTEREST = b'6'
MSGTYPE_ADVERTISEMENT = b'7'
MSGTYPE_EXECUTION_REPORT = b'8'
MSGTYPE_ORDER_CANCEL_REJECT = b'9'
MSGTYPE_LOGON = b'A'
MSGTYPE_NEWS = b'B'
MSGTYPE_EMAIL = b'C'
MSGTYPE_NEW_ORDER_SINGLE = b'D'
MSGTYPE_NEW_ORDER_LIST = b'E'
MSGTYPE_ORDER_CANCEL_REQUEST = b'F'
MSGTYPE_ORDER_CANCEL_REPLACE_REQUEST = b'G'
MSGTYPE_ORDER_STATUS_REQUEST = b'H'
MSGTYPE_ALLOCATION = b'J'
MSGTYPE_LIST_CANCEL_REQUEST = b'K'
MSGTYPE_LIST_EXECUTE = b'L'
MSGTYPE_LIST_STATUS_REQUEST = b'M'
MSGTYPE_LIST_STATUS = b'N'
MSGTYPE_ALLOCATION_ACK = b'P'
MSGTYPE_DONT_KNOW_TRADE = b'Q'
MSGTYPE_QUOTE_REQUEST = b'R'
MSGTYPE_QUOTE = b'S'
MSGTYPE_SETTLEMENT_INSTRUCTIONS = b'T'
MSGTYPE_MARKET_DATA_REQUEST = b'V'
MSGTYPE_MARKET_DATA_SNAPSHOT_FULL_REFRESH = b'W'
MSGTYPE_MARKET_DATA_INCREMENTAL_REFRESH = b'X'
MSGTYPE_MARKET_DATA_REQUEST_REJECT = b'Y'
MSGTYPE_QUOTE_CANCEL = b'Z'
MSGTYPE_QUOTE_STATUS_REQUEST = b'a'
MSGTYPE_QUOTE_ACKNOWLEDGEMENT = b'b'
MSGTYPE_SECURITY_DEFINITION_REQUEST = b'c'
MSGTYPE_SECURITY_DEFINITION = b'd'
MSGTYPE_SECURITY_STATUS_REQUEST = b'e'
MSGTYPE_SECURITY_STATUS = b'f'
MSGTYPE_TRADING_SESSION_STATUS_REQUEST = b'g'
MSGTYPE_TRADING_SESSION_STATUS = b'h'
MSGTYPE_MASS_QUOTE = b'i'
MSGTYPE_BUSINESS_MESSAGE_REJECT = b'j'
MSGTYPE_BID_REQUEST = b'k'
MSGTYPE_BID_RESPONSE = b'l'
MSGTYPE_LIST_STRIKE_PRICE = b'm'
MSGTYPE_XML_MESSAGE = b'n'
MSGTYPE_REGISTRATION_INSTRUCTIONS = b'o'
MSGTYPE_REGISTRATION_INSTRUCTIONS_RESPONSE = b'p'
MSGTYPE_ORDER_MASS_CANCEL_REQUEST = b'q'
MSGTYPE_ORDER_MASS_CANCEL_REPORT = b'r'
MSGTYPE_NEW_ORDER_CROSS = b's'
MSGTYPE_CROSS_ORDER_CANCEL_REPLACE_REQUEST = b't'
MSGTYPE_CROSS_ORDER_CANCEL_REQUEST = b'u'
MSGTYPE_SECURITY_TYPE_REQUEST = b'v'
MSGTYPE_SECURITY_TYPES = b'w'
MSGTYPE_SECURITY_LIST_REQUEST = b'x'
MSGTYPE_SECURITY_LIST = b'y'
MSGTYPE_DERIVATIVE_SECURITY_LIST_REQUEST = b'z'
MSGTYPE_DERIVATIVE_SECURITY_LIST = b'AA'
MSGTYPE_NEW_ORDER_MULTILEG = b'AB'
MSGTYPE_MULTILEG_ORDER_CANCEL_REPLACE_REQUEST = b'AC'
MSGTYPE_TRADE_CAPTURE_REPORT_REQUEST = b'AD'
MSGTYPE_TRADE_CAPTURE_REPORT = b'AE'
MSGTYPE_ORDER_MASS_STATUS_REQUEST = b'AF'
MSGTYPE_QUOTE_REQUEST_REJECT = b'AG'
MSGTYPE_RFQ_REQUEST = b'AH'
MSGTYPE_QUOTE_STATUS_REPORT = b'AI'
MSGTYPE_QUOTE_RESPONSE = b'AJ'
MSGTYPE_CONFIRMATION = b'AK'
MSGTYPE_POSITION_MAINTENANCE_REQUEST = b'AL'
MSGTYPE_POSITION_MAINTENANCE_REPORT = b'AM'
MSGTYPE_REQUEST_FOR_POSITIONS = b'AN'
MSGTYPE_REQUEST_FOR_POSITIONS_ACK = b'AO'
MSGTYPE_POSITION_REPORT = b'AP'
MSGTYPE_TRADE_CAPTURE_REPORT_REQUEST_ACK = b'AQ'
MSGTYPE_TRADE_CAPTURE_REPORT_ACK = b'AR'
MSGTYPE_ALLOCATION_REPORT = b'AS'
MSGTYPE_ALLOCATION_REPORT_ACK = b'AT'
MSGTYPE_CONFIRMATION_ACK = b'AU'
MSGTYPE_SETTLEMENT_INSTRUCTION_REQUEST = b'AV'
MSGTYPE_ASSIGNMENT_REPORT = b'AW'
MSGTYPE_COLLATERAL_REQUEST = b'AX'
MSGTYPE_COLLATERAL_ASSIGNMENT = b'AY'
MSGTYPE_COLLATERAL_RESPONSE = b'AZ'
MSGTYPE_COLLATERAL_REPORT = b'BA'
MSGTYPE_COLLATERAL_INQUIRY = b'BB'
MSGTYPE_NETWORK_STATUS_REQUEST = b'BC'
MSGTYPE_NETWORK_STATUS_RESPONSE = b'BD'
MSGTYPE_USER_REQUEST = b'BE'
MSGTYPE_USER_RESPONSE = b'BF'
MSGTYPE_COLLATERAL_INQUIRY_ACK = b'BG'
MSGTYPE_CONFIRMATION_REQUEST = b'BH'

# Tag 36
TAG_NEWSEQNO = b'36'

# Tag 37
TAG_ORDERID = b'37'

# Tag 38
TAG_ORDERQTY = b'38'

# Tag 39
TAG_ORDSTATUS = b'39'
ORDSTATUS_NEW = b'0'
ORDSTATUS_PARTIALLY_FILLED = b'1'
ORDSTATUS_FILLED = b'2'
ORDSTATUS_DONE_FOR_DAY = b'3'
ORDSTATUS_CANCELED = b'4'
ORDSTATUS_REPLACED = b'5'
ORDSTATUS_PENDING_CANCEL = b'6'
ORDSTATUS_STOPPED = b'7'
ORDSTATUS_REJECTED = b'8'
ORDSTATUS_SUSPENDED = b'9'
ORDSTATUS_PENDING_NEW = b'A'
ORDSTATUS_CALCULATED = b'B'
ORDSTATUS_EXPIRED = b'C'
ORDSTATUS_ACCEPTED_FOR_BIDDING = b'D'
ORDSTATUS_PENDING_REPLACE = b'E'

# Tag 40
TAG_ORDTYPE = b'40'
ORDTYPE_MARKET = b'1'
ORDTYPE_LIMIT = b'2'
ORDTYPE_STOP = b'3'
ORDTYPE_STOP_LIMIT = b'4'
ORDTYPE_MARKET_ON_CLOSE = b'5'
ORDTYPE_WITH_OR_WITHOUT = b'6'
ORDTYPE_LIMIT_OR_BETTER = b'7'
ORDTYPE_LIMIT_WITH_OR_WITHOUT = b'8'
ORDTYPE_ON_BASIS = b'9'
ORDTYPE_ON_CLOSE = b'A'
ORDTYPE_LIMIT_ON_CLOSE = b'B'
ORDTYPE_FOREX_MARKET = b'C'
ORDTYPE_PREVIOUSLY_QUOTED = b'D'
ORDTYPE_PREVIOUSLY_INDICATED = b'E'
ORDTYPE_FOREX_LIMIT = b'F'
ORDTYPE_FOREX_SWAP = b'G'
ORDTYPE_FOREX_PREVIOUSLY_QUOTED = b'H'
ORDTYPE_FUNARI = b'I'
ORDTYPE_MARKET_IF_TOUCHED = b'J'
ORDTYPE_MARKET_WITH_LEFTOVER_AS_LIMIT = b'K'
ORDTYPE_PREVIOUS_FUND_VALUATION_POINT = b'L'
ORDTYPE_NEXT_FUND_VALUATION_POINT = b'M'
ORDTYPE_PEGGED = b'P'
ORDTYPE_COUNTER_ORDER_SELECTION = b'Q'
ORDTYPE_STOP_ON_BID_OR_OFFER = b'R'
ORDTYPE_STOP_LIMIT_ON_BID_OR_OFFER = b'S'

# Tag 41
TAG_ORIGCLORDID = b'41'

# Tag 42
TAG_ORIGTIME = b'42'

# Tag 43
TAG_POSSDUPFLAG = b'43'
POSSDUPFLAG_NO = b'N'
POSSDUPFLAG_YES = b'Y'

# Tag 44
TAG_PRICE = b'44'

# Tag 45
TAG_REFSEQNUM = b'45'

# Tag 46
TAG_RELATDSYM = b'46'

# Tag 47
TAG_RULE80A = b'47'
RULE80A_AGENCY_SINGLE_ORDER = b'A'
RULE80A_ALL_OTHER_ORDERS_AS_AGENT_FOR_OTHER_MEMBER = b'W'
RULE80A_COMPETING_DEALER_TRADES = b'T'
RULE80A_INDIVIDUAL_INVESTOR_SINGLE_ORDER = b'I'
RULE80A_PRINCIPAL = b'P'
RULE80A_PROGRAM_ORDER_INDEX_ARB_FOR_INDIVIDUAL_CUSTOMER = b'J'
RULE80A_PROGRAM_ORDER_INDEX_ARB_FOR_MEMBER_FIRM_ORG = b'D'
RULE80A_PROGRAM_ORDER_INDEX_ARB_FOR_OTHER_AGENCY = b'U'
RULE80A_PROGRAM_ORDER_INDEX_ARB_FOR_OTHER_MEMBER = b'M'
RULE80A_PROGRAM_ORDER_NON_INDEX_ARB_FOR_INDIVIDUAL_CUSTOMER = b'K'
RULE80A_PROGRAM_ORDER_NON_INDEX_ARB_FOR_MEMBER_FIRM_ORG = b'C'
RULE80A_PROGRAM_ORDER_NON_INDEX_ARB_FOR_OTHER_AGENCY = b'Y'
RULE80A_PROGRAM_ORDER_NON_INDEX_ARB_FOR_OTHER_MEMBER = b'N'
RULE80A_ROPRIETARY_TRANSACTIONS_FOR_COMPETING_MARKET_MAKER_THAT_IS_AFFILIATED_WITH_THE_CLEARING_MEMBER = b'O'
RULE80A_SHORT_EXEMPT_TRANSACTION_B = b'B'
RULE80A_SHORT_EXEMPT_TRANSACTION_F = b'F'
RULE80A_SHORT_EXEMPT_TRANSACTION_FOR_MEMBER_COMPETING_MARKET_MAKER_AFFILIATED_WITH_THE_FIRM_CLEARING_THE_TRADE = b'L'
RULE80A_SHORT_EXEMPT_TRANSACTION_FOR_MEMBER_COMPETING_MARKET_MAKER_NOT_AFFILIATED_WITH_THE_FIRM_CLEARING_THE_THREAD = b'X'
RULE80A_SHORT_EXEMPT_TRANSACTION_FOR_NON_MEMBER_COMPETING_MARKET_MAKER = b'Z'
RULE80A_SHORT_EXEMPT_TRANSACTION_FOR_PRINCIPAL = b'E'
RULE80A_SHORT_EXEMPT_TRANSACTION_H = b'H'
RULE80A_SPECIALIST_TRADES = b'S'
RULE80A_TRANSACTIONS_FOR_THE_ACCOUNT_OF_A_NON_MEMBER_COMPETING_MARKET_MAKER = b'R'

# Tag 48
TAG_SECURITY_ID = b'48'

# Tag 49
TAG_SENDER_COMPID = b'49'

# Tag 50
TAG_SENDER_SUBID = b'50'

# Tag 51
TAG_SENDING_DATE = b'51'

# Tag 52
TAG_SENDING_TIME = b'52'

# Tag 53
TAG_QUANTITY = b'53'

# Tag 54
TAG_SIDE = b'54'
SIDE_BUY = b'1'
SIDE_SELL = b'2'
SIDE_BUY_MINUS = b'3'
SIDE_SELL_PLUS = b'4'
SIDE_SELL_SHORT = b'5'
SIDE_SELL_SHORT_EXEMPT = b'6'
SIDE_UNDISCLOSED = b'7'
SIDE_CROSS = b'8'
SIDE_CROSS_SHORT = b'9'
SIDE_CROSS_SHORT_EXEMPT = b'A'
SIDE_AS_DEFINED = b'B'
SIDE_OPPOSITE = b'C'
SIDE_SUBSCRIBE = b'D'
SIDE_REDEEM = b'E'
SIDE_LEND = b'F'
SIDE_BORROW = b'G'
SIDE_SELL_UNDISCLOSED = b'H'

# Tag 55
TAG_SYMBOL = b'55'

# Tag 56
TAG_TARGET_COMPID = b'56'

# Tag 57
TAG_TARGET_SUBID = b'57'

# Tag 58
TAG_TEXT = b'58'

# Tag 59
TAG_TIMEINFORCE = b'59'
TIMEINFORCE_DAY = b'0'
TIMEINFORCE_GOOD_TILL_CANCEL = b'1'
TIMEINFORCE_AT_THE_OPENING = b'2'
TIMEINFORCE_IMMEDIATE_OR_CANCEL = b'3'
TIMEINFORCE_FILL_OR_KILL = b'4'
TIMEINFORCE_GOOD_TILL_CROSSING = b'5'
TIMEINFORCE_GOOD_TILL_DATE = b'6'
TIMEINFORCE_AT_THE_CLOSE = b'7'
TIMEINFORCE_GOOD_THROUGH_CROSSING = b'8'
TIMEINFORCE_AT_CROSSING = b'9'
TIMEINFORCE_GOOD_FOR_TIME = b'A'
TIMEINFORCE_GOOD_FOR_AUCTION = b'B'

# Tag 60
TAG_TRANSACTTIME = b'60'

# Tag 61
TAG_URGENCY = b'61'
URGENCY_NORMAL = b'0'
URGENCY_FLASH = b'1'
URGENCY_BACKGROUND = b'2'

# Tag 62
TAG_VALIDUNTILTIME = b'62'

# Tag 63
TAG_SETTLTYPE = b'63'
SETTLTYPE_REGULAR = b'0'
SETTLTYPE_CASH = b'1'
SETTLTYPE_NEXT_DAY = b'2'
SETTLTYPE_T2 = b'3'
SETTLTYPE_T3 = b'4'
SETTLTYPE_T4 = b'5'
SETTLTYPE_FUTURE = b'6'
SETTLTYPE_WHEN_AND_IF_ISSUED = b'7'
SETTLTYPE_SELLERS_OPTION = b'8'
SETTLTYPE_T5 = b'9'
SETTLTYPE_T1 = b'A'
SETTLTYPE_BROKEN_DATE = b'B'
SETTLTYPE_SPOT1 = b'C'

# Tag 64
TAG_SETTLDATE = b'64'

# Tag 65
TAG_SYMBOLSFX = b'65'

# Tag 66
TAG_LISTID = b'66'

# Tag 67
TAG_LISTSEQNO = b'67'

# Tag 68
TAG_TOTNOORDERS = b'68'

# Tag 69
TAG_LISTEXECINST = b'69'

# Tag 70
TAG_ALLOCID = b'70'

# Tag 71
TAG_ALLOCTRANSTYPE = b'71'
ALLOCTRANSTYPE_NEW = b'0'
ALLOCTRANSTYPE_REPLACE = b'1'
ALLOCTRANSTYPE_CANCEL = b'2'
ALLOCTRANSTYPE_PRELIMINARY = b'3'
ALLOCTRANSTYPE_CALCULATED = b'4'
ALLOCTRANSTYPE_CALCULATED_WITHOUT_PRELIMINARY = b'5'
ALLOCTRANSTYPE_REVERSAL = b'6'

# Tag 72
TAG_REFALLOCID = b'72'

# Tag 73
TAG_NOORDERS = b'73'

# Tag 74
TAG_AVGPRXPRECISION = b'74'

# Tag 75
TAG_TRADEDATE = b'75'

# Tag 76
TAG_EXECBROKER = b'76'

# Tag 77
TAG_OPENCLOSE = b'77'
OPENCLOSE_OPEN = b'O'
OPENCLOSE_CLOSER = b'C'

# Tag 78
TAG_NOALLOCS = b'78'

# Tag 79
TAG_ALLOCACCOUNT = b'79'

# Tag 80
TAG_ALLOCSHARES = b'80'

# Tag 81
TAG_PROCESSCODE = b'81'
PROCESSCODE_REGULAR = b'0'
PROCESSCODE_SOFT_DOLLAR = b'1'
PROCESSCODE_STEP_IN = b'2'
PROCESSCODE_STEP_OUT = b'3'
PROCESSCODE_SOFT_DOLLAR_STEP_IN = b'4'
PROCESSCODE_SOFT_DOLLAR_STEP_OUT = b'5'
PROCESSCODE_PLAN_SPONSOR = b'6'

# Tag 82
TAG_NORPTS = b'82'

# Tag 83
TAG_RPTSEQ = b'83'

# Tag 84
TAG_CXLQTY = b'84'

# Tag 85

# Tag 86

# Tag 87
TAG_ALLOCSTATUS = b'87'
ALLOCSTATUS_ACCEPTED = b'0'
ALLOCSTATUS_REJECTED = b'1'
ALLOCSTATUS_PARTIAL_ACCEPT = b'2'
ALLOCSTATUS_RECEIVED = b'3'

# Tag 88
TAG_ALLOCREJCODE = b'88'
ALLOCREJCODE_UNKNOWN_ACCOUNT = b'0'
ALLOCREJCODE_INCORRECT_QUANTITY = b'1'
ALLOCREJCODE_INCORRECT_AVERAGE_PRICE = b'2'
ALLOCREJCODE_UNKNOWN_EXECUTING_BROKER_MNEMONIC = b'3'
ALLOCREJCODE_COMMISSION_DIFFERENCE = b'4'
ALLOCREJCODE_UNKNOWN_ORDERID = b'5'
ALLOCREJCODE_UNKNOWN_LISTID = b'6'
ALLOCREJCODE_OTHER = b'7'

# Tag 89
TAG_SIGNATURE = b'89'

# Tag 90
TAG_SECUREDATALEN = b'90'

# Tag 91
TAG_SECUREDATA = b'91'

# Tag 92
TAG_BROKEROFCREDIT = b'92'

# Tag 93
TAG_SIGNATURELENGTH = b'93'

# Tag 94
TAG_EMAILTYPE = b'94'
EMAILTYPE_NEW = b'0'
EMAILTYPE_REPLY = b'1'
EMAILTYPE_ADMIN_REPLY = b'2'

# Tag 95
TAG_RAWDATALENGTH = b'95'

# Tag 96
TAG_RAWDATA = b'96'

# Tag 97
TAG_POSSRESEND = b'97'

# Tag 98
TAG_ENCRYPTMETHOD = b'98'
ENCRYPTMETHOD_NONE = b'0'
ENCRYPTMETHOD_PKCS = b'1'
ENCRYPTMETHOD_DES = b'2'
ENCRYPTMETHOD_PKCS_DES = b'3'
ENCRYPTMETHOD_PGP_DES = b'4'
ENCRYPTMETHOD_PGP_DES_MD5 = b'5'
ENCRYPTMETHOD_PEM_DES_MD5 = b'6'

# Tag 99
TAG_STOPPX = b'99'

# TAg 100
TAG_EXDESTINATION = b'100'

# Tag 101

# Tag 102
TAG_CXLREJREASON = b'102'
CXLREJREASON_TOO_LATE_TO_CANCEL = b'0'
CXLREJREASON_UNKNOWN_ORDER = b'1'
CXLREJREASON_BROKER_OPTION = b'2'
CXLREJREASON_ORDER_ALREADY_PENDING_CANCEL = b'3'

# Tag 103
TAG_ORDERREJREASON = b'103'
ORDERREJREASON_BROKER_OPTION = b'0'
ORDERREJREASON_UNKNOWN_SYMBOL = b'1'
ORDERREJREASON_EXCHANGE_CLOSED = b'2'
ORDERREJREASON_ORDER_EXCEEDS_LIMIT = b'3'
ORDERREJREASON_TOO_LATE_TO_ENTER = b'4'
ORDERREJREASON_UNKNOWN_ORDER = b'5'
ORDERREJREASON_DUPLICATE_ORDER = b'6'
ORDERREJREASON_DUPLICATE_OF_VERBALLY_COMMUNICATED_ORDER = b'7'
ORDERREJREASON_STALE_ORDER = b'8'

# Tag 104
TAG_IOIQUALIFIER = b'104'
IOIQUALIFIER_ALL_OR_NONE = b'A'
IOIQUALIFIER_AT_THE_CLOSE = b'C'
IOIQUALIFIER_IN_TOUCH_WITH = b'I'
IOIQUALIFIER_LIMIT = b'L'
IOIQUALIFIER_MORE_BEHIND = b'M'
IOIQUALIFIER_AT_THE_OPEN = b'O'
IOIQUALIFIER_TAKING_A_POSITION = b'P'
IOIQUALIFIER_AT_THE_MARKET = b'Q'
IOIQUALIFIER_PORTFOLIO_SHOWN = b'S'
IOIQUALIFIER_THROUGH_THE_DAY = b'T'
IOIQUALIFIER_VERSUS = b'V'
IOIQUALIFIER_INDICATION_WORKING_AWAY = b'W'
IOIQUALIFIER_CROSSING_OPPORTUNITY = b'X'
IOIQUALIFIER_AT_THE_MIDPOINT = b'Y'
IOIQUALIFIER_PRE_OPEN = b'Z'

# Tag 105
TAG_WAVENO = b'105'

# Tag 106
TAG_ISSUER = b'106'

# Tag 107
TAG_SECURITYDESC = b'107'

# Tag 108
TAG_HEARTBTINT = b'108'

# Tag 109
TAG_CLIENTID = b'109'

# Tag 110
TAG_MINQTY = b'110'

# Tag 111
TAG_MAXFLOOR = b'111'

# Tag 112
TAG_TESTREQID = b'112'

# Tag 113
TAG_REPORTTOEXCH = b'113'

# Tag 114
TAG_LOCATEREQD = b'114'

# Tag 115
TAG_ONBEHALFOFCOMPID = b'115'

# Tag 116
TAG_ONBEHALFOFSUBID = b'116'

# Tag 117
TAG_QUOTEID = b'117'

# Tag 118
TAG_NETMONEY = b'118'

# Tag 119
TAG_SETTLCURRAMT = b'119'

# Tag 120
TAG_SETTLCURRENCY = b'120'

# Tag 122
TAG_ORIGSENDINGTIME = b'122'

# Tag 123
TAG_GAPFILLFLAG = b'123'
GAPFILLFLAG_NO = b'N'
GAPFILLFLAG_YES = b'Y'

# Tag 131
TAG_QUOTEREQID = b'131'

# Tag 132
TAG_BIDPX = b'132'

# Tag 133
TAG_ASKBX = b'133'

# Tag 141
TAG_RESETSEQNUMFLAG = b'141'
RESETSEQNUMFLAG_NO = b'N'
RESETSEQNUMFLAG_YES = b'Y'

# Tag 150
TAG_EXECTYPE = b'150'
EXECTYPE_NEW = b'0'
EXECTYPE_PARTIAL_FILL = b'1'
EXECTYPE_FILL = b'2'
EXECTYPE_DONE_FOR_DAY = b'3'
EXECTYPE_CANCELED = b'4'
EXECTYPE_REPLACE = b'5'
EXECTYPE_PENDING_CANCEL = b'6'
EXECTYPE_STOPPED = b'7'
EXECTYPE_REJECTED = b'8'
EXECTYPE_SUSPENDED = b'9'
EXECTYPE_PENDING_NEW = b'A'
EXECTYPE_CALCULATED = b'B'
EXECTYPE_EXPIRED = b'C'
EXECTYPE_RESTATED = b'D'
EXECTYPE_PENDING_REPLACE = b'E'

# Tag 151
TAG_LEAVESQTY = b'151'

# Tag 152
TAG_CASHORDERQTY = b'152'

# Tag 167
TAG_SECURITYTYPE = b'167'
SECURITYTYPE_WILDCARD_ENTRY = b'?'
SECURITYTYPE_BANKERS_ACCEPTANCE = b'BA'
SECURITYTYPE_CONVERTIBLE_BOND = b'CB'
SECURITYTYPE_CERTIFICATE_OF_DEPOSIT = b'CD'
SECURITYTYPE_COLLATERALIZE_MORTGAGE_OBLIGATION = b'CMO'
SECURITYTYPE_CORPORATE_BOND = b'CORP'
SECURITYTYPE_COMMERCIAL_PAPER = b'CP'
SECURITYTYPE_CORPORATE_PRIVATE_PLACEMENT = b'CPP'
SECURITYTYPE_COMMON_STOCK = b'CS'
SECURITYTYPE_FEDERAL_HOUSING_AUTHORITY = b'FHA'
SECURITYTYPE_FEDERAL_HOME_LOAN = b'FHL'
SECURITYTYPE_FEDERAL_NATIONAL_MORTGAGE_ASSOCIATION = b'FN'
SECURITYTYPE_FOREIGN_EXCHANGE_CONTRACT = b'FOR'
SECURITYTYPE_FUTURE = b'FUT'
SECURITYTYPE_GOVERNMENT_NATIONAL_MORTGAGE_ASSOCIATION = b'GN'
SECURITYTYPE_TREASURIES_PLUS_AGENCY_DEBENTURE = b'GOVT'
SECURITYTYPE_MORTGAGE_IOETTE = b'IET'
SECURITYTYPE_MUTUAL_FUND = b'MF'
SECURITYTYPE_MORTGAGE_INTEREST_ONLY = b'MIO'
SECURITYTYPE_MORTGAGE_PRINCIPAL_ONLY = b'MPO'
SECURITYTYPE_MORTGAGE_PRIVATE_PLACEMENT = b'MPP'
SECURITYTYPE_MISCELLANEOUS_PASS_THRU = b'MPT'
SECURITYTYPE_MUNICIPAL_BOND = b'MUNI'
SECURITYTYPE_NO_ISITC_SECURITY_TYPE = b'NONE'
SECURITYTYPE_OPTION = b'OPT'
SECURITYTYPE_PREFERRED_STOCK = b'PS'
SECURITYTYPE_REPURCHASE_AGREEMENT = b'RP'
SECURITYTYPE_REVERSE_REPURCHASE_AGREEMENT = b'RVRP'
SECURITYTYPE_STUDENT_LOAN_MARKETING_ASSOCIATION = b'SL'
SECURITYTYPE_TIME_DEPOSIT = b'TD'
SECURITYTYPE_US_TREASURY_BILL = b'USTB'
SECURITYTYPE_WARRANT = b'WAR'
SECURITYTYPE_CATS_TIGERS_LIONS = b'ZOO'

# Tag 297
TAG_QUOTESTATUS = b'297'
QUOTESTATUS_ACCEPTED = b'0'
QUOTESTATUS_CANCELED_FOR_SYMBOL = b'1'
QUOTESTATUS_CANCELED_FOR_SECURITY_TYPE = b'2'
QUOTESTATUS_CANCELED_FOR_UNDERLYING = b'3'
QUOTESTATUS_CANCELED_ALL = b'4'
QUOTESTATUS_REJECTED = b'5'
QUOTESTATUS_REMOVED_FROM_MARKET = b'6'
QUOTESTATUS_EXPIRED = b'7'
QUOTESTATUS_QUERY = b'8'
QUOTESTATUS_QUOTE_NOT_FOUND = b'9'
QUOTESTATUS_PENDING = b'10'
QUOTESTATUS_PASS = b'11'
QUOTESTATUS_LOCKED_MARKET_WARNING = b'12'
QUOTESTATUS_CROSS_MARKET_WARNING = b'13'
QUOTESTATUS_CANCELED_DUE_TO_LOCK_MARKET = b'14'
QUOTESTATUS_CANCELED_DUE_TO_CROSS_MARKET = b'15'

# Tag 373
TAG_SESSIONREJECTREASON = b'373'
SESSIONREJECTREASON_INVALID_TAG_NUMBER = b'0'
SESSIONREJECTREASON_REQUIRED_TAG_MISSING = b'1'
SESSIONREJECTREASON_TAG_NOT_DEFINED_FOR_THIS_MESSAGE_TYPE = b'2'
SESSIONREJECTREASON_UNDEFINED_TAG = b'3'
SESSIONREJECTREASON_TAG_SPECIFIED_WITHOUT_A_VALUE = b'4'
SESSIONREJECTREASON_VALUE_INCORRECT_FOR_THIS_TAG = b'5'
SESSIONREJECTREASON_INCORRECT_DATA_FORMAT_FOR_VALUE = b'6'
SESSIONREJECTREASON_DECRYPTION_PROBLEM = b'7'
SESSIONREJECTREASON_SIGNATURE_PROBLEM = b'8'
SESSIONREJECTREASON_COMPID_PROBLEM = b'9'
SESSIONREJECTREASON_SENDINGTIME_ACCURACY_PROBLEM = b'10'
SESSIONREJECTREASON_INVALID_MSGTYPE = b'11'
SESSIONREJECTREASON_XML_VALIDATION_ERROR = b'12'
SESSIONREJECTREASON_TAG_APPEARS_MORE_THAN_ONCE = b'13'
SESSIONREJECTREASON_TAG_SPECIFIED_OUT_OF_REQUIRED_ORDER = b'14'
SESSIONREJECTREASON_REPEATING_GROUP_FIELDS_OUT_OF_ORDER = b'15'
SESSIONREJECTREASON_INCORRECT_NUMINGROUP_COUNT = b'16'
SESSIONREJECTREASON_NON_DATA_VALUE_INCLUDES_FIELD_DELIMITER = b'17'
SESSIONREJECTREASON_OTHER = b'99'

# Tag 423
TAG_PRICETYPE = b'423'
PRICETYPE_PERCENTAGE = b'1'
PRICETYPE_PER_UNIT = b'2'
PRICETYPE_FIXED_AMOUNT = b'3'

# Tag 434
TAG_CXLREJRESPONSETO = b'434'
CXLREJRESPONSETO_ORDER_CANCEL_REQUEST = b'1'
CXLREJRESPONSETO_ORDER_CANCEL_REPLACE_REQUEST = b'2'

# Tag 658
TAG_QUOTEREQUESTREJECTREASON = b'658'
QUOTEREQUESTREJECTREASON_UNKNOWN_SYMBOL = b'1'
QUOTEREQUESTREJECTREASON_EXCHANGE = b'2'
QUOTEREQUESTREJECTREASON_QUOTE_REQUEST_EXCEEDS_LIMIT = b'3'
QUOTEREQUESTREJECTREASON_TOO_LATE_TO_ENTER = b'4'
QUOTEREQUESTREJECTREASON_INVALID_PRICE = b'5'
QUOTEREQUESTREJECTREASON_NOT_AUTHORIZED_TO_REQUEST_QUOTE = b'6'
QUOTEREQUESTREJECTREASON_NO_MATCH_FOR_INQUIRY = b'7'
QUOTEREQUESTREJECTREASON_NO_MARKET_FOR_INSTRUMENT = b'8'
QUOTEREQUESTREJECTREASON_NO_INVENTORY = b'9'
QUOTEREQUESTREJECTREASON_PASS = b'10'
QUOTEREQUESTREJECTREASON_OTHER = b'99'

# Tag 693
TAG_QUOTERESPID = b'693'

# Tag 2759
TAG_GROUPAMOUNT = b'2759'

# Tag 2760
TAG_GROUP_REMAINING_AMOUNT = b'2760'

# Tag 2761
TAG_ALLOCGROUPAMOUNT = b'2761'
