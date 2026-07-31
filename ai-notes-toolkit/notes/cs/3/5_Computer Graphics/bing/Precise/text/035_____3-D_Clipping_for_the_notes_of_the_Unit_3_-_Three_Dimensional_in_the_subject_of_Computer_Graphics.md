### 3-D Clipping

1. 3-D clipping is the process of removing objects or portions of objects that are outside the viewing volume in a three-dimensional graphics scene.
2. The viewing volume is defined by the view frustum, which is a truncated pyramid with the near and far clipping planes as the bases and the sides defined by the edges of the view window.
3. Objects or portions of objects that are outside the view frustum are not visible and can be removed from the scene to improve rendering performance.
4. Clipping can be performed in object space, where the objects are clipped against the view frustum before being transformed into screen space, or in screen space, where the objects are transformed into screen space and then clipped against the view window.
5. Common 3-D clipping algorithms include the Cohen-Sutherland algorithm, the Liang-Barsky algorithm, and the Sutherland-Hodgman algorithm.
6. Clipping can also be used to remove objects or portions of objects that are occluded by other objects in the scene, a process known as hidden surface removal.
7. 3-D clipping is an essential step in the rendering pipeline of a 3-D graphics system and is typically performed by the graphics hardware.