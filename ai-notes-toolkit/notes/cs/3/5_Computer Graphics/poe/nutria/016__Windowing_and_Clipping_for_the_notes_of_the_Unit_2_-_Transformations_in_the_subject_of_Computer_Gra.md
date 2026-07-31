
### Windowing and Clipping for the notes of the Unit 2 - Transformations in the subject of Computer Graphics

* Windowing is the process of selecting a portion of the display area to be displayed. It is used to display a particular portion of the scene on the screen.
* Clipping is the process of removing the objects that lie outside the viewing area. It is used to limit the objects to the viewing area.
* Windowing and Clipping are important operations in Computer Graphics as they help to reduce the time taken to render the scene.
* Windowing and Clipping can be performed in two ways:
    * Viewport Transformation: This method involves transforming the coordinates of the objects in the scene to the coordinates of the viewport.
    * Cohen-Sutherland Algorithm: This algorithm uses a four-bit code to identify whether an object is inside or outside the viewing area. If it is outside, then it is clipped.