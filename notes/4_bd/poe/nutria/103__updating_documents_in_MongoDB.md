
#### Updating Documents in MongoDB

* MongoDB provides a number of methods to update documents in a collection.
* The most commonly used methods are `updateOne()`, `updateMany()`, and `replaceOne()`. 
* The `updateOne()` method updates a single document that matches the query filter. 
* The `updateMany()` method updates multiple documents that match the query filter.
* The `replaceOne()` method replaces a single document that matches the query filter.
* All three methods accept two parameters: a query filter object and an update object.
* The query filter object is used to determine which documents to update.
* The update object is used to define the new values and operators that modify the existing values in the documents.
* MongoDB also provides the `findOneAndUpdate()` method, which is a combination of the `find()` and `updateOne()` methods.
* To update a document, the user must have `update` permission on the collection.