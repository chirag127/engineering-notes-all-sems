# 5. Determination of parameters of ac single phase series RLC circuit.

- A series RLC circuit is a circuit that contains a resistor (R), an inductor (L), and a capacitor (C) connected in series with an alternating current (ac) source.
- The ac source provides a sinusoidal voltage of the form $v_s(t) = V_m \sin(\omega t + \phi)$, where $V_m$ is the peak voltage, $\omega$ is the angular frequency, and $\phi$ is the phase angle.
- The current in the circuit is the same for all components and is given by $i(t) = I_m \sin(\omega t + \theta)$, where $I_m$ is the peak current and $\theta$ is the current phase angle.
- The parameters of the circuit are the resistance $R$, the inductance $L$, the capacitance $C$, the impedance $Z$, the reactance $X$, the phase difference $\delta$, and the power factor $pf$.
- The impedance $Z$ is the total opposition to the current flow in the circuit and is given by $Z = R + jX$, where $j$ is the imaginary unit and $X$ is the reactance.
- The reactance $X$ is the sum of the inductive reactance $X_L$ and the capacitive reactance $X_C$, where $X_L = \omega L$ and $X_C = \frac{1}{\omega C}$.
- The phase difference $\delta$ is the angle between the voltage and the current in the circuit and is given by $\delta = \phi - \theta$.
- The power factor $pf$ is the ratio of the real power to the apparent power in the circuit and is given by $pf = \cos \delta$.
- The parameters of the circuit can be determined by using the following formulas:

  - $R = Z \cos \delta$
  - $L = \frac{Z \sin \delta}{\omega}$
  - $C = \frac{1}{\omega Z \sin \delta}$
  - $Z = \sqrt{R^2 + X^2}$
  - $X = X_L - X_C$
  - $\delta = \tan^{-1} \frac{X}{R}$
  - $pf = \frac{R}{Z}$

- Alternatively, the parameters of the circuit can be determined by using the phasor diagram, which is a graphical representation of the voltage and current vectors in the complex plane.
- The phasor diagram shows the following relationships:

  - $V_s = V_R + V_L + V_C$, where $V_s$, $V_R$, $V_L$, and $V_C$ are the phasors of the source voltage, the resistor voltage, the inductor voltage, and the capacitor voltage, respectively.
  - $V_R = I Z_R$, where $Z_R = R$ is the impedance of the resistor.
  - $V_L = I Z_L$, where $Z_L = j \omega L$ is the impedance of the inductor.
  - $V_C = I Z_C$, where $Z_C = -j \frac{1}{\omega C}$ is the impedance of the capacitor.
  - $I = \frac{V_s}{Z}$, where $Z = Z_R + Z_L + Z_C$ is the impedance of the circuit.
  - $\delta = \angle V_s - \angle I$, where $\angle V_s$ and $\angle I$ are the phase angles of the source voltage and the current, respectively.
  - $pf = \cos \delta$, where $\delta$ is the phase difference between the voltage and the current.