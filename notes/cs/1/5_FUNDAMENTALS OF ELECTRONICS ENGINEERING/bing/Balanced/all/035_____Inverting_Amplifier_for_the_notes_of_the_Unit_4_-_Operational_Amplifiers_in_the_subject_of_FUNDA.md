# Inverting Amplifier

- An inverting amplifier is a type of operational amplifier circuit that produces an output signal that is 180 degrees out of phase with the input signal   .
- This means that if the input signal is positive, then the output signal will be negative and vice versa .
- An inverting amplifier can be used to amplify or invert a signal, depending on the values of the resistors in the circuit  .
- An inverting amplifier can also be used for signal conditioning or mathematical operations, such as subtraction, integration, differentiation, etc  .

## Circuit Diagram

- The basic circuit diagram of an inverting amplifier is shown below:

![Inverting amplifier circuit diagram](https://www.electronics-tutorials.ws/wp-content/uploads/2018/05/opamp-opamp2.gif)

- The circuit consists of an operational amplifier (op-amp), an input resistor (Ri), and a feedback resistor (Rf).
- The input signal (Vin) is applied to the inverting input (-) of the op-amp, while the non-inverting input (+) is connected to the ground.
- The output signal (Vout) is taken from the output terminal of the op-amp.

## Working Principle

- The working principle of an inverting amplifier is based on the negative feedback model of an op-amp .
- The negative feedback model assumes that the op-amp has a very high open-loop gain (A), a very high input impedance (Zin), and a very low output impedance (Zout).
- The negative feedback model also assumes that the op-amp maintains a virtual short circuit between its input terminals, which means that the voltage difference between the inverting and non-inverting inputs is zero (V- = V+).
- Based on these assumptions, the working principle of an inverting amplifier can be explained as follows:

  - Since the non-inverting input is grounded, the inverting input is also at zero volts (V- = V+ = 0).
  - The input current (Iin) is equal to the input voltage (Vin) divided by the input resistor (Ri), as per Ohm's law (Iin = Vin/Ri).
  - The input current (Iin) flows through the feedback resistor (Rf) and creates a voltage drop across it, which is equal to the output voltage (Vout), as per Ohm's law (Vout = Iin*Rf).
  - The output voltage (Vout) is negative, since the current flows from the inverting input to the output, and the output is connected to the negative terminal of the op-amp.
  - The output voltage (Vout) is proportional to the input voltage (Vin), and the proportionality constant is the closed-loop gain (G) of the inverting amplifier, which is given by the ratio of the feedback resistor (Rf) to the input resistor (Ri) (G = -Rf/Ri).
  - The closed-loop gain (G) can be adjusted by changing the values of the resistors (Rf and Ri) in the circuit.

## Applications

- Some of the applications of an inverting amplifier are:

  - Signal inversion: An inverting amplifier can be used to invert the polarity of a signal, which can be useful for some applications, such as phase shifting, noise cancellation, etc .
  - Signal amplification: An inverting amplifier can be used to amplify a signal, by choosing a feedback resistor (Rf) that is larger than the input resistor (Ri), which results in a closed-loop gain (G) that is greater than one in magnitude  .
  - Signal attenuation: An inverting amplifier can be used to attenuate a signal, by choosing a feedback resistor (Rf) that is smaller than the input resistor (Ri), which results in a closed-loop gain (G) that is less than one in magnitude  .
  - Signal subtraction: An inverting amplifier can be used to subtract two signals, by applying one signal to the inverting input and the other signal to the non-inverting input through a resistor, which results in an output signal that is the difference of