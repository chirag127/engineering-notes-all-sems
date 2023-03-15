# Integrator

- An integrator is an electronic circuit that performs the mathematical operation of integration with respect to time.
- An integrator uses an operational amplifier (op-amp) as the main component, along with a resistor and a capacitor.
- The basic configuration of an op-amp integrator is shown below:

![Op-amp integrator circuit](https://www.electronics-tutorials.ws/wp-content/uploads/2018/05/opamp-opamp6.gif)

- The input voltage V<sub>in</sub> is applied to the inverting terminal of the op-amp through the resistor R, while the output voltage V<sub>out</sub> is taken from the non-inverting terminal.
- The capacitor C is connected between the output and the inverting terminal, forming a negative feedback loop.
- The non-inverting terminal is grounded, so the virtual ground concept applies, meaning that the voltage at the inverting terminal is also zero.
- The current flowing through the resistor R is equal to V<sub>in</sub>/R, and this current charges the capacitor C, causing the output voltage to change over time.
- The output voltage is given by the following formula:

V<sub>out</sub> = -1/RC ∫ V<sub>in</sub> dt

- This means that the output voltage is proportional to the integral of the input voltage, with a negative sign and a scaling factor of 1/RC.
- The negative sign indicates that the output voltage is inverted with respect to the input voltage, and the scaling factor depends on the values of the resistor and the capacitor.
- The integrator circuit can be used to perform various functions, such as generating waveforms, filtering signals, measuring areas, and implementing mathematical operations.