### Viewing transformations for the notes of the Unit 2 - Transformations in the subject of Computer Graphics

- Viewing transformation is the mapping of coordinates of points and lines that form the picture into appropriate coordinates on the display device .
- Viewing transformation is part of the viewing pipeline, which consists of the following steps :
  - Define the world coordinate system (WCS), which is the right-handed Cartesian coordinate system where the picture is defined.
  - Define the viewing coordinate system (VCS), which is the coordinate system relative to the viewer's position and orientation.
  - Define the projection type, which can be parallel or perspective, and the projection plane, which is the plane where the picture is projected.
  - Define the window, which is the rectangular region of the projection plane that contains the picture of interest.
  - Define the viewport, which is the rectangular region of the display device where the window is mapped.
  - Apply the viewing transformation, which consists of the following substeps :
    - Translate the WCS origin to the VCS origin.
    - Rotate the WCS axes to align with the VCS axes.
    - Project the VCS coordinates onto the projection plane.
    - Scale the window to the size of the viewport.
    - Translate the window to the position of the viewport.
- Viewing transformation can be represented by a matrix that combines all the substeps into one operation.
- Viewing transformation can be applied to any geometric object, such as points, lines, polygons, curves, or surfaces.
- Viewing transformation can be affected by various factors, such as the viewer's position, orientation, distance, field of view, aspect ratio, and clipping planes.
- Viewing transformation can be implemented using various methods, such as homogeneous coordinates, normalized device coordinates, or clipping algorithms.