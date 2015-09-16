#!/usr/bin/env python3
# Windows tray icon to switch between power plans
# Run with pyw.exe to avoid the console window.
# 
# To run it at windows startup:
# Press Win + R and run shell:startup to open to Autorun folder
# Create a new shortcut and point it to "pyw C:\your\path\to\pypowertray.pyw"

from SysTrayIcon import SysTrayIcon

from Powercfg import Powercfg

if __name__ == '__main__':

    powercfg = Powercfg()

    def activate(sysTrayIcon, name):
        pid, newname = powercfg.activate(name)
        sysTrayIcon.hover_text = newname
        sysTrayIcon.refresh_icon()

    def planswitcher(name):
        return lambda sysTrayIcon: activate(sysTrayIcon, name)

    current = "Power Options"
    menu_options = []
    for pid, name, active in powercfg.plans():
        menu_options.append((name, None, planswitcher(name)))
        if active:
            current = name

    def bye(sysTrayIcon): print ('Bye, then.')
    
    SysTrayIcon("power.ico", current, tuple(menu_options), on_quit=bye, default_menu_index=1)
