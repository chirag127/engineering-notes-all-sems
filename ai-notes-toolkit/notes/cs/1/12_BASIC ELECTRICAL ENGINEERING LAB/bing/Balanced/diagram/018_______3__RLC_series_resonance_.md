##### 3. RLC series resonance.

- An RLC series circuit consists of a resistor (R), an inductor (L), and a capacitor (C) connected in series.
- The circuit has a natural frequency of oscillation, which is given by the formula:

$$f_0 = \frac{1}{2\pi\sqrt{LC}}$$

- At this frequency, the inductive reactance and the capacitive reactance are equal in magnitude and opposite in phase, so they cancel each other out. The circuit behaves like a pure resistor with an impedance of R ohms.
- The circuit is said to be in resonance at this frequency, and the current reaches a maximum value of:

$$I_{max} = \frac{V}{R}$$

- where V is the applied voltage.
- The power dissipated by the resistor is also maximum at this frequency, and is given by:

$$P_{max} = \frac{V^2}{R}$$

- The voltage across the inductor and the capacitor are also maximum at this frequency, and are given by:

$$V_L = V_C = I_{max}X_L = I_{max}X_C = \frac{V}{R}X_L = \frac{V}{R}X_C$$

- where X_L and X_C are the inductive and capacitive reactances, respectively.
- The voltage across the inductor and the capacitor are 90 degrees out of phase with the current and with each other, forming a voltage triangle.
- The phasor diagram of the circuit at resonance is shown below:

![RLC series resonance phasor diagram](https://i.imgur.com/0cJwZ8u.png)

- The quality factor (Q) of the circuit is a measure of how sharp the resonance is, and is given by:

$$Q = \frac{X_L}{R} = \frac{X_C}{R} = \frac{1}{R}\sqrt{\frac{L}{C}}$$

- The higher the Q, the narrower the bandwidth of the circuit, and the more selective it is to the resonant frequency.
- The bandwidth (B) of the circuit is the range of frequencies for which the power dissipated by the resistor is at least half of the maximum power, and is given by:

$$B = f_2 - f_1 = \frac{f_0}{Q} = \frac{R}{2\pi L}$$

- where f_1 and f_2 are the lower and upper half-power frequencies, respectively.
- The circuit can be used as a filter, an oscillator, or a tuner, depending on the application.