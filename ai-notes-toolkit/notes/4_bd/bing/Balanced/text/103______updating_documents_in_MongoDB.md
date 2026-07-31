#### Updating documents in MongoDB

- MongoDB is a document-oriented database that stores data in JSON-like format.
- To update documents in MongoDB, you can use the `updateOne()`, `updateMany()`, or `replaceOne()` methods of the `db.collection` object.
- The `updateOne()` method updates a single document that matches a given filter condition. It takes two parameters: a filter object and an update object. The filter object specifies the criteria for selecting the document to update, and the update object specifies the changes to apply to the document. For example:

```js
// Update the name field of the document with _id = 1
db.users.updateOne({_id: 1}, {$set: {name: "Alice"}})
```

- The `updateMany()` method updates all documents that match a given filter condition. It takes the same parameters as the `updateOne()` method, but applies the update to multiple documents. For example:

```js
// Update the status field of all documents with age > 18
db.users.updateMany({age: {$gt: 18}}, {$set: {status: "active"}})
```

- The `replaceOne()` method replaces a single document that matches a given filter condition with a new document. It takes two parameters: a filter object and a replacement object. The filter object specifies the criteria for selecting the document to replace, and the replacement object specifies the new document to insert. For example:

```js
// Replace the document with _id = 2 with a new document
db.users.replaceOne({_id: 2}, {name: "Bob", age: 25, status: "inactive"})
```

- To update documents in MongoDB, you can also use the `db.collection.findAndModify()` method, which combines the functionality of `find()`, `update()`, and `remove()` methods. It takes a query object, an update object, and an optional options object. The query object specifies the criteria for selecting the document to modify, the update object specifies the changes to apply to the document, and the options object specifies additional parameters such as whether to return the original or modified document, whether to sort the documents before updating, and whether to create a new document if none matches the query. For example:

```js
// Find the document with the lowest age and increment it by 1, returning the modified document
db.users.findAndModify({
  query: {},
  update: {$inc: {age: 1}},
  sort: {age: 1},
  new: true
})
```