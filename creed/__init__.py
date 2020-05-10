"""PyToast: the one only cross-platform Toaster/Notification in python """

import os
import platform

__all__ = ['Notification', 'NotificationError']

#env\Scripts\activate

class NotificationError(Exception):
    """Exception raised when a Notification Error happens"""
    def __init__(self):
        pass

class Notif:
    """
        Makes toast for every major os Windows, Mac & linux

        >Send toast on Windows https://stackoverflow.com/questions/17651017/python-post-osx-notification
        >Send toast on linux https://github.com/YuriyLisovskiy/pynotifier
        >Send toast on MacOS https://stackoverflow.com/questions/17651017/python-post-osx-notification
        
        ✔️ = Working
        ❌ = Not Working
        ❔ = I Dont Know

        Windows 10 = ✔️  MacOS Catalina = ❔     Ubuntu = ❔
        Windows 8.1 = ❔  MacOS Mojave = ✔️      Debian = ❔
        Windows 7 = ❔    MacOS High Sierra = ❔  CentOS = ❔

        || Send Testing for new OS or OS version to the issuse tab plz

        Parameters
            ----------
            title : str
                title that the toast should display
            message : str
                message that the toast should display
            duration : str , (optional)
                the amount in seconds that toast show be visible
                defaults to 10 seconds  
            urgency : str , (optional) (linux)
                defaults to low
            icon-path : str, (optional) (linux, windows)
                the icon to show on the toast
                image must be 
                    .ico for windows
                    .png for linux

        Returns
            ----------
            True : Boolean (Implementation Soon)
                returns 'True' if an error occured
            False : Boolean (Implementation Soon)
                returns 'False' if an error has not occured

        """
    def __init__(self, title, message, duration=10, urgency="low", icon_path="python.ico"):
        self.title = title
        self.message = message
        self.duration = duration
        self.urgency = urgency
        self.icon_path = icon_path

    def __repr__(self):
        return f"{self.message}"

    def __str__(self):
        return f"{self.message}"

    def Toast(self) -> bool:
        try:
            if platform.system().lower().startswith('win'): 
                """
                Windows NT
                """
                try:
                    try:
                        from win10toast import ToastNotifier
                    except ImportError as e:
                        print("Installing win10toast")
                        os.system('pip install win10toast')
                    finally:
                        from win10toast import ToastNotifier

                    toaster = ToastNotifier()
                    toaster.show_toast(self.title, self.message, icon_path=self.icon_path, duration=self.duration)
                    return True

                except BaseException as e:
                    # raise NotificationError
                    print("Cookie: Windows Toast Error: {}".format(e))
                    return False

            elif platform.system().lower().startswith('lin'):
                """
                Linux
                """
                URGENCY_LOW = 'low'
                URGENCY_NORMAL = 'normal'
                URGENCY_CRITICAL = 'critical'
                try:
                    import subprocess
                    if self.urgency not in [URGENCY_LOW, URGENCY_NORMAL, URGENCY_CRITICAL]:
                        print('Cookie: invalid urgency was given: {}').format(self.urgency)
                        urgency = "low"

                    command = [
                        'notify-send', '{}'.format(self.title),
                        '{}'.format(self.message),
                        '-u', self.urgency,
                        '-t', '{}'.format(self.duration * 1000)
                    ]
                    if icon_path is not None:
                        command += ['-i', self.icon_path]
                    subprocess.call(command)
                    return True
                except BaseException as e:
                    print("Cookie: Linux Toast Error: {}".format(e))
                    # raise NotificationError
                    return False

            elif platform.system().lower().startswith('dar'):
                """
                Darwin MacOS
                """
                try:
                    command = f""" osascript -e 'display notification "{self.message}" with title "{self.title}"' """
                    os.system(command)
                    return True
                except BaseException as e:
                    print("Cookie: MacOS Toast Error: {}".format(e))
                    # raise NotificationError
                    return False
            else:
                raise SystemError(f'Notifications are not supported for {platform.system()} system')

        except BaseException as e:
                print("Cookie: Toast error: {}".format(e))
                # raise NotificationError
                return False