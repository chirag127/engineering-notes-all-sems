### 2-D Clipping algorithms for the notes of the Unit 2 - Transformations in the subject of Computer Graphics

In computer graphics, clipping is the process of removing the portions of an object that are not visible to the viewer. 2-D clipping algorithms are used to clip 2-dimensional graphics objects such as lines, polygons, etc. In this unit, we will study various 2-D clipping algorithms. Let's dive into the details:

#### Cohen-Sutherland Line Clipping Algorithm

Cohen-Sutherland line clipping algorithm is a popular algorithm used to clip lines in 2-D space. This algorithm divides the 2-D space into nine regions and checks each endpoint of a line to determine whether it is inside, outside, or on the boundary of the clipping window. If an endpoint is inside the clipping window, it is accepted. If an endpoint is outside the clipping window, it is rejected. If an endpoint is on the boundary of the clipping window, the algorithm checks whether it is partially inside or outside the clipping window. If it is partially inside, the algorithm calculates the intersection point of the line with the boundary and accepts it.

#### Liang-Barsky Line Clipping Algorithm

Liang-Barsky line clipping algorithm is an improvement over the Cohen-Sutherland algorithm. It is faster and more efficient. This algorithm uses parametric equations to represent the line and the clipping edges. It checks whether the line intersects with the clipping edges and determines the intersection points. If the line is completely inside the clipping window, it is accepted. If it is completely outside, it is rejected. If it partially intersects, the algorithm calculates the intersection points and accepts the portion of the line that lies inside the clipping window.

#### Sutherland-Hodgman Polygon Clipping Algorithm

Sutherland-Hodgman polygon clipping algorithm is used to clip polygons in 2-D space. This algorithm clips a polygon against each edge of the clipping window. It uses the concept of inside and outside to determine which portion of the polygon lies inside the clipping window. The algorithm processes each vertex of the polygon and determines whether it is inside or outside the clipping window. If a vertex is inside, it is added to the output polygon. If a vertex is outside, the algorithm calculates the intersection point of the polygon edge with the clipping edge and adds it to the output polygon.

#### Advantages of 2-D Clipping Algorithms

- They help in improving the performance of the computer graphics system by removing the portions of objects that are not visible to the viewer.
- They help in reducing the complexity of the graphics objects by removing the hidden portions.
- They help in reducing the memory requirements of the graphics system by storing only the visible portions of the objects.

#### Disadvantages of 2-D Clipping Algorithms

- They can result in loss of information if the clipped portions of the objects are important for the application.
- They can introduce distortion in the graphics objects if the clipping is not done properly.

#### Applications of 2-D Clipping Algorithms

- They are used in video games to improve the performance of the game by removing the hidden portions of the objects.
- They are used in computer-aided design (CAD) software to clip the graphics objects to the viewport.
- They are used in image processing to crop the images and remove the unwanted portions. 

In conclusion, 2-D clipping algorithms are an important topic in computer graphics. They help in improving the performance and reducing the complexity and memory requirements of the graphics system. We have studied various 2-D clipping algorithms such as Cohen-Sutherland line clipping algorithm, Liang-Barsky line clipping algorithm, and Sutherland-Hodgman polygon clipping algorithm. We have also discussed their advantages, disadvantages, and applications.