# Analysis of single phase AC Circuits consisting R-L-C combination (Series and Parallel)

- A single phase AC circuit is a circuit that is powered by a single alternating voltage or current source.
- A R-L-C circuit is a circuit that contains a resistor (R), an inductor (L) and a capacitor (C) as its elements.
- A R-L-C circuit can be connected in series or parallel, depending on how the elements are arranged with respect to the voltage or current source.
- The analysis of R-L-C circuits involves finding the voltage, current, power, impedance, admittance, phase angle and resonance frequency of the circuit and its elements.

## Series R-L-C Circuit

- A series R-L-C circuit is a circuit where the resistor, inductor and capacitor are connected in series across a voltage source.
- The voltage source can be represented by a phasor V with an angle θ.
- The voltage across each element can be represented by a phasor VR, VL and VC with angles θR, θL and θC respectively.
- The current through the circuit can be represented by a phasor I with an angle θI, which is the same for all elements.
- The total impedance of the circuit can be represented by a phasor Z with an angle θZ, which is the sum of the impedances of the elements.
- The impedance of the resistor is ZR = R with an angle θR = 0°.
- The impedance of the inductor is ZL = jωL with an angle θL = 90°, where ω is the angular frequency and L is the inductance.
- The impedance of the capacitor is ZC = 1/jωC with an angle θC = -90°, where C is the capacitance.
- The phasor diagram of the series R-L-C circuit is shown below:

![Phasor diagram of series R-L-C circuit](https://www.electronics-tutorials.ws/wp-content/uploads/2018/05/accircuits-acp64.gif)

- The voltage phasors can be obtained by applying Kirchhoff's voltage law (KVL) to the circuit, which states that the sum of the voltage drops around a closed loop is zero.
- The current phasor can be obtained by applying Ohm's law to the circuit, which states that the voltage across an element is equal to the product of the current through it and its impedance.
- The power phasor can be obtained by multiplying the voltage and current phasors, which gives the complex power S = VI* (where * denotes the complex conjugate).
- The real power P is the projection of the complex power on the horizontal axis, and the reactive power Q is the projection of the complex power on the vertical axis.
- The apparent power |S| is the magnitude of the complex power, and the power factor cos(θ) is the ratio of the real power to the apparent power.
- The phase angle θ is the angle between the voltage and current phasors, which indicates the phase difference between them.
- The resonance frequency fr is the frequency at which the impedance of the circuit is purely resistive, which means that the inductive reactance and the capacitive reactance cancel each other out. This occurs when ωL = 1/ωC, or fr = 1/2π√LC.

## Parallel R-L-C Circuit

- A parallel R-L-C circuit is a circuit where the resistor, inductor and capacitor are connected in parallel across a current source.
- The current source can be represented by a phasor I with an angle θ.
- The current through each element can be represented by a phasor IR, IL and IC with angles θR, θL and θC respectively.
- The voltage across the circuit can be represented by a phasor V with an angle θV, which is the same for all elements.
- The total admittance of the circuit can be represented by a phasor Y with an angle θY, which is the sum of the admittances of the elements.
- The admittance of the resistor is YR = 1/R with an angle θR = 0°.
- The admittance of the inductor is YL = 1/jωL with an angle θL = -90°.
- The admittance of the capacitor is YC = jωC with an angle θC = 90°.