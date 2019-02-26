import math
import time

#clamping values
def clamp(n, smallest, largest):
    return max(smallest, min(n, largest))

# remaps value x from range [a-b] to range [c-d]
def mapFromTo(x,a,b,c,d):
    x=clamp(x,a,b)
    y=(x-a)/(b-a)*(d-c)+c
    return round(y)

# REPL console interruptible sleep:
def isleep(duration_seconds):
    for i in range(1,duration_seconds):
        time.sleep (1)

#simple task manager for microcontrollers
class SimpleTaskManager:

    _intervals_ms={}
    _timers_next_ms={}
    debug = False

    #returns true if it is time to run the task, else returs false
    #returns true on unitialised tasks, False on undefined tasks
    def checktask(self, tname):
        if tname in self._timers_next_ms:
            if time.ticks_ms() > self._timers_next_ms[tname]:
                self._timers_next_ms[tname] += self._intervals_ms[tname]
                if self.debug : print("Running task:", tname) 
                return True
            else:
                return False
        else:
            if self.debug : print("Unknown task:", tname) 
            return False

    def addTask(self, tname, interval_ms):
        self._intervals_ms[tname]=interval_ms
        self._timers_next_ms[tname] = time.ticks_ms() + self._intervals_ms[tname]
        if self.debug : print("Configured tasks intervals:",self._intervals_ms) 
