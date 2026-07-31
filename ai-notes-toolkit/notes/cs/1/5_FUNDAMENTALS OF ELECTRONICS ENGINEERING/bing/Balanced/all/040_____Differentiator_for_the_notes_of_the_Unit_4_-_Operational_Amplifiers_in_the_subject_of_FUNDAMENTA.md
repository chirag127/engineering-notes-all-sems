# Differentiator

A differentiator is a circuit that performs the mathematical operation of differentiation, that is, it produces an output voltage that is proportional to the rate of change of the input voltage. A differentiator can be constructed using an operational amplifier (op-amp) with a capacitor and a resistor in the feedback loop.

## Circuit Diagram

The circuit diagram of a differentiator using an op-amp is shown below:

![Differentiator Circuit](https://www.electronicshub.org/wp-content/uploads/2014/07/Operational-Amplifier-as-Differentiator.jpg)

The input voltage is applied to the inverting terminal of the op-amp through a capacitor C, and the output voltage is taken from the output terminal of the op-amp. A resistor R is connected between the output and the inverting terminal to provide negative feedback.

## Working Principle

The working principle of a differentiator can be explained as follows:

- The capacitor C acts as a short circuit for high-frequency signals and as an open circuit for low-frequency signals. Therefore, the input voltage is coupled to the inverting terminal of the op-amp only for high-frequency signals.
- The current through the capacitor C is given by:

  `i = C dv/dt`

  where `i` is the current, `C` is the capacitance, `v` is the input voltage, and `t` is the time.

- The current through the capacitor C is equal to the current through the resistor R, since the input impedance of the op-amp is very high and no current flows into the op-amp.

  `i = C dv/dt = Vout/R`

  where `Vout` is the output voltage.

- Rearranging the above equation, we get:

  `Vout = -RC dv/dt`

  where `-RC` is the gain of the differentiator.

- The negative sign indicates that the output voltage is 180 degrees out of phase with the input voltage.

- The output voltage is proportional to the rate of change of the input voltage, which is the definition of differentiation.

## Applications

Some of the applications of a differentiator are:

- To perform mathematical operations such as subtraction, multiplication, and integration in analog computers.
- To generate square waves and pulses from triangular and sinusoidal waves.
- To detect the edges and transitions of signals in digital circuits.
- To sharpen the peaks and valleys of signals in waveform generators.