### Coding for the notes of the Unit 5 - Programming the Arduino in the subject of Internet of Things

- Arduino is a platform that consists of hardware and software for creating interactive electronic projects. Arduino boards are microcontrollers that can be programmed using the Arduino Software (IDE) or other compatible tools.
- Arduino Software (IDE) is an offline application that allows you to write code and upload it to the board. There are two versions of the IDE: 1.x.x and 2.x.x. The 2.x.x version is faster and more powerful, with advanced features for coding and debugging.
- Arduino code (also called sketch) is written in a language that is based on C/C++. It has two main parts: setup() and loop(). The setup() function runs once when the board is powered on or reset, and is used to initialize variables, pin modes, libraries, etc. The loop() function runs repeatedly and contains the main logic of the program.
- Arduino code can use functions, variables, constants, operators, control structures, and data types from the Arduino language reference. It can also use libraries to extend the functionality of the board, such as communication protocols, sensors, actuators, etc.
- Arduino code can be verified (compiled) and uploaded to the board using the toolbar buttons or the menu options in the IDE. The message area and the text console show the feedback and the errors during the process. The serial monitor can be used to communicate with the board and display data.
- Arduino code can be organized into tabs, files, and folders for better readability and modularity. It can also be commented using // or /* */ to explain the purpose and the logic of the code.
- Arduino code can be shared with others using the web editor, the sketchbook, or the codebender platform. It can also be exported as a binary file (.hex) or as a compressed folder (.zip).

Some examples of Arduino code for Internet of Things projects are:

- Blinking an LED using a button and a resistor. This example shows how to use digital input and output pins, and how to debounce a switch.

```c
// define constants for the pin numbers
const int buttonPin = 2; // the number of the pushbutton pin
const int ledPin = 13; // the number of the LED pin

// variables for the button state
int buttonState = 0; // variable for reading the pushbutton status
int lastButtonState = 0; // variable for storing the last button state
unsigned long lastDebounceTime = 0; // variable for storing the last debounce time
const unsigned long debounceDelay = 50; // the debounce time in milliseconds

// variable for the LED state
int ledState = LOW; // variable for storing the LED state

void setup() {
  // initialize the LED pin as an output
  pinMode(ledPin, OUTPUT);
  // initialize the button pin as an input with a pull-up resistor
  pinMode(buttonPin, INPUT_PULLUP);
}

void loop() {
  // read the state of the button
  int reading = digitalRead(buttonPin);

  // check if the button state has changed
  if (reading != lastButtonState) {
    // reset the debounce timer
    lastDebounceTime = millis();
  }

  // if the debounce time has passed
  if ((millis() - lastDebounceTime) > debounceDelay) {
    // if the button state has changed
    if (reading != buttonState) {
      // update the button state
      buttonState = reading;

      // if the button is pressed
      if (buttonState == LOW) {
        // toggle the LED state
        ledState = !ledState;
      }
    }
  }

  // set the LED according to the ledState
  digitalWrite(ledPin, ledState);

  // save the last button state
  lastButtonState = reading;
}
```

- Reading a temperature sensor and sending the data to a web server. This example shows how to use an analog input pin, a library for the sensor, and a library for the Ethernet shield.

```c
// include the libraries for the sensor and the Ethernet shield
#include <OneWire.h>
#include <DallasTemperature.h>
#include <SPI.h>
#include <Ethernet.h>

// define constants for the pin numbers and the server address
const int sensorPin = A0; // the number of the analog input pin for the sensor
byte mac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED