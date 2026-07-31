# Unit 8 - MongoDB

## MongoDB Basics

- MongoDB is a document-oriented NoSQL database used for high-volume data storage.
- MongoDB stores data as JSON-like documents with optional schema instead of using tables and rows in relational databases .
- MongoDB supports dynamic queries, indexing, aggregation, replication, sharding, and other features to handle different types of data and applications .
- MongoDB can be installed on various operating systems and accessed through different drivers, tools, and interfaces .

## Creating your first MongoDB collection

- A collection is a group of documents in MongoDB that share a common structure or purpose.
- To create a collection, you can use the `db.createCollection()` method or the `db.collection.insertOne()` or `db.collection.insertMany()` methods .
- For example, to create a collection named `students` and insert a document with the fields `name`, `age`, and `grade`, you can run the following command in the MongoDB shell:

```javascript
db.students.insertOne({name: "Alice", age: 18, grade: "A"})
```

- This will create the `students` collection if it does not exist and insert the document into it. You can verify the creation of the collection by using the `show collections` command .

## Filtering records in MongoDB

- To filter specific records from a MongoDB collection, you can use the `db.collection.find()` method with a query document as an argument .
- The query document specifies the criteria or conditions for selecting the documents from the collection .
- For example, to find all the documents in the `students` collection where the `grade` is `"A"`, you can run the following command in the MongoDB shell:

```javascript
db.students.find({grade: "A"})
```

- This will return all the matching documents from the collection. You can also use various operators, such as `$gt`, `$lt`, `$in`, `$or`, etc., to specify more complex conditions .

## Common MongoDB commands

- MongoDB provides a rich set of commands and methods to perform various operations on the collections and documents.
- Some of the common MongoDB commands are:

  - `db.collection.updateOne()`: Updates a single document that matches the query document.
  - `db.collection.updateMany()`: Updates all the documents that match the query document.
  - `db.collection.deleteOne()`: Deletes a single document that matches the query document.
  - `db.collection.deleteMany()`: Deletes all the documents that match the query document.
  - `db.collection.countDocuments()`: Counts the number of documents that match the query document.
  - `db.collection.distinct()`: Returns an array of distinct values for a specified field in a collection.
  - `db.collection.aggregate()`: Performs aggregation operations on a collection using a pipeline of stages.

## Best Practice Considerations in MongoDB

- MongoDB is a flexible and scalable database that can handle different types of data and applications, but it also requires some best practices to ensure optimal performance and reliability .
- Some of the best practice considerations in MongoDB are:

  - Choose an appropriate data model that suits your application needs and avoids unnecessary joins, duplication, or denormalization .
  - Use indexes to speed up queries and sort operations, but avoid creating too many indexes that can affect write performance and storage space .
  - Use replication to ensure high availability and data redundancy, but also consider the trade-offs between consistency and latency .
  - Use sharding to distribute data across multiple servers and increase scalability, but also consider the impact on query complexity and network overhead .
  - Monitor and tune your MongoDB deployment using various tools and metrics, such as `mongostat`, `mongotop`, `db.serverStatus()`, etc .