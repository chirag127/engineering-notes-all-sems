
#### Capped Collections in MongoDB

1. Capped collections are a fixed-size collections that provide high performance for data that has a natural expiration date.
2. Capped collections have a maximum size, and once the maximum size is reached, MongoDB removes the oldest documents to make space for new documents.
3. Capped collections are ideal for storing events and logs, as well as for implementing a queue.
4. To create a capped collection, use the `createCollection()` method with the `capped` option set to `true`:
    ```
    db.createCollection("mycollection", { capped: true, size: <size in bytes> });
    ```
5. To retrieve documents from a capped collection, use the `find()` method.
6. To delete documents from a capped collection, use the `remove()` method.
7. To update documents in a capped collection, use the `update()` method.
8. Capped collections are not supported in sharded clusters.