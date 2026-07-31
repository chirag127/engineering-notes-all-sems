# Plane electromagnetic waves in conducting medium

- A plane electromagnetic wave is a wave that has constant amplitude and direction of electric and magnetic fields in any plane perpendicular to the direction of propagation.
- A conducting medium is a medium that has a finite conductivity (\uD835\uDF82) and can support electric currents.
- When a plane electromagnetic wave propagates in a conducting medium, it experiences attenuation and phase shift due to the presence of free charges.
- The wave equation for a plane electromagnetic wave in a conducting medium is given by:

$$\nabla^2 \mathbf{E} = \mu \epsilon \frac{\partial^2 \mathbf{E}}{\partial t^2} + \mu \sigma \frac{\partial \mathbf{E}}{\partial t}$$

- The general solution for the electric field of a plane electromagnetic wave in a conducting medium is given by:

$$\mathbf{E}(\mathbf{r},t) = \mathbf{E}_0 e^{-\alpha z} e^{i(\omega t - \beta z)}$$

- where \uD835\uDF0F is the angular frequency, \uD835\uDF0C is the phase constant, \uD835\uDF0B is the attenuation constant, and \uD835\uDF0E is the complex propagation constant given by:

$$\gamma = \alpha + i \beta = \sqrt{i \omega \mu (\sigma + i \omega \epsilon)}$$

- The magnetic field of a plane electromagnetic wave in a conducting medium is given by:

$$\mathbf{B}(\mathbf{r},t) = \frac{1}{\omega} \mathbf{k} \times \mathbf{E}(\mathbf{r},t)$$

- where \uD835\uDF0F is the unit vector in the direction of propagation.
- The power density of a plane electromagnetic wave in a conducting medium is given by:

$$\mathbf{S} = \frac{1}{2} \mathbf{E} \times \mathbf{H}^* = \frac{1}{2} \mathbf{E}_0 \times \mathbf{H}_0^* e^{-2 \alpha z}$$

- where \uD835\uDF0A is the complex conjugate of \uD835\uDF0A.
- The skin depth of a plane electromagnetic wave in a conducting medium is the distance at which the power density drops to 1/e of its initial value. It is given by:

$$\delta = \frac{1}{\alpha} = \sqrt{\frac{2}{\omega \mu \sigma}}$$

- The skin depth is smaller at higher frequencies, which implies that high frequency waves penetrate a shorter distance into a conductor than low frequency waves.
- The intrinsic impedance of a plane electromagnetic wave in a conducting medium is the ratio of the electric and magnetic fields. It is given by:

$$\eta = \frac{E}{H} = \frac{\gamma}{\omega \mu} = \sqrt{\frac{i \omega \mu}{\sigma + i \omega \epsilon}}$$

- The intrinsic impedance is a complex quantity that depends on the frequency, conductivity, permeability, and permittivity of the medium.