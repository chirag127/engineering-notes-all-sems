 Here is the content in markdown format for the topic ### 2-D Clipping algorithms for the notes of the Unit 2 - Transformations in the subject of Computer Graphics:

## 2-D Clipping Algorithms

- Clipping is a process of removing some parts of a geometric primitive that lie outside the viewing volume.
- The viewing volume is defined by a clipping window which is a bounded region. Any part of the primitive that lies within the clipping window is retained, and the parts outside are removed.
- Clipping algorithms decide whether a point lies inside or outside the clipping window and clip the primitives accordingly.
- The clipping algorithms are divided into two types:

1. Cohen-Sutherland Line Clipping Algorithm:
    - Clips lines that lie partially or completely outside the viewing window.
    - Each edge of the clipping window is assigned a code out of N, S, E, W denoting whether the line passes through that edge.
    - Based on the combinations of codes of the two endpoints of a line, the algorithm retains or rejects the line.
    - Advantages: Handles lines efficiently. Easy to implement.
    - Disadvantages: Only works for lines. Not extendable to other primitives.

2. Sutherland-Hodgman Polygon Clipping Algorithm:
    - Clips convex and concave polygons that lie partially or completely outside the viewing window.
    - Finds intersections of edges of the polygon with edges of the clipping window.
    - Deletes the portions of edges outside the clipping window and adds new edges for the clipped portion.
    - Can handle polygons of any shape. More generic than Cohen-Sutherland algorithm.
    - Disadvantage: Can produce extra vertices leading to loss in efficiency.

- The clipping algorithms are important to efficiently remove hidden portions of objects and retain only the visible parts to be displayed on the screen. This improves rendering speed and quality.
- They find applications in computer graphics, computer vision, and other fields.