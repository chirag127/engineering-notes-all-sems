#### c) Flash an LED at a given on time and off time cycle, where the two times are taken from a file.

- To flash an LED at a given on time and off time cycle, we need to use a microcontroller, an LED, a resistor, a breadboard, and some jumper wires.
- We also need to create a text file that contains the on time and off time values in milliseconds, separated by a comma. For example, the file could look like this:

```
1000,500
```

- This means that the LED will be on for 1000 ms and off for 500 ms, repeatedly.
- We need to upload the file to the microcontroller's memory, using a serial communication protocol such as UART, SPI, or I2C.
- We also need to write a program for the microcontroller that reads the file, parses the values, and controls the LED accordingly.
- The program could look something like this in pseudocode:

```
// Define the LED pin and the file name
const int LED_PIN = 13;
const char FILE_NAME[] = "times.txt";

// Declare variables to store the on time and off time
int on_time;
int off_time;

// Initialize the LED pin as output and the serial port as input
void setup() {
  pinMode(LED_PIN, OUTPUT);
  Serial.begin(9600);
}

// Read the file, parse the values, and flash the LED
void loop() {
  // Check if the file exists and can be opened
  if (File.exists(FILE_NAME)) {
    File file = File.open(FILE_NAME, READ);
    if (file) {
      // Read the first line of the file
      String line = file.readLine();
      // Split the line by the comma
      String[] values = line.split(",");
      // Convert the values to integers
      on_time = int(values[0]);
      off_time = int(values[1]);
      // Close the file
      file.close();
    }
  }
  // Flash the LED with the given on time and off time
  digitalWrite(LED_PIN, HIGH);
  delay(on_time);
  digitalWrite(LED_PIN, LOW);
  delay(off_time);
}
```

- This program assumes that the file name is "times.txt" and that the LED is connected to pin 13 of the microcontroller. These values can be changed according to the actual setup.
- The program also assumes that the serial port is set to 9600 baud rate and that the file is uploaded using the same port. These values can also be changed according to the actual configuration.