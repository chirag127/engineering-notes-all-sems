## Run the Pig Latin Scripts to find a max temp for each and every year

Pig Latin is a high-level platform for creating MapReduce programs used with Hadoop. It is an abstraction over MapReduce that achieves the parallel processing of large data sets without requiring the time-consuming development of custom MapReduce programs.

To find the maximum temperature for each year using Pig Latin, follow these steps:

1. Load the data into Pig using the `LOAD` command. The data should be in a format that can be easily parsed by Pig, such as a CSV file.
2. Use the `FOREACH` command to iterate over the data and extract the year and temperature values.
3. Use the `GROUP` command to group the data by year.
4. Use the `MAX` function to find the maximum temperature for each group.
5. Use the `STORE` command to save the results to a file.

Here is an example Pig Latin script that performs these steps:

```
data = LOAD 'temperature_data.csv' USING PigStorage(',') AS (year:int, temperature:float);
year_temperature = FOREACH data GENERATE year, temperature;
grouped_data = GROUP year_temperature BY year;
max_temperature = FOREACH grouped_data GENERATE group, MAX(year_temperature.temperature);
STORE max_temperature INTO 'max_temperature_by_year';
```

This script loads the temperature data from a CSV file, extracts the year and temperature values, groups the data by year, finds the maximum temperature for each year, and saves the results to a file.

Note: The Instructor may add/delete/modify/tune experiments for the notes of the BIG DATA AND ANALYTICS LAB in the subject of BIG DATA AND ANALYTICS LAB. It is important to follow the instructions provided by the instructor to ensure that the Pig Latin script is correctly implemented and produces the desired results.