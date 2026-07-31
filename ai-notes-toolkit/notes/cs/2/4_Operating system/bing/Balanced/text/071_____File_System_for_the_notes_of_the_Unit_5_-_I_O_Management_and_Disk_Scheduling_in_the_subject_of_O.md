### File System

- A file system is a method and data structure that the operating system uses to control how data is stored and retrieved on a storage device.
- A file system is responsible for organizing files and directories, and keeping track of which areas of the media belong to which file and which are not being used.
- A file system also provides an interface for users and applications to access and manipulate files and directories.
- A file system can be classified into two types: disk-based and network-based.
  - Disk-based file systems are installed on local storage devices, such as hard disks, flash drives, CDs, etc. Examples of disk-based file systems are FAT, NTFS, ext, etc .
  - Network-based file systems are accessed over a network, such as the Internet, LAN, etc. Examples of network-based file systems are NFS, CIFS, WebDAV, etc.
- A file system installed on an operating system consists of three layers: physical, virtual, and logical.
  - Physical file system: This layer deals with the low-level details of how data is stored on the physical media, such as sectors, blocks, clusters, etc.
  - Virtual file system: This layer provides a common interface for different types of file systems to interact with the operating system kernel, such as system calls, file descriptors, etc.
  - Logical file system: This layer implements the high-level features of a file system, such as file and directory structures, metadata, permissions, etc.