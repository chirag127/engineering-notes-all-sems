#### How Map Reduce works

MapReduce is a programming model for processing large data sets with a parallel, distributed algorithm on a cluster. It consists of two main functions: Map and Reduce.

The Map function takes an input pair and produces a set of intermediate key/value pairs. The MapReduce framework then shuffles the intermediate data, grouping values with the same key together, and feeds them to the Reduce function.

The Reduce function accepts an intermediate key and a set of values for that key. It then merges the values to form a smaller set of values, typically zero or one output value per Reduce invocation.

Here is an example of a MapReduce program in Python that counts the number of occurrences of each word in a text file:

```python
from mrjob.job import MRJob

class MRWordFrequencyCount(MRJob):

    def mapper(self, _, line):
        # split the line into words
        words = line.split()
        # emit each word with a count of 1
        for word in words:
            yield (word, 1)

    def reducer(self, key, values):
        # sum the counts for each word
        yield (key, sum(values))

if __name__ == '__main__':
    MRWordFrequencyCount.run()
```

This code defines a MapReduce job that consists of a mapper and a reducer function. The mapper function splits each line into words and emits each word with a count of 1. The reducer function then sums the counts for each word and emits the final word count. This program can be run on a Hadoop cluster to process large text files in parallel.