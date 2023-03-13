#### Updating Documents in MongoDB

Updating existing documents in a MongoDB database is a common operation when working with data. MongoDB provides various methods to update documents in a collection. In this section, we will discuss the different ways to update documents in MongoDB.

##### The Update Method

The update method is the primary method to update documents in MongoDB. It takes two parameters: a query parameter that specifies which documents to update, and an update parameter that specifies how to update the documents. The update parameter can contain different operators that specify the update operation to perform.

##### Update Operators

MongoDB provides several update operators that can be used to modify documents in a collection. Some of the commonly used update operators are:

- $set: Used to modify the value of a field in a document.
- $unset: Used to remove a field from a document.
- $inc: Used to increment a numeric value of a field.
- $push: Used to append a value to an array field.
- $pull: Used to remove a value from an array field.

##### Updating a Single Document

To update a single document in MongoDB, we use the updateOne() method. This method takes two parameters: a query parameter that specifies the document to update, and an update parameter that specifies how to update the document.

Example:

```
db.collection.updateOne(
   { "name": "John" },
   { $set: { "age": 40 } }
)
```

This will update the age field of the document where the name field is "John".

##### Updating Multiple Documents

To update multiple documents in MongoDB, we use the updateMany() method. This method takes two parameters: a query parameter that specifies which documents to update, and an update parameter that specifies how to update the documents.

Example:

```
db.collection.updateMany(
   { "age": { $lt: 30 } },
   { $inc: { "age": 5 } }
)
```

This will increment the age field of all documents where the age is less than 30.

##### Upsert

The upsert option is used to insert a new document if no documents match the query criteria. To enable upsert, we set the upsert option to true in the update method.

Example:

```
db.collection.updateOne(
   { "name": "John" },
   { $set: { "age": 40 } },
   { upsert: true }
)
```

If no document is found with the name "John", a new document will be inserted with the name "John" and age 40.

##### Learning Tricks

- Remember the common update operators using the mnemonic "SPUP" - Set, Push, Unset, Pull.
- Use the "find and modify" command to perform an update operation in a single atomic transaction. This can be helpful when updating multiple documents and ensuring consistency.