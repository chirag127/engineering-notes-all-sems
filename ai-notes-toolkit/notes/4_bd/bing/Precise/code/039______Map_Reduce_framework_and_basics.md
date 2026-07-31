#### Map Reduce framework and basics

MapReduce is a programming model and an associated implementation for processing and generating large data sets. Users specify a map function that processes a key/value pair to generate a set of intermediate key/value pairs, and a reduce function that merges all intermediate values associated with the same intermediate key.

Here is an example of a simple MapReduce program in Python that counts the number of occurrences of each word in a text file:

```python
from mrjob.job import MRJob

class MRWordFrequencyCount(MRJob):

    def mapper(self, _, line):
        # yield each word in the line
        for word in line.split():
            yield (word.lower(), 1)

    def reducer(self, key, values):
        # sum the words we've seen so far
        yield (key, sum(values))

if __name__ == '__main__':
    MRWordFrequencyCount.run()
```

This code defines a MapReduce job that consists of a mapper function and a reducer function. The mapper function takes a line of text as input and outputs a key-value pair for each word in the line, where the key is the word and the value is 1. The reducer function takes a key and a list of values as input and outputs the sum of the values for that key, which represents the number of occurrences of the word in the text file.
