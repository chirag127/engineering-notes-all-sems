#### b) Get input from two switches and switch on corresponding LEDs

- To get input from two switches and switch on corresponding LEDs, we need to use a microcontroller, such as Arduino, and connect it to two switches and two LEDs using wires and resistors.
- The switches are used as digital inputs, which means they can have only two states: HIGH (when pressed) or LOW (when not pressed).
- The LEDs are used as digital outputs, which means they can be turned on or off by sending a HIGH or LOW signal from the microcontroller.
- We need to write a program for the microcontroller that reads the state of the switches and sends the appropriate signals to the LEDs.
- The program can be written in Arduino IDE, which is a software that allows us to write and upload code to the microcontroller.
- The program can use the following functions:

  - `pinMode(pin, mode)` : This function sets the mode of a pin as either INPUT (for switches) or OUTPUT (for LEDs).
  - `digitalRead(pin)` : This function reads the state of a pin as either HIGH or LOW and returns it as a value.
  - `digitalWrite(pin, value)` : This function writes a value (either HIGH or LOW) to a pin, turning it on or off.

- The program can use the following logic:

  - If switch 1 is pressed (HIGH), turn on LED 1 (HIGH).
  - If switch 1 is not pressed (LOW), turn off LED 1 (LOW).
  - If switch 2 is pressed (HIGH), turn on LED 2 (HIGH).
  - If switch 2 is not pressed (LOW), turn off LED 2 (LOW).

- The program can be written as follows:

```c
// Define the pins for the switches and LEDs
#define SWITCH1 2
#define SWITCH2 3
#define LED1 4
#define LED2 5

// Set up the pins as inputs or outputs
void setup() {
  pinMode(SWITCH1, INPUT);
  pinMode(SWITCH2, INPUT);
  pinMode(LED1, OUTPUT);
  pinMode(LED2, OUTPUT);
}

// Read the state of the switches and control the LEDs
void loop() {
  // Read the state of switch 1
  int switch1State = digitalRead(SWITCH1);
  // If switch 1 is pressed, turn on LED 1
  if (switch1State == HIGH) {
    digitalWrite(LED1, HIGH);
  }
  // If switch 1 is not pressed, turn off LED 1
  else {
    digitalWrite(LED1, LOW);
  }
  // Read the state of switch 2
  int switch2State = digitalRead(SWITCH2);
  // If switch 2 is pressed, turn on LED 2
  if (switch2State == HIGH) {
    digitalWrite(LED2, HIGH);
  }
  // If switch 2 is not pressed, turn off LED 2
  else {
    digitalWrite(LED2, LOW);
  }
}
```

- The following diagram shows how to connect the switches and LEDs to the microcontroller:

![Diagram of switches and LEDs connected to Arduino](https://i.imgur.com/8Z6m9Za.png)