# Flash an LED at a given on time and off time cycle, where the two times are taken from a file.

- To flash an LED at a given on time and off time cycle, we need to use a microcontroller, an LED, a resistor, a breadboard, some wires, and a file that contains the on time and off time values in milliseconds.
- The microcontroller is a device that can execute a program and control the output of a pin. We can use any microcontroller that supports digital output, such as Arduino, Raspberry Pi, or ESP32.
- The LED is a light-emitting diode that can turn on and off when a voltage is applied across its terminals. We need to connect one terminal of the LED to a digital output pin of the microcontroller, and the other terminal to a resistor and then to the ground. The resistor limits the current that flows through the LED and prevents it from burning out.
- The breadboard is a board that allows us to connect components without soldering. We can use it to make the connections between the microcontroller, the LED, the resistor, and the wires.
- The wires are used to connect the components on the breadboard. We need to use different colors of wires to distinguish the connections. For example, we can use red wires for power, black wires for ground, and green wires for data.
- The file is a text file that contains two numbers separated by a comma. The first number is the on time of the LED in milliseconds, and the second number is the off time of the LED in milliseconds. For example, the file could contain `1000,500` which means the LED will be on for 1 second and off for 0.5 second. We need to store the file in the same folder as the program that we will write for the microcontroller.
- The program is a set of instructions that tells the microcontroller what to do. We need to write the program in a language that the microcontroller can understand, such as C, Python, or Arduino. The program should do the following steps:
  - Initialize the digital output pin that is connected to the LED and set it to low (off).
  - Open the file that contains the on time and off time values and read them into two variables.
  - Start a loop that repeats indefinitely.
  - Set the digital output pin to high (on) and wait for the on time duration.
  - Set the digital output pin to low (off) and wait for the off time duration.
  - End the loop and go back to the beginning.
- The following is an example of the program written in Arduino language:

```c
// Define the pin number that is connected to the LED
#define LED_PIN 13

// Define the file name that contains the on time and off time values
#define FILE_NAME "times.txt"

// Declare two variables to store the on time and off time values
int onTime;
int offTime;

void setup() {
  // Initialize the LED pin as an output and set it to low
  pinMode(LED_PIN, OUTPUT);
  digitalWrite(LED_PIN, LOW);

  // Open the file and read the on time and off time values
  File file = SD.open(FILE_NAME);
  if (file) {
    // Read the first number until the comma and convert it to an integer
    String onTimeString = file.readStringUntil(',');
    onTime = onTimeString.toInt();

    // Read the second number until the end of the file and convert it to an integer
    String offTimeString = file.readString();
    offTime = offTimeString.toInt();

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
  // Turn on the LED and wait for the on time duration
  digitalWrite(LED_PIN, HIGH);
  delay(onTime);

  // Turn off the LED and wait for the off time duration
  digitalWrite(LED_PIN, LOW);
  delay(offTime);
}
```