### Plane electromagnetic waves in conducting medium

- A plane electromagnetic wave is a wave that has a constant amplitude and direction of electric and magnetic fields in any plane perpendicular to the direction of propagation.
- A plane electromagnetic wave can be represented by the following equations:

  \begin{align*}
  \vec{E} &= \vec{E}_0 e^{i(\vec{k}\cdot\vec{r}-\omega t)} \\
  \vec{B} &= \vec{B}_0 e^{i(\vec{k}\cdot\vec{r}-\omega t)}
  \end{align*}

  where \(\vec{E}_0\) and \(\vec{B}_0\) are the amplitudes of the electric and magnetic fields, \(\vec{k}\) is the wave vector, \(\vec{r}\) is the position vector, \(\omega\) is the angular frequency, and \(i\) is the imaginary unit.
- A plane electromagnetic wave satisfies the following relations:

  \begin{align*}
  \vec{k} &= \frac{\omega}{c}\hat{n} \\
  \vec{E}_0 &\perp \vec{B}_0 \perp \hat{n} \\
  \frac{E_0}{B_0} &= c
  \end{align*}

  where \(c\) is the speed of light in vacuum, and \(\hat{n}\) is the unit vector along the direction of propagation.
- A conducting medium is a medium that has a finite conductivity \(\sigma\), which means that it allows electric currents to flow through it. A conducting medium also has a permittivity \(\epsilon\) and a permeability \(\mu\), which determine how the electric and magnetic fields interact with the medium.
- A plane electromagnetic wave in a conducting medium can be derived from Maxwell's equations, which are:

  \begin{align*}
  \nabla \cdot \vec{E} &= \frac{\rho}{\epsilon} \\
  \nabla \cdot \vec{B} &= 0 \\
  \nabla \times \vec{E} &= -\frac{\partial \vec{B}}{\partial t} \\
  \nabla \times \vec{B} &= \mu\vec{J} + \mu\epsilon\frac{\partial \vec{E}}{\partial t}
  \end{align*}

  where \(\rho\) is the charge density, and \(\vec{J}\) is the current density.
- Assuming that the medium is charge-free (\(\rho = 0\)) and external-current-free (\(\vec{J} = 0\)), the plane electromagnetic wave in a conducting medium can be expressed as:

  \begin{align*}
  \vec{E} &= \vec{E}_0 e^{-\alpha z} e^{i(\beta z - \omega t)} \\
  \vec{B} &= \vec{B}_0 e^{-\alpha z} e^{i(\beta z - \omega t)}
  \end{align*}

  where \(\alpha\) and \(\beta\) are the attenuation constant and the phase constant, respectively, given by:

  \begin{align*}
  \alpha &= \frac{\omega}{2c}\sqrt{\mu\epsilon}\sqrt{1+\left(\frac{\sigma}{\omega\epsilon}\right)^2} \\
  \beta &= \frac{\omega}{c}\sqrt{\mu\epsilon}\sqrt{1-\left(\frac{\sigma}{\omega\epsilon}\right)^2}
  \end{align*}

  The wave vector \(\vec{k}\) can be written as \(\vec{k} = (\alpha + i\beta)\hat{z}\), where \(\hat{z}\) is the direction of propagation.
- The plane electromagnetic wave in a conducting medium has the following properties:

  - The electric and magnetic fields are perpendicular to each other and to the direction of propagation, as in a vacuum.
  - The electric and magnetic fields have the same phase and decay exponentially as they travel through the medium, due to the presence of conductivity.
  - The ratio of the electric and magnetic field amplitudes is not equal to the speed of light, but to a complex quantity called the wave impedance, given by:

    \begin{align*}
    Z &= \frac{E_0}{B