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
    o----o S1 o----o LED1 o----o GND
    |    |    |    |      |    |
    R    |    R    |      R    |
    |    |    |    |      |    |
    o----o S2 o----o LED2 o----o GND
```

- In this diagram, +V is the positive terminal of the power source, GND is the ground or negative terminal, R is a resistor, S1 and S2 are the switches, and LED1 and LED2 are the LEDs.
- The resistors are used to limit the current and protect the LEDs from burning out.
- The switches and LEDs are connected in parallel, meaning that they have two common points: one connected to +V and one connected to GND.
- When a switch is closed, it completes the circuit and allows current to flow through the LED connected to it, making it light up.
- When a switch is open, it breaks the circuit and stops current from flowing through the LED connected to it, making it turn off.
- Therefore, the logic of this circuit is as follows:

```
S1 | S2 | LED1 | LED2
---------------------
 0 |  0 |   0  |   0
 0 |  1 |   0  |   1
 1 |  0 |   1  |   0
 1 |  1 |   1  |   1
```

- Where 0 means open or off, and 1 means closed or on.
- This logic is equivalent to the OR operation, meaning that LED1 or LED2 will be on if S1 or S2 is closed, and both will be on if both are closed.
- To test this circuit, we can use a breadboard, a device that allows us to easily insert and remove wires and components without soldering.
- The following image shows how to set up the circuit on a breadboard:

![Breadboard circuit](https://i.imgur.com/3s0yj8Z.png)

- The red wire connects +V to the positive rail of the breadboard, and the black wire connects GND to the negative rail.
- The resistors are inserted across the gap in the middle of the breadboard, and the switches and LEDs are inserted on either side of the resistors.
- The wires connect the common points of the switches and LEDs to the positive and negative rails of the breadboard.
- To operate the circuit, we can use a battery or a power supply as the power source, and connect it to the red and black wires.
- Then, we can toggle the switches and observe the LEDs.