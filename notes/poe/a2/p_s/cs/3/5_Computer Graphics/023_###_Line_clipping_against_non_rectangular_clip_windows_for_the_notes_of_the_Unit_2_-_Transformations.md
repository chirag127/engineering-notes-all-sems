 Here is the content in markdown format for the topic ### Line clipping against non rectangular clip windows for the notes of the Unit 2 - Transformations in the subject of Computer Graphics:

### Line Clipping against Non Rectangular Clip Windows

- Line clipping refers to truncating a line segment to fit within a given shape or window. Clipping against non rectangular windows is more complex than clipping against rectangular windows.
- Some common non rectangular windows are circles, ellipses, polygons, etc. Clipping a line segment against these windows involves checking if the line intersects the window and if so, computing the intersection points and truncating the line segment accordingly.
- To check if a line intersects a non rectangular window, we need to check if the line intersects the edges of the window for shapes like polygons or check if the distance between the line and the center of the window is less than the radius of the window for shapes like circles and ellipses. If an intersection is found, we compute the intersection point(s) and truncate the line segment at those points.
- The line clipping algorithm depends on the type of non rectangular window. For example, to clip a line against a circular window, we need to check if the line passes through or is outside/inside the circle and compute the intersection points accordingly. The algorithm to clip against a polygonal window is more complex and involves checking intersections with each edge of the polygon and handling some special cases.
- Line clipping against non rectangular windows finds applications in computer graphics, collision detection, and other geometry processing tasks. It is a key concept in generating visibility and creating special effects.
- The main advantages are the ability to restrict drawing to specific customized shapes and enabling visibility culling. The disadvantages are the complexity in implementing the clipping algorithm and increased processing time.

[Detailed diagrams and images can be added here to aid understanding]

[Code snippets for line clipping can be added here for reference]