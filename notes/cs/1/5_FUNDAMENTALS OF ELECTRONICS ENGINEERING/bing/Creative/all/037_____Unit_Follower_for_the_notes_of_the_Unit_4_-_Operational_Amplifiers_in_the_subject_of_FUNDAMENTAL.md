# Unit Follower

- A unit follower is a type of operational amplifier (op-amp) circuit that has a voltage gain of 1.
- It is also called a voltage follower, an op-amp buffer, or a unity-gain amplifier.
- It is used to isolate circuits from each other, to prevent loading effects, and to provide impedance matching.
- It consists of an op-amp with a direct feedback connection from the output to the inverting (-) input.
- The non-inverting (+) input is connected to the input voltage source.
- The output voltage is equal to the input voltage, hence the name voltage follower.
- The input impedance of the unit follower is very high, ideally infinite, so it does not draw any current from the input source.
- The output impedance of the unit follower is very low, ideally zero, so it can drive any load without voltage drop.
- The unit follower has a phase shift of zero degrees, meaning it does not invert the input signal.
- The unit follower has a bandwidth of almost the entire frequency range of the op-amp, since it does not have any external resistors or capacitors that affect the frequency response.
- The unit follower can be used for various applications, such as signal buffering, impedance transformation, level shifting, and voltage reference.

The following diagram shows the circuit of a unit follower using an op-amp:

![Unit follower circuit](https://electronicsreference.com/images/op_amps/voltage-follower/voltage-follower-circuit.png)

The following equations describe the operation of the unit follower:

Vout = Vin

Vout - V- = 0

V+ = V-

V+ = Vin

Vout = Vin

The following table summarizes the characteristics of the unit follower:

| Parameter | Value |
|-----------|-------|
| Voltage gain | 1 |
| Input impedance | Very high |
| Output impedance | Very low |
| Phase shift | 0 degrees |
| Bandwidth | Almost the entire op-amp frequency range |