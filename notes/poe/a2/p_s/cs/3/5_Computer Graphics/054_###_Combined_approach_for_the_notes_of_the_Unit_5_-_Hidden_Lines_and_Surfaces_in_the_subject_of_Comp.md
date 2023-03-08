 Here is the content in markdown format for the topic -

### Combined approach for the notes of the Unit 5 - Hidden Lines and Surfaces in the subject of Computer Graphics

1. Hidden Line Removal
- An object may be partially or fully hidden from view due to occlusion by other objects in the scene.
- These hidden lines need to be detected and removed to generate proper 3D graphics.
- Methods -
 -- Z-buffer algorithm - Stores depth info and suppresses pixels with z-values greater than the stored ones.
 -- Scan line algorithm - Processes polygons scan line by scan line and suppresses pixels of hidden portions.
- Advantages - Produces high quality images, handles intersecting surfaces well.
- Disadvantages - Complex and slow.

2. Hidden Surface Removal
- Need to determine which surfaces are visible and render only them.
- Methods -
 -- Depth sorting - Polygons are sorted based on depth and rendered in sorted order. Farther ones occlude closer ones.
 -- Back face culling - Back faces of polygons that face away from view are not rendered.
 -- Z-buffer - Same as hidden line removal.
- Advantages and disadvantages similar to hidden line removal.

3. Combined Approach
- As the name suggests, it combines hidden line and hidden surface removal techniques.
- It has following additional steps -
 -- First apply back face culling.
 -- Then sort remaining polygons in depth order.
 -- Finally process polygons in sorted order and apply Z-buffer algorithm to handle intersections.
- This approach proves to be optimal in most scenarios with good quality graphics and reasonable performance.

[Detailed diagrams and images can be added here to explain the concepts better.]