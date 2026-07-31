### Sutherland Hodgeman polygon clipping

- The Sutherland–Hodgman algorithm is an algorithm used for clipping polygons.
- It works by extending each line of the convex clip polygon in turn and selecting only vertices from the subject polygon that are on the visible side.
- The algorithm begins with an input list of all vertices in the subject polygon.
- It is performed by processing the boundary of polygon against each window corner or edge.
- First of all entire polygon is clipped against one edge, then resulting polygon is considered, then the polygon is considered against the second edge, so on for all four edges.
