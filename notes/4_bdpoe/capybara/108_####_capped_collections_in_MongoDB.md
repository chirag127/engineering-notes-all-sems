#### Capped Collections in MongoDB

Capped collections are a type of collection in MongoDB that have a fixed size and maintain insertion order. Once the collection reaches its maximum size, older documents are overwritten by new ones. This makes capped collections ideal for storing data that has a high turnover rate, such as logs or sensor data.

##### Creating a Capped Collection

To create a capped collection in MongoDB, you need to specify the maximum size and, optionally, the maximum number of documents it can hold. You can use the `db.createCollection()` method with the `capped` option set to `true`.

Example:

```
db.createCollection("logs", {
   capped: true,
   size: 100000
})
```

In this example, we create a capped collection named `logs` with a maximum size of `100000` bytes.

##### Advantages of Capped Collections

- Capped collections are efficient for storing data with a high turnover rate, as they prevent the collection from growing indefinitely and overwhelming the system.
- Capped collections maintain insertion order, making it easy to retrieve data in the order it was added.
- Capped collections can be used for tailable cursors, which allow you to retrieve new data as it is added to the collection.

##### Disadvantages of Capped Collections

- Capped collections have a fixed size, so they may not be suitable for storing data that needs to be retained for a long time.
- Overwriting old documents can lead to data loss if you need to retrieve information that was overwritten.
- Capped collections do not support updates that increase the size of a document. If you need to update a document, you must replace it entirely.

##### Mnemonic

One possible mnemonic for remembering capped collections in MongoDB is "CAP it and FORget it." This phrase emphasizes the idea that capped collections are designed for storing data that can be overwritten and forgotten once it has served its purpose.