### S3

- S3 stands for Simple Storage Service, and it is a cloud object storage solution provided by Amazon Web Services (AWS) .
- Object storage is a way of storing and retrieving any amount of data as discrete units called objects, which consist of data and metadata .
- S3 is designed for durability, availability, scalability, and performance, and it is ideal for data lakes, mobile applications, backup and restore, archival, IoT devices, ML, AI, and analytics .
- S3 has a web services interface that allows users to create, read, update, and delete objects using HTTP requests .
- S3 also has a management console that provides a graphical user interface for performing common tasks such as creating buckets, uploading objects, and setting permissions .
- A bucket is a container for objects stored in S3, and it has a unique name and a region .
- A region is a geographical area where AWS operates a set of data centers, and it affects the latency, availability, and cost of S3 .
- An object key (or key name) is a unique identifier for an object within a bucket, and it is composed of a prefix and a suffix .
- A prefix is a logical grouping of objects within a bucket, similar to a folder or a directory .
- A suffix is the name of the object itself, similar to a file name .
- For example, in the object key `images/cat.jpg`, the prefix is `images/` and the suffix is `cat.jpg`.
- S3 offers different storage classes for different use cases, such as Standard, Standard-Infrequent Access (SIA), One Zone-Infrequent Access (ZIA), Intelligent-Tiering, Glacier, and Glacier Deep Archive .
- Each storage class has different characteristics in terms of availability, durability, performance, and cost .
- For example, Standard is the default storage class that provides high availability and performance, but also higher cost, while Glacier is a low-cost storage class that provides long-term archival, but also lower availability and performance .
- S3 also provides various features and services to enhance the functionality and security of object storage, such as encryption, versioning, lifecycle management, replication, access control, logging, tagging, and analytics .
- For example, encryption is a feature that protects the data at rest and in transit, while versioning is a feature that preserves multiple versions of an object in the same bucket .