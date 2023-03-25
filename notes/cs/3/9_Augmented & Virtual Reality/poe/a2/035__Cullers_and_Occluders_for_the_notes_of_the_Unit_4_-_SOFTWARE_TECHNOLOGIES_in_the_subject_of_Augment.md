 Here is the content in markdown format without any emojis or external links and in formal tone:

### Cullers and Occluders for the notes of the Unit 4 - SOFTWARE TECHNOLOGIES in the subject of Augmented & Virtual Reality

1. Culling: It is the process of removing objects/models that are not visible to the user. This is done to optimize the performance of the application. Some common culling techniques are:
- Frustum Culling: Objects/models that are completely outside the view frustum are removed. View frustum is the pyramid shaped region in the scene that is visible to the user.
- Occlusion Culling: Objects/models that are occluded or hidden behind other objects from the user's point of view are removed.
- Layer Culling: The scene is divided into multiple layers and only layers that are visible to the user are rendered. Remaining layers are culled.

2. Occlusion: It refers to hiding of objects in a 3D scene with respect to a specified viewpoint. Effective occlusion techniques can improve the performance and experience of AR/VR applications. Some common occlusion techniques are:
-Occlusion Queries: The graphics API is queried to determine if an object's pixels are occluded or not. If occluded, the object need not be rendered.
-Z-buffer: The depth information is stored in a buffer which is then used to determine if an object is occluded or not.
-Visibility Maps: Pre-computed visibility information of the scene is stored which is then used to cull occluded objects.

The content summarizes two important concepts - culling and occlusion related to optimizing the performance of AR/VR applications. The techniques for culling and occlusion have been outlined with relevant examples. The tone is formal and no emojis or external links have been used. Please let me know if you would like me to elaborate on any of the points or modify the content in any way.