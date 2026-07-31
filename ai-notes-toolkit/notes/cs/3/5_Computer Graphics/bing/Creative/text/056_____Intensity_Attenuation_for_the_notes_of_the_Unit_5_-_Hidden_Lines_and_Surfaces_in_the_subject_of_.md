### Intensity Attenuation

- In computer graphics, **intensity attenuation** is the reduction or loss of intensity of any kind of flux through a medium .
- For example, sunlight is attenuated by dark glasses, x-rays are attenuated by lead, and light and sound are attenuated by water .
- Intensity attenuation is important for realistic rendering of scenes, as it affects the shading and lighting of objects.
- The intensity of a light source can be modeled as a function of the distance from the source and the angle of incidence.
- The intensity attenuation formula is given by:

$$
I = \frac{I_0}{a + bd + cd^2}
$$

where:

  - $I$ is the intensity at distance $d$ from the source
  - $I_0$ is the intensity at the source
  - $a$, $b$, and $c$ are attenuation coefficients that depend on the medium and the light source
  - $d$ is the distance from the source