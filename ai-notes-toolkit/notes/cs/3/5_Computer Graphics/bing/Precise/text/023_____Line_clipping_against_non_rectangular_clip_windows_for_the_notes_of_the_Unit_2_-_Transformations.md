### Line clipping against non rectangular clip windows

- Line clipping is the process of removing lines or portions of lines outside an area of interest.
- There are several algorithms for line clipping against non-rectangular clip windows.
- One such algorithm is the Cyrus Beck algorithm, which is made for convex polygons.
- It allows line clipping for non-rectangular windows, unlike other algorithms such as Cohen Sutherland or Nicholl Le Nicholl.
- The Cyrus Beck algorithm also removes the repeated clipping needed in the Cohen Sutherland algorithm  .
- The input for the Cyrus Beck algorithm includes the convex area of interest, which is defined by a set of coordinates given in a clockwise fashion .
- Another approach to clipping a line that cannot be trivially accepted is to intersect that line with each of the clip-rectangle edges to see whether any intersection points lie on those edges .
- The result of the classification determines the edges intersected by the line .