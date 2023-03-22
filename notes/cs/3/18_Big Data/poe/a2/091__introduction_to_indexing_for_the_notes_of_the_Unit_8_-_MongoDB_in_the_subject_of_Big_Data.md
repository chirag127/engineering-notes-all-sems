 Here is the content in markdown format without any feeling or friendliness:

### Introduction to Indexing for the notes of the Unit 8 - MongoDB in the subject of Big Data.

1. Indexes support the efficient execution of queries in MongoDB.
2. Without indexes, MongoDB must perform a collection scan, i.e. scan every document in a collection to select those documents that match the query statement.
3. Indexes store a small portion of the data set in an easy to traverse form. The index stores the value of a specific field or set of fields, ordered by the value of the field.
4. MongoDB supports indexes on any field or sub-field of the documents. Compound indexes can be created on multiple fields to support efficient queries on multiple fields.
5. The trade-off for indexes is additional storage space and slower writes as the index also needs to be updated with each write operation.
6. MongoDB automatically creates indexes on the _id field during the creation of a collection. The _id index prevents the _id field from being scanned and enables fast equality matches on the _id field.
7. Some important indexes to create include indexes to support sorts, indexes to support frequently used queries, including queries that filter or sort on embedded document fields.
8. Some tools and commands to work with indexes are db.collection.createIndex() to create indexes, db.collection.getIndexes() to list indexes on a collection and db.collection.dropIndex() to drop an index.

The above content is written in a formal tone with points and without any feeling or friendliness as required. The content is written for learning and exam preparation. Let me know if you would like me to modify or add any other points.