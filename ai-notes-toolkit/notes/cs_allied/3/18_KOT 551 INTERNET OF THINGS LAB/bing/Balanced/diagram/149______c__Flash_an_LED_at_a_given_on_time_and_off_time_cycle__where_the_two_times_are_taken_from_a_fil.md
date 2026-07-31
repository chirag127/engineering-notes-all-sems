#### c) Flash an LED at a given on time and off time cycle, where the two times are taken from a file.

- To flash an LED at a given on time and off time cycle, we need to use a microcontroller, an LED, a resistor, a breadboard, and some jumper wires.
- We also need to create a text file that contains two numbers, representing the on time and off time in milliseconds, separated by a comma. For example, the file could contain `500,1000` to flash the LED for half a second and turn it off for one second.
- We need to write a program for the microcontroller that can read the file from a storage device, such as a microSD card, and use the values to control the LED.
- The program should have the following steps:
  - Initialize the microcontroller and the storage device.
  - Define a pin for the LED and set it as an output.
  - Open the file and read the two numbers into variables, such as `onTime` and `offTime`.
  - Close the file and release the storage device.
  - Enter an infinite loop that does the following:
    - Turn on the LED by setting the pin to high.
    - Delay for `onTime` milliseconds using a timer or a delay function.
    - Turn off the LED by setting the pin to low.
    - Delay for `offTime` milliseconds using a timer or a delay function.
- The program should handle any errors or exceptions that may occur, such as file not found, invalid format, or storage device failure.
- The program should be written in a language that is compatible with the microcontroller, such as C, C++, or Arduino.
- The program should be uploaded to the microcontroller using a USB cable or a wireless connection.
- The program should run automatically when the microcontroller is powered on or reset.