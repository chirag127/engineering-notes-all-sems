### Differentiator

- A differentiator is a circuit that performs the mathematical operation of differentiation, that is, it produces an output voltage that is proportional to the rate of change of the input voltage.
- A differentiator can be constructed using an operational amplifier (op-amp) with a capacitor and a resistor in the feedback loop.
- The circuit diagram of a differentiator is shown below:

```
    +Vcc
     |
     |
    +|\
     | \    Rf
Vi --|  \____/\/\/\____ Vout
     |  /
    -| /
     |/
     |
    -Vcc
     |
     |
    C1
     |
     |
    GND
```

- The input voltage Vi is applied to the inverting terminal of the op-amp through a capacitor C1. The non-inverting terminal is grounded. The output voltage Vout is taken from the output terminal of the op-amp through a resistor Rf.
- The capacitor C1 blocks any DC component of the input voltage and allows only the AC component to pass through. The resistor Rf provides negative feedback to the op-amp and stabilizes the circuit.
- The output voltage Vout is given by the formula:

```
Vout = -Rf * C1 * dVi/dt
```

- where dVi/dt is the derivative of the input voltage with respect to time.
- The negative sign indicates that the output voltage is 180 degrees out of phase with the input voltage.
- The output voltage is proportional to the product of the feedback resistor Rf, the input capacitor C1, and the rate of change of the input voltage dVi/dt.
- The differentiator can be used to perform various functions such as edge detection, pulse shaping, frequency modulation, and waveform generation.