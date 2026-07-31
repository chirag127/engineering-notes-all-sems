#### b) Get input from two switches and switch on corresponding LEDs

- To get input from two switches and switch on corresponding LEDs, we need to use a microcontroller, such as Arduino, and connect it to two switches and two LEDs using wires and resistors.
- The switches are used to provide digital input signals to the microcontroller, which can be either HIGH (5V) or LOW (0V) depending on whether the switch is pressed or not.
- The LEDs are used to provide digital output signals from the microcontroller, which can be either HIGH (5V) or LOW (0V) depending on whether the LED is turned on or off.
- The microcontroller can read the input signals from the switches using digitalRead() function and write the output signals to the LEDs using digitalWrite() function.
- The logic of the program is to check the state of each switch and turn on the corresponding LED if the switch is pressed, or turn off the LED if the switch is not pressed.
- The circuit diagram and the code for this project are shown below:

```markdown
Circuit diagram:

    +5V
     |
     |
    [ ]  Switch 1
     |
     |    10K
     +---/\/\/\---+--- Pin 2
     |            |
     |            |
    [ ]  LED 1    |
     |            |
     |    220     |
     +---/\/\/\---+
     |
    GND

    +5V
     |
     |
    [ ]  Switch 2
     |
     |    10K
     +---/\/\/\---+--- Pin 3
     |            |
     |            |
    [ ]  LED 2    |
     |            |
     |    220     |
     +---/\/\/\---+
     |
    GND
```

```markdown
Code:

// Define the pins for switches and LEDs
const int switch1 = 2;
const int switch2 = 3;
const int led1 = 4;
const int led2 = 5;

void setup() {
  // Set the switch pins as inputs with pull-up resistors
  pinMode(switch1, INPUT_PULLUP);
  pinMode(switch2, INPUT_PULLUP);
  // Set the LED pins as outputs
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
}

void loop() {
  // Read the state of each switch
  int state1 = digitalRead(switch1);
  int state2 = digitalRead(switch2);
  // Turn on the corresponding LED if the switch is pressed, or turn off the LED if the switch is not pressed
  if (state1 == LOW) {
    digitalWrite(led1, HIGH);
  } else {
    digitalWrite(led1, LOW);
  }
  if (state2 == LOW) {
    digitalWrite(led2, HIGH);
  } else {
    digitalWrite(led2, LOW);
  }
}
```