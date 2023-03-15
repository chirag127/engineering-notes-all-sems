#### Real-world Map Reduce

MapReduce is a programming model for processing large data sets with a parallel, distributed algorithm on a cluster. Here is an example of a simple MapReduce program that counts the number of occurrences of each word in a given input set:

```python
from mrjob.job import MRJob

class MRWordFrequencyCount(MRJob):

    def mapper(self, _, line):
        # yield each word in the line
        for word in line.split():
            yield word.lower(), 1

    def reducer(self, key, values):
        # sum the values for each word
        yield key, sum(values)

if __name__ == '__main__':
    MRWordFrequencyCount.run()
```

This code can be run on a Hadoop cluster or locally on a single machine. The `mapper` function takes each line of the input data and yields a key-value pair for each word in the line, with the word as the key and the value as 1. The `reducer` function takes the key-value pairs from the `mapper` function and sums the values for each key, yielding the total count for each word.