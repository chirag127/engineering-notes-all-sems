## Run the Pig Latin Scripts to find a max temp for each and every year. Note: The Instructor may add/delete/modify/tune experiments for the notes of the BIG DATA AND ANALYTICS LAB in the subject of BIG DATA AND ANALYTICS LAB

Pig Latin is a high-level platform for processing large datasets in Hadoop. Pig Latin scripts can be used to perform complex data processing tasks, including finding the maximum temperature for each year.

To run a Pig Latin script to find the maximum temperature for each year, you need to perform the following steps:

1. Prepare the data: The data for the Pig Latin script should be stored in a Hadoop Distributed File System (HDFS) and should include the year and temperature for each record.

2. Write the Pig Latin script: The Pig Latin script should be written to perform the following steps:

- Load the data into Pig Latin
- Group the data by year
- Find the maximum temperature for each year
- Store the results in HDFS

Here is an example of a Pig Latin script that performs the above steps:

```
data = LOAD 'hdfs://path/to/data' USING PigStorage(',');
grouped = GROUP data BY year;
max_temp = FOREACH grouped GENERATE group, MAX(data.temp);
STORE max_temp INTO 'hdfs://path/to/results' USING PigStorage(',');
```

3. Run the Pig Latin script: The Pig Latin script can be run using the Pig command line interface or by submitting the script to a Pig job in a Hadoop cluster.

In conclusion, Pig Latin is a high-level platform for processing large datasets in Hadoop, and Pig Latin scripts can be used to perform complex data processing tasks, including finding the maximum temperature for each year. To run a Pig Latin script to find the maximum temperature for each year, you need to prepare the data, write the Pig Latin script, and run the script using the Pig command line interface or by submitting the script to a Pig job in a Hadoop cluster.
