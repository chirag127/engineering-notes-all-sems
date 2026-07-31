### Updating and Deleting Documents in MongoDB

MongoDB provides several methods to update and delete documents within a collection.

#### Updating Documents

- The `updateOne()` method updates a single document that matches the specified filter.
- The `updateMany()` method updates all documents that match the specified filter.
- The `$set` operator is used to update the value of a field.
- The `$inc` operator is used to increment the value of a field by a specified amount.
- The `$push` operator is used to add an element to an array field.

#### Deleting Documents

- The `deleteOne()` method deletes a single document that matches the specified filter.
- The `deleteMany()` method deletes all documents that match the specified filter.

These are some of the basic methods for updating and deleting documents in MongoDB. It is important to carefully construct the filter and update/delete criteria to ensure that the desired documents are updated or deleted.