### Capped Collections

Capped collections are fixed-size collections in MongoDB that support high-throughput operations that insert and retrieve documents based on insertion order. They are ideal for storing log data or other high-volume data that is accessed in a first-in, first-out (FIFO) manner.

Here are some key points to remember about capped collections:

1. Capped collections have a maximum size, specified in bytes, that cannot be exceeded. Once the maximum size is reached, the oldest documents are automatically removed to make room for new documents.

2. Capped collections maintain the insertion order of documents. This means that documents are always retrieved in the order in which they were inserted.

3. Capped collections support high-throughput insert and retrieval operations. This makes them ideal for storing log data or other high-volume data that is accessed in a first-in, first-out (FIFO) manner.

4. Capped collections do not support updates that increase the size of a document. If an update would cause a document to exceed its original size, the update will fail.

5. Capped collections do not support the `delete` operation. Documents can only be removed by reaching the maximum size of the collection and being automatically removed by the system.

6. Capped collections can be created using the `createCollection` command with the `capped` and `size` options. For example, to create a capped collection named `logs` with a maximum size of 1GB, the following command can be used:

```
db.createCollection("logs", { capped: true, size: 1073741824 })
```

7. Capped collections can be converted to regular (uncapped) collections using the `convertToCapped` command. However, once a collection is converted to a capped collection, it cannot be converted back to an uncapped collection.
