### Some Basic Boundary Descriptors for the notes of the Unit 4 - Feature Extraction in the subject of IMAGE ANALYTICS

- Boundary descriptors are features that describe the shape and contour of an object or a region in an image.
- Boundary descriptors can be used for image representation and description, which are important tasks in image processing, computer vision, pattern recognition, and machine learning .
- Some basic boundary descriptors are :
  - **Boundary length**: the number of pixels along the border of the object or region. It can be computed by counting the pixels or using a chain code representation.
  - **Diameter**: the maximum distance between any two pixels on the boundary of the object or region. It can be computed by finding the pair of pixels that have the largest Euclidean distance.
  - **Curvature**: the rate of change of the slope or direction of the boundary. It can be computed by using the first or second derivative of the chain code or by fitting a curve to the boundary points.
  - **Bounding box**: the smallest rectangle that encloses the object or region. It can be computed by finding the minimum and maximum values of the x and y coordinates of the boundary pixels.
  - **Convex hull**: the smallest convex polygon that contains the object or region. It can be computed by using a convex hull algorithm, such as Graham scan or Jarvis march.
  - **Eccentricity**: the ratio of the distance between the foci of the best fitting ellipse to the object or region and its major axis length. It can be computed by using the second moment matrix of the boundary pixels or by fitting an ellipse to the boundary points.
  - **Orientation**: the angle between the major axis of the best fitting ellipse to the object or region and the x-axis. It can be computed by using the second moment matrix of the boundary pixels or by fitting an ellipse to the boundary points.
  - **Compactness**: the ratio of the area of the object or region to the area of a circle with the same perimeter as the object or region. It can be computed by using the formula `4πA/P^2`, where A is the area and P is the perimeter of the object or region.
  - **Circularity**: the inverse of the compactness. It can be computed by using the formula `P^2/4πA`, where P is the perimeter and A is the area of the object or region.