# Capped Collections

Capped collections are a special type of collections in MongoDB that have the following characteristics  :

- They are fixed-size collections that support high-throughput operations that insert and retrieve documents based on insertion order.
- They work in a way similar to circular buffers: once a collection fills its allocated space, it makes room for new documents by overwriting the oldest documents in the collection.
- They do not support updates that increase the size of the documents. If an update operation causes a document to exceed the original size, MongoDB will remove the document from the capped collection.
- They do not support the delete operation. To remove all documents from a capped collection, use the drop () method.
- They guarantee preservation of the insertion order. As a result, queries do not need an index to return documents in insertion order. Additionally, queries can use the natural keyword to specify the order.
- They support creating a tailable cursor that remains open after the client exhausts the results, awaiting the insertion of new documents.

To create a capped collection, you must use the db.createCollection () method, which is a mongosh helper for the create command. When creating a capped collection, you must specify the maximum size of the collection in bytes, which MongoDB will pre-allocate for the collection . For example:

```javascript
db.createCollection("logs", { capped: true, size: 100000 } )
```

This command creates a capped collection named logs with a maximum size of 100000 bytes.

Capped collections are useful for storing log information, high volume of data, and cache information . Some of the benefits of using capped collections are:

- They provide high performance and low latency for read and write operations.
- They ensure that the most recent data is available by automatically removing the oldest data.
- They support tailable cursors that can be used for real-time data processing and notifications.

Some of the limitations of using capped collections are:

- They cannot be sharded. Sharding is a feature that distributes data across multiple servers for scalability and availability.
- They cannot use the $out and $merge aggregation stages. These stages allow writing the results of an aggregation pipeline to a collection.
- They cannot be converted to non-capped collections and vice versa. To change the type of a collection, you must create a new collection and copy the data.