 Here is the content in markdown format for the topic ### input formats for the notes of the Unit 3 - Map Reduce in the subject of Big Data:

### Input Formats for MapReduce

The input data for a MapReduce job is in the form of files/data stored in the HDFS. The MapReduce framework requires the input data to be in a specific format to process the data efficiently. The following are the commonly used input formats for MapReduce:

1. Text Input Format: This is the default input format used in MapReduce. The input data is in text files with each line as a record. The line is passed as a key-value pair to the Map function where the key is the line number and the value is the line of text. This format is suitable for processing logs, crawled web pages, etc.
2. Key-Value Input Format: In this input format, each input record has a key and a value. The keys should be in order for efficient sorting and shuffling. This format is suitable for processing datasets where key-based ordering or grouping is needed.
3. Sequence File Input Format: This is a binary input format suitable for passing serialized Java objects as input to the Map function. The serialization is performed using the Writable interface. This is efficient in terms of storage and processing as compared to the text input format.
4. DBInput Format: This input format is used to get input data from databases. The input splits are obtained from the database table splits. A connection to the database is established and the table is scanned to get the input splits. This is useful for processing data already stored in databases without extracting it out.

The input format is specified while setting up the MapReduce job along with the input locations and other job configurations. The MapReduce framework then takes care of splitting the input, distributing the splits, and providing the key-value record pairs to the Map functions. The output of the Map functions is then shuffled and sorted based on the keys before providing the inputs to the Reduce functions.