## Run the Pig Latin Scripts to find Word Count

In the Big Data and Analytics Lab, one of the important tasks is to analyze the data and extract meaningful insights from it. For this purpose, various tools and technologies are used, and one such tool is Pig Latin.

Pig Latin is a high-level scripting language that is used to analyze large datasets in a Hadoop cluster. It is an easy-to-learn language that enables you to write complex MapReduce jobs without writing actual MapReduce code.

To find the word count in Pig Latin, you need to follow these steps:

1. Load the data: First, you need to load the data into Pig using the LOAD function. The data can be stored in various formats such as CSV, JSON, or text.

2. Tokenize the data: Once the data is loaded, you need to tokenize it using the TOKENIZE function. This function splits the data into individual words.

3. Filter the data: After tokenizing the data, you need to filter out any unnecessary words such as stop words or punctuation marks.

4. Group the data: Next, you need to group the data by word using the GROUP function.

5. Count the data: Finally, you need to count the number of occurrences of each word using the COUNT function.

Here is an example Pig Latin script to find the word count:

```
data = LOAD 'input.txt' USING PigStorage(',');
tokens = FOREACH data GENERATE FLATTEN(TOKENIZE($0)) AS word;
filtered = FILTER tokens BY word MATCHES '\\w+';
grouped = GROUP filtered BY word;
wordcount = FOREACH grouped GENERATE group, COUNT(filtered);
STORE wordcount INTO 'output';
```

In this script, we load the data from a file called 'input.txt' using the PigStorage function. We then tokenize the data using the TOKENIZE function and filter out any non-word characters using a regular expression. We group the data by word and count the number of occurrences using the COUNT function. Finally, we store the result in a file called 'output'.

By running this script, you can easily find the word count of any text data in a Hadoop cluster using Pig Latin. This is just one example of how Pig Latin can be used to perform data analysis tasks in Big Data and Analytics Lab.