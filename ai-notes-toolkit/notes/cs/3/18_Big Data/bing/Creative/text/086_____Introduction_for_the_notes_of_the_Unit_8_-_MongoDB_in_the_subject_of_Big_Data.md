### Introduction for the notes of the Unit 8 - MongoDB in the subject of Big Data

- MongoDB is a popular open-source document-oriented database that stores data in JSON-like format.
- MongoDB is a NoSQL database, which means it does not use the relational model of tables, rows, and columns, but rather organizes data into collections of documents.
- MongoDB is designed for scalability, performance, and high availability, and supports various features such as replication, sharding, indexing, aggregation, text search, geospatial queries, and more.
- MongoDB is widely used for big data applications, as it can handle large volumes of structured, semi-structured, or unstructured data, and supports various data types such as strings, numbers, arrays, objects, dates, binary data, etc.
- MongoDB is also flexible and schema-less, which means it does not enforce a fixed structure for the documents in a collection, and allows the data to evolve over time.
- MongoDB is compatible with various programming languages and frameworks, and provides drivers and tools for connecting, querying, and managing the database.
- MongoDB is based on the following concepts:

  - Database: A logical container for collections of documents.
  - Collection: A group of documents that share a similar or related purpose.
  - Document: A record of data that consists of one or more key-value pairs.
  - Field: A key-value pair in a document.
  - BSON: A binary representation of JSON data, used to store and transfer data in MongoDB.
  - ObjectId: A 12-byte hexadecimal value that uniquely identifies a document in a collection.
  - Index: A data structure that improves the speed and efficiency of queries on a collection.
  - Query: An operation that retrieves data from a collection or performs some action on the data.
  - Projection: A specification of which fields to include or exclude in the query result.
  - Filter: A condition that matches a subset of documents in a collection.
  - Update: An operation that modifies one or more documents in a collection.
  - Aggregation: A process that performs complex data analysis and transformation on a collection.
  - Pipeline: A sequence of stages that define the steps of an aggregation operation.
  - Operator: A symbol or keyword that specifies a certain logic or function in a query, update, or aggregation.
  - Cursor: A pointer to the result set of a query, which can be iterated to access the documents.
  - Replica Set: A group of MongoDB servers that maintain the same data set and provide high availability and data redundancy.
  - Shard: A partition of data in a MongoDB cluster that distributes the data across multiple servers and provides horizontal scalability.
  - Router: A MongoDB server that routes queries and commands to the appropriate shards in a cluster.
  - Config Server: A MongoDB server that stores the metadata and configuration of a cluster.