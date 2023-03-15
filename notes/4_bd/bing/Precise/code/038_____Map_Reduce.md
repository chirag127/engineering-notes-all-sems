### Map Reduce

MapReduce is a programming model for processing large data sets with a parallel, distributed algorithm on a cluster. Here is an example of a simple MapReduce program in Python that counts the occurrences of words in a text file:

```python
from collections import defaultdict
import sys

def map_function(document):
    words = document.split()
    for word in words:
        yield (word, 1)

def reduce_function(key, values):
    yield (key, sum(values))

def main():
    intermediate = defaultdict(list)
    for line in sys.stdin:
        for key, value in map_function(line):
            intermediate[key].append(value)

    for key, values in intermediate.items():
        for result in reduce_function(key, values):
            print(result)

if __name__ == '__main__':
    main()
```