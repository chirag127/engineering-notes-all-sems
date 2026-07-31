### Basic Illumination Models

- Illumination models, also known as shading models or lighting models, are used to calculate the intensity and color of light that is reflected at a given point on a surface.
- Illumination models are based on the physical properties of light sources, surface materials, and viewing conditions.
- Illumination models can be classified into two categories: local and global.
  - Local illumination models only consider the direct and local interaction of objects with light sources, such as ambient, diffuse, and specular reflection.
  - Global illumination models consider all the interactions and exchange of light among objects, such as reflection, refraction, shadows, and interreflections.
- In this unit, we will focus on the basic local illumination model, which gives reasonably good results and is used in most graphics systems.
- The basic local illumination model consists of three components: ambient light, diffuse reflection, and specular reflection .
  - Ambient light is the uniform and constant light that is present in the environment, regardless of the position and orientation of the objects and the light sources . Ambient light is used to simulate the effect of indirect illumination and to avoid completely dark areas .
  - Diffuse reflection is the light that is reflected equally in all directions by a matte or rough surface . Diffuse reflection depends on the angle between the surface normal and the light direction, and the color and reflectivity of the surface .
  - Specular reflection is the light that is reflected in a mirror-like manner by a shiny or smooth surface . Specular reflection depends on the angle between the surface normal, the light direction, and the viewing direction, and the color and shininess of the surface .
- The basic local illumination model can be expressed as a linear combination of the three components :

  - I = I<sub>a</sub> + I<sub>d</sub> + I<sub>s</sub>
  - where I is the total intensity, I<sub>a</sub> is the ambient intensity, I<sub>d</sub> is the diffuse intensity, and I<sub>s</sub> is the specular intensity.
- The basic local illumination model can be applied to each pixel or polygon of a graphics object to compute the intensities and colors to display the surface.
- The basic local illumination model can be extended to include other effects, such as attenuation, spotlights, multiple light sources, and transparency .