# Get input from two switches and switch on corresponding LEDs

- This topic is about how to use two switches and two LEDs to create a simple logic circuit.
- A switch is a device that can open or close an electrical circuit, allowing current to flow or stop. A LED (light-emitting diode) is a device that emits light when current passes through it.
- To get input from two switches and switch on corresponding LEDs, we need to connect them in a certain way using wires, resistors, and a power source.
- The following diagram shows one possible way to connect the switches and LEDs:

```
    +V
    |
    R
    |
    o----o S1 o----o LED1 o----o
    |    |    |    |      |    |
    |    |    |    R      R    |
    |    |    |    |      |    |
    o----o S2 o----o LED2 o----o
    |    |    |    |      |    |
    |    |    |    R      R    |
    |    |    |    |      |    |
    o----o----o----o------o----o
    |
   GND
```

- In this diagram, +V and GND are the positive and negative terminals of the power source, R is a resistor, S1 and S2 are the switches, and LED1 and LED2 are the LEDs. The o symbols represent the connection points of the wires.
- The resistors are used to limit the current flowing through the LEDs and prevent them from burning out. The value of the resistors depends on the voltage of the power source and the specifications of the LEDs.
- The switches are connected in parallel, meaning that they can operate independently of each other. The LEDs are connected in series with the switches, meaning that they will only light up when the corresponding switch is closed.
- The logic of this circuit is as follows:

  - If both switches are open, no current flows and both LEDs are off.
  - If switch S1 is closed and switch S2 is open, current flows through LED1 and it lights up, while LED2 remains off.
  - If switch S1 is open and switch S2 is closed, current flows through LED2 and it lights up, while LED1 remains off.
  - If both switches are closed, current flows through both LEDs and they both light up.

- This circuit can be used to demonstrate the concept of Boolean logic, which is the basis of digital electronics. Each switch can represent a binary input (0 or 1), and each LED can represent a binary output (0 or 1). The output depends on the combination of the inputs, according to a logic function.
- In this case, the logic function is OR, which means that the output is 1 if either or both of the inputs are 1, and 0 otherwise. The truth table for this function is:

| S1 | S2 | LED1 | LED2 |
|----|----|------|------|
| 0  | 0  | 0    | 0    |
| 0  | 1  | 0    | 1    |
| 1  | 0  | 1    | 0    |
| 1  | 1  | 1    | 1    |

- Other logic functions, such as AND, NOT, XOR, etc., can be implemented by using different arrangements of switches and LEDs, or by adding other components, such as transistors, diodes, etc.