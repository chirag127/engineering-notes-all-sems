#### c) Flash an LED at a given on time and off time cycle, where the two times are taken from a file.

- To flash an LED at a given on time and off time cycle, we need to use a microcontroller, an LED, a resistor, a breadboard, and some jumper wires.
- We also need to create a text file that contains two numbers, representing the on time and off time in milliseconds, separated by a comma. For example, the file could have the following content: `500,1000`
- We need to connect the LED and the resistor in series between a digital output pin of the microcontroller and the ground. For example, we could use pin 13 on an Arduino board.
- We need to write a program that reads the file, parses the two numbers, and uses them to control the LED. We can use the `digitalWrite()` function to turn the LED on and off, and the `delay()` function to wait for the specified time. For example, the program could look like this:

```c
// Include the library for reading files
#include <SPI.h>
#include <SD.h>

// Define the pin for the LED
const int ledPin = 13;

// Define the file name
const char* fileName = "times.txt";

// Define variables for the on time and off time
int onTime = 0;
int offTime = 0;

void setup() {
  // Initialize the LED pin as output
  pinMode(ledPin, OUTPUT);

  // Initialize the serial monitor for debugging
  Serial.begin(9600);

  // Initialize the SD card
  if (!SD.begin(4)) {
    Serial.println("SD card initialization failed");
    return;
  }

  // Open the file
  File file = SD.open(fileName);

  // Check if the file exists
  if (file) {
    // Read the first number until the comma
    onTime = file.parseInt();

    // Skip the comma
    file.read();

    // Read the second number until the end of the file
    offTime = file.parseInt();

    // Close the file
    file.close();

    // Print the on time and off time for debugging
    Serial.print("On time: ");
    Serial.println(onTime);
    Serial.print("Off time: ");
    Serial.println(offTime);
  }
  else {
    // Print an error message if the file does not exist
    Serial.println("File not found");
  }
}

void loop() {
  // Turn the LED on
  digitalWrite(ledPin, HIGH);

  // Wait for the on time
  delay(onTime);

  // Turn the LED off
  digitalWrite(ledPin, LOW);

  // Wait for the off time
  delay(offTime);
}
```
- We need to upload the program to the microcontroller and the file to the SD card. We can use the Arduino IDE or any other software that supports the microcontroller.
- We should see the LED flashing at the given on time and off time cycle. We can change the file content to change the cycle.