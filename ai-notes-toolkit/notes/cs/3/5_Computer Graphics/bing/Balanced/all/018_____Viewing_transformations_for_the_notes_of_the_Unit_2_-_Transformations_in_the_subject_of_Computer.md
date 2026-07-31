# Viewing transformations for the notes of the Unit 2 - Transformations in the subject of Computer Graphics

- Viewing transformations are the processes of mapping the coordinates of points and lines that form the picture into appropriate coordinates on the display device .
- Viewing transformations are necessary to adjust the position, orientation, and size of the picture to fit the display device and the viewer's preferences .
- Viewing transformations can be divided into two types: projection and windowing .
- Projection is the process of transforming the three-dimensional world coordinates of the picture into two-dimensional eye coordinates that are relative to the viewer's position and direction.
- Projection can be either parallel or perspective, depending on whether the lines of projection are parallel or convergent.
- Parallel projection preserves the relative sizes and shapes of the objects, but does not create the illusion of depth.
- Perspective projection creates the illusion of depth by making the objects appear smaller and closer together as they are farther from the viewer, but distorts the relative sizes and shapes of the objects.
- Windowing is the process of selecting a rectangular region of the eye coordinates, called the window, that contains the part of the picture that the viewer wants to see .
- Windowing is also called clipping, as it removes the objects, lines, or line segments that are outside the window.
- Windowing is followed by mapping the window onto a subregion of the display device, called the viewport, that specifies the area on the screen where the picture will be displayed .
- Windowing can be either uniform or non-uniform, depending on whether the window and the viewport have the same or different aspect ratios.
- Uniform windowing preserves the relative proportions of the objects, but may leave some empty space on the screen or crop some parts of the picture.
- Non-uniform windowing fills the entire screen with the picture, but may stretch or compress the objects horizontally or vertically.
- Windowing can be done by using a simple scaling and translation formula that relates the window and the viewport coordinates.