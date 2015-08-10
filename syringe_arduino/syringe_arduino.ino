#include <Wire.h>
#include <Adafruit_MotorShield.h>
#include "utility/Adafruit_PWMServoDriver.h"

// Create the motor shield object with the default I2C address
Adafruit_MotorShield AFMS = Adafruit_MotorShield(); 

// Connect a stepper motor with 200 steps per revolution (1.8 degree)
// to motor port #2 (M3 and M4)
Adafruit_StepperMotor *myMotor = AFMS.getStepper(200, 2);

int incomingByte = 0;
int reads[10];
int counter = 0;
int setspeed = 0;
int setstep = 0;

/* 8-digit string passed from serialport
 *  
 * [0:3] setspeed 3 digit ###
 * [3:8] step 5 digit #####
 * [8] direction [1,2] -> [FORWARD, BACKWARD]
 * 
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
    
    int setspeed = 100*reads[0] + 10*reads[1] + reads[2];
    Serial.println("reading setspeed: ");
    Serial.println(setspeed);
    int setstep = 10000*reads[3] + 1000*reads[4] + 100*reads[5] + 10*reads[6] + reads[7];
    Serial.println("reading setsteps: ");
    Serial.println(setstep);
  
    for (int i = 0; i < 10; i++){
      Serial.println(reads[i]);
    }

    int dir = reads[8];
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

    myMotor->setSpeed(setspeed*4/3);  //rpm conversion
    myMotor->step(setstep, dir, DOUBLE);
    Serial.println("running");
    
  } //close if serial available

  delay(1000);
  
} //close loop


