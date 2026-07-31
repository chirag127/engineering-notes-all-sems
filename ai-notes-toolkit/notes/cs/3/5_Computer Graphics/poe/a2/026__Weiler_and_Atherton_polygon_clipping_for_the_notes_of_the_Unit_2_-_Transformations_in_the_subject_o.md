 Here is the formal content in Markdown format without any emojis or external links for the given topic:

### Weiler and Atherton polygon clipping

- Weiler and Atherton algorithm is used for clipping a polygon against a clipping window.
- It classifies each edge of the polygon as intersecting, inside or outside the clipping window.
- The intersecting edges are split into two parts - one inside and one outside.
- The final clipped polygon is formed by the edges classified as inside the clipping window.
- The algorithm proceeds as:

1. Label each vertex of the polygon as inside, outside or intersecting the clipping window.
2. Classify each edge of the polygon based on the labels of its end points.
3. Split the intersecting edges by computing the intersection point with the clipping window.
4. Discard the edges classified as outside and form the clipped polygon from the edges classified as inside.

- The Weiler and Atherton algorithm has a time complexity of O(n) where n is the number of edges of the polygon.
- It handles self-intersections and complex polygons well while clipping.
- It is an efficient polygon clipping algorithm and is commonly used in computer graphics applications.

The content is written in a formal tone with points and without any emojis or external links as per the given requirements. Please let me know if you would like me to modify or expand the answer.