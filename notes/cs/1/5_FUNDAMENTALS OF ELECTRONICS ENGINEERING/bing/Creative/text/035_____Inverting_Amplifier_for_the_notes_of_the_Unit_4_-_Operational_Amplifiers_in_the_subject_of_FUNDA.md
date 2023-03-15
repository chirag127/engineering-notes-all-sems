### Inverting Amplifier

- An inverting amplifier is a type of operational amplifier circuit that produces an output signal that is 180 degrees out of phase with the input signal   .
- An inverting amplifier uses a negative feedback loop to control the gain and stability of the circuit .
- An inverting amplifier consists of an operational amplifier, an input resistor (Ri), and a feedback resistor (Rf)  . See the diagram below:

```
    +Vcc
     |
     |
    | |
    | | Rf
    | |
     |
     |----------------------+
     |                      |
     |                      |
     |                      |
     |                      |
     |                      |
     |                      |
     |                      |
     |                      |
     |                      |
     |                      |
     |                      |
     |                      |
     |                      |
     |                      |
     |                      |
     |                      |
     |                      |
     +                      +
     |                      |
     |                      |
     |                      |
     |                      |
     |                      |
     |                      |
     |                      |
     |                      |
     |                      |
     |                      |
     |                      |
    | |                     |
    | | Ri                  |
    | |                     |
     |                      |
     |                      |
     |                      |
     |                      |
     |                      |
     |                      |
     |                      |
     |                      |
     |                      |
     |                      |
     |                      |
     |                      |
     |                      |
     +                      +
     |                      |
     |                      |
     |                      |
     |                      |
     |                      |
     |                      |
     |                      |
     |                      |
     |                      |
     |                      |
     |                      |
     |                      |
     |                      |
    Vin                     Vout
     |                      |
     |                      |
     |                      |
     |                      |
     |                      |
     |                      |
     |                      |
     |                      |
     |                      |
    GND                     GND
```

- The input signal (Vin) is applied to the inverting input terminal (-) of the op-amp, while the non-inverting input terminal (+) is connected to the ground  .
- The output signal (Vout) is fed back to the inverting input terminal (-) through the feedback resistor (Rf)  .
- The voltage at the inverting input terminal (-) is equal to the voltage at the non-inverting input terminal (+), which is zero . This is called the virtual ground principle.
- The current flowing through the input resistor (Ri) is equal to the current flowing through the feedback resistor (Rf), since no current enters or leaves the op-amp terminals . This is called the current rule.
- The voltage gain (Av) of the inverting amplifier is the ratio of the output voltage (Vout) to the input voltage (Vin)  . It can be derived from the virtual ground principle and the current rule as follows:

```
Av = Vout / Vin
   = - (Rf / Ri) * Vin / Vin
   = - Rf / Ri
```

- The negative sign indicates that the output signal is inverted with respect to the input signal  .
- The voltage gain (Av) of the inverting amplifier depends only on the values of the input resistor (Ri) and the feedback resistor (Rf), and not on the open loop gain (Avo) of the op-amp .
- The input impedance (Zin) of the inverting amplifier is the ratio of the input voltage (Vin) to the input current (Iin) . It can be derived from the current rule as follows:

```
Zin = Vin / Iin
    = Vin / (Vin / Ri)
    = Ri
```

- The input impedance (Zin) of the inverting amplifier is equal to the value of the input resistor (Ri) .
- The output impedance (Zout) of the