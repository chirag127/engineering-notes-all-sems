### Analysis of single phase AC Circuits consisting R-L-C combination (Series and Parallel)

In the steady-state analysis of single-phase AC circuits, we often come across circuits that consist of resistors, inductors, and capacitors. These circuits are known as R-L-C circuits, and they can be connected in either series or parallel configurations.

#### Series R-L-C Circuits

When resistors, inductors, and capacitors are connected in series, the total impedance of the circuit is the sum of the individual impedances. The total impedance can be calculated using the following formula:

$Z_{total}=\sqrt{(R^2+(\omega L-\frac{1}{\omega C})^2)}$

where R is the resistance, L is the inductance, C is the capacitance, and ω is the angular frequency of the AC source.

The phase angle between the current and voltage can be calculated using the following formula:

$\phi = \tan^{-1}(\frac{\omega L - \frac{1}{\omega C}}{R})$

where φ is the phase angle.

#### Parallel R-L-C Circuits

When resistors, inductors, and capacitors are connected in parallel, the total impedance of the circuit can be calculated using the following formula:

$\frac{1}{Z_{total}}=\sqrt{(\frac{1}{R^2}+\frac{1}{(\omega L - \frac{1}{\omega C})^2})}$

The phase angle between the current and voltage can be calculated using the following formula:

$\phi = \tan^{-1}(\frac{\frac{1}{\omega C}-\omega L}{R})$

#### Resonance in R-L-C Circuits

In R-L-C circuits, the resonant frequency is the frequency at which the impedance of the circuit is purely resistive. At resonance, the reactances of the inductor and capacitor cancel each other out, leaving only the resistance.

The resonant frequency can be calculated using the following formula:

$f_{resonance}=\frac{1}{2\pi\sqrt{LC}}$

At resonance, the current in the circuit is maximum, and the power factor is unity.

#### Quality Factor (Q) in R-L-C Circuits

The quality factor is a measure of the damping in an R-L-C circuit. It is defined as the ratio of the energy stored in the circuit to the energy dissipated per cycle.

The formula for quality factor is:

$Q=\frac{1}{R}\sqrt{\frac{L}{C}}$

A higher quality factor indicates less damping and more oscillations in the circuit.

In conclusion, the analysis of R-L-C circuits is an important part of steady-state analysis of single-phase AC circuits. Understanding the formulas and concepts related to series and parallel R-L-C circuits, resonance, and quality factor is vital for any electrical engineer.