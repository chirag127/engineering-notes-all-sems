# Flash an LED at a given on time and off time cycle, where the two times are taken from a file.

- To flash an LED at a given on time and off time cycle, we need to use a microcontroller, an LED, a resistor, a breadboard, some wires, and a file that contains the on time and off time values in milliseconds.
- The microcontroller is a device that can execute a program and control the output of a pin. We can use any microcontroller that supports digital output, such as Arduino, Raspberry Pi, or ESP32.
- The LED is a light-emitting diode that can turn on or off when a voltage is applied to its terminals. We need to connect the LED to a resistor and a pin of the microcontroller. The resistor limits the current that flows through the LED and prevents it from burning out.
- The breadboard is a board that allows us to make temporary connections between components without soldering. We can use the breadboard to connect the microcontroller, the LED, the resistor, and the wires.
- The wires are used to connect the components on the breadboard. We need to use different colors of wires to distinguish the positive and negative terminals of the LED and the microcontroller.
- The file is a text file that contains two numbers separated by a comma. The first number is the on time and the second number is the off time of the LED in milliseconds. For example, if the file contains 500,1000, it means the LED should be on for 500 milliseconds and off for 1000 milliseconds. We need to store the file in the same folder as the program that we will write for the microcontroller.

The steps to flash an LED at a given on time and off time cycle are:

- Connect the microcontroller to the computer using a USB cable.
- Open the IDE (integrated development environment) that is compatible with the microcontroller. For example, if we use Arduino, we can use the Arduino IDE.
- Write a program that reads the file, extracts the on time and off time values, and sets the pin of the microcontroller to high or low accordingly. For example, if we use Arduino, we can write a program like this:

```c
// Define the pin number that is connected to the LED
#define LED_PIN 13

// Define the file name that contains the on time and off time values
#define FILE_NAME "times.txt"

// Declare two variables to store the on time and off time values
int onTime;
int offTime;

// Declare a variable to store the file object
File file;

void setup() {
  // Initialize the serial communication
  Serial.begin(9600);

  // Initialize the LED pin as an output
  pinMode(LED_PIN, OUTPUT);

  // Initialize the SD card module
  if (!SD.begin()) {
    // If the SD card is not detected, print an error message and stop the program
    Serial.println("SD card initialization failed!");
    while (true);
  }

  // Open the file in read mode
  file = SD.open(FILE_NAME, FILE_READ);

  // If the file is opened successfully, read the first line and parse the on time and off time values
  if (file) {
    // Read the first line of the file as a string
    String line = file.readStringUntil('\n');

    // Split the string by the comma and convert the substrings to integers
    onTime = line.substring(0, line.indexOf(',')).toInt();
    offTime = line.substring(line.indexOf(',') + 1).toInt();

    // Print the on time and off time values to the serial monitor
    Serial.print("On time: ");
    Serial.println(onTime);
    Serial.print("Off time: ");
    Serial.println(offTime);

    // Close the file
    file.close();
  } else {
    // If the file is not opened successfully, print an error message and stop the program
    Serial.println("File opening failed!");
    while (true);
  }
}

void loop() {
  // Turn on the LED for the on time duration
  digitalWrite(LED_PIN, HIGH);
  delay(onTime);

  // Turn off the LED for the off time duration
  digitalWrite(LED_PIN, LOW);
  delay(offTime);
}
```

- Upload the program to the microcontroller and verify that it works as expected. The LED should flash at the given on time and off time cycle. We can change the values in the file and upload the program again to see the effect.