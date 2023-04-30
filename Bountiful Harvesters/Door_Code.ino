#include <Servo.h>

Servo myservo;
const int triggerPin = 8;
const int echoPin = A0;
const int ledPin = 5;
const int servoPin = 6;

long readUltrasonicDistance(int triggerPin, int echoPin) {
  digitalWrite(triggerPin, LOW);
  delayMicroseconds(2);
  digitalWrite(triggerPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(triggerPin, LOW);
  long duration = pulseIn(echoPin, HIGH);
  long distance = duration * 0.034 / 2;
  return distance;
}

void setup() {
  Serial.begin(9600);
  myservo.attach(servoPin);
  pinMode(ledPin, OUTPUT);
}

void loop() {
  long distance = readUltrasonicDistance(triggerPin, echoPin);
  Serial.println(distance);
  if (distance <= 7) {
    digitalWrite(ledPin, HIGH);
    myservo.write(90);
    delay(2);
  }
  else {
    myservo.write(0);
    digitalWrite(ledPin, LOW);
  }
  delay(10);
}
