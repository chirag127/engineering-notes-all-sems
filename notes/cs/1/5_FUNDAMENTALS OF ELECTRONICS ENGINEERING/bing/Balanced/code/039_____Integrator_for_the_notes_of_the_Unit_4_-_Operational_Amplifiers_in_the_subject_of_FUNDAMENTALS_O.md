### Integrator

- An integrator is an electronic circuit that performs the mathematical operation of integration with respect to time.
- An integrator uses an operational amplifier (op-amp) as the main component, along with a resistor and a capacitor.
- The basic configuration of an op-amp integrator is shown below:

![Op-amp integrator circuit](https://www.electronics-tutorials.ws/wp-content/uploads/2018/05/opamp-opamp6.gif)

- The input voltage is applied to the inverting terminal of the op-amp through the resistor R, and the output voltage is taken from the non-inverting terminal.
- The capacitor C is connected between the output and the inverting terminal, forming a negative feedback loop.
- The non-inverting terminal is grounded, so the virtual ground concept applies at the inverting terminal, i.e., the voltage at the inverting terminal is approximately zero.
- The current flowing through the resistor R is given by:

`I = V_in / R`

- Since the current through the capacitor is equal to the current through the resistor, we can write:

`I = C dV_out / dt`

- Equating the two expressions for the current, we get:

`V_in / R = C dV_out / dt`

- Rearranging the terms, we get:

`dV_out / dt = - (1 / RC) V_in`

- Integrating both sides with respect to time, we get:

`V_out = - (1 / RC) ∫ V_in dt + K`

- Where K is the constant of integration, which depends on the initial condition of the capacitor.
- The output voltage is therefore proportional to the integral of the input voltage, with a negative sign and a scaling factor of 1/RC.
- The negative sign indicates that the output voltage is 180 degrees out of phase with the input voltage.
- The scaling factor 1/RC determines the gain of the integrator, which can be adjusted by changing the values of R and C.
- The integrator can be used to perform various functions, such as waveform generation, signal conditioning, analog computation, etc.