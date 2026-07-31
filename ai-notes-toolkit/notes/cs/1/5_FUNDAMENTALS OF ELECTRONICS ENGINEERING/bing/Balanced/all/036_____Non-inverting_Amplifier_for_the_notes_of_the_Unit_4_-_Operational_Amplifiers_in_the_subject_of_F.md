# Non-inverting Amplifier

- A non-inverting amplifier is an op-amp circuit configuration that produces an amplified output signal and this output signal of the non-inverting op-amp is in-phase with the applied input signal .
- In other words, a non-inverting amplifier behaves like a voltage follower circuit.
- The basic circuit diagram of a non-inverting amplifier is shown below:

```
    +Vcc
     |
     |
    | |
    | | Rf
    | |
     |
     |------------------+
     |                  |
     |                  |
     |                  |
     |                  |
     |                  |
     |                  |
     |                  |
     |                  |
     |                  |
     |                  |
     |                  |
     |                  |
     |                  |
     |                  |
     |                  |
     |                  |
     +                  +
    -Vcc               Out
                       |
                       |
                      | |
                      | | Rl
                      | |
                       |
                       |
                      GND
```

- The input voltage signal, ( VIN ) is applied directly to the non-inverting ( + ) input terminal which means that the output gain of the amplifier becomes "Positive" in value in contrast to the "Inverting Amplifier" circuit we saw in the previous tutorial whose output gain is negative in value.
- The feedback resistor, Rf is connected between the output terminal and the inverting input terminal. The resistor, Rin is connected to the non-inverting input terminal and to ground.
- The voltage gain of a non-inverting amplifier is given by the formula   :

```
    Av = (1 + Rf / Rin)
```

- Where Av is the voltage gain, Rf is the feedback resistor, and Rin is the input resistor.
- The output voltage of a non-inverting amplifier is given by the formula   :

```
    Vout = Av * VIN
```

- Where Vout is the output voltage, Av is the voltage gain, and VIN is the input voltage.
- The output voltage of a non-inverting amplifier is always positive and in phase with the input voltage   .
- The output waveform of a non-inverting amplifier is shown below:

```
    VIN
    ^
    |    /‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\
    |   /                \
    |  /                  \
    | /                    \
    |/                      \
    +------------------------+----> t
    |                       /\
    |                      /  \
    |                     /    \
    |                    /      \
    |                   /        \
    |                  /          \
    |                 /            \
    |                /              \
    |               /                \
    |              /                  \
    |             /                    \
    |            /                      \
    |           /                        \
    |          /                          \
    |         /                            \
    |        /                              \
    |       /                                \
    |      /                                  \
    |     /                                    \
    |    /                                      \
    |   /                                        \
    |  /                                          \
    | /                                            \
    |/                                              \
    +------------------------------------------------+----> t
    Vout
```

- The advantages of a non-inverting amplifier are   :
  - It has a high input impedance and a low output impedance.
  - It does not invert the input signal.
  - It can have a voltage gain of less than or greater than unity.
  - It has a better bandwidth and stability than the inverting amplifier.
- The disadvantages of a non-inverting amplifier are   :
  - It requires a dual power supply for operation.
  - It may suffer from offset voltage and bias current problems.
  - It may introduce noise and distortion in the output signal.
- The applications of a non-inverting amplifier are   :
  - It can be used as a buffer amplifier to isolate the input and output stages of a circuit.