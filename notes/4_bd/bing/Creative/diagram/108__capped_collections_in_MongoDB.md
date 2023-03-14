A capped collection in MongoDB is a fixed-size collection that supports high-throughput operations that insert and retrieve documents based on insertion order. Capped collections work in a way similar to circular buffers: once a collection fills its allocated space, it makes room for new documents by overwriting the oldest documents in the collection .

The following ASCII diagram illustrates the basic architecture of a capped collection in MongoDB:

```
+-----------------+-----------------+-----------------+-----------------+
|                 |                 |                 |                 |
|  Document 1     |  Document 2     |  Document 3     |  Document 4     |
|                 |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
|                 |                 |                 |                 |
|  Document 5     |  Document 6     |  Document 7     |  Document 8     |
|                 |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
|                 |                 |                 |                 |
|  Document 9     |  Document 10    |  Document 11    |  Document 12    |
|                 |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
|                 |                 |                 |                 |
|  Document 13    |  Document 14    |  Document 15    |  Document 16    |
|                 |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
|                 |                 |                 |                 |
|  Document 17    |  Document 18    |  Document 19    |  Document 20    |
|                 |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
|                 |                 |                 |                 |
|  Document 21    |  Document 22    |  Document 23    |  Document 24    |
|                 |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
|                 |                 |                 |                 |
|  Document 25    |  Document 26    |  Document 27    |  Document 28    |
|                 |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
|                 |                 |                 |                 |
|  Document 29    |  Document 30    |  Document 31    |  Document 32    |
|                 |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
|                 |                 |                 |                 |
|  Document 33    |  Document 34    |  Document 35    |  Document 36    |
|                 |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
|                 |                 |                 |                 |
|  Document 37    |  Document 38    |  Document 39    |  Document 40    |
|                 |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
|                 |                 |                 |                 |
|  Document 41    |  Document 42    |  Document 43    |  Document 44    |
|                 |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
|                 |                 |                 |                 |
|  Document 45    |  Document 46    |  Document 47    |  Document 48    |
|                 |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
|                 |                 |                 |                 |
|  Document 49    |  Document 50    |  Document 51    |  Document 52    |
|                 |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
|                 |                 |                 |                 |
|  Document 53    |  Document 54    |  Document 55    |  Document 56    |
|                 |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
|                 |                 |                 |                 |
|  Document 57    |  Document 58    |  Document 59    |  Document 60    |
|                 |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
|                 |                 |                 |