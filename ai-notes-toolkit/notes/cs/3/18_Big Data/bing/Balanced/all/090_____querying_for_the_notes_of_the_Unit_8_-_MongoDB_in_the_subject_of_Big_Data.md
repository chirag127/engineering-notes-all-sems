# Unit 8 - MongoDB in Big Data

- MongoDB is a **NoSQL** database that stores data in **documents**, which are flexible and schema-less JSON-like objects.
- MongoDB is suitable for **big data** applications because it can handle **huge amounts of data**, **partition** and **shard** the data across multiple servers, and perform **MapReduce** calculations on the data.
- MongoDB supports **indexes** to improve the performance of queries. Indexes can be created on single or multiple fields, and can be deleted when not needed.
- Some of the features and benefits of MongoDB are:

  - **Scalability**: MongoDB can scale horizontally by adding more servers to a cluster, and distribute the data and load among them. This allows MongoDB to handle very large data sets and high throughput operations.
  - **Flexibility**: MongoDB does not enforce a fixed schema for the documents, which means that the structure and content of the documents can vary. This allows MongoDB to adapt to changing data and application requirements.
  - **Performance**: MongoDB can use in-memory computing and compression to speed up data access and processing. MongoDB also supports various types of indexes, such as text, geospatial, and hashed indexes, to optimize different kinds of queries.
  - **Availability**: MongoDB can provide high availability and fault tolerance by using **replication** and **automatic failover**. Replication is the process of copying data from one server to another, and automatic failover is the process of switching to a backup server in case of a failure. MongoDB uses a **replica set**, which is a group of servers that maintain the same data, to achieve this.
  - **Aggregation**: MongoDB can perform complex data analysis and transformation using the **aggregation framework**, which is a pipeline of stages that process the data. The aggregation framework can use operators such as match, group, sort, project, and unwind to filter, group, sort, and reshape the data. The aggregation framework can also use **MapReduce**, which is a programming model that allows parallel processing of large data sets using map and reduce functions.