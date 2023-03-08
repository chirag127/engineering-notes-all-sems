 Here is the content in markdown format:

#### Creating documents in MongoDB

- To create a document in MongoDB, you need to insert a record (document) into a collection.
- A document in MongoDB is a record in a collection and is composed of field and value pairs.
- The fields can be thought of as columns in a table and the values as the corresponding rows.
- To insert a document into a collection, you use the insertOne() or insertMany() methods.
- insertOne() inserts a single document into a collection. The syntax is:
db.collection.insertOne(document)
- insertMany() inserts an array of documents into a collection. The syntax is:
db.collection.insertMany([document1, document2, ...])
- Examples:
db.products.insertOne({item: "tennis ball", price: 2.50, quantity: 250})
db.products.insertMany([{item: "tennis racket", price: 25, quantity: 50}, {item: "ball carton", price: 15, quantity: 100}])
- The insert methods return an acknowledgment from the MongoDB server of the success/failure of the insertion.
- If the insert is successful, a document containing the _id of the inserted document(s) is returned.
- Advantages:
-- Flexible schema: In MongoDB, you can add fields on the fly and different documents in the same collection can have different fields.
-- Scalability: MongoDB scales horizontally easily by adding more servers in the replica set.
-- High performance: MongoDB is designed to provide high performance with large amounts of data and high throughput.
- Disadvantages:
-- Less support for JOINS: MongoDB supports only left outer joins, leading to limited query capabilities.
-- Schema validation: Although the flexible schema is an advantage, it may lead to issues with data consistency if not properly designed.
-- Complex architecture: MongoDB has a complex architecture with several components leading to a steep learning curve.