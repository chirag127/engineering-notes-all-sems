# Real-world Map Reduce

MapReduce is a programming model and an associated implementation for processing and generating big data sets with a parallel, distributed algorithm on a cluster.

A MapReduce program is composed of a map procedure, which performs filtering and sorting (such as sorting students by first name into queues, one queue for each name), and a reduce method, which performs a summary operation (such as counting the number of students in each queue, yielding name frequencies).

The map and reduce functions are both defined with respect to data structured in (key, value) pairs. Map takes one pair of data with a type in one data domain, and returns a list of pairs in a different domain:

map (k1,v1) → list(k2,v2)

The map function is applied in parallel to every pair (keyed by k1) in the input dataset. This produces a list of pairs (keyed by k2) for each call. After that, the MapReduce framework collects all pairs with the same key (k2) from all lists and groups them together, creating one group for each key.

The reduce function is then applied in parallel to each group, which in turn produces a collection of values in the same domain:

reduce (k2, list (v2)) → list(v3)

Each reduce call typically produces either one value v3 or an empty return, though one call is allowed to return more than one value. The returns of all calls are collected as the desired result list.

## Examples

### Word Count

One of the simplest and most common examples of MapReduce is counting the number of occurrences of each word in a large text corpus. The map function takes a line of text as input and outputs a key-value pair for each word in the line, where the key is the word and the value is 1. For example, the line "Hello world" would produce the output:

(Hello, 1)
(world, 1)

The reduce function takes a key and a list of values as input and outputs a key-value pair where the key is the same as the input key and the value is the sum of the input values. For example, the input:

(world, [1, 1, 1, 1])

would produce the output:

(world, 4)

The MapReduce framework would then combine the outputs of all the reduce calls and produce the final result, which is a list of words and their frequencies in the text corpus.

### Twitter Analysis

Another example of MapReduce is analyzing the tweets from Twitter. The map function takes a tweet as input and outputs a key-value pair for each token (word or hashtag) in the tweet, where the key is the token and the value is the tweet itself. For example, the tweet "I love #mapreduce" would produce the output:

(I, I love #mapreduce)
(love, I love #mapreduce)
(#mapreduce, I love #mapreduce)

The reduce function takes a key and a list of values as input and outputs a key-value pair where the key is the same as the input key and the value is a filtered list of tweets that contain the key. For example, the input:

(#mapreduce, [I love #mapreduce, #mapreduce is awesome, Learning #mapreduce today])

would produce the output:

(#mapreduce, [I love #mapreduce, #mapreduce is awesome, Learning #mapreduce today])

The MapReduce framework would then combine the outputs of all the reduce calls and produce the final result, which is a list of tokens and the tweets that contain them. This can be used for various purposes, such as sentiment analysis, topic modeling, or trend detection.