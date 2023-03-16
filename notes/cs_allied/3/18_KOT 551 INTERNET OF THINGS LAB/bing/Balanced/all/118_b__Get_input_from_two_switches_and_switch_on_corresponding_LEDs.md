# Get input from two switches and switch on corresponding LEDs

- This topic is about how to use two switches and two LEDs to create a simple logic circuit.
- A switch is a device that can open or close an electrical circuit, allowing current to flow or stop.
- An LED (light-emitting diode) is a device that emits light when current passes through it.
- To get input from two switches, we need to connect them to the input pins of a microcontroller, such as an Arduino.
- To switch on corresponding LEDs, we need to connect them to the output pins of the microcontroller, and use code to control their states.
- The code will read the values of the switches, and turn on or off the LEDs accordingly.
- For example, we can use the following circuit diagram and code to implement a simple AND gate, which will only turn on the LED when both switches are pressed.

![AND gate circuit diagram](https://i.imgur.com/9YXyH7l.png)

```c
// Define the input and output pins
const int switch1 = 2; // Switch 1 is connected to pin 2
const int switch2 = 3; // Switch 2 is connected to pin 3
const int led = 13; // LED is connected to pin 13

void setup() {
  // Set the input pins as inputs with pull-up resistors
  pinMode(switch1, INPUT_PULLUP);
  pinMode(switch2, INPUT_PULLUP);
  // Set the output pin as output
  pinMode(led, OUTPUT);
}

void loop() {
  // Read the values of the switches
  int switch1State = digitalRead(switch1);
  int switch2State = digitalRead(switch2);
  // If both switches are pressed (LOW), turn on the LED
  if (switch1State == LOW && switch2State == LOW) {
    digitalWrite(led, HIGH);
  }
  // Otherwise, turn off the LED
  else {
    digitalWrite(led, LOW);
  }
}
```