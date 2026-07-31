### Line clipping against non rectangular clip windows

- Line clipping is the process of removing the portions of a line that lie outside a given region of interest, such as a window or a polygon.
- Line clipping algorithms can be classified into two categories: rectangular and non-rectangular.
- Rectangular line clipping algorithms, such as Cohen-Sutherland and Liang-Barsky, are efficient and simple, but they can only handle rectangular windows.
- Non-rectangular line clipping algorithms, such as Cyrus-Beck and Sutherland-Hodgman, can handle convex polygons as windows, but they are more complex and require more computations.
- Cyrus-Beck is a non-rectangular line clipping algorithm that is based on the parametric equation of a line and the normal vectors of the polygon edges.
- The algorithm works as follows:

  - Given a line L: P = P0 + t(P1 - P0), where P0 and P1 are the endpoints of the line, and a convex polygon W with n edges, define the normal vector N[i] for each edge E[i] of W, pointing outside the polygon.
  - For each edge E[i] of W, compute the dot product D[i] = N[i] . (P1 - P0) and the parameter value t[i] = N[i] . (P0 - V[i]) / D[i], where V[i] is any vertex on E[i].
  - If D[i] = 0, then the line is parallel to the edge E[i]. If t[i] < 0, then the line is outside the edge E[i]. If t[i] > 0, then the line is inside the edge E[i].
  - If D[i] > 0, then the line is entering the polygon through the edge E[i]. If D[i] < 0, then the line is leaving the polygon through the edge E[i].
  - Find the maximum of the entering values tE = max{t[i] | D[i] > 0} and the minimum of the leaving values tL = min{t[i] | D[i] < 0}.
  - If tE > tL, then the line is completely outside the polygon and can be discarded. If tE < tL, then the line is partially inside the polygon and can be clipped to the segment P(tE) to P(tL). If tE = tL, then the line is tangent to the polygon and can be clipped to the point P(tE) = P(tL).

- The following figure illustrates the Cyrus-Beck algorithm for a line and a convex polygon.

```
    P1
    /\
   /  \
  /    \
 /      \
/        \
\        /
 \      /
  \    /
   \  /
    \/
    P0

    |<-- tE -->|<-- tL -->|
    P0        P(tE)     P(tL)        P1
    |----------------------------------|
    |          |          |           |
    |          |          |           |
    |          |          |           |
    |          |          |           |
    |          |          |           |
    |          |          |           |
    |          |          |           |
    |          |          |           |
    |          |          |           |
    |          |          |           |
    |          |          |           |
    |----------------------------------|
    V[0]      E[0]       E[1]       V[1]

    N[0] = (0, -1)
    N[1] = (1, 0)
    D[0] = N[0] . (P1 - P0) = -1
    D[1] = N[1] . (P1 - P0) = 1
    t[0] = N[0] . (P0 - V[0]) / D[0] = 0.25
    t[1] = N[1] . (P0 - V[1]) / D[1] = 0.75
    tE = max{t[0]} = 0.25
    tL = min{t[1]} = 0.75
    tE < tL, so the line is partially inside the polygon and can be clipped to P(0.25) to P(0.75).
```