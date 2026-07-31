## Run the Pig Latin Scripts to find a max temp for each and every year.

- Pig Latin is a high-level scripting language that allows users to write complex data transformations using a simple syntax. Pig Latin scripts can run on Apache Hadoop, a framework for distributed processing of large data sets.
- To find the maximum temperature for each year from a data set of weather records, we can use the following steps in Pig Latin:

  1. Load the data from a file into a relation using the `LOAD` statement. Specify the schema of the data using the `AS` clause. For example, if the data file has four fields: station, year, month, and temperature, we can load it as follows:

  ```
  weather = LOAD 'weather_data.txt' USING PigStorage(',') AS (station:chararray, year:int, month:int, temperature:float);
  ```

  2. Filter out the records that have missing or invalid temperature values using the `FILTER` statement. For example, if the temperature value is -9999, it means it is missing or invalid. We can filter out such records as follows:

  ```
  weather = FILTER weather BY temperature != -9999;
  ```

  3. Group the records by year using the `GROUP` statement. This will create a nested relation where each group has a bag of records that belong to the same year. For example, we can group the records by year as follows:

  ```
  weather_by_year = GROUP weather BY year;
  ```

  4. Find the maximum temperature for each group using the `MAX` function and the `FOREACH` statement. The `MAX` function takes a bag of numeric values and returns the maximum value. The `FOREACH` statement allows us to apply a transformation to each group. For example, we can find the maximum temperature for each year as follows:

  ```
  max_temp_by_year = FOREACH weather_by_year GENERATE group AS year, MAX(weather.temperature) AS max_temp;
  ```

  5. Store the result into a file using the `STORE` statement. Specify the output format and the delimiter using the `USING` clause. For example, we can store the result as a comma-separated file as follows:

  ```
  STORE max_temp_by_year INTO 'max_temp_by_year.txt' USING PigStorage(',');
  ```

- To run the Pig Latin script, we can use the following options:

  - Run the script in local mode, where Pig runs on a single machine without Hadoop. This is useful for testing and debugging purposes. To run the script in local mode, we can use the `-x local` option with the `pig` command. For example:

  ```
  pig -x local max_temp.pig
  ```

  - Run the script in mapreduce mode, where Pig runs on a Hadoop cluster and uses MapReduce to execute the script. This is useful for processing large data sets in a distributed manner. To run the script in mapreduce mode, we can use the `-x mapreduce` option with the `pig` command. For example:

  ```
  pig -x mapreduce max_temp.pig
  ```

  - Run the script in interactive mode, where Pig runs in a shell and allows us to enter Pig Latin statements one by one and see the results. This is useful for exploring and analyzing data interactively. To run the script in interactive mode, we can use the `pig` command without any options. For example:

  ```
  pig
  grunt> exec max_temp.pig
  ```