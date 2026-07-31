#### b) Get input from two switches and switch on corresponding LEDs

- To get input from two switches and switch on corresponding LEDs, we need to use a microcontroller, such as Arduino, and connect it to two switches and two LEDs using wires and resistors.
- The switches are used to provide digital input signals to the microcontroller, which can be either HIGH (5V) or LOW (0V) depending on whether the switch is pressed or not.
- The LEDs are used to provide digital output signals from the microcontroller, which can be either HIGH (5V) or LOW (0V) depending on whether the LED is turned on or off.
- The microcontroller can read the input signals from the switches using digitalRead() function and write the output signals to the LEDs using digitalWrite() function.
- The logic of the program is to check the state of each switch and turn on the corresponding LED if the switch is pressed, and turn off the LED if the switch is not pressed.
- The circuit diagram and the code for this task are shown below:

```markdown
Circuit diagram:

    +5V  +5V
     |    |
     |    |
    ---  ---
    | |  | |  Switches
    ---  ---
     |    |
     |    |
    10k  10k  Resistors
     |    |
     |    |
     |    |
    D2   D3  Digital pins for input
     |    |
     |    |
    ---  ---
    | |  | |  LEDs
    ---  ---
     |    |
     |    |
    220  220  Resistors
     |    |
     |    |
    GND  GND
     |    |
     |    |
    ---  ---
    | |  | |  Ground
    ---  ---

Code:

// Define the pin numbers for switches and LEDs
#define SWITCH1 2
#define SWITCH2 3
#define LED1 4
#define LED2 5

// Set up the pins as input or output
void setup() {
  pinMode(SWITCH1, INPUT);
  pinMode(SWITCH2, INPUT);
  pinMode(LED1, OUTPUT);
  pinMode(LED2, OUTPUT);
}

// Loop the program to read and write the signals
void loop() {
  // Read the state of each switch
  int switch1State = digitalRead(SWITCH1);
  int switch2State = digitalRead(SWITCH2);

  // Write the state of each LED
  digitalWrite(LED1, switch1State);
  digitalWrite(LED2, switch2State);
}
```