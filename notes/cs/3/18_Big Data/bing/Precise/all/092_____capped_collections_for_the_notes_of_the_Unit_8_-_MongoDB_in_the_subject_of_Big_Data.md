# Capped Collections

Capped collections are fixed-size collections that support high-throughput operations that insert and retrieve documents based on insertion order. Capped collections work in a way similar to circular buffers: once a collection fills its allocated space, it makes room for new documents by overwriting the oldest documents in the collection.

Here are some characteristics of capped collections:

1. Capped collections automatically remove the oldest documents without the need for an explicit remove operation.
2. Capped collections guarantee preservation of the insertion order. As a result, queries do not need an index to return documents in insertion order. Without this indexing overhead, capped collections can support higher insertion throughput.
3. Capped collections only allow updates if the update does not increase the size of the document.
4. Capped collections do not allow the use of the delete operation. To remove all documents from a capped collection, use the drop() method.
5. Capped collections have a maximum size and a maximum number of documents.

To create a capped collection, use the createCollection() method with the capped option. You must specify the maximum size of the capped collection in bytes. You can also specify the maximum number of documents in the collection.

Example:

```
db.createCollection("log", { capped: true, size: 100000, max: 5000 })
```

This command creates a capped collection named "log" with a maximum size of 100,000 bytes and a maximum of 5,000 documents.

Capped collections are commonly used for storing log information, cache data, and other high-throughput data where preservation of insertion order is important and old data can be automatically removed to make room for new data.