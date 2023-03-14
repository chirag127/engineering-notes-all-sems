## Unit 5 - Programming the Arduino

- Arduino is a platform that consists of hardware and software tools for creating interactive electronic projects.
- Arduino boards are microcontrollers that can be programmed using the Arduino programming language and the Arduino IDE (Integrated Development Environment).
- Arduino programming language is based on C/C++ and has some special features and functions that make it easy to work with sensors, actuators, serial communication, and other components.
- Arduino programs are called sketches and consist of two main parts: the setup() function and the loop() function.
- The setup() function runs once when the Arduino board is powered on or reset. It is used to initialize variables, pin modes, libraries, and other settings.
- The loop() function runs repeatedly after the setup() function. It is used to perform the main logic of the sketch, such as reading inputs, controlling outputs, and communicating with other devices.
- Arduino sketches can also use other functions, variables, constants, data types, operators, control structures, and libraries to create more complex and modular code.
- Arduino sketches can be uploaded to the Arduino board using a USB cable and the Arduino IDE. The IDE also provides tools for editing, compiling, debugging, and serial monitoring.
- Arduino sketches can also be run on a simulator, such as Tinkercad, to test the code and the circuit without the need for physical hardware.

Some examples of Arduino sketches are:

- Blink: This sketch turns an LED on and off every second. It demonstrates the use of digital output and the delay() function.

```c
// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED_BUILTIN, OUTPUT);
}

// the loop function runs over and over again forever
void loop() {
  digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(1000);                       // wait for a second
  digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
  delay(1000);                       // wait for a second
}
```

- AnalogReadSerial: This sketch reads an analog input pin, maps the result to a range from 0 to 255, and then uses that data to dim or brighten an LED. It also prints the analog value to the serial monitor. It demonstrates the use of analog input, analog output, map() function, and serial communication.

```c
// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
}

// the loop routine runs over and over again forever:
void loop() {
  // read the input on analog pin 0:
  int sensorValue = analogRead(A0);
  // print out the value you read:
  Serial.println(sensorValue);
  // map the sensor value to a range from 0 to 255:
  int outputValue = map(sensorValue, 0, 1023, 0, 255);
  // change the analog output (dimming the LED):
  analogWrite(9, outputValue);
  // wait 10 milliseconds before the next loop
  // for the analog-to-digital converter to settle
  // after the last reading:
  delay(10);
}
```

- ToneMelody: This sketch plays a melody with a piezo speaker. It demonstrates the use of arrays, for loops, and the tone() function.

```c
#include "pitches.h"

// notes in the melody:
int melody[] = {
  NOTE_C4, NOTE_G3, NOTE_G3, NOTE_A3, NOTE_G3, 0, NOTE_B3, NOTE_C4
};

// note durations: 4 = quarter note, 8 = eighth note, etc.:
int noteDurations[] = {
  4, 8, 8, 4, 4, 4, 4, 4
};

void setup() {
  // iterate over the notes of the melody:
  for (int thisNote = 0; thisNote < 8; thisNote++) {

    // to calculate the note duration, take one second
    // divided by the note type.
    //e.g. quarter note = 1000 / 4, eighth note = 1000/8, etc.
    int noteDuration = 1000 / noteDurations[thisNote];
    tone(8, melody[thisNote], noteDuration);

    // to distinguish the