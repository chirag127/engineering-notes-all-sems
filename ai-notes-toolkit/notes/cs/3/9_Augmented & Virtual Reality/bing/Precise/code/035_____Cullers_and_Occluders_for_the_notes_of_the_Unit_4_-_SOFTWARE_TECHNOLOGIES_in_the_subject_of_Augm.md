### Cullers and Occluders

Cullers and occluders are techniques used in computer graphics to improve the performance of rendering 3D scenes. These techniques are used to reduce the number of objects that need to be rendered, thus reducing the computational load on the graphics hardware.

#### Cullers
Cullers are algorithms that determine which objects in a 3D scene are visible to the camera and which are not. Objects that are not visible to the camera are culled, meaning they are not rendered. This can significantly reduce the number of objects that need to be rendered, thus improving performance.

There are several types of culling algorithms, including:
- **View frustum culling**: This algorithm checks if an object is inside the view frustum, which is the volume of space visible to the camera. Objects outside the view frustum are culled.
- **Backface culling**: This algorithm checks if the polygons of an object are facing away from the camera. If they are, the object is culled.
- **Occlusion culling**: This algorithm checks if an object is occluded by other objects in the scene. If it is, the object is culled.

#### Occluders
Occluders are objects in a 3D scene that can block the view of other objects. By identifying occluders, the occlusion culling algorithm can determine which objects are not visible to the camera and cull them.

Occluders can be static, such as walls and buildings, or dynamic, such as characters and vehicles. The effectiveness of occlusion culling depends on the complexity of the scene and the number and size of the occluders.

In summary, cullers and occluders are techniques used to improve the performance of rendering 3D scenes by reducing the number of objects that need to be rendered. These techniques are commonly used in real-time graphics applications, such as video games and virtual reality.