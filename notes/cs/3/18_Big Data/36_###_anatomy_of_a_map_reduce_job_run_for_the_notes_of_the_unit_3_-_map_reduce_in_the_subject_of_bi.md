### anatomy of a Map Reduce job run for the notes of the Unit 3 - Map Reduce in the subject of Big Data

The anatomy of a MapReduce job run refers to the process of executing a MapReduce job in a Hadoop cluster. The following are the key steps involved in an anatomy of a MapReduce job run:

1. Input Split: The input data is divided into smaller chunks called input splits, which are processed by individual Map tasks.

2. Map Task: The Map task takes an input split as input and applies the Map function to each record in the split, producing intermediate key-value pairs.

3. Shuffle and Sort: The intermediate key-value pairs produced by the Map tasks are shuffled and sorted, to group together all records with the same key.

4. Reduce Task: The Reduce task takes the sorted intermediate key-value pairs as input and applies the Reduce function to each group of records with the same key, producing the final output.

5. Output: The final output of the MapReduce job is written to the output directory in HDFS.

In this unit, you will learn about the anatomy of a MapReduce job run in Big Data, including input split, Map task, shuffle and sort, Reduce task, and output.

This unit will provide a foundation for understanding the principles and practices of MapReduce in Big Data, and for exploring the various concepts and techniques used in the field of Big Data.
