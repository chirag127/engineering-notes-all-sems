### Immutable Streams Defined from One AnotherTransformations and Aggregations

- In stream processing, a stream is a sequence of data items that are continuously generated over time.
- A stream can be defined from another stream by applying a transformation or an aggregation function.
- A transformation is a function that maps each data item in the input stream to one or more data items in the output stream.
- A transformation can be stateless or stateful. A stateless transformation does not depend on any previous or future data items in the input stream. A stateful transformation maintains some internal state that is updated based on the input stream.
- Examples of stateless transformations are map, filter, flatMap, and union. Examples of stateful transformations are window, join, groupBy, and reduce.
- An aggregation is a function that combines multiple data items in the input stream into a single data item in the output stream.
- An aggregation can be performed over a fixed or a sliding window of the input stream. A window is a subset of the input stream that is defined by a time interval or a number of data items.
- Examples of aggregation functions are sum, count, min, max, and average.