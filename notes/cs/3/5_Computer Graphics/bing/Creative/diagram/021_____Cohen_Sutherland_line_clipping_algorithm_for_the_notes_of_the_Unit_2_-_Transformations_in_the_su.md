### Cohen Sutherland line clipping algorithm

- Line clipping is the process of removing the portions of a line that are outside a given rectangular window, while preserving the portions that are inside or on the boundary of the window.
- Cohen Sutherland algorithm is a line clipping algorithm that divides a two-dimensional space into 9 regions and then efficiently determines the lines and portions of lines that are visible in the central region of interest (the viewport)  .
- The algorithm can be outlined as follows :
  - Nine regions are created, eight "outside" regions and one "inside" region. Each region is assigned a 4-bit code, called the outcode, based on the position of the region relative to the window. The outcode is computed as follows:

    | Bit | Position | Value |
    | --- | -------- | ----- |
    | 1   | Above    | 1 if the region is above the window, 0 otherwise |
    | 2   | Below    | 1 if the region is below the window, 0 otherwise |
    | 3   | Right    | 1 if the region is right of the window, 0 otherwise |
    | 4   | Left     | 1 if the region is left of the window, 0 otherwise |

  - For example, the outcode for the top-right region is 1001, and the outcode for the inside region is 0000.
  - For each line, the outcodes of the endpoints are computed. If both outcodes are 0000, the line is entirely inside the window and can be drawn. If the bitwise AND of the outcodes is not 0, the line is entirely outside the window and can be discarded.
  - If neither of the above cases apply, the line is partially inside the window and needs to be clipped. To do this, one of the endpoints that is outside the window is selected, and the intersection point of the line and the window boundary that corresponds to the first non-zero bit in the outcode is computed. The endpoint is then replaced by the intersection point, and the outcode is updated. This process is repeated until the line is either accepted or rejected.
- The algorithm is illustrated in the following diagram :

```
+-------------------+
|                   |
|                   |
|                   |
|                   |
|                   |
|                   |
|                   |
|                   |
|                   |
|                   |
|                   |
|                   |
|                   |
|                   |
|                   |
+-------------------+

  1001  1000  1010
  0001  0000  0010
  0101  0100  0110

  A: 1001
  B: 0000
  C: 0010
  D: 0100
  E: 0110

  Line AB: Accepted
  Line BC: Clipped to BQ
  Line CD: Clipped to PR
  Line DE: Rejected
```