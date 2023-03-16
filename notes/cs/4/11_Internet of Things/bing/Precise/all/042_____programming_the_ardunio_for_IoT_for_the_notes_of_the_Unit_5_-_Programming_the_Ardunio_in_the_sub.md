# Unit 5 - Programming the Arduino for IoT

### Introduction
- Arduino is an open-source electronics platform based on easy-to-use hardware and software.
- It is widely used in IoT projects due to its simplicity and versatility.
- Programming the Arduino involves writing code in the Arduino programming language and uploading it to the board using the Arduino Integrated Development Environment (IDE).

### Setting up the Arduino IDE
1. Download and install the Arduino IDE from the official website.
2. Connect the Arduino board to the computer using a USB cable.
3. Open the Arduino IDE and select the appropriate board and port from the Tools menu.

### Writing and Uploading Code
1. Write the code in the Arduino programming language, which is based on C/C++.
2. Verify the code by clicking on the Verify button in the IDE.
3. Upload the code to the board by clicking on the Upload button in the IDE.

### Libraries and Functions
- The Arduino programming language includes many built-in functions and libraries for common tasks such as reading inputs, controlling outputs, and communicating with other devices.
- Additional libraries can be downloaded and installed to add new functionality to the Arduino.

### Example: Blinking an LED
- The following code demonstrates how to blink an LED connected to pin 13 on the Arduino board:

```c++
void setup() {
  pinMode(13, OUTPUT);
}

void loop() {
  digitalWrite(13, HIGH);
  delay(1000);
  digitalWrite(13, LOW);
  delay(1000);
}
```

- The `setup` function is called once when the board is powered on or reset. It is used to initialize the pin modes and other settings.
- The `loop` function is called repeatedly and contains the main logic of the program. In this example, it turns the LED on and off with a delay of one second between each state change.
- The `pinMode` function sets the mode of the specified pin (input or output).
- The `digitalWrite` function sets the state of the specified pin (high or low).
- The `delay` function pauses the program for the specified number of milliseconds.

### Conclusion
- Programming the Arduino for IoT involves writing code in the Arduino programming language and uploading it to the board using the Arduino IDE.
- The Arduino programming language includes many built-in functions and libraries for common tasks, and additional libraries can be downloaded and installed to add new functionality.
- By understanding the basics of Arduino programming, it is possible to create a wide range of IoT projects using this versatile platform.