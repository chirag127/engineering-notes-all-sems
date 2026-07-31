### Non-inverting Amplifier

- A non-inverting amplifier is an op-amp circuit configuration that produces an amplified output signal and this output signal of the non-inverting op-amp is in-phase with the applied input signal .
- In other words, a non-inverting amplifier behaves like a voltage follower circuit.
- The basic circuit diagram of a non-inverting amplifier is shown below:

```
    +Vcc
     |
     |
     |
     |    Rf
     |----/\/\/\----+
     |              |
     |              |      +--------+
     |              +------| +      |
     |                     |        |---- Vout
     |              +------| -      |
     |              |      +--------+
     |              |
     |    Rin       |
     |----/\/\/\----+
     |
     |
     |
    -Vcc
```

- The input voltage signal, ( VIN ) is applied directly to the non-inverting ( + ) input terminal which means that the output gain of the amplifier becomes "Positive" in value in contrast to the "Inverting Amplifier" circuit we saw in the previous tutorial whose output gain is negative in value.
- The feedback resistor, Rf is connected between the output terminal and the inverting input terminal. The input resistor, Rin is connected between the non-inverting input terminal and the input voltage source.
- The voltage gain of the non-inverting amplifier is given by the formula:

```
    Av = Vout / Vin = (1 + Rf / Rin)
```

- The voltage gain of the non-inverting amplifier is always greater than one since Rf is greater than Rin.
- The input impedance of the non-inverting amplifier is very high, as the input voltage is applied to the non-inverting input terminal of the op-amp, which has a very high input impedance.
- The output impedance of the non-inverting amplifier is very low, as the output is taken from the op-amp, which has a very low output impedance.
- The non-inverting amplifier has some advantages over the inverting amplifier, such as no phase inversion, higher input impedance, lower output impedance, and higher bandwidth.
- The non-inverting amplifier has some applications, such as buffer amplifier, impedance converter, voltage follower, summing amplifier, and differential amplifier.