 Here is the content in markdown format for the topic ### Weiler and Atherton polygon clipping for the notes of the Unit 2 - Transformations in the subject of Computer Graphics:

### Weiler and Atherton Polygon Clipping

- Polygon clipping is a process of cutting a polygon by a clip window. The Weiler and Atherton algorithm is a technique to clip a convex polygon against a convex view window polygon.
- It works by finding intersections between edges of the subject polygon and clip window polygon and dividing the subject polygon into fragments. Each fragment is either retained if it is visible or discarded if not visible.
- The algorithm has two stages:
	1. Find intersections between edges of the two polygons. This gives dividing points on the edges of subject polygon.
	2. Use the dividing points to divide the subject polygon into fragments and test visibility of each fragment.
- Advantages:
	- Works for convex polygons.
	- Guaranteed to terminate.
	- Output is a set of visible polygon fragments.
- Disadvantages:
	- Complexity is proportional to the number of intersections between edges which can be O(n^2) where n is number of edges in polygons.
	- Only handles convex polygons. Non-convex polygons have to be triangulated first before using this algorithm.
- Applications: Viewing 3D models placed behind a viewing window, fast polygon rejection in computer graphics rendering.
- Here is a visual representation of the algorithm:

[A diagram showing the steps of Weiler Atherton polygon clipping algorithm]

- Overall, Weiler and Atherton polygon clipping is an efficient technique to clip a convex polygon against a convex viewing window polygon by finding edge intersections and dividing the polygon into visible fragments. It has applications in computer graphics for viewing 3D models through a window and fast polygon rejection in rendering.