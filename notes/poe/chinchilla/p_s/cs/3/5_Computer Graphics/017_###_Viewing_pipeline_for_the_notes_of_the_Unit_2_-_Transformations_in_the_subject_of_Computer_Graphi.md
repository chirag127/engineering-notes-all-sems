### Viewing pipeline for the notes of the Unit 2 - Transformations in the subject of Computer Graphics

The viewing pipeline is an essential part of computer graphics that enables us to view and interact with 3D objects. In this unit, we will learn about the different stages involved in the viewing pipeline.

1. Object Definition Stage: In this stage, we define the 3D objects that we want to view. The objects can be defined using mathematical equations or by creating a mesh of points, lines, and surfaces. 

2. Modeling Transformation Stage: Once the objects are defined, we can apply transformations to them to change their position, orientation, and size. The transformations can be translation, rotation, scaling, or a combination of these. 

3. Viewing Transformation Stage: After applying modeling transformations, we need to transform the objects into the viewing coordinate system. This transformation maps the objects from the model coordinate system to the world coordinate system. 

4. Projection Stage: In this stage, we project the 3D objects onto a 2D plane, which represents the computer screen. We can use different types of projections such as perspective or orthographic projection. 

5. Clipping Stage: Sometimes, the projected objects may extend beyond the boundaries of the viewing window. In such cases, we need to clip the objects to fit within the window. Clipping removes the parts of the objects that are not visible within the window. 

6. Scan Conversion Stage: After clipping, we convert the 3D objects into a 2D image by rasterizing them. Rasterization involves converting the objects into pixels that can be displayed on the computer screen. 

7. Display Stage: Finally, the 2D image is displayed on the computer screen for viewing and interaction.

Advantages of the Viewing Pipeline:
- Allows us to view and interact with 3D objects.
- Enables us to apply transformations to the objects, which can be useful in fields such as architecture, engineering, and medicine.
- Provides a way to project 3D objects onto a 2D plane, which is useful for creating computer graphics and animations.

Disadvantages of the Viewing Pipeline:
- Can be computationally intensive, especially for complex 3D objects.
- Requires knowledge of mathematical concepts such as linear algebra and geometry.

Example:
Suppose we want to create a 3D model of a building. We can define the building using mathematical equations or by creating a mesh of points, lines, and surfaces. We can then apply modeling transformations to change the position, orientation, and size of the building. After that, we can transform the building into the viewing coordinate system and project it onto a 2D plane. Finally, we can rasterize the building and display it on the computer screen.

Application:
The viewing pipeline has numerous applications in various fields such as:
- Architecture: Creating 3D models of buildings and visualizing them from different angles.
- Engineering: Designing and testing complex machinery and equipment.
- Medicine: Creating 3D models of organs and tissues for diagnosis and treatment planning.