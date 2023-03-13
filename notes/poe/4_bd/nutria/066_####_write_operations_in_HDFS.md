
#### Write Operations in HDFS

- **Writing Data into HDFS:** HDFS provides two types of operations for writing data into HDFS, namely `create()` and `append()`. 
- The `create()` operation is used to create a new file in HDFS and write data into it. 
- The `append()` operation is used to append data to an existing file in HDFS. 
- Both of these operations are provided by the `FileSystem` class. 
- The `create()` operation takes the path of the file to be created, the data to be written, and the replication factor as parameters. 
- The replication factor determines the number of replicas of the data that will be stored in the HDFS cluster. 
- The `append()` operation takes the path of the file to which data is to be appended, and the data to be written as parameters. 
- The data is written in the form of byte arrays. 
- HDFS also provides the `sync()` operation to ensure that the data is written to the disk.

Mnemonic: 
- Create: C for Create
- Append: A for Append
- Replication Factor: R for Replication
- Sync: S for Sync