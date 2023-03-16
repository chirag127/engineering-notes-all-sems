#### b) Get input from two switches and switch on corresponding LEDs

- To get input from two switches and switch on corresponding LEDs, we need to use a microcontroller, such as Arduino, and connect it to two switches and two LEDs using wires and resistors.
- The switches are used to provide digital input signals to the microcontroller, which can be either HIGH (5V) or LOW (0V) depending on whether the switch is pressed or not.
- The LEDs are used to provide digital output signals from the microcontroller, which can be either HIGH (5V) or LOW (0V) depending on whether the LED is turned on or off.
- The microcontroller can read the input signals from the switches using its digital pins, and write the output signals to the LEDs using its digital pins.
- The logic of the program is to check the state of each switch, and turn on the corresponding LED if the switch is pressed, and turn off the LED if the switch is not pressed.
- The program can be written in Arduino IDE using C/C++ language, and uploaded to the microcontroller using a USB cable.
- The circuit diagram and the code for the program are shown below:

```
// Circuit diagram
// +5V --- Switch 1 --- Pin 2
// +5V --- Switch 2 --- Pin 3
// Pin 4 --- Resistor --- LED 1 --- GND
// Pin 5 --- Resistor --- LED 2 --- GND

// Code
// Define the pin numbers for the switches and LEDs
#define SWITCH1 2
#define SWITCH2 3
#define LED1 4
#define LED2 5

// Initialize the pins as input or output
void setup() {
  pinMode(SWITCH1, INPUT);
  pinMode(SWITCH2, INPUT);
  pinMode(LED1, OUTPUT);
  pinMode(LED2, OUTPUT);
}

// Loop the program to check the switches and control the LEDs
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