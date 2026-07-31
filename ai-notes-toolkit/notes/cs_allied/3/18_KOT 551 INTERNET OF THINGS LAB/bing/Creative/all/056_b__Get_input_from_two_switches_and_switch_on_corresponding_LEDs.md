# Get input from two switches and switch on corresponding LEDs

- This topic is about how to use two switches and two LEDs to create a simple logic circuit.
- A switch is a device that can open or close an electrical circuit, allowing current to flow or stop.
- A LED (light-emitting diode) is a device that emits light when current passes through it.
- To get input from two switches and switch on corresponding LEDs, we need to connect them in a certain way using wires, resistors, and a power source.
- The following diagram shows one possible way to connect the switches and LEDs:

```
    +V
    |
    R
    |
    o----o S1 o----o LED1 o----o
    |    |    |    |      |    |
    |    |    |    R      |    |
    |    |    |    |      |    |
    o----o S2 o----o LED2 o----o
    |    |    |    |      |    |
    |    |    |    R      |    |
    |    |    |    |      |    |
    o----o----o----o------o----o
    |
   GND
```

- In this diagram, +V and GND are the positive and negative terminals of the power source, R is a resistor, S1 and S2 are the switches, and LED1 and LED2 are the LEDs.
- The o symbols represent the nodes where the wires are connected.
- The switches and LEDs are connected in parallel, meaning that they have two common nodes each.
- The resistors are connected in series with the LEDs, meaning that they limit the current that flows through them and protect them from burning out.
- The logic of this circuit is as follows:

  - If both switches are open, no current flows through the circuit and both LEDs are off.
  - If switch S1 is closed and switch S2 is open, current flows from +V to GND through S1, LED1, and their resistors, and LED1 turns on. LED2 remains off because no current flows through it.
  - If switch S1 is open and switch S2 is closed, current flows from +V to GND through S2, LED2, and their resistors, and LED2 turns on. LED1 remains off because no current flows through it.
  - If both switches are closed, current flows from +V to GND through both switches, both LEDs, and their resistors, and both LEDs turn on.

- This circuit can be used to demonstrate the concept of Boolean logic, where each switch represents a binary input (0 or 1) and each LED represents a binary output (0 or 1).
- The output of each LED depends on the combination of the inputs of the switches, according to the following truth table:

| S1 | S2 | LED1 | LED2 |
|----|----|------|------|
| 0  | 0  |  0   |  0   |
| 0  | 1  |  0   |  1   |
| 1  | 0  |  1   |  0   |
| 1  | 1  |  1   |  1   |

- The truth table shows that the output of each LED is equal to the input of the corresponding switch, regardless of the input of the other switch.
- This means that the circuit implements two independent identity functions, where the output is the same as the input.
- In Boolean algebra, this can be written as:

  - LED1 = S1
  - LED2 = S2

- This circuit can be modified to implement other logic functions, such as AND, OR, XOR, etc., by changing the way the switches and LEDs are connected.