# Integrator

## Definition
- An integrator is an electronic circuit that performs the mathematical operation of integration with respect to time.
- It is based on an operational amplifier (op-amp) with a capacitor and a resistor in the feedback loop.
- The output voltage of the integrator is proportional to the input voltage integrated over time.

## Circuit Diagram
- The basic circuit diagram of an op-amp integrator is shown below:

![Op-amp integrator circuit diagram](https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/Op-Amp_Integrator.svg/1200px-Op-Amp_Integrator.svg.png)

- The input voltage is applied to the inverting terminal of the op-amp through a resistor R.
- The output voltage is fed back to the inverting terminal through a capacitor C.
- The non-inverting terminal is grounded.

## Working Principle
- The working principle of the op-amp integrator can be explained using the virtual ground concept and the capacitor charge equation.
- The virtual ground concept states that the voltage at the inverting terminal of the op-amp is equal to the voltage at the non-inverting terminal, which is zero in this case.
- Therefore, the voltage across the resistor R is equal to the input voltage V<sub>in</sub>.
- The current flowing through the resistor R is given by:

I = V<sub>in</sub> / R

- This current also flows through the capacitor C, since the op-amp has a very high input impedance and draws negligible current.
- The capacitor charge equation states that the voltage across the capacitor C is equal to the charge on the capacitor divided by its capacitance, which is given by:

V<sub>C</sub> = Q / C

- The charge on the capacitor Q is equal to the integral of the current over time, which is given by:

Q = ∫ I dt

- Substituting the values of I and V<sub>C</sub>, we get:

V<sub>C</sub> = (1 / C) ∫ V<sub>in</sub> / R dt

- The output voltage V<sub>out</sub> is equal to the negative of the voltage across the capacitor C, since the op-amp is in inverting configuration. Therefore, we get:

V<sub>out</sub> = - V<sub>C</sub>

- Substituting the value of V<sub>C</sub>, we get:

V<sub>out</sub> = - (1 / C) ∫ V<sub>in</sub> / R dt

- This equation shows that the output voltage of the op-amp integrator is proportional to the integral of the input voltage over time, with a constant of proportionality of -1 / RC.

## Applications
- The op-amp integrator can be used for various applications, such as:
  - Signal processing: The op-amp integrator can be used to perform mathematical operations on signals, such as differentiation, integration, filtering, etc.
  - Waveform generation: The op-amp integrator can be used to generate different types of waveforms, such as triangular, sawtooth, square, etc., by applying different types of input signals, such as sinusoidal, square, etc.
  - Analog computation: The op-amp integrator can be used to perform analog computation, such as solving differential equations, calculating areas, etc., by applying the appropriate input signals and feedback components.