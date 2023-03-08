 Here is the content in markdown format for the topic ### 3-D Transformation for the notes of the Unit 3 - Three Dimensional in the subject of Computer Graphics:

### 3-D Transformation

3-D transformation involves transforming 3-D objects from one coordinate system to another. It is done using 4x4 transformation matrices. The 4x4 transformation matrix is multiplied with the 4x1 vector representing the coordinates of a vertex.

The different types of 3-D transformations are:

1. Translation: It moves an object from one position to another. The transformation matrix contains the translation values tx, ty and tz in the 4th column.
2. Rotation: It rotates an object around a fixed point called the pivot point. The transformation matrix contains rotation values in the 1st 3 rows and columns. Rotation can be around X-axis, Y-axis or Z-axis or a combination of two or three axes.
3. Scaling: It increases or decreases the size of an object. The transformation matrix contains the scale factors sx, sy and sz in the diagonal. Uniform scaling keeps the aspect ratio same while non-uniform scaling changes the aspect ratio.
4. View transformation: It is used to change the view or perspective of the scene. It is done using a camera or viewport. The scene can be rotated, translated or scaled in the view transformation.

Advantages:
- 3-D transformation provides flexibility to modify 3-D objects.
- Multiple transformations can be applied by multiplying the transformation matrices.
- Hierarchical modeling is possible by applying transformations locally and globally.

Disadvantages:
- Increased processing required which can slow down applications.
- Accumulation of errors due to multiple matrix multiplications.

Applications:
- 3-D modeling and animation
- Computer graphics
- Video games
- CAD software

[Include detailed diagrams and codes if required]