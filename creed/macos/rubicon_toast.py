import os
import platform
import subprocess

if platform.system().lower().startswith('dar'):
    """
    Darwin MacOS
    """
    from ctypes import cdll, util
    from rubicon.objc import ObjCClass

    NSUserNotification = ObjCClass('NSUserNotification')
    NSUserNotificationCenter = ObjCClass('NSUserNotificationCenter')
    NSDate = ObjCClass('NSDate')
else:
    raise SystemExit(f'Macos Rubicon Notifications are not supported for {platform.system()} system')

__author__ = 'Chromazmoves'
__license__ = 'MIT'

PYTHON_IMAGE = os.path.join(os.path.dirname(os.path.realpath(__file__)), "python.ico")
PYTHON_IMAGE_PNG = os.path.join(os.path.dirname(os.path.realpath(__file__)), "python_png.png")

class NativeNotif:
    def __init__(self):
        pass
        
    def create(self, title, subtitle):
        if platform.system().lower().startswith('dar'):
            """
            Darwin MacOS
            """
            try:
                nc = NSUserNotificationCenter.defaultUserNotificationCenter
                n = NSUserNotification.alloc().init()
                n.title = title
                n.informativeText = subtitle
                n.deliveryDate = NSDate.dateWithTimeInterval(0, sinceDate=NSDate.date())
                nc.scheduleNotification(n)
                return True
            except BaseException as e:
                print("Cookie: MacOS Toast Error: {}".format(e))
                raise NativeNotificationError

    
        except BaseException as e:
                print("Cookie: Toast error: {}".format(e))
                raise NativeNotificationError
