## Run the Pig Latin Scripts to find a max temp for each and every year

In this experiment, we will be using Pig Latin scripts to find the maximum temperature for each year in a dataset. Pig Latin is a high-level language used for processing large datasets in Apache Hadoop. 

To run the Pig Latin script, follow the steps below:

1. Open the Pig Latin script file in the Hadoop cluster.
2. Load the dataset into Pig using the LOAD function. The dataset should be in a comma-separated value (CSV) format.
3. Use the FILTER function to select the temperature column from the dataset.
4. Group the dataset by year using the GROUP BY function.
5. Find the maximum temperature for each year using the MAX function.
6. Store the results in a new file using the STORE function.

Note: The instructor may modify the Pig Latin script to suit the specific dataset being used. 

Here are some key points to keep in mind when running Pig Latin scripts:

- Pig Latin is a scripting language used for processing large datasets in Hadoop.
- Pig Latin scripts are written in a high-level language and are translated into MapReduce jobs by the Pig compiler.
- Pig Latin scripts can be used to perform a wide range of data processing tasks, including filtering, aggregation, and transformation.
- Pig Latin scripts are executed using the Pig engine, which can be run on a Hadoop cluster or a local machine.
- Pig Latin scripts can be used to process data stored in a variety of formats, including CSV, JSON, and Avro.

In conclusion, running Pig Latin scripts is a powerful tool for analyzing large datasets. By using Pig Latin to find the maximum temperature for each year in a dataset, we can gain valuable insights into temperature trends over time. Remember to consult with your instructor for any modifications or adjustments to the scripts.