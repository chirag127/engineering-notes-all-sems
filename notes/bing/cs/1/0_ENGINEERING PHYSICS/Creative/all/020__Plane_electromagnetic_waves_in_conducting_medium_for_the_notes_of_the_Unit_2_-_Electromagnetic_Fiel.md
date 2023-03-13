### Plane electromagnetic waves in conducting medium for the notes of the Unit 2 - Electromagnetic Field Theory in the subject of ENGINEERING PHYSICS

- A plane electromagnetic wave is a wave that has constant amplitude and direction of electric and magnetic fields in any plane perpendicular to the direction of propagation.
- A conducting medium is a medium that has finite conductivity (\uD835\uDF82), permeability (\uD835\uDF41) and permittivity (\uD835\uDF3A).
- When a plane electromagnetic wave propagates in a conducting medium, it experiences attenuation (loss of energy) and phase shift (change in phase angle) due to the presence of free charges and currents in the medium .
- The wave equation for a plane electromagnetic wave in a conducting medium is given by:

```
\nabla^2 \vec{E} = \mu \epsilon \frac{\partial^2 \vec{E}}{\partial t^2} + \mu \sigma \frac{\partial \vec{E}}{\partial t}
```

where \uD835\uDED1 is the electric field, \uD835\uDF41 is the permeability, \uD835\uDF3A is the permittivity, \uD835\uDF82 is the conductivity and t is the time.
- The general solution for the wave equation is:

```
\vec{E} = \vec{E}_0 e^{i(\vec{k} \cdot \vec{r} - \omega t)}
```

where \uD835\uDED0\uD835\uDC5F is the amplitude, \uD835\uDC4F is the wave vector, \uD835\uDC5B is the position vector, \uD835\uDC60 is the angular frequency and i is the imaginary unit.
- The wave vector \uD835\uDC4F has a complex magnitude and direction given by:

```
k = \beta + i \alpha = \omega \sqrt{\mu \epsilon} \sqrt{1 + i \frac{\sigma}{\omega \epsilon}}
```

where \uD835\uDC3B is the phase constant, \uD835\uDC46 is the attenuation constant and i is the imaginary unit.
- The phase constant \uD835\uDC3B determines the phase shift of the wave as it propagates, and the attenuation constant \uD835\uDC46 determines the rate of decay of the wave amplitude as it propagates.
- The ratio of the electric field amplitude to the magnetic field amplitude is called the intrinsic impedance of the medium, denoted by \uD835\uDF7A, and is given by:

```
\eta = \frac{E}{H} = \sqrt{\frac{\mu}{\epsilon}} \frac{1 - i \frac{\sigma}{\omega \epsilon}}{\sqrt{1 + i \frac{\sigma}{\omega \epsilon}}}
```

where \uD835\uDED1 is the electric field, \uD835\uDED7 is the magnetic field, \uD835\uDF41 is the permeability, \uD835\uDF3A is the permittivity, \uD835\uDF82 is the conductivity and \uD835\uDC60 is the angular frequency.
- The intrinsic impedance of the medium is a complex quantity that depends on the frequency of the wave and the properties of the medium. It determines the reflection and transmission of the wave at the interface of two different media.
- The skin depth of the medium, denoted by \uD835\uDC51, is the distance over which the wave amplitude decreases by a factor of 1/e (about 0.37), and is given by:

```
\delta = \frac{1}{\alpha} = \sqrt{\frac{2}{\omega \mu \sigma}}
```

where \uD835\uDC46 is the attenuation constant, \uD835\uDC60 is the angular frequency, \uD835\uDF41 is the permeability and \uD835\uDF82 is the conductivity.
- The skin depth of the medium is inversely proportional to the square root of the frequency and the conductivity of the medium. It indicates how far the wave can penetrate into the medium before it is absorbed by the free charges and currents.

Some mnemonics and learning tricks for the topic are:

- To remember the wave equation for a plane electromagnetic wave in a conducting medium, use the acronym **MEEP**:

```
MEEP = \nabla^2 \vec{E} = \mu \epsilon \frac{\partial