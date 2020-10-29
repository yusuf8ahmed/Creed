<p align="center">
  <a>
    <img src="https://em.wattpad.com/fd2a405da529df03f21c13addff414a29ea0bf03/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f776174747061642d6d656469612d736572766963652f53746f7279496d6167652f764649326463486b5f6f57534b673d3d2d3537373139353238322e313533303432313134656264333264343839363331353937373336352e676966" alt="Py-Toast-JPG" border="0">
    <br>
    <br>
    <img src="https://pepy.tech/badge/creed">
    <img src="https://pepy.tech/badge/creed/month">
    <img src="https://pepy.tech/badge/creed/week">  
    <br>
    <br>
    <img src="https://forthebadge.com/images/badges/oooo-kill-em.svg">
    <img src="https://forthebadge.com/images/badges/made-with-crayons.svg">
    <img src="https://forthebadge.com/images/badges/no-ragrets.svg">
  </a>
</p>

# Creed
Hi, Creed is a python package that is allow for platform/os agnostic notifications

## Notifications
### Windows
- Xlang
```python
  from creed import XlangNotification
  notification = XlangNotification()
  notification.text_two("hello", "bye").push()
```
- Pythonnet
```python
  from creed import NetNotification
  notification = NetNotification()
  notification.create("hello", "bye", duration=10, icon=NativeIcon.Application).push()
```
### Macos
- Custom
```python
# Not Working: uses c module as backend 
  from creed import MacOSNotification
  notifcation = MacOSNotification()
  MacOSNotification.set_bundle_identifier('com.apple.finder') #makes logo to finder
  MacOSNotification.send_notification('New file created',
                                      subtitle='why you make file', 
                                      text='are poopoo')
```
- AppleScript 
```python
# uses commandline
  from creed import AppleScriptNotification
  notif = AppleScriptNotification()
  notif.create("title", "bye").push()
```
- Rubicon
```python
# Not Working
  from creed import RubiconNotification
  notifcation = RubiconNotification()
  notification.create("hello", "bye").push()
```
- Pyobjc
```python
# Not Working
  from creed import PyObjcNotification
  notifcation = PyObjcNotification()
  notification.create("hello", "bye").push()
```
### Linux
- Custom
```python
# uses commandline
    from creed import LinuxCommandLineNotification
    notification = LinuxCommandLineNotification()
    notification.create("hello", "bye").push()
```
- PyGObject
```python
  from creed import GiNotification
  notification = GiNotification()
  notification.create("hello", "bye").push()
```
