### Diffuse reflection

- Diffuse reflection is the most basic form of reflection in computer graphics.
- It occurs when light strikes a surface and is scattered in many directions, giving the impression that the surface is rough .
- This type of reflection is what gives an object its matte finish.
- Diffuse reflection can be calculated by a ray tracer to enhance the photorealism of a rendered image.
- Instead of reflecting the light (specular reflection), the ray tracer takes samples of multiple diffuse reflection angles.
- This process increases the time and processing power required to render the image, but produces better results.
- Diffuse reflection can also be affected by the surrounding objects, which can reflect light onto the surface.
- This phenomenon is called diffuse interreflection and it adds more realism to the scene.
- Diffuse reflection can be modeled by the Lambertian reflectance, which assumes that the light intensity is proportional to the cosine of the angle between the light direction and the surface normal .
- The Lambertian reflectance can be expressed by the formula:

```math
I = k_d I_L \cos \theta
```

where:

- `I` is the reflected light intensity
- `k_d` is the diffuse reflection coefficient
- `I_L` is the incident light intensity
- `\theta` is the angle between the light direction and the surface normal

- The diffuse reflection coefficient `k_d` can be different for different wavelengths of light, resulting in different colors for the surface.
- The diffuse reflection coefficient can also vary across the surface, creating textures or patterns.