
#### Anatomy of a Map Reduce Job Run

* MapReduce is a programming model and an associated implementation for processing and generating large data sets with a parallel, distributed algorithm on a cluster. 
* The MapReduce model consists of two main tasks: map and reduce. 
* During the map phase, the data set is divided into smaller sub-sets and then each sub-set is mapped to a key-value pair or tuple. 
* The map phase can also perform filtering and sorting operations on the data set. 
* The reduce phase takes the output from the map phase and combines it into a smaller set of tuples. 
* The reduce phase can also perform aggregation operations on the data set.
* The MapReduce job is the process of running the MapReduce algorithm on a data set.
* A MapReduce job typically consists of a job tracker, which is responsible for scheduling tasks, and one or more task trackers, which are responsible for executing the tasks. 
* The job tracker is responsible for monitoring the progress of the job, managing resources and providing fault tolerance. 
* The task tracker is responsible for executing the tasks and reporting the progress to the job tracker.
* In addition to the job tracker and task trackers, a MapReduce job also includes a set of configuration parameters, such as the number of mappers, reducers and input/output formats. 
* The configuration parameters determine how the job is executed, such as the number of mappers and reducers to use, the input and output formats, and the type of data to be processed. 
* A MapReduce job can also include a set of user-defined functions, which are used to process the data in the map and reduce phases. 
* These functions can be written in any programming language, such as Java, Python or C++.
* Mnemonics: 
  * MAP - Map data into key-value pairs
  * REDUCE - Reduce data into smaller sets of tuples
  * JT - Job Tracker
  * TT - Task Tracker
  * CONFIG - Configuration parameters
  * UDF - User-defined functions