#### Test data and local tests in map reduce

One way to test map and reduce code locally is to use hadoop streaming, which allows you to write map and reduce scripts in any language that can read from standard input and write to standard output. For example, if you have a map.py and a reduce.py script in Python, you can test them locally by running the following command:

`cat *.csv | map.py | sort -k1,1 | reduce.py`

This will simulate the map and reduce phases of a map reduce job, using the csv files in the current directory as the input data. The sort command is necessary to group the key-value pairs by key before passing them to the reducer. The output of the reduce script will be printed to the standard output.

The following diagram illustrates the basic architecture of a map reduce job using hadoop streaming:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|   Input data    |     |   Map script    |     |   Reduce script |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       v                       v                       v
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|   Standard      |     |   Standard      |     |   Standard      |
|   input         |     |   input         |     |   input         |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       v                       |
       |                 +-----------------+           |
       |                 |                 |           |
       |                 |   Sort by key   |           |
       |                 |                 |           |
       |                 +-----------------+           |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       v                       v
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|   Standard      |     |   Standard      |     |   Standard      |
|   output        |     |   output        |     |   output        |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
```