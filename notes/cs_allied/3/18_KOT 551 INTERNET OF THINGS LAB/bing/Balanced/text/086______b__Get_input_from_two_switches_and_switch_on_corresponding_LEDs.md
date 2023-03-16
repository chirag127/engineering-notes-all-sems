#### b) Get input from two switches and switch on corresponding LEDs

- To get input from two switches and switch on corresponding LEDs, we need to use a microcontroller, such as Arduino, and connect it to two switches and two LEDs using wires and resistors.
- The switches are used as digital inputs to the microcontroller, which means they can send either a HIGH (5V) or a LOW (0V) signal to the microcontroller pins. The LEDs are used as digital outputs, which means the microcontroller can control their state by sending either a HIGH or a LOW signal to them.
- We need to use resistors to limit the current flowing through the LEDs and prevent them from burning out. The value of the resistors depends on the type and color of the LEDs, but a common value is 220 ohms.
- We also need to connect the ground (GND) pins of the microcontroller, the switches, and the LEDs to a common ground, such as the negative terminal of a battery or a power supply.
- The circuit diagram for this project is shown below:

![Circuit diagram](https://i.imgur.com/0t0Z7jy.png)

- The code for this project is shown below:

```c
// Define the pins for the switches and the LEDs
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

// Read the state of the switches and control the LEDs accordingly
void loop() {
  // Read the state of switch 1
  int switch1State = digitalRead(SWITCH1);
  // If switch 1 is pressed, turn on LED 1
  if (switch1State == HIGH) {
    digitalWrite(LED1, HIGH);
  }
  // Otherwise, turn off LED 1
  else {
    digitalWrite(LED1, LOW);
  }
  // Read the state of switch 2
  int switch2State = digitalRead(SWITCH2);
  // If switch 2 is pressed, turn on LED 2
  if (switch2State == HIGH) {
    digitalWrite(LED2, HIGH);
  }
  // Otherwise, turn off LED 2
  else {
    digitalWrite(LED2, LOW);
  }
}
```