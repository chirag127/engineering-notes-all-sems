# Scan line method

The scan line method is an algorithm for visible surface determination, in 3D computer graphics, that works on a row-by-row basis rather than a polygon-by-polygon or pixel-by-pixel basis . The main steps of the scan line method are:

- Sort all the polygons to be rendered by the top y coordinate at which they first appear.
- For each row or scan line of the image, compute the intersection of the scan line with the polygons on the front of the sorted list, while discarding the no-longer-visible polygons.
- Fill the pixels between the intersection points with the color and intensity of the visible polygon, using a refresh buffer to store the pixel values.
- Repeat the process for the next scan line until the entire image is rendered.

The scan line method is based on the image-space method and the concept of coherence. Coherence means that the pixels that are close to each other in the image space are likely to have similar properties, such as color, depth, and visibility. The scan line method exploits the coherence by processing one line at a time, rather than one pixel at a time, which reduces the computational cost and complexity.

The scan line method can handle concave and intersecting polygons, as well as polygons with holes, by using an active edge list (AEL) to store the edges that cross the current scan line, and a parity flag to indicate whether the scan line is inside or outside a polygon. The AEL is updated as the scan line moves down the image, and the parity flag is toggled whenever the scan line crosses an edge. The pixels between the edges in the AEL are filled with the color of the polygon that has the parity flag on, or the background color if the parity flag is off.

The scan line method is one of the simplest and most efficient algorithms for hidden surface removal, as it avoids the need to compare the depth of every pixel in the image. However, it also has some limitations, such as:

- It requires the polygons to be planar and non-overlapping in the image space, which may not be the case for curved or distorted surfaces.
- It does not handle transparency or shading effects, which require more information than just the color and intensity of the visible polygon.
- It may produce aliasing artifacts, which are jagged edges or gaps in the rendered image, due to the discrete nature of the scan line and the pixels. These artifacts can be reduced by using anti-aliasing techniques, such as supersampling or filtering.