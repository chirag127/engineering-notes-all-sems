### Warn model for the notes of the Unit 5 - Hidden Lines and Surfaces in the subject of Computer Graphics

- The Warn model is a lighting model that approximates large non-point sources close to objects in a scene by using several point sources arranged in a grid .
- The Warn model also allows one to specify "flaps" on the sides of the lighting region to give the light more directionality.
- The Warn model can be used to simulate studio lighting effects, such as spotlights.
- The Warn model takes into account the reflectance properties of the surface as well as the physics of light reflection.
- The Warn model can be implemented by using the following steps :
  - Define the position, size, and shape of the light source grid.
  - Define the position, orientation, and color of each point source in the grid.
  - Define the flaps on the sides of the grid and their angles.
  - For each point source, calculate the intensity attenuation based on the distance and angle between the source and the surface point.
  - For each surface point, sum up the contributions of all the point sources and apply the surface reflectance model.
  - For each pixel, determine the color and intensity based on the surface point and the viewing parameters.