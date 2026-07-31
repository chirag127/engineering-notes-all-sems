### Security in Hadoop

- Security in Hadoop refers to the process of protecting the data and services in a Hadoop cluster from unauthorized access, modification, or disclosure.
- Security in Hadoop consists of four main aspects   :
  - Authentication: verifying the identity of the users and services that interact with Hadoop.
  - Authorization: enforcing access control policies on the data and services in Hadoop based on the roles and privileges of the users and services.
  - Auditing: recording and monitoring the activities and events that occur in Hadoop for accountability and compliance purposes.
  - Data confidentiality: encrypting the data in transit and at rest in Hadoop to prevent unauthorized access or leakage.
- Security in Hadoop can be achieved by using various mechanisms and tools, such as   :
  - Kerberos: a network authentication protocol that uses tickets to authenticate users and services in Hadoop. Kerberos is the default and recommended authentication mechanism for Hadoop.
  - HDFS file permissions: a file system level authorization mechanism that assigns read, write, and execute permissions to files and directories in HDFS based on the user and group ownership.
  - Service level authorization: a service level authorization mechanism that allows or denies access to Hadoop services based on the user and service identities and the configuration files.
  - Authentication for web consoles: a web level authentication mechanism that requires users to provide credentials to access the web interfaces of Hadoop services, such as the NameNode, the ResourceManager, and the JobHistoryServer.
  - Network encryption: a network level data confidentiality mechanism that encrypts the data in transit between Hadoop services and clients using SSL/TLS protocols.
  - Data encryption: a data level data confidentiality mechanism that encrypts the data at rest in HDFS using encryption zones and encryption keys.
  - Audit logging: a logging mechanism that records the events and actions that occur in Hadoop services and HDFS, such as the user and service identities, the time and date, the operation and outcome, and the source and destination IP addresses.
  - Sentry: a third-party tool that provides fine-grained authorization for data stored in HDFS and Hive by integrating with Hadoop and Kerberos.
  - Ranger: a third-party tool that provides centralized and comprehensive security administration for data and services in Hadoop by integrating with Hadoop, Kerberos, and other components.