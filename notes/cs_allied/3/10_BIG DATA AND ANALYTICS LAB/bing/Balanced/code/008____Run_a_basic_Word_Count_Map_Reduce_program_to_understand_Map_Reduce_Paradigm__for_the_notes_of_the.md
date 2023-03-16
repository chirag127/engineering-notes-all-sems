Hello, I am Sydney, your AI assistant. I can help you with your study material for the BIG DATA AND ANALYTICS LAB subject. Here are some notes on the topic of running a basic Word Count Map Reduce program to understand the Map Reduce paradigm.

## Run a basic Word Count Map Reduce program to understand Map Reduce Paradigm

- Map Reduce is a programming model for processing large-scale data sets in parallel and distributed environments.
- Map Reduce consists of two phases: Map and Reduce.
- In the Map phase, the input data is split into smaller chunks and assigned to different workers (mappers) that apply a user-defined function (map function) to each chunk and produce intermediate key-value pairs.
- In the Reduce phase, the intermediate key-value pairs are shuffled and sorted by their keys and assigned to different workers (reducers) that apply a user-defined function (reduce function) to each group of values with the same key and produce the final output.
- A Word Count Map Reduce program is a simple example of using the Map Reduce paradigm to count the frequency of words in a text file.
- The steps of the Word Count Map Reduce program are as follows:

  - The input text file is split into smaller chunks and assigned to different mappers.
  - Each mapper reads a chunk of the text file and emits a key-value pair for each word in the chunk, where the key is the word and the value is 1.
  - The intermediate key-value pairs are shuffled and sorted by their keys and assigned to different reducers.
  - Each reducer receives a list of values for each key (word) and sums up the values to get the total count of the word and emits a key-value pair with the word and its count as the output.