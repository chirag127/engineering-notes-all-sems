### Scan line method for the notes of the Unit 5 - Hidden Lines and Surfaces in the subject of Computer Graphics

The scan line method is a popular hidden surface removal technique in computer graphics. It is also known as the scan-line polygon filling algorithm. This method works by dividing the image into a series of scan lines and then determining the visible surfaces on each line.

Here are the key points to remember about the scan line method:

- The scan line method is a popular algorithm for hidden surface removal in computer graphics.
- It works by dividing the image into a series of scan lines and then determining the visible surfaces on each line.
- The algorithm scans each line of the image from left to right, identifying the edges of polygons that intersect the line.
- It then uses the edges to determine which parts of the polygons are visible on that line.
- The algorithm repeats this process for each scan line, filling in the visible portions of each polygon.
- The scan line method is particularly useful for complex scenes with multiple overlapping polygons.
- It can also be used in conjunction with other algorithms for more accurate results.

Advantages of the scan line method:

- It is a relatively simple algorithm to implement.
- It is particularly effective for scenes with multiple overlapping polygons.
- It can be combined with other algorithms for more accurate results.
- It can handle non-convex polygons.

Disadvantages of the scan line method:

- It can be slow for large scenes with many polygons.
- It requires a lot of memory to store the data for each scan line.
- It may not be suitable for scenes with complex object occlusion.

Example of the scan line method:

Consider a scene with two polygons, A and B, as shown below:

```
Polygon A: (0,0), (3,3), (3,0)
Polygon B: (1,1), (4,4), (4,1)
```

To apply the scan line method, we divide the image into a series of scan lines and identify the edges of the polygons that intersect each line. We then fill in the visible portions of each polygon on each line.

The resulting image would show polygon A on the left and polygon B on the right, with the overlapping region between them filled in:

```
+---+---+---+---+
| A | A | A |   |
+---+---+---+---+
|   | B | B | B |
+---+---+---+---+
```

Applications of the scan line method:

The scan line method is commonly used in computer graphics for:

- Hidden surface removal
- Polygon filling
- Rendering of complex scenes with multiple overlapping polygons