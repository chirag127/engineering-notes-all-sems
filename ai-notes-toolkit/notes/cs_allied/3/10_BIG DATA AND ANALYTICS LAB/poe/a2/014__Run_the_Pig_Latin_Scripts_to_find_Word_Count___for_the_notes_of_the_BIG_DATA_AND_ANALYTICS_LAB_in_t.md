 Here is the content in markdown format without emojis and external links:

## Run the Pig Latin Scripts to find Word Count

- Load the file into Pig using `LOAD` statement.
- Split the loaded data into words using `TOKENIZE` statement.
- Filter out unwanted words like stopwords, punctuations, etc. using `FILTER` statement.
- Calculate the word count using `GROUP` and `COUNT` statements.
- Store the result back to the filesystem using `STORE` statement.

The above steps can be implemented in Pig Latin script as follows:

```pig
raw_data = LOAD 'input_file_path' AS (line:chararray);
words = TOKENIZE(raw_data) AS (word:chararray);
filtered_words = FILTER words BY word MATCHES '\\w+';
word_count = GROUP filtered_words BY (1) ALL;
count = FOREACH word_count GENERATE COUNT(filtered_words) AS count;
STORE count INTO 'output_file_path';
```

- The script loads the input data.
- Then, it tokenizes the data into words.
- It filters out unwanted words.
- Then, it groups the words and counts them.
- Finally, it stores the word count into the output file.

The above script can be used to find the word count of a given text file in Pig.