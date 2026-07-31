#### c) Flash an LED at a given on time and off time cycle, where the two times are taken from a file.

- To flash an LED at a given on time and off time cycle, we need to use a microcontroller, an LED, a resistor, a breadboard, and some jumper wires.
- We also need to create a text file that contains two numbers, representing the on time and off time in milliseconds, separated by a comma. For example, the file could contain `500,1000` to flash the LED for 500 ms and turn it off for 1000 ms.
- We need to connect the LED and the resistor in series between a digital output pin of the microcontroller and the ground. The resistor is used to limit the current and protect the LED from burning out.
- We need to write a program for the microcontroller that can read the file from a storage device, such as a microSD card or a USB flash drive, and parse the two numbers as integers.
- We need to use a loop to toggle the output pin according to the on time and off time values, using a delay function to wait for the specified duration. For example, in Arduino, we can use the `digitalWrite`, `delay`, and `Serial` functions to achieve this.
- The pseudocode for the program could look something like this:

```
// Define the output pin number
#define LED_PIN 13

// Define the file name
#define FILE_NAME "times.txt"

// Declare variables to store the on time and off time
int onTime;
int offTime;

// Setup function, runs once at the start
void setup() {
  // Initialize the output pin as output
  pinMode(LED_PIN, OUTPUT);

  // Initialize the serial communication
  Serial.begin(9600);

  // Open the file for reading
  File file = SD.open(FILE_NAME);

  // Check if the file exists and can be opened
  if (file) {
    // Read the first number until the comma
    onTime = file.parseInt();

    // Read the second number until the end of line
    offTime = file.parseInt();

    // Close the file
    file.close();

    // Print the on time and off time to the serial monitor
    Serial.print("On time: ");
    Serial.println(onTime);
    Serial.print("Off time: ");
    Serial.println(offTime);
  }
  else {
    // Print an error message if the file cannot be opened
    Serial.println("Error opening file");
  }
}

// Loop function, runs repeatedly
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