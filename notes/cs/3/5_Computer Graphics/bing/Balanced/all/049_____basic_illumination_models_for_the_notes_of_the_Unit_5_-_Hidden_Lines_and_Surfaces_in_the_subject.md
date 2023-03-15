# Basic Illumination Models

- Illumination models, also known as shading models or lighting models, are used to calculate the intensity and color of light that is reflected at a given point on a surface.
- Illumination models are based on the properties of the surface and the properties of the light sources.
- Illumination models can be classified into two categories: local and global.
  - Local illumination models only consider the direct and local interaction of objects with light sources, ignoring the effects of other objects in the scene.
  - Global illumination models consider all the interactions and exchange of light among objects in the scene, including reflection, refraction, and shadows.
- The most common local illumination model is the Phong model, which consists of three components: ambient, diffuse, and specular .
  - Ambient component represents the uniform background light that is present in the environment, independent of the light sources and the surface orientation .
  - Diffuse component represents the light that is scattered equally in all directions by a matte or rough surface, depending on the angle between the surface normal and the light direction .
  - Specular component represents the light that is reflected in a mirror-like manner by a shiny or smooth surface, depending on the angle between the surface normal, the light direction, and the view direction .
- The Phong model can be expressed mathematically as follows :

  - I = I<sub>a</sub> + I<sub>d</sub> + I<sub>s</sub>
  - I<sub>a</sub> = k<sub>a</sub> * I<sub>al</sub>
  - I<sub>d</sub> = k<sub>d</sub> * I<sub>l</sub> * cos θ
  - I<sub>s</sub> = k<sub>s</sub> * I<sub>l</sub> * cos<sup>n</sup> α
  - where I is the total intensity, I<sub>a</sub> is the ambient intensity, I<sub>d</sub> is the diffuse intensity, I<sub>s</sub> is the specular intensity, k<sub>a</sub> is the ambient reflection coefficient, k<sub>d</sub> is the diffuse reflection coefficient, k<sub>s</sub> is the specular reflection coefficient, I<sub>al</sub> is the ambient light intensity, I<sub>l</sub> is the light source intensity, θ is the angle between the surface normal and the light direction, α is the angle between the reflection direction and the view direction, and n is the shininess exponent.

- The following diagram illustrates the Phong model:

  ![Phong model diagram](https://image.slideserve.com/1379770/phong-model-n.jpg)

- The Phong model can be extended to include multiple light sources, color, and attenuation factors .
- The Phong model is a simple and efficient local illumination model, but it has some limitations, such as ignoring the effects of shadows, interreflections, and transparency .
- Global illumination models are more realistic and complex, but they are also more computationally expensive and difficult to implement.
- Some examples of global illumination models are ray tracing, radiosity, and photon mapping.