# Real-world Map Reduce

MapReduce is a programming model and an associated implementation for processing and generating big data sets with a parallel, distributed algorithm on a cluster.

A MapReduce program is composed of a map procedure, which performs filtering and sorting (such as sorting students by first name into queues, one queue for each name), and a reduce method, which performs a summary operation (such as counting the number of students in each queue, yielding name frequencies).

The map and reduce functions are both defined with respect to data structured in (key, value) pairs. Map takes one pair of data with a type in one data domain, and returns a list of pairs in a different domain:

map (k1,v1) → list(k2,v2)

The map function is applied in parallel to every pair (keyed by k1) in the input dataset. This produces a list of pairs (keyed by k2) for each call. After that, the MapReduce framework collects all pairs with the same key (k2) from all lists and groups them together, creating one group for each key.

The reduce function is then applied in parallel to each group, which in turn produces a collection of values in the same domain:

reduce (k2, list (v2)) → list(v3)

Each reduce call typically produces either one value v3 or an empty return, though one call is allowed to return more than one value. The returns of all calls are collected as the desired result list.

## Example: Word Count

One of the simplest and most common examples of MapReduce is counting the frequency of words in a large text corpus. The map function takes a document and emits a key-value pair for each word in the document, with the word as the key and the value as 1. The reduce function takes a word and a list of values, and sums up the values to get the total count of the word.

The pseudocode for the map and reduce functions are as follows:

```
map(document):
  for each word w in document:
    emit (w, 1)

reduce(word, values):
  count = 0
  for each v in values:
    count = count + v
  emit (word, count)
```

The following diagram illustrates the execution of the word count example on a small input of four documents:

![word count example](https://www.tutorialspoint.com/map_reduce/images/mapreduce_example.jpg)

## Example: Twitter Analysis

Another real-world example of MapReduce is analyzing the tweets from Twitter. Twitter receives around 500 million tweets per day, which is nearly 3000 tweets per second. The following steps show how Twitter manages its tweets with the help of MapReduce:

1. Tokenize: Tokenizes the tweets into maps of tokens and writes them as key-value pairs. For example, the tweet "I love MapReduce" is tokenized into (I, 1), (love, 1), (MapReduce, 1).
2. Filter: Filters unwanted words from the maps of tokens and writes the filtered maps as key-value pairs. For example, the word "I" is filtered out as it is not relevant for analysis.
3. Count: Generates a token counter per word. For example, the word "love" has a counter of 10 if it appears 10 times in the tweets.
4. Aggregate Counters: Prepares an aggregate of similar counter values into small manageable units. For example, the word "MapReduce" has an aggregate counter of 100 if it appears 100 times in the tweets.

The following diagram illustrates the execution of the Twitter analysis example on a small input of four tweets:

![twitter analysis example](https://www.tutorialspoint.com/map_reduce/images/mapreduce_example1.jpg)