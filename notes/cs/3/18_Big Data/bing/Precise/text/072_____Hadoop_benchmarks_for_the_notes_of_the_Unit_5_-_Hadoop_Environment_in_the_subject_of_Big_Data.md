### Hadoop Benchmarks

Hadoop benchmarks are used to evaluate the performance of Hadoop clusters. Some of the widely known Hadoop benchmarks are:

1. **TestDFSIO**: This is an HDFS benchmark application that performs read and write tests for HDFS. It writes or reads a number of files to and from HDFS and is designed in such a way that it will use one map task per file .

2. **TeraSort**: This benchmark combines testing the HDFS and MapReduce layers of a Hadoop cluster and consists of three MapReduce programs .

3. **Micro-benchmarks**: These are important elements for evaluating Hadoop performance and include sorting programs .

4. **Synthetic workloads**: These include programs such as Gridmix3 and SWIM .

5. **HiBench**: This is a representative and comprehensive Hadoop benchmark suite .

These benchmarks can be used to evaluate the performance of a Hadoop cluster in terms of I/O, CPU, and network . They can be run in standalone mode or remote mode depending on the configuration of the fs.defaultFS scheme .