## Run the Pig Latin Scripts to find Word Count

- Pig Latin is a high-level scripting language that is used to process and analyze large datasets using Apache Pig, a platform for big data analytics.
- Pig Latin scripts are composed of a series of statements that describe how to load, transform, and store data.
- To run a Pig Latin script, you need to have Apache Pig installed and configured on your system, and a text file that contains the script.
- One of the common tasks that can be performed using Pig Latin is to find the word count of a text file, which is the number of times each word appears in the file.
- To find the word count using Pig Latin, you can follow these steps:

  - Create a text file that contains some text, such as a paragraph from a book or an article. Save the file as input.txt in your working directory.
  - Create another text file that contains the following Pig Latin script and save it as wordcount.pig in your working directory:

    ```
    -- Load the input file using PigStorage loader
    input = LOAD 'input.txt' USING PigStorage() AS (line:chararray);

    -- Split each line into words using TOKENIZE function
    words = FOREACH input GENERATE FLATTEN(TOKENIZE(line)) AS word;

    -- Group the words by their value and count the occurrences using COUNT function
    grouped = GROUP words BY word;
    wordcount = FOREACH grouped GENERATE group, COUNT(words);

    -- Store the output in a file using PigStorage storer
    STORE wordcount INTO 'output.txt' USING PigStorage();
    ```

  - Open a terminal and navigate to your working directory. Run the following command to execute the Pig Latin script:

    ```
    pig wordcount.pig
    ```

  - The script will load the input file, split each line into words, group the words by their value, count the occurrences, and store the output in a file named output.txt in your working directory.
  - The output file will contain one line for each word, followed by a tab and the number of times the word appears in the input file. For example, if the input file contains the following text:

    ```
    The quick brown fox jumps over the lazy dog.
    ```

    The output file will contain the following lines:

    ```
    The	1
    brown	1
    dog.	1
    fox	1
    jumps	1
    lazy	1
    over	1
    quick	1
    the	1
    ```

- This is how you can run the Pig Latin scripts to find the word count of a text file using Apache Pig.