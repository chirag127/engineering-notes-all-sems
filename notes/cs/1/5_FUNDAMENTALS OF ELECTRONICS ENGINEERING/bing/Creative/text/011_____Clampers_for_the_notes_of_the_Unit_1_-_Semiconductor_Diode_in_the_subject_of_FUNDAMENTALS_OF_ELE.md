### Clampers

- Clampers are electronic circuits that shift the dc level of the AC signal .
- Clampers are also known as DC voltage restorers or level shifter.
- Clampers are used to add the dc level to the ac input signal. The input swing of a waveform is equal to the output swing.
- Clampers can be classified as positive or negative, and biased or unbiased.
- A positive clamper circuit (negative peak clamper) outputs a purely positive waveform from an input signal; it offsets the input signal so that all of the waveform is greater than 0 V.
- A negative clamper circuit (positive peak clamper) outputs a purely negative waveform from an input signal; it offsets the input signal so that all of the waveform is less than 0 V.
- A biased clamper circuit adds a fixed dc voltage to the input signal, either positive or negative, depending on the polarity of the bias.
- An unbiased clamper circuit does not add any dc voltage to the input signal, but only shifts it up or down.
- An application of the clamper circuit is as a “DC restorer” in “composite video” circuitry in both television transmitters and receivers. An NTSC (US video standard) video signal “white level” corresponds to a minimum (12.5%) transmitted power.
- A clamper circuit consists of a diode, a capacitor, and a resistor. The diode conducts during one half cycle of the input signal and charges the capacitor to a peak voltage. The capacitor maintains this voltage during the other half cycle and adds it to the input signal, thus shifting the dc level.
- The resistor in the clamper circuit is used to discharge the capacitor when the input signal is removed, and to limit the current through the diode. The resistor value should be large enough to avoid excessive power dissipation, but small enough to allow the capacitor to charge and discharge quickly.
- The clamper circuit can be analyzed using the concept of virtual ground. The virtual ground is the point where the voltage is zero with respect to the ground, regardless of the current flowing through it. The virtual ground in a clamper circuit is the anode of the diode when it is forward biased.