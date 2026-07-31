# Get input from two switches and switch on corresponding LEDs

- To get input from two switches and switch on corresponding LEDs, we need to use a microcontroller, such as Arduino, and connect it to the switches and LEDs using wires and resistors.
- A switch is a device that can be used to control the flow of electricity in a circuit. When the switch is closed, it allows current to pass through. When the switch is open, it stops the current from flowing.
- An LED (light-emitting diode) is a device that emits light when current passes through it. LEDs have two terminals: an anode (+) and a cathode (-). The anode must be connected to a higher voltage than the cathode for the LED to light up.
- A resistor is a device that limits the amount of current in a circuit. Resistors have a fixed value of resistance, measured in ohms (Ω). Resistors are used to protect the LEDs from getting too much current and burning out.
- To connect the switches and LEDs to the Arduino, we need to use the digital pins on the Arduino board. The digital pins can be configured as either inputs or outputs using the pinMode() function in the Arduino code. Inputs can read the state of a switch (HIGH or LOW) and outputs can control the state of an LED (ON or OFF).
- The circuit diagram for this project is shown below:

```
+5V  +---/ ---+  +---/ ---+  +5V
    |        |  |        |
    |        |  |        |
    |       [ ] |       [ ]  220Ω resistors
    |       [ ] |       [ ] 
    |        |  |        |
    |        |  |        |
    |        +--+--+     +--+--+
    |           |           |
    |           |           |
    |          LED1        LED2
    |           |           |
    |           |           |
    |        +--+--+     +--+--+
    |        |  |        |  |
    |       [ ] |       [ ] |  10kΩ resistors
    |       [ ] |       [ ] |
    |        |  |        |  |
    |        |  |        |  |
    |        |  +--------+  |
    |        |              |
    |        +--------------+
    |                       |
    |                       |
    +-----------------------+
              GND
```

- The code for this project is shown below:

```c
// Define the pin numbers for the switches and LEDs
#define SWITCH1 2
#define SWITCH2 3
#define LED1 4
#define LED2 5

// Setup the pin modes for the switches and LEDs
void setup() {
  pinMode(SWITCH1, INPUT); // Set SWITCH1 as an input
  pinMode(SWITCH2, INPUT); // Set SWITCH2 as an input
  pinMode(LED1, OUTPUT); // Set LED1 as an output
  pinMode(LED2, OUTPUT); // Set LED2 as an output
}

// Loop the code to read the switch states and control the LEDs
void loop() {
  // Read the state of SWITCH1 and store it in a variable
  int switch1State = digitalRead(SWITCH1);
  // Read the state of SWITCH2 and store it in a variable
  int switch2State = digitalRead(SWITCH2);
  // If SWITCH1 is closed (HIGH), turn on LED1
  if (switch1State == HIGH) {
    digitalWrite(LED1, HIGH); // Set LED1 to ON
  }
  // Otherwise, turn off LED1
  else {
    digitalWrite(LED1, LOW); // Set LED1 to OFF
  }
  // If SWITCH2 is closed (HIGH), turn on LED2
  if (switch2State == HIGH) {
    digitalWrite(LED2, HIGH); // Set LED2 to ON
  }
  // Otherwise, turn off LED2
  else {
    digitalWrite(LED2, LOW); // Set LED2 to OFF
  }
}
```