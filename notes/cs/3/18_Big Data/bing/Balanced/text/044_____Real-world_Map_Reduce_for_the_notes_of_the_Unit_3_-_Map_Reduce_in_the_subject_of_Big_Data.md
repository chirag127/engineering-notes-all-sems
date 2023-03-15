### Real-world Map Reduce

- Map Reduce is a framework that was developed to process massive amounts of data efficiently by dividing the work into smaller tasks and distributing them across a cluster of machines.
- Map Reduce consists of two phases: Map and Reduce.
  - Map phase: The input data is split into chunks and assigned to different mappers, which are processes that apply a user-defined function to each chunk and produce intermediate key-value pairs as output.
  - Reduce phase: The intermediate key-value pairs are shuffled and sorted by their keys and sent to different reducers, which are processes that apply another user-defined function to each group of values with the same key and produce the final output.
- Map Reduce can be used for various applications, such as word count, inverted index, web log analysis, recommendation systems, etc.
- One example of a real-world Map Reduce application is Twitter, which receives around 500 million tweets per day, which is nearly 3000 tweets per second .
  - Twitter uses Map Reduce to analyze the tweets and extract useful information, such as trending topics, sentiment analysis, user behavior, etc.
  - One possible Map Reduce workflow for Twitter is as follows:
    - Tokenize: Tokenizes the tweets into maps of tokens and writes them as key-value pairs, where the key is the token and the value is 1.
    - Filter: Filters unwanted words from the maps of tokens, such as stop words, punctuation, etc., and writes the filtered maps as key-value pairs.
    - Count: Generates a token counter per word by aggregating the values with the same key and writes the key-value pairs, where the key is the word and the value is the count.
    - Aggregate Counters: Prepares an aggregate of similar counter values into small manageable units and writes the key-value pairs, where the key is the count and the value is the list of words with that count.
    - Sort: Sorts the key-value pairs by the key in descending order and writes the key-value pairs, where the key is the count and the value is the list of words with that count.
    - Top N: Selects the top N key-value pairs and writes the key-value pairs, where the key is the count and the value is the list of words with that count. This gives the most frequent words in the tweets.