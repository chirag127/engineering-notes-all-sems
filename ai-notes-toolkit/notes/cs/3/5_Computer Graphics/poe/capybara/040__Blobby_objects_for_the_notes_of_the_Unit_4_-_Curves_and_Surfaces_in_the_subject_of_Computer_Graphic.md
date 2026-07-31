### Blobby objects for the notes of the Unit 4 - Curves and Surfaces in the subject of Computer Graphics.

Blobby objects are a type of implicit surface used in computer graphics. They are represented by a mathematical function that defines a surface in 3D space. Here are some key points to keep in mind when studying blobby objects:

- Blobby objects are also known as metaballs. They are often used to create organic shapes like clouds, smoke, and water droplets.

- The math behind blobby objects is based on the concept of a signed distance function. This function defines the distance between any point in 3D space and the surface of the blob. The sign of this distance indicates whether the point is inside or outside the blob.

- Blobby objects are created by combining multiple signed distance functions using a blending operator. The most commonly used blending operator is called the "sum of squares" operator, which adds the squares of the signed distance functions together.

- Blobby objects can be rendered using various techniques, such as ray marching or surface reconstruction. Ray marching involves casting rays from the camera through the scene and marching along the rays until they hit a surface. Surface reconstruction involves approximating the surface of the blob using a mesh of triangles or other polygons.

- Blobby objects have some advantages over traditional polygonal models. They are more flexible and can easily be animated or deformed. They also have a smooth, organic look that is difficult to achieve with polygons.

Overall, blobby objects are a powerful tool for creating complex, organic shapes in computer graphics. Understanding how they work and how to use them effectively can be a valuable skill for anyone working in the field.