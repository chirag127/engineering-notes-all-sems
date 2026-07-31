# Differentiator

A differentiator is a circuit that performs the mathematical operation of differentiation, that is, it produces an output voltage that is proportional to the rate of change of the input voltage. A differentiator can be constructed using an operational amplifier (op-amp) with a capacitor and a resistor in the feedback loop. The differentiator is one of the applications of op-amps in analog signal processing.

## Circuit Diagram

The circuit diagram of a differentiator using an op-amp is shown below:

![Differentiator circuit diagram](https://www.electronics-tutorials.ws/wp-content/uploads/2018/05/opamp-opamp7.gif)

The input voltage is applied to the inverting terminal of the op-amp through a capacitor C, while the non-inverting terminal is grounded. A resistor R is connected between the output and the inverting terminal to provide negative feedback. The output voltage is taken across the resistor R.

## Working Principle

The working principle of the differentiator can be explained using the capacitor's current to voltage relationship. The current through a capacitor is given by:

`i = C dv/dt`

where i is the current, C is the capacitance, v is the voltage across the capacitor, and t is the time.

The voltage across the capacitor is equal to the input voltage, since the inverting terminal of the op-amp is virtually grounded. Therefore, the current through the capacitor is:

`i = C dV_in/dt`

The current through the capacitor is also equal to the current through the resistor, since the op-amp has a very high input impedance and a very low output impedance. Therefore, the voltage across the resistor is:

`V_out = -iR = -RC dV_in/dt`

The negative sign indicates that the output voltage is 180 degrees out of phase with the input voltage. The output voltage is proportional to the rate of change of the input voltage, which is the definition of differentiation.

## Frequency Response

The frequency response of the differentiator can be obtained by applying a sinusoidal input voltage of the form:

`V_in = V_m sin(ωt)`

where V_m is the peak voltage, ω is the angular frequency, and t is the time.

The output voltage is then:

`V_out = -RC dV_in/dt = -RC V_m ω cos(ωt)`

The magnitude of the output voltage is:

`|V_out| = RC V_m ω`

The phase difference between the input and output voltages is:

`φ = tan^(-1)(-1/RCω)`

The frequency response of the differentiator is shown below:

![Differentiator frequency response](https://www.electronics-tutorials.ws/wp-content/uploads/2018/05/opamp-opamp7a.gif)

The frequency response shows that the differentiator acts as a high-pass filter, that is, it passes high-frequency signals and attenuates low-frequency signals. The gain of the differentiator increases linearly with frequency, which means that the output voltage can become very large for high-frequency signals. This can cause noise and distortion in the output signal. To avoid this, a resistor R1 can be added in series with the capacitor C, as shown below:

![Differentiator with R1](https://www.electronics-tutorials.ws/wp-content/uploads/2018/05/opamp-opamp7b.gif)

The resistor R1 limits the gain of the differentiator at high frequencies and improves the stability of the circuit. The output voltage of the modified differentiator is:

`V_out = -R/(R1 + 1/ωC) dV_in/dt`

The frequency response of the modified differentiator is shown below:

![Modified differentiator frequency response](https://www.electronics-tutorials.ws/wp-content/uploads/2018/05/opamp-opamp7c.gif)

The frequency response shows that the modified differentiator has a constant gain at low frequencies and a decreasing gain at high frequencies. The cutoff frequency of the modified differentiator is:

`f_c = 1/(2πR1C)`

The cutoff frequency is the frequency at which the gain of the differentiator drops by 3 dB from its maximum value. The cutoff frequency determines the range of frequencies over which the differentiator can perform accurate differentiation.

## Applications

The differentiator can be used in various applications, such as:

- Waveform generation: The differentiator can be used to generate square, triangular, and sawtooth waveforms from sinusoidal inputs.
- Edge detection: The differentiator can be used to detect the