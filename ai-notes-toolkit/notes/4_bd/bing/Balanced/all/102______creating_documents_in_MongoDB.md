#### Creating documents in MongoDB

- MongoDB is a document-oriented database that stores data in collections of JSON-like documents.
- A document is a set of key-value pairs, where the value can be any BSON type, such as string, number, array, object, or null.
- To create documents in MongoDB, you can use one of the following methods: `insertOne()`, `insertMany()`, or `insert()`.
- The `insertOne()` method inserts a single document into a collection. If the collection does not exist, MongoDB creates it automatically. The syntax is:

```javascript
db.collection.insertOne(document, options)
```

- The `insertMany()` method inserts an array of documents into a collection. If the collection does not exist, MongoDB creates it automatically. The syntax is:

```javascript
db.collection.insertMany(documents, options)
```

- The `insert()` method inserts one or more documents into a collection. If the collection does not exist, MongoDB creates it automatically. The syntax is:

```javascript
db.collection.insert(documents, options)
```

- The `documents` parameter can be either a single document or an array of documents. The `options` parameter is an optional object that specifies additional settings, such as write concern or ordered insertion.
- Each document inserted into a collection must have a unique `_id` field that acts as a primary key. If the document does not specify the `_id` field, MongoDB generates an `ObjectId` value for it automatically.
- To verify the insertion of documents, you can use the `find()` method to query the collection. The syntax is:

```javascript
db.collection.find(query, projection)
```

- The `query` parameter is an optional object that specifies the criteria for selecting documents. The `projection` parameter is an optional object that specifies the fields to return or exclude from the documents.