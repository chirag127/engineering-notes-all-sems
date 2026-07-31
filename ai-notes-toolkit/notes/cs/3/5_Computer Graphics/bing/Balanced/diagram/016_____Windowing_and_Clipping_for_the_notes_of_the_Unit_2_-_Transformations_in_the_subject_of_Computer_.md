### Windowing and Clipping

- Windowing is the process of selecting and viewing a part of a picture with different views .
- Clipping is the process of dividing each element of the picture into its visible and invisible portions, and discarding the invisible portion .
- A window is a rectangular region of the picture that defines the area of interest or the view that is to be displayed .
- A viewport is a rectangular region of the display device where the window is mapped to be shown .

![Window and viewport](https://www.tutorialspoint.com/computer_graphics/images/window_to_viewport_transformation.jpg)

- The primary use of clipping is to remove objects, lines, or line segments that are outside the viewing pane or the window .
- Clipping can be applied to different types of objects, such as points, lines, polygons, and curves  .
- There are different algorithms for clipping different types of objects, such as Cohen-Sutherland algorithm, Liang-Barsky algorithm, Sutherland-Hodgman algorithm, etc .
- Clipping can be performed in different coordinate systems, such as world coordinates, normalized device coordinates, or screen coordinates  .
- Clipping can also be done in three dimensions, where the window is a rectangular prism and the viewport is a projection plane .

![3D clipping](https://www.tutorialspoint.com/computer_graphics/images/3d_clipping.jpg)

- Some applications of clipping are:
  - Extracting the desired part of a picture
  - Identifying the visible and invisible areas in a 3D object
  - Creating objects using solid modeling
  - Performing drawing operations
  - Pointing to an object