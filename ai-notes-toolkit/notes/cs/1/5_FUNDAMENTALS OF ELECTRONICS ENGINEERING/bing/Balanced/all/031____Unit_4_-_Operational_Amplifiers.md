# Unit 4 - Operational Amplifiers

- An operational amplifier (op-amp) is an integrated circuit that can amplify weak electric signals.
- An op-amp has two input pins and one output pin. Its basic role is to amplify and output the voltage difference between the two input pins.
- The two input pins are called the inverting input (-) and the non-inverting input (+). The output pin is usually denoted by Vout.
- The output voltage of an op-amp is proportional to the input voltage difference, multiplied by a factor called the open-loop gain (A). The open-loop gain is very large, typically in the order of 10^5 to 10^6.
- The open-loop gain is not stable and depends on many factors such as temperature, frequency, and supply voltage. Therefore, op-amps are usually used with external feedback components, such as resistors and capacitors, to control the gain and the operation of the amplifier.
- The feedback components are connected between the output and the input pins of the op-amp, forming a closed-loop circuit. The feedback can be positive or negative, depending on which input pin is connected to the output.
- Negative feedback reduces the gain of the op-amp, but improves its stability, linearity, bandwidth, and input impedance. Negative feedback is used for most op-amp applications, such as amplifiers, filters, oscillators, and comparators.
- Positive feedback increases the gain of the op-amp, but reduces its stability, linearity, bandwidth, and input impedance. Positive feedback is used for applications that require switching or hysteresis, such as Schmitt triggers and multivibrators.
- There are different types of op-amps, classified by their input and output characteristics. Some common types are:
  - Voltage amplifiers: take voltage in and produce voltage out.
  - Current amplifiers: take current in and produce current out.
  - Transconductance amplifiers: take voltage in and produce current out.
  - Transresistance amplifiers: take current in and produce voltage out.
- Op-amps are one of the basic and versatile building blocks of analog circuits. They can perform various mathematical operations, such as addition, subtraction, integration, differentiation, and logarithm, by using appropriate feedback components.
- Op-amps are also used to implement various linear and nonlinear functions, such as signal conditioning, filtering, modulation, demodulation, detection, and generation.