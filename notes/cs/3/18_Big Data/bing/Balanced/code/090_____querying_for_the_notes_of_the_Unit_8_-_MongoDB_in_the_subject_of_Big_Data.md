Hello, I am Sydney, your AI assistant. I can help you with your query. Here are the notes of the Unit 8 - MongoDB in the subject of Big Data:

# Unit 8 - MongoDB

## Introduction

- MongoDB is a popular open-source document-oriented database that stores data in JSON-like format.
- MongoDB is a NoSQL database that does not use tables, rows, and columns to store data, but instead uses collections, documents, and fields.
- MongoDB supports dynamic schema, meaning that the structure of the documents in a collection can vary and change over time.
- MongoDB is designed for scalability, performance, and high availability, and supports sharding, replication, and aggregation.

## MongoDB Terminology

- Database: A logical container for collections of documents.
- Collection: A group of documents that share a common purpose or structure.
- Document: A record of data that consists of one or more fields.
- Field: A key-value pair that represents an attribute of a document.
- Index: A data structure that improves the speed and efficiency of queries and operations on a collection.
- Cursor: A pointer to the result set of a query that can be iterated over to fetch documents.
- Aggregation: A process of transforming and analyzing data from a collection using various operators and stages.
- Shard: A partition of data that is stored on a separate server or cluster of servers.
- Replica Set: A group of servers that maintain the same data and provide redundancy and fault tolerance.
- Query: A request to retrieve or modify data from a collection or an aggregation pipeline.

## MongoDB Installation and Configuration

- MongoDB can be installed on various operating systems, such as Windows, Linux, and Mac OS X, by downloading the appropriate package from the official website or using a package manager.
- MongoDB can be configured by editing the configuration file (mongod.conf) or using command-line options when starting the mongod process.
- MongoDB can be started by running the mongod command, which launches the MongoDB server and listens for connections on the default port 27017.
- MongoDB can be stopped by sending a SIGTERM signal to the mongod process or using the db.shutdownServer() method in the mongo shell.
- MongoDB can be connected to by using the mongo command, which launches the MongoDB shell and allows the user to interact with the database.

## MongoDB CRUD Operations

- CRUD stands for Create, Read, Update, and Delete, which are the basic operations that can be performed on data in a database.
- MongoDB provides various methods and commands to perform CRUD operations on collections and documents, such as:

  - db.collection.insertOne(), db.collection.insertMany(), and db.collection.insert() to create new documents in a collection.
  - db.collection.find() and db.collection.findOne() to read documents from a collection based on a query filter and projection.
  - db.collection.updateOne(), db.collection.updateMany(), and db.collection.update() to update existing documents in a collection based on a query filter and update document.
  - db.collection.deleteOne(), db.collection.deleteMany(), and db.collection.remove() to delete documents from a collection based on a query filter.

- MongoDB also provides various operators and modifiers to specify the query filter, projection, update document, and other options for CRUD operations, such as:

  - Comparison operators ($eq, $gt, $gte, $lt, $lte, $ne, $in, $nin) to compare the values of fields with a specified value or an array of values.
  - Logical operators ($and, $or, $nor, $not) to combine multiple query conditions with logical conjunctions or negations.
  - Element operators ($exists, $type) to check the existence or data type of a field in a document.
  - Array operators ($all, $elemMatch, $size) to match documents that contain an array field with a specified value, condition, or size.
  - Projection operators ($, $elemMatch, $slice, $meta) to include or exclude specific fields or elements from the result set of a query.
  - Update operators ($set, $unset, $inc, $mul, $rename, $min, $max, $currentDate) to modify the values of fields in an update document.
  - Array update operators ($push, $pop, $pull, $pullAll, $addToSet) to add or remove elements from an array field in an update document.

## MongoDB Indexes

- Indexes are data structures that store a subset of the collection's data in an ordered form, which makes it faster and more efficient to locate and retrieve documents that match a query or an operation.
- MongoDB supports various types of indexes, such as:

  - Single field index: An index that is created on a single field of