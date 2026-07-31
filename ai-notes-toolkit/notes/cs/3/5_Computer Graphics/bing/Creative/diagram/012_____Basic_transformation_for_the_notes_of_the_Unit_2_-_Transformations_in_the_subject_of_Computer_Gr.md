Hello, I am Sydney, your AI assistant. I can help you with your topic. Here is some information that I found from the web:

### Basic transformation for the notes of the Unit 2 - Transformations in the subject of Computer Graphics

- Transformations are operations that change the position, size, orientation, or shape of an object on a 2D or 3D plane  .
- There are three basic rigid transformations that preserve the shape and size of an object: reflections, rotations, and translations.
- There is a fourth common transformation called dilation or scaling that changes the size of an object .
- Transformations can be represented by matrices that multiply with the coordinates of the object to produce the transformed coordinates  .
- The basic transformation matrices for 2D are:

  - Translation: 
  ```
  | 1  0  tx |
  | 0  1  ty |
  | 0  0  1  |
  ```
  where tx and ty are the translation distances along the x and y axes respectively.
  - Rotation: 
  ```
  | cosθ  -sinθ  0 |
  | sinθ   cosθ  0 |
  | 0      0     1 |
  ```
  where θ is the angle of rotation in the counterclockwise direction.
  - Scaling: 
  ```
  | sx  0   0 |
  | 0   sy  0 |
  | 0   0   1 |
  ```
  where sx and sy are the scaling factors along the x and y axes respectively .
  - Reflection: 
  ```
  | -1  0  0 |
  | 0   1  0 |
  | 0   0  1 |
  ```
  for reflection about the y-axis, and 
  ```
  | 1  0   0 |
  | 0  -1  0 |
  | 0  0   1 |
  ```
  for reflection about the x-axis.
- Transformations can be combined by multiplying the matrices in the order of the desired operations .
- Transformations can be applied to points, lines, polygons, or any other graphical objects  .
- Transformations are widely used in computer graphics applications such as animation, modeling, rendering, and image processing  .