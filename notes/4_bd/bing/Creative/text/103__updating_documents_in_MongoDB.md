#### Updating Documents in MongoDB

- MongoDB provides various methods to update documents in a collection, such as `db.collection.updateOne()`, `db.collection.updateMany()`, and `db.collection.replaceOne()`.
- To update documents, MongoDB uses update operators, such as `$set`, `$inc`, `$push`, etc., to modify the field values of the matching documents.
- The update methods take a filter parameter to specify which documents to update, and an update parameter to specify the changes to apply.
- The update methods can also take an options parameter to configure the update operation, such as `upsert`, `multi`, `writeConcern`, etc.
- The update methods return a result object that contains information about the update operation, such as `matchedCount`, `modifiedCount`, `upsertedId`, etc.
- The `db.collection.updateOne()` method updates the first document that matches the filter.
- The `db.collection.updateMany()` method updates all the documents that match the filter.
- The `db.collection.replaceOne()` method replaces the entire document that matches the filter with a new document, except for the `_id` field.
- The replacement document must not contain any update operators, and can have different fields from the original document.
- The `_id` field is immutable, and if included in the replacement document, must have the same value as the current value.