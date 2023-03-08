 Here is the content in markdown format for the topic ### Resilient Distributed Databases for the notes of the Unit 9 - Spark in the subject of Big Data:

### Resilient Distributed Databases

- Resilient Distributed Databases (RDDs) are the primary data abstraction in Spark. They represent an immutable, partitioned collection of elements that can be operated on in parallel.
- RDDs can be created from Hadoop InputFormats (such as HDFS files), or by transforming other RDDs.
- RDDs are lazy, meaning that they do not compute their elements until an action occurs. This allows Spark to efficiently support iterative algorithms.
- If a partition of an RDD is lost due to a worker node failure, Spark can transparently recreate it by re-computing its elements from the original sources. This makes RDDs resilient to node failures.

#### Creation

There are a few ways to create RDDs:

- Parallelizing an existing collection in your driver program: `val data = sc.parallelize(Array(1, 2, 3))`
- Referencing a HDFS file: `val distFile = sc.textFile("hdfs://...")`
- Transforming an existing RDD: `val squared = numbs.map(x => x * x)`

#### Actions

RDDs are lazily evaluated, so no computation is performed until an action occurs. Some common actions are:

- `reduce` - Aggregate the elements of the RDD using a function
- `collect` - Return all the elements of the RDD to the driver program
- `count` - Return the number of elements in the RDD
- `first` - Return the first element of the RDD
- `take(n)` - Return an array with the first n elements of the RDD
- `saveAsTextFile` - Write the elements of the RDD to a text file

[Include detailed ascii diagrams, codes, markdown tables, advantages, disadvantages, examples, applications, etc here if required to learn and read from for exams]