# Line clipping algorithms

- Line clipping is the process of removing (clipping) lines or portions of lines outside an area of interest (a viewport or view volume) in computer graphics.
- Line clipping is useful for rendering only the visible parts of a scene, reducing the computational cost and improving the performance of graphics applications.
- There are many algorithms for line clipping, but two of the most common ones are Cohen–Sutherland and Liang–Barsky.

## Cohen–Sutherland algorithm

- The Cohen–Sutherland algorithm (named after Danny Cohen and Ivan Sutherland) is a line-clipping algorithm that divides a 2D space into 9 regions, of which only the middle part (viewport) is visible.
- The algorithm assigns a 4-bit code to each endpoint of a line, based on its position relative to the viewport. The code indicates which of the four boundaries (top, bottom, left, right) the point is outside of, or zero if the point is inside the viewport.
- The algorithm then performs a series of tests on the codes to determine if the line is trivially accepted (both endpoints are inside the viewport), trivially rejected (both endpoints are outside the same boundary), or needs to be clipped (one or both endpoints are outside different boundaries).
- If the line needs to be clipped, the algorithm finds the intersection point of the line with the boundary that corresponds to the first non-zero bit in the code, and replaces the endpoint with the intersection point. The algorithm then repeats the process until the line is either accepted or rejected.

## Liang–Barsky algorithm

- The Liang–Barsky algorithm is a line-clipping algorithm that uses a parametric form of the line equation to find the intersection points of the line with the viewport boundaries.
- The algorithm assumes that the line can be represented as P(t) = P0 + t(P1 - P0), where P0 and P1 are the endpoints of the line, and t is a parameter that ranges from 0 to 1.
- The algorithm then computes four values, p, q, r, and s, that represent the coefficients and constants of the inequalities that define the viewport. For example, p = P1x - P0x, q = P0x - xmin, r = p/q, and s = q/p, where xmin is the left boundary of the viewport.
- The algorithm then finds the values of t that satisfy the inequalities, and uses them to determine the intersection points of the line with the viewport. The algorithm then clips the line segment between the minimum and maximum values of t that are within the range of 0 to 1.