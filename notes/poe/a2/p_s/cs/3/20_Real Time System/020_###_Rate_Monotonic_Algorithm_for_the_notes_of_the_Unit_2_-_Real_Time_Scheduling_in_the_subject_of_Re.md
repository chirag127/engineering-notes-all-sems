 Here is the content in markdown format for the topic #### Hadoop archives in HDFS:

#### Hadoop archives in HDFS

- Hadoop archives (HAR files) are a utility to package multiple files into a single archive for efficient storage and distribution.
- They are simply tar archives with a .har extension, with data-nodes storing the individual blocks of a HAR file as they would for regular files.
- Advantages:
    - Reduces NameNode load by combining many small files into a single file.
    - Easier and more efficient to transfer/copy/distribute a single HAR file instead of many individual files.
    - Can be split into input splits for MapReduce, allowing HAR files to be used as inputs to MapReduce jobs.
- Creating a HAR file:
    - Using `hadoop archive` command:
        - `hadoop archive -archiveName myOutput.har -p <path/to/input/data> output/`
    - This will package everything under `<path/to/input/data>` into `myOutput.har` under `output/`
- Accessing files within a HAR:
    - HAR files can be accessed just like regular archives using `hadoop fs -har:///` to list contents and access individual files.
- Limitations:
    - Not splittable beyond a single block - input splits will contain entire HAR files, not individual files within.
    - Compression not supported - HAR files are just tar archives and do not utilize Hadoop's record-level compression.
    - Not query-able with Hive or Pig - must first extract files from HAR to query with these tools.
- Use cases:
    - Archiving log data or other related files for analysis.
    - Temporary data aggregation before further processing.
    - Data transfer/distribution.

[Detailed diagrams and examples can be added here to aid learning]