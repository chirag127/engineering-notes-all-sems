# File System

A file system is a method and data structure that the operating system uses to control how data is stored and retrieved on a storage device. A file system organizes data into files and directories, and provides operations to create, delete, modify, and access them.

Some common types of file systems include:

- FAT (File Allocation Table): An older file system used by older versions of Windows and other operating systems. It uses a table to keep track of the clusters that store each file.
- NTFS (New Technology File System): A newer file system used by Windows. It supports larger file sizes, encryption, compression, security, and journaling.
- ext (Extended File System): A family of file systems used by Linux and other Unix-like systems. It supports large file sizes, symbolic links, journaling, and permissions.
- HFS (Hierarchical File System): A file system used by Mac OS. It uses a tree structure to organize files and directories, and supports metadata, aliases, and resource forks.
- APFS (Apple File System): A newer file system used by macOS, iOS, and other Apple devices. It supports encryption, snapshots, cloning, and space sharing.

A file system installed on an operating system consists of three layers:

- Physical file system: The lowest layer that interacts with the hardware and manages the allocation and deallocation of disk blocks.
- Virtual file system: The middle layer that provides a common interface for different types of file systems and handles file and directory operations.
- Logical file system: The highest layer that manages the metadata, such as file names, attributes, and permissions, and maps them to the physical file system.

Some of the functions of a file system are:

- Formatting: Preparing the storage device for use by the operating system by creating the file system structure and metadata.
- Naming: Assigning unique and human-readable names to files and directories, and enforcing naming rules and conventions.
- Storing: Writing data to the storage device in an efficient and reliable manner, and avoiding fragmentation and data loss.
- Retrieving: Reading data from the storage device and locating the desired file or directory based on the name or other criteria.
- Protecting: Securing the data from unauthorized access or modification by using encryption, passwords, permissions, and backups.
- Sharing: Allowing multiple users or processes to access the same file or directory concurrently, and resolving any conflicts or inconsistencies.