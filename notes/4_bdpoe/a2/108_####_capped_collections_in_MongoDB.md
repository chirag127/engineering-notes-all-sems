 Here is the content in markdown format for the topic #### capped collections in MongoDB:

#### Capped Collections in MongoDB
Capped collections are fixed-size collections in MongoDB that support high throughput operations. Some key points about capped collections are:

- Once a capped collection reaches its maximum size, it will override the oldest documents with new ones. This is useful for storing recently accumulated data like logs.
- Capped collections maintain insertion order, i.e. documents are inserted and retrieved in the same order. This makes them efficient for storing chronological data.
- Capped collections do not support indexing.
- Capped collections are best suited for frequently written, time-series data where you don't need to preserve all entries or run sorts and range queries.

**Mnemonics**:
- Capped collections are like logs - newest entries override oldest
- Insertion order is maintained - great for time-series data
- No indexing - high throughput, not suited for complex queries

**Learning Tricks**:
- Think of capped collections as circular buffers that are useful for storing recent data and time-series data.
- The name 'capped' comes from the fact that the size is capped/limited. Once the limit is reached, old data is overwritten.
- Remember that insertion order is maintained but no indexing is supported. This lends capped collections to high throughput use cases.

**Examples and Applications**:
- Storing server logs
- Time series data and metrics
- Temporary data caching

Overall, capped collections are ideal for use cases requiring high throughput and involving frequently appended data where maintaining the most recent data is a priority and complex queries are not needed. The limitations around size, indexing and overwriting old data make sense for such use cases and allow for optimal performance.