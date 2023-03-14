Big Data features – security, compliance, auditing and protection

Security, compliance, auditing and protection are important aspects of Big Data analytics that aim to keep the data sources secure, available, and reliable. According to , proper security entails more than just keeping the bad guys out; it also means backing up data and protecting data from corruption. The main challenges of Big Data security are:

- Access: Data can be easily protected, but only if you eliminate access to the data. The key is to control access, but even then, knowing the who, what, when, and where of data access is only a start.
- Availability: Controlling where the data are stored and how the data are distributed. The more control you have, the better you are positioned to protect the data.
- Performance: Higher levels of encryption, complex security methodologies, and additional security layers can all improve security. However, these security techniques all carry a processing burden that can severely affect performance.
- Liability: Accessible data carry with them liability, such as the sensitivity of the data, the legal requirements connected to the data, privacy issues, and intellectual property concerns.

The following diagram illustrates the basic architecture of a Big Data security system:

```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Data Source   +---->   Data Storage  +---->   Data Analysis |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Data Access   +<---+   Data Backup   +<---+   Data Recovery |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Data Audit    +<---+   Data Encrypt  +<---+   Data Decrypt  |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
```

The diagram shows the following components and processes:

- Data Source: The origin of the data, such as sensors, web logs, social media, etc.
- Data Storage: The place where the data are stored, such as databases, data warehouses, data lakes, etc.
- Data Analysis: The process of applying analytics tools and techniques to the data, such as machine learning, data mining, visualization, etc.
- Data Access: The process of granting or denying access to the data, based on user roles, permissions, policies, etc.
- Data Backup: The process of creating copies of the data, in case of data loss or corruption.
- Data Recovery: The process of restoring the data from the backup, in case of data loss or corruption.
- Data Audit: The process of monitoring and recording the data access, usage, and changes, for accountability and compliance purposes.
- Data Encrypt: The process of transforming the data into an unreadable form, using cryptographic algorithms and keys, to protect the data from unauthorized access or modification.
- Data Decrypt: The process of reversing the encryption, using the same or different keys, to restore the data to its original form.