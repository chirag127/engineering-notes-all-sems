### Cullers and Occluders for the notes of the Unit 4 - SOFTWARE TECHNOLOGIES in the subject of Augmented & Virtual Reality

- Cullers and occluders are techniques to improve the performance and realism of augmented and virtual reality applications by reducing the number of objects or polygons that need to be rendered.
- Culling is the process of discarding objects or parts of objects that are not visible to the user, such as those that are outside the field of view, behind other objects, or too far away.
- Occlusion is the phenomenon of hiding virtual objects behind real objects or vice versa, depending on the perspective of the user. Occlusion culling is a specific type of culling that discards objects that are occluded by other objects.
- Culling and occlusion culling can reduce the rendering workload and improve the frame rate, as well as enhance the sense of immersion and realism by avoiding visual artifacts such as virtual objects floating in front of real objects or penetrating them.
- Some of the challenges and methods of culling and occlusion culling in augmented and virtual reality are:

  - Culling methods based on the view frustum, the bounding volume, or the level of detail can be applied to both augmented and virtual reality, but they may not be sufficient to handle complex and dynamic scenes with many objects and occluders.
  - Occlusion culling methods based on the depth buffer, the occlusion query, or the occlusion map can be applied to virtual reality, but they require the knowledge of the depth information of the scene, which may not be available or accurate in augmented reality.
  - Occlusion culling methods based on the environment mesh, the depth sensor, or the deep learning can be applied to augmented reality, but they have limitations such as the need for pre-built meshes, low-resolution depth maps, or high computational cost.
  - Occlusion culling methods should also consider the trade-off between the accuracy and the efficiency of the occlusion test, as well as the latency and the coherence of the occlusion result, to avoid flickering or popping artifacts.