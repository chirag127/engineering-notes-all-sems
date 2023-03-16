#### b) Get input from two switches and switch on corresponding LEDs

- To get input from two switches and switch on corresponding LEDs, we need to use a microcontroller, such as Arduino, and connect the switches and LEDs to its digital pins.
- We also need to write a program that reads the state of the switches and controls the state of the LEDs accordingly.
- The program should use the pinMode() function to set the switches as inputs and the LEDs as outputs, and the digitalRead() and digitalWrite() functions to read and write the digital values of the pins.
- The program should use conditional statements, such as if-else or switch-case, to check the combination of the switch states and turn on the corresponding LEDs.
- For example, if both switches are on, both LEDs should be on; if only one switch is on, only the corresponding LED should be on; if both switches are off, both LEDs should be off.
- The program should run in a loop, so that it can continuously monitor the switches and update the LEDs.
- The following is a possible circuit diagram and program for this task:

```
// Circuit diagram
// Connect switch 1 to pin 2 and LED 1 to pin 4
// Connect switch 2 to pin 3 and LED 2 to pin 5
// Connect the common terminals of the switches to ground
// Connect the anodes of the LEDs to 5V through 220 ohm resistors

// Program
// Define the pin numbers
#define SWITCH_1 2
#define SWITCH_2 3
#define LED_1 4
#define LED_2 5

// Setup function
void setup() {
  // Set the switches as inputs
  pinMode(SWITCH_1, INPUT);
  pinMode(SWITCH_2, INPUT);
  // Set the LEDs as outputs
  pinMode(LED_1, OUTPUT);
  pinMode(LED_2, OUTPUT);
}

// Loop function
void loop() {
  // Read the switch states
  int switch_1_state = digitalRead(SWITCH_1);
  int switch_2_state = digitalRead(SWITCH_2);
  // Check the combination of the switch states
  if (switch_1_state == HIGH && switch_2_state == HIGH) {
    // If both switches are on, turn on both LEDs
    digitalWrite(LED_1, HIGH);
    digitalWrite(LED_2, HIGH);
  } else if (switch_1_state == HIGH && switch_2_state == LOW) {
    // If only switch 1 is on, turn on LED 1 and turn off LED 2
    digitalWrite(LED_1, HIGH);
    digitalWrite(LED_2, LOW);
  } else if (switch_1_state == LOW && switch_2_state == HIGH) {
    // If only switch 2 is on, turn on LED 2 and turn off LED 1
    digitalWrite(LED_1, LOW);
    digitalWrite(LED_2, HIGH);
  } else {
    // If both switches are off, turn off both LEDs
    digitalWrite(LED_1, LOW);
    digitalWrite(LED_2, LOW);
  }
}
```