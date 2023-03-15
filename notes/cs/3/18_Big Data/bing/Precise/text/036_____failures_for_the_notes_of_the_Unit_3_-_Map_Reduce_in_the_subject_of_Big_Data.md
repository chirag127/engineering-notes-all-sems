### Failures for the notes of the Unit 3 - Map Reduce in the subject of Big Data

1. **Task Failure**: A task may fail due to various reasons such as hardware failure, software bugs, or data corruption. In such cases, the MapReduce framework automatically reschedules the failed task on another machine.

2. **Worker Failure**: A worker machine may fail due to hardware or software issues. In such cases, the MapReduce framework detects the failure and reschedules all the tasks that were assigned to the failed worker on other machines.

3. **Master Failure**: The master node is responsible for coordinating the MapReduce job. If the master node fails, the entire MapReduce job fails. To mitigate this risk, the master node can be made fault-tolerant by using techniques such as replication or checkpointing.

4. **Data Loss**: Data loss can occur due to various reasons such as disk failure, network failure, or human error. To prevent data loss, the input and output data of a MapReduce job can be replicated across multiple machines.

5. **Network Failure**: A network failure can disrupt the communication between the master and worker nodes, leading to task failures or delays. To mitigate this risk, the network infrastructure can be made fault-tolerant by using techniques such as redundant network paths or network virtualization.

6. **Power Failure**: A power failure can cause the entire MapReduce cluster to shut down, leading to job failure. To prevent this, the cluster can be equipped with backup power supplies such as uninterruptible power supplies (UPS) or generators.

7. **Resource Contention**: Resource contention can occur when multiple MapReduce jobs are running concurrently on the same cluster, leading to degraded performance or job failure. To prevent this, the cluster resources can be managed using techniques such as resource allocation or job scheduling.