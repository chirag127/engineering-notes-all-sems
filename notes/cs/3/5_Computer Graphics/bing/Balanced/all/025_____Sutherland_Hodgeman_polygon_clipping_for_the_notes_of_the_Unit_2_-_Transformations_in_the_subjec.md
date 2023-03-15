# Sutherland Hodgeman polygon clipping

- Sutherland Hodgeman polygon clipping is an algorithm used for clipping polygons.
- Clipping is the process of removing parts of a polygon that lie outside a given region, such as a window or a viewport.
- The algorithm works by extending each line of the convex clip polygon in turn and selecting only vertices from the subject polygon that are on the visible side.
- The algorithm begins with an input list of all vertices in the subject polygon, and processes the boundary of the polygon against each window edge.
- For each window edge, the algorithm generates a new list of vertices by iterating over the input list and applying the following rules:
  - If the current vertex is inside the window edge, and the previous vertex is outside, then output the intersection point of the polygon edge and the window edge, followed by the current vertex.
  - If the current vertex is inside the window edge, and the previous vertex is also inside, then output the current vertex.
  - If the current vertex is outside the window edge, and the previous vertex is inside, then output the intersection point of the polygon edge and the window edge.
  - If the current vertex is outside the window edge, and the previous vertex is also outside, then output nothing.
- The output list of vertices becomes the input list for the next window edge, until all four edges are processed.
- The final output list contains the vertices of the clipped polygon, in the same order as the original polygon.

: Sutherland–Hodgman algorithm - Wikipedia
: Computer Graphics | Sutherland-Hodgeman Polygon Clipping - javatpoint
: Polygon Clipping | Sutherland–Hodgman Algorithm - GeeksforGeeks