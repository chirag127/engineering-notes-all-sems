 Here is the content in markdown format on the topic ### transaction control commands for the notes of the Unit 5 - Structured Query Language (SQL) in the subject of Basics of Data Base Management System:

#### Commit:
- Finalizes a transaction and makes all data changes permanent.
- Releases any locks held by the transaction.
- Used to end a transaction and save the changes.

```
COMMIT;
```

#### Rollback:
- Undoes all the changes made by the current transaction.
- Releases any locks held by the transaction.
- Used to cancel a transaction and revert to the original state.

```
ROLLBACK;
```

#### Savepoint:
- Sets a savepoint within a transaction.
- Acts as a rollback point to which the transaction can return to in case of a error.
- The savepoints allow to rollback a transaction partially. All savepoints after it get released.

```
SAVEPOINT savepoint_name;
```

#### Release Savepoint:
- Releases a previously set savepoint.
- The released savepoint can no longer be used as a rollback point.

```
RELEASE SAVEPOINT savepoint_name;
```

The transaction control commands help to maintain atomicity, consistency, isolation and durability (ACID) properties of a transaction. They are used to either commit or undo changes made by a transaction. Savepoints provide more granular control over transactions by allowing partial rollbacks.

Diagrams and examples can be included if required. The points can be expanded with more details and applications. Please let me know if you would like me to modify or add anything to the answer.