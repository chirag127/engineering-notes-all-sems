### Updating and Deleting Documents in MongoDB

MongoDB provides several methods for updating and deleting documents within a collection.

#### Updating Documents

1. The `updateOne()` method updates a single document that matches the specified filter. The method takes two arguments: a filter document to match the document to update, and an update document that specifies the modifications to make.
2. The `updateMany()` method updates all documents that match the specified filter. Like `updateOne()`, it takes a filter document and an update document as arguments.
3. The `replaceOne()` method replaces a single document that matches the specified filter. It takes a filter document and a replacement document as arguments.

#### Deleting Documents

1. The `deleteOne()` method deletes a single document that matches the specified filter. It takes a filter document as its only argument.
2. The `deleteMany()` method deletes all documents that match the specified filter. Like `deleteOne()`, it takes a filter document as its only argument.

These methods provide a flexible and powerful way to update and delete documents in a MongoDB collection. It is important to carefully construct the filter and update/replacement documents to ensure that the desired changes are made.