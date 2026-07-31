### Polyline

- A polyline is a continuous line that is composed of one or more connected straight line segments, which, together, make up a shape .
- A polyline can also include arc segments, or a combination of straight and arc segments .
- A polyline is created as a single object, which means that it can be modified, moved, copied, or deleted as a whole .
- A polyline can have different properties, such as width, color, linetype, and elevation .
- A polyline can be used for various purposes, such as:
  - Smart application of non-continuous linetypes across vertices .
  - Creation of complex shapes with fewer objects .
  - Editing of multiple segments simultaneously .
  - Calculation of the length, area, and perimeter of the shape .
- A polyline can be created by specifying the endpoints of each segment, or by using existing objects, such as lines, arcs, circles, or ellipses .
- A polyline can be edited by using commands, such as PEDIT, JOIN, TRIM, EXTEND, FILLET, CHAMFER, or SPLINE .

Here is an example of a polyline that consists of four straight segments and one arc segment:

```
    A
   / \
  /   \
 /     \
B       C
|       |
|       |
D-------E
```

The polyline can be created by specifying the coordinates of points A, B, D, E, and C, and choosing the Arc option for the segment between A and C. Alternatively, the polyline can be created by using existing lines and arcs, and joining them with the PEDIT command. The polyline can be modified by changing its width, color, linetype, or elevation, or by adding or removing vertices, or by converting it to a spline. The polyline can be measured by using the LIST or PROPERTIES command, or by using the AREA command with the Object option. The polyline can be deleted by selecting it and pressing the Delete key.