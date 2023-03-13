Kirchhoff's laws are a set of laws that quantify how current flows through a circuit and how voltage varies around a loop in a circuit. They are used to govern the conservation of charge and energy in standard electrical circuits.

There are two Kirchhoff's laws:

- Kirchhoff's current law (KCL): This law states that the sum of currents entering a node is equal to the sum of currents leaving the node. In other words, the algebraic sum of currents at a junction is zero. This law is based on the principle of conservation of charge.

- Kirchhoff's voltage law (KVL): This law states that the sum of voltages around a closed loop is equal to zero. In other words, the algebraic sum of potential differences in a closed circuit is zero. This law is based on the principle of conservation of energy.

##### 1. Kirchhoff‟s laws

The following diagram illustrates a simple circuit with two resistors and a battery. The current and voltage values are labeled on the diagram.

```
    +---R1---+---R2---+
    |        |        |
    |        |        |
    |        |        |
    |        |        |
    +--------+--------+
    |                 |
    |                 |
    |                 |
    |                 |
    +--------+--------+
    |        |        |
    |        |        |
    |        |        |
    |        |        |
    +---+ +--+---+ +--+
        | |       | |
        | |       | |
        | |       | |
        | |       | |
        +-+       +-+
         +         -
        Vb        Vb
```

To apply KCL, we can choose any node in the circuit and write the equation for the currents. For example, if we choose the node at the top right corner, we can write:

`I1 - I2 - I3 = 0`

where I1 is the current entering the node from the battery, I2 is the current leaving the node through R1, and I3 is the current leaving the node through R2.

To apply KVL, we can choose any closed loop in the circuit and write the equation for the voltages. For example, if we choose the loop that goes clockwise from the positive terminal of the battery, we can write:

`Vb - V1 - V2 - Vb = 0`

where Vb is the voltage of the battery, V1 is the voltage drop across R1, and V2 is the voltage drop across R2.

Using Ohm's law, we can relate the current and voltage of each resistor as:

`V1 = I2 * R1`

`V2 = I3 * R2`

By substituting these expressions into the KVL equation, we can solve for the current I1 as:

`I1 = (Vb * (R1 + R2)) / (R1 * R2)`

By using KCL, we can also find the currents I2 and I3 as:

`I2 = I1 * R2 / (R1 + R2)`

`I3 = I1 * R1 / (R1 + R2)`

These are the basic steps to apply Kirchhoff's laws to a circuit. For more complex circuits, we may need to write more equations and use methods such as matrix inversion or nodal analysis to solve them.