### Disconnected operations

- Disconnected operation is a mode of operation in mobile computing that allows users to execute applications during temporary failures in networks or when they explicitly decide to work off-line .
- Disconnected operation is a key enabling technology for mobile computing, as it enhances the availability and reliability of mobile applications in the face of network limitations such as short range, inability to operate underground and in steel-framed buildings, or line-of-sight constraints .
- Disconnected operation requires mechanisms to handle the following issues  :
  - Data management: how to ensure data consistency and coherence between the mobile device and the server when the connection is restored.
  - Application adaptation: how to modify the application behavior and interface to cope with the reduced functionality and resources in the disconnected mode.
  - Disconnection detection: how to determine when a disconnection occurs, either voluntarily or involuntarily, and how to notify the user and the application.
  - Reconnection: how to resume the normal operation of the application and the data synchronization when the connection is reestablished.

- Disconnected operation can be implemented using different techniques, such as  :
  - Data replication: copying a subset of the data from the server to the mobile device, and vice versa, to allow local access and modification in the disconnected mode. Data replication can be either eager (performed before the disconnection) or lazy (performed after the reconnection).
  - Mobile computation: transferring a part of the application logic from the server to the mobile device, and vice versa, to allow local execution and interaction in the disconnected mode. Mobile computation can be either proactive (performed before the disconnection) or reactive (performed after the reconnection).
  - Application-specific solutions: designing the application to tolerate or exploit the disconnection, such as by using caching, prefetching, hoarding, or logging techniques.

- Disconnected operation poses several challenges and trade-offs, such as  :
  - Data consistency: how to resolve conflicts and inconsistencies that may arise due to concurrent updates on the replicated data by the mobile device and the server.
  - Data coherence: how to ensure that the mobile device and the server have the same view of the data, and that the data is fresh and valid.
  - Data granularity: how to determine the optimal size and scope of the data to be replicated or transferred, considering the storage and bandwidth constraints of the mobile device and the network.
  - Data selection: how to select the most relevant and useful data to be replicated or transferred, considering the user preferences and the application requirements.
  - Data security: how to protect the data from unauthorized access, modification, or loss, both on the mobile device and during the data transmission.
  - Application performance: how to optimize the application response time, throughput, and quality of service, both in the connected and disconnected modes.
  - Application usability: how to provide a user-friendly and consistent interface for the application, both in the connected and disconnected modes.
  - Application portability: how to ensure that the application can run on different platforms and devices, and can adapt to different network conditions and user contexts.