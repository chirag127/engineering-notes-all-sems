### Hadoop Archives

Hadoop Archives, or HAR, is an archiving facility that packs files into HDFS blocks efficiently. This can be used to tackle the small files problem in Hadoop . A HAR is created from a collection of files, and the archiving tool will run a MapReduce job to process the input files in parallel and create an archive file .

HAR files can reduce NameNode memory usage while still allowing transparent access to files . Hadoop Archives can also be used as input to MapReduce . For example, if you have a Hadoop archive stored in HDFS in `/user/zoo/foo.har`, then for using this archive for MapReduce input, all you need to do is specify the input directory as `har:///user/zoo/foo.har` .