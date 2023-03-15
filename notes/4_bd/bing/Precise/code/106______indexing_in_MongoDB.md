#### Indexing in MongoDB

- MongoDB uses indexing to make query processing more efficient. If there is no indexing, then MongoDB must scan every document in the collection and retrieve only those documents that match the query.
- Indexes are special data structures that store information related to the documents, making it easier for MongoDB to find the right data file. The indexes are ordered by the value of the field specified in the index.
- MongoDB provides a method called `createIndex()` that allows the user to create an index.
- MongoDB supports various types of indexes, including single field, compound, and multikey indexes.
- Multikey indexes are used to index the content stored in arrays. If you index a field that holds an array value, MongoDB creates separate index entries for every element of the array.