### Weiler and Atherton polygon clipping

- Weiler and Atherton polygon clipping is a polygon clipping algorithm that can handle concave polygons and polygons with holes.
- Polygon clipping is the process of cutting out a part of a polygon that lies outside a given clipping region, such as a window or a viewport.
- The algorithm works by finding the intersection points of the subject polygon and the clipping polygon, and labeling them as entry or exit points .
- The algorithm then traverses the subject polygon in a clockwise direction, starting from any entry point, and copies the vertices to the output polygon until an exit point is reached .
- The algorithm then switches to the clipping polygon and traverses it in a counter-clockwise direction, copying the vertices to the output polygon until an entry point is reached .
- The algorithm repeats this process until all the entry and exit points are visited, and the output polygon is closed .
- The algorithm can handle multiple output polygons if the subject polygon is split into disjoint parts by the clipping polygon .
- The algorithm can also handle holes in the subject polygon by using a flag to indicate whether a vertex is inside or outside the hole .
- The algorithm can be implemented using data structures such as doubly-linked lists or arrays to store the vertices and the intersection points .
- The algorithm has a time complexity of O(n + m), where n is the number of vertices in the subject polygon and m is the number of vertices in the clipping polygon.