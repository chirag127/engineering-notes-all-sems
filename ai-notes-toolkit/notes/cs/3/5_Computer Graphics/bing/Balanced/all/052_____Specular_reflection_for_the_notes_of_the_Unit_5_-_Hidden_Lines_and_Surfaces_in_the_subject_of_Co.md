# Specular reflection

- Specular reflection is the phenomenon of light bouncing off a smooth and shiny surface in a single direction, creating a bright spot or highlight on the surface .
- Specular reflection depends on the angle of incidence of the light ray, the angle of reflection of the light ray, and the viewing angle of the observer .
- The angle of incidence is equal to the angle of reflection, and both are measured with respect to the normal vector of the surface .
- The viewing angle is the angle between the normal vector and the line of sight of the observer .
- The intensity of the specular reflection is highest when the viewing angle is equal to the angle of reflection, and decreases as the viewing angle deviates from the angle of reflection .
- Specular reflection is influenced by the color and intensity of the light source, the material and roughness of the surface, and the distance between the light source, the surface, and the observer   .
- In computer graphics, specular reflection is often modeled using empirical formulas that approximate the physical behavior of light and materials .
- One of the most common models is the Phong model, proposed by Bui-Tuong Phong in 1975, which uses a power function to calculate the intensity of the specular reflection based on the angle of reflection and the viewing angle .
- The Phong model has three parameters: the ambient component, the diffuse component, and the specular component, which represent the contribution of each type of reflection to the final color of the surface.
- The ambient component is a constant value that accounts for the background illumination of the scene.
- The diffuse component is proportional to the cosine of the angle of incidence, and represents the reflection of light in all directions by a rough surface.
- The specular component is proportional to the cosine of the angle between the angle of reflection and the viewing angle, raised to a power called the shininess, and represents the reflection of light in a single direction by a smooth surface.
- The shininess parameter controls the size and sharpness of the highlight, with higher values resulting in smaller and sharper highlights.
- The Phong model can produce realistic effects for many types of materials, but it has some limitations, such as not accounting for the Fresnel effect, the polarization of light, or the interreflection of light between surfaces.
- Other models that extend or improve the Phong model include the Blinn-Phong model, the Cook-Torrance model, the Ward model, and the Bidirectional reflectance distribution function (BRDF) model.