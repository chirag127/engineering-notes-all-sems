#### Creating documents in MongoDB

- MongoDB is a document-oriented database that stores data as BSON documents, which are binary representations of JSON documents.
- MongoDB provides two methods for creating documents in a collection: `insertOne()` and `insertMany()`.
- The `insertOne()` method inserts a single document into a collection, using the following syntax:

```javascript
db.collection.insertOne(
   <document>,
   {
      writeConcern: <document>,
      bypassDocumentValidation: <boolean>
   }
)
```

- The `insertMany()` method inserts multiple documents into a collection, using the following syntax:

```javascript
db.collection.insertMany(
   [ <document 1> , <document 2>, ... ],
   {
      writeConcern: <document>,
      ordered: <boolean>,
      bypassDocumentValidation: <boolean>
   }
)
```

- Both methods return a result object that contains information about the operation, such as the number of documents inserted and the `_id` values of the inserted documents.
- The `_id` field is a unique identifier for each document in a collection. MongoDB automatically generates an `_id` value of the `ObjectId` type if the document does not specify one. The `_id` field is immutable and must be unique in the collection.
- MongoDB also supports creating documents with other types of indexes, such as capped collections, time series collections, and clustered collections. These collections have different properties and limitations than regular collections. For more details, see the [create command documentation](https://www.mongodb.com/docs/manual/reference/command/create/).
- MongoDB also supports creating views, which are read-only collections that display the results of an aggregation pipeline on an underlying collection. Views do not store any data, but rather query the data in real time. For more details, see the [create command documentation](https://www.mongodb.com/docs/manual/reference/command/create/).
- To create documents in MongoDB using VS Code, you can use the MongoDB Playground feature, which allows you to write and execute MongoDB commands and scripts. For more details, see the [MongoDB for VS Code documentation](https://www.mongodb.com/docs/mongodb-vscode/create-document-playground/).
- To create documents in MongoDB using Compass, you can use the Create Database dialog, which allows you to create a database and its first collection at the same time. You can then insert documents into the collection using the Insert Document button. For more details, see the [MongoDB Compass documentation](https://www.mongodb.com/basics/create-database).

Some mnemonics and learning tricks for creating documents in MongoDB are:

- Remember the acronym CRUD for the four basic operations on data: Create, Read, Update, and Delete. Creating documents is the first operation in CRUD.
- Remember the difference between `insertOne()` and `insertMany()` by their names: one inserts one document, and many inserts many documents.
- Remember the syntax of `insertOne()` and `insertMany()` by their parameters: the first parameter is always the document or the array of documents to insert, and the second parameter is an optional object that specifies options for the operation.
- Remember the structure of a BSON document by its components: a document is composed of field-and-value pairs, where the value can be any of the BSON data types, including other documents, arrays, and arrays of documents. A document can also have an `_id` field that uniquely identifies it in the collection.