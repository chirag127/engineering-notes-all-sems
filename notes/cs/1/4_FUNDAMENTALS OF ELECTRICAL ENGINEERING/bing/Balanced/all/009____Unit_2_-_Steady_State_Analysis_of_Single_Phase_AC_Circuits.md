# Unit 2 - Steady State Analysis of Single Phase AC Circuits

## Introduction

- A single phase AC circuit is a circuit that is powered by a single alternating voltage or current source.
- The voltage and current in a single phase AC circuit vary sinusoidally with time and have the same frequency.
- The steady state analysis of a single phase AC circuit involves finding the voltage, current, power and power factor across different elements or combinations of elements in the circuit.

## Basic Concepts

- The sinusoidal voltage and current in a single phase AC circuit can be represented by phasors, which are complex numbers that indicate the magnitude and phase angle of the sinusoidal quantities.
- The phasor diagram of a single phase AC circuit shows the relative positions of the voltage and current phasors for different elements or combinations of elements in the circuit.
- The impedance of an element or a combination of elements in a single phase AC circuit is the ratio of the phasor voltage to the phasor current across it. It is also a complex number that indicates the opposition to the flow of AC current.
- The impedance of a resistor is equal to its resistance and has zero phase angle. The impedance of an inductor is equal to jωL, where j is the imaginary unit, ω is the angular frequency and L is the inductance. It has a positive phase angle of 90°. The impedance of a capacitor is equal to 1/jωC, where C is the capacitance. It has a negative phase angle of 90°.
- The impedance of a series combination of elements is equal to the sum of the impedances of the individual elements. The impedance of a parallel combination of elements is equal to the reciprocal of the sum of the reciprocals of the impedances of the individual elements.
- The voltage and current in a single phase AC circuit are in phase when the impedance is purely resistive, leading when the impedance is purely inductive and lagging when the impedance is purely capacitive.
- The power in a single phase AC circuit is the product of the voltage and current. It consists of two components: the active power (P), which is the average power delivered or consumed by the circuit, and the reactive power (Q), which is the power that is stored and released by the inductive and capacitive elements in the circuit. The active power is given by P = VI cos θ, where V and I are the rms values of the voltage and current and θ is the phase angle between them. The reactive power is given by Q = VI sin θ.
- The power factor of a single phase AC circuit is the ratio of the active power to the apparent power (S), which is the product of the rms values of the voltage and current. It is also equal to the cosine of the phase angle between the voltage and current. The power factor indicates how efficiently the circuit utilizes the power supplied by the source. It ranges from 0 to 1, with 1 being the ideal value. A low power factor means that the circuit draws more current than necessary and causes more losses in the transmission lines.
- The power factor of a single phase AC circuit can be improved by adding a capacitor or an inductor in parallel with the load, such that the reactive power of the capacitor or the inductor cancels out the reactive power of the load. This is called power factor correction.

## Examples

- Example 1: Find the impedance, current, power and power factor of a single phase AC circuit that consists of a 120 V rms source and a series combination of a 10 Ω resistor, a 0.1 H inductor and a 50 μF capacitor. Assume a frequency of 60 Hz.

  - Solution: The impedance of the circuit is given by Z = R + jωL - 1/jωC, where ω = 2πf. Substituting the values, we get Z = 10 + j(0.1)(2π)(60) - 1/j(50×10^-6)(2π)(60) = 10 + j37.7 - j53.1 = 10 - j15.4 Ω. The magnitude of the impedance is |Z| = √(10^2 + (-15.4)^2) = 18.4 Ω. The phase angle of the impedance is θ = tan^-1(-15.4/10) = -56.6°.
  - The current in the circuit is given by I = V/Z, where V is the phasor voltage of the source. Substituting the values, we get I = 120∠0° / 10 - j15.4 =