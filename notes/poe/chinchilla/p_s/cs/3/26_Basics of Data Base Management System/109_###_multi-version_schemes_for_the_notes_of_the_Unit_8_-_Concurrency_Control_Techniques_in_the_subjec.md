### Multi-Version Schemes for the notes of the Unit 8 - Concurrency Control Techniques in the subject of Basics of Data Base Management System

Concurrency control is an essential aspect of database management systems. It ensures that multiple users can access and modify the database concurrently without causing inconsistencies in the data. Multi-version schemes are one of the techniques used for concurrency control. In this section, we will discuss multi-version schemes in detail.

#### What are Multi-Version Schemes?

Multi-version schemes are concurrency control techniques that allow multiple versions of a data item to coexist in the database. Each version of the data item is assigned a unique timestamp or version number. When a transaction accesses a data item, it reads the version that existed at the time it started. If the transaction modifies the data item, it creates a new version with a new timestamp or version number.

#### Advantages of Multi-Version Schemes

- Multi-version schemes provide high concurrency and scalability as multiple transactions can access the database simultaneously.
- They provide a high level of isolation as each transaction works on a separate version of the data item.
- They ensure that read-only transactions do not block write transactions.
- They prevent cascading rollbacks as each transaction works on a separate version of the data item.

#### Disadvantages of Multi-Version Schemes

- Multi-version schemes require more storage space as multiple versions of the same data item are stored in the database.
- They may cause performance degradation due to the overhead of managing multiple versions of the data item.

#### Examples of Multi-Version Schemes

- Snapshot Isolation: In snapshot isolation, each transaction reads a snapshot of the database at the time it started. The snapshot consists of all the versions of the data items that existed at that time. If the transaction modifies a data item, it creates a new version with a new timestamp.
- Multi-Version Concurrency Control (MVCC): In MVCC, each transaction reads a version of the data item that existed at the time it started. If the transaction modifies the data item, it creates a new version with a new timestamp. The database keeps track of all the versions of the data item and ensures that transactions only access the appropriate version.

#### Applications of Multi-Version Schemes

Multi-version schemes are commonly used in database management systems that require high concurrency and scalability. They are used in systems such as e-commerce websites, online banking, and social media platforms.

In conclusion, multi-version schemes are an effective way of ensuring concurrency control in database management systems. They provide high concurrency, isolation, and prevent cascading rollbacks. However, they may require more storage space and cause performance degradation. Understanding multi-version schemes is essential for anyone working with database management systems.