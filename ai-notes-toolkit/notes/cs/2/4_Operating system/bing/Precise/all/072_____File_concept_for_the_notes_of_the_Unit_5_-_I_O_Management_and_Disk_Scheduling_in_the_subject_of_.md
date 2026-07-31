# File Concept

A file is a named collection of related information that is recorded on secondary storage. It is a sequence of bits, bytes, lines, or records whose meaning is defined by the files creator and user.

## File Attributes
- **Name**: The symbolic file name is the only information kept in human-readable form.
- **Identifier**: This unique tag, usually a number, identifies the file within the file system; it is the non-human-readable name for the file.
- **Type**: This information is needed for systems that support different types.
- **Location**: This information is a pointer to a device and to the location of the file on that device.
- **Size**: The current size of the file (in bytes, words, or blocks) and possibly the maximum allowed size are included in this attribute.
- **Protection**: Access-control information determines who can do reading, writing, executing, and so on.
- **Time, date, and user identification**: This information may be kept for creation, last modification, and last use. These data can be useful for protection, security, and usage monitoring.

## File Operations
- **Creating a file**: Two steps are necessary to create a file. First, space in the file system must be found for the file. Second, an entry for the new file must be made in the directory.
- **Writing a file**: To write a file, we make a system call specifying both the name of the file and the information to be written to the file.
- **Reading a file**: To read from a file, we use a system call that specifies the name of the file and where in memory the next block of the file should be put.
- **Deleting a file**: To delete a file, we search the directory for the named file. Having found the associated directory entry, we release all file space, so that it can be reused by other files, and erase the directory entry.
- **Truncating a file**: The user may want to erase the contents of a file but keep its attributes. Rather than forcing the user to delete the file and then recreate it, this function allows all attributes to remain unchanged—except for file length—but lets the file be reset to length zero and its file space released.

## File Types
- **Regular files**: Regular files contain user information. These files may be ASCII files or binary files.
- **Directories**: Directories are system files for maintaining the structure of the file system.
- **Character special files**: Character special files are related to input/output and used to model serial I/O devices, such as terminals, printers, and networks.
- **Block special files**: Block special files are used to model disks.

## File Access Methods
- **Sequential access**: A sequential-access file is read from the beginning, and records are accessed one after the other in some sequence until the desired record is reached.
- **Direct access**: A direct-access file allows arbitrary blocks to be read or written. Thus, you can read block 14, then read block 53, and then write block 7.
- **Indexed sequential access**: An indexed sequential-access file is basically a sequential-access file with an index that allows software to locate individual records.
