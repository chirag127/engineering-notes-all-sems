# Flash an LED at a given on time and off time cycle, where the two times are taken from a file.

- To flash an LED at a given on time and off time cycle, we need to use a microcontroller, an LED, a resistor, a breadboard, some jumper wires, and a file that contains the on time and off time values in milliseconds.
- The microcontroller is a device that can execute a program that controls the output pins. We can use any microcontroller that supports the Arduino IDE, such as Arduino Uno, Nano, or Mega.
- The LED is a light-emitting diode that can turn on or off depending on the voltage applied to its terminals. We need to connect the LED to one of the output pins of the microcontroller through a resistor to limit the current and protect the LED from burning out.
- The resistor is a passive component that reduces the current flow and the voltage drop across the LED. We can use any resistor value that is suitable for the LED, such as 220 ohms, 330 ohms, or 470 ohms.
- The breadboard is a prototyping board that allows us to connect the components without soldering. We can use any breadboard that has enough rows and columns for our circuit.
- The jumper wires are wires that can connect the components on the breadboard and the microcontroller. We can use any jumper wires that are long enough and have the appropriate connectors for our circuit.
- The file is a text file that contains the on time and off time values in milliseconds, separated by a comma. For example, the file could have the following content:

```
1000,500
```

This means that the LED should be on for 1000 milliseconds (1 second) and off for 500 milliseconds (0.5 second) in each cycle.

- To flash the LED at the given on time and off time cycle, we need to follow these steps:

  1. Connect the microcontroller to the computer using a USB cable and open the Arduino IDE.
  2. Write a program that reads the file from the computer, parses the on time and off time values, and sets the output pin to high or low accordingly using the `digitalWrite()` function and the `delay()` function.
  3. Upload the program to the microcontroller using the Arduino IDE.
  4. Disconnect the microcontroller from the computer and connect it to a power source, such as a battery or a wall adapter.
  5. Connect the LED to the output pin of the microcontroller through the resistor and the breadboard using the jumper wires.
  6. Observe the LED flashing at the given on time and off time cycle.

- A possible program that can flash the LED at the given on time and off time cycle is shown below:

```c
// Define the output pin number
#define LED_PIN 13

// Define the file name
#define FILE_NAME "times.txt"

// Declare the variables for the on time and off time
int onTime;
int offTime;

void setup() {
  // Initialize the output pin as output
  pinMode(LED_PIN, OUTPUT);

  // Initialize the serial communication
  Serial.begin(9600);

  // Open the file from the computer
  File file = SD.open(FILE_NAME);

  // Check if the file exists
  if (file) {
    // Read the first line from the file
    String line = file.readStringUntil('\n');

    // Split the line by the comma
    int commaIndex = line.indexOf(',');
    String onTimeStr = line.substring(0, commaIndex);
    String offTimeStr = line.substring(commaIndex + 1);

    // Convert the strings to integers
    onTime = onTimeStr.toInt();
    offTime = offTimeStr.toInt();

    // Close the file
    file.close();
  }
  else {
    // Print an error message if the file does not exist
    Serial.println("File not found");
  }
}

void loop() {
  // Turn the LED on for the on time
  digitalWrite(LED_PIN, HIGH);
  delay(onTime);

  // Turn the LED off for the off time
  digitalWrite(LED_PIN, LOW);
  delay(offTime);
}
```