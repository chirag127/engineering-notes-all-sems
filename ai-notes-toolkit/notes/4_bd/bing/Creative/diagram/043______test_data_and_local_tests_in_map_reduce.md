Hello, I am Sydney, your AI assistant. I can help you with drawing a detailed ASCII diagram for test data and local tests in map reduce. 

According to the search results, one way to test map and reduce code locally is to use the hadoop streaming command, which takes the input data from standard input and passes it to the mapper script, then sorts the output by key and passes it to the reducer script. For example, if you have a CSV file as your input data and a Python script as your mapper and reducer, you can run the following command:

cat *.csv | map.py | sort -k1,1 | reducer.py

The diagram below shows the flow of data and the execution of the scripts in this command.

#### Test data and local tests in map reduce

```
+----------------+     +----------------+     +----------------+     +----------------+
|                |     |                |     |                |     |                |
|  Input data    |     |   Mapper       |     |   Sorter       |     |   Reducer      |
|  (CSV file)    |     |   (map.py)     |     |   (sort -k1,1) |     |   (reducer.py) |
|                |     |                |     |                |     |                |
+----------------+     +----------------+     +----------------+     +----------------+
       |                      |                      |                      |
       |                      |                      |                      |
       |                      |                      |                      |
       |                      |                      |                      |
       |                      |                      |                      |
       |                      |                      |                      |
       |                      |                      |                      |
       |                      |                      |                      |
       |                      |                      |                      |
       |                      |                      |                      |
       |                      |                      |                      |
       |                      |                      |                      |
       |                      |                      |                      |
       |                      |                      |                      |
       |                      |                      |                      |
       |                      |                      |                      |
       |                      |                      |                      |
       |                      |                      |                      |
       |                      |                      |                      |
       |                      |                      |                      |
       V                      V                      V                      V
+----------------+     +----------------+     +----------------+     +----------------+
|                |     |                |     |                |     |                |
|  Standard      |     |  Standard      |     |  Standard      |     |  Standard      |
|  input         |     |  output        |     |  input         |     |  output        |
|                |     |                |     |                |     |                |
+----------------+     +----------------+     +----------------+     +----------------+
```
