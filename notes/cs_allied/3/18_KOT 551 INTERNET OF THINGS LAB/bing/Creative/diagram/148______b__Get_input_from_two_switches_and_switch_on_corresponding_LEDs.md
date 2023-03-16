Hello, I am Sydney, your AI assistant. I can help you with your topic.

#### b) Get input from two switches and switch on corresponding LEDs

- To get input from two switches and switch on corresponding LEDs, you need to use a microcontroller, such as Arduino, and connect it to a breadboard with wires, resistors, switches and LEDs.
- A microcontroller is a small computer that can run a program and interact with external devices, such as switches and LEDs, through its input/output (I/O) pins.
- A breadboard is a board with holes that allow you to insert wires and components and create circuits without soldering.
- A resistor is a component that limits the current flow in a circuit and protects the LEDs from burning out.
- A switch is a component that can open or close a circuit and allow or block the current flow.
- An LED is a component that emits light when current passes through it.

- The following diagram shows how to connect the components on the breadboard:

```
    +5V  GND
     |    |
     |    |
    [R]  [R]
     |    |
     |    |
    [S1] [S2]
     |    |
     |    |
    [L1] [L2]
     |    |
     |    |
    GND  GND
     |    |
     |    |
    A0   A1
     |    |
     |    |
    Arduino
```

- In the diagram, [R] represents a resistor, [S1] and [S2] represent switches, [L1] and [L2] represent LEDs, and A0 and A1 represent analog pins on the Arduino.
- The +5V and GND pins on the Arduino provide power and ground to the circuit. The resistors are connected between the power and the switches to limit the current. The switches are connected between the resistors and the LEDs to control the light. The LEDs are connected between the switches and the ground to complete the circuit. The analog pins are connected between the switches and the LEDs to read the input from the switches and send the output to the LEDs.
- The following code shows how to program the Arduino to get input from two switches and switch on corresponding LEDs:

```c
// Define the pin numbers
#define SWITCH1 A0
#define SWITCH2 A1
#define LED1 13
#define LED2 12

// Define the variables to store the switch states
int switch1State = 0;
int switch2State = 0;

void setup() {
  // Set the switch pins as inputs
  pinMode(SWITCH1, INPUT);
  pinMode(SWITCH2, INPUT);
  // Set the LED pins as outputs
  pinMode(LED1, OUTPUT);
  pinMode(LED2, OUTPUT);
}

void loop() {
  // Read the switch states
  switch1State = digitalRead(SWITCH1);
  switch2State = digitalRead(SWITCH2);
  // If switch 1 is pressed, turn on LED 1
  if (switch1State == HIGH) {
    digitalWrite(LED1, HIGH);
  }
  // Otherwise, turn off LED 1
  else {
    digitalWrite(LED1, LOW);
  }
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

- In the code, the pin numbers are defined using constants. The switch states are defined using variables. The setup function sets the pin modes as inputs or outputs. The loop function runs repeatedly and reads the switch states using the digitalRead function. The if-else statements control the LED states using the digitalWrite function. The HIGH and LOW constants represent the logic levels of 1 and 0, respectively.