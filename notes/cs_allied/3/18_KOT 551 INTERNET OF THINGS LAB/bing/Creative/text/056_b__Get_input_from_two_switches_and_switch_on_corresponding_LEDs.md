# Get input from two switches and switch on corresponding LEDs

- This topic is about how to use two switches and two LEDs to create a simple logic circuit.
- A switch is a device that can open or close an electrical circuit, allowing current to flow or stop.
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
    o----o----o----o----o GND
```

- In this diagram, +V is the positive terminal of the power source, GND is the ground or negative terminal, R is a resistor, S1 and S2 are switches, and LED1 and LED2 are LEDs.
- The o symbols represent the nodes or junctions where wires are connected.
- The switches and LEDs are connected in parallel, meaning they have two common nodes each.
- The resistors are connected in series with the LEDs, meaning they have one common node each.
- The resistors limit the current flowing through the LEDs, preventing them from burning out.
- The switches control the current flowing through the LEDs, turning them on or off.
- When a switch is closed, it creates a closed circuit, allowing current to flow from +V to GND through the resistor and the LED.
- When a switch is open, it creates an open circuit, stopping current from flowing through the resistor and the LED.
- The following table shows the possible states of the switches and LEDs:

| S1 | S2 | LED1 | LED2 |
|----|----|------|------|
| Open | Open | Off | Off |
| Open | Closed | Off | On |
| Closed | Open | On | Off |
| Closed | Closed | On | On |

- This table shows that the LEDs are switched on corresponding to the switches, meaning LED1 is on when S1 is closed, and LED2 is on when S2 is closed.
- This logic circuit can be used to demonstrate the concept of Boolean algebra, where switches represent binary variables (0 or 1), and LEDs represent logical outputs (false or true).
- For example, the table can be interpreted as:

| S1 | S2 | LED1 | LED2 |
|----|----|------|------|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 1 | 1 |

- This means that LED1 is equal to S1, and LED2 is equal to S2, in terms of Boolean logic.
- This logic circuit can also be used to create different logic functions, such as AND, OR, XOR, etc., by changing the way the switches and LEDs are connected.
- For example, the following diagram shows how to create an AND function, where LED1 is on only when both S1 and S2 are closed:

```
    +V
    |
    R
    |
    o----o S1 o----o
    |    |    |    |
    |    |    |    R
    |    |    |    |
    o----o S2 o----o LED1 o----o
    |    |    |    |      |    |
    |    |    |    R      |    |
    |    |    |    |      |    |
    o----o----o----o----o GND
```

- The following table shows the states of the switches and LED1 for the AND function:

| S1 | S2 | LED1 |
|----|----|------|
| Open | Open | Off |
| Open | Closed | Off |
| Closed | Open | Off |
| Closed | Closed | On |

- This means that LED1 is equal to S1 AND S2, in terms of Boolean logic.