# Windowing and Clipping

Windowing and clipping are two techniques used in computer graphics to display a part of a scene or an object on the screen.

## Windowing

- Windowing is the process of selecting and viewing the picture with different views .
- A window is an area on the screen that defines the region of interest or the portion of the scene that is visible .
- A window can be rectangular or arbitrary in shape.
- A window can be moved, resized, or rotated to change the view of the scene.
- Windowing is useful for zooming in or out, panning, or focusing on a specific part of the scene.

## Clipping

- Clipping is the process of dividing each element of the picture into its visible and invisible portions, allowing the invisible portion to be discarded .
- Clipping is necessary to remove objects, lines, or line segments that are outside the window or the viewing volume .
- Clipping can be done in two dimensions or three dimensions .
- Clipping can be done using various algorithms, such as Cohen-Sutherland, Liang-Barsky, Sutherland-Hodgman, etc .
- Clipping is useful for saving memory, improving performance, and avoiding rendering artifacts .

## Window and Viewport

- A window and a viewport are two related concepts in computer graphics .
- A window is a region of interest in the world coordinate system, which defines what part of the scene is visible .
- A viewport is a region on the device coordinate system, which defines where and how the window is displayed on the screen .
- A window and a viewport can have different shapes and sizes, but they are usually rectangular.
- A window and a viewport can be related by a transformation that maps the coordinates of the window to the coordinates of the viewport.
- A window and a viewport can be used to achieve various effects, such as scaling, translation, rotation, or perspective.