### Updating and Deleting Documents in MongoDB

MongoDB is a document-oriented database that stores data in collections of JSON-like documents. MongoDB provides various methods to update and delete documents from a collection.

#### Updating Documents

To update a document, MongoDB provides update operators, such as `$set`, `$inc`, `$push`, etc., to modify field values. To use the update operators, pass to the update methods an update document of the form:

```
{ <operator1>: { <field1>: <value1>, ... },
  <operator2>: { <field2>: <value2>, ... },
  ...
}
```

Some of the update methods are:

- `db.collection.updateOne(filter, update, options)`: Updates a single document that matches the filter condition.
- `db.collection.updateMany(filter, update, options)`: Updates all documents that match the filter condition.
- `db.collection.replaceOne(filter, replacement, options)`: Replaces a single document that matches the filter condition with the replacement document.
- `db.collection.findOneAndUpdate(filter, update, options)`: Finds a single document that matches the filter condition and updates it. Returns the original or updated document.

For example, to update the `price` field of the document with `_id` equal to `1` in the `products` collection, you can use the following command:

```
db.products.updateOne({ _id: 1 }, { $set: { price: 9.99 } })
```

#### Deleting Documents

To delete a document, MongoDB provides delete operators, such as `$unset`, `$pull`, etc., to remove field values. To use the delete operators, pass to the delete methods a delete document of the form:

```
{ <operator1>: { <field1>: <value1>, ... },
  <operator2>: { <field2>: <value2>, ... },
  ...
}
```

Some of the delete methods are:

- `db.collection.deleteOne(filter, options)`: Deletes a single document that matches the filter condition.
- `db.collection.deleteMany(filter, options)`: Deletes all documents that match the filter condition.
- `db.collection.findOneAndDelete(filter, options)`: Finds a single document that matches the filter condition and deletes it. Returns the deleted document.

For example, to delete the document with `_id` equal to `1` from the `products` collection, you can use the following command:

```
db.products.deleteOne({ _id: 1 })
```