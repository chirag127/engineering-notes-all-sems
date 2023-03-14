### Basics of Virtualization for the notes of the Unit 2 - Cloud Enabling Technologies Service Oriented Architecture in the subject of Cloud Computing

- Virtualization is the technology that allows creating virtual representations of physical resources, such as servers, storage, networks, and devices.
- Virtualization enables more efficient utilization of physical hardware resources and reduces the cost and complexity of managing IT infrastructure.
- Virtualization is the foundation of cloud computing, which provides on-demand access to computing resources over the internet.
- There are different types of virtualization, such as server virtualization, network virtualization, storage virtualization, desktop virtualization, and application virtualization.
- Server virtualization is the process of creating multiple virtual machines (VMs) on a single physical server, each running its own operating system (OS) and applications. This allows for better resource allocation, isolation, scalability, and security.
- Network virtualization is the process of creating virtual networks that can span across multiple physical networks, devices, and locations. This allows for better network performance, flexibility, and security.
- Storage virtualization is the process of creating virtual storage devices that can pool and abstract the physical storage resources, such as disks, tapes, and arrays. This allows for better storage management, availability, and backup.
- Desktop virtualization is the process of creating virtual desktops that can run on a remote server and be accessed by users from any device. This allows for better desktop management, mobility, and security.
- Application virtualization is the process of creating virtual applications that can run on a remote server and be accessed by users from any device. This allows for better application management, compatibility, and performance.

- A simple mnemonic to remember the types of virtualization is **SNSDA** (Server, Network, Storage, Desktop, Application).
- A simple diagram to illustrate the concept of virtualization is:

```
+-----------------+    +-----------------+    +-----------------+
| Physical Server |    | Physical Server |    | Physical Server |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
| +-----+ +-----+ |    | +-----+ +-----+ |    | +-----+ +-----+ |
| | VM1 | | VM2 | |    | | VM3 | | VM4 | |    | | VM5 | | VM6 | |
| +-----+ +-----+ |    | +-----+ +-----+ |    | +-----+ +-----+ |
| | OS1 | | OS2 | |    | | OS3 | | OS4 | |    | | OS5 | | OS6 | |
| +-----+ +-----+ |    | +-----+ +-----+ |    | +-----+ +-----+ |
| | A1  | | A2  | |    | | A3  | | A4  | |    | | A5  | | A6  | |
| +-----+ +-----+ |    | +-----+ +-----+ |    | +-----+ +-----+ |
+-----------------+    +-----------------+    +-----------------+
```

- Where VM stands for virtual machine, OS stands for operating system, and A stands for application.