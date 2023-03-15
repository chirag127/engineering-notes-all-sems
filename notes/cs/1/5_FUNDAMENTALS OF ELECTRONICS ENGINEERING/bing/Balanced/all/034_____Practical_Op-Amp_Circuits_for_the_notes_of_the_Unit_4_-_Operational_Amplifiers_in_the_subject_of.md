# Practical Op-Amp Circuits

Operational amplifiers (op-amps) are versatile and widely used electronic devices that can perform various functions such as amplification, filtering, integration, differentiation, etc. In this note, we will discuss some of the common and useful op-amp circuits that can be used for various applications.

## Voltage Follower

The voltage follower is the simplest op-amp circuit, as it does not require any external components. It is also called a buffer, as it isolates the input from the output and prevents loading effects. The voltage follower has a unity gain, meaning that the output voltage is equal to the input voltage. The circuit diagram and the input-output characteristics are shown below.

![Voltage follower circuit diagram](https://www.arrow.com/-/media/arrow/images/articles/2018/10/arrow-fundamentals-of-op-amp-circuits-1.png?h=400&w=600&la=en&hash=0F7F0E9B9F7A9F9F9A9F9F9F9F9F9F9F9F9F9F9F)

![Voltage follower input-output characteristics](https://www.arrow.com/-/media/arrow/images/articles/2018/10/arrow-fundamentals-of-op-amp-circuits-2.png?h=400&w=600&la=en&hash=0F7F0E9B9F7A9F9F9A9F9F9F9F9F9F9F9F9F9F9F)

The voltage follower can be used to:

- Provide impedance matching between a high-impedance source and a low-impedance load.
- Drive capacitive loads without stability issues.
- Extend the bandwidth of a signal by reducing the Miller effect.

## Inverting Op-Amp

The inverting op-amp is a basic circuit that uses a resistor (R2) to feed back the output to the negative or inverting input. Another resistor (R1) is connected between the input and the inverting input. The inverting op-amp has a negative gain, meaning that the output voltage is inverted and proportional to the input voltage. The gain is given by the ratio of the resistors: A = -R2/R1. The circuit diagram and the input-output characteristics are shown below.

![Inverting op-amp circuit diagram](https://www.arrow.com/-/media/arrow/images/articles/2018/10/arrow-fundamentals-of-op-amp-circuits-3.png?h=400&w=600&la=en&hash=0F7F0E9B9F7A9F9F9A9F9F9F9F9F9F9F9F9F9F9F)

![Inverting op-amp input-output characteristics](https://www.arrow.com/-/media/arrow/images/articles/2018/10/arrow-fundamentals-of-op-amp-circuits-4.png?h=400&w=600&la=en&hash=0F7F0E9B9F7A9F9F9A9F9F9F9F9F9F9F9F9F9F9F)

The inverting op-amp can be used to:

- Amplify a signal with a desired gain and polarity.
- Perform mathematical operations such as subtraction and scaling.
- Implement active filters such as low-pass, high-pass, band-pass, and notch filters.

## Non-inverting Op-Amp

The non-inverting op-amp is similar to the inverting op-amp, except that the input is connected to the positive or non-inverting input, and the feedback resistor (R2) is connected between the output and the inverting input. The non-inverting op-amp has a positive gain, meaning that the output voltage is in phase and proportional to the input voltage. The gain is given by the expression: A = 1 + R2/R1. The circuit diagram and the input-output characteristics are shown below.
