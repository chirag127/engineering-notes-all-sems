## Write a Map Reduce program that mines weather data. Hint: Weather sensors collecting data every hour at many locations across the globe gather a large volume of log data, which is a good candidate for analysis with Map Reduce, since it is semi structured and record-oriented for the notes of the BIG DATA AND ANALYTICS LAB in the subject of BIG DATA AND ANALYTICS LAB

- Map Reduce is a programming model that allows processing large-scale data sets in parallel on a cluster of machines.
- Weather data is a type of semi-structured data that consists of records with different attributes, such as date, time, location, temperature, humidity, wind speed, etc.
- To mine weather data using Map Reduce, we need to define two functions: a mapper function and a reducer function.
- The mapper function takes a record of weather data as input and emits a key-value pair as output. The key is usually a composite of some attributes that define a group or a category of interest, such as year, month, location, etc. The value is usually a numeric attribute that we want to aggregate or analyze, such as temperature, humidity, etc.
- The reducer function takes a key and a list of values as input and emits a key-value pair as output. The key is the same as the input key, and the value is the result of some aggregation or analysis function applied to the list of values, such as sum, average, maximum, minimum, etc.
- For example, if we want to find the average temperature for each month and location, we can write the following mapper and reducer functions in Python:

```python
# mapper function
def mapper(record):
  # split the record by comma
  fields = record.split(",")
  # extract the date, time, location and temperature fields
  date = fields[0]
  time = fields[1]
  location = fields[2]
  temperature = float(fields[3])
  # parse the date to get the year and month
  year, month, day = date.split("-")
  # emit a key-value pair with year, month and location as key and temperature as value
  key = (year, month, location)
  value = temperature
  print(key, value)

# reducer function
def reducer(key, values):
  # calculate the average temperature from the list of values
  sum = 0
  count = 0
  for value in values:
    sum += value
    count += 1
  average = sum / count
  # emit a key-value pair with the same key and the average temperature as value
  print(key, average)
```

- To run the Map Reduce program, we need to use a framework such as Hadoop or Spark that can distribute the data and the computation across a cluster of machines.
- The framework will take care of splitting the input data into chunks, assigning the chunks to different mapper tasks, shuffling and sorting the intermediate key-value pairs, assigning the pairs to different reducer tasks, and collecting the final output.