#### Deleting documents in MongoDB

- MongoDB provides two methods to delete documents from a collection: `db.collection.deleteOne()` and `db.collection.deleteMany()`.
- The `deleteOne()` method deletes the first document that matches the specified filter. The `deleteMany()` method deletes all documents that match the specified filter.
- Both methods return a `DeleteResult` object that contains the number of deleted documents and a boolean flag indicating whether the operation acknowledged by the server.
- To delete all documents from a collection, use `deleteMany()` method with an empty filter `{}`.
- To delete a single document by its `_id` field, use `deleteOne()` method with the `_id` value as the filter.
- To delete multiple documents that match a condition, use `deleteMany()` method with the condition as the filter.
- To delete documents in a transaction, use `session.withTransaction()` method and pass the delete operations as callbacks.

##### Examples

- Delete the first document where the field `status` is equal to `"D"`:

```javascript
db.orders.deleteOne({ status: "D" })
```

- Delete all documents where the field `status` is equal to `"D"`:

```javascript
db.orders.deleteMany({ status: "D" })
```

- Delete all documents from the `orders` collection:

```javascript
db.orders.deleteMany({})
```

- Delete the document with the `_id` value of `ObjectId("5f6a4b8c9d1e4a3b3c9b0f88")`:

```javascript
db.orders.deleteOne({ _id: ObjectId("5f6a4b8c9d1e4a3b3c9b0f88") })
```

- Delete all documents where the field `qty` is less than `20`:

```javascript
db.orders.deleteMany({ qty: { $lt: 20 } })
```

- Delete documents in a transaction:

```javascript
// Start a session
const session = db.getMongo().startSession();

// Start a transaction
session.startTransaction();

// Delete one document from the inventory collection
session.withTransaction(() => {
  db.inventory.deleteOne({ sku: "abc123" }, { session });
});

// Delete many documents from the orders collection
session.withTransaction(() => {
  db.orders.deleteMany({ sku: "abc123" }, { session });
});

// Commit the transaction
session.commitTransaction();

// End the session
session.endSession();
```

##### Mnemonics and learning tricks

- Remember the CRUD acronym for the four basic operations on MongoDB collections: Create, Read, Update, and Delete.
- Remember the difference between `deleteOne()` and `deleteMany()` by their names: one deletes one document, many deletes many documents.
- Remember that both methods require a filter argument, which can be an empty object `{}` to match all documents.
- Remember that both methods return a `DeleteResult` object, which has two properties: `deletedCount` and `acknowledged`.
- Remember that to delete a document by its `_id`, you need to use the `ObjectId()` constructor to match the `_id` value.
- Remember that to delete documents in a transaction, you need to use a session object and the `withTransaction()` method.