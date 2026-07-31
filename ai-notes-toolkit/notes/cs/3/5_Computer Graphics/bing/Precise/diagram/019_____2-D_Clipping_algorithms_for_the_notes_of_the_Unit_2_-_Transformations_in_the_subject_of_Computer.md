### 2-D Clipping Algorithms

2-D clipping algorithms are used in computer graphics to remove the portions of an object that are outside the viewing area. This is necessary to improve the efficiency of the rendering process and to prevent the display of unwanted or irrelevant information. Some common 2-D clipping algorithms include:

1. **Cohen-Sutherland Algorithm**: This algorithm divides the viewing area into nine regions and uses a set of rules to determine which lines or portions of lines are inside, outside, or partially inside the viewing area. The algorithm then clips the lines accordingly.

2. **Liang-Barsky Algorithm**: This algorithm is similar to the Cohen-Sutherland algorithm, but uses a different set of rules to determine which lines or portions of lines are inside, outside, or partially inside the viewing area. The algorithm then clips the lines accordingly.

3. **Sutherland-Hodgman Algorithm**: This algorithm is used to clip polygons. It works by clipping the polygon against each edge of the viewing area in turn. The resulting clipped polygon is then used as the input for the next edge clipping operation.

4. **Weiler-Atherton Algorithm**: This algorithm is also used to clip polygons. It works by dividing the polygon into a set of sub-polygons, each of which is then clipped against the viewing area. The resulting clipped sub-polygons are then combined to form the final clipped polygon.

These are some of the most commonly used 2-D clipping algorithms in computer graphics. Each algorithm has its own strengths and weaknesses, and the choice of algorithm will depend on the specific requirements of the application.