# File System

A file system is a method and data structure that the operating system uses to control how data is stored and retrieved on a storage device. A file system is responsible for organizing files and directories, and keeping track of which areas of the media belong to which file and which are not being used.

A file system in an operating system decides the way the contents of its storage medium (secondary memory, etc) are stored and organized. Examples of filesystems are btrfs, xfs, zfs, ext series, ntfs, etc. These filesystems differ in aspects of implementation, use cases, etc.

A file system installed on an operating system consists of three layers:

- Physical file system: This layer handles the physical placement of data blocks on the storage device. It also manages the free space and the allocation of blocks to files. It provides an abstraction of the device as a collection of blocks.
- Virtual file system: This layer provides a common interface for different types of file systems. It allows the operating system to access files on different devices and file systems in a uniform way. It also handles the mounting and unmounting of file systems, and the caching of file data.
- Logical file system: This layer handles the logical organization of files and directories. It provides operations such as creating, deleting, renaming, moving, and searching files and directories. It also maintains the metadata of files, such as name, size, type, permissions, etc.

Some common types of file systems include:

- FAT (File Allocation Table): An older file system used by older versions of Windows and other operating systems. It uses a table to store the mapping of files to clusters of blocks. It has limitations on file size, file name length, and number of files.
- NTFS (New Technology File System): A newer file system used by modern versions of Windows. It supports larger file sizes, longer file names, encryption, compression, security, and journaling. It uses a master file table (MFT) to store the metadata of files and directories.
- ext (extended file system): A family of file systems used by Linux and other Unix-like operating systems. It supports journaling, symbolic links, hard links, permissions, and large file sizes. It uses inodes to store the metadata of files and directories, and superblocks to store the information of the file system.
- HFS (Hierarchical File System): A file system used by Mac OS and macOS. It supports long file names, metadata, and resource forks. It uses a catalog file to store the hierarchy of files and directories, and an extents file to store the allocation of blocks to files.