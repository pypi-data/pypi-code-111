import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40x"

# Module version
version_str = "0.1.0.post130"
version_tuple = (0, 1, 0, 130)
try:
    from packaging.version import Version as V
    pversion = V("0.1.0.post130")
except ImportError:
    pass

# Data version info
data_version_str = "0.1.0.post4"
data_version_tuple = (0, 1, 0, 4)
try:
    from packaging.version import Version as V
    pdata_version = V("0.1.0.post4")
except ImportError:
    pass
data_git_hash = "ae8cce614fd18dcad1c880cc283943c694f0b8c7"
data_git_describe = "0.1.0-4-gae8cce6"
data_git_msg = """\
commit ae8cce614fd18dcad1c880cc283943c694f0b8c7
Merge: 35944de 9871699
Author: Arjan Bink <40633348+Silabs-ArjanB@users.noreply.github.com>
Date:   Thu Feb 17 12:15:48 2022 +0100

    Merge pull request #442 from Silabs-ArjanB/ArjanB_cch
    
    Added copyright headers (not an actual documentation update)

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_cv32e40x."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_cv32e40x".format(f))
    return fn
