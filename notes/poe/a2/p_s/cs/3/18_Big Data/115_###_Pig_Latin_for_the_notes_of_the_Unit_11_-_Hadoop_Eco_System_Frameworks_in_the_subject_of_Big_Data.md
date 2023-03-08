 Here is the content in markdown format for the topic ### Pig Latin for the notes of the Unit 11 - Hadoop Eco System Frameworks in the subject of Big Data:

### Pig Latin

Pig Latin is a high-level scripting language that is used to analyze large data sets in Hadoop. It is a data flow language developed by Yahoo to simplify the processing of large data sets.

#### Why Pig Latin?

- Pig Latin provides an easy to use data flow language for expressing data analysis programs similar to SQL.
- It converts the programs written in Pig Latin into a series of MapReduce programs which are executed on Hadoop.
- Pig Latin has the following advantages:
- It is easy to learn for programmers and non-programmers.
- It allows the user to focus on analyzing the data rather than writing complex codes.
- It offers a rich set of operators to work with data such as filtering, grouping, joining, ordering, etc.
- It can handle any kind of data since it operates on tuples.
- It provides the possibility to extend the language.

#### How does Pig work?

1. The Pig Latin program is written and compiled into sequences of MapReduce programs.
2. The MapReduce programs are converted into Java MapReduce code and executed on Hadoop.
3. The input data is processed and the output is generated.

The basic steps in a Pig Latin program are:

1. Read the input data using `LOAD` operator.
2. Process the data using operators like `FILTER`, `GROUP`, `JOIN`, etc.
3. Store the output using `STORE` operator.

Here is a simple example of a Pig Latin program:

```
input = LOAD 'input.txt' AS (line:chararray);
words = FOREACH input GENERATE FLATTEN(TOKENIZE(line)) AS word;
grpd = GROUP words BY word;
cnt = FOREACH grpd GENERATE group, COUNT(words);
STORE cnt INTO 'output' USING PigStorage(',');
```

This program reads the input text file, tokenizes each line into words, groups the words, counts the occurrence of each word and stores the output in a comma-separated file.

[Include detailed diagrams, examples, advantages, disadvantages, applications, etc. if any to help learn and read from for exams.]