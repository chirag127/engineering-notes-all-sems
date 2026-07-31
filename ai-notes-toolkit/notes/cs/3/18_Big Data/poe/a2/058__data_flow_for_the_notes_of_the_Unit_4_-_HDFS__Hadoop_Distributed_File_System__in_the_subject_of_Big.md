 Here is the content in Markdown format without any emoji or external links as per your instructions:

### Data flow for the notes of the Unit 4 - HDFS (Hadoop Distributed File System)

1. HDFS architecture:
- Master/Slave architecture
- NameNode (Master): Metadata (file structure/location)
- DataNodes (Slaves): Actual data blocks
- Blocks: Files split into blocks (default 128MB) and stored on DataNodes
- Replication: Multiple replicas of blocks stored on different DataNodes for fault tolerance (default 3)

2. HDFS read/write data flow:
- Write: Client → NameNode (get locations for blocks) → DataNodes (stores blocks)
- Read: Client → NameNode (get locations for blocks) → DataNodes (retrieves blocks) → Client

3. HDFS advantages:
- Fault tolerance: Block replication, easy to recover from DataNode failures
- Scalability: Can use a cluster of machines, store very large files (terabytes to petabytes)
- Low cost: Commodity hardware, open source
- Streaming access: Can start processing files before they finish writing

4. HDFS limitations:
- Not suitable for low latency data access
- Not suitable for a large number of small files (performance issue)
- Single writer, multiple reader model (no random writes)

I have written the content in points in a formal tone without any emojis or external links as you instructed. Please let me know if you would like me to modify or expand the content in any way.