### File systems for the notes of the Unit 2 - OPEN SOURCE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- A file system is a software component that manages the storage and retrieval of data on a persistent device, such as a hard disk, flash memory, or SD card.
- A file system organizes data into files and directories, and provides an interface to access and manipulate them.
- A file system also maintains metadata, such as file names, attributes, permissions, and timestamps.
- A file system can be integrated with an operating system, such as Windows, Linux, or macOS, or it can be embedded in a real-time operating system (RTOS), such as Azure RTOS, FreeRTOS, or RTEMS.
- An embedded file system is designed to have a small footprint, high performance, and reliability for resource-constrained devices that require file operations.
- An embedded file system can support different file formats, such as Microsoft FAT (FAT12, FAT16, FAT32, and exFAT), ISO 9660, or custom formats.
- An embedded file system can also provide features such as power fail-safety, wear leveling, encryption, compression, and transactional updates.
- Some examples of embedded file systems for open source RTOS are:

  - Reliance Edge: a transactional file system for FreeRTOS that is portable, open source, MISRA compliant, and fail safe. It protects critical data from corruption, even when power failures occur.
  - Azure RTOS FileX: a high-performance file system for Azure RTOS that is compatible with Microsoft FAT file formats. It is fully integrated with Azure RTOS ThreadX and is available for all supported processors .
  - RTEMS File Systems: a collection of file systems for RTEMS that include IMFS, Mini-IMFS, JFFS2, RFS, and DOSFS. IMFS and Mini-IMFS are memory-resident file systems that facilitate mounting other file systems and ensure a file system is available even if storage devices are not connected. JFFS2 and RFS are flash file systems that support wear leveling and compression. DOSFS is a FAT-compatible file system that supports long file names and Unicode.