### Integrator

- An integrator is an electronic circuit that performs the mathematical operation of integration with respect to time  .
- An integrator circuit is based on an operational amplifier (op-amp) with a resistor and a capacitor connected in the feedback loop  .
- The output voltage of an integrator circuit is proportional to the integral of the input voltage  .
- The integrator circuit can be used to perform various functions, such as signal processing, waveform generation, analog computation, and filtering .

#### Circuit diagram and working principle

- The circuit diagram of an op-amp integrator is shown below:

![Op-amp integrator circuit diagram](https://www.electronics-tutorials.ws/wp-content/uploads/2018/05/opamp-opamp6.gif)

- The input voltage V<sub>in</sub> is applied to the inverting terminal of the op-amp through a resistor R<sub>1</sub>. The non-inverting terminal is grounded .
- The output voltage V<sub>out</sub> is fed back to the inverting terminal through a capacitor C<sub>1</sub>. The feedback resistor R<sub>f</sub> is replaced by a capacitor to achieve integration .
- The op-amp is assumed to be ideal, that is, it has infinite gain, infinite input impedance, and zero output impedance .
- The voltage at the inverting terminal is equal to the voltage at the non-inverting terminal, which is zero. This is called the virtual ground condition .
- The current flowing through the resistor R<sub>1</sub> is equal to the current flowing through the capacitor C<sub>1</sub>, since no current enters or leaves the op-amp .
- The current through the resistor R<sub>1</sub> is given by Ohm's law as:

  I<sub>1</sub> = V<sub>in</sub> / R<sub>1</sub>

- The current through the capacitor C<sub>1</sub> is given by the capacitor equation as:

  I<sub>1</sub> = C<sub>1</sub> dV<sub>out</sub> / dt

- Equating the two currents, we get:

  V<sub>in</sub> / R<sub>1</sub> = C<sub>1</sub> dV<sub>out</sub> / dt

- Rearranging the equation, we get:

  dV<sub>out</sub> / dt = - (1 / R<sub>1</sub> C<sub>1</sub>) V<sub>in</sub>

- Integrating both sides, we get:

  V<sub>out</sub> = - (1 / R<sub>1</sub> C<sub>1</sub>) ∫ V<sub>in</sub> dt + K

- Where K is the constant of integration, which depends on the initial condition of the capacitor .

- The output voltage is thus the negative of the integral of the input voltage, scaled by a factor of 1 / R<sub>1</sub> C<sub>1</sub> .
- The output voltage can be adjusted by varying the values of R<sub>1</sub> and C<sub>1</sub>. The smaller the value of R<sub>1</sub> C<sub>1</sub>, the faster the output voltage changes with respect to the input voltage .
- The output voltage can also be affected by the op-amp's finite gain and bandwidth, the capacitor's leakage current and parasitic resistance, and the input and output offset voltages .

#### Applications and examples

- The integrator circuit can be used to perform various functions, such as signal processing, waveform generation, analog computation, and filtering .
- Some examples of the applications of the integrator circuit are:

  - The integrator circuit can be used to