## Unit 2 - Hadoop and Map Reduce

Hadoop is an open-source software framework for storing and processing large datasets using a distributed computing model. It is designed to scale up from single servers to thousands of machines, each offering local computation and storage. The core of Hadoop consists of a storage part, known as Hadoop Distributed File System (HDFS), and a processing part called MapReduce.

MapReduce is a programming model for processing large datasets in parallel across a Hadoop cluster. It consists of two main phases: the Map phase and the Reduce phase. In the Map phase, the input data is divided into chunks and processed by multiple map tasks in parallel. Each map task processes a chunk of data and produces a set of intermediate key-value pairs. In the Reduce phase, the intermediate key-value pairs are grouped by key and processed by multiple reduce tasks in parallel. Each reduce task processes a group of key-value pairs with the same key and produces a set of output values.

Here is an example of a simple MapReduce program that counts the number of occurrences of each word in a text file:

```python
from mrjob.job import MRJob

class MRWordCount(MRJob):

    def mapper(self, _, line):
        # split the line into words
        words = line.split()
        # emit each word as a key with a value of 1
        for word in words:
            yield (word, 1)

    def reducer(self, key, values):
        # sum the values for each key
        yield (key, sum(values))

if __name__ == '__main__':
    MRWordCount.run()
```

This code can be run on a Hadoop cluster using the `mrjob` library. The `mapper` function takes a line of text as input and emits each word in the line as a key with a value of 1. The `reducer` function takes a key (a word) and a list of values (the counts) as input and emits the sum of the values for each key. This produces the final word count for each word in the text file.
