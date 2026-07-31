### 2D Transforms for the Notes of the Unit 1 - Digital Image Fundamentals in the Subject of Image Processing

2D transforms are an essential tool in image processing that enables us to manipulate the position, orientation, and size of an image. In this section, we will discuss the various types of 2D transforms used in image processing.

1. Translation Transform
- The translation transform is used to move an image from one position to another.
- The transform is defined by the distance moved in the horizontal and vertical directions.
- The formula for the translation transform is:
```
T(x,y) = (x + tx, y + ty)
```
- Where `(x,y)` are the coordinates of the original image, and `(tx,ty)` are the translation distances.

2. Rotation Transform
- The rotation transform is used to rotate an image by a given angle.
- The transform is defined by the angle of rotation and the pivot point.
- The formula for the rotation transform is:
```
R(x,y) = (x*cosθ - y*sinθ, x*sinθ + y*cosθ)
```
- Where `(x,y)` are the coordinates of the original image, `θ` is the angle of rotation in radians, and the pivot point is the origin `(0,0)`.

3. Scaling Transform
- The scaling transform is used to change the size of an image.
- The transform is defined by scaling factors in the horizontal and vertical directions.
- The formula for the scaling transform is:
```
S(x,y) = (sx*x, sy*y)
```
- Where `(x,y)` are the coordinates of the original image, and `(sx,sy)` are the scaling factors.

4. Shearing Transform
- The shearing transform is used to distort an image by shifting the position of the pixels in one direction.
- The transform is defined by the shearing factor in the horizontal or vertical direction.
- The formula for the shearing transform is:
```
SH(x,y) = (x + k*y, y + k*x)
```
- Where `(x,y)` are the coordinates of the original image, and `k` is the shearing factor.

In conclusion, 2D transforms are a powerful tool in image processing that enables us to manipulate images in various ways. By understanding the different types of transforms and their formulas, we can perform complex image manipulations with ease.