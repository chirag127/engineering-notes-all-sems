#### b) Get input from two switches and switch on corresponding LEDs

- To get input from two switches and switch on corresponding LEDs, we need to use a microcontroller, such as Arduino, and connect it to the switches and LEDs using wires and resistors.
- The switches are used as digital inputs, which means they can have only two states: HIGH (when pressed) or LOW (when not pressed).
- The LEDs are used as digital outputs, which means they can be turned on or off by sending a HIGH or LOW signal from the microcontroller.
- The circuit diagram for this project is shown below:

```
    +5V
     |
     |
    [ ] 10k
     |
     +---[ ] SW1
     |    |
     |    |
    [ ] 2k
     |
     +---[ ] LED1
     |    |
     |    |
    GND  GND

    +5V
     |
     |
    [ ] 10k
     |
     +---[ ] SW2
     |    |
     |    |
    [ ] 2k
     |
     +---[ ] LED2
     |    |
     |    |
    GND  GND
```

- The code for this project is shown below:

```c
// Define the pins for the switches and LEDs
#define SW1 2
#define SW2 3
#define LED1 4
#define LED2 5

// Initialize the variables for the switch states
int sw1State = 0;
int sw2State = 0;

void setup() {
  // Set the switch pins as inputs with pull-up resistors
  pinMode(SW1, INPUT_PULLUP);
  pinMode(SW2, INPUT_PULLUP);
  // Set the LED pins as outputs
  pinMode(LED1, OUTPUT);
  pinMode(LED2, OUTPUT);
}

void loop() {
  // Read the switch states
  sw1State = digitalRead(SW1);
  sw2State = digitalRead(SW2);
  // If SW1 is pressed, turn on LED1
  if (sw1State == LOW) {
    digitalWrite(LED1, HIGH);
  }
  // If SW1 is not pressed, turn off LED1
  else {
    digitalWrite(LED1, LOW);
  }
  // If SW2 is pressed, turn on LED2
  if (sw2State == LOW) {
    digitalWrite(LED2, HIGH);
  }
  // If SW2 is not pressed, turn off LED2
  else {
    digitalWrite(LED2, LOW);
  }
}
```