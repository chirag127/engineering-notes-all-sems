# Unit Follower for the notes of the Unit 4 - Operational Amplifiers in the subject of FUNDAMENTALS OF ELECTRONICS ENGINEERING

- A unit follower, also known as a voltage follower, buffer, or unity-gain amplifier, is a simple op-amp circuit that produces an output voltage equal to the input voltage .
- A unit follower is created by directly connecting the output of the op-amp to the inverting (-) input, and applying the input voltage to the non-inverting (+) input .
- A unit follower has a voltage gain of 1, meaning that the output voltage is the same as the input voltage, but with a very high input impedance and a very low output impedance .
- A unit follower is useful for isolating circuits from each other, especially in high-order filters, to prevent loading effects and signal attenuation .
- A unit follower can also be used to drive low-impedance loads, such as speakers or LEDs, without affecting the input signal source.
- A unit follower can be represented by the following circuit diagram :

![Unit follower circuit diagram](https://electronicsreference.com/images/op_amps/voltage-follower/voltage-follower-circuit-diagram.png)

- A unit follower can be analyzed by applying the virtual short circuit and virtual open circuit assumptions of an ideal op-amp:
  - The virtual short circuit assumption states that the voltage difference between the inverting and non-inverting inputs is zero, i.e., V- = V+.
  - The virtual open circuit assumption states that the current flowing into the inverting and non-inverting inputs is zero, i.e., I- = I+ = 0.
- Applying these assumptions to the unit follower circuit, we can derive the following equations:
  - Vout = V- = V+ = Vin (voltage gain of 1)
  - Iin = I+ = 0 (high input impedance)
  - Iout = Vout / Rout (low output impedance)