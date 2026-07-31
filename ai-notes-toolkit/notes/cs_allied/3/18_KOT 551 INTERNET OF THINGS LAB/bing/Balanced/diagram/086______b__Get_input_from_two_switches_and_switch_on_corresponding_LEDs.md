Hello, I am Sydney, your AI assistant. I can help you with your topic.

#### b) Get input from two switches and switch on corresponding LEDs

- To get input from two switches and switch on corresponding LEDs, you need to use a microcontroller, such as Arduino, and connect it to a breadboard with wires, resistors, switches and LEDs.
- A microcontroller is a small computer that can run a program and interact with external devices, such as switches and LEDs, through its input/output (I/O) pins.
- A breadboard is a board with holes that can hold wires and components and create electrical connections between them.
- A resistor is a component that limits the current flow in a circuit and protects the LEDs from burning out.
- A switch is a component that can open or close a circuit and control the flow of electricity.
- An LED is a component that emits light when current passes through it.

- The following diagram shows how to connect the components on the breadboard:

```
    +5V    GND
    |      |
    |      |
    |      |
    |      |
    |      |
    |      |
    |      |
    |      |
    |      |
    |      |
    |      |
    |      |
    |      |
    |      |
    |      |
    |      |
    |      |
    |      |
    |      |
    |      |
    |      |
    |      |
    |      |
   +|+    -|-    LED1
    |      |
    |      |
    |      |
    |      |
    |      |
    |      |
    |      |
    |      |
    |      |
    |      |
   +|+    -|-    LED2
    |      |
    |      |
    |      |
    |      |
    |      |
    |      |
    |      |
    |      |
    |      |
    |      |
   +|+    -|-    Switch1
    |      |
    |      |
    |      |
    |      |
    |      |
    |      |
    |      |
    |      |
    |      |
    |      |
   +|+    -|-    Switch2
    |      |
    |      |
    |      |
    |      |
    |      |
    |      |
    |      |
    |      |
    |      |
    |      |
   +|+    -|-    Resistor1
    |      |
    |      |
    |      |
    |      |
    |      |
    |      |
    |      |
    |      |
    |      |
    |      |
   +|+    -|-    Resistor2
    |      |
    |      |
    |      |
    |      |
    |      |
    |      |
    |      |
    |      |
    |      |
    |      |
    +------+    Arduino
    |      |
    |      |
    |      |
    |      |
    |      |
    |      |
    |      |
    |      |
    |      |
    |      |
    |      |
    |      |
    |      |
    |      |
    |      |
    |      |
    |      |
    |      |
    |      |

```

- The following table shows how to connect the wires between the components and the Arduino pins:

| Component | Arduino Pin |
|-----------|-------------|
| LED1      | 13          |
| LED2      | 12          |
| Switch1   | 2           |
| Switch2   | 3           |
| Resistor1 | 5V          |
| Resistor2 | 5V          |
| GND       | GND         |

- The following code shows how to program the Arduino to read the input from the switches and turn on the corresponding LEDs:

```c
// Define the pin numbers for the LEDs and switches
#define LED1 13
#define LED2 12
#define SWITCH1 2
#define SWITCH2 3

// Set up the input and output pins
void setup() {
  // Set the LED pins as output
  pinMode(LED1, OUTPUT);
  pinMode(LED2, OUTPUT);
  // Set the switch pins as input with pull-up resistors
  pinMode(SWITCH1, INPUT_PULLUP);
  pinMode(SWITCH2, INPUT_PULLUP);
}

// Loop the program and check the switch states
void loop() {
  // Read the switch values
  int switch1 = digitalRead(SWITCH1);
  int switch2 = digitalRead(SWITCH2);
  // Turn on the LED

```
