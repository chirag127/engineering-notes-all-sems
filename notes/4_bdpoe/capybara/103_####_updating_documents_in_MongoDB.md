#### Updating Documents in MongoDB

Updating documents in MongoDB is a crucial operation that allows you to modify the data stored in the database. The update operation can be used to add, modify or remove fields in a document. In this section, we will discuss the different ways you can update documents in MongoDB.

##### Updating Documents Using updateOne()

The `updateOne()` method is used to update a single document that matches a specific filter. Here's the syntax for the `updateOne()` method:

```
db.collection.updateOne(filter, update, options)
```

* `filter`: Specifies which document to update.
* `update`: Specifies the modifications to apply.
* `options`: Specifies additional options such as upsert and write concern.

##### Updating Documents Using updateMany()

The `updateMany()` method is used to update multiple documents that match a specific filter. Here's the syntax for the `updateMany()` method:

```
db.collection.updateMany(filter, update, options)
```

* `filter`: Specifies which documents to update.
* `update`: Specifies the modifications to apply.
* `options`: Specifies additional options such as upsert and write concern.

##### Updating Documents Using $set Operator

The `$set` operator is used to modify the value of a field in a document. Here's an example:

```
db.collection.updateOne({ _id: ObjectId("5d8b8e9a87c9e63172d0b8e1") }, { $set: { name: "John Doe" } })
```

This query updates the value of the `name` field to "John Doe" in a document with the specified `_id`.

##### Updating Documents Using $unset Operator

The `$unset` operator is used to remove a field from a document. Here's an example:

```
db.collection.updateOne({ _id: ObjectId("5d8b8e9a87c9e63172d0b8e1") }, { $unset: { age: "" } })
```

This query removes the `age` field from a document with the specified `_id`.

##### Upsert

If the document specified in the `filter` parameter is not found, the `updateOne()` and `updateMany()` methods will not make any changes to the collection. However, you can use the `upsert` option to insert a new document if the filter does not match any documents. Here's an example:

```
db.collection.updateOne({ name: "John Doe" }, { $set: { age: 30 } }, { upsert: true })
```

##### Learning Trick

Remember the following points while updating documents in MongoDB:

* Use the `updateOne()` method to update a single document that matches a specific filter.
* Use the `updateMany()` method to update multiple documents that match a specific filter.
* Use the `$set` operator to modify the value of a field in a document.
* Use the `$unset` operator to remove a field from a document.
* Use the `upsert` option to insert a new document if the filter does not match any documents.

By following these points, you can easily update documents in MongoDB.