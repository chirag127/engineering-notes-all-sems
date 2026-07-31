# Unit 5 - Programming the Arduino

### Introduction to coding for the Arduino

1. The Arduino is an open-source electronics platform based on easy-to-use hardware and software.
2. The Arduino Integrated Development Environment (IDE) is the software used to write and upload code to the Arduino board.
3. The Arduino programming language is based on C/C++ and includes many built-in functions and libraries for common tasks.
4. The basic structure of an Arduino program includes two main functions: `setup()` and `loop()`.
5. The `setup()` function is called once when the program starts and is used to initialize variables, pin modes, and other libraries.
6. The `loop()` function is called repeatedly and contains the main code that controls the behavior of the Arduino.
7. Digital and analog input/output (I/O) functions are used to read data from sensors and control actuators.
8. Serial communication functions are used to send and receive data between the Arduino and a computer or other devices.

### Examples of coding for the Arduino

- Blinking an LED: This is a simple example that demonstrates how to control a digital output pin on the Arduino. The code sets the pin as an output, then turns the LED on and off with a delay in between.

```c
void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  digitalWrite(LED_BUILTIN, HIGH);
  delay(1000);
  digitalWrite(LED_BUILTIN, LOW);
  delay(1000);
}
```

- Reading a potentiometer: This example demonstrates how to read an analog input on the Arduino. The code reads the value of the potentiometer, maps it to a range of 0 to 255, and then uses that value to control the brightness of an LED.

```c
int potPin = A0;
int ledPin = 9;

void setup() {
  pinMode(ledPin, OUTPUT);
}

void loop() {
  int potValue = analogRead(potPin);
  int brightness = map(potValue, 0, 1023, 0, 255);
  analogWrite(ledPin, brightness);
}
```

These are just a few examples of the many possibilities for programming the Arduino in the context of the Internet of Things. With its easy-to-use hardware and software, the Arduino provides a powerful platform for developing IoT projects and applications.