### Sutherland Hodgeman polygon clipping

Sutherland Hodgeman polygon clipping is an algorithm used for clipping polygons. It works by extending each line of the convex clip polygon in turn and selecting only vertices from the subject polygon that are on the visible side.

The algorithm is performed by processing the boundary of the polygon against each window corner or edge. First, the entire polygon is clipped against one edge, then the resulting polygon is considered against the second edge, and so on for all four edges.

This algorithm is useful for clipping polygons in computer graphics applications. It is a standard algorithm for this purpose and is widely used in the field.