###Hackable Syringe Pump

If you want to be able to control an open source syringe pump
* with an arduino
* using python
* with others
* from anywhere

this will show you how. This modifies the [open-source syringe pump](http://www.appropedia.org/Open-source_syringe_pump) (also found [here](http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0107216)) by Michigan Tech's Open Sustainability Technology Lab to use Arduino, not Raspberry Pi. Python is then used to control the motor through [pithy](https://github.com/dansteingart/pithy) and [nodeforwarder](https://github.com/dansteingart/nodeforwarder). 

###Code Examples

Instead of calculating the rpm and steps needed to control a motor, this program takes in any 2 of the following:
* volume (mL)
* time (min)
* flowrate (mL/min)

calculates the remaining parameter and automatically runs the motor at the required speed and steps. 

For example,

	syringe(‘forward’, time=0.7, volume=10)

will push the syringe forward for 0.7 minutes (42 seconds) to dispense 10mL of liquid. The motor moves 8400 steps at 60 rpm. 

	syringe(direction[, time=0, volume=0, flowrate=0])

The function syringe only has 1 required parameter, direction, which is either ‘forward’ or ‘backward’. The other three default to 0 and will be changed when given. 

###How it Works

Pithy writes a string to a url, which acts like a serialport thanks to nodeforwarder. Arduino then reads off the serialport and runs the motor accordingly. 


###Building the Pump

Please refer to the [instructions](http://www.appropedia.org/Open-source_syringe_pump) from Michigan Tech to build the open-source syringe pump.

Also refer to the documentation file for more specific details on how we printed ours. 

###Additional Hardware

In addition to the parts needed to build the syringe pump, the parts for the arduino / pithy controller include:
* Arduino Uno (we used R3, but any version works)
* Adafruit Motor Shield v2
* Micro-USB adaptor cable (to connect the board to the computer)
* 4 wires to connect motor to motor shield

Attach the Adafruit Motor Shield onto the Arduino, and attach the syringe pump motor to the M3 and M4 motor ports on the shield. 

###Software Prerequisites

To run this, you will need:
* [python 2.7](https://www.python.org/downloads/)
* [node.js](https://nodejs.org/)
* [arduino](https://www.arduino.cc/en/Main/Software)
* [adafruit motor shield library v2](https://learn.adafruit.com/adafruit-motor-shield-v2-for-arduino/install-software)

###Software Installation

1. Download [nodeforwarder](https://github.com/dansteingart/nodeforwarder) and follow directions. Note: our arduino code uses a serial speed of 9600.
2. Download [pithy](https://github.com/dansteingart/pithy) and follow directions. 
3. Clone this repository 
4. If a serialport is open using nodeforwarder, close it, as only one thing can talk to the serialport at one time. Then download sketch_aug04a_workingstepper to the arduino. The serialport should read “Stepper test successful!”
5. Open a serialport on 9005 (or whatever number, just remember to change it in pithy) using nodeforwarder.
6. Open syringe.py using pithy and run the code. 

And that’s it! 

###Special thanks to

* [Lindsey Adamson](https://github.com/LindseyCAdamson)
* [Kathryn Jiang](https://github.com/kjiang8)
* [Dan Steingart](https://github.com/dansteingart)

