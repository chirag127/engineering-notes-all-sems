### Phong model

The Phong model is an empirical model of the local illumination of points on a surface designed by the computer graphics researcher Bui Tuong Phong. It is sometimes referred to as "Phong shading", particularly if the model is used with the interpolation method of the same name.

The Phong model describes the interaction of light with a surface, in terms of the properties of the surface and the nature of the incident light. It consists of three components: ambient, diffuse, and specular.

- Ambient component: This represents the constant background light that is present in the environment. It is independent of the surface orientation and the light direction. It is usually given by a constant color value.
- Diffuse component: This represents the light that is scattered uniformly in all directions by the surface. It depends on the surface orientation and the light direction, but not on the viewer position. It is usually given by the Lambertian model, which states that the intensity of the diffuse reflection is proportional to the cosine of the angle between the surface normal and the light direction.
- Specular component: This represents the light that is reflected in a mirror-like manner by the surface. It depends on the surface orientation, the light direction, and the viewer position. It is usually given by the Phong model, which states that the intensity of the specular reflection is proportional to the cosine of the angle between the reflected light direction and the viewer direction, raised to some power called the shininess.

The Phong model can be expressed mathematically as follows:

I = I_a + I_d + I_s

where I is the total intensity of the reflected light, I_a is the ambient component, I_d is the diffuse component, and I_s is the specular component.

The ambient component can be computed as:

I_a = k_a * I_L

where k_a is the ambient reflection coefficient of the surface, and I_L is the intensity of the ambient light.

The diffuse component can be computed as:

I_d = k_d * I_L * cos(theta)

where k_d is the diffuse reflection coefficient of the surface, I_L is the intensity of the light source, and theta is the angle between the surface normal and the light direction.

The specular component can be computed as:

I_s = k_s * I_L * cos(alpha)^n

where k_s is the specular reflection coefficient of the surface, I_L is the intensity of the light source, alpha is the angle between the reflected light direction and the viewer direction, and n is the shininess of the surface.

The Phong model can be used to simulate the appearance of shiny surfaces, such as glittering surfaces, polished metal sheets, apple etc. However, it has some limitations, such as:

- It does not account for the global illumination effects, such as shadows, reflections, refractions, etc.
- It does not account for the wavelength-dependent behavior of light, such as color dispersion, polarization, etc.
- It does not account for the physical properties of the surface, such as roughness, texture, etc.
- It does not account for the distance-dependent attenuation of light, such as fog, haze, etc.

Therefore, the Phong model is a simplified and approximate model of the local illumination of points on a surface, and it may not produce realistic results for some scenes and materials.