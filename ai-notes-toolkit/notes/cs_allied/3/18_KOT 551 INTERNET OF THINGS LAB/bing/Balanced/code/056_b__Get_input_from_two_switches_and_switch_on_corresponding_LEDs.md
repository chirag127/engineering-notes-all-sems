# Get input from two switches and switch on corresponding LEDs

- The objective of this topic is to learn how to use two switches as digital inputs and control two LEDs as digital outputs using an Arduino board.
- The switches are connected to digital pins 2 and 3 of the Arduino, and the LEDs are connected to digital pins 8 and 9, respectively.
- The switches are wired with pull-down resistors, which means they will read LOW when not pressed and HIGH when pressed.
- The LEDs are wired with current-limiting resistors, which means they will turn on when the output pin is HIGH and turn off when the output pin is LOW.
- The Arduino code for this topic is as follows:

```c
// Define constants for the pin numbers
const int switch1 = 2; // The first switch is connected to pin 2
const int switch2 = 3; // The second switch is connected to pin 3
const int led1 = 8; // The first LED is connected to pin 8
const int led2 = 9; // The second LED is connected to pin 9

// Define variables to store the switch states
int switch1State = 0; // The initial state of the first switch is 0 (LOW)
int switch2State = 0; // The initial state of the second switch is 0 (LOW)

void setup() {
  // Set the switch pins as inputs
  pinMode(switch1, INPUT);
  pinMode(switch2, INPUT);
  // Set the LED pins as outputs
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
}

void loop() {
  // Read the switch states and store them in variables
  switch1State = digitalRead(switch1);
  switch2State = digitalRead(switch2);
  // If the first switch is pressed, turn on the first LED
  if (switch1State == HIGH) {
    digitalWrite(led1, HIGH);
  }
  // Otherwise, turn off the first LED
  else {
    digitalWrite(led1, LOW);
  }
  // If the second switch is pressed, turn on the second LED
  if (switch2State == HIGH) {
    digitalWrite(led2, HIGH);
  }
  // Otherwise, turn off the second LED
  else {
    digitalWrite(led2, LOW);
  }
}
```
- The code uses constants to define the pin numbers for the switches and LEDs, and variables to store the switch states.
- The code sets the switch pins as inputs and the LED pins as outputs in the setup() function, which runs once when the Arduino is powered on or reset.
- The code reads the switch states using the digitalRead() function and stores them in variables in the loop() function, which runs repeatedly.
- The code uses if-else statements to check the switch states and turn on or off the corresponding LEDs using the digitalWrite() function.
- The code can be uploaded to the Arduino board using the Arduino IDE software and a USB cable.
- The code can be tested by pressing the switches and observing the LEDs. The expected behavior is that the first LED will turn on when the first switch is pressed, and the second LED will turn on when the second switch is pressed. The LEDs will turn off when the switches are released.