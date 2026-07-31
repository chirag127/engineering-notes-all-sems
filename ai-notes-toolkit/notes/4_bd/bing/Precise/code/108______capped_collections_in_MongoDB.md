#### Capped Collections in MongoDB
- Capped collections are fixed-size collections that support high-throughput operations that insert and retrieve documents based on insertion order.
- Capped collections work in a way similar to circular buffers: once a collection fills its allocated space, it makes room for new documents by overwriting the oldest documents in the collection.
- To create a capped collection, you must specify the size of the collection in bytes. Optionally, you can also specify the maximum number of documents for the collection.
- Capped collections automatically maintain insertion order for the documents in the collection. This means that you can use natural order queries to retrieve documents in the order they were inserted.
- Capped collections have some limitations. For example, you cannot delete documents from a capped collection, and you cannot update documents in a way that would increase their size.
- Capped collections are ideal for applications that require fast, high-throughput insertion and retrieval of documents in insertion order, such as log data or real-time data feeds.