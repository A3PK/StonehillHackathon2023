#include <Servo.h>

const int SERVO1_PIN = 3;
const int SERVO2_PIN = 5;
const int SERVO3_PIN = 9;

Servo servo1;
Servo servo2;
Servo servo3;

int servo2Pos = 0;
int servo3Pos = 0;
int servo1Pos = 0;

void setup() {
  servo1.attach(SERVO1_PIN);
  servo2.attach(SERVO2_PIN);
  servo3.attach(SERVO3_PIN);
  Serial.begin(9600);
}

void loop() {
  // Move servo2 to 180 degrees, then move servo3 to 45 degrees
  for (servo2Pos = 0; servo2Pos >= -180; servo2Pos -= 1) {
    servo2.write(servo2Pos);
    delay(15);
  }
  for (servo3Pos = 0; servo3Pos >= -45; servo3Pos -= 1) {
    servo3.write(servo3Pos);
    delay(15);
  }
delay(1000);
  // Move servo3 to 0 degrees, then move servo2 to 180 degrees
  for (servo3Pos = -45; servo3Pos <= 0; servo3Pos += 1) {
    servo3.write(servo3Pos);
    delay(15);
  }
  delay(5000);
  for (servo2Pos = -180; servo2Pos <= 0; servo2Pos += 1) {
    servo2.write(servo2Pos);
    delay(15);
  }

  // Move servo1 to 180 degrees, then move it back to 0 degrees
  for (servo1Pos = 0; servo1Pos <= 180; servo1Pos += 1) {
    servo1.write(servo1Pos);
    delay(15);
  }
  delay(5000);
  for (servo1Pos = 180; servo1Pos >= 0; servo1Pos -= 1) {
    servo1.write(servo1Pos);
    delay(15);
  }

  // Move servo3 to 180 degrees, then move servo2 to 45 degrees
  for (servo3Pos = 0; servo3Pos >= 180; servo3Pos -= 1) {
    servo3.write(servo3Pos);
    delay(15);
  }
  for (servo2Pos = 0; servo2Pos >= 45; servo2Pos -= 1) {
    servo2.write(servo2Pos);
    delay(15);
  }
  delay(5000);

  // Move servo2 to 0 degrees, then move servo3 to 180 degrees
  for (servo2Pos = 45; servo2Pos >= 0; servo2Pos -= 1) {
    servo2.write(servo2Pos);
    delay(15);
  }
  delay(5000);
  for (servo3Pos = 180; servo3Pos >= 0; servo3Pos -= 1) {
    servo3.write(servo3Pos);
    delay(15);
  }
}
