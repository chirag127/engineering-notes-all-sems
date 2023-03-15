### Practical Op-Amp Circuits

Operational amplifiers (op-amps) are versatile and widely used electronic devices that can perform various functions such as amplification, filtering, integration, differentiation, etc. In this section, we will discuss some of the most common and fundamental op-amp circuits that are used in practical applications.

1. **Voltage Follower**: This is the simplest op-amp circuit that does not require any external components. It acts as a buffer that provides high input impedance and low output impedance, thus preventing loading effects and signal loss. The output voltage is equal to the input voltage, as shown in the following figure.

![Voltage Follower](https://www.arrow.com/-/media/arrow/images/articles/2018/10/01/voltage-follower.png?h=400&w=400&la=en&hash=8F0F1F9F0C9B9F7F8F0F1F9F0C9B9F7F8F0F1F9F)

2. **Inverting Op-Amp**: This circuit uses a resistor (R2) to feed back the output to the negative or inverting input of the op-amp. The input signal is applied to the positive or non-inverting input through another resistor (R1). The output voltage is inverted and proportional to the input voltage, with a gain of -R2/R1, as shown in the following figure.

![Inverting Op-Amp](https://www.arrow.com/-/media/arrow/images/articles/2018/10/01/inverting-op-amp.png?h=400&w=400&la=en&hash=8F0F1F9F0C9B9F7F8F0F1F9F0C9B9F7F8F0F1F9F)

3. **Non-inverting Op-Amp**: This circuit uses a resistor (R2) to feed back the output to the positive or non-inverting input of the op-amp. The input signal is applied to the negative or inverting input through another resistor (R1). The output voltage is in phase and proportional to the input voltage, with a gain of 1 + R2/R1, as shown in the following figure.

![Non-inverting Op-Amp](https://www.arrow.com/-/media/arrow/images/articles/2018/10/01/non-inverting-op-amp.png?h=400&w=400&la=en&hash=8F0F1F9F0C9B9F7F8F0F1F9F0C9B9F7F8F0F1F9F)

4. **Non-inverting Summing Amplifier**: This circuit uses two or more resistors (R1, R2, ...) to apply multiple input signals to the positive or non-inverting input of the op-amp. The output voltage is in phase and proportional to the sum of the input voltages, with a gain of 1 + Rf/Rg, where Rf is the feedback resistor and Rg is the common resistor, as shown in the following figure.

![Non-inverting Summing Amplifier](https://www.arrow.com/-/media/arrow/images/articles/2018/10/01/non-inverting-summing-amplifier.png?h=400&w=400&la=en&hash=8F0F1F9F0C9B9F7F8F0F1F9F0C9B9F7F8F0F1F9F)

5. **Inverting Summing Amplifier**: This circuit uses two or more resistors (R1, R2, ...) to apply multiple input signals to the negative or inverting input of the op-amp. The output voltage is inverted and proportional to the sum of the input voltages, with a gain of -Rf/Rg, where Rf is the feedback resistor and Rg is the common resistor, as shown in the following figure.

![Inverting Summing Amplifier](https://www.arrow.com/-/media/arrow/images/articles/2018/10/01/inverting-summing-amplifier.png?h=400&w=400&la=en&hash=8F0F1F9F0C9B9F7F8F0F1F9F0C9B9F7F8F0F1F9F)

6.