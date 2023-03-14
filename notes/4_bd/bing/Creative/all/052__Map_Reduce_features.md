#### Map Reduce features

- Map Reduce is a programming model and an associated implementation for processing and generating large data sets with a parallel, distributed algorithm on a cluster.
- Map Reduce consists of two phases: map and reduce. The map phase applies a user-defined function to each input key-value pair and produces a set of intermediate key-value pairs. The reduce phase aggregates all the intermediate values associated with the same intermediate key and produces the final output.
- Map Reduce is designed to handle large-scale data processing on commodity hardware. It can scale up from a single machine to thousands of machines, each offering local computation and storage.
- Map Reduce is fault-tolerant and resilient to failures. It automatically handles the failures of machines, processes, or network partitions. It also provides mechanisms for monitoring and debugging the execution of the tasks.
- Map Reduce is expressive and flexible. It can support a wide range of applications, such as web indexing, data mining, machine learning, log analysis, etc. It can also be extended with user-defined functions, combiners, partitioners, and input/output formats.
- Map Reduce is simple and easy to use. It abstracts away the details of distributed computing, such as communication, synchronization, load balancing, etc. It allows the user to focus on the logic of the application, rather than the implementation details.

A possible mnemonic to remember the features of Map Reduce is:

**M**assive data processing
**A**pply map and reduce functions
**P**arallel and distributed execution
**R**esilient to failures
**E**xpressive and flexible
**D**esigned for commodity hardware
**U**ser-defined extensions
**C**omputation and storage locality
**E**asy and simple to use