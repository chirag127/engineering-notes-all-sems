#### c) Flash an LED at a given on time and off time cycle, where the two times are taken from a file.

To flash an LED at a given on time and off time cycle, where the two times are taken from a file, the following steps are required:

- Connect an LED to a digital output pin of a microcontroller, such as Arduino, and a resistor to limit the current.
- Create a text file with two numbers separated by a comma, representing the on time and off time in milliseconds, for example: 500,1000
- Save the file in the same folder as the Arduino sketch, and name it as "times.txt".
- Use the `File` and `SD` libraries to access the file from the microcontroller's memory card.
- Use the `parseInt()` function to read the two numbers from the file and store them in variables, for example: `int onTime = file.parseInt(); int offTime = file.parseInt();`
- Use the `digitalWrite()` function to turn the LED on and off according to the on time and off time variables, for example: `digitalWrite(ledPin, HIGH); delay(onTime); digitalWrite(ledPin, LOW); delay(offTime);`
- Use a `while` loop to repeat the flashing cycle indefinitely, for example: `while (true) { // flash the LED }`

The following is an example of an Arduino sketch that implements the above steps:

```c
// include the libraries for file and SD card access
#include <File.h>
#include <SD.h>

// define the pin number for the LED
const int ledPin = 13;

// define the variables for the on time and off time
int onTime;
int offTime;

// define the file object
File file;

void setup() {
  // initialize the LED pin as an output
  pinMode(ledPin, OUTPUT);

  // initialize the serial communication for debugging
  Serial.begin(9600);

  // initialize the SD card and check if it is ready
  if (!SD.begin()) {
    Serial.println("SD card initialization failed");
    return;
  }

  // open the file and check if it exists
  file = SD.open("times.txt");
  if (!file) {
    Serial.println("File not found");
    return;
  }

  // read the on time and off time from the file
  onTime = file.parseInt();
  offTime = file.parseInt();

  // close the file
  file.close();

  // print the on time and off time for debugging
  Serial.print("On time: ");
  Serial.println(onTime);
  Serial.print("Off time: ");
  Serial.println(offTime);
}

void loop() {
  // flash the LED according to the on time and off time
  digitalWrite(ledPin, HIGH);
  delay(onTime);
  digitalWrite(ledPin, LOW);
  delay(offTime);
}
```