# Flash an LED at a given on time and off time cycle, where the two times are taken from a file.

- To flash an LED at a given on time and off time cycle, we need to use a microcontroller, an LED, a resistor, a breadboard, some jumper wires, and a file that contains the on time and off time values in milliseconds.
- The microcontroller is a device that can execute a program and control the output of a pin. We can use any microcontroller that supports digital output, such as Arduino, Raspberry Pi, or ESP32.
- The LED is a light-emitting diode that can turn on and off when a voltage is applied across its terminals. We need to connect the LED to a resistor to limit the current and prevent it from burning out. The resistor value depends on the LED voltage and the microcontroller output voltage, but a common value is 220 ohms.
- The breadboard is a board that allows us to connect components without soldering. We can use the breadboard to connect the microcontroller, the LED, the resistor, and the jumper wires.
- The jumper wires are wires that can be used to make connections between the components. We need to use four jumper wires: one to connect the microcontroller ground to the breadboard ground, one to connect the microcontroller output pin to the resistor, one to connect the resistor to the LED, and one to connect the LED to the breadboard ground.
- The file is a text file that contains two numbers separated by a comma. The first number is the on time in milliseconds, and the second number is the off time in milliseconds. For example, the file could contain "500,1000" to indicate that the LED should be on for 500 milliseconds and off for 1000 milliseconds. The file should be stored in the same folder as the microcontroller program.
- The program is a set of instructions that tells the microcontroller what to do. We need to write the program in a language that the microcontroller can understand, such as C, Python, or Arduino. The program should do the following steps:
  - Initialize the output pin as digital output and set it to low.
  - Open the file and read the on time and off time values.
  - Enter a loop that repeats indefinitely.
  - Set the output pin to high and wait for the on time duration.
  - Set the output pin to low and wait for the off time duration.
  - End the loop.
- The following is an example of the program written in Arduino:

```c
// Define the output pin number
#define LED_PIN 13

// Define the file name
#define FILE_NAME "times.txt"

// Declare variables to store the on time and off time values
int onTime;
int offTime;

void setup() {
  // Initialize the output pin as digital output and set it to low
  pinMode(LED_PIN, OUTPUT);
  digitalWrite(LED_PIN, LOW);

  // Open the file and read the on time and off time values
  File file = SD.open(FILE_NAME);
  if (file) {
    // Read the first number until the comma
    String onTimeStr = file.readStringUntil(',');
    // Convert the string to integer
    onTime = onTimeStr.toInt();
    // Read the second number until the end of line
    String offTimeStr = file.readStringUntil('\n');
    // Convert the string to integer
    offTime = offTimeStr.toInt();
    // Close the file
    file.close();
  }
  else {
    // If the file cannot be opened, print an error message and stop the program
    Serial.println("Error opening file");
    while (true);
  }
}

void loop() {
  // Set the output pin to high and wait for the on time duration
  digitalWrite(LED_PIN, HIGH);
  delay(onTime);
  // Set the output pin to low and wait for the off time duration
  digitalWrite(LED_PIN, LOW);
  delay(offTime);
}
```