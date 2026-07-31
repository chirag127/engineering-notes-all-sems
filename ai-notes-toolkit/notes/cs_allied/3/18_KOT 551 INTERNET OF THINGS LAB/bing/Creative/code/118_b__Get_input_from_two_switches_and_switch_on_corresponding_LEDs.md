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
    o----o----o----o----o-o----o
    |
   GND
```

- In this diagram, +V and GND are the positive and negative terminals of the power source, R is a resistor, S1 and S2 are the switches, and LED1 and LED2 are the LEDs.
- The switches and LEDs are connected in parallel, meaning that they have two common nodes (points of connection).
- The resistors are used to limit the current flowing through the LEDs and prevent them from burning out.
- The logic of this circuit is as follows:

  - If both switches are open (off), no current flows through the circuit and both LEDs are off.
  - If switch S1 is closed (on) and switch S2 is open (off), current flows through the upper branch of the circuit and LED1 is on, while LED2 is off.
  - If switch S1 is open (off) and switch S2 is closed (on), current flows through the lower branch of the circuit and LED2 is on, while LED1 is off.
  - If both switches are closed (on), current flows through both branches of the circuit and both LEDs are on.

- This circuit can be used to demonstrate the concept of Boolean logic, where each switch represents a binary input (0 or 1) and each LED represents a binary output (0 or 1).
- The output of each LED depends on the combination of the inputs of the switches, according to the following truth table:

| S1 | S2 | LED1 | LED2 |
|----|----|------|------|
| 0  | 0  |  0   |  0   |
| 0  | 1  |  0   |  1   |
| 1  | 0  |  1   |  0   |
| 1  | 1  |  1   |  1   |

- The truth table shows that the output of each LED is equal to the input of the corresponding switch, which means that this circuit implements the identity function.
- The identity function is a function that returns the same value as its argument, for example, f(x) = x.
- The identity function is also an example of a unary function, which is a function that takes one argument and returns one output.
- Other examples of unary functions are the NOT function, which returns the opposite value of its argument, for example, NOT(0) = 1, and the constant function, which returns the same value regardless of its argument, for example, f(x) = 0.