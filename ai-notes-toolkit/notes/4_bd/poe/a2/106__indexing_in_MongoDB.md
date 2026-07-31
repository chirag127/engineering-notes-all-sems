 Here is the formal content on the topic 'Indexing in MongoDB' in markdown format:

#### Indexing in MongoDB

1. Indexes support the efficient execution of queries in MongoDB. They can significantly speed up read operations and are useful for supporting certain queries.
2. Without indexes, MongoDB must perform a collection scan, i.e. scan every document in a collection to select those documents that match the query statement. If an appropriate index exists for a query, MongoDB can use the index to directly access the documents it needs, resulting in much faster performance.
3. Indexes are stored separately from the collection's documents and consume additional space in the database. However, they provide benefits in terms of performance and efficiency which can outweigh the additional storage space required in most cases.
4. The MongoDB query optimizer automatically chooses which index to use for a query out of the available indexes, based on each index's design and the query pattern. However, manually creating additional appropriate indexes is important to ensure efficient querying performance as the database grows in size and usage.
5. The MongoDB indexing functionality supports indexes on any field or sub-field of the documents in a MongoDB collection. This includes nested fields/arrays. Compound indexes can also be created to support efficient execution of queries on multiple fields.
6. The three main types of indexes in MongoDB are:
- Single Field Index: Indexes a single field in a document.
- Compound Index: Indexes two or more fields in a document.
- Multikey Index: Indexes on arrays or nested documents.

Does this satisfy your requirements? Let me know if you would like me to modify or expand the content in any way.