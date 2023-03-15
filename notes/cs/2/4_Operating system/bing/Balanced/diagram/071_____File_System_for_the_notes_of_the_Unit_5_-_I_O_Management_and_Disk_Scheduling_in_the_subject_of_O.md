### File System

A file system is a method and data structure that the operating system uses to control how data is stored and retrieved on a storage device. A file system organizes files and directories, and keeps track of which areas of the media belong to which file and which are not being used. A file system also provides an interface for users and applications to access and manipulate files.

Some common types of file systems include:

- FAT (File Allocation Table): An older file system used by older versions of Windows and other operating systems. It uses a table to store the location and size of each file on the disk.
- NTFS (New Technology File System): A newer file system used by modern versions of Windows. It supports larger file sizes, encryption, compression, and security features. It uses a master file table to store metadata about each file and a bitmap to track free space.
- ext (Extended File System): A family of file systems used by Linux and other Unix-like operating systems. It supports journaling, which records changes to the file system before they are applied, to prevent data loss in case of a crash. It also supports symbolic links, permissions, and file attributes. The latest version is ext4.
- HFS (Hierarchical File System): A file system used by macOS and iOS. It supports journaling, encryption, compression, and metadata. It uses a catalog file to store information about files and directories, and an extents file to store the location of file fragments.

A file system installed on an operating system consists of three layers:

- Physical file system: This layer handles the physical layout of data on the disk, such as sectors, clusters, and partitions. It also performs low-level operations such as reading and writing data, and managing free space and bad sectors.
- Virtual file system: This layer provides a common interface for different types of file systems, such as FAT, NTFS, ext, etc. It also handles file system mounting, caching, buffering, and locking.
- Logical file system: This layer handles the logical structure of files and directories, such as file names, attributes, permissions, and links. It also provides system calls and commands for users and applications to access and manipulate files.