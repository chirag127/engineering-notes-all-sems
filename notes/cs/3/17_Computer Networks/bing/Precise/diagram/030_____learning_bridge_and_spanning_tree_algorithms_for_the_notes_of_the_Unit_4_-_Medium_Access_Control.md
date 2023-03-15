### Learning Bridge and Spanning Tree Algorithms

Unit 4 - Medium Access Control and Local Area Networks in the subject of Computer Networks

1. **Bridge algorithms** are used to connect multiple Local Area Networks (LANs) together to form a larger network.
2. A **bridge** is a device that connects two or more LANs and forwards data between them.
3. Bridges operate at the **data link layer** of the OSI model and use **MAC addresses** to determine where to forward data.
4. The **Spanning Tree Protocol (STP)** is a bridge algorithm used to prevent loops in a network.
5. STP creates a **loop-free logical topology** by blocking certain ports on bridges to prevent loops.
6. STP uses the **Bridge Protocol Data Unit (BPDU)** to exchange information between bridges and determine the best path for data to travel.
7. The **root bridge** is the bridge with the lowest bridge ID and is responsible for generating BPDUs.
8. The **designated bridge** is the bridge responsible for forwarding data on a particular LAN segment.
9. The **port cost** is used to determine the best path for data to travel and is based on the speed of the link.
10. STP can take up to **50 seconds** to converge and can cause temporary network outages.
