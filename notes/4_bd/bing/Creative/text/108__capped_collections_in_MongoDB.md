#### Capped Collections in MongoDB

Capped collections are fixed-size collections that support high-throughput operations that insert and retrieve documents based on insertion order. Capped collections work in a way similar to circular buffers: once a collection fills its allocated space, it makes room for new documents by overwriting the oldest documents in the collection.

Some of the features and limitations of capped collections are:

- Capped collections guarantee preservation of the insertion order. As a result, queries do not need an index to return documents in insertion order. Without this indexing overhead, capped collections can support higher insertion throughput.
- Capped collections automatically remove the oldest documents in the collection without requiring scripts or explicit remove operations. This makes them suitable for storing log information, high-volume data, and cache information  .
- Capped collections have an _id field and an index on the _id field by default.
- Capped collections cannot be sharded.
- Capped collections do not support read concern "snapshot".
- Capped collections do not allow updates or replacements that change the document size. If an update or a replacement operation changes the document size, the operation will fail.
- Capped collections do not allow deletion of documents. To remove all documents from a collection, use the drop () method to drop the collection and recreate the capped collection.

To create a capped collection, you must use the db.createCollection () method, which is a mongosh helper for the create command. When creating a capped collection you must specify the maximum size of the collection in bytes, which MongoDB will pre-allocate for the collection .

For example, the following command creates a capped collection named logs with a maximum size of 10000 bytes:

```javascript
db.createCollection("logs", { capped: true, size: 10000 })
```

To query a capped collection, you can use the natural ordering to retrieve the most recently inserted elements from the collection efficiently.

For example, the following command returns the last 10 documents inserted in the logs collection:

```javascript
db.logs.find().sort({ $natural: -1 }).limit(10)
```

To check if a collection is capped, you can use the isCapped () method, which is a mongosh helper for the collStats command .

For example, the following command returns true if the logs collection is capped, and false otherwise:

```javascript
db.logs.isCapped()
```

To convert a normal collection to a capped collection, you can use the convertToCapped command .

For example, the following command converts the normal collection named users to a capped collection with a maximum size of 5000 bytes:

```javascript
db.runCommand({ convertToCapped: "users", size: 5000 })
```

To change the size or the maximum number of documents of a capped collection, you can use the collMod command with the max or the size option .

For example, the following command changes the size of the logs collection to 15000 bytes:

```javascript
db.runCommand({ collMod: "logs", size: 15000 })
```

And the following command changes the maximum number of documents in the logs collection to 100:

```javascript
db.runCommand({ collMod: "logs", max: 100 })
```

Capped collections also support tailable cursors, which are special cursors that remain open after the client exhausts the results in the initial cursor. Tailable cursors are useful for creating pub/sub mechanisms and for tailing the MongoDB oplog .

For example, the following command creates a tailable cursor on the logs collection:

```javascript
var cursor = db.logs.find().tailable()
```

The cursor can then be iterated over to retrieve the documents in the collection, and it will remain open even if there are no more documents to return. To check if there are new documents in the collection, you can use the hasNext () method on the cursor:

```javascript
while (true) {
  if (cursor.hasNext()) {
    printjson(cursor.next());
  }
}
```

This will print the documents in the logs collection as they are inserted, and will keep waiting for new documents until the cursor is closed.