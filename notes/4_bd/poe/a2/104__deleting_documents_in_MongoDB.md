 Here is the content in markdown format with formal tone and without any emojis or external links:

#### Deleting documents in MongoDB

1. Use the deleteOne() method to delete a single document that matches a filter.
Syntax: db.collection.deleteOne(filter)
Example: db.collection.deleteOne({name: 'John'})

2. Use the deleteMany() method to delete multiple documents that match a filter.
Syntax: db.collection.deleteMany(filter)
Example: db.collection.deleteMany({price: {$lt: 20}})

3. Remove all documents from a collection using remove().
Syntax: db.collection.remove({})

4. Delete documents in a bulk using bulk.execute().
Syntax:
bulk = db.collection.initializeUnorderedBulkOperation()
bulk.find({name: 'John'}).deleteOne()
bulk.find({name: 'Alice'}).deleteMany()
bulk.execute()

The above methods are used to delete documents from a MongoDB collection. Proper filters should be used to selectively delete required documents. Bulk operations can be used to perform deletion of multiple documents in an efficient manner.