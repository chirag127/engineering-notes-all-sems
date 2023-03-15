

#### Hadoop 2.0 New Features - NameNode High Availability

- NameNode High Availability (HA) is a feature of Hadoop 2.0 that allows for a cluster to remain operational even if the NameNode fails.
- HA works by having two NameNodes running in the cluster, one active and the other passive. The passive NameNode will take over the active NameNode's duties if it fails.
- HA also provides an automated failover process to ensure that the cluster remains operational.
- HA requires a shared storage system, such as an NFS or SAN, to store the namespace and edit logs. This shared storage system allows the passive NameNode to access the same data as the active NameNode.
- HA also requires a separate machine to run a separate Zookeeper service. This service is used to coordinate the failover process.
- The main benefits of HA are increased reliability and availability. With HA enabled, a cluster can remain operational even if the NameNode fails. This can be especially beneficial for large clusters that require high uptime.
- Mnemonic: "NameNode HA: High Availability for NameNode".