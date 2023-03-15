### Inverting Amplifier

- An inverting amplifier is a type of operational amplifier circuit that produces an output signal that is 180 degrees out of phase with the input signal   .
- This means that if the input signal is positive, the output signal will be negative, and vice versa .
- An inverting amplifier can be used to amplify or invert a signal, depending on the values of the resistors in the circuit  .
- The basic circuit diagram of an inverting amplifier is shown below:

```
    +Vcc
     |
     |
     |
    Rf
     |
     +-----+
     |     |
     |     |
     |     |
     |     |
     |     |
     |     |    Vout
     |     +----+
     |     |    |
     |     |    |
     |     |    |
     |     |    |
     |     |    |
     |     |    |
     |     |    |
     |     |    |
     |     |    |
     |     |    |
     |     |    |
     |     |    |
     |     |    |
     |     |    |
     |     |    |
     |     |    |
     |     |    |
     |     |    |
     |     |    |
     +-----+    |
     |          |
     |          |
     |          |
     |          |
     |          |
     |          |
     |          |
     |          |
     |          |
     |          |
     |          |
     |          |
     |          |
     |          |
     |          |
    Ri         |
     |          |
     |          |
     |          |
     |          |
     |          |
     |          |
     |          |
     |          |
     |          |
     |          |
     |          |
     |          |
     |          |
     |          |
    Vin        |
     +----------+
     |
     |
     |
    -Vcc
```

- The input signal, Vin, is applied to the inverting input terminal of the op-amp through a resistor, Ri   .
- The output signal, Vout, is fed back to the inverting input terminal through a resistor, Rf   .
- The non-inverting input terminal of the op-amp is connected to the ground   .
- The op-amp is powered by a dual supply voltage, +Vcc and -Vcc   .
- The gain of the inverting amplifier is given by the formula:

```
    Gain = -Rf/Ri
```

- The negative sign indicates that the output signal is inverted with respect to the input signal   .
- The gain can be adjusted by changing the values of Rf and Ri  .
- The input impedance of the inverting amplifier is equal to Ri   .
- The output impedance of the inverting amplifier is very low, as the op-amp has a high open-loop gain   .

- Some applications of the inverting amplifier are:

  - Signal inversion: The inverting amplifier can be used to reverse the polarity of a signal, such as converting a positive voltage to a negative voltage or vice versa  .
  - Signal amplification: The inverting amplifier can be used to increase the amplitude of a signal, such as boosting a weak audio signal or a sensor signal  .
  - Signal attenuation: The inverting amplifier can be used to decrease the amplitude of a signal, such as reducing a loud audio signal or a sensor signal  .
  - Signal mixing: The inverting amplifier can be used to combine two