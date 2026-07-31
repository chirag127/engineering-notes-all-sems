### Unit Follower for the notes of the Unit 4 - Operational Amplifiers in the subject of FUNDAMENTALS OF ELECTRONICS ENGINEERING

- A unit follower, also known as a voltage follower, buffer, or unity-gain amplifier, is a simple op-amp circuit that produces an output voltage equal to the input voltage .
- A unit follower is created by directly connecting the output of the op-amp to the inverting (-) input, and applying the input voltage to the non-inverting (+) input .
- A unit follower has a voltage gain of 1, meaning that the output voltage follows the input voltage without any amplification or attenuation .
- A unit follower has a very high input impedance and a very low output impedance, meaning that it can isolate the input source from the load without affecting the signal .
- A unit follower is useful for impedance matching, signal buffering, level shifting, and driving low-impedance loads  .
- A unit follower is also a special case of a non-inverting amplifier, where the feedback resistor is zero and the input resistor is infinite.
- A unit follower can be represented by the following circuit diagram  :

![Unit follower circuit diagram](https://electronicsreference.com/images/op_amps/voltage-follower/voltage-follower-circuit-diagram.png)

- A unit follower can be analyzed by applying the virtual short circuit and the ideal op-amp assumptions:
  - The voltage at the inverting input is equal to the voltage at the non-inverting input, which is the input voltage.
  - The current flowing into the inverting input and the non-inverting input is zero.
  - The output voltage is equal to the input voltage multiplied by the open-loop gain, which is very large.
- Therefore, the output voltage can be expressed as:

![Unit follower output voltage equation](https://latex.codecogs.com/png.latex?V_%7Bout%7D%20%3D%20V_%7Bin%7D%20%5Ctimes%20A_%7BOL%7D)

- However, since the output voltage is also connected to the inverting input, it cannot exceed the supply voltage of the op-amp, which is usually ±15V.
- Therefore, the output voltage is limited by the supply voltage, and the open-loop gain is effectively reduced to 1.
- Hence, the output voltage is equal to the input voltage, as expected:

![Unit follower output voltage equation simplified](https://latex.codecogs.com/png.latex?V_%7Bout%7D%20%3D%20V_%7Bin%7D)

- A unit follower can be verified by measuring the input and output voltages using a multimeter or an oscilloscope.
- A unit follower can be implemented using any op-amp, such as the LM741, LM358, or TL081.