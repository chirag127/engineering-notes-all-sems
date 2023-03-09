 Here is the content in markdown format for the topic ### Cullers and Occluders for the notes of the Unit 4 - SOFTWARE TECHNOLOGIES in the subject of Augmented & Virtual Reality:

# Cullers and Occluders

Cullers and occluders are techniques used in computer graphics to optimize the rendering process and improve performance.

## Cullers

Cullers are algorithms that decide which objects are outside the view frustum (viewing volume) and discard them from the rendering pipeline. This reduces the number of objects that enter the graphics pipeline and speeds up the rendering process. Common culling techniques include:

- View frustum culling: Objects outside the view frustum are discarded.
- Backface culling: Polygons facing away from the camera are discarded.
- Occlusion culling: Objects occluded by other objects are discarded.

Advantages:

- Improves rendering performance by reducing objects processed.
- Saves computing resources.

Disadvantages:

- May discard objects that are partially visible.
- Additional overhead to perform culling algorithms.

## Occluders

Occluders are objects that obscure other objects from view. By detecting occluders, obscured objects can be culled from the rendering pipeline. This is known as occlusion culling. Common occlusion culling techniques include:

- Object-object occlusion: Detecting if one object occludes another.
- Portal-based occlusion: Using portals (openings) to determine visibility.

Advantages:

- Renders only visible objects, improving performance.
- More efficient than rendering all objects and using Z-buffering to handle occlusion.

Disadvantages:

- Difficult to implement.
- May require preprocessing.
- Additional overhead to perform occlusion detection.

[Detailed diagrams and examples can be added here to aid understanding]