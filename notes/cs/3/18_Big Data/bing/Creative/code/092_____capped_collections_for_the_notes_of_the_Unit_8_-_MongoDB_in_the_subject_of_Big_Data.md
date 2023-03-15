### Capped Collections

Capped collections are a type of collections in MongoDB that have the following characteristics  :

- They are fixed-size collections that support high-throughput operations that insert and retrieve documents based on insertion order.
- They work in a way similar to circular buffers: once a collection fills its allocated space, it makes room for new documents by overwriting the oldest documents in the collection.
- They do not support updates that increase the size of the documents. If an update operation causes the document to exceed the original size, MongoDB will remove the document from the collection.
- They do not support the delete operation. To remove documents from a capped collection, you can drop the collection or use the $pop operator to remove either the first or the last document of the collection.
- They guarantee preservation of the insertion order. As a result, queries do not need an index to return documents in insertion order. Additionally, queries can use the natural keyword to specify the order.
- They automatically create an index on the _id field, which cannot be removed.
- They support creating additional indexes, except for text indexes.
- They support the creation of tailable cursors, which are special cursors that remain open after the client exhausts the results in the initial cursor. Tailable cursors enable clients to wait for new data and process results asynchronously.

To create a capped collection, you must use the db.createCollection() method, which is a mongosh helper for the create command. When creating a capped collection, you must specify the maximum size of the collection in bytes, which MongoDB will pre-allocate for the collection. You can also optionally specify the maximum number of documents that the collection can hold. For example, the following command creates a capped collection named logs with a maximum size of 10 MB and a maximum of 1000 documents :

```javascript
db.createCollection("logs", { capped: true, size: 10485760, max: 1000 })
```

To check if a collection is capped, you can use the db.collection.isCapped() method, which returns true if the collection is capped and false otherwise. For example, the following command checks if the logs collection is capped:

```javascript
db.logs.isCapped()
```

To convert a non-capped collection to a capped collection, you can use the db.collection.convertToCapped() method, which takes the name of the collection and the maximum size in bytes as arguments. For example, the following command converts the users collection to a capped collection with a maximum size of 5 MB:

```javascript
db.users.convertToCapped("users", 5242880)
```

Capped collections are useful for storing log information, high volume of data, and cache information. They offer performance advantages over non-capped collections for these use cases, as they do not require indexes, fragmentation, or compaction. However, they also have some limitations, such as the inability to delete or update documents, the fixed size of the collection, and the dependency on the natural order of the documents. Therefore, you should carefully consider the trade-offs before using capped collections in your application.