# Weiler and Atherton polygon clipping

- Weiler and Atherton polygon clipping is a polygon clipping algorithm that can handle concave polygons and polygons with holes.
- Polygon clipping is the process of finding the intersection of a polygon and a clipping region, such as a window or a viewport.
- The algorithm works by finding the intersection points of the subject polygon and the clipping polygon, and labeling them as entry or exit points .
- The algorithm then traverses the subject polygon in a clockwise direction, starting from any entry point, and adds the vertices to the output polygon until an exit point is reached .
- The algorithm then switches to the clipping polygon and traverses it in a counter-clockwise direction, adding the vertices to the output polygon until an entry point is reached .
- The algorithm repeats this process until all the entry and exit points are visited, and the output polygon is closed .
- The algorithm can handle multiple output polygons if the subject polygon is split into disjoint parts by the clipping polygon .
- The algorithm can also handle holes in the subject polygon by using a flag to indicate whether a vertex is inside or outside the hole.
- The algorithm is more efficient than the Sutherland-Hodgman algorithm for concave polygons, but it requires more preprocessing and sorting of the intersection points .