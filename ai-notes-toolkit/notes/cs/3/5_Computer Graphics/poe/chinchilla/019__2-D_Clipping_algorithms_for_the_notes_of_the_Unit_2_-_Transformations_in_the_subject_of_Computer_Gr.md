### 2-D Clipping algorithms for the notes of the Unit 2 - Transformations in the subject of Computer Graphics

2-D clipping algorithms are techniques used to remove unwanted parts of an image or object that are outside the viewing area. These algorithms are critical in computer graphics as they help in rendering images and objects more efficiently. This article will discuss the various 2-D clipping algorithms used in computer graphics.

#### 1. Cohen-Sutherland Algorithm

The Cohen-Sutherland algorithm is one of the most widely used 2-D clipping algorithms. It works by dividing the viewing area into nine regions, with each region assigned a specific binary code. The algorithm then tests each point in the object to determine whether it is inside or outside the viewing area. If a point is found to be outside, the algorithm uses the binary code to determine which part of the object should be clipped. The process continues until all points in the object have been tested.

#### 2. Liang-Barsky Algorithm

The Liang-Barsky algorithm is another popular 2-D clipping algorithm. It works by finding the intersections between the object and the viewing area. The algorithm then calculates the parameter values that define the points of intersection. This information is then used to clip the object.

#### 3. Sutherland-Hodgman Algorithm

The Sutherland-Hodgman algorithm works by clipping an object against each edge of the viewing area. The algorithm starts by clipping the object against the left edge of the viewing area. The resulting object is then clipped against the right edge, and the process continues until all edges of the viewing area have been used.

#### 4. Nicholl-Lee-Nicholl Algorithm

The Nicholl-Lee-Nicholl algorithm is a modification of the Sutherland-Hodgman algorithm. This algorithm is faster and more efficient than the Sutherland-Hodgman algorithm. It works by clipping an object against each edge of the viewing area. The algorithm uses a table to store the results of each clipping operation, which is then used to clip the object against the next edge.

In conclusion, 2-D clipping algorithms are essential in computer graphics as they help in rendering images and objects more efficiently. The Cohen-Sutherland, Liang-Barsky, Sutherland-Hodgman, and Nicholl-Lee-Nicholl algorithms are the most commonly used 2-D clipping algorithms. It is essential to understand these algorithms to create efficient and visually appealing computer graphics.