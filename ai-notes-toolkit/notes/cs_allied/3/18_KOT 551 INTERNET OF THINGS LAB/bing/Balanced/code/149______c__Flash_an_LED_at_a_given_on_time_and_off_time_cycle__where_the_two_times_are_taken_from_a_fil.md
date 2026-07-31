#### c) Flash an LED at a given on time and off time cycle, where the two times are taken from a file.

- To flash an LED at a given on time and off time cycle, we need to use a microcontroller, an LED, a resistor, a breadboard, and some jumper wires.
- We also need to create a text file that contains the on time and off time values in milliseconds, separated by a comma. For example, the file could look like this:

```
1000,500
```

- This means that the LED will be on for 1000 ms and off for 500 ms in each cycle.
- We need to connect the LED and the resistor in series between a digital output pin of the microcontroller and the ground. For example, we could use pin 13 of an Arduino Uno board.
- We need to write a program that can read the file from the microcontroller's memory or an external storage device, such as an SD card, and store the on time and off time values in two variables.
- We also need to use a function that can control the digital output pin and set it to high or low, such as digitalWrite() in Arduino.
- We need to use a loop that can repeat the following steps:
  - Set the output pin to high and turn on the LED.
  - Use a function that can delay the execution for a given number of milliseconds, such as delay() in Arduino, and pass the on time variable as the argument.
  - Set the output pin to low and turn off the LED.
  - Use the delay() function again and pass the off time variable as the argument.
- The loop will run indefinitely until the microcontroller is reset or powered off.
- The pseudocode for the program could look like this:

```
// Define the output pin number
#define LED_PIN 13

// Declare the on time and off time variables
int onTime;
int offTime;

// Setup the output pin mode
void setup() {
  pinMode(LED_PIN, OUTPUT);
  // Read the file and store the values in the variables
  // This part depends on the file format and the storage device
  // For example, using an SD card and a file named "times.txt"
  // We need to include the SD library and initialize the card
  #include <SD.h>
  if (!SD.begin(4)) {
    // If the card fails, stop the program
    return;
  }
  // Open the file for reading
  File file = SD.open("times.txt");
  if (file) {
    // Read the first line of the file
    String line = file.readStringUntil('\n');
    // Split the line by the comma
    int commaIndex = line.indexOf(',');
    // Convert the substrings to integers
    onTime = line.substring(0, commaIndex).toInt();
    offTime = line.substring(commaIndex + 1).toInt();
    // Close the file
    file.close();
  }
}

// Loop the flashing cycle
void loop() {
  // Turn on the LED
  digitalWrite(LED_PIN, HIGH);
  // Wait for the on time
  delay(onTime);
  // Turn off the LED
  digitalWrite(LED_PIN, LOW);
  // Wait for the off time
  delay(offTime);
}
```