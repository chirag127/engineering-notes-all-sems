#### Map Reduce scripts in Hive

- Map Reduce is a programming model for processing large-scale data sets in parallel and distributed manner.
- Hive is a data warehousing platform that supports SQL-like queries and Map Reduce operations on structured and semi-structured data.
- Users can plug in their own custom mappers and reducers in the data stream by using the TRANSFORM clause in the Hive language .
- The TRANSFORM clause allows the user to specify an executable script or program that can read the input data from stdin and write the output data to stdout.
- The input and output data formats are determined by the user and the script or program.
- The script or program can be written in any language that can handle text data, such as Python, Perl, Ruby, etc.
- The script or program can also access external resources, such as files, databases, web services, etc.
- The syntax of the TRANSFORM clause is as follows:

```sql
SELECT TRANSFORM (input_columns) [IN input_format]
USING 'script' [AS output_columns] [OUT output_format]
FROM table
[WHERE condition]
[GROUP BY columns]
[CLUSTER BY columns]
[DISTRIBUTE BY columns]
[SORT BY columns]
[LIMIT number]
```

- The input_columns are the columns from the table that are passed to the script as input.
- The input_format is an optional clause that specifies the format of the input data, such as ROW FORMAT DELIMITED, AVRO, etc.
- The script is the path or name of the executable script or program that performs the transformation.
- The output_columns are the columns that are returned by the script as output.
- The output_format is an optional clause that specifies the format of the output data, such as ROW FORMAT DELIMITED, AVRO, etc.
- The other clauses are the same as in a regular SELECT statement.

- An example of using the TRANSFORM clause is as follows:

```sql
-- This query uses a Python script to calculate the average temperature for each city
SELECT TRANSFORM (city, temperature)
USING 'python avg_temp.py'
AS city, avg_temp
FROM weather
GROUP BY city;
```

- The Python script avg_temp.py can be something like this:

```python
#!/usr/bin/env python
import sys

# A dictionary to store the sum and count of temperatures for each city
city_temp = {}

# Read the input data from stdin line by line
for line in sys.stdin:
  # Split the line by tab and get the city and temperature
  city, temp = line.strip().split('\t')
  # Convert the temperature to float
  temp = float(temp)
  # If the city is not in the dictionary, initialize it with zero sum and count
  if city not in city_temp:
    city_temp[city] = [0.0, 0]
  # Add the temperature to the sum and increment the count
  city_temp[city][0] += temp
  city_temp[city][1] += 1

# For each city, calculate the average temperature and write it to stdout
for city in city_temp:
  # Get the sum and count of temperatures for the city
  sum_temp, count_temp = city_temp[city]
  # Calculate the average temperature
  avg_temp = sum_temp / count_temp
  # Write the city and the average temperature to stdout, separated by tab
  print(city + '\t' + str(avg_temp))
```

- The output of the query and the script will be something like this:

```
New York    15.6
Los Angeles 22.3
Chicago     12.4
...
```