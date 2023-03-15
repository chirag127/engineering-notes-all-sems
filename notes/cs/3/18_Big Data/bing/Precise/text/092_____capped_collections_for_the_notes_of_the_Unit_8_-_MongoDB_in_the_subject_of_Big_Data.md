### Capped Collections

- Capped collections are fixed-size collections that maintain insertion order.
- They are created using the `createCollection` command with the `capped` option set to `true`.
- The size of the capped collection is specified in bytes and must be large enough to hold at least one document.
- Once the size limit is reached, the oldest documents are automatically removed to make room for new documents.
- Capped collections are ideal for storing log data or other time-sensitive information.
- They support high-throughput operations and can be used with tailable cursors to create real-time data processing systems.
- Capped collections do not support the `remove` operation, but documents can be updated as long as the update does not increase the size of the document.
- Capped collections can be converted to regular collections by setting the `capped` option to `false` using the `collMod` command.
