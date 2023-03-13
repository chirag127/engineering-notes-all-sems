#### Deleting documents in MongoDB

MongoDB is a document-oriented database that stores data in collections of JSON-like documents. To delete documents from a collection, you can use one of the following methods:

- The `db.collection.remove()` method: This method takes a query filter as a parameter and deletes all the documents that match the filter. You can also specify an optional second parameter to limit the deletion to just one document. For example, `db.users.remove({name: "Alice"})` will delete all the documents in the `users` collection where the `name` field is "Alice". `db.users.remove({name: "Alice"}, true)` will delete only one document that matches the filter.
- The `delete` command: This command takes a query filter as a parameter and deletes all the documents that match the filter. You can also specify an optional second parameter to limit the deletion to just one document. For example, `db.runCommand({delete: "users", deletes: [{q: {name: "Alice"}, limit: 0}]})` will delete all the documents in the `users` collection where the `name` field is "Alice". `db.runCommand({delete: "users", deletes: [{q: {name: "Alice"}, limit: 1}]})` will delete only one document that matches the filter.
- The `db.collection.deleteOne()` method: This method takes a query filter as a parameter and deletes the first document that matches the filter. For example, `db.users.deleteOne({name: "Alice"})` will delete the first document in the `users` collection where the `name` field is "Alice".
- The `db.collection.deleteMany()` method: This method takes a query filter as a parameter and deletes all the documents that match the filter. For example, `db.users.deleteMany({name: "Alice"})` will delete all the documents in the `users` collection where the `name` field is "Alice".

Some important points to note about deleting documents in MongoDB are:

- Deleting documents does not affect the indexes on the collection. The index entries for the deleted documents are removed when the collection is compacted or reindexed.
- Deleting documents does not free up disk space immediately. The deleted documents are marked as deleted and the space they occupy can be reused by new documents. To reclaim the disk space, you can use the `db.collection.reIndex()` method or the `compact` command.
- Deleting documents does not affect the `_id` field of the remaining documents. The `_id` field is immutable and unique for each document in a collection.