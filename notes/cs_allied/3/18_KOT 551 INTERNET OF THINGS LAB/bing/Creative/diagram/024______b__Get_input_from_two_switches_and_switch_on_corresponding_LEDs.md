Hello, I am Sydney, your AI assistant. I can help you with your topic. Here is some content that you can use for your study material.

#### b) Get input from two switches and switch on corresponding LEDs

- To get input from two switches and switch on corresponding LEDs, you need to use a microcontroller, such as Arduino, and connect it to the switches and LEDs using wires and resistors.
- A switch is a device that can open or close an electrical circuit, allowing current to flow or stop. A LED (light-emitting diode) is a device that emits light when current passes through it.
- You can use the digital pins of the Arduino to read the state of the switches and control the state of the LEDs. You need to declare the pin numbers of the switches and LEDs as constants, and set them as input or output using the pinMode() function in the setup() function.
- You can use the digitalRead() function to read the state of the switches, which will return either HIGH or LOW depending on whether the switch is closed or open. You can use the digitalWrite() function to write the state of the LEDs, which will turn them on or off depending on whether you write HIGH or LOW.
- You can use the if-else statements to check the state of the switches and write the corresponding state of the LEDs in the loop() function, which will run repeatedly. For example, if switch 1 is closed and switch 2 is open, you can write HIGH to LED 1 and LOW to LED 2, and vice versa.
- Here is a diagram of the circuit and a sample code for the Arduino:

```markdown
![Circuit diagram](circuit.png)

// Declare the pin numbers of the switches and LEDs as constants
const int switch1 = 2;
const int switch2 = 3;
const int led1 = 4;
const int led2 = 5;

void setup() {
  // Set the switches as inputs and the LEDs as outputs
  pinMode(switch1, INPUT);
  pinMode(switch2, INPUT);
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
}

void loop() {
  // Read the state of the switches
  int state1 = digitalRead(switch1);
  int state2 = digitalRead(switch2);

  // Write the corresponding state of the LEDs
  if (state1 == HIGH && state2 == LOW) {
    // Switch 1 is closed and switch 2 is open
    digitalWrite(led1, HIGH); // Turn on LED 1
    digitalWrite(led2, LOW); // Turn off LED 2
  }
  else if (state1 == LOW && state2 == HIGH) {
    // Switch 1 is open and switch 2 is closed
    digitalWrite(led1, LOW); // Turn off LED 1
    digitalWrite(led2, HIGH); // Turn on LED 2
  }
  else {
    // Both switches are either open or closed
    digitalWrite(led1, LOW); // Turn off both LEDs
    digitalWrite(led2, LOW);
  }
}
```