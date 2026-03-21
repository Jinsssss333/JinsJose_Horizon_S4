#include <Servo.h>

int angle = 0;

Servo servo_9;

void setup()
{
  pinMode(A0, INPUT);
  servo_9.attach(9, 500, 2500);
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop()
{
  angle = map(analogRead(A0), 0, 1023, 0, 180);
  if (angle > 68) {
    servo_9.write(68);
    digitalWrite(LED_BUILTIN, HIGH);
  } else {
    servo_9.write(angle);
    digitalWrite(LED_BUILTIN, LOW);
  }
  delay(10); 
}