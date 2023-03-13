##### 6. Determination of parameters of ac single phase series RLC circuit

- An ac single phase series RLC circuit is a circuit that consists of a resistor, an inductor, and a capacitor connected in series across an alternating voltage source.
- The voltage source produces an emf of the form: $$\epsilon = \epsilon_0 \cos(\omega t)$$ where $\epsilon_0$ is the peak emf, $\omega$ is the angular frequency, and $t$ is the time.
- The current in the circuit is the same for all the elements and is given by: $$i = i_0 \cos(\omega t - \phi)$$ where $i_0$ is the peak current, and $\phi$ is the phase angle between the current and the emf.
- The phase angle $\phi$ depends on the relative values of the resistance, the inductive reactance, and the capacitive reactance in the circuit. These are defined as: $$R = R$$ $$X_L = \omega L$$ $$X_C = \frac{1}{\omega C}$$ where $R$ is the resistance, $L$ is the inductance, $C$ is the capacitance, and $\omega$ is the angular frequency.
- The phase angle $\phi$ can be positive, negative, or zero depending on whether the circuit is inductive, capacitive, or resistive. The following table summarizes the cases:

| Case | Condition | Phase angle | Power factor |
| --- | --- | --- | --- |
| Resistive | $X_L = X_C$ | $\phi = 0$ | $1$ |
| Inductive | $X_L > X_C$ | $\phi > 0$ | $\cos \phi < 1$ |
| Capacitive | $X_L < X_C$ | $\phi < 0$ | $\cos \phi < 1$ |

- The power factor is the ratio of the average power dissipated in the circuit to the apparent power supplied by the source. It is a measure of how efficiently the circuit uses the power. A power factor of 1 means that the circuit is purely resistive and all the power is dissipated as heat. A power factor less than 1 means that the circuit is either inductive or capacitive and some power is stored and returned to the source as reactive power.
- The impedance of the circuit is the total opposition to the current flow and is given by: $$Z = \sqrt{R^2 + (X_L - X_C)^2}$$ The impedance is the ratio of the peak emf to the peak current and has the unit of ohm. It is also the hypotenuse of the impedance triangle, which is a right triangle with the resistance, the inductive reactance, and the capacitive reactance as the sides.
- The phasor diagram of the circuit is a graphical representation of the voltages and currents as vectors in the complex plane. The emf is taken as the reference vector and has a phase of zero. The current is lagging or leading the emf by the phase angle $\phi$. The voltages across the resistor, the inductor, and the capacitor are in phase, 90 degrees ahead, and 90 degrees behind the current, respectively. The phasor diagram is shown below for the three cases:

![Phasor diagram of ac single phase series RLC circuit](https://i.imgur.com/1Z0fQZc.png)

- The parameters of the ac single phase series RLC circuit can be determined by applying Kirchhoff's voltage law, which states that the sum of the voltages around a closed loop is zero. In terms of the peak values, this gives: $$\epsilon_0 = V_R + V_L - V_C$$ where $V_R$, $V_L$, and $V_C$ are the peak voltages across the resistor, the inductor, and the capacitor, respectively. Using the definitions of the resistance, the inductive reactance, and the capacitive reactance, this can be rewritten as: $$\epsilon_0 = i_0 R + i_0 \omega L - i_0 \frac{1}{\omega C}$$ Dividing by $i_0$ and rearranging, this gives: $$\frac{\epsilon_0}{i_0} = Z = R + j \omega L - j \frac{1}{\omega C}$$ where $j$ is the imaginary unit. This is the complex form of the