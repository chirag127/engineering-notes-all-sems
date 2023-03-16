# Flash an LED at a given on time and off time cycle, where the two times are taken from a file.

- To flash an LED at a given on time and off time cycle, we need to use a microcontroller, an LED, a resistor, a breadboard, some wires, and a file that contains the on time and off time values in milliseconds.
- The microcontroller is a device that can execute a program that controls the output pins. We can use any microcontroller that supports digital output, such as Arduino, Raspberry Pi, or ESP32.
- The LED is a light-emitting diode that can turn on or off depending on the voltage applied to its terminals. We need to connect the LED to one of the output pins of the microcontroller through a resistor, which limits the current and protects the LED from burning out.
- The breadboard is a board that allows us to make temporary connections between components without soldering. We can use the breadboard to connect the microcontroller, the LED, the resistor, and the wires.
- The wires are used to connect the components on the breadboard. We need to use different colors of wires to distinguish the positive and negative terminals of the LED and the microcontroller.
- The file is a text file that contains two numbers separated by a comma, which represent the on time and off time of the LED in milliseconds. For example, the file could contain "500, 1000", which means the LED should be on for 500 milliseconds and off for 1000 milliseconds. We need to store the file in the same folder as the program that we will write for the microcontroller.
- The program is a set of instructions that tells the microcontroller what to do. We need to write the program in a language that the microcontroller can understand, such as C, Python, or Arduino. The program should do the following steps:

  - Initialize the output pin that is connected to the LED and set it to low (off) state.
  - Open the file that contains the on time and off time values and read them into two variables.
  - Start a loop that repeats indefinitely.
  - Set the output pin to high (on) state and wait for the on time duration.
  - Set the output pin to low (off) state and wait for the off time duration.
  - End the loop.

- The following is an example of the program written in Arduino language, which is based on C. The program assumes that the LED is connected to pin 13, and the file is named "times.txt".

```c
// Define the output pin
#define LED_PIN 13

// Define the file name
#define FILE_NAME "times.txt"

// Declare the variables for on time and off time
int onTime;
int offTime;

// Declare the file object
File file;

void setup() {
  // Initialize the output pin and set it to low
  pinMode(LED_PIN, OUTPUT);
  digitalWrite(LED_PIN, LOW);

  // Initialize the serial communication
  Serial.begin(9600);

  // Initialize the SD card
  if (!SD.begin()) {
    // If the SD card is not detected, print an error message and stop the program
    Serial.println("SD card initialization failed");
    while (true);
  }

  // Open the file
  file = SD.open(FILE_NAME);

  // If the file is not found, print an error message and stop the program
  if (!file) {
    Serial.println("File not found");
    while (true);
  }

  // Read the on time and off time values from the file
  onTime = file.parseInt();
  offTime = file.parseInt();

  // Close the file
  file.close();

  // Print the on time and off time values
  Serial.print("On time: ");
  Serial.println(onTime);
  Serial.print("Off time: ");
  Serial.println(offTime);
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