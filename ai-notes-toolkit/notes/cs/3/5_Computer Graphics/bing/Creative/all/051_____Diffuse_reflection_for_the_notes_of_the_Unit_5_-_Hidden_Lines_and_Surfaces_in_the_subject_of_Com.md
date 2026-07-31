# Diffuse Reflection

- Diffuse reflection is the most basic form of reflection in computer graphics.
- It occurs when light strikes a surface and is scattered in many directions, giving the impression that the surface is rough.
- This type of reflection is what gives an object its matte finish.
- Diffuse reflection can be calculated by a ray tracer to enhance the photorealism of a rendered image.
- Instead of reflecting the light (specular reflection), the ray tracer takes samples of multiple diffuse reflection angles.
- This process increases the time and processing power required to render the image, but produces better results.
- Diffuse reflection can also be affected by the color and texture of the surface, as well as the position and intensity of the light source.
- Diffuse reflection can be modeled by the Lambertian reflectance model, which assumes that the reflected light is proportional to the cosine of the angle between the surface normal and the light direction.
- Diffuse interreflection is a process whereby light reflected from an object strikes other objects in the surrounding area, illuminating them.
- Diffuse interreflection specifically describes light reflected from objects which are not shiny or specular.
- Diffuse interreflection can be simulated by using radiosity methods, which solve a system of linear equations that represent the energy exchange between surfaces.
- Diffuse interreflection can create soft shadows and color bleeding effects, which add realism to the scene.