#include <Servo.h>
const int servo_water = 3;
const int servo_bottom = 5;
const int servo_top = 9;
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
  servo_ein.attach(servo_top); 
  servo_zwei.attach(servo_bottom);
  servo_dwei.attach(servo_top);
}

void loop() {
  long data = 0.01723 * readUltrasonicDistance(triggerPin, echoPin);
for(int pos1 = 90; pos1 >= 0; pos1--){
  servo_zwei.write(pos1);
  delay(100);
}
delay(100);
for(int pos2 = 0; pos2 <= 45; pos2++){
  servo_dwei.write(pos2);
  delay(100);
delay(100);
for(int pos1 = 0; pos1 <= 160; pos1++){
  servo_zwei.write(pos1);
  delay(100);
}
delay(100);
for(int pos2 = 45; pos2 >= 0; pos2--){
  servo_dwei.write(pos2);
  delay(100);
}
delay(100);
for(int pos1 = 90; pos1 >= 0; pos1--){
  servo_zwei.write(pos1);
  delay(100);
}
delay(100);
for(int pos3 = 0; pos3 <= 180; pos2++){
  servo_ein.write(pos3);
  delay(100);
}
delay(2000);
for(int pos3 = 180; pos3 >= 0; pos3--){
  servo_ein.write(pos3);
  delay(100);
}
delay(15000);
}
