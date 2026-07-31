## Run the Pig Latin Scripts to find Word Count

1. Pig Latin is a high-level platform for creating MapReduce programs used with Hadoop.
2. It is used to analyze large data sets representing them as data flows.
3. Pig Latin scripts are translated into a series of MapReduce jobs that are run on the Apache Hadoop platform.
4. To find the word count using Pig Latin, you need to write a script that will load the data, tokenize the words, group the words, count the occurrences of each word, and store the results.
5. Here is an example of a Pig Latin script that finds the word count of a text file:

```
-- Load the data
data = LOAD 'input.txt' USING PigStorage() AS (line:chararray);

-- Tokenize the words
words = FOREACH data GENERATE FLATTEN(TOKENIZE(line)) AS word;

-- Group the words
grouped = GROUP words BY word;

-- Count the occurrences of each word
wordcount = FOREACH grouped GENERATE group, COUNT(words);

-- Store the results
STORE wordcount INTO 'output';
```

6. This script can be run on the Pig command line or saved to a file and run using the Pig command.
7. The results of the word count will be stored in the specified output directory.