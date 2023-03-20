 Here is the content in Markdown format without any emojis or external links as per your instructions:

### Case Study of Oracle for the notes of the Unit 5 - Concurrency Control Techniques in the subject of Database Management System

1. Oracle uses a multi-version concurrency control (MVCC) model to provide high performance and scalability for its database system.
2. In MVCC, each user gets a snapshot view of the database at a particular point in time. This allows multiple users to access the same data concurrently without blocking each other.
3. Oracle uses a system change number (SCN) to track the versions of data. Each transaction is assigned an SCN when it begins.
4. When a user queries the database, Oracle retrieves the versions of rows that were committed at an SCN earlier than the transaction's SCN. This gives the user a consistent view of the database at an earlier point in time.
5. When a transaction commits, the SCN is used to determine which transactions need to see the changes. Only those transactions with an SCN greater than the committing transaction will see the changes.
6. The MVCC model requires extra storage to keep the old row versions, but it avoids the performance penalties of locking mechanisms like two-phase locking. The extra storage requirements can be managed through regular cleanup of old data versions.
7. Additional features in Oracle like snapshot isolation and read consistency provide advanced concurrency control capabilities for specific application requirements.

The above points cover the key highlights of how Oracle implements concurrency control using the MVCC model for optimal performance and scalability. The content is written in a formal tone with points and without any emojis or external links as per your instructions. Please let me know if you would like me to modify or expand the response.