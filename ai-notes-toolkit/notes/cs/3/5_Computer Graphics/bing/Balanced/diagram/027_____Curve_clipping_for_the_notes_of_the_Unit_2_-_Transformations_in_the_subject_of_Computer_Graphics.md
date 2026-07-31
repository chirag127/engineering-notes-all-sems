### Curve clipping

- Curve clipping is a method to selectively enable or disable rendering operations within a defined region of interest.
- Curve clipping involves complex procedures as compared to line clipping or polygon clipping .
- Curve clipping requires more processing than for objects with linear boundaries.
- A common technique for curve clipping is to approximate the curve by a series of line segments and then clip each segment individually.
- Another technique is to use a parametric representation of the curve and clip it against the boundaries of the clipping window.
- The window against which the curve is clipped is called a clip window. It can be curved or rectangular in shape.
- An example of curve clipping is shown below:

![Curve clipping example](https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Clipping_example.svg/1200px-Clipping_example.svg.png)

- In this example, the blue curve is clipped against the red rectangular window. The resulting curve is shown in green. The parts of the curve that are outside the window are discarded.