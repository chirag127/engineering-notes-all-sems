 Here is the content in markdown format with formal tone and without emojis:

### Hadoop 2.0 New Features - NameNode high availability

1. Previously, NameNode was a single point of failure in Hadoop 1.x cluster. If the NameNode goes down, the entire cluster becomes unavailable.
2. In Hadoop 2.x, NameNode high availability is achieved through a new architecture called Federation or NameNode HA.
3. In Federation, multiple independent NameNodes are configured to act as a namespace federation. Each NameNode manages a subset of the filesystem namespace and together provide a global namespace view.
4. In NameNode HA, two or more NameNodes are configured as a hot standby, so that if one NameNode fails, the other can take over, providing continuous service.
5. The key difference between Federation and NameNode HA is that in HA, the two NameNodes operate in an active-standby fashion on a single namespace whereas in Federation, multiple NameNodes operate on independent namespaces.
6. The key advantages of NameNode HA are:
- Improved reliability: The cluster continues to operate even if one NameNode fails.
- Improved performance: The second NameNode can take over a portion of the load even under normal operations, increasing overall throughput.
- Software upgrades: Rolling upgrades and maintenance of software become easier as one NameNode can be taken offline while the other is operational.

The points cover the key features and differences between Federation and NameNode HA. The content is written in a formal tone with points and without any emojis or external links as specified. Please let me know if you would like me to modify or expand the answer.