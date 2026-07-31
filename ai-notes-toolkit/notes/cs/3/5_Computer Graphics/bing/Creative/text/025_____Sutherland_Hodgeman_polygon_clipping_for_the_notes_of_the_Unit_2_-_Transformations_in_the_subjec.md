### Sutherland Hodgeman polygon clipping

- Sutherland Hodgeman polygon clipping is an algorithm used for clipping polygons.
- Clipping is the process of removing parts of a polygon that lie outside a given region, such as a window or a viewport.
- The algorithm works by extending each line of the convex clip polygon in turn and selecting only vertices from the subject polygon that are on the visible side.
- The algorithm begins with an input list of all vertices in the subject polygon in clockwise order.
- The algorithm then clips the input polygon against each edge of the clip polygon, one at a time, and produces a new list of vertices for the output polygon.
- The algorithm repeats this process for all four edges of the clip polygon, and the final output polygon is the result of the clipping.
- The algorithm can handle concave subject polygons, but the clip polygon must be convex.
- The algorithm can also handle holes in the subject polygon, by reversing the order of the vertices for the hole and treating it as a separate polygon.
- The algorithm is efficient and simple to implement, but it can produce degenerate cases, such as when a vertex lies on an edge of the clip polygon, or when an edge of the subject polygon is parallel to an edge of the clip polygon.
- The algorithm can be modified to handle these cases, by using a different vertex selection rule, or by introducing a small perturbation to the vertices or the edges.

: Sutherland–Hodgman algorithm - Wikipedia
: Computer Graphics | Sutherland-Hodgeman Polygon Clipping - javatpoint
: Polygon Clipping | Sutherland–Hodgman Algorithm - GeeksforGeeks