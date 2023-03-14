#### Deleting documents in MongoDB

- MongoDB provides two methods to delete documents from a collection: `db.collection.deleteOne()` and `db.collection.deleteMany()`.
- The `deleteOne()` method deletes the first document that matches a given filter condition. The `deleteMany()` method deletes all the documents that match a given filter condition. If no filter condition is specified, both methods delete all the documents in the collection.
- The syntax of the `deleteOne()` and `deleteMany()` methods is:

```javascript
db.collection.deleteOne(
   <filter>,
   {
      writeConcern: <document>,
      collation: <document>
   }
)

db.collection.deleteMany(
   <filter>,
   {
      writeConcern: <document>,
      collation: <document>
   }
)
```

- The `<filter>` parameter is a document that specifies the query criteria to select the documents to delete. It can be an empty document `{}` to match all the documents in the collection, or it can use any of the query operators supported by MongoDB.
- The `writeConcern` and `collation` options are optional and specify the level of acknowledgment requested from MongoDB for the write operation and the collation to use for string comparisons, respectively.
- The `deleteOne()` and `deleteMany()` methods return a `DeleteResult` object that contains the following fields:

```javascript
{
   // The number of documents deleted
   deletedCount: <number>,
   // A document containing the _id of the deleted document if the operation is run with write concern
   result: { n: <number>, ok: <number> }
}
```

- Some examples of using the `deleteOne()` and `deleteMany()` methods are:

```javascript
// Delete the first document where the field x is equal to 1
db.collection.deleteOne({ x: 1 })

// Delete all the documents where the field y is less than 10
db.collection.deleteMany({ y: { $lt: 10 } })

// Delete all the documents in the collection
db.collection.deleteMany({})
```

- A mnemonic to remember the difference between `deleteOne()` and `deleteMany()` is: **One** rhymes with **fun**, so it deletes the **first** document that matches the filter. **Many** rhymes with **plenty**, so it deletes **all** the documents that match the filter.