# Get input from two switches and switch on corresponding LEDs

- This topic is about how to use two switches and two LEDs to create a simple logic circuit that can perform basic operations such as AND, OR, XOR, etc.
- To get input from two switches, we need to connect them to two digital pins on an Arduino board, such as pin 2 and pin 3. We also need to enable the internal pull-up resistors for these pins, so that they will read HIGH when the switches are open and LOW when they are closed.
- To switch on corresponding LEDs, we need to connect them to two other digital pins on the Arduino board, such as pin 8 and pin 9. We also need to add current-limiting resistors in series with the LEDs, to prevent them from burning out.
- The code for this project is as follows:

```c
// Define the pin numbers for the switches and LEDs
const int switch1 = 2;
const int switch2 = 3;
const int led1 = 8;
const int led2 = 9;

void setup() {
  // Set the switch pins as inputs with pull-up resistors
  pinMode(switch1, INPUT_PULLUP);
  pinMode(switch2, INPUT_PULLUP);
  // Set the LED pins as outputs
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
}

void loop() {
  // Read the state of the switches
  int state1 = digitalRead(switch1);
  int state2 = digitalRead(switch2);
  // Perform a logic operation on the switch states and write the result to the LEDs
  // For example, this is an AND operation
  digitalWrite(led1, state1 && state2);
  // For example, this is an OR operation
  digitalWrite(led2, state1 || state2);
  // You can also try other operations such as XOR, NAND, NOR, etc.
}
```
- The circuit diagram for this project is as follows:

```markdown
![Circuit diagram](circuit.png)
```

- The circuit diagram shows how to connect the switches and LEDs to the Arduino board using a breadboard and jumper wires. The switches are connected to pins 2 and 3, and the LEDs are connected to pins 8 and 9, with 220 ohm resistors in series. The Arduino board is powered by a USB cable or a battery.

- The expected output of this project is as follows:

```markdown
| Switch 1 | Switch 2 | LED 1 | LED 2 |
|----------|----------|-------|-------|
|    0     |    0     |   0   |   0   |
|    0     |    1     |   0   |   1   |
|    1     |    0     |   0   |   1   |
|    1     |    1     |   1   |   1   |
```

- The output table shows the state of the LEDs for each combination of the switch states. LED 1 performs an AND operation, and LED 2 performs an OR operation. You can change the code to perform other operations and see the results on the LEDs.