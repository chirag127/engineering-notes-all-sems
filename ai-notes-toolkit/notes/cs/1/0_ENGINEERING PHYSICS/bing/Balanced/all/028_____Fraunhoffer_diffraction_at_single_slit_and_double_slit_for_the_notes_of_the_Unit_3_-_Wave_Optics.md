# Fraunhofer Diffraction at Single Slit and Double Slit

- Fraunhofer diffraction is a type of diffraction that occurs when plane waves are incident on a diffracting object, and the diffraction pattern is observed at a sufficiently long distance from the object (in the far-field region), or at the focal plane of a converging lens.
- Fraunhofer diffraction can be analyzed using the Huygens-Fresnel principle, which states that every point on a wavefront acts as a secondary source of spherical waves, and the resultant wave at any point is the superposition of these secondary waves.
- Fraunhofer diffraction can be used to study the shape and size of the diffracting object, such as a slit, a grating, a circular aperture, etc.

## Fraunhofer Diffraction at a Single Slit

- A single slit of width `a` is illuminated by a parallel beam of monochromatic light of wavelength `λ` as shown in the figure below. The light is diffracted by the slit and forms a diffraction pattern on a screen at a distance `D` from the slit, or at the focal plane of a lens placed after the slit .

![Single slit diffraction](https://gkscientist.com/wp-content/uploads/2020/08/Fraunhofer-Diffraction-at-a-Single-Slit-1.png)

- According to the Huygens-Fresnel principle, every point on the slit acts as a secondary source of spherical waves, and the resultant wave at any point on the screen is the superposition of these waves. The intensity of the light at any point on the screen depends on the phase difference between the waves from different points on the slit .
- The phase difference between the waves from the two ends of the slit is given by `δ = k a sin θ`, where `k = 2π/λ` is the wave number, and `θ` is the angle between the central axis and the point on the screen. The phase difference between the waves from any two adjacent points on the slit is `dδ = k a sin θ da/a`, where `da` is the infinitesimal width of the slit element .
- The amplitude of the resultant wave at any point on the screen is given by the integral of the amplitudes of the secondary waves over the slit width, multiplied by a constant `C` that depends on the slit width and the distance to the screen. The amplitude is given by :

`A(θ) = C ∫_0^a e^(i k a sin θ da/a) da`

- The intensity of the light at any point on the screen is proportional to the square of the amplitude, i.e., `I(θ) ∝ |A(θ)|^2`. The intensity can be simplified by using the identity `sin x = 2 sin(x/2) cos(x/2)`, and the integral of `e^(i x)` from `0` to `π` is `2 i / x`. The intensity is given by :

`I(θ) ∝ |A(θ)|^2 = C^2 a^2 (sin(π a sin θ / λ) / (π a sin θ / λ))^2`

- The intensity distribution of the diffraction pattern is shown in the figure below. The central maximum is the brightest and the widest, and the intensity decreases and the width increases for the successive minima and maxima. The positions of the minima are given by `a sin θ = n λ`, where `n` is an integer .

![Single slit diffraction intensity](https://physicscatalyst.com/images/diffraction0_1.png)

## Fraunhofer Diffraction at a Double Slit

- A double slit consists of two slits of width `b` separated by a distance `d`, as shown in the figure below. The double slit is illuminated by a parallel beam of monochromatic light of wavelength `λ`, and the diffraction pattern is observed on a screen at a distance `D` from the slit, or at the focal plane of a lens placed after the slit .

![Double slit diffraction](https://scienceworld.wolfram