### Updating and Deleting Documents in MongoDB

- MongoDB provides various methods to update and delete documents from a collection.
- To update a document, MongoDB provides update operators, such as `$set`, `$inc`, `$push`, etc., to modify field values. 
- To use the update operators, pass to the update methods an update document of the form: `{<operator1>: {<field1>: <value1>, ...}, <operator2>: {<field2>: <value2>, ...}, ...}`
- The update methods are:
  - `db.collection.updateOne(filter, update, options)`: Updates a single document that matches the filter.
  - `db.collection.updateMany(filter, update, options)`: Updates all documents that match the filter.
  - `db.collection.replaceOne(filter, replacement, options)`: Replaces a single document that matches the filter with the replacement document.
- To delete a document, MongoDB provides delete operators, such as `$unset`, `$pull`, etc., to remove field values or array elements.
- To use the delete operators, pass to the delete methods a delete document of the form: `{<operator1>: {<field1>: <value1>, ...}, <operator2>: {<field2>: <value2>, ...}, ...}`
- The delete methods are:
  - `db.collection.deleteOne(filter, options)`: Deletes a single document that matches the filter.
  - `db.collection.deleteMany(filter, options)`: Deletes all documents that match the filter.
  - `db.collection.remove(query, justOne)`: Deletes documents that match the query. If `justOne` is true, only the first matching document is deleted.
- To delete all documents from a collection, pass an empty filter document `{}` to the `db.collection.deleteMany()` or `db.collection.remove()` method.