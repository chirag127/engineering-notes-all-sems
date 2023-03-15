

#### Capped Collections in MongoDB

- Capped collections are fixed-size collections that maintain insertion order and support high-throughput operations. 
- They are useful for storing data that needs to be accessed in a FIFO (first-in, first-out) manner, such as logs and other time-based data. 
- Capped collections have a maximum size, and once they reach that size, they automatically overwrite the oldest data. 
- Capped collections are created using the `createCollection` command, which takes an additional `capped` option. 
- When creating a capped collection, you must specify the maximum size in bytes, as well as the maximum number of documents that the collection can hold. 
- Capped collections are useful for storing data that needs to be accessed in a FIFO (first-in, first-out) manner, such as logs and other time-based data. 
- They also provide performance benefits, as they are stored in a contiguous block of memory and do not require frequent compaction. 
- Capped collections are also useful for maintaining a fixed-size cache of recent documents. 
- Capped collections are read-only, meaning that documents cannot be updated or deleted. 
- Capped collections are also not indexed, meaning that queries must be done using the `$natural` operator. 
- Additionally, capped collections do not support the `$push` and `$pull` operators. 
- Capped collections are ideal for storing data that needs to be accessed in a FIFO (first-in, first-out) manner, such as logs and other time-based data.