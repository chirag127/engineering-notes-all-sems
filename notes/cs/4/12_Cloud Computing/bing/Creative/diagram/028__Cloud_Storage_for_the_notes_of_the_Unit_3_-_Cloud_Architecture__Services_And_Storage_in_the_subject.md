The following diagram illustrates the basic architecture of a cloud storage system:

```
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|   Application   |       |   Application   |       |   Application   |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|   API Gateway   |       |   API Gateway   |       |   API Gateway   |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|   Storage API   |       |   Storage API   |       |   Storage API   |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|   Storage Node  |       |   Storage Node  |       |   Storage Node  |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
```

A cloud storage system consists of the following components:

- Application: The end-user application that interacts with the cloud storage system via an API. Examples of applications are web browsers, mobile apps, or desktop clients.
- API Gateway: The entry point for the cloud storage system that handles authentication, authorization, load balancing, and routing of requests to the appropriate storage API.
- Storage API: The interface that exposes the functionality of the cloud storage system, such as creating, reading, updating, or deleting objects, files, or blocks. The storage API may also provide features such as encryption, compression, deduplication, replication, or backup.
- Storage Node: The physical or virtual server that stores the data on disks, tapes, or other media. The storage node may also perform tasks such as data integrity checking, data recovery, or data migration.