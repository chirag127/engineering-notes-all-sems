# Differential and Common-Mode Operation of Op-Amp

- An op-amp (operational amplifier) is a device that can amplify the difference between two input signals and provide a single output signal.
- The input signals are called the differential input voltage, denoted by Vd, and the output signal is called the differential output voltage, denoted by Vout.
- The ratio of the differential output voltage to the differential input voltage is called the differential voltage gain, denoted by Ad.
- Vout = Ad * Vd
- The differential voltage gain is ideally infinite, meaning that the output voltage can be very large even for a small input voltage difference.
- However, in reality, the op-amp has some limitations on the input and output voltage ranges, which affect its performance and accuracy.

## Common-Mode Operation

- Common-mode operation is when the input signals are equal and have the same polarity, meaning that they have the same voltage with respect to a common reference point, usually ground.
- The common-mode input voltage is denoted by Vcm, and the common-mode output voltage is denoted by Vcmo.
- The ratio of the common-mode output voltage to the common-mode input voltage is called the common-mode voltage gain, denoted by Acm.
- Vcmo = Acm * Vcm
- The common-mode voltage gain is ideally zero, meaning that the output voltage is unaffected by the common-mode input voltage.
- However, in reality, the op-amp has some common-mode voltage gain, which causes the output voltage to change with the common-mode input voltage. This is undesirable, as it introduces noise and distortion to the output signal.

## Differential-Mode Operation

- Differential-mode operation is when the input signals are unequal and have opposite polarity, meaning that they have different voltages with respect to a common reference point, usually ground.
- The differential input voltage is the difference between the two input voltages, denoted by Vd.
- Vd = V1 - V2
- The differential output voltage is the output voltage with respect to the common reference point, denoted by Vout.
- The differential voltage gain is the ratio of the differential output voltage to the differential input voltage, denoted by Ad.
- Vout = Ad * Vd
- The differential voltage gain is ideally infinite, meaning that the output voltage can be very large even for a small input voltage difference.
- However, in reality, the op-amp has some finite differential voltage gain, which limits the output voltage range and the accuracy of the amplification.

## Common-Mode Rejection Ratio

- The common-mode rejection ratio (CMRR) is a measure of how well the op-amp can reject the common-mode input voltage and amplify only the differential input voltage.
- The CMRR is defined as the ratio of the differential voltage gain to the common-mode voltage gain, denoted by CMRR.
- CMRR = Ad / Acm
- The CMRR is ideally infinite, meaning that the op-amp can completely ignore the common-mode input voltage and amplify only the differential input voltage.
- However, in reality, the op-amp has some finite CMRR, which means that the output voltage is affected by both the differential and the common-mode input voltages.
- The higher the CMRR, the better the op-amp can perform as a differential amplifier and reduce the noise and distortion in the output signal.