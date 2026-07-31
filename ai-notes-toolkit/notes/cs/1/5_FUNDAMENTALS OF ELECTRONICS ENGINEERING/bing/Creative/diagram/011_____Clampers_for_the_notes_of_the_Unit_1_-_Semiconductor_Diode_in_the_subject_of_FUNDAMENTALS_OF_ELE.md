### Clampers

- Clampers are electronic circuits that change the DC level of an AC signal without changing its shape  .
- Clampers are also known as DC voltage restorers or level shifters.
- Clampers are used to add a DC level to an AC input signal. For example, a clamper can shift a signal that oscillates between -5 V and 5 V to a signal that oscillates between 0 V and 10 V.
- Clampers are composed of a diode, a capacitor, and a resistor  .
- Clampers can be classified into four types: positive clamper, negative clamper, positive biased clamper, and negative biased clamper  .
- A positive clamper (or negative peak clamper) shifts the input signal so that the negative peak of the signal is at 0 V . A positive clamper circuit is shown below:

![Positive clamper circuit](https://www.physics-and-radio-electronics.com/images/positive-clamper-circuit.png)

- A negative clamper (or positive peak clamper) shifts the input signal so that the positive peak of the signal is at 0 V . A negative clamper circuit is shown below:

![Negative clamper circuit](https://www.physics-and-radio-electronics.com/images/negative-clamper-circuit.png)

- A positive biased clamper adds a positive DC voltage to the input signal, shifting it upward  . A positive biased clamper circuit is shown below:

![Positive biased clamper circuit](https://www.physics-and-radio-electronics.com/images/positive-biased-clamper-circuit.png)

- A negative biased clamper adds a negative DC voltage to the input signal, shifting it downward  . A negative biased clamper circuit is shown below:

![Negative biased clamper circuit](https://www.physics-and-radio-electronics.com/images/negative-biased-clamper-circuit.png)

- The operation of a clamper circuit depends on the charging and discharging of the capacitor through the diode and the resistor  .
- The capacitor charges to the peak value of the input signal during the first half cycle, and then discharges through the resistor during the second half cycle  .
- The diode allows the current to flow only in one direction, either during the positive or the negative half cycle, depending on the polarity of the diode  .
- The resistor determines the time constant of the circuit, which affects the speed of the charging and discharging of the capacitor  .
- The output voltage of a clamper circuit is equal to the input voltage plus or minus the voltage across the capacitor  .
- The output waveform of a clamper circuit is shown below for different types of clampers:

![Output waveform of a clamper circuit](https://www.physics-and-radio-electronics.com/images/output-waveform-of-a-clamper-circuit.png)

- Clampers have applications in DC restoration, peak detection, and modulation  .
- A clamper can be used as a DC restorer to restore the DC component of a signal that has been lost or distorted during transmission or processing.
- A clamper can be used as a peak detector to measure the peak value of an AC signal.
- A clamper can be used as a modulator to modulate an AC signal with a DC signal. For example, a clamper can be used to modulate a video signal with a sync pulse.