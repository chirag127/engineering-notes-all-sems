### Phong model

The Phong model is an empirical model of the local illumination of points on a surface designed by the computer graphics researcher Bui Tuong Phong. It is sometimes referred to as "Phong shading", particularly if the model is used with the interpolation method of the same name and in the context of pixel shaders or other places where a lighting calculation can be referred to as “shading”.

The Phong model describes the interaction of light with a surface, in terms of the properties of the surface and the nature of the incident light. It consists of three components: ambient, diffuse, and specular reflection.

- Ambient reflection: This is the constant term that represents the amount of light that is reflected by the surface in all directions, regardless of the light source or the viewer position. It is usually a small fraction of the surface color, and it accounts for the general brightness of the scene.
- Diffuse reflection: This is the term that represents the amount of light that is reflected by the surface in a direction that is proportional to the cosine of the angle between the surface normal and the light direction. It is also known as Lambertian reflection, and it depends on the surface color and the light intensity.
- Specular reflection: This is the term that represents the amount of light that is reflected by the surface in a direction that is proportional to the cosine of the angle between the reflection direction and the viewer direction. It is also known as mirror-like reflection, and it depends on the surface shininess and the light color.

The Phong model can be expressed mathematically as follows:

![Phong model equation](https://wikimedia.org/api/rest_v1/media/math/render/svg/0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6f0f6f8f6c0a6