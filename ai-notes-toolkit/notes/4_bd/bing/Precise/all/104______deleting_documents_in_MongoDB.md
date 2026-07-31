#### Deleting Documents in MongoDB

MongoDB provides several methods to delete documents from a collection:

1. `deleteOne()`: This method deletes a single document that matches the specified filter. If multiple documents match the filter, only the first document is deleted.

2. `deleteMany()`: This method deletes all documents that match the specified filter.

3. `findOneAndDelete()`: This method finds a single document that matches the specified filter, deletes it, and returns the deleted document.

Here is an example of how to use the `deleteOne()` method to delete a document from a collection:

```javascript
db.collectionName.deleteOne({field: value})
```

In this example, `collectionName` is the name of the collection from which you want to delete the document, `field` is the name of the field you want to use to filter the documents, and `value` is the value of the field that the document must have to be deleted.

It is important to note that deleting documents from a collection is a permanent action and cannot be undone. Therefore, it is recommended to use caution when deleting documents from a collection.