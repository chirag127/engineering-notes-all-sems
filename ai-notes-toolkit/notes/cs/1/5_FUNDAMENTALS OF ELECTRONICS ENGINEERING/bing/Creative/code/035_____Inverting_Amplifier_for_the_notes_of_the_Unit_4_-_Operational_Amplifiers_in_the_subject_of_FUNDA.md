# Inverting Amplifier

- An inverting amplifier is a type of operational amplifier circuit that produces an output signal that is 180 degrees out of phase with the input signal   .
- This means that if the input signal is positive, then the output signal will be negative and vice versa .
- An inverting amplifier can be used to amplify or invert a signal, depending on the values of the resistors in the circuit   .
- An inverting amplifier can also be used for signal conditioning or mathematical operations, such as subtraction, integration, differentiation, etc  .

## Circuit Diagram

- The basic circuit diagram of an inverting amplifier is shown below:

![Inverting amplifier circuit diagram](https://www.electronics-tutorials.ws/wp-content/uploads/2018/05/opamp-opamp2.gif)

- The circuit consists of an operational amplifier (op-amp), an input resistor (Ri), and a feedback resistor (Rf).
- The input signal (Vin) is applied to the inverting input terminal (-) of the op-amp, while the non-inverting input terminal (+) is connected to the ground.
- The output signal (Vout) is taken from the output terminal of the op-amp.

## Working Principle

- The working principle of an inverting amplifier is based on the negative feedback model, which means that a fraction of the output signal is fed back to the input through the feedback resistor (Rf) .
- The op-amp tries to maintain the same voltage at both of its input terminals, which is called the virtual ground or virtual short condition .
- This means that the voltage at the inverting input terminal (-) is equal to the voltage at the non-inverting input terminal (+), which is zero in this case .
- Therefore, the voltage across the input resistor (Ri) is equal to the input signal (Vin), and the current flowing through the input resistor (Ii) is given by:

$$I_i = \frac{V_{in}}{R_i}$$

- The same current (Ii) also flows through the feedback resistor (Rf), since the op-amp has a very high input impedance and draws negligible current .
- Therefore, the voltage across the feedback resistor (Rf) is given by:

$$V_f = I_i \times R_f = \frac{V_{in}}{R_i} \times R_f$$

- The output signal (Vout) is the difference between the voltage at the output terminal and the voltage at the inverting input terminal of the op-amp .
- Since the voltage at the inverting input terminal is zero, the output signal (Vout) is equal to the negative of the voltage across the feedback resistor (Rf), which is given by:

$$V_{out} = -V_f = -\frac{V_{in}}{R_i} \times R_f$$

- The ratio of the output signal (Vout) to the input signal (Vin) is called the voltage gain (Av) of the inverting amplifier, which is given by:

$$A_v = \frac{V_{out}}{V_{in}} = -\frac{R_f}{R_i}$$

- The voltage gain (Av) of the inverting amplifier depends on the values of the resistors (Rf and Ri) in the circuit .
- The voltage gain (Av) is negative, which means that the output signal (Vout) is inverted with respect to the input signal (Vin) .
- The magnitude of the voltage gain (Av) can be increased or decreased by changing the values of the resistors (Rf and Ri) in the circuit .
- For example, if Rf is larger than Ri, then the magnitude of the voltage gain (Av) is greater than one, which means that the output signal (Vout) is amplified and inverted with respect to the input signal (Vin) .
- If Rf is smaller than Ri, then the magnitude of the voltage