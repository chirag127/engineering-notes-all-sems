### Warn model for the notes of the Unit 5 - Hidden Lines and Surfaces in the subject of Computer Graphics

- Hidden lines and surfaces are the lines and surfaces that are not visible from a particular viewpoint or projection direction.
- Hidden line and surface elimination is the process of determining which parts of a 3D object are visible or invisible to the observer at a specified point.
- Hidden line and surface elimination is also known as visible surface detection or visible surface elimination.
- Hidden line and surface elimination is important for realistic rendering of 3D scenes, as it avoids the clutter and confusion of overlapping and occluded objects.
- Hidden line and surface elimination can be classified into two categories: object-space methods and image-space methods.
- Object-space methods operate on the 3D geometry of the objects and compare them with the viewing parameters to decide which parts are visible or hidden.
- Image-space methods operate on the 2D projection of the objects and use depth information to determine which pixels are closer to the viewer or farther away.
- One of the object-space methods is the Warnock algorithm, proposed by John Warnock in 1969.
- The Warnock algorithm uses the concept of area coherence, which means that a region of the scene may have the same visibility properties for all the pixels in that region.
- The Warnock algorithm divides the viewing window into smaller subregions recursively until each subregion satisfies one of the following conditions:
  - The subregion is empty, i.e., it contains no objects.
  - The subregion is simple, i.e., it contains only one object or part of an object that is entirely visible or hidden.
  - The subregion is complex, i.e., it contains more than one object or part of an object that may overlap or occlude each other.
- The Warnock algorithm then fills the pixels in each subregion with the appropriate color and intensity of the visible object or the background.
- The Warnock algorithm is efficient and easy to implement, but it may not handle some cases of concave objects or objects with holes correctly.