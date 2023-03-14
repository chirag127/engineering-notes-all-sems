#### Security in Hadoop in Hadoop Environment

- Security in Hadoop is a complex and evolving topic that involves various aspects such as authentication, authorization, encryption, and audit.
- By default, Hadoop does not have any security and assumes a level of trust among the users and services in the cluster. However, this assumption is not valid for most enterprise scenarios where data is sensitive and access needs to be controlled and monitored.
- Hadoop provides several mechanisms and tools to enhance the security of the cluster and the data, such as Kerberos, Knox, Ranger, and encryption.
- Kerberos is a network authentication protocol that uses tickets to verify the identity of users and services. Kerberos is the foundation of Hadoop security and is required to enable other security features such as authorization and encryption.
- Knox is a REST API gateway that provides a single access point for all REST interactions with the cluster. Knox supports authentication via LDAP and Active Directory, federated identity management, and auditing. Knox also simplifies the management of security policies and configurations across the cluster.
- Ranger is a centralized framework that enables administrators to define and enforce fine-grained access policies for different Hadoop components such as HDFS, YARN, Hive, HBase, etc. Ranger supports role-based and attribute-based access control, data masking, row and column level filtering, and auditing.
- Encryption is the process of transforming data into an unreadable form to protect its confidentiality and integrity. Hadoop supports encryption of data in transit and at rest using various techniques such as SSL/TLS, SASL, and transparent encryption.
- Audit is the process of recording and reviewing the activities and events that occur in the cluster and the data. Audit helps to ensure compliance, detect anomalies, and investigate incidents. Hadoop supports audit logging for different components and integrates with external tools such as Apache Flume and Apache Kafka for collecting and processing audit data.

Some mnemonics and learning tricks for security in Hadoop are:

- Remember the four pillars of Hadoop security: A-A-E-A (Authentication, Authorization, Encryption, Audit).
- Remember the three main tools for Hadoop security: K-K-R (Kerberos, Knox, Ranger).
- Remember the difference between encryption of data in transit and at rest: In transit means data is encrypted when it is moving across the network, while at rest means data is encrypted when it is stored on disk.
- Remember the difference between role-based and attribute-based access control: Role-based means access is granted based on the user's role or group, while attribute-based means access is granted based on the user's attributes or characteristics.