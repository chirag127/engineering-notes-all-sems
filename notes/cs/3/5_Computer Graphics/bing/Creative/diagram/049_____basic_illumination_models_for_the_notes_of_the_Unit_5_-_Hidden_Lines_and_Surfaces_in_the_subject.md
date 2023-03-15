### Basic Illumination Models

- Illumination models, also known as shading models or lighting models, are used to calculate the intensity and color of light that is reflected at a given point on a surface.
- Illumination models are based on the physical properties of light sources, surfaces, and the interaction between them.
- Illumination models can be classified into two categories: local and global.
  - Local illumination models only consider the direct and local interaction of objects with light sources, ignoring the effects of other objects in the scene.
  - Global illumination models account for all the interactions and exchange of light among objects in the scene, such as reflection, refraction, and shadows.
- A basic illumination model that gives reasonably good results and is used in most graphics systems consists of three components: ambient light, diffuse reflection, and specular reflection .
  - Ambient light is the uniform and constant light that is present in the environment, regardless of the position and orientation of the surface .
  - Diffuse reflection is the light that is reflected equally in all directions by a matte or rough surface, depending on the angle between the surface normal and the light direction .
  - Specular reflection is the light that is reflected in a dominant direction by a shiny or smooth surface, depending on the angle between the surface normal, the light direction, and the viewer direction .
- The total intensity of light at a point on a surface can be computed by adding the contributions of each component, multiplied by a coefficient that depends on the surface material and color .
- The basic illumination model can be extended to include other effects, such as attenuation, spotlights, multiple light sources, and color .