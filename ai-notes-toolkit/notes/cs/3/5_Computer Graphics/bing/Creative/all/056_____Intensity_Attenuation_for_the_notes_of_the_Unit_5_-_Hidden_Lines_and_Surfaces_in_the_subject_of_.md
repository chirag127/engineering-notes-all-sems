# Intensity Attenuation

- In computer graphics, **intensity attenuation** is the reduction or loss of intensity of any kind of flux through a medium .
- For example, sunlight is attenuated by dark glasses, x-rays are attenuated by lead, and light and sound are attenuated by water .
- Intensity attenuation is important for realistic rendering of scenes, as it affects the shading and visibility of objects.
- Intensity attenuation can be modeled by a formula that depends on the distance from the light source, the properties of the medium, and the angle of incidence.
- The formula for intensity attenuation is:

  $$I = I_0 \frac{1}{a + bd + cd^2}$$

  where $I$ is the intensity at distance $d$ from the light source, $I_0$ is the intensity at the light source, $a$, $b$, and $c$ are constants that depend on the medium, and $d$ is the distance from the light source.
- Intensity attenuation can be applied to different types of light sources, such as point lights, spot lights, and directional lights.
- Intensity attenuation can also be combined with other effects, such as ambient, diffuse, and specular lighting, to create more realistic shading models.