The following is a detailed ASCII diagram for S3 for the notes of the Unit 3 - Cloud Architecture, Services And Storage in the subject of Cloud Computing.

### S3

S3 stands for Simple Storage Service. It is a public cloud storage service that allows users to store and retrieve various types of data using API calls. S3 does not contain any computing element. S3 organizes data into buckets and objects. A bucket is a container for objects, and an object is a file with metadata. S3 supports different storage classes, encryption, versioning, lifecycle management, and access control policies for buckets and objects.

The diagram below illustrates the basic architecture of S3.

```
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  S3 Standard    |      |  S3 Standard-   |      |  S3 One Zone-   |
|                 |      |  Infrequent     |      |  Infrequent     |
|                 |      |  Access (IA)    |      |  Access (IA)    |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  S3 Intelligent |      |  S3 Glacier     |      |  S3 Glacier     |
|  Tiering        |      |                 |      |  Deep Archive   |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  S3 Outposts    |      |  S3 Reduced     |      |  S3 Object      |
|                 |      |  Redundancy     |      |  Lock           |
|                 |      |  Storage (RRS)  |      |                 |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
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
       |                      |                      |
       +----------------------+----------------------+
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |