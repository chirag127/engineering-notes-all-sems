### Sutherland Hodgeman polygon clipping

Sutherland Hodgeman polygon clipping is an algorithm used in computer graphics to clip polygonal shapes against a rectangular clipping region. It is named after its inventors, Ivan Sutherland and Gary Hodgeman.

The algorithm works by processing the polygon's vertices and edges, and determining which parts of the polygon are inside or outside the clipping region. The resulting clipped polygon is then constructed from the vertices that are inside the clipping region, as well as the intersection points of the polygon's edges with the clipping region's boundaries.

The algorithm can be summarized in the following steps:
1. Initialize the output list of vertices to be the input polygon's vertices.
2. For each edge of the clipping region, do the following:
    1. Initialize a new, empty list of vertices.
    2. For each pair of consecutive vertices in the output list, do the following:
        1. If the first vertex is inside the clipping region, add it to the new list of vertices.
        2. If the edge formed by the two vertices crosses the clipping region's boundary, compute the intersection point and add it to the new list of vertices.
    3. Set the output list of vertices to be the new list of vertices.
3. The resulting output list of vertices is the clipped polygon.

This algorithm is efficient and easy to implement, making it a popular choice for polygon clipping in computer graphics. It is important to note that the algorithm only works for convex clipping regions, and may produce incorrect results for concave clipping regions. Additionally, the algorithm may produce degenerate polygons (e.g. polygons with zero area) in certain cases, which may need to be handled separately.