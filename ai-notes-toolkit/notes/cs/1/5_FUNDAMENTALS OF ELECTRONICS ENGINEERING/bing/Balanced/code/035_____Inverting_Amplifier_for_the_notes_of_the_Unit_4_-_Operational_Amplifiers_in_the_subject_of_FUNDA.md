### Inverting Amplifier

- An inverting amplifier is a type of operational amplifier circuit that produces an output signal that is out of phase with respect to its input signal by 180 degrees .
- This means that if the input signal is positive, then the output signal will be negative and vice versa .
- An inverting amplifier can be used to amplify or invert a signal, depending on the values of the resistors in the circuit .
- The basic circuit diagram of an inverting amplifier is shown below:

```
    +Vcc
     |
     |
    | |
    | | Rf
    | |
     |
     |-----------------o Vout
     |
     |      |
   --|+     |    Op-amp
Vin o-|-  --|-
     |      |
     |      |
    | |
    | | Ri
    | |
     |
     |
    -Vcc
```

- The input signal is applied to the inverting input terminal (-) of the op-amp through a resistor Ri .
- The non-inverting input terminal (+) of the op-amp is connected to the ground .
- The output terminal of the op-amp is connected to the inverting input terminal through a feedback resistor Rf .
- The output voltage Vout is taken across Rf .
- The voltage gain of the inverting amplifier is given by the formula :

```
A = -Rf/Ri
```

- The negative sign indicates that the output signal is inverted with respect to the input signal .
- The voltage gain can be increased or decreased by changing the values of Rf and Ri .
- The input impedance of the inverting amplifier is equal to Ri .
- The output impedance of the inverting amplifier is very low, as the op-amp has a high open-loop gain .
- Some applications of the inverting amplifier are :
  - Signal inversion
  - Signal amplification
  - Voltage subtraction
  - Summing amplifier
  - Differential amplifier
  - Integrator
  - Differentiator
  - Active filter
  - Oscillator
  - Comparator