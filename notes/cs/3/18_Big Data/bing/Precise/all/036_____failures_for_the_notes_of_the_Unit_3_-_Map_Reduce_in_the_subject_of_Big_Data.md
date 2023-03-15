# Unit 3 - Map Reduce: Failures

1. **Task Failure**: A task may fail due to various reasons such as bugs in the code or hardware issues. In such cases, the failed task is rescheduled on another node.

2. **Worker Failure**: A worker node may fail due to hardware or software issues. In such cases, all tasks running on the failed node are rescheduled on other nodes.

3. **Master Failure**: The master node may fail due to hardware or software issues. In such cases, a new master is elected from the remaining nodes and the system continues to operate.

4. **Data Loss**: Data loss may occur due to hardware failure or human error. In such cases, the lost data is recovered from replicas stored on other nodes.

5. **Network Partition**: A network partition may occur due to network issues, causing the system to split into multiple disjoint clusters. In such cases, the system continues to operate in each cluster independently until the network is restored.

6. **Straggler**: A straggler is a task that takes an unusually long time to complete due to various reasons such as hardware issues or data skew. In such cases, the straggler task is rescheduled on another node to speed up the overall execution.