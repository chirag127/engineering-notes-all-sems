
### Phong Model

The Phong Model is a lighting model used in computer graphics to simulate the interaction of light with surfaces. It is used to calculate the intensity of light reflected from a surface at a given point, and is based on the concept of local illumination. It is named after Bui Tuong Phong, who developed the model in 1973.

The Phong Model consists of three components: 
* Ambient Light: This is the light that is present in the environment, and is independent of the light source. It is usually modelled as a constant color.
* Diffuse Reflection: This is the light that is reflected off of the surface in all directions. It is modelled as a Lambertian reflectance.
* Specular Reflection: This is the light that is reflected off of the surface in a specific direction. It is modelled as a Phong reflectance.

In the context of hidden lines and surfaces, the Phong Model is used to calculate the intensity of light that is reflected off of a surface, and thus determine which parts of the surface are visible. This is used to render objects that have hidden lines and surfaces, such as a cube or a sphere.