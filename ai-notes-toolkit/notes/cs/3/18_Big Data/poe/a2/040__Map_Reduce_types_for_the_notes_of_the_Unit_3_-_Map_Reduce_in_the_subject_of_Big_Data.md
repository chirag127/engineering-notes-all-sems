 Here is the content in Markdown format without emojis or external links, being formal and writing in points:

### Map Reduce types for the notes of the Unit 3 - Map Reduce in the subject of Big Data

1.  Map Reduce - Map Reduce is a programming model for processing large data sets with a parallel, distributed algorithm on a cluster.
2.  Types of Map Reduce jobs - There are 2 types of Map Reduce jobs:
    - Map only job - Only the map phase is executed. Reduce phase is not required if the processing can be done in the map phase only. Eg: calculating averages.
    - Map and Reduce job - Both map and reduce phases are executed. Map phase processes the input data and generates output which is sorted and shuffled to be processed by reducers. Eg: finding top 10 occurrences of words from a dataset.
3.  Working of Map Reduce - The working of Map Reduce is as follows:
    - Input data is split into multiple splits which are processed by multiple mappers in parallel.
    - Mappers process the input and generate intermediate key-value pairs.
    - The intermediate data is shuffled and sorted to be sent to the reducers.
    - Reducers aggregate the shuffled data and generate the final output.
4.  Benefits of Map Reduce - The benefits of Map Reduce are:
    - Scalability - It is scalable to large clusters and huge datasets.
    - Fault Tolerance - It is fault tolerant as the jobs are divided into tasks and replicas can be run in case of failures.
    - Low Cost - It uses a large number of commodity machines leading to low cost.
    - Data Locality - It tries to schedule tasks on the nodes containing the data leading to data locality.