### Cohen Sutherland line clipping algorithm

- Line clipping is the process of removing the portions of a line that are outside a given rectangular window, while preserving the portions that are inside or on the boundary of the window.
- Cohen Sutherland algorithm is a line clipping algorithm that divides a two-dimensional space into 9 regions and then efficiently determines the lines and portions of lines that are visible in the central region of interest (the viewport).
- The algorithm can be outlined as follows:

  1. Assign a 4-bit code to each endpoint of the line, based on its position relative to the window. The code is computed by testing the endpoint against the four boundaries of the window, and setting the corresponding bit to 1 if the endpoint is outside that boundary, or 0 if it is inside or on the boundary. The four bits represent the top, bottom, right and left boundaries, in that order. For example, the code 1010 means that the endpoint is above and to the left of the window, while the code 0000 means that the endpoint is inside the window.
  2. Perform a logical OR operation on the two endpoint codes. If the result is 0000, then the line is completely inside the window and can be drawn. If the result has any 1 bits, then the line may be partially or completely outside the window, and further tests are needed.
  3. Perform a logical AND operation on the two endpoint codes. If the result is not 0000, then the line is completely outside the window and can be discarded. If the result is 0000, then the line is partially inside the window, and one of the endpoints needs to be clipped to the window boundary.
  4. To clip an endpoint, find the boundary where the endpoint is outside, and compute the intersection point of the line and that boundary using the parametric equation of the line. Replace the original endpoint with the intersection point, and assign a new code to it. Repeat steps 2 and 3 until the line is either accepted or rejected.

- The algorithm is efficient because it avoids unnecessary calculations and comparisons by using the bit codes to quickly identify the trivial cases (completely inside or outside) and the boundary where the clipping is needed.
- The algorithm works only for rectangular windows. For other shapes of windows, other algorithms such as Cyrus Beck algorithm or Sutherland Hodgman algorithm are needed.