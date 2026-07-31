### Basic Illumination Models

- Illumination models, also known as shading models or lighting models, are used to calculate the intensity and color of light that is reflected at a given point on a surface  .
- Illumination models are based on the properties of the light source, the surface material, and the viewing direction .
- The basic illumination model consists of three components: ambient light, diffuse reflection, and specular reflection  .
  - Ambient light is the uniform background light that is present in the environment. It is independent of the light source, the surface material, and the viewing direction. It is used to simulate the effect of indirect illumination from multiple light sources  .
  - Diffuse reflection is the light that is scattered equally in all directions by a rough or matte surface. It depends on the light source and the surface material, but not on the viewing direction. It is used to simulate the effect of diffuse or lambertian surfaces that have no specular highlights  .
  - Specular reflection is the light that is reflected in a preferred direction by a smooth or glossy surface. It depends on the light source, the surface material, and the viewing direction. It is used to simulate the effect of shiny or metallic surfaces that have specular highlights or glints  .
- The basic illumination model can be expressed as a linear combination of the three components  :

  - I = I<sub>a</sub> + I<sub>d</sub> + I<sub>s</sub>
  - where I is the total intensity, I<sub>a</sub> is the ambient intensity, I<sub>d</sub> is the diffuse intensity, and I<sub>s</sub> is the specular intensity.
- The ambient intensity can be computed as a product of the ambient light intensity and the ambient reflection coefficient of the surface  :

  - I<sub>a</sub> = k<sub>a</sub> * I<sub>a</sub>
  - where k<sub>a</sub> is the ambient reflection coefficient, and I<sub>a</sub> is the ambient light intensity.
- The diffuse intensity can be computed as a product of the diffuse light intensity, the diffuse reflection coefficient of the surface, and the cosine of the angle between the light direction and the surface normal  :

  - I<sub>d</sub> = k<sub>d</sub> * I<sub>d</sub> * cos θ
  - where k<sub>d</sub> is the diffuse reflection coefficient, I<sub>d</sub> is the diffuse light intensity, and θ is the angle between the light direction and the surface normal.
- The specular intensity can be computed as a product of the specular light intensity, the specular reflection coefficient of the surface, and the cosine of the angle between the reflection direction and the viewing direction raised to a power that controls the shininess of the surface  :

  - I<sub>s</sub> = k<sub>s</sub> * I<sub>s</sub> * cos<sup>n</sup> α
  - where k<sub>s</sub> is the specular reflection coefficient, I<sub>s</sub> is the specular light intensity, α is the angle between the reflection direction and the viewing direction, and n is the shininess exponent.
- The basic illumination model can be extended to handle multiple light sources, colored light, and colored surfaces by using vector or matrix operations  .
- The basic illumination model can be implemented using different shading methods, such as flat shading, Gouraud shading, or Phong shading, that vary in the way they evaluate and interpolate the illumination components across the surface polygons .