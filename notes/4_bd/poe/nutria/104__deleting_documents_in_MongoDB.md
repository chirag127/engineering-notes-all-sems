

#### Deleting Documents in MongoDB

1. To delete a single document in MongoDB, you can use the `deleteOne()` method. This method takes a query object to specify the document to delete.

2. To delete multiple documents, you can use the `deleteMany()` method. This method takes a query object to specify the documents to delete.

3. To delete all documents from a collection, you can use the `drop()` method. This method will delete all documents from the collection, and will also delete the indexes associated with the collection.

4. It is important to note that all of these methods are permanent and cannot be undone. It is always best practice to create a backup of your data before deleting documents.