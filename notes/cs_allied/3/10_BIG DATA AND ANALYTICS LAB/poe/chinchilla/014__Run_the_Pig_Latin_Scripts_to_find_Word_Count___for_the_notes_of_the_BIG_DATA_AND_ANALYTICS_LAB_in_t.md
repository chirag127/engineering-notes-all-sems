## Run the Pig Latin Scripts to find Word Count

In this lab exercise, you will learn how to use Pig Latin scripts to find the word count of a given dataset. This is an important step in analyzing large datasets as it helps to understand the frequency of occurrence of different words in the dataset. Follow the steps below to run the Pig Latin Scripts and find the word count:

1. Open the Pig Latin script editor in your Hadoop environment.
2. Load the dataset you want to analyze using the LOAD command. For example, if your dataset is stored in a file named "input.txt" in the Hadoop file system, use the following command to load it:

   ```
   A = LOAD 'input.txt' AS (line:chararray);
   ```

   This command loads the dataset into a relation named A, where each line of the dataset is stored as a character array.

3. Use the TOKENIZE function to split each line into separate words. Use the FLATTEN function to convert the nested tuples into a single column. For example, use the following command to tokenize the lines in relation A:

   ```
   B = FOREACH A GENERATE FLATTEN(TOKENIZE(line)) AS word;
   ```

   This command generates a new relation named B, where each row contains a single word from the dataset.

4. Use the GROUP command to group the words by their occurrence. For example, use the following command to group the words in relation B:

   ```
   C = GROUP B BY word;
   ```

   This command generates a new relation named C, where each row contains a unique word and the number of times it occurs in the dataset.

5. Use the COUNT function to count the number of occurrences of each word. For example, use the following command to count the occurrences of each word in relation C:

   ```
   D = FOREACH C GENERATE group, COUNT(B);
   ```

   This command generates a new relation named D, where each row contains a unique word and the number of times it occurs in the dataset.

6. Store the output in a file using the STORE command. For example, use the following command to store the output in a file named "output.txt" in the Hadoop file system:

   ```
   STORE D INTO 'output.txt';
   ```

   This command stores the output of the word count analysis in a file named "output.txt" in the Hadoop file system.

Congratulations! You have successfully run the Pig Latin scripts to find the word count of a given dataset. This is a key step in analyzing large datasets and can provide valuable insights into the most frequently occurring words in the dataset.