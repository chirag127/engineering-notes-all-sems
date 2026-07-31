### Immutable Streams Defined from One Another Transformations and Aggregations

- Stream processing is the execution of continuous computations over unbounded streams of events.
- Streams are immutable, append-only collections that can represent a series of historical facts or see data in motion.
- Tables are mutable collections that represent the latest version of each value per key.
- Streams and tables can be defined from one another using transformations and aggregations.
- Transformations are operations that change the structure or content of a stream or a table, such as map, filter, join, etc.
- Aggregations are operations that group and summarize a stream or a table by a key, such as count, sum, average, etc.
- Window aggregations are a special type of aggregations that divide a stream or a table into finite time intervals, called windows, and compute aggregates for each window.
- There are different types of windows, such as tumbling, hopping, sliding, and session windows.
- Tumbling windows are fixed-size, non-overlapping windows that cover the entire stream or table.
- Hopping windows are fixed-size, overlapping windows that advance by a fixed hop size.
- Sliding windows are variable-size, overlapping windows that are defined by a start and end time for each event.
- Session windows are variable-size, non-overlapping windows that are defined by a session gap, which is the maximum allowed inactivity time between events.

: https://www.confluent.io/blog/stream-processing-ultimate-guide/
: https://www.baeldung.com/java-kafka-streams-vs-kafka-consumer
: https://ksqldb.io/