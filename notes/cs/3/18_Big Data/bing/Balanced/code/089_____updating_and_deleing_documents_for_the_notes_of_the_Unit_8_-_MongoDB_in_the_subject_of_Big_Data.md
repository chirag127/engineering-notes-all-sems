### Updating and Deleting Documents in MongoDB

MongoDB is a document-oriented database that stores data in collections of JSON-like documents. To manipulate the data in MongoDB, we can use various methods to insert, update, and delete documents.

#### Updating Documents

- To update a document, we need to specify a filter condition that matches the document we want to modify, and an update document that specifies the new values for the fields we want to change.
- MongoDB provides update operators, such as `$set`, `$inc`, `$push`, etc., to modify the field values in the update document.
- MongoDB also provides update methods, such as `db.collection.updateOne()`, `db.collection.updateMany()`, and `db.collection.replaceOne()`, to perform different types of update operations on the matched documents.
- For example, to update the price field of a document with the _id field equal to 100 in the products collection, we can use the following command:

```js
db.products.updateOne(
  { _id: 100 }, // filter condition
  { $set: { price: 9.99 } } // update document
)
```

- To update multiple documents that match a filter condition, we can use the `db.collection.updateMany()` method. For example, to increase the price of all the documents with the category field equal to "books" in the products collection by 10%, we can use the following command:

```js
db.products.updateMany(
  { category: "books" }, // filter condition
  { $mul: { price: 1.1 } } // update document
)
```

- To replace an entire document with a new one, we can use the `db.collection.replaceOne()` method. For example, to replace the document with the _id field equal to 100 in the products collection with a new document, we can use the following command:

```js
db.products.replaceOne(
  { _id: 100 }, // filter condition
  { name: "New Product", price: 19.99, category: "electronics" } // new document
)
```

#### Deleting Documents

- To delete a document, we need to specify a filter condition that matches the document we want to remove.
- MongoDB provides delete methods, such as `db.collection.deleteOne()`, `db.collection.deleteMany()`, and `db.collection.drop()`, to perform different types of delete operations on the matched documents.
- For example, to delete the document with the _id field equal to 100 in the products collection, we can use the following command:

```js
db.products.deleteOne(
  { _id: 100 } // filter condition
)
```

- To delete multiple documents that match a filter condition, we can use the `db.collection.deleteMany()` method. For example, to delete all the documents with the category field equal to "books" in the products collection, we can use the following command:

```js
db.products.deleteMany(
  { category: "books" } // filter condition
)
```

- To delete all the documents and the collection itself, we can use the `db.collection.drop()` method. For example, to delete the products collection, we can use the following command:

```js
db.products.drop()
```