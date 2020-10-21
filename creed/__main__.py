"""creed: the one and only python cross-platform Toaster/Notification """

#stan
import os
import platform
import subprocess

if platform.system().lower().startswith('win'): 
    """
    Windows NT:
    """
    # pythonnet is need for Windows
    import clr
    clr.AddReference("System.Windows.Forms")
    import System.Windows.Forms as WinForms
    clr.AddReference("System.Drawing")
    from System.Drawing import SystemIcons, Icon
elif platform.system().lower().startswith('lin'):
    """
    Linux
    """
elif platform.system().lower().startswith('dar'):
    """
    Darwin MacOS
    """
    from ctypes import cdll, util
    from rubicon.objc import ObjCClass

    NSUserNotification = ObjCClass('NSUserNotification')
    NSUserNotificationCenter = ObjCClass('NSUserNotificationCenter')
    NSDate = ObjCClass('NSDate')

else:
    raise SystemExit(f'Notifications are not supported for {platform.system()} system')

__author__ = 'Chromazmoves'
__license__ = 'MIT'
__all__ = ["NativeIcon", "NativeBalloonTipIcon", "NativeNotificationError", "NativeNotif"]

PYTHON_IMAGE = os.path.join(os.path.dirname(os.path.realpath(__file__)), "python.ico")
PYTHON_IMAGE_PNG = os.path.join(os.path.dirname(os.path.realpath(__file__)), "python_png.png")

def stoms(s):
    """ STOMS: seconds to milliseconds """
    return s * 1000

class NativeIcon:
    """ Used for System.Drawing.SystemIcons """  
    Application = SystemIcons.Application
    Asterisk = SystemIcons.Asterisk
    Equals = SystemIcons.Equals
    Error = SystemIcons.Error
    Exclamation = SystemIcons.Exclamation
    Hand = SystemIcons.Hand
    Information = SystemIcons.Information
    Question = SystemIcons.Question
    Shield = SystemIcons.Shield
    Warning = SystemIcons.Warning
    Custom = Icon

class NativeBalloonTipIcon:
    """ Used for System.Windows.Forms.NotifyIcon().BalloonTipIcon"""    
    Error = WinForms.ToolTipIcon.Error
    Info = WinForms.ToolTipIcon.Info
    Warning_ = WinForms.ToolTipIcon.Warning
    None_ = getattr(WinForms.ToolTipIcon, 'None')

#* Native Iterface Notification Starts Here
  
class NativeNotificationError(Exception):
    """Exception raised when a Notification Error happens"""
    def __init__(self):
        pass

class NativeNotif:
    """
        # This class is dependent on the Native bridge's to your OS to start   
        Makes toast for every major os Windows, Mac & linux.  
        ✔️ = Working       Windows 10 = ✔️   MacOS Catalina = 🤷    Ubuntu = 🤷  
        ❌ = Not Working   Windows 8.1 = ✔️  MacOS Mojave = ✔️      Debian = 🤷  
        🤷 = I Dont Know   Windows 7 = ✔️    MacOS High Sierra = 🤷 CentOS = 🤷  
        >Send Testing for new OS or OS version to PR or Issues Tab  
    """
    def __init__(self, title, message, duration=10, icon=None, urgency="low"):
        """Inits Notif with title, message, duration, urgency, icon_path"""
        self.title = title
        self.message = message
        self.duration = stoms(duration)
        self.icon = icon
        self.urgency = urgency
        
    def __repr__(self):
        return f"<{self.__module__}.{type(self).__name__} object at {hex(id(self))} with attrs {self.title} {self.message} {self.duration} {self.icon} {self.urgency}>"

    def __str__(self):
        return f"<{self.title} {self.message} {self.duration} {self.icon} {self.urgency}>"

    def Toast(self):
        try:
            if platform.system().lower().startswith('win'): 
                """
                Windows NT:
                """
                try:
                    notifyIcon1 = WinForms.NotifyIcon()
                    if self.icon == None:
                        # only .ico file allowed
                        notifyIcon1.Icon = NativeIcon.Custom(PYTHON_IMAGE) 
                    else:
                        notifyIcon1.Icon = NativeIcon.Custom(icon)
                    notifyIcon1.BalloonTipTitle = self.title 
                    notifyIcon1.BalloonTipText = self.message
                    notifyIcon1.BalloonTipIcon = NativeBalloonTipIcon.None_
                    notifyIcon1.Visible = True
                    notifyIcon1.ShowBalloonTip(self.duration)
                    return True
                except BaseException as e:
                    print("Cookie: Windows Toast Error: {}".format(e))
                    raise NativeNotificationError

            elif platform.system().lower().startswith('lin'):
                """
                Linux
                """
                try:
                    return True
                except BaseException as e:
                    print("Cookie: Linux Toast Error: {}".format(e))
                    raise NativeNotificationError

            elif platform.system().lower().startswith('dar'):
                """
                Darwin MacOS
                """
                try:
                    nc = NSUserNotificationCenter.defaultUserNotificationCenter
                    n = NSUserNotification.alloc().init()
                    n.title = title
                    n.informativeText = message
                    n.userInfo = {}
                    n.deliveryDate = NSDate.dateWithTimeInterval(0, sinceDate=NSDate.date())
                    nc.scheduleNotification(n)
                    return True
                except BaseException as e:
                    print("Cookie: MacOS Toast Error: {}".format(e))
                    raise NativeNotificationError
            else:
                raise SystemError(f'Notifications are not supported for {platform.system()} system')

        except BaseException as e:
                print("Cookie: Toast error: {}".format(e))
                raise NativeNotificationError
