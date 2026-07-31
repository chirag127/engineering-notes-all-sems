# Cullers and Occluders for the notes of the Unit 4 - SOFTWARE TECHNOLOGIES in the subject of Augmented & Virtual Reality

- Cullers are algorithms or techniques that reduce the number of objects or polygons that need to be rendered in a virtual environment, by discarding those that are not visible to the viewer or are too far away to be noticeable.
- Occluders are objects or regions that block the view of other objects or regions in a virtual environment, creating a realistic effect of depth and occlusion.
- Cullers and occluders are important for improving the performance and realism of augmented and virtual reality applications, as they reduce the computational load and increase the immersion of the user .
- Some examples of cullers and occluders are:
  - View frustum culling: a technique that discards objects or polygons that are outside the viewing volume of the camera or the user's eye.
  - Back-face culling: a technique that discards polygons that are facing away from the camera or the user's eye, as they are not visible.
  - Occlusion culling: a technique that discards objects or polygons that are hidden behind other objects or regions, using occlusion queries, depth maps, or pre-computed visibility information  .
  - Level of detail (LOD): a technique that simplifies the geometry or texture of objects or polygons that are far away from the camera or the user's eye, reducing the number of vertices or pixels that need to be processed.
  - Image-based rendering (IBR): a technique that uses pre-rendered images or videos of the virtual environment, instead of rendering it in real time, reducing the computational load and increasing the realism.
- Some challenges and limitations of cullers and occluders are:
  - Occlusion culling is difficult to achieve in augmented reality, as the real world is dynamic and complex, and the depth information is often noisy or incomplete .
  - Cullers and occluders may introduce visual artifacts or errors, such as popping, flickering, or aliasing, if they are not implemented carefully or accurately.
  - Cullers and occluders may not be compatible with some rendering techniques or hardware, such as ray tracing, stereoscopic rendering, or head-mounted displays.
  - Cullers and occluders may require additional memory or storage space, or pre-processing time, to store or compute the visibility information or the simplified geometry or texture.