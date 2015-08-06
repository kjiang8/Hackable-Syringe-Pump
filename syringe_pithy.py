from pithy import *
from urllib import urlopen as uo
import ast
from time import sleep,time

#IP address or localhost
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
    thickness = 1/area/800 #experimentally found it takes 800 steps for 1 mL
    #print "thickness of 1 step (cm): ", thickness
    return thickness
    

def syringe(direction, diameter, volume = 0.0, time = 0.0, flowrate = 0.0):
    
    try:
    
        area = (diameter/20.0)**2*math.pi #cross sectional area of pump in cm^2
        stepLength = thickness() #cm distance of 1 step calculated by thickness()
        
        if volume == 0.0:
            print "calculating displaced volume"
            volume = float(flowrate*time*3600) #mL
        
        elif time == 0.0:
            print "calculating time of pump operation"
            time = float(volume / flowrate) #minutes
        
        elif flowrate == 0.0:
            print "calculating flowrate of the pump"
            flowrate = float(volume / time) #mL/minute
        
        else:
            print "please input 2 of the following: volume, time, or flowrate"
        
        if direction.lower() == 'forward':
            direction = '2' #backward in arduino code
        else:
            direction = '1' #forward in arduino code
            
        steps = int(round(volume/area/stepLength + 400, 2)) #added 400 compensates for lag at start
        speed = str(int(steps/(time*200))) #convert 200 steps/rev, to speed in rpm
        steps = str(steps)
    
        #add leading zeros to fill up the string properly
        while len(steps)<5:
            steps = '0' + steps
        while len(speed)<3:
            speed = '0' + speed
    
        #string that will be sent to the arduino, then to the motor
        string = steps + speed + direction
        print "string: ", string
    
        print "volume(mL): ", volume
        print "time(s): ", time*60
        print "flowrate(cc/min): ", flowrate
        print "steps: ", steps
        print "speed(rpm): ", speed
        
        #send string to arduino and motor
        awrite(string)
        #delay for 30 seconds after the motor stops running
        sleep(time + 30)
    
    except TypeError:
        print "please input a string for direction and int or float for the other inputs"
        
    except ZeroDivisionError:
        print "cannot divide by zero, please input non-zero values"
        
    except IOError:
        print "check to make sure serial ports are open and/or arguments are non-negative"

#call function for syringe pump operation
syringe('forward', 20.05, time=0.7, volume=10)



