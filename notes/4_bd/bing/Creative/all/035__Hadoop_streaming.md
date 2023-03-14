#### Hadoop streaming

- Hadoop streaming is a utility that comes with the Hadoop distribution. The utility allows you to create and run MapReduce jobs with any executable or script as the mapper and/or the reducer  .
- Hadoop streaming works by launching the executable or script as a separate process for each mapper or reducer task and feeding the input data to the stdin of the process and collecting the output data from the stdout of the process .
- Hadoop streaming uses the following default conventions for the input and output formats of the mapper and reducer :
  - The input key and value are separated by a tab character.
  - The output key and value are also separated by a tab character.
  - The key is anything before the first tab character in a line.
  - The value is anything after the first tab character in a line.
  - If there is no tab character in a line, the entire line is the key and the value is null.
- Hadoop streaming supports various command options to customize the input and output formats, the number of mappers and reducers, the partitioning and sorting of the data, the environment variables, the configuration variables, the files and archives to be distributed to the tasks, and the Java classes to be used as the mapper, reducer, combiner, partitioner, or comparator .
- Hadoop streaming also provides some built-in classes for common use cases, such as the Hadoop aggregate package, the Hadoop field selection class, the Hadoop partitioner class, and the Hadoop comparator class .
- Hadoop streaming has the following advantages:
  - It allows you to use any programming language or tool that can read from stdin and write to stdout for writing MapReduce programs.
  - It enables you to leverage the existing libraries and modules in different languages for data processing.
  - It simplifies the development and testing of MapReduce programs by avoiding the need to compile and package Java code.
- Hadoop streaming has the following disadvantages:
  - It may incur some performance overhead due to the serialization and deserialization of data between the Java framework and the external processes.
  - It may not support some advanced features of the MapReduce framework, such as counters, progress reports, and custom input/output formats.
  - It may not handle complex data types or binary data well, as it relies on text-based formats.
- Hadoop streaming can be used for various applications, such as text processing, web log analysis, machine learning, data mining, etc. Here is an example of using Hadoop streaming to perform word count with Python scripts :

  - mapper.py
  ```python
  #!/usr/bin/env python
  import sys
  # input comes from STDIN (standard input)
  for line in sys.stdin:
      # remove leading and trailing whitespace
      line = line.strip()
      # split the line into words
      words = line.split()
      # increase counters
      for word in words:
          # write the results to STDOUT (standard output);
          # what we output here will be the input for the
          # Reduce step, i.e. the input for reducer.py
          #
          # tab-delimited; the trivial word count is 1
          print '%s\t%s' % (word, 1)
  ```
  - reducer.py
  ```python
  #!/usr/bin/env python
  from operator import itemgetter
  import sys
  current_word = None
  current_count = 0
  word = None
  # input comes from STDIN
  for line in sys.stdin:
      # remove leading and trailing whitespace
      line = line.strip()
      # parse the input we got from mapper.py
      word, count = line.split('\t', 1)
      # convert count (currently a string) to int
      try:
          count = int(count)
      except ValueError:
          # count was not a number, so silently
          # ignore/d