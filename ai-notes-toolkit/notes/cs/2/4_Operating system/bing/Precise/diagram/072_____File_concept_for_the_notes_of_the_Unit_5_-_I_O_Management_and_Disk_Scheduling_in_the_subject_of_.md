### File Concept

A file is a named collection of related information that is recorded on secondary storage. It is a sequence of bits, bytes, lines, or records whose meaning is defined by the files creator and user.

- **File Attributes**: A file has certain attributes, which vary from one operating system to another, but typically consist of the following:
  - Name: The symbolic file name is the only information kept in human-readable form.
  - Identifier: This unique tag, usually a number, identifies the file within the file system.
  - Type: This information is needed for systems that support different types of files.
  - Location: This information is a pointer to a device and to the location of the file on that device.
  - Size: The current size of the file (in bytes, words, or blocks) and possibly the maximum allowed size are included in this attribute.
  - Protection: Access-control information determines who can do reading, writing, executing, and so on.
  - Time, date, and user identification: This information may be kept for creation, last modification, and last use.

- **File Operations**: A file is an abstract data type. To define a file properly, we need to consider the operations that can be performed on files. The operating system can provide system calls to create, write, read, reposition, delete, and truncate files.

- **File Types**: There are many different types of files. These types include:
  - Regular files: These files contain user information.
  - Directories: These files are system files for maintaining the structure of the file system.
  - Character special files: These files are related to input/output and used to model serial I/O devices, such as terminals, printers, and networks.
  - Block special files: These files are used to model disks.

- **File Access Methods**: Files store information. When it is used, this information must be accessed and read into computer memory. The information in the file can be accessed in several ways. Some systems provide only one access method for files. Other systems, such as those of IBM, support many access methods, and choosing the right one for a particular application is a major design problem. The access methods are:
  - Sequential access
  - Direct access
  - Indexed sequential access

- **File System Structure**: The file system resides on secondary storage, which is organized into logical units called blocks. These blocks are the smallest unit of transfer between the disk and the memory. The file system is responsible for organizing these blocks into files and directories and keeping track of which blocks are used and which are free. It also maintains the file attributes and the directory structure.

- **File System Mounting**: A file system must be mounted before it can be available to processes on the system. Mounting is the process by which the operating system makes a file system available for use and associates it with a particular point in the system's directory structure, known as a mount point.

- **File Sharing**: File sharing is the practice of making files available to other users or processes. This can be done in several ways, including through a network file system, through a distributed file system, or through a file transfer protocol.

- **Protection**: File protection is the process of ensuring that only authorized users have access to files and that they can only perform authorized operations on those files. This can be done through access control lists, permissions, and other mechanisms.
