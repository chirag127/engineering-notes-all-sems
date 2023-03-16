## Run the Pig Latin Scripts to find Word Count

- Pig Latin is a high-level scripting language that can be used to process and analyze large-scale data sets using Apache Pig, a platform for parallel data processing.
- Pig Latin scripts are composed of a series of statements that define how to load, transform, filter, group, join, and store data.
- To run a Pig Latin script, you need to have Apache Pig installed and configured on your system, or use a cloud service that provides Pig as a service, such as Amazon EMR or Google Cloud Dataproc.
- To find the word count of a text file using Pig Latin, you can follow these steps:

  1. Load the text file into a relation using the `LOAD` statement. Specify the file path, the delimiter (such as whitespace or comma), and the schema (such as chararray for strings) of the data. For example:

     `A = LOAD 'input.txt' USING PigStorage(' ') AS (word:chararray);`

  2. Group the words by their values using the `GROUP` statement. This will create a relation with two fields: the word and a bag of tuples containing the word. For example:

     `B = GROUP A BY word;`

  3. Count the number of occurrences of each word using the `COUNT` function. This will create a relation with two fields: the word and the count. For example:

     `C = FOREACH B GENERATE group, COUNT(A);`

  4. Store the result into a file using the `STORE` statement. Specify the file path and the storage function (such as PigStorage or TextLoader) to use. For example:

     `STORE C INTO 'output.txt' USING PigStorage(',');`

  5. Run the script using the `pig` command in the terminal or the Pig shell. For example:

     `pig -x local wordcount.pig`

  6. Check the output file for the word count. For example:

     `cat output.txt`

     `hello,2`

     `world,1`

     `goodbye,1`