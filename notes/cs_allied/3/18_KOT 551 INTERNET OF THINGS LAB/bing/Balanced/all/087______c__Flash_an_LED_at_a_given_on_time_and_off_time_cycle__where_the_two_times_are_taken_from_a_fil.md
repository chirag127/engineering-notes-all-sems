#### c) Flash an LED at a given on time and off time cycle, where the two times are taken from a file.

- To flash an LED at a given on time and off time cycle, we need to use a microcontroller, an LED, a resistor, a breadboard, and some jumper wires.
- We also need to create a text file that contains the on time and off time values in milliseconds, separated by a comma. For example, the file could look like this:

```
500,1000
```

- This means that the LED will be on for 500 ms and off for 1000 ms in each cycle.
- We need to upload the file to the microcontroller's memory using a serial communication protocol, such as UART, SPI, or I2C.
- We need to write a program for the microcontroller that can read the file from the memory, parse the on time and off time values, and use them to control the LED's state using a digital output pin.
- The program could look something like this in pseudocode:

```
// Define the LED pin and the file name
const LED_PIN = 13;
const FILE_NAME = "times.txt";

// Declare variables to store the on time and off time values
int on_time;
int off_time;

// Initialize the LED pin as output
pinMode(LED_PIN, OUTPUT);

// Open the file from the memory
File file = open(FILE_NAME);

// Read the first line from the file
String line = file.readLine();

// Close the file
file.close();

// Split the line by comma and convert the values to integers
String[] values = line.split(",");
on_time = int(values[0]);
off_time = int(values[1]);

// Start an infinite loop
while (true) {
  // Turn on the LED
  digitalWrite(LED_PIN, HIGH);

  // Wait for the on time
  delay(on_time);

  // Turn off the LED
  digitalWrite(LED_PIN, LOW);

  // Wait for the off time
  delay(off_time);
}
```

- The program will run indefinitely until the microcontroller is reset or powered off.