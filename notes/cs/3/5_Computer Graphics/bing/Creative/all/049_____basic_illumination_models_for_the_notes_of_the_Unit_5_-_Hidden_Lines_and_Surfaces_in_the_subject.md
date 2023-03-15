# Basic Illumination Models

- Illumination models, also known as shading models or lighting models, are used to calculate the intensity and color of light that is reflected at a given point on a surface.
- Illumination models are based on the physical properties of light and the interaction of light with different materials.
- Illumination models can be classified into two categories: local and global.
  - Local illumination models only consider the direct and local interaction of objects with light sources, such as ambient, diffuse, and specular reflection.
  - Global illumination models consider all the interactions and exchange of light among objects, such as reflection, refraction, shadows, and interreflections.
- In this unit, we will focus on the local illumination models, which are simpler and faster to compute than the global ones.
- The local illumination models have three main components: light sources, surface properties, and viewing parameters.
  - Light sources are the entities that emit light in the scene. They can have different types, such as point, directional, or spot. They can also have different colors and intensities.
  - Surface properties are the characteristics of the material that affect how it reflects light, such as color, reflectivity, roughness, or transparency.
  - Viewing parameters are the factors that depend on the position and orientation of the viewer and the surface, such as the angle of incidence, the angle of reflection, or the distance.
- The local illumination models can be further divided into three types: ambient, diffuse, and specular.
  - Ambient reflection is the uniform and constant light that is present in the scene regardless of the light sources or the viewing parameters. It is used to simulate the effect of indirect illumination from the environment.
  - Diffuse reflection is the light that is reflected equally in all directions from a matte or rough surface. It depends on the angle between the light source and the surface normal, and the color and intensity of the light source and the surface.
  - Specular reflection is the light that is reflected in a mirror-like manner from a shiny or smooth surface. It depends on the angle between the light source, the surface normal, and the viewer, and the color and intensity of the light source and the surface. It also depends on the shininess or glossiness of the surface, which determines how concentrated or spread the reflected light is.
- The basic illumination model combines the ambient, diffuse, and specular components to obtain the final intensity and color of the reflected light at a point on the surface. The formula is:

  - I = I<sub>a</sub> + I<sub>d</sub> + I<sub>s</sub>
  - where I is the total intensity, I<sub>a</sub> is the ambient intensity, I<sub>d</sub> is the diffuse intensity, and I<sub>s</sub> is the specular intensity.
  - The ambient intensity is calculated as:

    - I<sub>a</sub> = k<sub>a</sub> * I<sub>al</sub>
    - where k<sub>a</sub> is the ambient reflectance coefficient of the surface, and I<sub>al</sub> is the ambient light intensity.
  - The diffuse intensity is calculated as:

    - I<sub>d</sub> = k<sub>d</sub> * I<sub>l</sub> * cos θ
    - where k<sub>d</sub> is the diffuse reflectance coefficient of the surface, I<sub>l</sub> is the light source intensity, and θ is the angle between the light source and the surface normal.
  - The specular intensity is calculated as:

    - I<sub>s</sub> = k<sub>s</sub> * I<sub>l</sub> * cos<sup>n</sup> α
    - where k<sub>s</sub> is the specular reflectance coefficient of the surface, I<sub>l</sub> is the light source intensity, α is the angle between the reflected light and the viewer, and n is the shininess exponent of the surface.
- The basic illumination model can be extended to include multiple light sources, multiple surfaces, and multiple colors. The formula is:

  - I = I<sub>a</sub> + Σ