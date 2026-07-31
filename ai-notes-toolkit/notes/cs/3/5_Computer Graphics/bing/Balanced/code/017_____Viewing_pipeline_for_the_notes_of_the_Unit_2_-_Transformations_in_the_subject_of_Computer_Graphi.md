### Viewing pipeline for the notes of the Unit 2 - Transformations in the subject of Computer Graphics

- The viewing pipeline is a series of transformations that convert geometry data into image data that can be displayed on a device .
- The viewing pipeline consists of the following stages :
  - Object coordinates: The coordinates of the geometry data in their own local coordinate system.
  - World coordinates: The coordinates of the geometry data after applying the modeling transformation, which places them in a common coordinate system relative to the world origin.
  - Viewing coordinates: The coordinates of the geometry data after applying the viewing transformation, which aligns them with the camera or eye position and orientation.
  - Projection coordinates: The coordinates of the geometry data after applying the projection transformation, which maps them onto a 2D plane that represents the view window or screen.
  - Device coordinates: The coordinates of the geometry data after applying the viewport transformation, which scales and translates them to fit the device resolution and aspect ratio.
- The viewing pipeline can be illustrated by the following diagram :

```
Object coordinates -> World coordinates -> Viewing coordinates -> Projection coordinates -> Device coordinates
|------------------| |------------------| |-------------------| |---------------------| |-------------------|
| Modeling         | | Viewing          | | Projection        | | Viewport            | | Rasterization     |
| transformation   | | transformation   | | transformation    | | transformation      | | and display       |
|------------------| |------------------| |-------------------| |---------------------| |-------------------|
```

- An example of the viewing pipeline is as follows:
  - Suppose we have a 2D object with coordinates (1, 1), (2, 2), (3, 1) in its own coordinate system.
  - We apply a modeling transformation that translates the object by (2, 3) and scales it by 2, resulting in the world coordinates (4, 8), (8, 10), (10, 8).
  - We apply a viewing transformation that rotates the object by 90 degrees clockwise and translates it by (-5, -5), resulting in the viewing coordinates (3, -9), (5, -13), (3, -15).
  - We apply a projection transformation that maps the viewing coordinates to a view window with coordinates (-10, -10), (10, 10), resulting in the projection coordinates (0.3, 0.1), (0.5, -0.3), (0.3, -0.5).
  - We apply a viewport transformation that scales and translates the projection coordinates to fit a device with resolution 800x600, resulting in the device coordinates (320, 340), (400, 280), (320, 220).
  - We apply a rasterization and display process that converts the device coordinates into pixels and displays them on the device screen.