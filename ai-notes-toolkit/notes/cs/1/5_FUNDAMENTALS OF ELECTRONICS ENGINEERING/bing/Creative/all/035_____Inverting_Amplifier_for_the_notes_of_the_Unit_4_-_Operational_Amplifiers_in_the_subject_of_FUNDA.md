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
- The op-amp tries to maintain the same voltage at both of its input terminals, which is called the virtual ground principle .
- This means that the voltage at the inverting input terminal (-) is equal to the voltage at the non-inverting input terminal (+), which is zero in this case .
- Therefore, the voltage across the input resistor (Ri) is equal to the input signal (Vin), and the current through the input resistor (Ii) is given by:

Ii = Vin / Ri

- Since the op-amp has a very high input impedance, the current through the inverting input terminal (-) is negligible, and the same current (Ii) flows through the feedback resistor (Rf) .
- The voltage across the feedback resistor (Rf) is equal to the output signal (Vout), and the current through the feedback resistor (Ii) is given by:

Ii = Vout / Rf

- Equating the two expressions for the current (Ii), we get:

Vin / Ri = Vout / Rf

- Rearranging the equation, we get the voltage gain (Av) of the inverting amplifier, which is given by:

Av = Vout / Vin = - Rf / Ri

- The negative sign indicates that the output signal is inverted with respect to the input signal  .
- The magnitude of the voltage gain depends on the ratio of the feedback resistor (Rf) to the input resistor (Ri)  .
- If Rf > Ri, the voltage gain is greater than 1, and the circuit acts as an inverting amplifier  .
- If Rf < Ri, the voltage gain is less than 1, and the circuit acts as an inverting attenuator  .
- If Rf = Ri, the voltage gain is equal to 1, and the circuit acts as an inverting buffer  .

## Applications

- Some of the applications of an inverting amplifier are:

  - Signal inversion: An inverting amplifier can be used to invert the polarity of a signal, such as converting a positive signal to a negative signal or vice versa   .
  - Signal amplification: An inverting amplifier can be used to amplify a signal by choosing a suitable value of the feedback resistor (Rf) that is larger than the input resistor (Ri)  [