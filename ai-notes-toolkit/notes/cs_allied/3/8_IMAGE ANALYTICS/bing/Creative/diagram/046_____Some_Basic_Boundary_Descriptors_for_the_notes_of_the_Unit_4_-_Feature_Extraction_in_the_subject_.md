### Some Basic Boundary Descriptors

- Boundary descriptors are features that describe the shape and size of an object based on its boundary or contour.
- Boundary descriptors can be classified into two types: global and local.
- Global boundary descriptors capture the overall properties of the boundary, such as length, area, perimeter, compactness, circularity, eccentricity, etc.
- Local boundary descriptors capture the local variations of the boundary, such as curvature, angle, direction, etc.
- Some examples of global boundary descriptors are:

  - **Length**: The length of the boundary is the sum of the distances between consecutive boundary pixels. It can be computed using the Euclidean distance or the city-block distance.
  - **Area**: The area of the object is the number of pixels inside the boundary. It can be computed using a simple counting algorithm or a more efficient scan-line algorithm.
  - **Perimeter**: The perimeter of the object is the length of the boundary. It can be used to measure the smoothness or roughness of the boundary.
  - **Compactness**: The compactness of the object is the ratio of the area to the perimeter squared. It can be used to measure how close the object is to a circle. A circle has the maximum compactness of 1/4π, while a line has the minimum compactness of 0.
  - **Circularity**: The circularity of the object is the ratio of the area to the area of the smallest enclosing circle. It can be used to measure how close the object is to a circle. A circle has the maximum circularity of 1, while a line has the minimum circularity of 0.
  - **Eccentricity**: The eccentricity of the object is the ratio of the distance between the foci of the smallest enclosing ellipse to the major axis of the ellipse. It can be used to measure how elongated the object is. A circle has the minimum eccentricity of 0, while a line has the maximum eccentricity of 1.

- Some examples of local boundary descriptors are:

  - **Curvature**: The curvature of the boundary at a point is the inverse of the radius of the circle that best fits the local neighborhood of the point. It can be used to measure how sharp or smooth the boundary is at that point.
  - **Angle**: The angle of the boundary at a point is the angle between the tangent vectors at that point and the previous point. It can be used to measure the direction change of the boundary at that point.
  - **Direction**: The direction of the boundary at a point is the angle between the tangent vector at that point and a fixed reference axis. It can be used to measure the orientation of the boundary at that point.