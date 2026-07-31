```markdown
## Unit 3 - Map Reduce

- MapReduce is a programming paradigm that runs in the background of Hadoop to provide scalability and easy data-processing solutions.
- MapReduce is designed for processing large volumes of data in parallel by dividing the work into a set of independent tasks.
- MapReduce consists of two phases: Map and Reduce.
  - The Map phase takes an input pair and produces a set of intermediate key/value pairs. The MapReduce framework groups together all intermediate values associated with the same intermediate key and passes them to the Reduce phase.
  - The Reduce phase takes an intermediate key and a set of values for that key and merges those values together to form a possibly smaller set of values. Typically just zero or one output value is produced per Reduce invocation. The output of the Reduce phase is the final output of the MapReduce job.
- MapReduce framework consists of a single master JobTracker and one slave TaskTracker per cluster-node. The master is responsible for scheduling the jobs' component tasks on the slaves, monitoring them and re-executing the failed tasks. The slaves execute the tasks as directed by the master.
- MapReduce applications can be written in various languages, such as Java, Python, Ruby, etc. The framework provides APIs for defining the map and reduce functions, as well as configuring the job parameters, such as input and output formats, number of reducers, etc.
- MapReduce can be used for various types of data analysis, such as word count, inverted index, join, aggregation, etc. MapReduce can also be combined with other tools, such as Hive, Pig, Spark, etc., to perform more complex data processing tasks.
```