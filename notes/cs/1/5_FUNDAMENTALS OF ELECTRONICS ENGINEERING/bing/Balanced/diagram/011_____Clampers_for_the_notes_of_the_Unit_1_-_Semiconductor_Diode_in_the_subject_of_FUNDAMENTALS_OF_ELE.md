### Clampers

- Clampers are electronic circuits that shift the dc level of the AC signal .
- Clampers are also known as DC voltage restorers or level shifter.
- Clampers are used to add the dc level to the ac input signal. The input swing of a waveform is equal to the output swing.
- Clampers can be classified as positive or negative, and biased or unbiased.
- A positive clamper circuit (negative peak clamper) outputs a purely positive waveform from an input signal; it offsets the input signal so that all of the waveform is greater than 0 V.
- A negative clamper circuit (positive peak clamper) outputs a purely negative waveform from an input signal; it offsets the input signal so that all of the waveform is less than 0 V.
- A biased clamper circuit adds a fixed dc voltage to the input signal, either positive or negative, depending on the polarity of the bias.
- An unbiased clamper circuit does not add any dc voltage to the input signal, but only shifts it up or down.
- An example of a clamper circuit is a diode and a capacitor connected in parallel across the input signal .
- The diode allows the capacitor to charge or discharge during one half cycle of the input signal, and blocks the current during the other half cycle .
- The capacitor maintains a constant voltage across its terminals, which is added to or subtracted from the input signal, depending on the orientation of the diode .
- A clamper circuit can be represented by the following diagram :

![Clamper circuit diagram](https://electronicscoach.com/wp-content/uploads/2018/03/clamper-circuit.png)

- An application of the clamper circuit is as a “DC restorer” in “composite video” circuitry in both television transmitters and receivers.
- A video signal “white level” corresponds to a minimum transmitted power, and a “black level” corresponds to a maximum transmitted power.
- A clamper circuit can restore the dc level of the video signal to the correct value, so that the brightness and contrast of the image are preserved.