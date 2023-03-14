#### Deleting documents in MongoDB

- MongoDB is a document-oriented database that stores data in collections of JSON-like documents.
- To delete documents from a collection, MongoDB provides the following methods:
  - `db.collection.deleteOne()`: Deletes at most one document that matches a specified filter.
  - `db.collection.deleteMany()`: Deletes all documents that match a specified filter.
  - `db.collection.remove()`: Deletes one or more documents that match a specified filter. This method is deprecated in MongoDB 4.0 and should be avoided.
- To delete all documents from a collection, pass an empty filter document `{}` to the delete method.
- To delete documents that match a condition, use a query filter document that specifies the criteria for deletion. The query filter document can use the same syntax and operators as read operations.
- To specify additional options for the delete operation, such as write concern, ordered execution, or collation, use the `delete` command instead of the delete methods. The `delete` command takes an array of delete specifications that contain the query filter, the limit, and the optional collation and hint fields.
- Delete operations do not drop indexes, even if deleting all documents from a collection.
- All write operations in MongoDB are atomic on the level of a single document. For more information on MongoDB and atomicity, see [Atomicity and Transactions](https://www.mongodb.com/docs/core/transactions/).