#include <Servo.h>

Servo myServo;

const int trigPin = 9;
const int echoPin = 10;
long duration;
int distance;

void setup() {
  myServo.attach(11); // Connect the servo to pin 11
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  Serial.begin(9600);
}

void loop() {
  // Send ultrasonic pulse
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  // Measure echo return time
  duration = pulseIn(echoPin, HIGH);

  // Calculate distance in cm
  distance = duration * 0.034 / 2;

  // Check if distance is less than 10 cm
  if (distance < 10) {
    myServo.write(90); // Rotate servo to 90 degrees
    Serial.println("Object detected within 10 cm, rotating servo to 90 degrees.");
  } else {
    myServo.write(0);  // Reset servo to 0 degrees
    Serial.println("No object within 10 cm, servo at 0 degrees.");
  }

  delay(500); // Delay to stabilize readings
}
