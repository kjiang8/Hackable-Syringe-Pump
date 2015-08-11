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

def thickness(): #calibration function to get distance travelled in one step of motor. based off of the HSW norm-ject 20mL syringe
    diameter = 20.05 #mm for 20mL pump as reference
    area = (diameter/20.0)**2*math.pi #divided by 20.0 to have cross-sectional area in cm^2
    #print "area (cm^2): ",area
    #print "thickness of 1mL (cm): ", 1/area
    thickness = 1/area/804 #experimentally found it takes 804 steps for 1 mL
    #print "thickness of 1 step (cm): ", thickness
    return thickness
    

def syringe(direction, diameter, volume = 0.0, time = 0.0, flowrate = 0.0):
    
    try:
    
        area = (diameter/20.0)**2*math.pi #cross sectional area of pump in cm^2
        stepLength = thickness() #cm distance of 1 step calculated by thickness()
        
        if volume == 0.0:
            print "case 1"
            volume = float(flowrate*time) #mL
        
        elif time == 0.0:
            print "case 2"
            time = float(volume) / flowrate #minutes
        
        elif flowrate == 0.0:
            print "case 3"
            flowrate = float(volume) / time #mL/minute
        
        else:
            print "need to input 2/3 of volume, time, or flowrate"
        
        if direction.lower() == 'forward':
            direction = '1' #backward in arduino code
        else:
            direction = '2' #forward in arduino code
            
        steps = int(round(volume/area/stepLength, 2))
        speed = str(int(steps/(time*200))) #convert 200 steps/rev, to speed in rpm
        steps = str(steps)
    
        while len(steps)<5:
            steps = '0' + steps
        while len(speed)<3:
            speed = '0' + speed
    
        string = speed + steps + direction
        print "string: ", string
    
        print "volume(mL): ", volume
        print "time(s): ", time*60
        print "flowrate(cc/min): ", flowrate
        print "steps: ", steps
        print "speed(rpm): ", speed
        
        awrite(string)
        sleep(time*60)
    
    except TypeError:
        print "please input a string for direction and int or float for the other inputs"
        
    except ZeroDivisionError:
        print "cannot divide by zero, please input non-zero values"
        
    except IOError:
        print "check to make sure serial ports are open and/or arguments are non-negative"


#syringe('forward' or 'backward', syringe diameter(mm), [2 out of the following: volume (mL), time (min), flowrate (cc/min)])
syringe('forward', 20.05, time=0.2, flowrate=5) 

