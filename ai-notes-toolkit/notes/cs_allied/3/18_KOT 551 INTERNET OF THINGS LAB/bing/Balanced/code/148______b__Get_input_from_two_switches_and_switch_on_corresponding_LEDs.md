#### b) Get input from two switches and switch on corresponding LEDs

- To get input from two switches and switch on corresponding LEDs, we need to use a microcontroller, such as Arduino, and connect it to two switches and two LEDs using wires and resistors.
- The switches are used to provide digital input signals to the microcontroller, which can be either HIGH (5V) or LOW (0V) depending on whether the switch is pressed or not.
- The LEDs are used to provide digital output signals from the microcontroller, which can be either HIGH (5V) or LOW (0V) depending on whether the LED is turned on or off.
- The microcontroller can read the input signals from the switches using digitalRead() function and write the output signals to the LEDs using digitalWrite() function.
- The logic of the program is to check the state of each switch and turn on the corresponding LED if the switch is pressed, or turn off the LED if the switch is not pressed.
- The following is a possible circuit diagram and code for this task:

```markdown
Circuit diagram:

    +5V
     |
     |
    [ ]  Switch 1
     |
     |    10K
     +---/\/\/\---+---[ ]---GND
     |            |
     |            |
    A0           LED 1
                 |
                 |
                A1

    +5V
     |
     |
    [ ]  Switch 2
     |
     |    10K
     +---/\/\/\---+---[ ]---GND
     |            |
     |            |
    A2           LED 2
                 |
                 |
                A3

Code:

// Define the pins for switches and LEDs
const int switch1 = A0;
const int switch2 = A2;
const int led1 = A1;
const int led2 = A3;

void setup() {
  // Set the switch pins as input
  pinMode(switch1, INPUT);
  pinMode(switch2, INPUT);
  // Set the LED pins as output
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
}

void loop() {
  // Read the state of each switch
  int state1 = digitalRead(switch1);
  int state2 = digitalRead(switch2);
  // Turn on the corresponding LED if the switch is pressed, or turn off the LED if the switch is not pressed
  if (state1 == HIGH) {
    digitalWrite(led1, HIGH);
  } else {
    digitalWrite(led1, LOW);
  }
  if (state2 == HIGH) {
    digitalWrite(led2, HIGH);
  } else {
    digitalWrite(led2, LOW);
  }
}
```