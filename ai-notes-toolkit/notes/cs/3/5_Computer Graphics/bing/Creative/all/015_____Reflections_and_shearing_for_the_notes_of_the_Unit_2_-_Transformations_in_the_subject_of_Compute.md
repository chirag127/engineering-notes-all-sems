# Reflections and Shearing

## Reflection

- Reflection is a type of transformation in computer graphics that produces a mirror image of an object.
- Reflection can be performed in any direction, such as horizontal, vertical, diagonal, or along an arbitrary axis.
- Reflection is equivalent to a rotation of 180 degrees about the line of reflection, which acts as a mirror.
- To perform reflection, we need to find the coordinates of the reflected point with respect to the line of reflection.
- The general formula for reflection is:

  - If the line of reflection is y = mx + c, then the reflected point (x', y') of a point (x, y) is given by:

    - x' = (x + 2my - 2c) / (1 + m^2)
    - y' = (y + 2mx + 2c) / (1 + m^2)

  - If the line of reflection is x = k, then the reflected point (x', y') of a point (x, y) is given by:

    - x' = 2k - x
    - y' = y

  - If the line of reflection is y = k, then the reflected point (x', y') of a point (x, y) is given by:

    - x' = x
    - y' = 2k - y

- An example of reflection is shown below:

  - The original object is a triangle with vertices A(1, 1), B(3, 4), and C(5, 2).
  - The line of reflection is y = x.
  - The reflected object is a triangle with vertices A'(1, 1), B'(4, 3), and C'(2, 5).

```
  y
  ^
  |   B'  C'
  |  / \ /
  | /   X
  |/   / \
  +---------> x
 /|   /   \
/ |  /     \
   A'      A B
           \ |
            \|
             C
```

## Shearing

- Shearing is a type of transformation in computer graphics that changes the shape of an object by sliding its layers in one or more directions.
- Shearing can be performed in any direction, such as horizontal, vertical, or along an arbitrary axis.
- Shearing does not change the area or volume of the object, but it may change its orientation and aspect ratio.
- To perform shearing, we need to find the coordinates of the sheared point with respect to the shearing factor and the direction of shearing.
- The general formula for shearing is:

  - If the shearing is in the x-direction, then the sheared point (x', y') of a point (x, y) is given by:

    - x' = x + shx * y
    - y' = y

    - where shx is the shearing factor in the x-direction.

  - If the shearing is in the y-direction, then the sheared point (x', y') of a point (x, y) is given by:

    - x' = x
    - y' = y + shy * x

    - where shy is the shearing factor in the y-direction.

- An example of shearing is shown below:

  - The original object is a rectangle with vertices A(1, 1), B(5, 1), C(5, 3), and D(1, 3).
  - The shearing is in the x-direction with a shearing factor of 0.5.
  - The sheared object is a parallelogram with vertices A'(1, 1), B'(7.5, 1), C'(7.5, 3), and D'(3, 3).

```
  y
  ^
  |   C'  B'
  |   |\ /|
  |   | X |
  |   |/ \|
  +---------> x
  |   /   \
  |  /     \
  | /       \
  D'        A' B
  |         | |
  |         | |
  D         A C
```