#### c) Flash an LED at a given on time and off time cycle, where the two times are taken from a file.

- To flash an LED at a given on time and off time cycle, we need to use a microcontroller, an LED, a resistor, a breadboard, and some jumper wires.
- We also need to create a text file that contains two numbers, representing the on time and off time in milliseconds, separated by a comma. For example, the file could contain `500,1000` to flash the LED for 500 ms and turn it off for 1000 ms.
- We need to write a program for the microcontroller that can read the file from a storage device, such as a USB flash drive or a micro SD card, and store the on time and off time values in two variables.
- We also need to configure one of the digital pins of the microcontroller as an output and connect it to the LED through a resistor. The resistor is used to limit the current and protect the LED from burning out.
- The program should then use a loop to repeatedly turn the LED on and off, using the `digitalWrite` function and the `delay` function. The `digitalWrite` function takes two arguments: the pin number and the state (HIGH or LOW). The `delay` function takes one argument: the time in milliseconds to wait.
- The pseudocode for the program could look something like this:

```
// Define the pin number for the LED
#define LED_PIN 13

// Declare two variables for the on time and off time
int onTime;
int offTime;

// Initialize the serial communication
Serial.begin(9600);

// Initialize the LED pin as an output
pinMode(LED_PIN, OUTPUT);

// Open the file from the storage device
File file = SD.open("times.txt");

// Check if the file exists and can be read
if (file) {
  // Read the first number from the file and store it in onTime
  onTime = file.parseInt();
  
  // Read the second number from the file and store it in offTime
  offTime = file.parseInt();
  
  // Close the file
  file.close();
  
  // Print the on time and off time values to the serial monitor
  Serial.print("On time: ");
  Serial.println(onTime);
  Serial.print("Off time: ");
  Serial.println(offTime);
}
else {
  // Print an error message to the serial monitor
  Serial.println("Error opening file");
}

// Start the loop
while (true) {
  // Turn the LED on
  digitalWrite(LED_PIN, HIGH);
  
  // Wait for the on time
  delay(onTime);
  
  // Turn the LED off
  digitalWrite(LED_PIN, LOW);
  
  // Wait for the off time
  delay(offTime);
}
```