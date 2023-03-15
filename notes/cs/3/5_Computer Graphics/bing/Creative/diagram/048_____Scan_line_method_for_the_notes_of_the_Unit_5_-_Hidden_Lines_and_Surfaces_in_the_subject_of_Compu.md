Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the scan line method for hidden lines and surfaces in computer graphics:

### Scan line method

- Scan line method is an algorithm for visible surface determination, in 3D computer graphics, that works on a row-by-row basis rather than a polygon-by-polygon or pixel-by-pixel basis.
- The basic idea is to sort all the polygons to be rendered by the top y coordinate at which they first appear, then scan each row or scan line of the image and compute the intersection of the scan line with the polygons on the front of the sorted list, while updating the list to discard no-longer-visible polygons.
- The scan line method can be applied to both solid and wireframe models, and can handle concave and self-intersecting polygons as well.
- The scan line method can be divided into two phases: the initialization phase and the scan conversion phase.

#### Initialization phase

- In this phase, the polygons are sorted by their minimum y coordinate, and an active edge list (AEL) is created to store the edges that intersect the current scan line.
- The AEL is sorted by the x coordinate of the intersection point, and each edge has a flag to indicate whether it belongs to a visible surface or not.
- The AEL is updated as the scan line moves down, by adding new edges that start at the current scan line, and removing edges that end at the current scan line.
- The AEL is also updated by changing the x coordinate of the intersection point according to the slope of the edge, and by changing the flag of the edge according to the parity rule.
- The parity rule states that an edge is visible if the number of visible edges to its left is odd, and invisible if the number of visible edges to its left is even.

#### Scan conversion phase

- In this phase, the pixels on the current scan line are filled with the color of the visible surface, by using the information in the AEL.
- The algorithm scans the AEL from left to right, and maintains a flag to indicate whether the current pixel is inside or outside a visible surface.
- The flag is toggled whenever the algorithm encounters an edge in the AEL.
- The algorithm fills the pixels with the color of the surface that corresponds to the first edge in the AEL, and skips the pixels that are outside any visible surface.
- The algorithm repeats this process for each scan line until all the polygons are processed.

#### Example

- Consider the following example of three polygons A, B, and C, with their minimum and maximum y coordinates and their colors:

| Polygon | Min y | Max y | Color |
|---------|-------|-------|-------|
| A       | 2     | 6     | Red   |
| B       | 3     | 7     | Green |
| C       | 4     | 8     | Blue  |

- The initialization phase will sort the polygons by their min y coordinate, and create the AEL as follows:

| Scan line | AEL                          |
|-----------|------------------------------|
| 2         | (A, visible)                 |
| 3         | (A, visible), (B, visible)   |
| 4         | (A, invisible), (B, visible), (C, visible) |
| 5         | (A, invisible), (B, visible), (C, visible) |
| 6         | (B, visible), (C, visible)   |
| 7         | (B, invisible), (C, visible) |
| 8         | (C, visible)                 |

- The scan conversion phase will fill the pixels on each scan line with the color of the visible surface, as follows:

| Scan line | Pixels filled |
|-----------|---------------|
| 2         | Red           |
| 3         | Red, Green    |
| 4         | Green, Blue   |
| 5         | Green, Blue   |
| 6         | Green, Blue   |
| 7         | Blue          |
| 8         | Blue          |

- The final image will look like this:

![Scan line method example](https://media.geeksforgeeks.org/wp-content/uploads/20210214184128/