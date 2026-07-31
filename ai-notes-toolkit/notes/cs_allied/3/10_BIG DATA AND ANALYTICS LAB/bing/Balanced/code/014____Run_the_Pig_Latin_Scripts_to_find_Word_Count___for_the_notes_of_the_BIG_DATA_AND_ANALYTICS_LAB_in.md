## Run the Pig Latin Scripts to find Word Count

- Pig Latin is a scripting language that can be used to perform data analysis tasks on large datasets using Apache Pig, a platform for parallel data processing.
- To run the Pig Latin scripts, you need to have Apache Pig installed and configured on your system, or use a cloud service that provides Pig as a service, such as Amazon EMR or Google Cloud Dataproc.
- To find the word count of a text file using Pig Latin, you can follow these steps:

  1. Load the text file into a relation using the `LOAD` operator. For example, `A = LOAD 'input.txt' USING TextLoader() AS (line:chararray);`
  2. Split each line into words using the `TOKENIZE` function. For example, `B = FOREACH A GENERATE TOKENIZE(line) AS words;`
  3. Flatten the nested bag of words into a single bag using the `FLATTEN` operator. For example, `C = FOREACH B GENERATE FLATTEN(words) AS word;`
  4. Group the words by their value using the `GROUP` operator. For example, `D = GROUP C BY word;`
  5. Count the number of occurrences of each word using the `COUNT` function. For example, `E = FOREACH D GENERATE group, COUNT(C);`
  6. Store the output relation into a file using the `STORE` operator. For example, `STORE E INTO 'output.txt' USING PigStorage(',');`

- The final script can be written as:

```pig
A = LOAD 'input.txt' USING TextLoader() AS (line:chararray);
B = FOREACH A GENERATE TOKENIZE(line) AS words;
C = FOREACH B GENERATE FLATTEN(words) AS word;
D = GROUP C BY word;
E = FOREACH D GENERATE group, COUNT(C);
STORE E INTO 'output.txt' USING PigStorage(',');
```

- To run the script, you can use the `pig` command in the terminal, or use the Pig shell or the Grunt shell. For example, `pig -x local wordcount.pig` will run the script in local mode. You can also use the `-f` option to specify the script file name. For example, `pig -f wordcount.pig -x local`.
- The output file will contain the word and its count separated by a comma. For example:

```text
hello,3
world,2
pig,1
latin,1
```