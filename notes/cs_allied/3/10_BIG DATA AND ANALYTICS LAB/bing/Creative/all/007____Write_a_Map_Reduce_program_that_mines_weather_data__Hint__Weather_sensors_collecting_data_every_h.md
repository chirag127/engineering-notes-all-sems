# Write a Map Reduce program that mines weather data. Hint: Weather sensors collecting data every hour at many locations across the globe gather a large volume of log data, which is a good candidate for analysis with Map Reduce, since it is semi structured and record-oriented for the notes of the BIG DATA AND ANALYTICS LAB in the subject of BIG DATA AND ANALYTICS LAB

- Map Reduce is a programming model that allows processing large-scale data sets in parallel on a cluster of machines.
- Weather data is a type of semi-structured data that consists of records with different attributes, such as date, time, location, temperature, humidity, wind speed, etc.
- Weather data can be mined using Map Reduce to perform various tasks, such as finding the average temperature for each month, identifying the hottest or coldest days, detecting anomalies or outliers, etc.
- To write a Map Reduce program that mines weather data, one needs to follow these steps:

  - Define the input and output formats of the data. For example, the input data can be a text file with comma-separated values, and the output data can be a text file with key-value pairs.
  - Define the mapper function that takes a record of weather data as input and emits a key-value pair as output. The key can be any attribute or combination of attributes that defines a group or a category, such as the month, the location, the temperature range, etc. The value can be any attribute or aggregation of attributes that represents a measure or a statistic, such as the temperature, the count, the average, the sum, etc. For example, if the task is to find the average temperature for each month, the mapper function can emit the month as the key and the temperature as the value for each record.
  - Define the reducer function that takes a key and a list of values as input and emits a key-value pair as output. The reducer function can perform any operation or computation on the values, such as finding the average, the maximum, the minimum, the standard deviation, etc. For example, if the task is to find the average temperature for each month, the reducer function can emit the month as the key and the average of the temperatures as the value for each key.
  - Run the Map Reduce program on a cluster of machines using a framework such as Hadoop or Spark. The framework will take care of distributing the data, executing the mapper and reducer functions, and collecting the results.

- Here is an example of a Map Reduce program that mines weather data to find the average temperature for each month using Python and Hadoop:

  - The input data is a text file named weather.txt with the following format:

    ```
    date,time,location,temperature,humidity,wind
    2023-01-01,00:00:00,New York,5,80,10
    2023-01-01,01:00:00,New York,4,82,12
    2023-01-01,02:00:00,New York,3,84,14
    ...
    2023-01-01,00:00:00,London,8,75,8
    2023-01-01,01:00:00,London,7,77,10
    2023-01-01,02:00:00,London,6,79,12
    ...
    ```

  - The mapper function is a Python script named mapper.py with the following code:

    ```python
    #!/usr/bin/env python
    import sys
    # read each line from standard input
    for line in sys.stdin:
      # split the line into fields
      fields = line.split(",")
      # extract the date and temperature fields
      date = fields[0]
      temperature = fields[3]
      # extract the month from the date
      month = date[5:7]
      # emit the month as the key and the temperature as the value
      print(f"{month}\t{temperature}")
    ```

  - The reducer function is a Python script named reducer.py with the following code:

    ```python
    #!/usr/bin/env python
    import sys
    # initialize the current key and the list of values
    current_key = None
    current_values = []
    # read each line from standard input
    for line in sys.stdin:
      # split the line into key and value
      key, value = line.split("\t")
      # convert the value to a float
      value = float(value)
      # if the key is the same as the current key, append the value to the list
      if key == current_key:
        current_values.append

```
