Security of big data is the process of implementing safeguards to protect an enterprise’s big data from unauthorized access or breaches throughout the entirety of its lifecycle. Big data security involves various technologies and practices, such as encryption, centralized key management, user access control, data masking, auditing, and monitoring.

#### Security of Big Data

The following diagram illustrates the basic architecture of a big data security system using ASCII characters:

```
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|   Data Sources  |      |   Data Storage  |      |   Data Analysis |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  - Web          |      |  - Hadoop       |      |  - Spark        |
|  - IoT          |      |  - NoSQL        |      |  - R            |
|  - Social Media |      |  - Cloud        |      |  - Python       |
|  - Logs         |      |  - File System  |      |  - SQL          |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  - Encryption   |      |  - Encryption   |      |  - Encryption   |
|  - Authentication|     |  - Key Management|     |  - Access Control|
|  - Authorization |     |  - Access Control|     |  - Data Masking |
|  - Firewall      |     |  - Data Masking |     |  - Auditing     |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
```

The diagram shows the three main stages of big data lifecycle: data sources, data storage, and data analysis. Each stage has different types of data and technologies, and requires different security measures to protect the data from threats. Some of the common security measures are encryption, key management, access control, data masking, auditing, and firewall. Encryption protects the data from unauthorized access or modification, key management ensures the proper management and distribution of encryption keys, access control regulates who can access the data and what they can do with it, data masking obscures sensitive data from unauthorized users, auditing records the activities and events related to the data, and firewall blocks unwanted network traffic. These security measures can be applied at different levels of the big data system, such as the data itself, the network, the application, or the user.