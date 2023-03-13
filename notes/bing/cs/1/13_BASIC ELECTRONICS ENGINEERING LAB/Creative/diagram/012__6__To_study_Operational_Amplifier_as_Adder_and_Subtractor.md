An operational amplifier (op-amp) is a DC-coupled high-gain electronic voltage amplifier with a differential input and, usually, a single-ended output. It can be used to perform mathematical operations such as addition, subtraction, integration, and differentiation. An op-amp as an adder circuit can produce an output voltage that is the sum of the input voltages. An op-amp as a subtractor circuit can produce an output voltage that is the difference of the input voltages.

The following diagram illustrates the basic architecture of an op-amp as an adder and subtractor circuit using ASCII art:

```
    +Vcc
     |
     |
    | |
    | | Rf
    | |
     |
     |     +------+
     +-----|      |
           |  OP  |---- Vo
     +-----|      |
     |     +------+
    | |
    | | R1
    | |
     |
     |     Vin1
     |
    GND

    -Vcc
     |
     |
    | |
    | | R2
    | |
     |
     |     Vin2
     |
    GND
```

In this circuit, the op-amp is configured as an inverting amplifier with a feedback resistor Rf and two input resistors R1 and R2. The output voltage Vo is given by:

Vo = -Rf/R1 * Vin1 - Rf/R2 * Vin2

This equation shows that the output voltage is the weighted sum of the negative input voltages. If Rf = R1 = R2, then the output voltage is simply the negative sum of the input voltages. This is the op-amp as an adder circuit.

To make the op-amp as a subtractor circuit, we can swap the input voltages Vin1 and Vin2. Then the output voltage becomes:

Vo = -Rf/R2 * Vin1 - Rf/R1 * Vin2

This equation shows that the output voltage is the weighted difference of the negative input voltages. If Rf = R1 = R2, then the output voltage is simply the negative difference of the input voltages. This is the op-amp as a subtractor circuit.