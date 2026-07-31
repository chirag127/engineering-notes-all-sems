# Analysis of single phase AC Circuits consisting R-L-C combination (Series and Parallel)

- A single phase AC circuit is a circuit that is powered by a single alternating voltage or current source.
- A R-L-C circuit is a circuit that contains a resistor, an inductor and a capacitor connected in series or parallel.
- The analysis of R-L-C circuits involves finding the voltage, current, power and impedance of each component and the circuit as a whole.
- The analysis of R-L-C circuits can be done using phasor diagrams, complex algebra, Kirchhoff's laws, mesh analysis, nodal analysis, Thevenin's theorem, Norton's theorem, etc.

## Series R-L-C Circuit

- A series R-L-C circuit is a circuit where the resistor, the inductor and the capacitor are connected in series across a single AC voltage source.
- The voltage across each component is different and depends on the frequency of the source and the values of R, L and C.
- The current through each component is the same and is equal to the source current.
- The total impedance of the circuit is given by:

$$Z = R + j(X_L - X_C) = R + j\omega L - \frac{j}{\omega C}$$

where $j$ is the imaginary unit, $\omega$ is the angular frequency of the source, $X_L$ is the inductive reactance, and $X_C$ is the capacitive reactance.

- The total impedance can also be written in polar form as:

$$Z = |Z| \angle \phi = \sqrt{R^2 + (X_L - X_C)^2} \angle \tan^{-1} \left(\frac{X_L - X_C}{R}\right)$$

where $|Z|$ is the magnitude of the impedance and $\phi$ is the phase angle.

- The phase angle indicates the phase difference between the source voltage and the source current. It can be positive, negative or zero depending on the relative values of R, L and C.
- If $X_L > X_C$, the circuit is inductive and the current lags the voltage by $\phi$.
- If $X_L < X_C$, the circuit is capacitive and the current leads the voltage by $\phi$.
- If $X_L = X_C$, the circuit is resonant and the current is in phase with the voltage. The impedance is purely resistive and has the minimum value of $R$.

- The voltage across each component can be found by multiplying the current by the impedance of the component. For example, the voltage across the resistor is given by:

$$V_R = IZ_R = IR \angle 0$$

- The power dissipated by each component can be found by multiplying the voltage by the current and taking the real part. For example, the power dissipated by the resistor is given by:

$$P_R = \Re(V_R I^*) = \Re(IR \angle 0 \cdot I \angle -\phi) = IR^2 \cos \phi$$

where $I^*$ is the complex conjugate of the current.

- The power factor of the circuit is the ratio of the real power to the apparent power. It is given by:

$$pf = \frac{P}{S} = \frac{IR^2 \cos \phi}{|V||I|} = \frac{R}{|Z|} \cos \phi$$

where $P$ is the real power, $S$ is the apparent power, and $|V|$ is the magnitude of the source voltage.

- The power factor indicates how efficiently the circuit uses the power supplied by the source. It can range from 0 to 1. A power factor of 1 means that the circuit is purely resistive and all the power is dissipated as heat. A power factor of 0 means that the circuit is purely reactive and no power is dissipated.

## Parallel R-L-C Circuit

- A parallel R-L-C circuit is a circuit where the resistor, the inductor and the capacitor are connected in parallel across a single AC voltage source.
- The voltage across each component is the same and is equal to the source voltage.
- The current through each component is different and depends on the frequency of the source and the values of R, L and C.
- The total admittance of the circuit is given by:

$$Y = G + j(B_L + B_C) = \frac{1}{R} + j\left(\omega C - \frac{1}{