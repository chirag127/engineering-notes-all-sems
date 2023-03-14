#### Hadoop archives in HDFS

- Hadoop archives or HAR files are a special format of archives that can pack files into HDFS blocks more efficiently, thereby reducing the NameNode memory usage and the namespace pressure  .
- HAR files can be used to tackle the small files problem in Hadoop, which occurs when there are too many small files that occupy more blocks and metadata than the actual data size .
- HAR files can be created from a collection of files using a simple command that runs a MapReduce job to process the input files in parallel and create an archive file.
- HAR files can be used as input to MapReduce jobs, and they expose themselves as a file system layer, so all the fs shell commands work with a different URI  .
- HAR files are immutable, so rename, delete and create operations are not allowed on them .
- HAR files have a *.har extension, and they contain metadata (_index and _masterindex) and data (part-*) files. The _index file contains the name and the location of the files that are part of the archive .
- HAR files can be created using the following syntax:

```
hadoop archive -archiveName name -p <parent> [-r <replication factor>] <src>* <dest>
```

- The -archiveName argument specifies the name of the archive, which should have a *.har extension. The -p argument specifies the relative path to which the files should be archived. The -r argument specifies the desired replication factor, which defaults to 3 if not specified. The <src> argument specifies the source files or directories to be archived, and the <dest> argument specifies the destination directory for the archive .
- For example, to create an archive named foo.har from the directories /user/hadoop/dir1 and /user/hadoop/dir2, using /user/hadoop as the relative path and /user/zoo as the destination directory, the command would be:

```
hadoop archive -archiveName foo.har -p /user/hadoop dir1 dir2 /user/zoo
```

- This command will create an archive file /user/zoo/foo.har, which will contain the files from /user/hadoop/dir1 and /user/hadoop/dir2. The archiving process does not delete the input files, so they have to be deleted manually if needed .
- To look up files in HAR files, the URI for Hadoop archives is:

```
har://scheme-hostname:port/archivepath/fileinarchive
```

- If no scheme is provided, it assumes the underlying filesystem. In that case, the URI would be:

```
har:///archivepath/fileinarchive
```

- For example, to list all the files in the archive /user/zoo/foo.har, the command would be:

```
hadoop dfs -lsr har:///user/zoo/foo.har/
```

- To unarchive files from HAR files, the copy command can be used, either sequentially or in parallel using DistCp. For example, to unarchive the directory /user/zoo/foo.har/dir1 to /user/zoo/newdir, the command would be:

```
hdfs dfs -cp har:///user/zoo/foo.har/dir1 hdfs:/user/zoo/newdir
```

- Or, to unarchive in parallel, the command would be:

```
hadoop distcp har:///user/zoo/foo.har/dir1 hdfs:/user/zoo/newdir
```

- HAR files have some advantages and disadvantages. Some of the advantages are:

  - They reduce the NameNode memory usage and the namespace pressure by packing many small files into fewer large files.
  - They allow transparent access to the archived files using the fs shell commands and the MapReduce jobs.
  - They can be encrypted or decrypted depending on the encryption zone of the archive file and the source files.

- Some of the disadvantages are:

  - They are immutable, so any changes to the archived files require creating a new archive.
  - They add an extra layer of indirection, which may affect the performance and the complexity of the file system operations.
  - They do not support compression, so the archive size may be larger than the sum of the input file sizes.

- A possible mnemonic to remember the HAR file format is:

``