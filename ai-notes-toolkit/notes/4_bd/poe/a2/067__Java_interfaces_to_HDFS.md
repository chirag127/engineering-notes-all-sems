 Here is the formal content on the topic "Java interfaces to HDFS" in markdown format:

#### Java interfaces to HDFS

1. Java DFS (Distributed File System) API - The basic Java API for interacting with HDFS. It allows you to create, open, close, read and write files on HDFS.
2. Hadoop Common - Provides the common utilities and OS level abstractions for a Hadoop system. It includes the Java DFS API.
3. Hadoop File System (FS) Shell - A command line shell interface for interacting with HDFS. It uses the Java DFS API under the hood.
4. Hadoop Streaming API - Allows you to create and run MapReduce jobs with any executable or script as the mapper and/or the reducer. Data is passed between the map and reduce tasks via stdin and stdout.
5. Hadoop Archives (HAR) - Facilitates archiving files and directories within HDFS. This allows you to package a set of files in a compressed archive to reduce storage use and enhance data organization.
6. WebHDFS - A REST API for HDFS which allows HTTP access to HDFS. This can be useful for accessing HDFS from languages other than Java or for accessing HDFS in distributed systems where Java is not the primary language.

The points are written in formal tone without any feelings or emojis. Only markdown format is used with headings and points. External links are not included. The content is written from the perspective of study material for exams. Please let me know if you would like me to modify or add any other points.