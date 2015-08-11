#include <Wire.h>
#include <Adafruit_MotorShield.h>
#include "utility/Adafruit_PWMServoDriver.h"

// Create the motor shield object with the default I2C address
Adafruit_MotorShield AFMS = Adafruit_MotorShield(); 
// Connect a stepper motor with 200 steps per revolution (1.8 degree)
// to motor port #2 (M3 and M4) - motor port #1 (M1 and M2)
Adafruit_StepperMotor *myMotor = AFMS.getStepper(200, 2);


void setup() {
  // set up Serial library at 9600 bps
  Serial.begin(9600);
  
  Serial.println("Stepper test!");
  
  // create with the default frequency 1.6KHz
  AFMS.begin();  
  // OR with a different frequency, say 1KHz
  //AFMS.begin(1000); 
  
  // Sets the rpm speed of the motor. Currently set to 60 rpm
  myMotor->setSpeed(60);  
}

void loop() {
  //The BACKWARD direction pushes liquid out of the syringe pump
  //The FORWARD direction pulls liquid into the syringe pump
  //Please keep the step type at DOUBLE
  //The first number is the number of steps that the stepper motor
  //will take 
  Serial.println("Backward/Forward Double coil steps");
  //myMotor->step((800*(#ofmL)), FORWARD, DOUBLE); 
  myMotor->step((800*(#ofmL)), BACKWARD, DOUBLE);
  
  //Stops the syringe pump for a minute so that you can think
  //about inputting a new command. 
  delay(60000);
}
