## Write a Map Reduce program that mines weather data. Hint: Weather sensors collecting data every hour at many locations across the globe gather a large volume of log data, which is a good candidate for analysis with Map Reduce, since it is semi structured and record-oriented for the notes of the BIG DATA AND ANALYTICS LAB in the subject of BIG DATA AND ANALYTICS LAB

- Map Reduce is a programming model that allows processing large-scale data sets in parallel on a cluster of machines.
- A Map Reduce program consists of two functions: a map function and a reduce function.
- The map function takes an input key-value pair and produces a set of intermediate key-value pairs.
- The reduce function takes an intermediate key and a set of values associated with that key and produces a set of output key-value pairs.
- The Map Reduce framework handles the distribution of data, the scheduling of tasks, the fault tolerance, and the aggregation of results.

- To write a Map Reduce program that mines weather data, we need to define the input, output, map, and reduce functions.
- The input data can be a set of weather records, each containing information such as location, date, time, temperature, humidity, wind speed, etc.
- The output data can be a set of statistics, such as the average temperature, the maximum wind speed, the number of rainy days, etc., for each location or time period.
- The map function can parse each weather record and emit intermediate key-value pairs, where the key can be a location or a time period, and the value can be a weather attribute, such as temperature, wind speed, etc.
- The reduce function can aggregate the values for each key and compute the statistics, such as the average, the maximum, the count, etc., and emit the output key-value pairs.

- For example, if we want to find the average temperature for each month in each location, we can write the following pseudo-code:

```python
# map function
def map(key, value):
  # key is the file name, value is the weather record
  # parse the weather record and extract the location, month, and temperature
  location = value.location
  month = value.date.month
  temperature = value.temperature
  # emit the intermediate key-value pair, where the key is a tuple of location and month, and the value is the temperature
  emit((location, month), temperature)

# reduce function
def reduce(key, values):
  # key is a tuple of location and month, values is a list of temperatures
  # compute the average temperature
  sum = 0
  count = 0
  for value in values:
    sum += value
    count += 1
  average = sum / count
  # emit the output key-value pair, where the key is the same as the input key, and the value is the average temperature
  emit(key, average)
```