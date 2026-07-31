### Intensity Attenuation

- In computer graphics, **attenuation** is the reduction or loss of intensity of any kind of flux through a medium .
- For example, sunlight is attenuated by dark glasses, x-rays are attenuated by lead, and light and sound are attenuated by water .
- **Intensity** is the power per unit cross-sectional area.
- **Intensity attenuation** is the gradual decrease in energy as the radiation passes through absorbing material .
- Intensity attenuation affects the appearance of objects in computer graphics, especially when using realistic lighting models.
- One way to model intensity attenuation is to use an **attenuation formula** that depends on the distance between the light source and the point on the surface.
- The attenuation formula can be written as:

```math
I = I_0 / (a + bd + cd^2)
```

- where `I` is the intensity at the point, `I_0` is the intensity at the light source, `d` is the distance between them, and `a`, `b`, and `c` are constants that control the rate of attenuation.
- The attenuation formula can be used to compute the intensity of the diffuse and specular components of the lighting model.
- Intensity attenuation can also be affected by other factors, such as the angle of incidence, the surface reflectance, and the atmospheric scattering.