### Sharding

Sharding is a method of splitting and storing a single logical dataset in multiple databases. By distributing the data among multiple machines, a cluster of database systems can store larger datasets and handle additional requests. Sharding is necessary when a dataset is too large to be stored in a single database.

Here are some key points to remember about sharding:

1. Sharding involves breaking up a large dataset into smaller, more manageable parts called shards.
2. Each shard is stored on a separate database server, known as a shard or node.
3. Sharding can improve the performance and scalability of a database system.
4. Sharding can be done either horizontally or vertically. Horizontal sharding involves splitting a table by rows, while vertical sharding involves splitting a table by columns.
5. Sharding requires a way to determine which shard a particular piece of data should be stored on. This is typically done using a sharding key or a sharding function.
6. Sharding can add complexity to a database system, as it requires additional logic to route queries to the correct shard and to reassemble results from multiple shards.
