# Flash an LED at a given on time and off time cycle, where the two times are taken from a file.

- To flash an LED at a given on time and off time cycle, we need to use a microcontroller, an LED, a resistor, a breadboard, some wires, and a file that contains the on time and off time values in milliseconds.
- The microcontroller is a device that can run a program to control the output pins, which can be connected to the LED. The resistor is used to limit the current flowing through the LED and protect it from burning out. The breadboard is a platform that allows us to connect the components easily. The wires are used to make the connections between the components and the microcontroller.
- The file that contains the on time and off time values can be stored in the microcontroller's memory or on an external storage device, such as a microSD card. The file can have any name and format, as long as the program can read it and extract the values. For example, the file can be a text file with two numbers separated by a comma, such as `1000,500`, which means the LED should be on for 1000 milliseconds and off for 500 milliseconds.
- The program that runs on the microcontroller can be written in any programming language that is compatible with the microcontroller, such as C, Python, or Arduino. The program should perform the following steps:
  - Initialize the output pin that is connected to the LED and set it to low (off) state.
  - Open the file that contains the on time and off time values and read the values into two variables, such as `onTime` and `offTime`.
  - Start a loop that repeats indefinitely or until a condition is met, such as a button press or a sensor input.
  - Inside the loop, set the output pin to high (on) state and wait for `onTime` milliseconds.
  - Then, set the output pin to low (off) state and wait for `offTime` milliseconds.
  - End the loop and close the file.
- The following is an example of a program written in Arduino that flashes an LED at a given on time and off time cycle, where the two times are taken from a file named `times.txt` stored on a microSD card. The LED is connected to pin 13 and a microSD card module is connected to pins 10, 11, 12, and 4.

```c
// Include the library for the microSD card module
#include <SPI.h>
#include <SD.h>

// Define the output pin for the LED
#define LED_PIN 13

// Define the chip select pin for the microSD card module
#define CS_PIN 4

// Define the variables for the on time and off time
int onTime = 0;
int offTime = 0;

// Define the file object for the file that contains the times
File timesFile;

void setup() {
  // Initialize the output pin and set it to low
  pinMode(LED_PIN, OUTPUT);
  digitalWrite(LED_PIN, LOW);

  // Initialize the serial monitor for debugging
  Serial.begin(9600);

  // Initialize the microSD card module
  if (!SD.begin(CS_PIN)) {
    // If the initialization fails, print an error message and stop the program
    Serial.println("Card initialization failed!");
    return;
  }

  // Open the file that contains the times
  timesFile = SD.open("times.txt");

  // If the file is opened successfully, read the times into the variables
  if (timesFile) {
    // Read the first number until the comma and convert it to an integer
    onTime = timesFile.parseInt();

    // Read the second number until the end of the line and convert it to an integer
    offTime = timesFile.parseInt();

    // Print the times for debugging
    Serial.print("On time: ");
    Serial.println(onTime);
    Serial.print("Off time: ");
    Serial.println(offTime);

    // Close the file
    timesFile.close();
  }
  else {
    // If the file cannot be opened, print an error message and stop the program
    Serial.println("File not found!");
    return;
  }
}

void loop() {
  // Set the output pin to high and wait for the on time
  digitalWrite(LED_PIN, HIGH);
  delay(onTime);

  // Set the output pin to low and wait for the off time
  digitalWrite(LED_PIN, LOW);
  delay(offTime);
}
```