### Basic Illumination Models

In computer graphics, illumination models are used to calculate the appearance of objects in a virtual scene. These models take into account the properties of the light sources, the properties of the objects, and the properties of the environment to determine how light is reflected, absorbed, and transmitted by the objects in the scene. Here are some basic illumination models:

1. **Ambient lighting:** This model assumes that light is scattered uniformly throughout the environment, so that all objects are illuminated evenly, regardless of their position or orientation. This model is simple to implement, but it does not produce realistic results, as it does not take into account the direction of the light sources or the shadows cast by objects.

2. **Diffuse lighting:** This model assumes that light is reflected equally in all directions by the surface of an object. The amount of light reflected depends on the angle between the surface normal and the direction of the light source. This model produces more realistic results than the ambient lighting model, as it takes into account the direction of the light sources, but it still does not produce shadows.

3. **Specular lighting:** This model assumes that light is reflected in a specific direction by the surface of an object, depending on the angle of incidence of the light and the properties of the surface. This model produces highlights on shiny surfaces, and can be combined with the diffuse lighting model to produce more realistic results.

4. **Phong lighting:** This model is an extension of the specular lighting model, which takes into account the roughness of the surface to produce more realistic highlights. It is widely used in computer graphics, as it produces realistic results with relatively low computational cost.

These are some of the basic illumination models used in computer graphics. They can be combined and extended to produce more complex and realistic lighting effects.