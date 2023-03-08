 Here is the content in markdown format for the topic ### Phong model for the notes of the Unit 5 - Hidden Lines and Surfaces in the subject of Computer Graphics:

### Phong Model

The Phong model is a local illumination model used in 3D computer graphics to compute the illumination at a point on a surface. It is a combination of three components -

1. Ambient light - The ambient light component models the diffuse illumination that comes from all directions. It is a constant value and does not depend on the viewer or light source positions.

2. Diffuse reflection - The diffuse component models direct illumination from a light source that gets scattered in all directions upon hitting the surface. The intensity depends on the angle between the surface normal and the light source direction.

3. Specular reflection - The specular component models the shiny highlight that appears on shiny surfaces. The intensity depends on the angle between the surface normal, light source direction and viewer direction. A shininess factor controls the size and brightness of the highlight.

Advantages -

- Produces more realistic images compared to the Gouraud shading model.
- Computationally inexpensive compared to ray tracing.

Disadvantages -

- Does not account for complex lighting effects like shadows, caustics, etc.
- Diffuse and specular components are approximated and not physically accurate.

Applications -

- Used in real-time 3D graphics for interactive applications like games to achieve reasonable image quality at lower computational cost.
- Used as a building block to develop more advanced shading models.

[Include diagrams/images/codes/tables if any to help understand the topic better]