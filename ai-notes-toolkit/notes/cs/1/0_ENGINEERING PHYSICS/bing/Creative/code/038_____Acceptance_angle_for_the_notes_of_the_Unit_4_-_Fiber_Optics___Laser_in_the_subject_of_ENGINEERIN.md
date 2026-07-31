# Acceptance Angle in Fiber Optics

- The acceptance angle of an optical fiber is defined based on a purely geometrical consideration (ray optics): it is the maximum angle of a ray (against the fiber axis) hitting the fiber core which allows the incident light to be guided by the core .
- The acceptance angle depends on the refractive indices of the core, the cladding, and the surrounding medium (usually air). The larger the difference between the core and the cladding refractive indices, the larger the acceptance angle.
- The acceptance angle can be calculated using Snell's law and the condition for total internal reflection at the core-cladding interface. If n_f is the core refractive index, n_c is the cladding refractive index, and n_0 is the surrounding medium refractive index, then the acceptance angle \theta_a is given by:

\theta_a = \sin^{-1} \left( \frac{n_f}{n_0} \sqrt{1 - \left( \frac{n_c}{n_f} \right)^2} \right)

- The acceptance angle can also be expressed in terms of the numerical aperture (NA) of the fiber, which is defined as:

NA = n_0 \sin \theta_a = \sqrt{n_f^2 - n_c^2}

- The numerical aperture is a dimensionless parameter that characterizes the light-gathering ability of the fiber. It is commonly used in datasheets for fiber optic cable.
- The acceptance angle defines a cone of light that can enter the fiber and propagate along the core. The cone has an apex at the fiber end and an opening angle of 2\theta_a. The acceptance cone can be visualized by tracing the rays that hit the core at the critical angle for total internal reflection.