# Cullers and Occluders

Cullers and occluders are techniques used in computer graphics to improve the performance of rendering 3D scenes. These techniques are used to reduce the number of objects that need to be rendered, thus reducing the computational load on the graphics hardware.

## Cullers

Culling is the process of removing objects from the rendering pipeline that are not visible to the camera. This can be done in several ways, including:

- **View frustum culling:** Objects outside the camera's view frustum (the volume of space visible to the camera) are not rendered.

- **Backface culling:** The backfaces of objects (the sides facing away from the camera) are not rendered.

- **Occlusion culling:** Objects that are occluded (hidden) by other objects in the scene are not rendered.

## Occluders

Occlusion culling is the process of determining which objects in a 3D scene are hidden from view by other objects. This is done by using occluders, which are objects that can potentially block the view of other objects. Occluders can be static (such as walls or terrain) or dynamic (such as moving objects).

Occlusion culling can be performed using several techniques, including:

- **Hardware occlusion queries:** The graphics hardware can be used to determine if an object is occluded by other objects in the scene.

- **Software occlusion culling:** Occlusion culling can be performed using software algorithms, such as the Hierarchical Z-Buffer or the Hierarchical Occlusion Map.

Cullers and occluders are important techniques for improving the performance of 3D rendering, especially in complex scenes with many objects. By reducing the number of objects that need to be rendered, these techniques can help to maintain high frame rates and smooth, responsive interaction in virtual and augmented reality applications.