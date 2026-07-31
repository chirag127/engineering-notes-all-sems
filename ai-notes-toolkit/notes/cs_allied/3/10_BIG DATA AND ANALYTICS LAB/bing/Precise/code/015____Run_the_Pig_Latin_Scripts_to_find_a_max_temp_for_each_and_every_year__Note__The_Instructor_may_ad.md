## Run the Pig Latin Scripts to find a max temp for each and every year

Pig Latin is a high-level platform for creating MapReduce programs used with Hadoop. It is used to analyze large data sets representing them as data flows. Pig Latin scripts are translated into a series of MapReduce jobs that are run on the Apache Hadoop platform.

To find the maximum temperature for each year using Pig Latin scripts, the following steps can be followed:

1. Load the data: The first step is to load the data into the Pig script. This can be done using the `LOAD` command. The data should be in a format that can be easily parsed by Pig, such as CSV or TSV.

```pig
data = LOAD 'hdfs://data/temperature_data.csv' USING PigStorage(',') AS (year:int, temperature:float);
```

2. Group the data by year: The next step is to group the data by year. This can be done using the `GROUP` command.

```pig
grouped_data = GROUP data BY year;
```

3. Find the maximum temperature for each year: Once the data is grouped by year, the maximum temperature for each year can be found using the `MAX` function.

```pig
max_temp = FOREACH grouped_data GENERATE group AS year, MAX(data.temperature) AS max_temperature;
```

4. Store the results: The final step is to store the results. This can be done using the `STORE` command.

```pig
STORE max_temp INTO 'hdfs://data/max_temp_by_year' USING PigStorage(',');
```

Note: The Instructor may add/delete/modify/tune experiments for the notes of the BIG DATA AND ANALYTICS LAB in the subject of BIG DATA AND ANALYTICS LAB. It is important to follow the instructions provided by the instructor and adapt the script accordingly.