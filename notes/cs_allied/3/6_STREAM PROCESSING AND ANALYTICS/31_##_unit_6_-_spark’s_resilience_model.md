## Unit 6 - Spark’s Resilience Model

Spark's Resilience Model is the mechanism by which Spark ensures that the processing of data streams is resilient to failures and continues to operate even in the presence of node failures and network delays. 

The key features of Spark's Resilience Model include:
1. Replication: Spark uses data replication to ensure that multiple copies of data are maintained, so that if a node fails, the data can be recovered from another node.

2. Lineage: Spark uses lineage information to track the transformations applied to data, so that if a node fails, the data can be recovered from the lineage information.

3. Checkpointing: Spark uses checkpointing to periodically save the state of the processing pipeline to disk, so that if a node fails, the state can be recovered from the checkpoint.

4. Task retries: Spark uses task retries to automatically retry failed tasks, so that if a task fails, it can be automatically retried on another node.

5. Failure recovery: Spark provides a mechanism for recovering from failures, so that if a node fails, the processing can continue on another node.

In summary, Spark's Resilience Model is the mechanism by which Spark ensures that the processing of data streams is resilient to failures and continues to operate even in the presence of node failures and network delays. The model includes features such as data replication, lineage, checkpointing, task retries, and failure recovery.
