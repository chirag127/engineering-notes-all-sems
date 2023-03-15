### Map Reduce

- Map Reduce is a programming model and an associated implementation for processing and generating large data sets with a parallel, distributed algorithm on a cluster.
- The model is inspired by the map and reduce functions commonly used in functional programming, although their purpose in the Map Reduce framework is not the same as in their original forms.
- The key idea is to split the input data set into independent chunks that are processed by the map tasks in a completely parallel manner. The framework sorts the outputs of the maps, which are then input to the reduce tasks. Typically both the input and the output of the job are stored in a file-system. The framework takes care of scheduling tasks, monitoring them and re-executes the failed tasks.
- The Map Reduce model allows for distributed processing of the map and reduction operations. Provided each mapping operation is independent of the others, all maps can be performed in parallel – though in practice it is limited by the number of independent data sources and/or the number of CPUs near each source. Similarly, a set of 'reducers' can perform the reduction phase, provided all outputs of the map operation that share the same key are presented to the same reducer at the same time, or that the reduction function is associative. While this process can often appear inefficient compared to algorithms that are more sequential, Map Reduce can be applied to significantly larger data sets than "commodity" servers can handle – a large server farm can use Map Reduce to sort a petabyte of data in only a few hours. The parallelism also offers some possibility of recovering from partial failure of servers or storage during the operation: if one mapper or reducer fails, the work can be rescheduled – assuming the input data is still available.
- Another way to look at Map Reduce is as a 5-step parallel and distributed computation:

  1. Prepare the Map() input – the "MapReduce system" (also called "the infrastructure" or "the framework") designates Map processors, assigns the input key value K1 that each processor would work on, and provides that processor with all the input data associated with that key value.
  2. Run the user-provided Map() code – Map() is run exactly once for each K1 key value, generating output organized by key values K2.
  3. "Shuffle" the Map output to the Reduce processors – the MapReduce system designates Reduce processors, assigns the K2 key value each processor should work on, and provides that processor with all the Map-generated data associated with that key value.
  4. Run the user-provided Reduce() code – Reduce() is run exactly once for each K2 key value produced by the Map step.
  5. Produce the final output – the MapReduce system collects all the Reduce output, and sorts it by K2 to produce the final outcome.

- Map Reduce can be used for various applications, such as:

  - Counting words, web links, or citations in a large corpus of documents
  - Creating an inverted index for a web crawl
  - Computing the PageRank of a web graph
  - Finding frequent itemsets or association rules in a large transaction database
  - Performing machine learning tasks such as clustering, classification, or regression
  - Analyzing social network data such as finding communities, influencers, or recommendations

- Some advantages of Map Reduce are:

  - It is simple and easy to use for programmers who are familiar with the map and reduce functions
  - It is scalable and fault-tolerant, as it can handle large data sets and recover from failures of nodes or tasks
  - It is flexible and expressive, as it can support a wide range of data types and operations
  - It is portable and compatible, as it can run on various platforms and interoperate with other systems

- Some disadvantages of Map Reduce are:

  - It is not suitable for interactive or real-time queries, as it has high latency and overhead
  - It is not efficient for complex or iterative algorithms, as it requires multiple passes over the data and intermediate data shuffling
  - It is not optimal for data sets that do not fit the key-value pair model, as it may require data transformation or serialization
  - It is not secure or private, as it does not provide any encryption or authentication mechanisms

- A possible mnemonic to remember the steps of Map Reduce is:

  - **M**ap the input to key-value pairs
  - **A**ssign the keys to reducers
  - **P**rocess the values with the reducers
  - **R**eorganize the output by keys
  - **E**mit the final result
  - **D**istribute the computation across nodes
  - **U**se the framework to handle failures and scheduling