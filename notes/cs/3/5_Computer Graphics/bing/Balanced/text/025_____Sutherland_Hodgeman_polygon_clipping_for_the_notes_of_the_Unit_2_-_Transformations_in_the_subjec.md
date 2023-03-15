### Sutherland Hodgeman polygon clipping

- Sutherland Hodgeman polygon clipping is an algorithm used for clipping polygons.
- Clipping is the process of removing parts of a polygon that lie outside a given region, such as a window or a viewport.
- The algorithm works by extending each line of the convex clip polygon in turn and selecting only vertices from the subject polygon that are on the visible side.
- The algorithm begins with an input list of all vertices in the subject polygon, and processes the boundary of the polygon against each window edge.
- For each window edge, the algorithm generates a new list of vertices by examining each pair of consecutive vertices in the input list and applying the following rules:
  - If both vertices are inside the window, the second vertex is added to the output list.
  - If the first vertex is outside and the second vertex is inside, the intersection point of the edge and the window boundary is added to the output list, followed by the second vertex.
  - If both vertices are outside, no vertices are added to the output list.
  - If the first vertex is inside and the second vertex is outside, the intersection point of the edge and the window boundary is added to the output list.
- The output list becomes the input list for the next window edge, and the process is repeated until all window edges are processed.
- The final output list contains the vertices of the clipped polygon.

The following diagram illustrates the algorithm for a sample polygon and a window:

![Sutherland Hodgeman polygon clipping example](https://media.geeksforgeeks.org/wp-content/uploads/20180527194916/Sutherland-Hodgman-Algorithm.png)

: Sutherland–Hodgman algorithm - Wikipedia
: Computer Graphics | Sutherland-Hodgeman Polygon Clipping - javatpoint
: Polygon Clipping | Sutherland–Hodgman Algorithm - GeeksforGeeks