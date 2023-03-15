### Basic Illumination Models

- Illumination models, also known as shading models or lighting models, are used to calculate the intensity and color of light that is reflected at a given point on a surface.
- Illumination models are based on the physical properties of light sources, surfaces, and the interaction between them.
- Illumination models can be classified into two categories: local and global.
  - Local illumination models only consider the direct and local interaction of objects with light sources, such as ambient, diffuse, and specular reflection.
  - Global illumination models consider all the interactions and exchange of light among objects, such as reflection, refraction, shadows, and interreflections.
- Local illumination models are simpler and faster to compute, but they cannot capture some realistic effects that global illumination models can.
- The basic local illumination model consists of three components: ambient light, diffuse reflection, and specular reflection .
  - Ambient light is the uniform and constant light that is present in the environment, regardless of the position and orientation of the surface .
  - Diffuse reflection is the light that is reflected equally in all directions by a matte or rough surface, depending on the angle between the surface normal and the light direction .
  - Specular reflection is the light that is reflected in a mirror-like manner by a shiny or smooth surface, depending on the angle between the surface normal, the light direction, and the view direction .
- The basic local illumination model can be expressed by the following equation:

  - I = I<sub>a</sub> + I<sub>d</sub> + I<sub>s</sub>
  - where I is the total intensity of the reflected light, I<sub>a</sub> is the intensity of the ambient light, I<sub>d</sub> is the intensity of the diffuse reflection, and I<sub>s</sub> is the intensity of the specular reflection.
- The intensity of the ambient light can be computed by the following equation:

  - I<sub>a</sub> = k<sub>a</sub> * I<sub>al</sub>
  - where k<sub>a</sub> is the ambient reflection coefficient of the surface, and I<sub>al</sub> is the intensity of the ambient light source.
- The intensity of the diffuse reflection can be computed by the following equation:

  - I<sub>d</sub> = k<sub>d</sub> * I<sub>dl</sub> * cos θ
  - where k<sub>d</sub> is the diffuse reflection coefficient of the surface, I<sub>dl</sub> is the intensity of the diffuse light source, and θ is the angle between the surface normal and the light direction.
- The intensity of the specular reflection can be computed by the following equation:

  - I<sub>s</sub> = k<sub>s</sub> * I<sub>sl</sub> * cos<sup>n</sup> α
  - where k<sub>s</sub> is the specular reflection coefficient of the surface, I<sub>sl</sub> is the intensity of the specular light source, n is the shininess factor of the surface, and α is the angle between the reflection direction and the view direction.
- The following diagram illustrates the basic local illumination model:

  ```
  +-----------------+     +-----------------+
  |                 |     |                 |
  |                 |     |                 |
  |                 |     |                 |
  |                 |     |                 |
  |                 |     |                 |
  |                 |     |                 |
  |                 |     |                 |
  |                 |     |                 |
  |                 |     |                 |
  |                 |     |                 |
  |                 |     |                 |
  +-----------------+     +-----------------+
  |                 |     |                 |
  |                 |     |                 |
  |                 |     |                 |
  |                 |     |                 |
  |                 |     |                 |
  |                 |     |                 |
  |                 |     |                 |
  |                 |     |                 |
  |                 |     |                 |
  +-----------------+     +-----------------+
  |                 |     |                 |
  |                 |