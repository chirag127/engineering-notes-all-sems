### Cullers and Occluders

Cullers and occluders are techniques used in computer graphics to improve the performance of rendering 3D scenes. These techniques are used to reduce the number of objects that need to be rendered, thus reducing the computational load on the graphics hardware.

- **Culling** is the process of removing objects from the rendering pipeline that are not visible to the camera. This can be done using various techniques such as view frustum culling, backface culling, and occlusion culling.

- **View frustum culling** involves removing objects that are outside the camera's view frustum, which is the volume of space that is visible to the camera.

- **Backface culling** involves removing the faces of objects that are facing away from the camera, as they are not visible to the viewer.

- **Occlusion culling** involves removing objects that are hidden behind other objects in the scene. This can be done using various techniques such as depth buffer occlusion culling, hierarchical z-buffer occlusion culling, and portal culling.

- **Occluders** are objects in the scene that can be used to hide other objects. For example, a wall can be used as an occluder to hide objects that are behind it. Occluders can be used to improve the performance of occlusion culling by reducing the number of objects that need to be tested for visibility.

In summary, cullers and occluders are techniques used to improve the performance of rendering 3D scenes by reducing the number of objects that need to be rendered. These techniques can be used in the development of augmented and virtual reality applications to improve the performance and user experience.