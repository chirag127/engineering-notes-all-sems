#### b) Get input from two switches and switch on corresponding LEDs

- To get input from two switches and switch on corresponding LEDs, we need to connect the switches and the LEDs to the input and output pins of a microcontroller, such as Arduino.
- We also need to write a program that reads the state of the switches and controls the state of the LEDs accordingly.
- The program can be written in Arduino IDE, which is a software that allows us to write and upload code to the microcontroller.
- The program can use the `digitalRead()` function to read the state of the switches, which can be either HIGH or LOW, depending on whether they are pressed or not.
- The program can also use the `digitalWrite()` function to set the state of the LEDs, which can be either HIGH or LOW, depending on whether they are on or off.
- The program can use `if` statements to check the state of the switches and set the state of the LEDs accordingly.
- For example, if switch 1 is pressed and switch 2 is not pressed, then LED 1 should be on and LED 2 should be off.
- The program can use a `void setup()` function to initialize the input and output pins, and a `void loop()` function to run the code repeatedly.
- The program can be uploaded to the microcontroller using a USB cable and the Arduino IDE.
- The following is an example of the program:

```c
// Define the input and output pins
#define SWITCH_1 2 // Switch 1 is connected to pin 2
#define SWITCH_2 3 // Switch 2 is connected to pin 3
#define LED_1 4 // LED 1 is connected to pin 4
#define LED_2 5 // LED 2 is connected to pin 5

// Initialize the input and output pins
void setup() {
  pinMode(SWITCH_1, INPUT); // Set pin 2 as input
  pinMode(SWITCH_2, INPUT); // Set pin 3 as input
  pinMode(LED_1, OUTPUT); // Set pin 4 as output
  pinMode(LED_2, OUTPUT); // Set pin 5 as output
}

// Run the code repeatedly
void loop() {
  // Read the state of the switches
  int switch_1_state = digitalRead(SWITCH_1); // Read pin 2
  int switch_2_state = digitalRead(SWITCH_2); // Read pin 3

  // Check the state of the switches and set the state of the LEDs accordingly
  if (switch_1_state == HIGH && switch_2_state == LOW) {
    // If switch 1 is pressed and switch 2 is not pressed
    digitalWrite(LED_1, HIGH); // Turn on LED 1
    digitalWrite(LED_2, LOW); // Turn off LED 2
  } else if (switch_1_state == LOW && switch_2_state == HIGH) {
    // If switch 1 is not pressed and switch 2 is pressed
    digitalWrite(LED_1, LOW); // Turn off LED 1
    digitalWrite(LED_2, HIGH); // Turn on LED 2
  } else if (switch_1_state == HIGH && switch_2_state == HIGH) {
    // If both switches are pressed
    digitalWrite(LED_1, HIGH); // Turn on LED 1
    digitalWrite(LED_2, HIGH); // Turn on LED 2
  } else {
    // If both switches are not pressed
    digitalWrite(LED_1, LOW); // Turn off LED 1
    digitalWrite(LED_2, LOW); // Turn off LED 2
  }
}
```