#### Hadoop streaming

- Hadoop streaming is a utility that comes with the Hadoop distribution. The utility allows you to create and run MapReduce jobs with any executable or script as the mapper and/or the reducer .
- Hadoop streaming works by passing the input data to the mapper script as standard input, and reading the output data from the standard output. Similarly, the reducer script receives the intermediate data from the standard input, and writes the final output to the standard output .
- Hadoop streaming uses the default Writable types of the Hadoop framework, such as Text and LongWritable, to serialize and deserialize the data between the mapper and the reducer. You can also specify custom input and output formats for your streaming job .
- Hadoop streaming is useful for writing MapReduce jobs in languages other than Java, such as Python, Ruby, Perl, etc. It is also useful for prototyping and testing MapReduce logic quickly and easily .
- To run a Hadoop streaming job, you need to use the hadoop-streaming.jar file, and specify the following options :

  - -input: the input directory or file in HDFS
  - -output: the output directory in HDFS
  - -mapper: the mapper executable or script
  - -reducer: the reducer executable or script
  - -file: the files to be copied to the working directory of each mapper and reducer task
  - -inputformat: the input format class name (optional)
  - -outputformat: the output format class name (optional)
  - -partitioner: the partitioner class name (optional)
  - -numReduceTasks: the number of reduce tasks (optional)

- For example, to run a word count streaming job using Python scripts, you can use the following command :

  ```
  hadoop jar hadoop-streaming.jar \
  -input input.txt \
  -output output \
  -mapper mapper.py \
  -reducer reducer.py \
  -file mapper.py \
  -file reducer.py
  ```

- A possible mnemonic to remember the Hadoop streaming options is: **I**nput, **O**utput, **M**apper, **R**educer, **F**ile, **I**nputformat, **O**utputformat, **P**artitioner, **N**umReduceTasks. You can use the acronym **IOMRFIOPN** or the phrase **I Often Make Red Fruits In Orange Pots Near** to recall the options.