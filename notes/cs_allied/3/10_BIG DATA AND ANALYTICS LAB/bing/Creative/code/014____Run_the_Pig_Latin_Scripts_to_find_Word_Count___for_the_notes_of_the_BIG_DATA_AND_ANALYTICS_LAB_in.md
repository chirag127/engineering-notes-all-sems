Hello, I am Sydney, your AI assistant. I can help you with your notes on Big Data and Analytics Lab. Here is the content for the topic of running the Pig Latin scripts to find word count.

## Run the Pig Latin Scripts to find Word Count

- Pig Latin is a high-level scripting language that allows users to write complex data transformations using a simple syntax. Pig Latin scripts are executed by a Pig engine, which can run on a single machine or on a Hadoop cluster.
- To find the word count of a text file using Pig Latin, we need to follow these steps:

  - Load the text file into a relation using the `LOAD` operator. A relation is a bag of tuples, where each tuple is a sequence of fields. For example, `A = LOAD 'input.txt' USING TextLoader() AS (line:chararray);` loads the text file `input.txt` into a relation `A` with one field named `line` of type `chararray`.
  - Split each line into words using the `TOKENIZE` function, which returns a bag of words. For example, `B = FOREACH A GENERATE TOKENIZE(line) AS words;` creates a new relation `B` with one field named `words` of type `bag`, where each tuple contains a bag of words from a line of the input file.
  - Flatten the bags of words into individual words using the `FLATTEN` operator, which flattens a nested bag into a single-level bag. For example, `C = FOREACH B GENERATE FLATTEN(words) AS word;` creates a new relation `C` with one field named `word` of type `chararray`, where each tuple contains a single word from the input file.
  - Group the words by their value using the `GROUP` operator, which groups the tuples by one or more fields and creates a new relation with two fields: the group key and the bag of tuples with that key. For example, `D = GROUP C BY word;` creates a new relation `D` with two fields: `word` and `C`, where each tuple contains a word and a bag of tuples with that word from relation `C`.
  - Count the number of tuples in each group using the `COUNT` function, which returns the number of tuples in a bag. For example, `E = FOREACH D GENERATE group, COUNT(C) AS count;` creates a new relation `E` with two fields: `group` and `count`, where each tuple contains a word and its frequency in the input file.
  - Store the result into a file using the `STORE` operator, which stores a relation into a file or directory. For example, `STORE E INTO 'output.txt' USING PigStorage(',');` stores the relation `E` into a file `output.txt` using a comma as the field delimiter.

- The complete Pig Latin script for finding the word count of a text file is:

```
A = LOAD 'input.txt' USING TextLoader() AS (line:chararray);
B = FOREACH A GENERATE TOKENIZE(line) AS words;
C = FOREACH B GENERATE FLATTEN(words) AS word;
D = GROUP C BY word;
E = FOREACH D GENERATE group, COUNT(C) AS count;
STORE E INTO 'output.txt' USING PigStorage(',');
```

- To run the script, we need to launch the Pig shell using the command `pig` and then use the `run` command to execute the script file. For example, `run wordcount.pig` runs the script file `wordcount.pig` and stores the output in `output.txt`. Alternatively, we can use the `-f` option to run the script file directly from the command line. For example, `pig -f wordcount.pig` does the same thing as the previous command.