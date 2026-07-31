# Viewing transformations for the notes of the Unit 2 - Transformations in the subject of Computer Graphics

- Viewing transformations are the processes of mapping coordinates of points and lines that form the picture into appropriate coordinates on the display device .
- Viewing transformations are necessary to remove objects, lines, or line segments that are outside the viewing pane or behind the viewer, and to adjust the size and position of the picture on the screen.
- Viewing transformations consist of two steps: projection and window-to-viewport mapping .
- Projection is the process of transforming 3D world coordinates into 2D eye coordinates, which are relative to the viewer's position and orientation.
- Projection can be either parallel or perspective, depending on whether the lines of projection are parallel or converge at a single point.
- Window-to-viewport mapping is the process of transforming 2D eye coordinates into 2D device coordinates, which are relative to the display device's resolution and origin.
- Window-to-viewport mapping involves defining a window, which is a rectangular region of interest in the eye coordinate system, and a viewport, which is a rectangular region of the display device where the window is mapped to.
- Window-to-viewport mapping can be done by applying scaling, translation, and clipping operations to the eye coordinates to fit them into the viewport.