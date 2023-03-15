### Inverting Amplifier

- An inverting amplifier is a type of operational amplifier circuit that produces an output signal that is 180 degrees out of phase with the input signal   .
- The signal is inverted by reversing the polarity of the signal. This is done by using an operational amplifier, which is a type of amplifier that can be used to amplify or invert a signal.
- The inverting amplifier has a negative feedback configuration, which means that the output signal is fed back to the inverting input terminal of the op-amp through a feedback resistor  .
- The inverting amplifier has a constant or fixed gain, which is determined by the ratio of the feedback resistor and the input resistor   .
- The inverting amplifier can be used for signal conditioning, mathematical operations, voltage inversion, impedance transformation, and other applications   .

The basic circuit diagram of an inverting amplifier is shown below:

![Inverting amplifier circuit diagram](https://www.electronics-tutorials.ws/wp-content/uploads/2018/05/opamp-opamp2.gif)

The input signal is applied to the inverting input terminal of the op-amp through the input resistor R1. The output signal is fed back to the same terminal through the feedback resistor R2. The non-inverting input terminal of the op-amp is connected to the ground or reference voltage.

The voltage gain of the inverting amplifier is given by:

![Voltage gain formula](https://www.electronics-tutorials.ws/wp-content/uploads/2018/05/opamp-opamp2a.gif)

The voltage gain is negative, which means that the output signal is inverted with respect to the input signal. The magnitude of the gain depends on the values of R1 and R2. The gain can be increased by increasing R2 or decreasing R1. The gain can be decreased by decreasing R2 or increasing R1.

The input impedance of the inverting amplifier is equal to the input resistor R1. The output impedance of the inverting amplifier is very low, as the op-amp has a high open-loop gain and a negative feedback. The output impedance can be approximated by:

![Output impedance formula](https://www.electronics-tutorials.ws/wp-content/uploads/2018/05/opamp-opamp2b.gif)

where A is the open-loop gain of the op-amp.

The inverting amplifier has some advantages and disadvantages, which are summarized below:

| Advantages | Disadvantages |
|------------|---------------|
| Simple and easy to design | Inverts the input signal |
| Provides a constant and fixed gain | Reduces the bandwidth of the op-amp |
| Has a low output impedance | May introduce phase shift and distortion |
| Can perform mathematical operations | May suffer from noise and offset errors |
| Can invert the polarity of the input signal | May saturate or clip the output signal |

Some examples of applications of the inverting amplifier are:

- Signal conditioning: The inverting amplifier can be used to adjust the amplitude, polarity, and offset of the input signal to match the requirements of the next stage of the circuit.
- Mathematical operations: The inverting amplifier can be used to perform addition, subtraction, integration, differentiation, and scaling of the input signal by using appropriate resistors and capacitors in the feedback loop.
- Voltage inversion: The inverting amplifier can be used to generate a negative voltage from a positive voltage source or vice versa.
- Impedance transformation: The inverting amplifier can be used to match the impedance of the input signal to the impedance of the load or the next stage of the circuit by choosing suitable values of R1 and R2.
- Other applications: The inverting amplifier can be used for audio amplification, analog computation, active filtering, waveform generation, and modulation.