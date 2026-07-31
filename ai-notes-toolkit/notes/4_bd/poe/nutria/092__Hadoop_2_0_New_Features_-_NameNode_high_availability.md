

#### Hadoop 2.0 New Features - NameNode high Availability

1. Hadoop 2.0 introduced a feature called NameNode High Availability (NNHA). This feature provides a way to create a redundant NameNode in order to prevent NameNode failure.

2. NNHA uses an active-standby pair of NameNodes in the same cluster. The active NameNode handles all client operations, while the standby NameNode acts as a hot backup and continuously synchronizes with the active NameNode.

3. In the event of a failure, the standby NameNode can take over the active NameNode’s functions without any manual intervention.

4. NNHA also provides faster recovery from NameNode failures, as it eliminates the need for manual intervention.

5. NNHA also provides better scalability, as it allows for multiple NameNodes in the same cluster. This allows for more efficient resource utilization and better performance.

6. NNHA also provides better data security, as it allows for multiple copies of the same data to be stored on different NameNodes. This ensures that data is not lost in the event of a single NameNode failure.