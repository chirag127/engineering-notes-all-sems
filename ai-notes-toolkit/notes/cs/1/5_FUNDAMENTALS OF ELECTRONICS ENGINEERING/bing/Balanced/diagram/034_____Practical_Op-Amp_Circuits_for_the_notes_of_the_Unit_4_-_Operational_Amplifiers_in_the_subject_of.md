### Practical Op-Amp Circuits

An operational amplifier (op-amp) is a versatile device that can be used to amplify signals, filter signals, perform mathematical operations and more. Op-amps are usually used in conjunction with passive components such as resistors and capacitors to create various circuits with different functions. Some of the most common and fundamental op-amp circuits are:

- **Voltage follower**: This is the simplest op-amp circuit, where the output voltage is equal to the input voltage. It does not require any external components and it provides a high input impedance and a low output impedance. It can be used to isolate or buffer a signal from a source or a load. 

- **Inverting op-amp**: This is a circuit where the output voltage is proportional to the input voltage, but with opposite polarity. It requires a feedback resistor (R2) and an input resistor (R1) to set the gain of the circuit. The gain is given by -R2/R1. It can be used to invert or amplify a signal. 

- **Non-inverting op-amp**: This is a circuit where the output voltage is proportional to the input voltage, but with the same polarity. It requires a feedback resistor (R2) and a resistor (R1) to set the gain of the circuit. The gain is given by 1 + R2/R1. It can be used to amplify a signal without changing its polarity. 

- **Non-inverting summing amplifier**: This is a circuit where the output voltage is proportional to the sum of the input voltages, but with the same polarity. It requires a feedback resistor (Rf) and a resistor (R) for each input voltage to set the gain of the circuit. The gain for each input is given by Rf/R. It can be used to add or mix signals. 

- **Inverting summing amplifier**: This is a circuit where the output voltage is proportional to the sum of the input voltages, but with opposite polarity. It requires a feedback resistor (Rf) and an input resistor (R) for each input voltage to set the gain of the circuit. The gain for each input is given by -Rf/R. It can be used to subtract or mix signals. 

- **Differential amplifier**: This is a circuit where the output voltage is proportional to the difference of the input voltages. It requires two resistors (R1 and R2) for each input voltage and a feedback resistor (Rf) to set the gain of the circuit. The gain is given by Rf/R1. It can be used to measure or amplify the difference between two signals. 

- **Integrator**: This is a circuit where the output voltage is proportional to the integral of the input voltage. It requires a feedback capacitor (Cf) and an input resistor (R) to set the time constant of the circuit. The time constant is given by RC. It can be used to perform integration or low-pass filtering. 

- **Differentiator**: This is a circuit where the output voltage is proportional to the derivative of the input voltage. It requires a feedback resistor (Rf) and an input capacitor (C) to set the time constant of the circuit. The time constant is given by RC. It can be used to perform differentiation or high-pass filtering. 

- **Comparator**: This is a circuit where the output voltage is either high or low, depending on whether the input voltage is higher or lower than a reference voltage. It does not require any feedback components and it operates in the open-loop mode. It can be used to compare or detect signals. 

- **Schmitt trigger**: This is a circuit where the output voltage is either high or low, depending on whether the input voltage crosses a certain threshold. It requires a feedback resistor (Rf) and a resistor (R) to set the hysteresis of the circuit. The hysteresis is the difference between the upper and lower thresholds. It can be used to eliminate noise or oscillations in signals. 

The following diagram shows the schematic symbols and the basic configurations of these op-amp circuits:

![Op-amp circuits diagram](https://i.imgur.com/8zvYwYB.png)