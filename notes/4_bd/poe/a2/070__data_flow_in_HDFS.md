 Here is the formal content on data flow in HDFS in markdown format:

#### Data Flow in HDFS

1. Client writes data to HDFS
- Client contacts NameNode to get permission to write data and get block locations
- NameNode returns block locations (DataNodes) to Client
- Client writes data directly to DataNodes (blocks)

2. DataNodes store data blocks
- Data is replicated across multiple DataNodes for fault tolerance (typically 3 replicas)
- DataNodes regularly report to NameNode with block report
- NameNode keeps track of locations of blocks and replication factor

3. Reading data from HDFS
- Client contacts NameNode to get list of locations of blocks of file
- Client reads data directly from DataNodes that hold the blocks
- If a block is unavailable (e.g. node failure), client can read from a replica

[No emojis or external links included as requested]

The content is written in points and in a formal style for learning and exam preparation as requested. Please let me know if you would like me to modify or expand the content in any way.