PowerPlansTray
==============

Tray icon to switch between power plans in Windows. Wrapper for **powercfg.exe**


Requires:
 * Python 2.7 or 3.x
 * [pywin32](http://sourceforge.net/projects/pywin32/) 
 * [SysTrayIcon.py](http://www.brunningonline.net/simon/blog/archives/SysTrayIcon.py.html)

Tested with Windows 10.

Run with `pyw.exe` or `pythonw.exe` to avoid the command line to open.

To run it at **windows startup**:
 * Press Win + R and run `shell:startup` to open the Autorun folder
 * Create a new shortcut and point it to `pyw C:\your\path\to\powertray.pyw`
 
 ![Screenshot of tray icon](https://raw.githubusercontent.com/cvzi/PowerPlansTray/master/screenshot.png)