## Run the Pig Latin Scripts to find a max temp for each and every year.

- Pig Latin is a high-level scripting language that allows users to write complex data transformations using a simple syntax. Pig Latin scripts can run on Apache Hadoop, a framework for distributed processing of large data sets.
- To find the maximum temperature for each year from a data set of weather records, we can use the following steps:

  1. Load the data from a file into a relation using the LOAD operator. The data file should have the following format: station_id, year, month, day, temperature, quality.
  2. Filter out the records that have missing or invalid temperature values using the FILTER operator. The temperature value should be between -500 and 500, and the quality value should be 0, 1, 4, 5, or 9.
  3. Group the records by year using the GROUP operator. This will create a nested relation that contains the year as the key and a bag of records as the value.
  4. Apply the MAX function to each group to find the maximum temperature for that year using the FOREACH operator. The MAX function takes a bag of numeric values and returns the largest one.
  5. Store the results into a file using the STORE operator.

- The Pig Latin script that implements these steps is shown below:

  ```pig
  -- Load the data from a file
  weather = LOAD 'weather_data.txt' USING PigStorage(',') AS (station_id:chararray, year:int, month:int, day:int, temperature:int, quality:int);

  -- Filter out the records with missing or invalid temperature values
  weather_clean = FILTER weather BY temperature >= -500 AND temperature <= 500 AND quality IN (0, 1, 4, 5, 9);

  -- Group the records by year
  weather_by_year = GROUP weather_clean BY year;

  -- Find the maximum temperature for each year
  max_temp_by_year = FOREACH weather_by_year GENERATE group AS year, MAX(weather_clean.temperature) AS max_temp;

  -- Store the results into a file
  STORE max_temp_by_year INTO 'max_temp_by_year.txt' USING PigStorage(',');
  ```

- To run the Pig Latin script, we need to have Pig installed and configured on our system. We can use the pig command to execute the script in either local mode or mapreduce mode. Local mode runs the script on a single machine, while mapreduce mode runs the script on a Hadoop cluster.

  - To run the script in local mode, we can use the following command:

    ```bash
    pig -x local max_temp.pig
    ```

  - To run the script in mapreduce mode, we can use the following command:

    ```bash
    pig -x mapreduce max_temp.pig
    ```

- The output file will contain the year and the maximum temperature for that year, separated by a comma. For example:

  ```txt
  1901,317
  1902,317
  1903,322
  ...
  ```