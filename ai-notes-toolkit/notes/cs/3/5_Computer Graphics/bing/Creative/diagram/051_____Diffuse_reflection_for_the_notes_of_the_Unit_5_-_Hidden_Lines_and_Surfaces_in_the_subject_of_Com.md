### Diffuse reflection

- Diffuse reflection is the most basic form of reflection in computer graphics.
- It occurs when light strikes a surface and is scattered in many directions, giving the impression that the surface is rough .
- This type of reflection is what gives an object its matte finish.
- Diffuse reflection can be calculated by a ray tracer to enhance the photorealism of a rendered image.
- Instead of reflecting the light (specular reflection), the ray tracer takes samples of multiple diffuse reflection angles.
- This process increases the time and processing power required to render the image, but produces better results.
- Diffuse reflection can be modeled by Lambert's cosine law, which states that the intensity of the reflected light is proportional to the cosine of the angle between the light source and the surface normal .
- Diffuse reflection can also be affected by diffuse interreflection, which is a process whereby light reflected from an object strikes other objects in the surrounding area, illuminating them.
- Diffuse interreflection specifically describes light reflected from objects which are not shiny or specular.
- Diffuse interreflection can be simulated by global illumination algorithms, such as radiosity or Monte Carlo methods.