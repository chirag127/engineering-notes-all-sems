### Viewing pipeline for the notes of the Unit 2 - Transformations in the subject of Computer Graphics

- The viewing pipeline is a series of transformations that convert geometric data into image data that can be displayed on a device .
- The viewing pipeline consists of the following stages :
  - Object coordinates: The coordinates of the geometric primitives that define the objects in the scene.
  - World coordinates: The coordinates of the objects after applying the modeling transformation, which positions and orientates them in the 3D space.
  - Viewing coordinates: The coordinates of the objects after applying the viewing transformation, which defines the position and orientation of the camera or the eye.
  - Projection coordinates: The coordinates of the objects after applying the projection transformation, which maps the 3D scene onto a 2D plane.
  - Normalized device coordinates: The coordinates of the objects after applying the normalization transformation, which scales and translates the projected scene to fit within a unit cube.
  - Device coordinates: The coordinates of the objects after applying the viewport transformation, which maps the normalized device coordinates to the physical device coordinates.
- The viewing pipeline can be represented by the following diagram :

```
Object coordinates -> World coordinates -> Viewing coordinates -> Projection coordinates -> Normalized device coordinates -> Device coordinates
```

- An example of the viewing pipeline is as follows :
  - Suppose we have a triangle with vertices (1, 1), (2, 3), and (3, 2) in object coordinates.
  - We apply a modeling transformation that translates the triangle by (2, 1) and scales it by 2, resulting in the following world coordinates: (4, 4), (6, 8), and (8, 6).
  - We apply a viewing transformation that rotates the scene by 90 degrees clockwise around the origin, resulting in the following viewing coordinates: (4, -4), (8, -6), and (6, -8).
  - We apply a projection transformation that uses an orthographic projection with a clipping window of (-10, 10) x (-10, 10), resulting in the following projection coordinates: (4, -4), (8, -6), and (6, -8).
  - We apply a normalization transformation that maps the clipping window to the unit square of (-1, 1) x (-1, 1), resulting in the following normalized device coordinates: (0.4, -0.4), (0.8, -0.6), and (0.6, -0.8).
  - We apply a viewport transformation that maps the unit square to the device coordinates of (0, 0) x (100, 100), resulting in the following device coordinates: (40, 60), (80, 70), and (60, 80).
  - The final image is a triangle with vertices (40, 60), (80, 70), and (60, 80) on the device.