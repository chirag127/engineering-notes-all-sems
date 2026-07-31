### Hadoop Archives (HAR)

- Hadoop Archives or HAR is an archiving facility that packs files into HDFS blocks efficiently and hence HAR can be used to tackle the small files problem in Hadoop.
- HAR is created from a collection of files and the archiving tool (a simple command) will run a MapReduce job to process the input files in parallel and create an archive file.
- Hadoop Archives can be used as input to MapReduce.
- Using Hadoop Archives in MapReduce is as easy as specifying a different input filesystem than the default file system.
- If you have a Hadoop archive stored in HDFS in /user/zoo/foo.har then for using this archive for MapReduce input, all you need is to specify the input directory as har:///user/zoo/foo.har .