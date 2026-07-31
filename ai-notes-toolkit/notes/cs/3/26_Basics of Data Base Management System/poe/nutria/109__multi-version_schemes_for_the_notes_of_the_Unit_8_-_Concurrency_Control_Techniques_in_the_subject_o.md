
### Multi-version Schemes for Unit 8 - Concurrency Control Techniques in Basics of Database Management System 

1. Multi-version schemes are concurrency control techniques used to manage concurrent transactions in a database.
2. Multi-version schemes allow multiple versions of the same data item to exist in the database at the same time.
3. The versions are created when a transaction reads a data item and then updates it.
4. The data item is kept in a version list, which contains the version number, the timestamp of when the version was created, and the data itself.
5. When a transaction attempts to update a data item, the version list is checked to see if the transaction is trying to update a version that is not the most recent.
6. If the transaction is trying to update an outdated version, the transaction is aborted and the data item is not updated.
7. If the transaction is trying to update the most recent version, the data item is updated and a new version is created in the version list.
8. This ensures that concurrent transactions can be processed without any data loss.