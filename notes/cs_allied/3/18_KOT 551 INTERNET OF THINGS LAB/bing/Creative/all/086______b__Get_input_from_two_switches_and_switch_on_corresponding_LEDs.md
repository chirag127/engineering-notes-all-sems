#### b) Get input from two switches and switch on corresponding LEDs

- To get input from two switches and switch on corresponding LEDs, we need to use a microcontroller, such as Arduino, and connect it to two switches and two LEDs using wires and resistors.
- The switches are used as digital inputs, which can be either HIGH (5V) or LOW (0V) depending on whether they are pressed or not. The LEDs are used as digital outputs, which can be either ON or OFF depending on the voltage applied to them by the microcontroller.
- We need to write a program for the microcontroller that reads the state of the switches and controls the state of the LEDs accordingly. For example, if switch 1 is pressed, LED 1 should be ON, and if switch 2 is pressed, LED 2 should be ON. If both switches are pressed, both LEDs should be ON. If neither switch is pressed, both LEDs should be OFF.
- The program can be written in Arduino IDE, which is a software that allows us to write and upload code to the microcontroller. The code can be written in C or C++ language, which are common programming languages for embedded systems.
- The code can be divided into two main parts: setup and loop. The setup part runs once when the microcontroller is powered on, and it is used to initialize the pins that are connected to the switches and LEDs. The loop part runs repeatedly, and it is used to read the state of the switches and write the state of the LEDs.
- The code can look something like this:

```c
// Define the pins that are connected to the switches and LEDs
#define SWITCH_1 2 // Switch 1 is connected to pin 2
#define SWITCH_2 3 // Switch 2 is connected to pin 3
#define LED_1 4 // LED 1 is connected to pin 4
#define LED_2 5 // LED 2 is connected to pin 5

// Define the variables that store the state of the switches and LEDs
int switch_1_state = 0; // 0 means LOW, 1 means HIGH
int switch_2_state = 0;
int led_1_state = 0; // 0 means OFF, 1 means ON
int led_2_state = 0;

void setup() {
  // Set the pins as inputs or outputs
  pinMode(SWITCH_1, INPUT); // Switch 1 is an input
  pinMode(SWITCH_2, INPUT); // Switch 2 is an input
  pinMode(LED_1, OUTPUT); // LED 1 is an output
  pinMode(LED_2, OUTPUT); // LED 2 is an output
}

void loop() {
  // Read the state of the switches
  switch_1_state = digitalRead(SWITCH_1); // Read the voltage at pin 2
  switch_2_state = digitalRead(SWITCH_2); // Read the voltage at pin 3

  // Control the state of the LEDs based on the state of the switches
  if (switch_1_state == HIGH) { // If switch 1 is pressed
    led_1_state = HIGH; // Turn on LED 1
  } else { // If switch 1 is not pressed
    led_1_state = LOW; // Turn off LED 1
  }
  if (switch_2_state == HIGH) { // If switch 2 is pressed
    led_2_state = HIGH; // Turn on LED 2
  } else { // If switch 2 is not pressed
    led_2_state = LOW; // Turn off LED 2
  }

  // Write the state of the LEDs to the pins
  digitalWrite(LED_1, led_1_state); // Write the voltage to pin 4
  digitalWrite(LED_2, led_2_state); // Write the voltage to pin 5
}
```
- To upload the code to the microcontroller, we need to connect it to the computer using a USB cable, select the correct board and port in the Arduino IDE, and click the upload button. The code will be compiled and transferred to the microcontroller, and it will start running automatically.
- To test the code, we can press the switches and observe the LEDs. They should turn on and off according to the logic we defined in the code. If they do not work as expected, we can check the wiring, the code, and the power supply for any errors or faults.