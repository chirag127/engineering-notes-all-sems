#### Map Reduce scripts in Hive

- Map Reduce is a programming model for processing large-scale data sets in parallel and distributed manner.
- Hive is a data warehouse system that provides a SQL-like interface to query and analyze structured and semi-structured data stored in Hadoop.
- Hive can translate SQL queries into Map Reduce jobs and execute them on Hadoop cluster.
- Hive also supports writing custom Map Reduce scripts in various languages, such as Java, Python, Ruby, etc., and use them as user-defined functions (UDFs), user-defined aggregates (UDAFs), or user-defined table-generating functions (UDTFs).
- Map Reduce scripts in Hive can be useful for performing complex data transformations, custom aggregations, or data analysis that cannot be expressed in SQL.
- To write Map Reduce scripts in Hive, one needs to follow these steps:

  - Define the input and output formats of the script, such as TEXTFILE, SEQUENCEFILE, RCFILE, etc.
  - Write the script in the chosen language and save it as a file with the appropriate extension, such as .py, .rb, .java, etc.
  - Add the script file to the distributed cache using the ADD FILE command in Hive.
  - Use the TRANSFORM clause in the SELECT statement to invoke the script and pass the input columns as standard input to the script.
  - Specify the output columns of the script as standard output using the AS clause.
  - Optionally, use the USING clause to specify the command to run the script, such as python, ruby, java, etc.

- For example, the following Hive query uses a Python script to calculate the average rating of each movie in a table called movies:

  ```
  ADD FILE avg_rating.py;

  SELECT TRANSFORM(movie_id, rating)
  USING 'python avg_rating.py'
  AS (movie_id, avg_rating)
  FROM movies
  GROUP BY movie_id;
  ```

  - The Python script avg_rating.py can be written as:

    ```
    #!/usr/bin/env python
    import sys

    # Initialize a dictionary to store the sum and count of ratings for each movie
    ratings = {}

    # Read each line from the standard input
    for line in sys.stdin:
      # Split the line by tab and get the movie_id and rating
      movie_id, rating = line.strip().split('\t')
      # Convert the rating to a float
      rating = float(rating)
      # If the movie_id is not in the dictionary, initialize its sum and count to zero
      if movie_id not in ratings:
        ratings[movie_id] = [0, 0]
      # Add the rating to the sum and increment the count for the movie_id
      ratings[movie_id][0] += rating
      ratings[movie_id][1] += 1

    # For each movie_id in the dictionary, calculate the average rating and print it to the standard output
    for movie_id in ratings:
      avg_rating = ratings[movie_id][0] / ratings[movie_id][1]
      print(movie_id + '\t' + str(avg_rating))
    ```

- Some advantages of using Map Reduce scripts in Hive are:

  - They can leverage the existing skills and libraries of various programming languages.
  - They can perform complex data transformations or analysis that are not possible or efficient in SQL.
  - They can be reused across different queries or tables.

- Some disadvantages of using Map Reduce scripts in Hive are:

  - They can introduce performance overhead and latency due to the serialization and deserialization of data between Hive and the script.
  - They can be difficult to debug and test, especially for distributed and parallel execution.
  - They can be less portable and maintainable than SQL queries, as they depend on the availability and compatibility of the script language and libraries on the cluster.