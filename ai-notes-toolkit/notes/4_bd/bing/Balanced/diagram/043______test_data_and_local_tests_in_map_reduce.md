To test data and local tests in map reduce, you can use the following steps:

1. Prepare some input data in a text file, such as a CSV file, that contains the key-value pairs that you want to process with your map and reduce functions.
2. Write your map and reduce functions in a programming language of your choice, such as Python, and save them as separate scripts, such as map.py and reduce.py.
3. Use a command-line tool, such as cat, to pipe the input data to your map function, and use another tool, such as sort, to sort the output by key before passing it to your reduce function. For example, you can use the following command:

```
cat input.csv | map.py | sort -k1,1 | reduce.py
```

4. Check the output of your reduce function and compare it with the expected output. You can also use a tool, such as diff, to compare the output files.

#### Test data and local tests in map reduce

```
+----------------+     +----------------+     +----------------+     +----------------+
|                |     |                |     |                |     |                |
|   input.csv    |     |    map.py      |     |    sort        |     |   reduce.py    |
|                |     |                |     |                |     |                |
+----------------+     +----------------+     +----------------+     +----------------+
        |                     |                     |                     |
        |                     |                     |                     |
        |                     |                     |                     |
        |                     |                     |                     |
        |                     |                     |                     |
        |                     |                     |                     |
        |                     |                     |                     |
        |                     |                     |                     |
        |                     |                     |                     |
        |                     |                     |                     |
        |                     |                     |                     |
        |                     |                     |                     |
        |                     |                     |                     |
        |                     |                     |                     |
        v                     v                     v                     v
+----------------+     +----------------+     +----------------+     +----------------+
|                |     |                |     |                |     |                |
|   cat          |     |    map         |     |    sort        |     |   reduce       |
|                |     |                |     |                |     |                |
+----------------+     +----------------+     +----------------+     +----------------+
        |                     |                     |                     |
        |                     |                     |                     |
        |                     |                     |                     |
        |                     |                     |                     |
        |                     |                     |                     |
        |                     |                     |                     |
        |                     |                     |                     |
        |                     |                     |                     |
        v                     v                     v                     v
+----------------+     +----------------+     +----------------+     +----------------+
|                |     |                |     |                |     |                |
|   output       |     |    output      |     |    output      |     |   output       |
|                |     |                |     |                |     |                |
+----------------+     +----------------+     +----------------+     +----------------+
```