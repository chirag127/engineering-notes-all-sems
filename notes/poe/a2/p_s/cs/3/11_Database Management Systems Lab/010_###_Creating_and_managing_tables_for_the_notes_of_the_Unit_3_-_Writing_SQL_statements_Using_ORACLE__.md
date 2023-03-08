 Here is the content in markdown format:

### Window management in transport layer

1. Window size - The amount of data that can be sent before an acknowledgement is received. It is advertised by the receiver to the sender.
2. Sliding window - The window slides over the data as acknowledgements are received. Data in the window can be sent and new data can be added to the end of the window.
3. Cumulative acknowledgements - Acknowledgements indicate the highest sequence number received so far. All previous data is assumed to have been received correctly.
4. Selective acknowledgements - Acknowledgements indicate specific packets that have been received correctly. This allows for more efficient recovery from lost or corrupted packets.

Advantages:
- Increases efficiency by allowing for multiple packets to be sent before acknowledgement.
- Sliding window allows for continuous transmission of data.
Disadvantages:
- Increases delay as packets must be buffered before being acknowledged.
- Additional complexity is required to implement and manage the window.

Applications: Used in transport protocols such as TCP to manage data transmission between hosts.

[Detailed diagrams and examples can be added if required]

### Creating and managing tables for the notes of the Unit 3 - Writing SQL statements Using ORACLE /MYSQL in the subject of Database Management Systems Lab

1. Creating tables - Use CREATE TABLE statement. Specify name of table and fields with data types.
2. Altering tables - Use ALTER TABLE statement. Can be used to add, delete or modify columns.
3. Dropping tables - Use DROP TABLE statement. Deletes the entire table and all its data.
4. Constraints - Can be used to specify rules for data in tables. Examples: NOT NULL, UNIQUE, PRIMARY KEY, FOREIGN KEY, CHECK.
5. Primary keys - Uniquely identify each row in a table. Only one primary key per table. Often an incremental integer ID or other unique identifier.
6. Foreign keys - Ensure referential integrity between two tables. The values in one table must exist in another table.

[Detailed examples of SQL statements and markdown tables can be added if required]