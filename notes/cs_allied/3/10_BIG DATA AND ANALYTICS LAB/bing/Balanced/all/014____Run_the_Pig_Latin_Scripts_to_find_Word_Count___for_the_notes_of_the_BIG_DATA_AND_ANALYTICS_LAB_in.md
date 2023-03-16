## Run the Pig Latin Scripts to find Word Count

- Pig Latin is a high-level scripting language that can be used to process and analyze large-scale data sets using Apache Pig, a platform for parallel data processing.
- Pig Latin scripts can be executed in two modes: local mode and MapReduce mode. Local mode runs on a single machine, while MapReduce mode runs on a cluster of machines using Hadoop.
- To run a Pig Latin script, you need to have Pig installed and configured on your machine or cluster. You can download Pig from https://pig.apache.org/download.html and follow the installation instructions.
- To find the word count of a text file using Pig Latin, you can use the following steps:

  1. Create a text file with some sample text, such as `sample.txt`, and save it in your local directory or HDFS (Hadoop Distributed File System).
  2. Create a Pig Latin script, such as `wordcount.pig`, that contains the following code:

     ```
     -- Load the text file as a relation
     A = LOAD 'sample.txt' AS (line:chararray);

     -- Split each line into words and flatten the result
     B = FOREACH A GENERATE FLATTEN(TOKENIZE(line)) AS word;

     -- Group the words by their value and count the occurrences
     C = GROUP B BY word;
     D = FOREACH C GENERATE group, COUNT(B);

     -- Store the output in a file
     STORE D INTO 'wordcount.out';
     ```

  3. Run the Pig Latin script in local mode or MapReduce mode, depending on your setup. For example, to run it in local mode, you can use the following command:

     ```
     pig -x local wordcount.pig
     ```

  4. Check the output file, `wordcount.out`, to see the word count of each word in the text file. The output file will contain one line for each word, with the word and its count separated by a tab. For example:

     ```
     hello	2
     world	1
     pig	3
     latin	1
     ```