### Non-inverting Amplifier

- A non-inverting amplifier is an op-amp circuit configuration that produces an amplified output signal and this output signal of the non-inverting op-amp is in-phase with the applied input signal .
- In other words, a non-inverting amplifier behaves like a voltage follower circuit.
- The basic circuit diagram of a non-inverting amplifier is shown below:

![Non-inverting amplifier circuit diagram](https://www.electronicshub.org/wp-content/uploads/2013/07/Non-Inverting-Operational-Amplifier.jpg)

- The input voltage signal, ( V<sub>IN</sub> ) is applied directly to the non-inverting ( + ) input terminal which means that the output gain of the amplifier becomes "Positive" in value in contrast to the "Inverting Amplifier" circuit we saw in the previous tutorial whose output gain is negative in value.
- The feedback resistor, R<sub>F</sub> and the input resistor, R<sub>IN</sub> form a potential divider network across the amplifier and the voltage gain of a non-inverting amplifier can be calculated as  :

![Non-inverting amplifier voltage gain formula](https://www.electronicshub.org/wp-content/uploads/2013/07/Non-Inverting-Operational-Amplifier-Formula.jpg)

- The voltage gain of a non-inverting amplifier is always greater than one.
- The input impedance of a non-inverting amplifier is very high, as the input signal is applied to the non-inverting input terminal of the op-amp, which has a very high input impedance .
- The output impedance of a non-inverting amplifier is very low, as the output signal is taken from the output terminal of the op-amp, which has a very low output impedance .
- The advantages of a non-inverting amplifier are:
  - It has a high input impedance and a low output impedance, which makes it suitable for impedance matching applications.
  - It has a positive voltage gain, which means that the output signal is in-phase with the input signal, which is useful for signal conditioning applications.
  - It has a simple circuit design, as it requires only two resistors to set the voltage gain.
- The disadvantages of a non-inverting amplifier are:
  - It has a minimum voltage gain of one, which means that it cannot attenuate the input signal, which may be required for some applications.
  - It may suffer from stability issues, as the feedback loop may introduce oscillations or noise in the output signal, which may degrade the performance of the amplifier.