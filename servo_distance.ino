#include <Servo.h>

const int trigPin = 9, echoPin = 10;
Servo myServo;
unsigned long last = 0;

void setup() {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  myServo.attach(6);
  Serial.begin(9600);
  Serial.setTimeout(20);
}

void loop() {
  if (millis() - last > 100) {
    digitalWrite(trigPin, LOW); delayMicroseconds(2);
    digitalWrite(trigPin, HIGH); delayMicroseconds(10);
    digitalWrite(trigPin, LOW);
    long t = pulseIn(echoPin, HIGH, 30000);
    Serial.println(t * 0.034 / 2);   // distance in cm
    last = millis();
  }
  if (Serial.available()) {
    String s = Serial.readStringUntil('\n');
    s.trim();
    if (s.length() > 0) {
      int a = s.toInt();
      if (a >= 0 && a <= 180)
        myServo.write(a);
    }
  }
}
