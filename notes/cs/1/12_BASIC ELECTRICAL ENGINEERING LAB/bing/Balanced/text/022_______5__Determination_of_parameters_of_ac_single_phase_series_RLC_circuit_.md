##### 5. Determination of parameters of ac single phase series RLC circuit.

- A series RLC circuit is a circuit that contains a resistor (R), an inductor (L), and a capacitor (C) connected in series with an alternating current (ac) source.
- The ac source provides a sinusoidal voltage of the form $v_s(t) = V_m \sin(\omega t + \phi)$, where $V_m$ is the peak voltage, $\omega$ is the angular frequency, and $\phi$ is the phase angle.
- The current in the circuit is the same for all components and is given by $i(t) = I_m \sin(\omega t + \theta)$, where $I_m$ is the peak current and $\theta$ is the current phase angle.
- The parameters of the circuit are the resistance $R$, the inductance $L$, the capacitance $C$, the impedance $Z$, the reactance $X$, the phase difference $\delta$, and the power factor $pf$.
- The impedance $Z$ is the total opposition to the current flow in the circuit and is given by $Z = \sqrt{R^2 + (X_L - X_C)^2}$, where $X_L = \omega L$ is the inductive reactance and $X_C = \frac{1}{\omega C}$ is the capacitive reactance.
- The reactance $X$ is the net reactance of the circuit and is given by $X = X_L - X_C$.
- The phase difference $\delta$ is the angle between the voltage and the current and is given by $\delta = \theta - \phi$.
- The power factor $pf$ is the ratio of the real power to the apparent power and is given by $pf = \cos \delta = \frac{R}{Z}$.
- The parameters of the circuit can be determined by measuring the voltage and the current and applying the following formulas:

  - $R = Z \cos \delta = Z \frac{v_s(t) \cdot i(t)}{v_s^2(t)}$
  - $L = \frac{X + \sqrt{R^2 + X^2} \sin \delta}{\omega} = \frac{X + Z \sin \delta}{\omega}$
  - $C = \frac{1}{\omega (X - \sqrt{R^2 + X^2} \sin \delta)} = \frac{1}{\omega (X - Z \sin \delta)}$
  - $Z = \frac{V_m}{I_m}$
  - $X = Z \sin \delta = Z \frac{v_s(t) \times i(t)}{v_s(t) \cdot i(t)}$
  - $\delta = \arctan \frac{X}{R} = \arctan \frac{v_s(t) \times i(t)}{v_s(t) \cdot i(t)}$
  - $pf = \frac{R}{Z} = \frac{v_s(t) \cdot i(t)}{v_s^2(t)}$