 Here is the formal write-up on capped collections in MongoDB in Markdown format:

#### Capped Collections in MongoDB

- Capped collections are fixed-size collections that support high-throughput operations that retrieve documents in insertion order.
- Once a capped collection reaches its maximum size, MongoDB will remove the oldest documents to make space for new ones. This makes capped collections well-suited for storing log data or as a rotating buffer.
- Capped collections have the following characteristics:
    - Fixed size - When a capped collection is created, you specify a maximum size for the collection. Once the collection reaches this maximum size, MongoDB will remove the oldest documents to make space for new ones.
    - Have an insertion order - Documents in a capped collection are always returned in the order in which they were inserted. This ordering can be useful for time-series data or queued processing.
    - Support efficient retrieval - Retrieving documents from the beginning or end of a capped collection is very efficient. This is useful for accessing the most recent log entries or the oldest ones.
- To create a capped collection, pass the capped boolean and a maximum value in bytes for the size parameter in db.createCollection(). For example:
    db.createCollection("logs", { capped: true, size: 10000 })

- This creates a capped collection called "logs" with a maximum size of 10000 bytes.
- Capped collections are well-suited for storing log or time-series data where new records are continually inserted and the older ones are discarded. The insertion ordering and efficient retrieval of first/last documents make capped collections ideal for this use case.