#### b) Get input from two switches and switch on corresponding LEDs

- To get input from two switches and switch on corresponding LEDs, we need to use a microcontroller, such as Arduino, and connect it to two switches and two LEDs using wires and resistors.
- The switches are used as digital inputs, which can be either HIGH (5V) or LOW (0V) depending on whether they are pressed or not. The LEDs are used as digital outputs, which can be either ON or OFF depending on the voltage applied to them by the microcontroller.
- We need to write a program for the microcontroller that reads the state of the switches and controls the state of the LEDs accordingly. For example, if switch 1 is pressed, LED 1 should be ON, and if switch 2 is pressed, LED 2 should be ON. If both switches are pressed, both LEDs should be ON. If neither switch is pressed, both LEDs should be OFF.
- The program can be written in Arduino IDE, which is a software that allows us to write and upload code to the microcontroller. The code can be written in C or C++ language, which are common programming languages for embedded systems.
- The code can be divided into two main parts: setup and loop. The setup part runs once when the microcontroller is powered on or reset, and it is used to initialize the pins and variables. The loop part runs repeatedly and it is used to read the inputs and control the outputs.
- The code can look something like this:

```c
// Define the pin numbers for the switches and LEDs
#define SWITCH1 2
#define SWITCH2 3
#define LED1 4
#define LED2 5

// Define variables to store the state of the switches and LEDs
int switch1State = 0;
int switch2State = 0;
int led1State = 0;
int led2State = 0;

void setup() {
  // Set the switches as inputs and the LEDs as outputs
  pinMode(SWITCH1, INPUT);
  pinMode(SWITCH2, INPUT);
  pinMode(LED1, OUTPUT);
  pinMode(LED2, OUTPUT);
}

void loop() {
  // Read the state of the switches
  switch1State = digitalRead(SWITCH1);
  switch2State = digitalRead(SWITCH2);

  // Control the state of the LEDs based on the state of the switches
  if (switch1State == HIGH) {
    led1State = HIGH;
  } else {
    led1State = LOW;
  }

  if (switch2State == HIGH) {
    led2State = HIGH;
  } else {
    led2State = LOW;
  }

  // Write the state of the LEDs to the pins
  digitalWrite(LED1, led1State);
  digitalWrite(LED2, led2State);
}
```
- To upload the code to the microcontroller, we need to connect it to the computer using a USB cable, select the correct board and port in the Arduino IDE, and click on the upload button. The code will be compiled and transferred to the microcontroller, and it will start running automatically.
- To test the code, we can press the switches and observe the LEDs. They should turn on and off according to the logic we defined in the code. If the code does not work as expected, we can debug it by checking the connections, the code syntax, and the logic. We can also use the serial monitor or the serial plotter in the Arduino IDE to print or plot the values of the variables and see how they change over time.