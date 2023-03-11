### 2-D Clipping algorithms for the notes of the Unit 2 - Transformations in the subject of Computer Graphics

In computer graphics, clipping is the process of selecting the geometry that lies within a particular region of interest (ROI). This process is essential because not all objects in a scene need to be rendered, which saves computational resources and increases performance. Clipping algorithms are used to remove the portions of an object that are outside the ROI. In this section, we will discuss 2-D clipping algorithms in detail.

#### Cohen-Sutherland Algorithm

The Cohen-Sutherland algorithm is a line clipping algorithm that was developed in 1967. It is a simple algorithm that works by dividing the 2-D space into nine regions. Each region is assigned a binary code based on the position of the endpoints of the line. If the endpoints of the line lie in the same region, the line is completely inside the ROI. If the endpoints are in different regions, the algorithm checks if the line intersects with the ROI. If it does, the algorithm recursively clips the line until it is completely inside or outside the ROI. The advantage of this algorithm is that it can quickly determine if a line is completely inside or outside the ROI.

#### Liang-Barsky Algorithm

The Liang-Barsky algorithm is another line clipping algorithm that was developed in 1984. It is a more efficient algorithm than the Cohen-Sutherland algorithm because it uses parametric equations to clip the line. The algorithm works by computing the intersection points between the line and the ROI. If the endpoints of the line lie outside the ROI, the algorithm clips the line based on the intersection points. The advantage of this algorithm is that it can handle lines that are partially inside and partially outside the ROI.

#### Sutherland-Hodgman Algorithm

The Sutherland-Hodgman algorithm is a polygon clipping algorithm that was developed in 1974. It works by clipping a polygon against a plane, one edge at a time. The algorithm uses the intersection points between the polygon edges and the plane to generate a new polygon that lies inside the ROI. The advantage of this algorithm is that it can clip concave polygons as well as convex polygons.

#### Weiler-Atherton Algorithm

The Weiler-Atherton algorithm is another polygon clipping algorithm that was developed in 1977. It works by using two linked lists to represent the polygon and the ROI. The algorithm traverses the linked lists and generates a new linked list that represents the portion of the polygon that lies inside the ROI. The advantage of this algorithm is that it can handle concave polygons as well as convex polygons.

In conclusion, 2-D clipping algorithms are essential in computer graphics because they help to remove the portions of an object that are outside the ROI. The Cohen-Sutherland, Liang-Barsky, Sutherland-Hodgman, and Weiler-Atherton algorithms are some of the most commonly used 2-D clipping algorithms. Each algorithm has its advantages and disadvantages, and the choice of algorithm depends on the specific requirements of the application.