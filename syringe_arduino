/* This is a test sketch for the Adafruit assembled Motor Shield for Arduino v2
It won't work with v1.x motor shields! Only for the v2's with built in PWM
control

For use with the Adafruit Motor Shield v2 
---->  http://www.adafruit.com/products/1438
*/


#include <Wire.h>
#include <Adafruit_MotorShield.h>
#include "utility/Adafruit_PWMServoDriver.h"

// Create the motor shield object with the default I2C address
Adafruit_MotorShield AFMS = Adafruit_MotorShield(); 
// Or, create it with a different I2C address (say for stacking)
// Adafruit_MotorShield AFMS = Adafruit_MotorShield(0x61); 

// Connect a stepper motor with 200 steps per revolution (1.8 degree)
// to motor port #2 (M3 and M4)
Adafruit_StepperMotor *myMotor = AFMS.getStepper(200, 2);

int incomingByte = 0;
int reads[15];
int counter = 0;
int setspeed = 0;
int setstep = 0;

/* [0] first one is M for motor
 * [1:3] setspeed 3 digit ###
 * [4:8] step 5 digit #####
 * [9] direction [1,2] -> [FORWARD, BACKWARD]
 * [10] steptype [1, 2, 3, 4] -> [SINGLE, DOUBLE, INTERLEAVE, MICROSTEP]
 * 
 * void old() {
  //Serial.println("Single coil steps");
  //myMotor->step(100, FORWARD, SINGLE); 
  //myMotor->step(100, BACKWARD, SINGLE); 

  Serial.println("Backward Double coil steps");
  //myMotor->step(100, FORWARD, DOUBLE); 
  myMotor->step(20000, BACKWARD, DOUBLE);
  
  //Serial.println("Interleave coil steps");
  //myMotor->step(100, FORWARD, INTERLEAVE); 
  //myMotor->step(100, BACKWARD, INTERLEAVE); 
  
  //Serial.println("Microstep steps");
  //myMotor->step(50, FORWARD, MICROSTEP); 
  //myMotor->step(50, BACKWARD, MICROSTEP);
}
 * 
 * 
 */

void setup() {
  Serial.begin(9600);           // set up Serial library at 9600 bps
  Serial.println("Stepper test successful!");

  AFMS.begin();  // create with the default frequency 1.6KHz
  //AFMS.begin(1000);  // OR with a different frequency, say 1KHz  
}

void loop(){
  if (Serial.available() > 5) {
    Serial.println("serial");
    while (Serial.available() > 0) {
      incomingByte = Serial.read();
      Serial.println(incomingByte);

      //if incomingByte is a number, treat like a number
      if (incomingByte >= 48 && incomingByte < 59) {
        reads[counter] = incomingByte - 48; //yay ascii -> char(i)-48 = i 
        Serial.println(reads[counter]);
        counter++;
      } else {
        reads[counter] = incomingByte;
        Serial.println(reads[counter]);
        //Serial.print(reads[counter]);
        counter++;
        }
    }

  counter = 0;
  //logic!

//if (char(reads[0])== 'M') { //make sure we're running a motor 
    
    int setspeed = 100*reads[1] + 10*reads[2] + reads[3];
    Serial.println("reading setspeed: ");
    Serial.println(setspeed);
    int setstep = 10000*reads[4] + 1000*reads[5] + 100*reads[6] + 10*reads[7] + reads[8];
    Serial.println("reading setsteps: ");
    Serial.println(setstep);

    
    for (int i = 0; i < 15; i++){
      Serial.println(reads[i]);
    }

    
    int dir = reads[9];
    Serial.println("reading dir: ");
    Serial.println(dir);
    
    //direction [1, 2] -> [FORWARD, BACKWARD]
    switch (dir){ //its weird like that. forward and backward are switched.
      case 1:
        dir = BACKWARD;
        Serial.println("forward");
        break;
      case 2:
        dir = FORWARD;
        Serial.println("backward");
        break;
      default:
        dir = BACKWARD;
        Serial.println("defaults forward");
    }

    myMotor->setSpeed(setspeed);  //rpm
    myMotor->step(setstep, dir, DOUBLE);
    Serial.println("running");
     
  //} else { 
    //Serial.println("not running motor");
    //}
    
  } //close if serial available

  delay(1000);
  
} //close loop


