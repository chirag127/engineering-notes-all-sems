# Sutherland Hodgeman polygon clipping

- Sutherland Hodgeman polygon clipping is an algorithm used for clipping polygons.
- Clipping is the process of removing parts of a polygon that lie outside a given region, such as a window or a viewport.
- The algorithm works by extending each line of the convex clip polygon in turn and selecting only vertices from the subject polygon that are on the visible side.
- The algorithm begins with an input list of all vertices in the subject polygon, and processes them against each edge of the clip polygon in a clockwise order .
- For each edge of the clip polygon, the algorithm generates a new list of vertices by examining each pair of consecutive vertices in the input list and applying one of the following rules :
  - If both vertices are inside the clip edge, output the second vertex.
  - If the first vertex is outside and the second vertex is inside, output the intersection point of the edge and the clip boundary, followed by the second vertex.
  - If the first vertex is inside and the second vertex is outside, output the intersection point of the edge and the clip boundary.
  - If both vertices are outside, output nothing.
- The output list of vertices becomes the input list for the next clip edge, until all edges are processed .
- The final output list contains the vertices of the clipped polygon .

: Sutherland–Hodgman algorithm - Wikipedia
: Computer Graphics | Sutherland-Hodgeman Polygon Clipping - javatpoint
: Polygon Clipping | Sutherland–Hodgman Algorithm - GeeksforGeeks