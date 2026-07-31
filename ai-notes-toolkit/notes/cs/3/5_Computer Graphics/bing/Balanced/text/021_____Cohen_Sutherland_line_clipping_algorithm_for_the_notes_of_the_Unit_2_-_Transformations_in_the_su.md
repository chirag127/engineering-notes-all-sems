### Cohen Sutherland line clipping algorithm

- Line clipping is the process of removing lines or portions of lines that are outside a given region of interest, such as a rectangular window or a viewport.
- Cohen Sutherland algorithm is a line clipping algorithm that divides a two-dimensional space into nine regions: one inside region and eight outside regions, each corresponding to a bit code of four bits.
- The bit code of a point is determined by comparing its x and y coordinates with the boundaries of the window. The four bits represent the top, bottom, right and left positions of the point relative to the window, as shown below:

```
  1001 | 1000 | 1010
  -----+------+-----
  0001 | 0000 | 0010
  -----+------+-----
  0101 | 0100 | 0110
```

- The algorithm can be summarized as follows:

  - Assign a bit code to each endpoint of the line.
  - If both endpoints have a bit code of 0000, the line is entirely inside the window and can be drawn.
  - If the logical AND of the bit codes of the endpoints is not 0000, the line is entirely outside the window and can be discarded.
  - If neither of the above cases apply, the line is partially inside the window and needs to be clipped. To do this, find an intersection point of the line with one of the window boundaries, and replace the endpoint that is outside the window with the intersection point. Repeat this process until the line is either accepted or rejected.