#### Map Reduce scripts in Hive

- Map Reduce scripts in Hive are used to plug in custom mappers and reducers in the data stream by using features natively supported in the Hive language  .
- Map Reduce scripts can be written in any executable language such as Python, Ruby, Perl, etc. and can be invoked using the TRANSFORM clause in Hive queries  .
- Map Reduce scripts can also be used to perform complex transformations or aggregations that are not supported by the built-in operators and functions in Hive .
- Map Reduce scripts can be specified in two ways: using TRANSFORM for single-step scripts, or using MAP and REDUCE for multi-step scripts  .
- Map Reduce scripts read the input data from stdin and write the output data to stdout. The input and output data are delimited by tabs (\t) by default, but this can be changed using the ROW FORMAT clause  .
- Map Reduce scripts can access the configuration properties of the Hive session using the getconf utility  .
- Map Reduce scripts can be tested locally using the SET hive.exec.mode.local.auto=true; command before running the Hive query  .
- Map Reduce scripts can be combined with other Hive features such as partitioning, bucketing, sampling, etc. to optimize the performance and scalability of the queries .