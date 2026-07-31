#### c) Flash an LED at a given on time and off time cycle, where the two times are taken from a file.

- To flash an LED at a given on time and off time cycle, we need to use a microcontroller, an LED, a resistor, a breadboard, and some jumper wires.
- We also need to create a text file that contains two numbers, representing the on time and off time in milliseconds, separated by a comma. For example, the file could contain `500,1000` to flash the LED for half a second and turn it off for one second.
- We need to write a program for the microcontroller that can read the file from a storage device, such as a microSD card, and use the values to control the LED.
- The program should have the following steps:
  - Initialize the microcontroller and the storage device.
  - Define a pin for the LED and set it as an output.
  - Open the file and read the two numbers into variables.
  - Close the file and free the memory.
  - Enter an infinite loop that does the following:
    - Turn on the LED and wait for the on time.
    - Turn off the LED and wait for the off time.
- The program could be written in C, Arduino, or any other language that is compatible with the microcontroller.
- The program could look something like this in Arduino:

```c
// Define the pin for the LED
#define LED_PIN 13

// Define the file name
#define FILE_NAME "times.txt"

// Declare variables for the on time and off time
int onTime;
int offTime;

// Declare a variable for the file
File file;

void setup() {
  // Initialize the microcontroller and the storage device
  Serial.begin(9600);
  pinMode(LED_PIN, OUTPUT);
  if (!SD.begin(4)) {
    Serial.println("SD card initialization failed");
    return;
  }

  // Open the file and read the two numbers
  file = SD.open(FILE_NAME);
  if (file) {
    // Read the first number until the comma
    String onTimeString = file.readStringUntil(',');
    // Convert the string to an integer
    onTime = onTimeString.toInt();
    // Read the second number until the end of the line
    String offTimeString = file.readStringUntil('\n');
    // Convert the string to an integer
    offTime = offTimeString.toInt();
    // Close the file and free the memory
    file.close();
  } else {
    // If the file does not exist, print an error message
    Serial.println("File not found");
    return;
  }
}

void loop() {
  // Turn on the LED and wait for the on time
  digitalWrite(LED_PIN, HIGH);
  delay(onTime);
  // Turn off the LED and wait for the off time
  digitalWrite(LED_PIN, LOW);
  delay(offTime);
}
```