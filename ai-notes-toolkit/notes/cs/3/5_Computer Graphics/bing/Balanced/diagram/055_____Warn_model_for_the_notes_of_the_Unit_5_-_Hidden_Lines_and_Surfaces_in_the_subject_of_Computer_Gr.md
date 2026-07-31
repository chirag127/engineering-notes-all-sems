### Warn model for the notes of the Unit 5 - Hidden Lines and Surfaces in the subject of Computer Graphics

- The Warn model is a lighting model that approximates large non-point sources close to objects in a scene by using several point sources arranged in a grid .
- The Warn model also allows one to specify "flaps" on the sides of the lighting region to give the light more directionality.
- The Warn model can be used to simulate studio lighting effects, such as spotlights.
- The Warn model takes into account the reflectance properties of the surface as well as the physics of light reflection.
- The Warn model can be implemented by using the following formula :

```
I = I0 * (1 / (a + b * d + c * d^2)) * cos^n(theta)
```

where:

  - I is the intensity of the light at a point on the surface
  - I0 is the intensity of the light source
  - a, b, and c are attenuation coefficients that depend on the distance d between the light source and the point on the surface
  - theta is the angle between the light direction and the surface normal
  - n is the specular exponent that controls the shininess of the surface

- The Warn model can be extended to include color considerations and transparency effects by using the RGB components of the light source and the surface, and the alpha value of the surface.