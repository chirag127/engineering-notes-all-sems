#### Real-world Map Reduce

Map Reduce is a programming model for processing large-scale data sets in parallel and distributed environments. It consists of two phases: map and reduce. The map phase applies a user-defined function to each input record and produces a set of intermediate key-value pairs. The reduce phase applies another user-defined function to all the values associated with the same key and produces a set of output records.

Here is an example of a Map Reduce program that counts the number of occurrences of each word in a text file. The input file is split into chunks and assigned to different map tasks. Each map task reads a chunk of the file and emits a key-value pair for each word, where the key is the word and the value is 1. The intermediate key-value pairs are shuffled and sorted by key and sent to different reduce tasks. Each reduce task receives a list of values for each key and sums them up to get the final count of each word. The output of the reduce tasks is written to a file or a database.

The code for the map and reduce functions is written in Python and can be executed using the Hadoop framework.

```python
# map function
def map(key, value):
  # key: document name
  # value: document contents
  for word in value.split():
    # emit a key-value pair for each word
    emit(word, 1)

# reduce function
def reduce(key, values):
  # key: a word
  # values: a list of counts
  # sum up the counts for each word
  total = 0
  for count in values:
    total += count
  # emit the word and its total count
  emit(key, total)
```