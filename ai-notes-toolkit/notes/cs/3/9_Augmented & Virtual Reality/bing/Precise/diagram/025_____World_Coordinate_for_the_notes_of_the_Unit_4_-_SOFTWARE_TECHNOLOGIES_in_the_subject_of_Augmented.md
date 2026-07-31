### World Coordinate

World Coordinate is a fundamental concept in Augmented and Virtual Reality. It is used to map the virtual world to the real space. Here are some key points to understand about World Coordinate:

1. In the case of Tango, where the augmentation happens on a camera feed, the position and orientation of the rendering device needs to be in real world coordinates. Only if the position and orientation of a Tango device is reported accurately, and fast enough, proper augmented reality is possible .

2. When writing games, data visualization apps, or virtual reality apps, the typical approach is to establish one absolute world coordinate system that all other coordinates can reliably map back to. In that environment, you can always find a stable transform that defines a relationship between any two objects in that world .

3. World Locking Tools (WLT) gets you the best of both worlds, stabilizing a single rigid coordinate system using an internal supply of spatial anchors spread throughout the virtual scene as the user moves around. WLT analyzes the coordinates of the camera and those spatial anchors every frame .

4. Augmented Reality (AR) depends on a dynamic, accurate 3D map: a digital twin that anchors location based content and experiences to real-world coordinates. With the WRLD AR mapping system, virtual and physical worlds merge together to transform how we tell stories, understand data, and interact with our environment .

5. We live in three-dimensional space, which means that three values are required to fully define the position of any point in the world. These three values can be expressed by the x, y, and z-axes of the coordinate frame .
