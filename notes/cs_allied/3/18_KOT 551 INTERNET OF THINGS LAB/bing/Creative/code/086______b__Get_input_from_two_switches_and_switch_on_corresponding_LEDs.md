#### b) Get input from two switches and switch on corresponding LEDs

- To get input from two switches and switch on corresponding LEDs, we need to use a microcontroller, such as Arduino, and connect it to the switches and LEDs using wires and resistors.
- The switches are used as digital inputs, which means they can have two states: HIGH (when pressed) or LOW (when not pressed). The LEDs are used as digital outputs, which means they can be turned on or off by sending HIGH or LOW signals from the microcontroller.
- The wiring diagram for this project is shown below:

```
+5V  o-----/ ----o 10K o-----o A0
                  |
                  |
GND  o------------o

+5V  o-----/ ----o 10K o-----o A1
                  |
                  |
GND  o------------o

      +5V  o-----o 220 o-----|<|-----o 13
                  |
                  |
      GND  o------o

      +5V  o-----o 220 o-----|<|-----o 12
                  |
                  |
      GND  o------o
```

- The code for this project is shown below:

```c
// Define the pins for the switches and LEDs
const int switch1 = A0;
const int switch2 = A1;
const int led1 = 13;
const int led2 = 12;

// Define variables to store the switch states
int switch1State = 0;
int switch2State = 0;

void setup() {
  // Set the switch pins as inputs with pull-down resistors
  pinMode(switch1, INPUT_PULLDOWN);
  pinMode(switch2, INPUT_PULLDOWN);
  // Set the LED pins as outputs
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
}

void loop() {
  // Read the switch states
  switch1State = digitalRead(switch1);
  switch2State = digitalRead(switch2);
  // If switch1 is pressed, turn on led1
  if (switch1State == HIGH) {
    digitalWrite(led1, HIGH);
  }
  // Otherwise, turn off led1
  else {
    digitalWrite(led1, LOW);
  }
  // If switch2 is pressed, turn on led2
  if (switch2State == HIGH) {
    digitalWrite(led2, HIGH);
  }
  // Otherwise, turn off led2
  else {
    digitalWrite(led2, LOW);
  }
}
```