### Unit 2 - Transformations: Reflections and Shearing

#### Reflections
- Reflection is a type of transformation that produces a mirror image of an object.
- It is achieved by flipping the object over an imaginary line called the axis of reflection.
- In 2D, the reflection can be performed with respect to the x-axis, y-axis, or any line.
- In 3D, the reflection can be performed with respect to a plane.
- The reflection matrix for reflection with respect to the x-axis is given by:
```
[ -1  0 ]
[  0  1 ]
```
- The reflection matrix for reflection with respect to the y-axis is given by:
```
[  1  0 ]
[  0 -1 ]
```

#### Shearing
- Shearing is a type of transformation that distorts the shape of an object.
- It is achieved by sliding the points of the object along a fixed line or plane.
- In 2D, shearing can be performed with respect to the x-axis or y-axis.
- In 3D, shearing can be performed with respect to a plane.
- The shearing matrix for shearing with respect to the x-axis is given by:
```
[  1  shx ]
[  0   1  ]
```
- The shearing matrix for shearing with respect to the y-axis is given by:
```
[  1   0  ]
[ shy  1  ]
```
- where `shx` and `shy` are the shearing factors along the x and y axes, respectively.
