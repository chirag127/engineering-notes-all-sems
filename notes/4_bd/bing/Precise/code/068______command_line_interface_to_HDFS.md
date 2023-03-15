#### Command Line Interface to HDFS

Here is an example of how to use the command line interface to interact with HDFS:

```sh
# List the contents of the root directory in HDFS
hdfs dfs -ls /

# Create a new directory in HDFS
hdfs dfs -mkdir /new_directory

# Copy a file from the local file system to HDFS
hdfs dfs -put local_file.txt /new_directory

# View the contents of a file in HDFS
hdfs dfs -cat /new_directory/local_file.txt

# Delete a file in HDFS
hdfs dfs -rm /new_directory/local_file.txt

# Delete a directory in HDFS
hdfs dfs -rmdir /new_directory
```