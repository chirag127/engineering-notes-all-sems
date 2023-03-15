# Plane electromagnetic waves in conducting medium

- A plane electromagnetic wave is a wave that has constant amplitude and direction of electric and magnetic fields in any plane perpendicular to the direction of propagation.
- A conducting medium is a medium that has a finite conductivity (\uD835\uDF82), which means that it allows electric currents to flow through it when an electric field is applied.
- When a plane electromagnetic wave propagates in a conducting medium, it experiences attenuation and phase shift due to the presence of electric currents and charges in the medium.
- The electric and magnetic fields of a plane electromagnetic wave in a conducting medium can be written as:

$$
\begin{aligned}
\vec{E} &= \vec{E}_0 e^{-\alpha x} e^{i(\omega t - \beta x)} \\
\vec{B} &= \vec{B}_0 e^{-\alpha x} e^{i(\omega t - \beta x)}
\end{aligned}
$$

where \(\vec{E}_0\) and \(\vec{B}_0\) are the amplitudes of the electric and magnetic fields, \(\alpha\) is the attenuation constant, \(\beta\) is the phase constant, \(\omega\) is the angular frequency, and \(x\) is the distance along the direction of propagation.

- The attenuation constant \(\alpha\) measures the rate of decrease of the wave amplitude as it travels in the medium. It depends on the conductivity, permittivity, and frequency of the medium and the wave:

$$
\alpha = \frac{\sqrt{\pi f \mu \sigma}}{2}
$$

where \(f\) is the frequency, \(\mu\) is the permeability, and \(\sigma\) is the conductivity of the medium.

- The phase constant \(\beta\) measures the rate of change of the wave phase as it travels in the medium. It also depends on the conductivity, permittivity, and frequency of the medium and the wave:

$$
\beta = \frac{\omega}{c} \sqrt{1 - \frac{\sigma^2}{4 \epsilon^2 \omega^2}}
$$

where \(c\) is the speed of light in vacuum, and \(\epsilon\) is the permittivity of the medium.

- The ratio of the electric and magnetic fields in a plane electromagnetic wave in a conducting medium is given by the intrinsic impedance of the medium \(\eta\), which is a complex quantity that describes the resistance of the medium to the wave propagation:

$$
\eta = \frac{E}{B} = \sqrt{\frac{\mu}{\epsilon}} \left( 1 - i \frac{\sigma}{2 \epsilon \omega} \right)
$$

- The real part of \(\eta\) represents the ratio of the magnitudes of the electric and magnetic fields, while the imaginary part represents the phase difference between them. The phase difference indicates that the electric and magnetic fields are not in phase in a conducting medium, unlike in a vacuum or a lossless medium.
- The skin depth \(\delta\) is a parameter that defines the distance at which the wave amplitude decreases by a factor of \(e^{-1}\) or about 37% in the medium. It is inversely proportional to the attenuation constant \(\alpha\):

$$
\delta = \frac{1}{\alpha} = \frac{2}{\sqrt{\pi f \mu \sigma}}
$$

- The skin depth indicates how far the electromagnetic wave can penetrate into the conducting medium before it is significantly attenuated. The skin depth is smaller at higher frequencies, which means that high frequency waves are more easily absorbed by the medium than low frequency waves.