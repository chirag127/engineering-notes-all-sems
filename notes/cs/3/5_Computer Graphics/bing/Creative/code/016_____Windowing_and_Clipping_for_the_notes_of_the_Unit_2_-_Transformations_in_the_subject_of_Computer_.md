### Windowing and Clipping

Windowing and clipping are two techniques used in computer graphics to display a part of a scene or an object on the screen. They are useful for zooming, panning, and culling operations.

- Windowing is the process of selecting and viewing a picture with different views. A window is a rectangular region of the world coordinate system that defines the area of interest or the portion of the picture that is to be displayed on the screen. A viewport is a rectangular region of the device coordinate system that specifies where the window is to be mapped on the screen. The mapping from the window to the viewport is called the viewing transformation. Windowing allows the user to change the scale and position of the picture on the screen by adjusting the window and the viewport parameters .

- Clipping is the process of dividing each element of the picture into its visible and invisible portions, and discarding the invisible portion. Clipping is necessary to remove the objects, lines, or line segments that are outside the viewing pane or the window, as they are irrelevant for the display. Clipping can be done in the world coordinate system before the viewing transformation, or in the device coordinate system after the viewing transformation. Clipping can be applied to different types of objects, such as points, lines, polygons, circles, curves, and text .

There are different algorithms for clipping different types of objects, such as Cohen-Sutherland algorithm, Liang-Barsky algorithm, Sutherland-Hodgman algorithm, Cyrus-Beck algorithm, etc. These algorithms usually assign a region code to each endpoint of the object, and use bitwise operations to determine whether the object is inside, outside, or partially inside the window. Then, they compute the intersection points of the object with the window boundaries, and keep only the visible portion of the object .

Here is an example of windowing and clipping a line segment:

![Windowing and clipping a line segment](https://www.tutorialspoint.com/computer_graphics/images/line_clipping.jpg)

The line segment AB has endpoints A(40, 40) and B(80, 80) in the world coordinate system. The window has coordinates (20, 20) and (60, 60). The viewport has coordinates (0, 0) and (100, 100) in the device coordinate system. The region codes for A and B are 1001 and 1010, respectively. The bitwise AND of the region codes is not zero, so the line segment is partially inside the window. The intersection points of the line segment with the window boundaries are C(20, 20) and D(60, 60). The visible portion of the line segment is CD, which is mapped to the viewport as CD'(0, 0) and D'(100, 100) in the device coordinate system.