#### Deleting Documents in MongoDB

MongoDB provides several methods to delete documents from a collection:

1. **deleteOne()**: This method deletes a single document that matches the specified filter. If multiple documents match the filter, only the first document is deleted.

2. **deleteMany()**: This method deletes all documents that match the specified filter.

3. **findOneAndDelete()**: This method finds a single document that matches the specified filter and deletes it. It also returns the deleted document.

Here is an example of how to use the `deleteOne()` method to delete a document from a collection:

```javascript
db.collectionName.deleteOne({ field: value });
```

In this example, `collectionName` is the name of the collection from which you want to delete the document, and `{ field: value }` is the filter that specifies the document to delete.

Similarly, you can use the `deleteMany()` method to delete multiple documents from a collection:

```javascript
db.collectionName.deleteMany({ field: value });
```

And you can use the `findOneAndDelete()` method to find and delete a single document from a collection:

```javascript
db.collectionName.findOneAndDelete({ field: value });
```

It is important to note that deleting documents from a collection is a permanent action and cannot be undone. Therefore, it is recommended to use caution when deleting documents from a collection.