# Disk characteristics

- Disk characteristics are the physical and logical properties of a disk that affect its performance and reliability.
- Some of the disk characteristics are:

  - **Capacity**: The amount of data that can be stored on a disk. It is measured in bytes (B), kilobytes (KB), megabytes (MB), gigabytes (GB), terabytes (TB), etc.
  - **Sector size**: The smallest unit of data that can be read or written on a disk. It is usually 512 bytes or 4096 bytes. A disk can have multiple sectors in a cluster, which is the smallest allocation unit of a file system.
  - **Cylinders, heads, and sectors (CHS)**: The geometric parameters of a disk that describe its physical layout. A disk is divided into cylinders, which are concentric tracks on the disk surface. Each cylinder has one or more heads, which are the read/write devices that access the data. Each track has one or more sectors, which are the subdivisions of the track that store the data.
  - **Logical block addressing (LBA)**: The logical scheme of addressing the sectors on a disk. It assigns a linear sequence of numbers to the sectors, starting from zero. LBA is independent of the physical geometry of the disk and simplifies the disk access.
  - **Master boot record (MBR)**: The first sector of a disk that contains the boot code and the partition table. The boot code is a small program that loads the operating system from the active partition. The partition table is a data structure that defines the boundaries and types of the partitions on the disk.
  - **GUID partition table (GPT)**: An alternative to MBR that supports larger disk sizes and more partitions. It uses a globally unique identifier (GUID) to identify each partition and stores a backup copy of the partition table at the end of the disk. It also has a protective MBR to ensure compatibility with legacy systems.
  - **File system**: The logical structure that organizes the data on a disk. It defines how the data is stored, accessed, and managed. Some of the common file systems are FAT, NTFS, EXT, HFS, etc.
  - **Slack space**: The unused space in a disk cluster that results from the difference between the cluster size and the file size. It can contain residual data from previous files or random data. It can be a source of forensic evidence or a hiding place for malicious data.
  - **Unallocated space**: The unused space on a disk that is not assigned to any partition or file system. It can also contain residual data from previous partitions or files. It can be recovered or overwritten by forensic tools or disk utilities.