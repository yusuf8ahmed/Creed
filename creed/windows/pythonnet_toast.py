import platform

from helpers import WindowsInstCorrectVersion, PlaformIsntWindows
from helpers import get_windows_version, NotificationError, stoms

if platform.system().lower().startswith('win'): 
    #pythonnet stuff
    import clr
    clr.AddReference("System.Windows.Forms")
    import System.Windows.Forms as WinForms
    clr.AddReference("System.Drawing")
    from System.Drawing import SystemIcons, Icon
else:
    raise PlaformIsntWindows

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

class NetNotification:
    """
        # This class is dependent on the Native bridge's to your OS to start   
        Makes toast  
        ✔️ = Working       Windows 10 = ✔️   MacOS Catalina = 🤷    Ubuntu = 🤷  
        ❌ = Not Working   Windows 8.1 = ✔️  MacOS Mojave = ✔️      Debian = 🤷  
        🤷 = I Dont Know   Windows 7 = ✔️    MacOS High Sierra = 🤷 CentOS = 🤷  
        >Send Testing for new OS or OS version to PR or Issues Tab  
    """
    def __init__(self):
        pass

    def create(self, title, subtitle, duration, tip_icon=None, icon=None):
        self.title = title
        self.subtitle = subtitle
        self.tip_icon = tip_icon
        self.icon = icon
        # windows 10 wants in milliseconds so convert seconds to milliseconds
        self.duration = stoms(duration) 
        """
        Windows NT:
        """
        try:
            self.notification = WinForms.NotifyIcon()
            if self.icon == None:
                # only .ico file allowed
                self.notification.Icon = NativeIcon.Custom(PYTHON_IMAGE) 
            else:
                self.notification.Icon = self.icon
            if self.tip_icon == None:
                self.notification.BalloonTipIcon = NativeBalloonTipIcon.None_
            else:
                # check NativeBalloonTipIcon for others
                self.notification.BalloonTipIcon = self.tip_icon
            self.notification.BalloonTipTitle = self.title 
            self.notification.BalloonTipText = self.subtitle
            self.notification.Visible = True
            return self
        except BaseException as e:
            print("Cookie: Windows Toast Error: {}".format(e))
            raise NotificationError
        
    def push(self):
        self.notification.ShowBalloonTip(self.duration)

if __name__ == "__main__":
    notification = NetNotification()
    notification.create("hello", "bye", duration=10, icon=NativeIcon.Application).push()
