### Intensity Attenuation

- In computer graphics, **intensity attenuation** is the reduction or loss of intensity of any kind of flux through a medium .
- For example, sunlight is attenuated by dark glasses, x-rays are attenuated by lead, and light and sound are attenuated by water .
- Intensity attenuation is important for realistic rendering of scenes with light sources, shadows, and reflections.
- The intensity of a light source at a point on a surface depends on the distance from the light source, the angle of incidence, and the properties of the medium.
- The intensity attenuation formula in computer graphics is:

```
I = I0 / (a + bd + cd^2)
```

where:

- `I` is the intensity at the point on the surface
- `I0` is the intensity at the light source
- `a`, `b`, and `c` are attenuation coefficients that depend on the medium
- `d` is the distance from the light source to the point on the surface

- The attenuation coefficients `a`, `b`, and `c` can be used to model different types of attenuation, such as constant, linear, or quadratic.
- Constant attenuation (`a > 0`, `b = c = 0`) means that the intensity does not depend on the distance, but only on the angle of incidence.
- Linear attenuation (`b > 0`, `a = c = 0`) means that the intensity decreases linearly with the distance.
- Quadratic attenuation (`c > 0`, `a = b = 0`) means that the intensity decreases quadratically with the distance.
- In general, the attenuation coefficients can be chosen to fit the desired effect or the physical properties of the medium.