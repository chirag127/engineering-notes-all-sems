MapReduce is a programming model for processing large data sets in parallel and distributed manner. It consists of two phases: map and reduce. The map phase takes an input data set and applies a user-defined function to each element, producing a set of intermediate key-value pairs. The reduce phase takes the intermediate key-value pairs and merges them according to the user-defined function, producing the final output.

A diagram for a real-world MapReduce example is shown below. The example is a word count program that counts the frequency of each word in a collection of documents. The diagram illustrates the steps involved in the map and reduce phases, as well as the data flow between them.

#### Real-world Map Reduce
```
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|  Document 1    |     |  Document 2    |     |  Document 3    |
|                |     |                |     |                |
+-------+--------+     +-------+--------+     +-------+--------+
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        v                      v                      v
+-------+--------+     +-------+--------+     +-------+--------+
|                |     |                |     |                |
|  Map Function  |     |  Map Function  |     |  Map Function  |
|                |     |                |     |                |
+-------+--------+     +-------+--------+     +-------+--------+
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        v                      v                      v
+-------+--------+     +-------+--------+     +-------+--------+
|                |     |                |     |                |
|  Key-Value     |     |  Key-Value     |     |  Key-Value     |
|  Pairs         |     |  Pairs         |     |  Pairs         |
|                |     |                |     |                |
+-------+--------+     +-------+--------+     +-------+--------+
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        +---------------------->                      |
        |                      |                      |
        |                      +----------------------+
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        v                      v                      v
+-------+--------+     +-------+--------+     +-------+--------+
|                |     |                |     |                |
|  Shuffle and   |     |  Shuffle and   |     |  Shuffle and   |
|  Sort          |     |  Sort          |     |  Sort          |
|                |     |                |     |                |
+-------+--------+     +-------+--------+     +-------+--------+
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        +---------------------->                      |
        |                      |                      |
        |                      +----------------------+
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        v                      v                      v
+-------+--------+     +-------+--------+     +-------+--------+
|                |     |                |     |                |
|  Reduce        |     |  Reduce        |     |  Reduce        |
|  Function      |     |  Function      |     |  Function      |
|                |     |                |     |                |

```
