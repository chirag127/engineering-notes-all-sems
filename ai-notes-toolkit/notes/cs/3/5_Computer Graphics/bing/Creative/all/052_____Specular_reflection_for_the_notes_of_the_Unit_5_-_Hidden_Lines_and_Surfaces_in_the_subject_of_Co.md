# Specular Reflection

- Specular reflection is the phenomenon of light reflecting from a smooth or shiny surface in a mirror-like manner.
- Specular reflection occurs when the angle of incidence is equal to the angle of reflection, and the reflected rays are parallel to each other.
- Specular reflection produces a bright spot of light on the surface, called a specular highlight, that has the color of the light source rather than of the object.
- Specular reflection depends on the surface normal, the direction of the light source, and the direction of the viewer.
- Specular reflection can be modeled by an empirical formula suggested by Bui-Tuong Phong in 1975, which is often used in computer graphics.
- The Phong model defines the specular reflection as:

  - I<sub>s</sub> = k<sub>s</sub> I<sub>l</sub> (R ⋅ V)<sup>n</sup>
  - where I<sub>s</sub> is the intensity of the specular reflection, k<sub>s</sub> is the specular reflection coefficient, I<sub>l</sub> is the intensity of the light source, R is the direction of the reflected ray, V is the direction of the viewer, and n is the shininess exponent.
  - The shininess exponent controls the size and sharpness of the specular highlight. A higher value of n produces a smaller and sharper highlight, while a lower value of n produces a larger and softer highlight.
  - The Phong model assumes that the surface is perfectly smooth and the light source is a point source. It does not account for the effects of roughness, texture, or multiple light sources.