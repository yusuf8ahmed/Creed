"""
to use this package 
-Must be Python 3+
-Must be Windows 10
"""
import sys
import platform
from xml.etree.ElementTree import Element, SubElement, tostring

from helpers import WindowsInstCorrectVersion, PlaformIsntWindows
from helpers import get_windows_version, NotificationError, stoms

if platform.system().lower().startswith('win'): 
    #pywinrt stuff
    import winrt.windows.ui.notifications as notifications
    import winrt.windows.data.xml.dom as dom
else:
    raise PlaformIsntWindows

class XlangNotification:
    def __init__(self, appname="Python Notification", group="Group-1", tag="Group-2"):
        if get_windows_version()[0] != 10:
            # Must be Windows 10
            raise WindowsInstCorrectVersion
        self.manager = notifications.ToastNotificationManager
        self.xml_document = dom.XmlDocument()
        self.appname = appname
        self.group = group
        self.tag = tag

    def _create_template(self, template):
        root = Element("toast")
        visual = SubElement(root, "visual")
        binding = SubElement(visual, "binding", {'template': template})
        return root, binding

    def text_one(self, title):
        root, binding = self._create_template("ToastText01")
        text_title = SubElement(binding, "text", {'id': '1'})
        text_title.text = title
        self.notif = tostring(root).decode("utf-8")
        return self

    def text_two(self, title, subtitle):
        root, binding = self._create_template("ToastText02")
        text_title = SubElement(binding, "text", {'id': '1'})
        text_title.text = title
        text_subtitle = SubElement(binding, "text", {'id': '2'})
        text_subtitle.text = subtitle
        self.notif = tostring(root).decode("utf-8")
        return self

    def push(self):
        self.xml_document.load_xml(self.notif)
        notif_clean = notifications.ToastNotification(self.xml_document)
        notif_clean.group = self.group
        notif_clean.tag = self.tag
        notifier = self.manager.create_toast_notifier(self.appname); #display notification
        notifier.show(notif_clean)

if __name__ == "__main__":
    notification = XlangNotification()
    notification.text_two("hello", "bye").push()




