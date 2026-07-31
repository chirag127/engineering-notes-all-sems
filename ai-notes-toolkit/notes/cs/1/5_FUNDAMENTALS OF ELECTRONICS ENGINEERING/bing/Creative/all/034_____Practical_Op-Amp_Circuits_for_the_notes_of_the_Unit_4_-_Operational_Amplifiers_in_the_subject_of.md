# Practical Op-Amp Circuits

Operational amplifiers (op-amps) are versatile and widely used electronic devices that can perform various functions such as amplification, filtering, integration, differentiation, etc. In this note, we will discuss some of the common and useful op-amp circuits that can be used for various applications.

## 1. Voltage Follower

The voltage follower is the simplest op-amp circuit, as it does not require any external components. It is also called a buffer, as it isolates the input from the output and prevents loading effects. The voltage follower has a unity gain, which means that the output voltage is equal to the input voltage. The circuit diagram and the input-output characteristics are shown below.

![Voltage follower circuit diagram](https://www.arrow.com/-/media/arrow/images/articles/2018/10/arrow_fundamentals_of_op_amp_circuits_1.png?h=400&w=400&la=en&hash=0F2F1B7F3E3E3A7B0F6F9F7F9F0F9F9F9F9F9F9F)

![Voltage follower input-output characteristics](https://www.arrow.com/-/media/arrow/images/articles/2018/10/arrow_fundamentals_of_op_amp_circuits_2.png?h=400&w=400&la=en&hash=0F2F1B7F3E3E3A7B0F6F9F7F9F0F9F9F9F9F9F9F)

The voltage follower can be used to:

- Provide impedance matching between different stages of a circuit
- Drive low-impedance loads such as speakers or LEDs
- Extend the bandwidth of a circuit by reducing the capacitive loading
- Protect sensitive inputs from noise or interference

## 2. Inverting Op-Amp

The inverting op-amp is a basic circuit that can perform voltage amplification with a negative gain. The output voltage is proportional to the input voltage, but with an opposite polarity. The gain of the circuit is determined by the ratio of the feedback resistor R2 to the input resistor R1. The circuit diagram and the input-output characteristics are shown below.

![Inverting op-amp circuit diagram](https://www.arrow.com/-/media/arrow/images/articles/2018/10/arrow_fundamentals_of_op_amp_circuits_3.png?h=400&w=400&la=en&hash=0F2F1B7F3E3E3A7B0F6F9F7F9F0F9F9F9F9F9F9F)

![Inverting op-amp input-output characteristics](https://www.arrow.com/-/media/arrow/images/articles/2018/10/arrow_fundamentals_of_op_amp_circuits_4.png?h=400&w=400&la=en&hash=0F2F1B7F3E3E3A7B0F6F9F7F9F0F9F9F9F9F9F9F)

The inverting op-amp can be used to:

- Amplify signals with a desired gain and polarity
- Perform mathematical operations such as subtraction and scaling
- Implement active filters such as low-pass, high-pass, band-pass, etc.
- Generate oscillations and waveforms

## 3. Non-inverting Op-Amp

The non-inverting op-amp is another basic circuit that can perform voltage amplification with a positive gain. The output voltage is proportional to the input voltage, but with the same polarity. The gain of the circuit is determined by the ratio of the feedback resistor R2 to the input resistor R1, plus one. The circuit diagram and the input-output characteristics are shown below.

![Non-inverting op-amp circuit diagram](https://www.arrow.com/-/media/arrow/images/articles/2018/10/arrow_fundamentals_of_op_amp_circuits_5.png?h=400&w=400&la=en&hash=0F2F1B7F3E3E3A7B0F6F9F7F9F0F9F9F9F9F9F9F)
