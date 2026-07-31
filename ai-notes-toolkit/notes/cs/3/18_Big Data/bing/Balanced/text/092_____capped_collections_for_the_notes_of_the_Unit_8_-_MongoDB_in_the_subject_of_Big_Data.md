### Capped Collections

Capped collections are a type of collections in MongoDB that have the following characteristics:

- They have a fixed size in bytes, which is specified when they are created. MongoDB will pre-allocate the space for the collection and will not allow it to grow beyond the limit.
- They support high-throughput operations that insert and retrieve documents based on the insertion order. This makes them suitable for storing log information, high volume of data, and cache information.
- They work in a way similar to circular buffers: once a collection fills its allocated space, it makes room for new documents by overwriting the oldest documents in the collection. This means that the documents in a capped collection are not guaranteed to persist forever.
- They do not support updates that increase the size of the documents. If an update operation would cause a document to grow, MongoDB will reject the update.
- They do not support the delete operation. To remove all documents from a capped collection, use the drop () method.
- They automatically create an index on the _id field, which reflects the insertion order. This index cannot be removed.
- They can be used to create tailable cursors, which are special cursors that remain open after returning the last document from a query and can retrieve new documents as they are inserted.

To create a capped collection, use the db.createCollection () method, which is a mongosh helper for the create command. You must specify the name of the collection and the maximum size in bytes as parameters. For example, the following command creates a capped collection named logs with a size limit of 10 MB:

```javascript
db.createCollection("logs", { capped: true, size: 10485760 })
```

You can also optionally specify the maximum number of documents that the collection can hold, using the max parameter. For example, the following command creates a capped collection named cache with a size limit of 5 MB and a document limit of 1000:

```javascript
db.createCollection("cache", { capped: true, size: 5242880, max: 1000 })
```

To verify that a collection is capped, use the isCapped () method, which returns true if the collection is capped and false otherwise. For example, the following command checks if the logs collection is capped:

```javascript
db.logs.isCapped()
```

To convert a non-capped collection to a capped collection, use the convertToCapped command. You must specify the name of the collection and the maximum size in bytes as parameters. For example, the following command converts the users collection to a capped collection with a size limit of 20 MB:

```javascript
db.runCommand({ convertToCapped: "users", size: 20971520 })
```

Note that converting a non-capped collection to a capped collection may delete some documents if the size limit is smaller than the current size of the collection.

Capped collections have some advantages and disadvantages compared to regular collections. Some of the advantages are:

- They provide fast and predictable performance for inserting and retrieving documents in insertion order.
- They do not require a background process to remove expired documents, as they automatically overwrite the oldest documents when the space is full.
- They can be used to implement publish-subscribe patterns, using tailable cursors to stream data to subscribers.

Some of the disadvantages are:

- They have a fixed size limit, which may not be suitable for some applications that require dynamic growth or persistence of data.
- They do not support updates that increase the size of the documents, which may limit the flexibility of the schema.
- They do not support the delete operation, which may make it difficult to remove unwanted or sensitive data.

Capped collections are a useful feature of MongoDB that can be used for specific use cases that require high-throughput operations and insertion order preservation. However, they also have some limitations and trade-offs that should be considered before using them.

: Capped Collections — MongoDB Manual
: Functions of MongoDB Capped Collections - EDUCBA