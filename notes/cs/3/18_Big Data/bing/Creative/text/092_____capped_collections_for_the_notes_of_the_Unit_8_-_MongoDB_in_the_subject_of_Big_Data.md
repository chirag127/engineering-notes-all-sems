### Capped Collections

Capped collections are a special type of collections in MongoDB that have the following characteristics  :

- They are fixed-size collections that support high-throughput operations that insert and retrieve documents based on insertion order.
- They work in a way similar to circular buffers: once a collection fills its allocated space, it makes room for new documents by overwriting the oldest documents in the collection.
- They do not support updates that increase the size of the documents. If an update operation causes the document to exceed the original size, MongoDB will remove the document from the capped collection.
- They do not support the delete operation. To remove all documents from a capped collection, use the drop () method.
- They guarantee preservation of the insertion order. As a result, queries do not need an index to return documents in insertion order. Additionally, queries can use the natural sort order to return results in insertion order.
- They automatically remove the oldest documents in the collection without requiring scripts or explicit remove operations.
- They support creating tailable cursors, which are special cursors that remain open after the client exhausts the results in the initial cursor. Tailable cursors are useful for creating pub/sub type of applications.

To create a capped collection, you must use the db.createCollection () method, which is a mongosh helper for the create command. When creating a capped collection, you must specify the maximum size of the collection in bytes, which MongoDB will pre-allocate for the collection. You can also optionally specify the maximum number of documents in the collection .

For example, the following command creates a capped collection named logs with a maximum size of 100 MB and a maximum of 1000 documents:

```javascript
db.createCollection("logs", { capped: true, size: 100000000, max: 1000 })
```

Capped collections are useful for storing log information, high volume of data, and cache information. They provide fast and efficient access to the most recent data, and can be used for real-time analytics, monitoring, or messaging systems. However, they also have some limitations, such as:

- They cannot be sharded, as sharding requires an index on the shard key, which is not supported by capped collections.
- They cannot be part of a transaction, as transactions require the ability to roll back changes, which is not possible with capped collections.
- They cannot be converted to regular collections, or vice versa, without dropping and recreating the collection.