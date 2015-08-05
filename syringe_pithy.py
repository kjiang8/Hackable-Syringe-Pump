from pithy import *
from urllib import urlopen as uo
import ast
from time import sleep,time

#IP address
site = "http://localhost:9005"

#write to serial port (expects 0 to 255)
def awrite(val):
    uo(site+"/write/"+str(val)).read()
    sleep(.5)
 
def aread():
    return uo(site+"/read/").read()

string = ""; 

def syringe(direction, volume = 0.0, time = 0.0, flowrate = 0.0):
    if volume == 0.0:
        print "case 1"
        volume = float(flowrate*time*3600) #mL
    
    elif time == 0.0:
        print "case 2"
        time = float(volume / flowrate) #minutes
    
    elif flowrate == 0.0:
        print "case 3"
        flowrate = float(volume / time) #mL/minute
    
    else:
        print "need to input 2/3 of volume, time, or flowrate"
    
    if direction.lower() == 'forward':
        direction = '1'
    else:
        direction = '2' 
        
    steps = volume*800 + 400 #added 400 compensates for lag at start
    speed = str(int(steps/(time*200))) #convert 200 steps/rev, to speed in rpm
    steps = str(steps)


    while len(steps)<5:
        steps = '0' + steps
    while len(speed)<3:
        speed = '0' + speed

    string = steps + speed + direction
    print "string: ", string

    print "volume(mL): ", volume
    print "time(s): ", time*60
    print "flowrate(cc/min): ", flowrate
    print "steps: ", steps
    print "speed(rpm): ", speed
    
    awrite(string)
    sleep(time*60)


syringe('forward', time=0.7, volume=10)


