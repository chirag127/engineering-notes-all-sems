### Hadoop Archives

- Hadoop Archives (HAR) are special format archives that efficiently pack small files into HDFS blocks.
- The Hadoop Distributed File System (HDFS) is designed to store and process large data sets, but HDFS can be less efficient when storing a large number of small files.
- Hadoop Archives can be used as input to MapReduce.
- Using Hadoop Archives in MapReduce is as easy as specifying a different input filesystem than the default file system.
- If you have a Hadoop archive stored in HDFS in `/user/zoo/foo.har`, then for using this archive for MapReduce input, all you need is to specify the input directory as `har:///user/zoo/foo.har` .