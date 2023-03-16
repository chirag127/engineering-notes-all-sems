### Immutable Streams Defined from One AnotherTransformations and Aggregations

- In stream processing, a stream is a sequence of immutable data records that are continuously produced and consumed.
- A stream can be defined from another stream by applying transformations and aggregations on the data records.
- Transformations are operations that change the content or structure of the data records in a stream, such as filtering, mapping, joining, splitting, etc.
- Aggregations are operations that combine multiple data records in a stream into a single value, such as counting, summing, averaging, etc.
- Transformations and aggregations can be applied in different ways, such as stateless, stateful, windowed, or incremental.
- Stateless transformations and aggregations do not depend on any previous or future data records in the stream, and can be applied independently on each record.
- Stateful transformations and aggregations depend on some state information that is derived from previous or future data records in the stream, and can be applied only when the state is updated.
- Windowed transformations and aggregations divide the stream into finite segments called windows, and apply the operations on each window separately. Windows can be defined by time, count, or session.
- Incremental transformations and aggregations update the result of the operations as new data records arrive in the stream, and avoid recomputing the entire result from scratch.