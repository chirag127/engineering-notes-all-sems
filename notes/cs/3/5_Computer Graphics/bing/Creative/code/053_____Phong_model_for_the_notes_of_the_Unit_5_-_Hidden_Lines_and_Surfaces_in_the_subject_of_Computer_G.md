### Phong model

The Phong model is a widely used model for the local illumination of points on a surface in computer graphics. It was designed by Bui Tuong Phong in 1973 and is based on the empirical observation that the reflection of light from a surface can be divided into three components: ambient, diffuse, and specular.

- Ambient component: This represents the constant background light that is present in the environment and affects all surfaces equally. It is independent of the surface orientation and the light direction. It is usually modeled as a constant color multiplied by a surface reflectivity factor.
- Diffuse component: This represents the light that is scattered uniformly in all directions by a rough or matte surface. It depends on the angle between the surface normal and the light direction. It is usually modeled as the product of the light color, the surface color, and the cosine of the angle between the surface normal and the light direction, also known as the Lambertian cosine law.
- Specular component: This represents the light that is reflected in a preferred direction by a shiny or glossy surface. It depends on the angle between the surface normal, the light direction, and the view direction. It is usually modeled as the product of the light color, the surface specular color, and a power function of the cosine of the angle between the reflection direction and the view direction, also known as the Phong specular term.

The Phong model can be expressed mathematically as follows:

`I = k_a I_a + k_d I_d (N ⋅ L) + k_s I_s (R ⋅ V)^n`

where

- `I` is the resulting color of the surface point
- `k_a`, `k_d`, and `k_s` are the surface reflectivity factors for ambient, diffuse, and specular components, respectively
- `I_a`, `I_d`, and `I_s` are the light colors for ambient, diffuse, and specular components, respectively
- `N` is the unit surface normal vector
- `L` is the unit light direction vector
- `R` is the unit reflection direction vector, computed as `R = 2(N ⋅ L)N - L`
- `V` is the unit view direction vector
- `n` is the shininess exponent, which controls the size and sharpness of the specular highlight

The Phong model can produce realistic results for a variety of materials and lighting conditions, but it also has some limitations. For example, it does not account for the interreflection of light between surfaces, the shadowing and occlusion effects, the wavelength-dependent reflection and refraction, and the polarization of light. These effects require more advanced models, such as global illumination, ray tracing, and physically based rendering.