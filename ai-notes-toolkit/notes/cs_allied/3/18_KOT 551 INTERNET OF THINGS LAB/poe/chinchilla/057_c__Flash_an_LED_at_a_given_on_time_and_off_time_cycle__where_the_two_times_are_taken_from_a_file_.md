# Flashing an LED with On and Off Time Cycle from File

Flashing an LED is a common exercise in microcontroller programming. In this exercise, we will be flashing an LED at a given on time and off time cycle, where the two times are taken from a file. This exercise will help you understand how to read data from a file and how to use it in your program.

## Required Components

To perform this exercise, you will need the following components:

- A microcontroller board (e.g., Arduino Uno)
- A breadboard
- An LED
- A resistor (220 ohms)
- Jumper wires

## Circuit Diagram

The circuit diagram for this exercise is straightforward. Connect the longer leg of the LED to pin 13 of the microcontroller board and connect the shorter leg of the LED to the resistor. Connect the other end of the resistor to the ground of the microcontroller board. See the circuit diagram below:

```
                +--|>|--+
                |       |
                |      ---
                |      GND
                |       |
                +-------+
                   |
                  Pin 13
```

## Code Explanation

The code for this exercise will read the on time and off time values from a file and use them to flash the LED. The file should contain two values separated by a comma. The first value is the on time, and the second value is the off time. The code will then loop through these two values and flash the LED accordingly.

Here are the steps involved in the code:

1. First, we will include the necessary libraries for the exercise. In this exercise, we will be using the `SD.h` library to read the file from the SD card and the `SPI.h` library to communicate with the SD card.

2. Next, we will define the pins for the LED and the chip select pin for the SD card.

3. We will then declare the variables for reading the file from the SD card. We will use the `File` data type to store the file.

4. In the `setup()` function, we will initialize the SD card and open the file.

5. In the `loop()` function, we will read the values from the file and use them to flash the LED. We will use the `millis()` function to measure the time and the `digitalWrite()` function to turn the LED on and off.

6. Finally, we will close the file and turn off the LED.

Here is the code for the exercise:

```cpp
#include <SPI.h>
#include <SD.h>

const int LED_PIN = 13;
const int CS_PIN = 10;

File myFile;

void setup() {
  pinMode(LED_PIN, OUTPUT);
  Serial.begin(9600);

  if (!SD.begin(CS_PIN)) {
    Serial.println("SD card initialization failed!");
    return;
  }

  myFile = SD.open("on_off_times.txt");

  if (!myFile) {
    Serial.println("File not found!");
    return;
  }
}

void loop() {
  if (myFile.available()) {
    int on_time = myFile.parseInt();
    int off_time = myFile.parseInt();

    digitalWrite(LED_PIN, HIGH);
    delay(on_time);
    digitalWrite(LED_PIN, LOW);
    delay(off_time);
  } else {
    myFile.close();
    digitalWrite(LED_PIN, LOW);
  }
}
```

## Conclusion

Flashing an LED at a given on time and off time cycle, where the two times are taken from a file, is a good exercise in microcontroller programming. This exercise gives you a good understanding of how to read data from a file and how to use it in your program. With this exercise, you can experiment with different on and off times and see how it affects the flashing of the LED.