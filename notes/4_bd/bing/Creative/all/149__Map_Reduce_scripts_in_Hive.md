#### Map Reduce scripts in Hive

- Map Reduce is a programming model for processing large-scale data sets in parallel and distributed manner.
- Hive is a data warehouse system that provides a SQL-like interface to query and analyze data stored in Hadoop.
- Hive can translate SQL queries into Map Reduce jobs and execute them on Hadoop cluster.
- Hive also supports writing custom Map Reduce scripts in various languages, such as Java, Python, Ruby, etc., and use them as user-defined functions (UDFs), user-defined aggregates (UDAFs), or user-defined table-generating functions (UDTFs).
- Map Reduce scripts in Hive can be useful for performing complex data transformations, custom aggregations, or data analysis that cannot be expressed in SQL.
- To write a Map Reduce script in Hive, one needs to follow these steps:

  - Define the input and output formats of the script, such as text, sequence file, JSON, etc.
  - Write the mapper and reducer functions in the chosen language, and make sure they read from standard input and write to standard output.
  - Package the script and any dependencies into a JAR file, and add it to the distributed cache using `ADD FILE` or `ADD JAR` commands in Hive.
  - Use the `TRANSFORM` clause in Hive query to invoke the script as a UDF, UDAF, or UDTF, and specify the input and output formats using `ROW FORMAT` and `SERDE` clauses.
  - Optionally, use the `MAPREDUCE` clause in Hive query to specify the number of mappers and reducers, and any other Map Reduce parameters.

- For example, suppose we have a table `sales` with columns `date`, `product`, `quantity`, and `price`, and we want to calculate the total revenue per product per month using a Python script. We can write the script as follows:

  ```python
  #!/usr/bin/env python
  import sys
  from datetime import datetime

  # A mapper function that reads each line from standard input, parses the date and product columns, and emits a key-value pair of (product, month) and price
  def mapper():
      for line in sys.stdin:
          line = line.strip()
          date, product, quantity, price = line.split('\t')
          date = datetime.strptime(date, '%Y-%m-%d')
          month = date.strftime('%Y-%m')
          print('%s\t%s\t%s' % (product, month, price))

  # A reducer function that reads each key-value pair from standard input, groups them by key, and sums up the values to get the total revenue
  def reducer():
      current_key = None
      current_sum = 0.0
      for line in sys.stdin:
          line = line.strip()
          key, value = line.split('\t', 1)
          value = float(value)
          if current_key == key:
              current_sum += value
          else:
              if current_key:
                  print('%s\t%.2f' % (current_key, current_sum))
              current_key = key
              current_sum = value
      if current_key:
          print('%s\t%.2f' % (current_key, current_sum))

  if __name__ == '__main__':
      mapper()
      reducer()
  ```

  - We can save this script as `revenue.py`, and package it into a JAR file using `zip revenue.jar revenue.py`.
  - We can then add the JAR file to the distributed cache using `ADD FILE revenue.jar;` in Hive.
  - We can then use the `TRANSFORM` clause to invoke the script as a UDTF, and specify the input and output formats using `ROW FORMAT DELIMITED` and `SERDE 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe'` clauses. We can also use the `MAPREDUCE` clause to specify the number of reducers as 1, and any other Map Reduce parameters.
  - The final Hive query would look like this:

  ```sql
  ADD FILE revenue.jar;
  SELECT product, month, revenue
  FROM (
    SELECT TRANSFORM(date, product, quantity, price)
    USING 'python revenue.py'
    AS (product, month, revenue)
    ROW FORMAT DELIMITED
    FIELDS TERMINATED BY '\t'
    LINES TERMINATED BY '\n'
    MAPREDUCE
    NUMREDUCERS 1
    FROM sales
  ) t
  ORDER BY product, month;
  ```

- Some advantages of using Map Reduce scripts in Hive are:

  - They can leverage the existing skills and libraries of various programming languages, such as Java, Python