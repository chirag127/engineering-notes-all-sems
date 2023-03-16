### World Coordinate System

- A world coordinate system is a reference frame that defines the position and orientation of virtual objects in relation to the real world in augmented and virtual reality applications    .
- A world coordinate system is usually based on a Cartesian coordinate system, which consists of three perpendicular axes: X, Y, and Z  .
- The origin of the world coordinate system is an arbitrary point that serves as the reference for all other points in the scene  .
- The orientation of the world coordinate system is defined by the direction of the axes, which can be either right-handed or left-handed  .
- A right-handed coordinate system is one where the positive X-axis points to the right, the positive Y-axis points up, and the positive Z-axis points out of the screen  .
- A left-handed coordinate system is one where the positive X-axis points to the right, the positive Y-axis points up, and the positive Z-axis points into the screen  .
- Different platforms and frameworks may use different conventions for the world coordinate system, so it is important to be aware of the differences and convert between them if necessary  .
- For example, Unity uses a left-handed coordinate system, while Microsoft Mixed Reality and Apple ARKit use a right-handed coordinate system   .
- A world coordinate system is not fixed, but can change over time as the device moves and tracks the environment  .
- To create a stable and consistent world coordinate system, augmented and virtual reality applications use various techniques, such as visual-inertial odometry, spatial anchors, world locking, and feature points  .
- Visual-inertial odometry is a process that combines information from the device's motion sensors and camera to estimate the device's position and orientation in the world.
- Spatial anchors are points in the real world that are tracked by the device and can be used to anchor virtual objects to specific locations   .
- World locking is a technique that stabilizes a single rigid coordinate system using an internal supply of spatial anchors spread throughout the virtual scene as the user moves around.
- Feature points are distinctive points in the real world that are detected by the device's camera and can be used to map the geometry and texture of the environment .