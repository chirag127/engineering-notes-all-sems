 Here is the content in markdown format without any emojis or external links, written in points and in a formal tone:

### Hadoop file system interfaces for the notes of the Unit 4 - HDFS (Hadoop Distributed File System) in the subject of Big Data:

1.HDFS exposes a file system interface (or namespace) familiar to users. It presents a hierarchical file system view akin to a typical file system.

2.Files are broken into large blocks (typically 128 MB) and distributed across multiple DataNodes for reliability and performance.

3.The NameNode operates as a traditional file system namespace, maintaining file names, directories, and permissions.

4.The DataNodes operate as a distributed file system, storing blocks and serving read/write requests.

5.Clients interact directly with the NameNode for metadata operations (file creation, deletion, renaming) and indirectly with DataNodes for block read/write operations.

Does this meet your requirements? Let me know if you would like me to modify or expand the content in any way.