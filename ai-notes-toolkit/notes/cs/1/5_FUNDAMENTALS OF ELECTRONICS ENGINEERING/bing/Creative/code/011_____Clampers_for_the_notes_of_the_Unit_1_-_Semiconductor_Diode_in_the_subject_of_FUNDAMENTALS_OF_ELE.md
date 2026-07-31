### Clampers

Clampers are electronic circuits that shift the dc level of the AC signal. They are also known as DC voltage restorers or level shifters . Clampers are used to add the dc level to the ac input signal without changing the peak-to-peak voltage of the waveform .

Clampers are basically classified as positive and negative that includes both biased and unbiased conditions individually. A positive clamper circuit (negative peak clamper) outputs a purely positive waveform from an input signal; it offsets the input signal so that all of the waveform is greater than 0 V. A negative clamper circuit (positive peak clamper) outputs a purely negative waveform from an input signal; it offsets the input signal so that all of the waveform is less than 0 V.

A biased clamper circuit adds a fixed dc voltage to the input signal, either positive or negative, depending on the polarity of the bias voltage . An unbiased clamper circuit does not add any fixed dc voltage to the input signal, but only shifts it to the desired level .

Clampers are composed of a diode, a capacitor, and a resistor . The diode determines the polarity of the clamping, the capacitor stores the peak voltage of the input signal, and the resistor discharges the capacitor when the input signal changes its polarity .

An application of the clamper circuit is as a “DC restorer” in “composite video” circuitry in both television transmitters and receivers. An NTSC (US video standard) video signal “white level” corresponds to a minimum (12.5%) transmitted power. The “black level” corresponds to a maximum (87.5%) transmitted power. The “sync level” corresponds to a 100% transmitted power. A clamper circuit can restore the dc level of the video signal so that the sync level is at 0 V and the black level is at 0.7 V.

The following diagram shows the circuit of a positive biased clamper:

![Positive biased clamper circuit](https://electronicscoach.com/wp-content/uploads/2018/03/positive-biased-clamper.png)

The following diagram shows the input and output waveforms of a positive biased clamper:

![Positive biased clamper waveforms](https://electronicscoach.com/wp-content/uploads/2018/03/positive-biased-clamper-waveform.png)

The following diagram shows the circuit of a negative biased clamper:

![Negative biased clamper circuit](https://electronicscoach.com/wp-content/uploads/2018/03/negative-biased-clamper.png)

The following diagram shows the input and output waveforms of a negative biased clamper:

![Negative biased clamper waveforms](https://electronicscoach.com/wp-content/uploads/2018/03/negative-biased-clamper-waveform.png)