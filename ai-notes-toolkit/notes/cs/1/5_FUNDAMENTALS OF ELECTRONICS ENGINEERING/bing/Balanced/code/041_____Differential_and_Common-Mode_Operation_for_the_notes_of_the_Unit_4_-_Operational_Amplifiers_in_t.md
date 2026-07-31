### Differential and Common-Mode Operation of Operational Amplifiers

- An operational amplifier (op-amp) is a circuit that can amplify a small input signal into a large output signal, with high input impedance and low output impedance.
- An op-amp can be used in different modes of operation, depending on the nature and configuration of its inputs and outputs.
- The two main modes of operation are differential mode and common mode.

#### Differential Mode

- In differential mode, the op-amp amplifies the difference between the two input signals, and provides a single-ended output.
- The differential mode gain (Ad) is the ratio of the output voltage (Vout) to the differential input voltage (Vd), where Vd = V1 - V2, and V1 and V2 are the input voltages.
- The differential mode gain is usually very high, in the order of 10^5 or more.
- The differential mode operation is useful for applications such as signal processing, filtering, instrumentation, and feedback control.

#### Common Mode

- In common mode, the op-amp amplifies the average of the two input signals, and provides a single-ended output.
- The common mode gain (Ac) is the ratio of the output voltage (Vout) to the common mode input voltage (Vc), where Vc = (V1 + V2) / 2, and V1 and V2 are the input voltages.
- The common mode gain is usually very low, in the order of 10^-3 or less.
- The common mode operation is not desirable, as it introduces noise and interference to the output signal.

#### Common-Mode Rejection Ratio (CMRR)

- The common-mode rejection ratio (CMRR) is a measure of how well the op-amp can reject the common mode signal and amplify only the differential mode signal.
- The CMRR is defined as the ratio of the differential mode gain (Ad) to the common mode gain (Ac), in decibels (dB).
- The CMRR is usually very high, in the order of 10^2 dB or more.
- The higher the CMRR, the better the op-amp can perform in differential mode and suppress the noise and interference in common mode.

#### Fully-Differential Amplifier

- A fully-differential amplifier is a special type of op-amp that has differential inputs and differential outputs.
- The differential output voltage (Vod) is the difference between the two output voltages (Vo1 and Vo2), where Vod = Vo1 - Vo2.
- The differential output voltage is proportional to the differential input voltage (Vd), with a gain factor (Afd).
- The output common-mode voltage (Voc) is the average of the two output voltages (Vo1 and Vo2), where Voc = (Vo1 + Vo2) / 2.
- The output common-mode voltage can be controlled independently of the differential output voltage, by adjusting a reference voltage (Vref) or a feedback network.
- The fully-differential amplifier has several advantages over the standard op-amp, such as higher CMRR, lower distortion, lower noise, and better immunity to power supply variations.