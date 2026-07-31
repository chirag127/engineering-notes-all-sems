### Diffuse reflection

- Diffuse reflection is the most basic form of reflection in computer graphics.
- It occurs when light strikes a surface and is scattered in many directions, giving the impression that the surface is rough.
- This type of reflection is what gives an object its matte finish.
- Diffuse reflection can be modeled by Lambertian reflectance, which assumes that the surface reflects light equally in all directions.
- The amount of light reflected by a diffuse surface depends only on the angle between the surface normal and the light source direction.
- The formula for diffuse reflection is:

```math
I_d = k_d I_l \cos \theta
```

where:

  - $I_d$ is the intensity of the diffuse reflection
  - $k_d$ is the diffuse reflection coefficient of the surface
  - $I_l$ is the intensity of the light source
  - $\theta$ is the angle between the surface normal and the light source direction

- Diffuse reflection can be calculated by a ray tracer to enhance the photorealism of a rendered image.
- Instead of reflecting the light directly, the ray tracer takes samples of multiple diffuse reflection angles.
- This process increases the time and processing power required to render the image, but produces better results.
- Diffuse reflection can also be affected by diffuse interreflection, which is a process whereby light reflected from an object strikes other objects in the surrounding area, illuminating them.
- Diffuse interreflection can create soft shadows and color bleeding effects.