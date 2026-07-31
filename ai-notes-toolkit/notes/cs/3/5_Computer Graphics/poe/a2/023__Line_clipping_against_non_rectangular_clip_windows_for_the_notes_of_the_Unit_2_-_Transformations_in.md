 Here is the formal content in markdown format without any emojis or external links on the topic "Line clipping against non rectangular clip windows" for the notes of Unit 2 - Transformations in Computer Graphics:

### Line clipping against non rectangular clip windows

1. Line clipping is a process of modifying a line segment so that it fits within a rectangular window. Clipping against non rectangular windows is an extension of line clipping against rectangular windows.
2. The clip window can be any arbitrary shape. The line segment is clipped against the edges of this window. The input is the line segment and the clip window. The output is the clipped line segment.
3. The line segment can be clipped in three ways:
- Completely inside: If the line segment lies completely inside the clip window, then the clipped line segment is the same as the input line segment.
- Completely outside: If the line segment lies completely outside the clip window, then the clipped line segment is a null line segment.
- Partly inside and outside: If the line segment intersects the clip window, then the portions of the line segment inside the clip window are retained and the portions outside are discarded. The retained portions form the clipped line segment.
4. To clip a line against a non rectangular clip window, the clip window is approximated to a rectangle. The line is clipped against this approximated rectangle. The clipped line may extend beyond the actual clip window. These portions are again clipped against the actual clip window edges to get the final clipped line segment. This is done iteratively till the clipped line segment lies within the actual clip window.
5. The above algorithm can lead to computation errors if the approximation is poor. A more efficient algorithm is to express the non rectangular clip window as a combination of rectangular and triangular primitives and then clip the line segment against these primitives. This avoids multiple approximations and iterations leading to more accurate results.