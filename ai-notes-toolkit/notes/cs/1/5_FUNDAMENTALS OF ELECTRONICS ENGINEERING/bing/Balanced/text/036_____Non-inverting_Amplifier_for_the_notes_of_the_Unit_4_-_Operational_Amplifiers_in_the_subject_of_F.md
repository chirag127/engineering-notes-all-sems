### Non-inverting Amplifier

- A non-inverting amplifier is an op-amp circuit configuration that produces an amplified output signal and this output signal of the non-inverting op-amp is in-phase with the applied input signal .
- In other words, a non-inverting amplifier behaves like a voltage follower circuit.
- The basic circuit diagram of a non-inverting amplifier is shown below:

```
    +Vcc
     |
     |
     |
    | |
    | | Rf
    | |
     |
     |-----------------+
     |                 |
     |                 |
     |                 |
     |                 |
     |                 |
     |                 |
     |                 |
     |                 |
     |                 |
     |                 |
     |                 |
     |                 |
     |                 |
     |                 |
     |                 |    +Vout
     |                 |------+
     |                 |      |
     |                 |      |
     |                 |      |
     |                 |      |
     |                 |      |
     |                 |      |
     |                 |      |
     |                 |      |
     |                 |      |
     |                 |      |
     |                 |      |
     |                 |      |
     |                 |      |
     |                 |      |
     |                 |      |
     |                 |      |
     |                 |      |
     |                 |      |
     |                 |      |
     |                 |      |
    +|                 |-+    |
    -|                 |-+    |
     |                 |      |
     |                 |      |
     |                 |      |
     |                 |      |
     |                 |      |
     |                 |      |
     |                 |      |
     |                 |      |
     |                 |      |
     |                 |      |
     |                 |      |    +Vin
     |                 |      +------+
     |                 |             |
     |                 |             |
     |                 |             |
     |                 |             |
     |                 |             |
     |                 |             |
     |                 |             |
     |                 |             |
     |                 |             |
     |                 |             |
     |                 |             |
    | |               | |            |
    | | Ri            | | Rg         |
    | |               | |            |
     |                 |             |
     |                 |             |
     |                 |             |
     |                 |             |
     |                 |             |
     |                 |             |
     |                 |             |
     |                 |             |
     |                 |             |
     |                 |             |
     |                 |             |
     |                 |             |
    -Vee               |             |
                       |             |
                       |             |
                       |             |
                       |             |
                       |             |
                       |             |
                       |             |
                       |             |
                       |             |
                       |             |
                       |             |
                       |             |
                       |             |
                       |             |
                       |             |
                       |             |
                       +-------------+
```

- The input signal is applied to the non-inverting (+) input terminal of the op-amp and the output signal is taken from the output terminal of the op-amp .
- The feedback resistor Rf is connected between the output and the inverting (-) input terminal of the op-amp .
- The input resistor Ri is connected between the inverting input terminal and the ground .
- The resistor Rg is connected between the non-inverting input terminal and the ground to balance the input bias currents .
- The voltage gain of the non-inverting amplifier is given by the formula   :

```
    Av = 1 + (Rf / Ri)
```

- Where Av is the voltage gain, Rf is the feedback resistor, and Ri is the input resistor.
- The voltage gain of the non-inverting amplifier is always greater than or equal to 1   .
- The input impedance of the non-inverting amplifier is very high, which means that it draws very little current from the input source  .
- The output impedance of the non-inverting amplifier is very low