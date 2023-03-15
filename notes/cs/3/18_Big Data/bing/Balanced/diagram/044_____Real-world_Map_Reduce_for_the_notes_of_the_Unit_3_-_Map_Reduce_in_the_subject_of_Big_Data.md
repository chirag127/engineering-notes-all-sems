### Real-world Map Reduce

- Map Reduce is a framework that was developed to process massive amounts of data efficiently by dividing the work into smaller tasks and distributing them among multiple machines or nodes.
- Map Reduce consists of two phases: Map and Reduce.
  - Map phase: The input data is split into chunks and assigned to different mappers, which are functions that process the data and produce intermediate key-value pairs as output.
  - Reduce phase: The intermediate key-value pairs are shuffled and sorted by their keys and sent to different reducers, which are functions that aggregate the values for each key and produce the final output.
- Map Reduce can be used for various applications, such as word count, inverted index, web log analysis, recommendation systems, etc.
- One example of Map Reduce is how Twitter manages its tweets, which are around 500 million per day.
  - Tokenize: The tweets are tokenized into words and written as key-value pairs, where the key is the word and the value is 1.
  - Filter: The words are filtered to remove unwanted ones, such as stop words, punctuation, etc.
  - Count: The words are counted by adding the values for each key and written as key-value pairs, where the key is the word and the value is the count.
  - Aggregate Counters: The word counts are aggregated into smaller units, such as top 10 words, words by category, etc.