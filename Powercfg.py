#!/usr/bin/env python3
# Wrapper for powercfg /list and powercfg /setactive
import subprocess
import re

class Powercfg:
    def __init__(self):
        pass

    def __status(self):
        planlistpattern = re.compile(':\s+([a-z0-9-]+)\s+\((.*)\)\s*(\*?)')
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        result = subprocess.check_output(["powercfg", "/LIST"], universal_newlines=True, shell=False, startupinfo=startupinfo)
        #print(result)
        self.plans = planlistpattern.findall(result)
        self.plans = [(pid, name, bool(star)) for pid, name, star in self.plans]

    def __activate(self, pid):
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        try:
            subprocess.check_call(["powercfg", "/SETACTIVE", pid], shell=False, startupinfo=startupinfo)
        except subprocess.CalledProcessError:
            pass
        return self.active()
    
        
    def active(self):
	    # Get current active power plan id and name
        self.__status()
        for pid, name, active in self.plans:
            if active:
                return (pid, name)

    def plans(self):
	    # Get all available power plans (id, name, isactive)
        self.__status()
        return self.plans

    def activate(self, plan):
	    # Activate a powerplan. plan can be either a plan name or a plan id
        self.__status()
        idpattern = re.compile('[a-z0-9]{8}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{12}')
        if idpattern.match(plan):
            return self.__activate(plan)
        else:
            for pid, name, active in self.plans:
                if name == plan:
                    return self.__activate(pid)
            print("No plan with name name '%s' found" % plan)
    
