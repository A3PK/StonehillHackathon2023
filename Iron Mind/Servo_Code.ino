
#include <Servo.h>
const int servo1 = 3;
const int servo_first = 5;
const int servo_second = 9;
const int triggerPin = 2;
const int echoPin = A0;

Servo servo_ein;  // create servo object to control a servo
Servo servo_zwei; // create servo object to control a servo
Servo servo_dwei;
// twelve servo objects can be created on most boards

int pos1 = 0;    // variable to store the servo1 position
int pos2 = 1;    // variable to store the servo2 position
int pos3 = 2;    // variable to store the servo3 position

long readUltrasonicDistance(int triggerPin, int echoPin)
{
  pinMode(triggerPin, OUTPUT);  // Clear the trigger
  digitalWrite(triggerPin, LOW);
  delayMicroseconds(2);
  // Sets the trigger pin to HIGH state for 10 microseconds
  digitalWrite(triggerPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(triggerPin, LOW);
  pinMode(echoPin, INPUT);
  // Reads the echo pin, and returns the sound wave travel time in microseconds
  return pulseIn(echoPin, HIGH);
}
void setup() {
  servo_ein.attach(servo1); 
  servo_zwei.attach(servo_first);
  servo_vier.attach(servo_second);
}

void loop() {
  long data = 0.01723 * readUltrasonicDistance(triggerPin, echoPin);
  
  for (pos = 0; pos <= 180; pos += 1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
  delay(5000);
  for (pos = 180; pos >= 0; pos -= 1) { // goes from 180 degrees to 0 degrees
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
}
