# Sutherland Hodgeman Polygon Clipping

Sutherland Hodgeman polygon clipping is an algorithm used for clipping polygons. It works by extending each line of the convex clip polygon in turn and selecting only vertices from the subject polygon that are on the visible side.

The algorithm begins with an input list of all vertices in the subject polygon. It is performed by processing the boundary of the polygon against each window corner or edge. First of all, the entire polygon is clipped against one edge, then the resulting polygon is considered, then the polygon is considered against the second edge, and so on for all four edges.

This algorithm is used to clip polygon edges using a convex polygon and a convex clipping area. The input is in the form of vertices of the polygon in clockwise order.