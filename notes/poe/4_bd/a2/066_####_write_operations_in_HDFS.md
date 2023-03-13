 Here is the content in markdown format for the write operations in HDFS:

#### Write operations in HDFS

The write operations in HDFS are:

1. Appending to a file: Data can be appended to an existing file in HDFS using `dfs -appendToFile` command. The data is appended to the end of the file.
2. Creating a file: A new file can be created in HDFS using `dfs -create` command. The file is created with specified permissions and replication factor.
3. Overwriting a file: An existing file in HDFS can be overwritten using `dfs -create` command with the overwrite option. The file is overwritten with new data and permissions/replication factor can also be changed.

**Mnemonics:**
- Think of appending data as adding more items to the end of a list.
- Overwriting is like erasing the existing file and writing a new file with the same name.

**Advantages:**
- Appending allows adding more data to existing files without recreating them.
- Overwriting allows updating files in-place without using more space.

**Disadvantages:**
- Appending can make files fragmented if not done sequentially.
- Overwriting loses the previous version of the file.

**Examples:**
```
hdfs dfs -appendToFile <localsrc> ...
hdfs dfs -create ... [-overwrite] <dest>
```

**Applications:** Append is useful for log files, metrics, etc. Overwriting is useful for updating configuration files, etc.

Detailed diagrams and more examples can be included if required. The content can be expanded with more details and points as needed. The suggestions were to write in a formal and exam-friendly style with mnemonics/tricks only if easy to remember. Please let me know if you would like me to modify or expand the answer.