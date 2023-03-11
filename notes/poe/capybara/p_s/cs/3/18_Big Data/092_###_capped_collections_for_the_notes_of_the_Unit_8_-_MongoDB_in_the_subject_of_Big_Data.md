### Capped Collections

Capped collections are special collections in MongoDB that have a fixed size and follow a specific insertion order. They are useful for storing data that has a limited lifespan, such as log data or sensor data, where old data can be discarded to make room for new data.

#### Creating Capped Collections

To create a capped collection, you can use the `createCollection()` method with the `capped` option set to true, along with the `size` option to specify the maximum size of the collection:

```
db.createCollection("myCappedCollection", { capped: true, size: 1000000 })
```

This will create a capped collection named `myCappedCollection` with a maximum size of 1 MB.

#### Limitations of Capped Collections

While capped collections have some advantages, they also have some limitations:

- Once a capped collection is created, its size cannot be changed.
- Documents in a capped collection cannot be updated, only inserted or deleted.
- Capped collections do not support indexes on fields other than the `_id` field.
- Capped collections do not support the `$natural` sort order.

#### Advantages of Capped Collections

Despite their limitations, capped collections have some advantages:

- Capped collections are efficient for storing a large volume of data that has a limited lifespan, such as log data or sensor data.
- Capped collections can be used as a buffer to store data temporarily before it is moved to a permanent storage location.
- Capped collections are useful for implementing a FIFO (First-In-First-Out) data structure.

#### Example

Here is an example of creating a capped collection and inserting documents into it:

```
db.createCollection("myCappedCollection", { capped: true, size: 1000000 })

for (var i = 1; i <= 1000; i++) {
    db.myCappedCollection.insert({ "value": i })
}
```

This will create a capped collection named `myCappedCollection` with a maximum size of 1 MB, and insert 1000 documents into it with a `value` field ranging from 1 to 1000.

#### Applications

Capped collections are commonly used for:

- Storing log data
- Storing sensor data
- Storing real-time data
- Implementing a FIFO data structure.