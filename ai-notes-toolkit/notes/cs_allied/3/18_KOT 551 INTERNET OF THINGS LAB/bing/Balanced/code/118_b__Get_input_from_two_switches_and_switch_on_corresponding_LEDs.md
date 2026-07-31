# Get input from two switches and switch on corresponding LEDs

- This is a simple project that demonstrates how to use two switches as digital inputs and control two LEDs as digital outputs.
- The switches are connected to pins 2 and 3 of the Arduino board, and the LEDs are connected to pins 8 and 9.
- The switches are wired with pull-down resistors, which means they are normally LOW and become HIGH when pressed.
- The LEDs are wired with current-limiting resistors, which means they are normally OFF and become ON when the corresponding pin is HIGH.
- The code for this project is as follows:

```c
// Define the pin numbers for the switches and LEDs
#define SWITCH1 2
#define SWITCH2 3
#define LED1 8
#define LED2 9

// Initialize the switch and LED states
int switch1State = 0;
int switch2State = 0;
int led1State = 0;
int led2State = 0;

void setup() {
  // Set the switch pins as inputs and the LED pins as outputs
  pinMode(SWITCH1, INPUT);
  pinMode(SWITCH2, INPUT);
  pinMode(LED1, OUTPUT);
  pinMode(LED2, OUTPUT);
}

void loop() {
  // Read the switch states
  switch1State = digitalRead(SWITCH1);
  switch2State = digitalRead(SWITCH2);

  // If switch 1 is pressed, toggle LED 1 state
  if (switch1State == HIGH) {
    led1State = !led1State;
    digitalWrite(LED1, led1State);
  }

  // If switch 2 is pressed, toggle LED 2 state
  if (switch2State == HIGH) {
    led2State = !led2State;
    digitalWrite(LED2, led2State);
  }
}
```

- The code uses the `digitalRead()` function to read the switch states, and the `digitalWrite()` function to control the LED states.
- The code also uses the `!` operator to invert the LED states, which means if the LED is ON, it becomes OFF, and vice versa.
- The code runs in an infinite loop, and checks the switch states every time.
- The result is that when a switch is pressed, the corresponding LED will toggle its state, and when the switch is released, the LED will keep its state.