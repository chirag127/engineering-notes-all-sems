#### Map Reduce features

MapReduce is a programming model and an associated implementation for processing and generating large data sets. It has the following features:

- **Scalability**: MapReduce can process large amounts of data by dividing the work among multiple nodes in a cluster.

- **Fault tolerance**: MapReduce can handle node failures by reassigning the work to other nodes.

- **Data locality**: MapReduce tries to move the computation to the data, rather than moving the data to the computation. This reduces the amount of data that needs to be transferred over the network.

- **Simplicity**: MapReduce provides a simple programming model that abstracts away many of the complexities of distributed computing.

Here is an example of a simple MapReduce program in Python that counts the number of occurrences of each word in a text file:

```python
from mrjob.job import MRJob

class MRWordFrequencyCount(MRJob):

    def mapper(self, _, line):
        # yield each word in the line
        for word in line.split():
            yield (word.lower(), 1)

    def reducer(self, key, values):
        # sum the values for each word
        yield (key, sum(values))

if __name__ == '__main__':
    MRWordFrequencyCount.run()
```