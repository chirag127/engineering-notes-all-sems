### Structured Streaming Processing Model

- The key idea in Structured Streaming is to treat a live data stream as a table that is being continuously appended.
- This leads to a new stream processing model that is very similar to a batch processing model.
- You can express your streaming computation the same way you would express a batch computation on static data.
- In Structured Streaming, you express your streaming computation as a standard batch-like query as on a static table, but Spark runs it as an incremental query on the unbounded input table.
- Structured Streaming is a scalable and fault-tolerant stream processing engine built on the Spark SQL engine.