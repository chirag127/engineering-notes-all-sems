### Introduction to Indexing

- Indexing is a technique that improves the performance of queries in MongoDB by creating data structures that store a subset of the document fields in a sorted order.
- Indexes can be created on one or more fields of a collection, and can support various types of queries, such as exact matches, range queries, text searches, geospatial queries, etc.
- Indexes can also enforce uniqueness constraints on the indexed fields, preventing duplicate values from being inserted or updated in the collection.
- Indexes are stored in a special collection called `system.indexes`, which is hidden from the user. Each index document in this collection contains the name, namespace, key specification, and other options of the index.
- MongoDB provides several types of indexes, such as:

  - Single field index: an index on a single field of a document.
  - Compound index: an index on multiple fields of a document, where the order of the fields matters.
  - Multikey index: an index on an array field or a field that contains subdocuments, where each element or subfield is indexed as a separate value.
  - Text index: an index that supports text search queries on string fields of a document, using a language-specific analyzer and a set of stop words.
  - Hashed index: an index that hashes the values of the indexed field and stores the hash values in the index, enabling equality matches on the hashed field.
  - Geospatial index: an index that supports geospatial queries on geospatial data types, such as points, lines, polygons, etc.
  - TTL index: an index that automatically deletes documents from a collection after a specified amount of time, based on a date field or an expiration expression.
  - Sparse index: an index that only includes documents that have the indexed field, omitting documents that do not have the field or have a null value for the field.
  - Partial index: an index that only includes documents that match a specified filter expression, reducing the index size and improving the query efficiency.
  - Unique index: an index that ensures that the indexed fields do not have any duplicate values in the collection, except for null values, which are allowed by default.
  - Background index: an index that is built in the background, without blocking other database operations.