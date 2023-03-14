## Unit 3 - Cloud Architecture, Services And Storage

Cloud architecture is the way technology components combine to build a cloud, in which resources are pooled through virtualization technology and shared across a network. Cloud storage is a service that allows users to store and access data on remote servers over the internet. Cloud storage is based on virtualized infrastructure and is like cloud computing in terms of accessible interfaces, scalability and metered resources.

The following diagram illustrates the basic architecture of a cloud storage service:

```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Front-end     |    |   Back-end      |    |   Cloud         |
|   Platform      |    |   Platform      |    |   Storage       |
|                 |    |                 |    |   Service       |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Client or     |    |   Servers and   |    |   Data stored   |
|   device used   |    |   storage       |    |   on remote     |
|   to access     |    |   devices       |    |   servers       |
|   the cloud     |    |                 |    |                 |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Web browser,  |    |   Virtual       |    |   Object,       |
|   mobile app,   |    |   machines,     |    |   file, block,  |
|   desktop app,  |    |   containers,   |    |   or database   |
|   etc.          |    |   etc.          |    |   storage       |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Application   |    |   Application   |    |   Application   |
|   programming   |    |   programming   |    |   programming   |
|   interface     |    |   interface     |    |   interface     |
|   (API)         |    |   (API)         |    |   (API)         |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   REST, SOAP,   |    |   REST, SOAP,   |    |   REST, SOAP,   |
|   etc.          |    |   etc.          |    |   etc.          |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Network       |    |   Network       |    |   Network       |
|   connection    |    |   connection    |    |   connection    |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Internet      |    |   Internet      |    |   Internet      |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
```

Some examples of cloud storage services are:

- Azure Blob Storage: A massively scalable object store for text and binary data. Also includes support for big data analytics through Azure Data Lake Storage Gen2.
- Azure Files: Managed file shares for cloud or on-premises deployments.
- AWS S3: A scalable, high-performance, and durable object storage service that offers a range of storage classes and features.
- AWS EBS: A block-level storage service that provides persistent and low-latency storage for Amazon EC2 instances.
- Google Cloud Storage: A unified object storage service that offers multiple storage classes, lifecycle management, encryption, and access control.
- Google Cloud Filestore: A fully managed file storage service that provides consistent performance and high availability for applications that require a file system interface.