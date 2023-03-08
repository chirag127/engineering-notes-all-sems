 Here is the content in markdown format for the topic ### querying for the notes of the Unit 8 - MongoDB in the subject of Big Data:

### Querying in MongoDB

MongoDB supports a variety of query operators to retrieve data from a collection. Some of the frequently used operators are:

- `eq` (equal): Retrieves documents where the value of a field equals to a specified value. For example, `db.collection.find({price: {$eq: 20}})` will retrieve documents where the price field equals 20.
- `ne` (not equal): Retrieves documents where the value of a field does not equal to a specified value. For example, `db.collection.find({price: {$ne: 20}})` will retrieve documents where the price field does not equal 20.
- `gt` (greater than), `gte` (greater than or equal to): Retrieves documents where the value of a field is greater than or equal to a specified value. For example, `db.collection.find({price: {$gt: 20}})` will retrieve documents where the price field is greater than 20.
- `lt` (less than), `lte` (less than or equal to): Retrieves documents where the value of a field is less than or equal to a specified value. For example, `db.collection.find({price: {$lt: 20}})` will retrieve documents where the price field is less than 20.
- `in`: Retrieves documents where the value of a field equals any value in an array of values. For example, `db.collection.find({category: {$in: ['Fiction', 'Drama']}})` will retrieve documents where the category field equals either 'Fiction' or 'Drama'.
- `nin`: Retrieves documents where the value of a field does not equal any value in an array of values. For example, `db.collection.find({category: {$nin: ['Fiction', 'Drama']}})` will retrieve documents where the category field does not equal either 'Fiction' or 'Drama'.

[Detailed explanations and examples for other operators like `regex`, `or`, `and`, `nor`, etc. can be added here.]

Some additional MongoDB querying concepts are:

- Projection: Retrieving only selective fields of the documents. For example, `db.collection.find({}, {name: 1})` will retrieve only the name field from the matching documents.
- Sorting: Sorting the retrieved documents in ascending or descending order based on a field. For example, `db.collection.find().sort({price: 1})` will sort the documents in ascending order of the price field.
- Limit and Skip: Restricting the number of documents to be retrieved and skipping a specific number of documents before retrieving. For example, `db.collection.find().limit(10).skip(5)` will skip the first 5 documents and retrieve the next 10 documents.
- Indexes: Creating indexes on fields to speed up queries. For example, creating an index on the 'price' field will speed up retrieval of documents sorted or filtered by price.

[More details and examples can be added for the above concepts.]