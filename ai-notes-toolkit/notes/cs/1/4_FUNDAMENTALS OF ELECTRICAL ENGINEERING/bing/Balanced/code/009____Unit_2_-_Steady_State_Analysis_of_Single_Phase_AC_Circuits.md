## Unit 2 - Steady State Analysis of Single Phase AC Circuits

- Single phase AC circuits are electrical circuits that are powered by alternating current (AC) sources with a single frequency and phase.
- AC sources produce sinusoidal voltages and currents that vary periodically with time.
- The frequency of an AC source is the number of cycles per second, measured in hertz (Hz).
- The phase of an AC source is the angle that the sinusoidal waveform makes with the horizontal axis at a given instant, measured in degrees or radians.
- The amplitude of an AC source is the maximum value of the sinusoidal waveform, measured in volts (V) or amperes (A).
- The root mean square (RMS) value of an AC source is the effective value that produces the same power as a direct current (DC) source of the same magnitude, given by:

```math
V_{rms} = \frac{V_{max}}{\sqrt{2}}
I_{rms} = \frac{I_{max}}{\sqrt{2}}
```

- The average value of an AC source over one cycle is zero, since the positive and negative halves cancel out.
- The average power delivered by an AC source to a resistive load is given by:

```math
P_{avg} = V_{rms} I_{rms} \cos \phi
```

where $\phi$ is the phase difference between the voltage and the current.

- The power factor of an AC circuit is the ratio of the average power to the apparent power, given by:

```math
pf = \frac{P_{avg}}{V_{rms} I_{rms}} = \cos \phi
```

- The power factor indicates how efficiently the AC circuit utilizes the power supplied by the source. A power factor of 1 means that the voltage and the current are in phase and the circuit is purely resistive. A power factor of 0 means that the voltage and the current are out of phase by 90 degrees and the circuit is purely reactive (inductive or capacitive).
- The impedance of an AC circuit is the ratio of the phasor voltage to the phasor current, given by:

```math
Z = \frac{V}{I} = R + jX
```

where $R$ is the resistance and $X$ is the reactance of the circuit. The impedance is a complex number that has a magnitude and a phase angle, given by:

```math
|Z| = \sqrt{R^2 + X^2}
\angle Z = \tan^{-1} \frac{X}{R}
```

- The impedance of a resistor is equal to its resistance and has no phase angle.
- The impedance of an inductor is proportional to its inductance and the frequency of the AC source, and has a positive phase angle of 90 degrees, given by:

```math
Z_L = j \omega L
\angle Z_L = 90^{\circ}
```

where $\omega = 2 \pi f$ is the angular frequency of the AC source and $L$ is the inductance of the inductor.
- The impedance of a capacitor is inversely proportional to its capacitance and the frequency of the AC source, and has a negative phase angle of 90 degrees, given by:

```math
Z_C = \frac{1}{j \omega C}
\angle Z_C = -90^{\circ}
```

where $C$ is the capacitance of the capacitor.
- The impedance of a series AC circuit is the sum of the impedances of the individual components, given by:

```math
Z_{series} = Z_1 + Z_2 + ... + Z_n
```

- The impedance of a parallel AC circuit is the reciprocal of the sum of the reciprocals of the impedances of the individual components, given by:

```math
Z_{parallel} = \frac{1}{\frac{1}{Z_1} + \frac{1}{Z_2} + ... + \frac{1}{Z_n}}
```

- The phasor diagram of an AC circuit is a graphical representation of the voltages and currents as vectors in the complex plane, with the reference phasor being the source voltage. The phasor diagram can be used to find the impedance, the power factor, and the phase difference of the AC circuit.