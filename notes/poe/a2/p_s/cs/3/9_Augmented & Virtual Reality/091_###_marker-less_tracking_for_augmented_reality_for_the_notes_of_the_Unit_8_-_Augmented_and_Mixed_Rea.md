 Here is the content in markdown format for the topic ### marker-less tracking for augmented reality for the notes of the Unit 8 - Augmented and Mixed Reality in the subject of Augmented & Virtual Reality:

Marker-less tracking for augmented reality refers to the methods of tracking the position and orientation of a device like mobile or head-mounted display (HMD) in the real-world without the use of any physical markers in the environment. This enables the overlay of augmented reality objects on the real-world scenes viewed through the device without any limitations due to the use of markers. Some of the popular marker-less tracking methods are:

1. Simultaneous Localization and Mapping (SLAM): SLAM algorithms localize the device in an unknown environment while building and updating a map of the environment. Visual features like edges, corners, planes, etc are used to find correspondence between frames and compute the pose. Examples are SLAM based on visual features, plane-based SLAM, etc.
Advantages: Does not require any preparation of the environment. Can handle dynamic environments.
Disadvantages: Computationally expensive. Drifts over time leading to inaccurate tracking.
Applications: AR navigation, AR in unprepared environments, etc.

2. Visual Inertial Odometry (VIO): Combines inputs from cameras and inertial measurement units (IMUs) to determine the pose. Visual features are tracked across frames to determine relative motion and IMU data provides rotational velocities and accelerations to reduce drift.
Advantages: Provides robust and accurate tracking. Handles dynamic environments and fast motions well.
Disadvantages: Additional hardware required leads to increased cost and power consumption.
Applications: AR/VR headsets, autonomous vehicles, drones, etc.

[Further details and diagrams can be added here as required]

The key advantages of marker-less tracking are that it enables AR in unprepared, unconstrained environments without any limitations due to markers. However, marker-less tracking is computationally more complex and can suffer from inaccuracies and drift over time. Hybrid approaches combining multiple marker-less methods or using markers along with marker-less tracking can help achieve robust and accurate tracking for AR.