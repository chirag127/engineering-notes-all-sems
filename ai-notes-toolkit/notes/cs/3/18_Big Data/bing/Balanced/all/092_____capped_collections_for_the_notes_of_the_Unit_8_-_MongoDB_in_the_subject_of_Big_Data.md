# Capped Collections

Capped collections are a type of collections in MongoDB that have the following characteristics:

- They have a fixed size in bytes, which is specified when they are created.
- They support high-throughput operations that insert and retrieve documents based on insertion order.
- They work like circular buffers, meaning that when they reach their maximum size, they overwrite the oldest documents with the new ones.
- They do not support updates that increase the size of the documents.
- They do not support the delete operation, except for dropping the entire collection.
- They automatically create an index on the _id field, which reflects the insertion order.

Some of the use cases for capped collections are:

- Storing log information, such as web server logs or application logs.
- Storing high volume of data, such as sensor data or real-time analytics.
- Storing cache information, such as frequently accessed data or session data.

To create a capped collection, you can use the db.createCollection() method, which is a mongosh helper for the create command. For example, the following command creates a capped collection named logs with a maximum size of 10 MB:

```javascript
db.createCollection("logs", { capped: true, size: 10 * 1024 * 1024 })
```

To verify that a collection is capped, you can use the db.collection.isCapped() method, which returns true if the collection is capped and false otherwise. For example, the following command checks if the logs collection is capped:

```javascript
db.logs.isCapped()
```

To insert documents into a capped collection, you can use the same methods as for regular collections, such as db.collection.insertOne() or db.collection.insertMany(). However, you cannot insert documents that are larger than the capped size of the collection, or that would cause the collection to exceed its capped size. For example, the following command inserts a document into the logs collection:

```javascript
db.logs.insertOne({ message: "Hello, world!", timestamp: new Date() })
```

To retrieve documents from a capped collection, you can use the same methods as for regular collections, such as db.collection.find() or db.collection.findOne(). However, you can also use the db.collection.find().tailable() method, which returns a cursor that remains open after the last document is retrieved, and continues to return new documents as they are inserted. This allows you to stream data from a capped collection in real time. For example, the following command creates a tailable cursor on the logs collection:

```javascript
var cursor = db.logs.find().tailable()
```

To update documents in a capped collection, you can use the same methods as for regular collections, such as db.collection.updateOne() or db.collection.updateMany(). However, you cannot update documents that would increase their size, as this would violate the capped size of the collection. For example, the following command updates a document in the logs collection by adding a new field:

```javascript
db.logs.updateOne({ message: "Hello, world!" }, { $set: { level: "info" } })
```

To delete documents from a capped collection, you cannot use the db.collection.deleteOne() or db.collection.deleteMany() methods, as they are not supported. The only way to delete documents from a capped collection is to drop the entire collection using the db.collection.drop() method. For example, the following command drops the logs collection:

```javascript
db.logs.drop()
```

To modify the capped size of a collection, you cannot use the db.collection.createIndex() method, as it is not supported. The only way to modify the capped size of a collection is to use the db.collection.convertToCapped() method, which converts a regular collection to a capped collection, or changes the capped size of an existing capped collection. For example, the following command converts the users collection to a capped collection with a maximum size of 5 MB:

```javascript
db.users.convertToCapped(5 * 1024 * 1024)
```