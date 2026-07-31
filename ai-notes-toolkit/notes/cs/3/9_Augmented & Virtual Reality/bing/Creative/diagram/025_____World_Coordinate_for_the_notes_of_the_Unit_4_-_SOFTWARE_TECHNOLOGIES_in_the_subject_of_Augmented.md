### World Coordinate System

- A world coordinate system is a reference frame that defines the position and orientation of virtual objects in relation to the real world in augmented and virtual reality applications    .
- A world coordinate system is typically based on a Cartesian coordinate system, which uses three perpendicular axes (X, Y, and Z) to describe the location of any point in 3D space  .
- A world coordinate system can be either absolute or relative, depending on how it is established and maintained   .
  - An absolute world coordinate system is fixed and does not change with the movement of the user or the device. It is usually defined by a global reference frame, such as the Earth's magnetic north or the GPS coordinates  .
  - A relative world coordinate system is dynamic and adapts to the movement of the user or the device. It is usually defined by a local reference frame, such as the device's initial position and orientation or the features of the surrounding environment   .
- A world coordinate system is essential for creating a realistic and consistent alignment between the virtual and the real world, as well as enabling spatial interactions and persistence   .
- A world coordinate system can be established and updated by various methods, such as visual-inertial odometry, spatial anchors, world locking, or marker-based tracking  .
  - Visual-inertial odometry is a technique that combines information from the device's motion sensors and camera to estimate the device's position and orientation in the world.
  - Spatial anchors are points of interest that are identified and tracked by the device's camera and can be used to anchor virtual objects to the real world .
  - World locking is a technique that stabilizes a single rigid coordinate system using a set of spatial anchors spread throughout the virtual scene as the user moves around.
  - Marker-based tracking is a technique that uses predefined images or patterns as reference points to determine the device's position and orientation in the world.