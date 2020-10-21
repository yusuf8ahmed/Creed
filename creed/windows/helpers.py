import sys

# Execptions
class WindowsInstCorrectVersion(Exception):
    """Exception raised when Windows plaform inst Windows 10"""
    def __init__(self):
        pass

class PlaformIsntWindows(Exception):
    """Exception raised when Windows plaform inst Windows 10"""
    def __init__(self):
        pass

class NotificationError(Exception):
    """Exception raised when a Notification Error happens"""
    def __init__(self):
        pass

# Helper Functions
def get_windows_version():
    wv = sys.getwindowsversion()
    if hasattr(wv, 'service_pack_major'):  # python >= 2.7
        sp = wv.service_pack_major or 0
    else:
        import re
        r = re.search("\s\d$", wv.service_pack)
        sp = int(r.group(0)) if r else 0
    return (wv.major, wv.build)

def stoms(s):
    """ STOMS: seconds to milliseconds """
    return s * 1000
