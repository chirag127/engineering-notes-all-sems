#### Indexing in MongoDB

- MongoDB uses indexing to make query processing more efficient. If there is no indexing, then MongoDB must scan every document in the collection and retrieve only those documents that match the query.
- Indexes are special data structures that store information related to the documents, making it easier for MongoDB to find the right data file. The indexes are ordered by the value of the field specified in the index.
- MongoDB provides a method called `createIndex()` that allows users to create an index.
- MongoDB has its ways of implementing indexing and offers various types. In MongoDB, we use the `createIndex` function to create an index and the `dropIndex` function to drop the index.
- MongoDB uses multikey indexes to index the content stored in arrays. If you index a field that holds an array value, MongoDB creates separate index entries for every element of the array. These multikey indexes allow queries to select documents that contain arrays by matching on element or elements of the arrays.
- MongoDB supports the creation of user-defined indexes on multiple fields, i.e. compound indexes. The order of the fields listed in a compound index is important.