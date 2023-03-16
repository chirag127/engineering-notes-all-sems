# Get input from two switches and switch on corresponding LEDs

- This topic is about how to use two switches and two LEDs to create a simple logic circuit.
- A switch is a device that can open or close an electrical circuit, allowing or blocking the flow of current.
- An LED (light-emitting diode) is a device that emits light when current passes through it.
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
- The o symbols represent the nodes where the wires are connected, and the | symbols represent the wires themselves.
- The switches and LEDs are connected in parallel, meaning that they have two nodes in common.
- The resistors are connected in series with the LEDs, meaning that they share one node with the LED and one node with the power source.
- The resistors are used to limit the current flowing through the LEDs, preventing them from burning out.
- The switches are normally open, meaning that they do not allow current to flow unless they are pressed.
- When a switch is pressed, it closes the circuit and allows current to flow from the power source, through the resistor, through the LED, and back to the power source.
- This causes the LED to light up.
- When the switch is released, it opens the circuit and stops the current from flowing.
- This causes the LED to turn off.
- The following table shows the possible states of the switches and LEDs:

| S1 | S2 | LED1 | LED2 |
|----|----|------|------|
| 0  | 0  |  0   |  0   |
| 0  | 1  |  0   |  1   |
| 1  | 0  |  1   |  0   |
| 1  | 1  |  1   |  1   |

- In this table, 0 means off and 1 means on.
- The state of the LEDs depends on the state of the switches.
- If both switches are off, both LEDs are off.
- If one switch is on and the other is off, the corresponding LED is on and the other is off.
- If both switches are on, both LEDs are on.
- This way, we can get input from two switches and switch on corresponding LEDs.