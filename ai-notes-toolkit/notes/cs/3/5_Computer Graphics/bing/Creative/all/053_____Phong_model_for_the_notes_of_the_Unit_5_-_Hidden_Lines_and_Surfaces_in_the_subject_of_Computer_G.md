# Phong model

The Phong model is an empirical model of the local illumination of points on a surface designed by the computer graphics researcher Bui Tuong Phong. It is sometimes referred to as "Phong shading", particularly if the model is used with the interpolation method of the same name and in the context of pixel shaders or other places where a lighting calculation can be referred to as “shading”.

The Phong model describes the interaction of light with a surface, in terms of the properties of the surface and the nature of the incident light. It consists of three components: ambient, diffuse, and specular.

- Ambient component: This represents the constant background light that is present in the scene. It is independent of the surface orientation and the light direction. It is usually a constant color or a low-intensity color map.
- Diffuse component: This represents the light that is scattered uniformly in all directions by the surface. It depends on the surface orientation and the light direction, but not on the viewer position. It is proportional to the cosine of the angle between the surface normal and the light direction. It is usually a color map or a texture map multiplied by the light color.
- Specular component: This represents the light that is reflected in a mirror-like manner by the surface. It depends on the surface orientation, the light direction, and the viewer position. It is proportional to the cosine of the angle between the reflection direction and the viewer direction, raised to some power. It is usually a constant color or a specular map multiplied by the light color.

The Phong model can be expressed mathematically as:

I = I_a + I_d + I_s

where I is the total intensity, I_a is the ambient component, I_d is the diffuse component, and I_s is the specular component.

The ambient component can be calculated as:

I_a = k_a * I_L

where k_a is the ambient reflection coefficient, and I_L is the ambient light intensity.

The diffuse component can be calculated as:

I_d = k_d * I_L * (N . L)

where k_d is the diffuse reflection coefficient, I_L is the light intensity, N is the surface normal, and L is the light direction. The dot product (N . L) represents the cosine of the angle between N and L.

The specular component can be calculated as:

I_s = k_s * I_L * (R . V)^n

where k_s is the specular reflection coefficient, I_L is the light intensity, R is the reflection direction, V is the viewer direction, and n is the shininess exponent. The dot product (R . V) represents the cosine of the angle between R and V.

The reflection direction R can be computed as:

R = 2 * (N . L) * N - L

The viewer direction V can be computed as:

V = -E

where E is the eye position.

The Phong model can produce realistic-looking images of shiny surfaces, such as metals, plastics, and ceramics. However, it has some limitations, such as:

- It does not account for the global illumination effects, such as shadows, reflections, and refractions.
- It does not account for the wavelength-dependent behavior of light, such as dispersion and polarization.
- It does not account for the roughness or microstructure of the surface, which can affect the scattering and reflection of light.
- It does not account for the Fresnel effect, which is the variation of reflectance with the angle of incidence.
- It does not account for the subsurface scattering, which is the penetration and diffusion of light inside the surface.

To overcome some of these limitations, more advanced models have been developed, such as the Blinn-Phong model, the Cook-Torrance model, the Oren-Nayar model, and the Bidirectional Reflectance Distribution Function (BRDF) model.