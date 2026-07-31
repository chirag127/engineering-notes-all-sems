 Here is the formal content on how HDFS stores data, written in Markdown format with points:

#### How does HDFS store data?

1. HDFS splits files into large blocks (typically 128MB):
- This enables fast processing of large files since the blocks can be processed in parallel.
- The blocks are replicated for fault tolerance.

2. The blocks are stored on DataNodes:
- The Namenode (master node) manages the file system namespace and regulates access to files.
- The Datanodes (slave nodes) store the blocks and serve read/write requests.

3. The blocks are replicated across multiple DataNodes:
- The replication factor (typically 3) can be configured.
- This provides fault tolerance in the event of DataNode failures. The replicas are stored on different racks/ Data Centers for high availability.

4. The blocks are stored on the local file system of DataNodes:
- The local file system of DataNodes is typically a normal file system like ext4.
- This decouples the file system for the block storage from the HDFS namespace.

5. HDFS provides high throughput access to large files:
- The large block size enables efficient streaming access of data.
- The replication and rack-aware placement enable high aggregate bandwidth.

Does this fulfill the required criteria? Let me know if you would like me to modify or expand the content in any way.