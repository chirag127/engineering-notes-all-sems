### File system for mobile computing

A file system is a software component that manages the storage and retrieval of data on a persistent device. A file system for mobile computing is a file system that supports the needs and challenges of mobile devices and users, such as:

- Mobility: Mobile devices can move across different networks and locations, and may experience disconnections, delays, or bandwidth limitations. A file system for mobile computing should be able to handle these changes and provide consistent and reliable access to data.
- Replication: Mobile devices may have limited storage capacity, battery life, or network connectivity. A file system for mobile computing should be able to replicate data across multiple devices or servers, and synchronize them when possible, to improve availability, performance, and fault tolerance.
- Security: Mobile devices may be exposed to various threats, such as theft, loss, or unauthorized access. A file system for mobile computing should be able to protect data from unauthorized or malicious users, and provide encryption, authentication, and access control mechanisms.
- Adaptability: Mobile devices may have different capabilities, preferences, or usage patterns. A file system for mobile computing should be able to adapt to the changing needs and conditions of mobile devices and users, and provide flexible and customizable services.

Some examples of file systems for mobile computing are:

- Coda: Coda is a distributed file system that originated from AFS2. It supports disconnected operation for mobile computing, which allows mobile clients to access and modify cached data when disconnected from the network, and reconcile the changes when reconnected. Coda also supports server replication, security, and network adaptation.
- VMDFS: VMDFS is a virtual memory based mobile distributed file system that employs dynamic frame-lock to reduce network latency and improve performance. It uses a thin-client/fat-server model, where the mobile client only maintains a small cache of frequently accessed data, and the server handles most of the file operations.
- GLOMAR: GLOMAR is a mobility enabled file system that provides adaptable consistency control mechanisms based on Web services and SOAP protocol. It allows mobile clients to specify their desired consistency level and update frequency, and the server to adjust the consistency service according to the network conditions.