# Unit 3 - Hadoop Eco System and YARN , no SQL databases , MongoDB , Spark , Scala

- Hadoop Ecosystem is a platform or a suite which provides various services to solve the big data problems. It includes Apache projects and various commercial tools and solutions.
- Hadoop Ecosystem consists of four major elements: HDFS, MapReduce, YARN, and Hadoop Common.
- HDFS is the distributed file system that stores the data in a cluster of nodes. It provides high availability, fault tolerance, scalability, and reliability.
- MapReduce is the programming model that processes the data in parallel using key-value pairs. It consists of two phases: map and reduce. Map phase applies a function to each input record and generates intermediate key-value pairs. Reduce phase aggregates the intermediate values associated with the same key and produces the final output.
- YARN (Yet Another Resource Negotiator) is the resource management layer of Hadoop. It is responsible for allocating and scheduling the resources (CPU, memory, disk, network) for the applications running on the cluster. It also monitors and manages the workloads. YARN consists of two components: ResourceManager and NodeManager.
- ResourceManager is the master daemon that runs on a dedicated node and oversees the global resource allocation and application lifecycle management. It has two sub-components: Scheduler and ApplicationsManager.
- Scheduler is responsible for allocating resources to the applications based on the resource requests, constraints, and policies. It does not perform any monitoring or tracking of the application status. It supports multiple scheduling algorithms such as FIFO, Capacity, and Fair.
- ApplicationsManager is responsible for accepting and rejecting the application submissions, negotiating the first container for the application, and recovering the applications in case of failure. It also maintains the application metadata and history.
- NodeManager is the slave daemon that runs on each worker node and manages the resources and containers on that node. It communicates with the ResourceManager and reports the resource utilization and availability. It also launches and monitors the containers that execute the application tasks.
- Hadoop Common is the set of common utilities and libraries that support the other Hadoop modules. It provides the basic functionalities such as configuration, I/O, serialization, logging, and security.

- NoSQL databases are the databases that do not follow the relational model and SQL standards. They are designed to handle large volumes of unstructured, semi-structured, or structured data with high scalability, availability, and performance. They support various data models such as key-value, document, column-family, graph, and multi-model.
- MongoDB is a popular open-source NoSQL database that follows the document data model. It stores the data as JSON-like documents in collections. It provides various features such as dynamic schema, indexing, aggregation, replication, sharding, transactions, and text search.
- MongoDB supports various data types such as string, number, boolean, array, object, null, date, object id, binary, code, regular expression, timestamp, and decimal.
- MongoDB provides CRUD (create, read, update, and delete) operations to manipulate the documents in the collections. The basic syntax for these operations are as follows:
  - Create: `db.collection.insertOne(document)` or `db.collection.insertMany(documents)`
  - Read: `db.collection.find(query, projection)`
  - Update: `db.collection.updateOne(filter, update, options)` or `db.collection.updateMany(filter, update, options)`
  - Delete: `db.collection.deleteOne(filter, options)` or `db.collection.deleteMany(filter, options)`
- MongoDB also supports indexing to improve the query performance. Indexes are special data structures that store a subset of the collection's data in an easy-to-traverse form. MongoDB supports various types of indexes such as single field, compound, multikey, text, hashed, geospatial, and wildcard.
- MongoDB also supports capped collections, which are fixed-size collections that automatically remove the oldest documents when they reach their maximum size. Capped collections are useful for storing log data, time series data, or any data that requires a FIFO (first-in first-out) retrieval order.

- Spark is a fast and general-purpose framework for large-scale data processing. It provides an in-memory computation engine that can run up to 100 times faster than MapReduce. It also supports various APIs for different languages such as Scala, Python, Java, and R. It also supports SQL, streaming, machine learning, and