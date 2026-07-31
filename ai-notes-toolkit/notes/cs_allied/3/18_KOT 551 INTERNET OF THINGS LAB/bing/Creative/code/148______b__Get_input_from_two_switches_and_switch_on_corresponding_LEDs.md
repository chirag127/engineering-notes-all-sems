#### b) Get input from two switches and switch on corresponding LEDs

- To get input from two switches and switch on corresponding LEDs, we need to use a microcontroller, such as Arduino, and connect it to two push buttons and two LEDs.
- The push buttons are used as digital inputs to the microcontroller, and the LEDs are used as digital outputs. The microcontroller can read the state of the push buttons (HIGH or LOW) and control the state of the LEDs (ON or OFF) accordingly.
- The circuit diagram for this project is shown below:

```
+5V  +5V
 |    |
 |    |
 |    |
 |    |       +-----+
 |    +-------| LED1|----+
 |            +-----+    |
 |                       |
 |                       |
 |            +-----+    |
 |    +-------| LED2|----+
 |    |       +-----+    |
 |    |                  |
 |    |                  |
 |    |                  |
 |    |                  |
 |    |                  |
 |    |                  |
 |    |                  |
 |    |                  |
 |    |                  |
 |    |                  |
 |    |                  |
 |    |                  |
 |    |                  |
 |    |                  |
 +----+----+----+----+---+
 |    |    |    |    |
 |    |    |    |    |
 |    |    |    |    |
 |    |    |    |    |
 |    |    |    |    |
 |    |    |    |    |
 |    |    |    |    |
 |    |    |    |    |
 |    |    |    |    |
 |    |    |    |    |
 |    |    |    |    |
 +----+----+----+----+
  2    3    4    5
  |    |    |    |
  |    |    |    |
  |    |    |    |
  |    |    |    |
  |    |    |    |
  |    |    |    |
  |    |    |    |
  |    |    |    |
  |    |    |    |
  |    |    |    |
  |    |    |    |
  |    |    |    +-----+
  |    |    +----------| SW2|
  |    |               +-----+
  |    +-----+
  +----------| SW1|
             +-----+
```

- The code for this project is shown below:

```c
// Define the pins for the push buttons and LEDs
#define SW1 2
#define SW2 3
#define LED1 4
#define LED2 5

// Declare variables to store the button states
int SW1_state = 0;
int SW2_state = 0;

void setup() {
  // Set the push buttons as inputs with pull-up resistors
  pinMode(SW1, INPUT_PULLUP);
  pinMode(SW2, INPUT_PULLUP);

  // Set the LEDs as outputs
  pinMode(LED1, OUTPUT);
  pinMode(LED2, OUTPUT);
}

void loop() {
  // Read the button states
  SW1_state = digitalRead(SW1);
  SW2_state = digitalRead(SW2);

  // If SW1 is pressed, turn on LED1
  if (SW1_state == LOW) {
    digitalWrite(LED1, HIGH);
  }
  // Otherwise, turn off LED1
  else {
    digitalWrite(LED1, LOW);
  }

  // If SW2 is pressed, turn on LED2
  if (SW2_state == LOW) {
    digitalWrite(LED2, HIGH);
  }
  // Otherwise, turn off LED2
  else {
    digitalWrite(LED2, LOW);
  }
}
```