#!/usr/bin/env python

# initial PyObjC code copied from:

# cocoa_keypress_monitor.py
# Copyright © 2016 Bjarte Johansen <Bjarte.Johansen@gmail.com>

from AppKit import NSApplication, NSApp
from Foundation import NSObject, NSLog
from Cocoa import NSEvent, NSKeyDownMask
from PyObjCTools import AppHelper
import keycode
import subprocess

'''
* In order to get the little python icon to go away,
* you have have to navigate to the directory:
* /System/Library/Frameworks/Python.framework/Versions/2.7/Resources/Python.app/Contents/
* and then edit the Info.plist file to include the key:
* <key>LSUIElement</key>
* <true/>

* You also may have to change sytem settings to allow Python to 
* control your computer. You do this by navigating to 
* System Preferences > Security & Privacy > Privacy > Accessibility
* And then check the box for python.

* In order to bind more shortcuts, just copy/paste the following lines:
* 	if "flags=[select flag]" in str(event) and 'chars="[select char]"' in str(event):
*		subprocess.Popen( ["/usr/bin/open", "-W", "-n", "-a", "/Applications/[select app].app"] )
* the cmd flag = 0x100108

* Might need to add some sort of cron job or functionality that
* initializes this on startup

* run with command:
* nohup python listener.py &
'''

class AppDelegate(NSObject):
    def applicationDidFinishLaunching_(self, notification):
        mask = NSKeyDownMask
        NSEvent.addGlobalMonitorForEventsMatchingMask_handler_(mask, handler)

def handler(event):
	if "flags=0x100108" in str(event) and 'chars="e"' in str(event):
		subprocess.Popen( ["/usr/bin/open", "-W", "-n", "-a", "/Applications/Utilities/Terminal.app"] )
	logFile = open("log.txt", 'a')
	print >> logFile, str(event)
	logFile.close()

	# try:
	# 	NSLog(u"%@", event)
	# except KeyboardInterrupt:
	# 	AppHelper.stopEventLoop()

def main():
    app = NSApplication.sharedApplication()
    delegate = AppDelegate.alloc().init()
    NSApp().setDelegate_(delegate)
    AppHelper.runEventLoop()
    
if __name__ == '__main__':
    main()