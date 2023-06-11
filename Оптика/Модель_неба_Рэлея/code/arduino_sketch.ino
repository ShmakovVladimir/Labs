#include <Servo.h>

Servo servo;

const uint8_t Servo_Pin = 9;

void setup() {
  servo.attach(Servo_Pin);
  servo.write(15);
  Serial.begin(9600);
}

void loop() {
  while(!Serial.available());
  servo.write(Serial.parseInt());
  Serial.println(Serial.parseInt());
}