#### Updating Documents in MongoDB

MongoDB provides several methods to update documents in a collection. Here are some key points to remember when updating documents in MongoDB:

1. The `updateOne()` method updates a single document that matches the specified filter.
2. The `updateMany()` method updates all documents that match the specified filter.
3. The `$set` operator is used to update the value of a field in a document.
4. The `$inc` operator is used to increment the value of a field in a document.
5. The `$push` operator is used to add an element to an array field in a document.
6. The `$pull` operator is used to remove an element from an array field in a document.
7. The `upsert` option can be used to insert a new document if no document matches the specified filter.
8. The `multi` option can be used to update multiple documents that match the specified filter.
