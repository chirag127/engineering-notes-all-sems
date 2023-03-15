#### Security in Hadoop in Hadoop Environment

Hadoop is a framework for distributed processing of large-scale data. By default, Hadoop does not have any security and assumes that only trusted users have access to the cluster. However, this is not suitable for enterprise environments where data security is essential. Therefore, Hadoop can be configured in secure mode, which requires authentication, authorization, encryption, and audit for every user and service.

Authentication is the process of verifying the identity of a user or a service. Hadoop uses Kerberos, a network authentication protocol, to authenticate users and services in secure mode. Kerberos uses tickets to prove the identity of the parties involved in a communication.

Authorization is the process of granting or denying access to resources based on the identity and privileges of a user or a service. Hadoop uses Access Control Lists (ACLs) and permissions to control the access to files and directories in HDFS, the distributed file system of Hadoop. Hadoop also uses Apache Ranger, a framework for centralized security administration, to manage the access policies for HDFS, Hive, HBase, and other components.

Encryption is the process of transforming data into an unreadable form to prevent unauthorized access. Hadoop supports encryption at rest and encryption in transit. Encryption at rest means encrypting the data stored in HDFS using encryption zones and keys. Encryption in transit means encrypting the data transferred between Hadoop nodes using SSL/TLS protocols.

Audit is the process of recording and reviewing the activities and events that occur in the Hadoop cluster. Hadoop uses Apache Audit, a tool for auditing Hadoop services, to generate audit logs for HDFS, MapReduce, YARN, and other components. Audit logs can be used to monitor, analyze, and troubleshoot the security issues and incidents in the Hadoop cluster.

Depending on the cloud platform, Hadoop security can be handled by different components external to Hadoop. For example, on Google Cloud, authentication is handled by Cloud Identity and Access Management (IAM), authorization is handled by Cloud Data Access, encryption is handled by Cloud Key Management Service (KMS), and audit is handled by Cloud Audit Logs.

Hadoop security is crucial for the organizations that store their valuable data in the Hadoop environment. Hadoop security can protect the data from various forms of attacks, such as denial-of-service (DoS) attacks, which can cause a crash of data or flooding the target with traffic. Hadoop security can also ensure the data confidentiality, integrity, and availability in the Hadoop cluster.