 Here is the content in markdown format for the topic ### Windowing and Clipping for the notes of the Unit 2 - Transformations in the subject of Computer Graphics:

### Windowing

- Windowing refers to defining a rectangular region on the screen within which all the graphics output will be displayed.
- Any graphics lying outside the window region will be clipped.
- It is done to restrict the drawing region and reduce computation as only the graphics within the window needs to be processed.
- The window region is defined using 4 parameters - x(min), x(max), y(min), y(max).
- Example: If window is defined as x(min)=100, x(max)=200, y(min)=50, y(max)=150, then only the graphics lying within the rectangular region with (x,y) coordinates between (100,50) and (200,150) will be displayed.

Advantages:
- Reduces computation as only graphics within window needs processing.
- Makes effective use of display screen.

Disadvantages:
- Imposes restriction on drawing region. Graphics lying outside window gets clipped.

Applications:
- In computer graphics to restrict drawing region.
- In image processing to view a portion of an large image.

### Clipping

- Clipping refers to discarding the graphics lying outside a given region.
- The clipping region can be a window, a polygon or any arbitrary shape.
- Any graphics lying outside the clipping region is not displayed.
- It is done to hide the graphics lying outside the region of interest and reduce computation.
- The clipping region can be defined using lines, points or equations and graphics is checked if it lies inside the region or not. If not inside, it is clipped.

Advantages:
- Hides unwanted graphics and reduces computation.
- Makes effective use of display screen.

Disadvantages:
- Graphics lying outside clipping region gets discarded which may be required in some cases.

Applications:
- In computer graphics to hide unwanted parts of an image/scene.
- In image/video processing to extract a region of interest.