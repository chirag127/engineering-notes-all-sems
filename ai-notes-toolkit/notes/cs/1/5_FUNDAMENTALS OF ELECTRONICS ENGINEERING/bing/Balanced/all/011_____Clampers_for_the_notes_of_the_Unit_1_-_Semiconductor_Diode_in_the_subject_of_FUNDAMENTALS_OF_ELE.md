# Clampers

- Clampers are electronic circuits that shift the dc level of the AC signal .
- Clampers are also known as DC voltage restorers or level shifter.
- Clampers are used to add the dc level to the ac input signal. The input swing of a waveform is equal to the output swing.
- Clampers can be classified as positive or negative, and biased or unbiased.
- A positive clamper circuit (negative peak clamper) outputs a purely positive waveform from an input signal; it offsets the input signal so that all of the waveform is greater than 0 V.
- A negative clamper circuit (positive peak clamper) outputs a purely negative waveform from an input signal; it offsets the input signal so that all of the waveform is less than 0 V.
- A biased clamper circuit adds a fixed dc voltage to the input signal, either positive or negative, depending on the polarity of the bias voltage.
- An unbiased clamper circuit does not add any dc voltage to the input signal, but only shifts it up or down by the peak value of the input signal.
- An example of a clamper circuit is a diode and a capacitor connected in parallel across the input signal. The diode conducts when the input signal is positive or negative, depending on the orientation of the diode, and charges the capacitor to the peak value of the input signal. The capacitor then acts as a dc source that shifts the input signal up or down by the peak value.
- An application of the clamper circuit is as a “DC restorer” in “composite video” circuitry in both television transmitters and receivers. An NTSC (US video standard) video signal “white level” corresponds to a minimum (12.5%) transmitted power. A clamper circuit can restore the dc level of the video signal so that the white level corresponds to the maximum transmitted power.