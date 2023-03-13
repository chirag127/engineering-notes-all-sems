A plane electromagnetic wave is a type of wave that consists of oscillating electric and magnetic fields that are perpendicular to each other and to the direction of propagation. A plane electromagnetic wave can be represented by a sinusoidal function of the form:

$$E = E_0 \sin(kx - \omega t)$$

$$B = B_0 \sin(kx - \omega t)$$

where $E$ and $B$ are the electric and magnetic field strengths, $E_0$ and $B_0$ are their amplitudes, $k$ is the wave number, $x$ is the position, $\omega$ is the angular frequency, and $t$ is the time. The wave number and the angular frequency are related by the speed of light in vacuum, $c$, as:

$$k = \frac{\omega}{c}$$

In a conducting medium, such as a metal, the electric field induces a current density, $J$, that is proportional to the electric field strength, $E$, by a constant known as the electrical conductivity, $\sigma$, as:

$$J = \sigma E$$

The current density, in turn, generates a magnetic field, $B$, that is proportional to the current density, $J$, by a constant known as the magnetic permeability, $\mu$, as:

$$B = \mu J$$

The magnetic field, in turn, induces an electric field, $E$, that is proportional to the rate of change of the magnetic field, $B$, by a constant known as the electric permittivity, $\epsilon$, as:

$$E = \epsilon \frac{\partial B}{\partial t}$$

These relations imply that the plane electromagnetic wave in a conducting medium is attenuated and phase-shifted as it propagates. The attenuation is due to the dissipation of energy by the current density, and the phase-shift is due to the lag between the electric and magnetic fields. The attenuation and phase-shift can be quantified by introducing a complex wave number, $k^*$, and a complex angular frequency, $\omega^*$, as:

$$k^* = k + i \alpha$$

$$\omega^* = \omega + i \beta$$

where $i$ is the imaginary unit, $\alpha$ is the attenuation constant, and $\beta$ is the phase-shift constant. The plane electromagnetic wave in a conducting medium can then be written as:

$$E = E_0 e^{-\alpha x} \sin(kx - \omega t + \beta x)$$

$$B = B_0 e^{-\alpha x} \sin(kx - \omega t + \beta x)$$

The following diagram illustrates the plane electromagnetic wave in a conducting medium:

```
y
^
|
|   /|   /|   /|   /|   /|   /|   /|   /|   /|   /|   /|   /|   /|   /|   /|
|  / |  / |  / |  / |  / |  / |  / |  / |  / |  / |  / |  / |  / |  / |  / |
| /  | /  | /  | /  | /  | /  | /  | /  | /  | /  | /  | /  | /  | /  | /  |
|/   |/   |/   |/   |/   |/   |/   |/   |/   |/   |/   |/   |/   |/   |/   |
+---------------------------------------------------------------------------> x
|   /|   /|   /|   /|   /|   /|   /|   /|   /|   /|   /|   /|   /|   /|   /|
|  / |  / |  / |  / |  / |  / |  / |  / |  / |  / |  / |  / |  / |  / |  / |
| /  | /  | /  | /  | /  | /  | /  | /  | /  | /  | /  | /  | /  | /  | /  |
|/   |/   |/   |/   |/   |/   |/   |/   |/   |/   |/   |/   |/   |/   |/   |
+---------------------------------------------------------------------------> z
|   /|   /|   /|   /|   /|   /