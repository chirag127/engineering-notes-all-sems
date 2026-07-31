# Cohen Sutherland line clipping algorithm

The Cohen Sutherland line clipping algorithm is a computer graphics algorithm used for line clipping. It is used to determine the parts of a line that are inside or outside a clipping window. The algorithm divides a two-dimensional space into 9 regions and then efficiently determines the lines and portions of lines that are visible inside the region defined by the clipping window.

The algorithm works by using a 4-bit code called an outcode for each endpoint of the line. The outcode represents the location of the point relative to the clipping window. Each bit of the outcode represents a direction: top, bottom, left, and right. If the point is to the left of the clipping window, the left bit is set to 1. If the point is to the right of the clipping window, the right bit is set to 1. If the point is above the clipping window, the top bit is set to 1. If the point is below the clipping window, the bottom bit is set to 1.

The algorithm then compares the outcodes of the two endpoints of the line. If the logical AND of the outcodes is not 0, the line is completely outside the clipping window and can be discarded. If the logical AND of the outcodes is 0, the line may be partially or completely inside the clipping window. In this case, the algorithm finds the intersection of the line with the clipping window and clips the line accordingly.

The Cohen Sutherland line clipping algorithm is efficient and easy to implement. It is widely used in computer graphics for clipping lines against a rectangular clipping window.