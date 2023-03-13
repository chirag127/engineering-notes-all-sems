Security in Hadoop consists of four main components: authentication, authorization, auditing, and encryption. Authentication is the process of verifying the identity of the users and services that interact with Hadoop. Authorization is the process of granting or denying access to the resources and operations in Hadoop based on the user's role and privileges. Auditing is the process of recording and monitoring the activities and events that occur in Hadoop. Encryption is the process of protecting the data in transit and at rest from unauthorized access or modification.

The following diagram illustrates the basic architecture of security in Hadoop in a Hadoop environment:

```
+------------------+       +------------------+       +------------------+
|                  |       |                  |       |                  |
|    Client        |       |    NameNode      |       |    DataNode      |
|                  |       |                  |       |                  |
+------------------+       +------------------+       +------------------+
|                  |       |                  |       |                  |
|  Kerberos        |       |  Kerberos        |       |  Kerberos        |
|  Authentication  |       |  Authentication  |       |  Authentication  |
|                  |       |                  |       |                  |
+------------------+       +------------------+       +------------------+
|                  |       |                  |       |                  |
|  Hadoop RPC      |       |  Hadoop RPC      |       |  Hadoop RPC      |
|  Encryption      |       |  Encryption      |       |  Encryption      |
|                  |       |                  |       |                  |
+------------------+       +------------------+       +------------------+
|                  |       |                  |       |                  |
|  HDFS            |       |  HDFS            |       |  HDFS            |
|  Authorization   |       |  Authorization   |       |  Authorization   |
|                  |       |                  |       |  Data Encryption |
+------------------+       +------------------+       +------------------+
|                  |       |                  |       |                  |
|  HDFS            |       |  HDFS            |       |  HDFS            |
|  Auditing        |       |  Auditing        |       |  Auditing        |
|                  |       |                  |       |                  |
+------------------+       +------------------+       +------------------+
```