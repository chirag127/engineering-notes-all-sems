### Differential and Common-Mode Operation

- A differential amplifier is a circuit that can accept two input signals and amplify the difference between these two input signals.
- An op-amp is a type of differential amplifier that has a very high voltage gain and a very high input impedance.
- The differential input voltage of an op-amp is the difference between the voltages applied to the two input terminals, denoted by Vd = V+ - V-.
- The common-mode input voltage of an op-amp is the average of the voltages applied to the two input terminals, denoted by Vcm = (V+ + V-) / 2.
- The differential output voltage of an op-amp is the voltage at the output terminal with respect to ground, denoted by Vout.
- The common-mode output voltage of an op-amp is the voltage at the output terminal with respect to the common-mode input voltage, denoted by Vout - Vcm.
- The differential mode operation of an op-amp is when the input signals have opposite polarities and the output voltage is proportional to the differential input voltage.
- The common-mode operation of an op-amp is when the input signals have the same polarity and the output voltage is proportional to the common-mode input voltage.
- The common-mode rejection ratio (CMRR) of an op-amp is a measure of how well the op-amp rejects the common-mode input voltage and amplifies only the differential input voltage.
- The CMRR is defined as the ratio of the differential voltage gain to the common-mode voltage gain, denoted by CMRR = Ad / Ac.
- The ideal op-amp has an infinite CMRR, meaning that it completely rejects the common-mode input voltage and amplifies only the differential input voltage.
- The practical op-amp has a finite CMRR, meaning that it has some sensitivity to the common-mode input voltage and some distortion in the output voltage.
- The CMRR is usually expressed in decibels (dB), which is 20 times the logarithm of the ratio, denoted by CMRR(dB) = 20 log (Ad / Ac).
- The higher the CMRR, the better the performance of the op-amp in differential mode operation.
- The lower the CMRR, the more the op-amp is affected by common-mode interference or noise.

: https://resources.system-analysis.cadence.com/blog/msa2021-understanding-common-mode-vs-differential-mode-signals
: https://www.mphysicstutorial.com/2021/01/differential-amplifier-common-mode-rejection-ratio-common-differential-mode-signals.html
: https://www.analog.com/media/en/training-seminars/tutorials/MT-041.pdf