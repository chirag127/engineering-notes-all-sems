There are four ways to delete a document in MongoDB :

- The db.collection.remove() method
- The delete command
- The db.collection.deleteOne() method
- The db.collection.deleteMany() method

The following diagram illustrates the basic architecture of a MongoDB database and how these methods can be used to delete documents from a collection:

```
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  MongoDB Shell  |       |  MongoDB Server |       |  MongoDB Client |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       | db.collection.remove()  |                         |
       |------------------------>|                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         | delete command          |
       |                         |------------------------>|
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         | db.collection.deleteOne()|
       |                         |------------------------>|
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         | db.collection.deleteMany()|
       |                         |------------------------>|
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
```

The db.collection.remove() method takes a filter document as a parameter and deletes all documents that match the filter from the collection . For example, to delete all documents where the status field equals "A" from the inventory collection, you can use:

```
db.inventory.remove({status: "A"})
```

The delete command takes a query document as a parameter and deletes all documents that match the query from the collection. For example, to delete all documents where the status field equals "D" from the inventory collection, you can use:

```
delete {q: {status: "D"}, limit: 0}
```

The db.collection.deleteOne() method takes a filter document as a parameter and deletes at most one document that matches the filter from the collection . For example, to delete the first document where the status field equals "P" from the inventory collection, you can use:

```
db.inventory.deleteOne({status: "P"})
```

The db.collection.deleteMany() method takes a filter document as a parameter and deletes all documents that match the filter from the collection . For example, to delete all documents where the status field equals "B" from the inventory collection, you can use:

```
db.inventory.deleteMany({status: "B"})
```