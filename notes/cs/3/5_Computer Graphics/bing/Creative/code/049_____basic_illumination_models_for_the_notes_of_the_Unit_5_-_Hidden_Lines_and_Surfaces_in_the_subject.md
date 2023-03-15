### Basic Illumination Models

Illumination models are used to calculate the intensity and color of light that is reflected by a surface in a computer graphics scene. Illumination models can be classified into two categories: local and global. Local illumination models only consider the direct and local interaction of objects with light sources, while global illumination models account for all the interactions and exchange of light among objects, such as reflection, refraction, and shadows .

A basic local illumination model consists of three components: ambient light, diffuse reflection, and specular reflection .

- Ambient light: This is the background light that is present in the environment, regardless of the position and orientation of the surface. Ambient light is assumed to be constant and uniform, and it affects all surfaces equally. Ambient light is usually modeled as a constant term that is added to the final intensity of the surface .
- Diffuse reflection: This is the light that is reflected by a surface in all directions equally, depending on the angle between the surface normal and the light direction. Diffuse reflection is also known as Lambertian reflection, and it depends on the color and the diffuse reflectance coefficient of the surface. Diffuse reflection is usually modeled as a term that is proportional to the cosine of the angle between the surface normal and the light direction .
- Specular reflection: This is the light that is reflected by a surface in a mirror-like manner, depending on the angle between the surface normal, the light direction, and the viewer direction. Specular reflection is also known as Phong reflection, and it depends on the color, the specular reflectance coefficient, and the shininess of the surface. Specular reflection is usually modeled as a term that is proportional to the cosine of the angle between the reflected light direction and the viewer direction, raised to a power that controls the shininess .

The basic local illumination model can be expressed as:

I = I_a + I_d + I_s

where I is the final intensity of the surface, I_a is the ambient light intensity, I_d is the diffuse reflection intensity, and I_s is the specular reflection intensity .

The basic local illumination model can be applied to each pixel or polygon of a graphics object, depending on the shading technique used. Shading is the process of applying the illumination model to the graphics objects to compute the intensities and colors to display the surface. There are three common shading techniques: flat shading, Gouraud shading, and Phong shading.

- Flat shading: This is the simplest shading technique, where each polygon of the object is assigned a single intensity and color, based on the illumination model applied to the polygon's normal. Flat shading produces a faceted appearance of the object, and it does not account for the variation of the surface normal within the polygon.
- Gouraud shading: This is a shading technique that interpolates the intensities and colors of the vertices of the polygons, based on the illumination model applied to the vertex normals. Gouraud shading produces a smoother appearance of the object, and it accounts for the variation of the surface normal within the polygon. However, Gouraud shading does not handle specular highlights well, as they may be missed or distorted by the interpolation.
- Phong shading: This is a shading technique that interpolates the surface normals of the vertices of the polygons, and then applies the illumination model to each pixel of the polygon, based on the interpolated normal. Phong shading produces the most realistic appearance of the object, and it accounts for the variation of the surface normal and the specular highlights within the polygon. However, Phong shading is more computationally expensive than Gouraud shading, as it requires more calculations per pixel.

The basic illumination model and the shading techniques are the foundation of computer graphics, as they allow the creation of realistic and visually appealing images of 3D objects. However, the basic illumination model has some limitations, such as:

- It does not account for the global effects of light, such as shadows, reflection, refraction, and transparency .
- It does not account for the physical properties of light, such as wavelength, polarization, and interference .
- It does not account for the human perception of light, such as color, brightness, and contrast .

To overcome these limitations, more advanced illumination