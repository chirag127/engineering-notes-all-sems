The following diagram illustrates the basic architecture of a comparison of methods for concurrency control for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM.

```
+-------------------------+-------------------------+-------------------------+-------------------------+
| Two-phase locking       | Timestamp ordering      | Multiversion            | Validation              |
| Protocol                | Protocol                | Concurrency Control     | Concurrency Control     |
+-------------------------+-------------------------+-------------------------+-------------------------+
| Locking is an operation | A timestamp is a tag    | Multiversion schemes    | The optimistic approach |
| which secures:          | that can be attached to | keep old versions of    | is based on the         |
| permission to read, OR  | any transaction or any  | data item to increase   | assumption that the     |
| permission to write a   | data item, which        | concurrency.            | majority of the         |
| data item.              | denotes a specific time |                         | database operations do  |
|                         | on which the            |                         | not conflict.           |
|                         | transaction or the data |                         |                         |
|                         | item had been used in   |                         |                         |
|                         | any way.                |                         |                         |
+-------------------------+-------------------------+-------------------------+-------------------------+
| A transaction in the    | The timestamp of a data | Each successful write   | A transaction is        |
| Two Phase Locking       | item can be of 2 types: | results in the creation | executed without        |
| Protocol can assume one |                         | of a new version of the | checking the            |
| of the 2 phases:        |                         | data item written.      | consistency or          |
|                         |                         |                         | isolation requirement   |
|                         |                         |                         | until the transaction   |
|                         |                         |                         | is ready to commit.     |
+-------------------------+-------------------------+-------------------------+-------------------------+
| Growing Phase: In this  | W-timestamp (X): This   | Timestamps are used to  | Then, the transaction   |
| phase a transaction can | means the latest time   | label the versions.     | is validated to ensure  |
| only acquire locks but  | when the data item X    |                         | that its execution      |
| cannot release any      | has been written into.  |                         | does not violate the    |
| lock. The point when a  |                         |                         | serializability         |
| transaction acquires    |                         |                         | property.               |
| all the locks it needs  |                         |                         |                         |
| is called the Lock      |                         |                         |                         |
| Point.                  |                         |                         |                         |
+-------------------------+-------------------------+-------------------------+-------------------------+
| Shrinking Phase: In     | R-timestamp (X): This   | When a read (X)         | If the validation is    |
| this phase a            | means the latest time   | operation is issued,    | successful, the         |
| transaction can only    | when the data item X    | select an appropriate   | transaction is allowed  |
| release locks but       | has been read from.     | version of X based on   | to commit. Otherwise,   |
| cannot acquire any.     |                         | the timestamp of the    | the transaction is      |
|                         |                         | transaction.            | aborted and restarted.  |
+-------------------------+-------------------------+-------------------------+-------------------------+
```

The diagram is based on the information from the web search results   . I hope this helps you with your notes.😊