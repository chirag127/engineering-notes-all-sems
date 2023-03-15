#### Deleting Documents in MongoDB

MongoDB provides several methods to delete documents from a collection:

1. `deleteOne()`: This method deletes a single document that matches the specified filter.
2. `deleteMany()`: This method deletes all documents that match the specified filter.
3. `findOneAndDelete()`: This method finds a single document that matches the specified filter and deletes it, returning the deleted document.

Here is an example of how to use the `deleteOne()` method to delete a document from a collection:

```javascript
db.collection.deleteOne({ name: "John" });
```

This command will delete the first document in the collection where the `name` field is equal to "John".

Similarly, here is an example of how to use the `deleteMany()` method to delete multiple documents from a collection:

```javascript
db.collection.deleteMany({ age: { $lt: 18 } });
```

This command will delete all documents in the collection where the `age` field is less than 18.

Finally, here is an example of how to use the `findOneAndDelete()` method to find and delete a document from a collection:

```javascript
db.collection.findOneAndDelete({ name: "Jane" });
```

This command will find the first document in the collection where the `name` field is equal to "Jane" and delete it, returning the deleted document.

It is important to note that when deleting documents from a collection, any indexes associated with the deleted documents will also be removed. Additionally, if the collection is capped, the `deleteOne()` and `deleteMany()` methods will not work and an error will be returned. In this case, the `findOneAndDelete()` method can be used instead.