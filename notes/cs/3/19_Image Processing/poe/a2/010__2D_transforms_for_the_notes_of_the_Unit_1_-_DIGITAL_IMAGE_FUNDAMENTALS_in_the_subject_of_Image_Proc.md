 Here is the content in markdown format without any emojis or external links and in a formal tone:

### 2D transforms for the notes of the Unit 1 - DIGITAL IMAGE FUNDAMENTALS

1. Translation: Shifting an image horizontally, vertically or both. It does not change the size or shape of the image. Formula: x' = x + a, y' = y + b.

2. Scaling: Increasing or decreasing the size of an image. It can be done in x direction, y direction or both. Formula: x' = ax, y' = by.

3. Rotation: Rotating an image at an angle theta. Formula: x' = xcos(theta) - ysin(theta), y' = xsin(theta) + ycos(theta).

4. Shearing: Distorting the shape of an object by slanting one of its sides. Formula: x' = x + ky, y' = y. It shears the object in x direction. For y direction, formula is: x' = x, y' = y + kx.

5. Affine transform: Most generic 2D transform involving scaling, rotation, shearing, translation, skewing and combinations of these. Formula: [x' y'] = [a b c d] * [x y] + [e f] where a, b, c, d, e and f are parameters.

The 2D transforms are useful in image registration, object recognition, geometric correction etc. The transformation matrix and inverse matrix can be used to transform and inverse transform images respectively.