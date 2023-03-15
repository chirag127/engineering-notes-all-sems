### Specular reflection

- Specular reflection is the phenomenon of light reflecting off a smooth surface in a mirror-like way, creating a bright spot or highlight on the surface .
- Specular reflection depends on the angle of incidence of the light ray, the angle of reflection of the light ray, and the viewing angle of the observer.
- Specular reflection is modeled by the Phong reflection model, which consists of three components: ambient, diffuse, and specular.
- The ambient component represents the constant background illumination of the scene, independent of the light source or the surface orientation.
- The diffuse component represents the Lambertian reflection of the light source, which is proportional to the cosine of the angle between the light ray and the surface normal.
- The specular component represents the mirror-like reflection of the light source, which is proportional to the cosine of the angle between the reflected light ray and the viewing direction, raised to some power called the shininess.
- The shininess determines how sharp or blurry the specular highlight is, with higher values resulting in sharper highlights and lower values resulting in blurrier highlights.
- The Phong reflection model can be expressed as:

![Phong reflection model formula](https://wikimedia.org/api/rest_v1/media/math/render/svg/8c2c2d0f0b9f0f9c9b2f2e0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9f0c9