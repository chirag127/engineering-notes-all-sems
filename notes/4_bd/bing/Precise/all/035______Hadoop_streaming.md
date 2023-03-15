#### Hadoop Streaming
Hadoop Streaming is a utility that comes with the Hadoop distribution. This utility allows you to create and run Map/Reduce jobs with any executable or script as the mapper and/or the reducer.

- Hadoop Streaming is written in Python, and it is a part of the Hadoop ecosystem.
- It is used to write MapReduce programs in languages other than Java, such as Python, Ruby, and Perl.
- Hadoop Streaming works by passing data between the Map and Reduce functions via standard input (stdin) and standard output (stdout).
- The input data is passed to the mapper line by line, and the mapper processes the data and writes the output to stdout.
- The output of the mapper is then passed to the reducer as input, and the reducer processes the data and writes the final output to stdout.
- The final output is then written to the Hadoop Distributed File System (HDFS).

Advantages of Hadoop Streaming:
- It allows developers to write MapReduce programs in languages other than Java.
- It is easy to use and does not require knowledge of Java or the Hadoop API.
- It is flexible and can be used with any executable or script as the mapper and/or the reducer.

Disadvantages of Hadoop Streaming:
- It may not be as efficient as writing MapReduce programs in Java, as there is an additional overhead of passing data between the processes.
- It may not be able to take full advantage of the Hadoop ecosystem, as some features may only be available in Java.

Example:
Here is an example of a simple word count program written using Hadoop Streaming and Python:

Mapper:
```python
#!/usr/bin/env python
import sys
for line in sys.stdin:
    line = line.strip()
    words = line.split()
    for word in words:
        print('%s\t%s' % (word, 1))
```

Reducer:
```python
#!/usr/bin/env python
from operator import itemgetter
import sys
current_word = None
current_count = 0
word = None
for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t', 1)
    try:
        count = int(count)
    except ValueError:
        continue
    if current_word == word:
        current_count += count
    else:
        if current_word:
            print('%s\t%s' % (current_word, current_count))
        current_count = count
        current_word = word
if current_word == word:
    print('%s\t%s' % (current_word, current_count))
```

To run this example, save the mapper and reducer scripts to files, make them executable, and then use the following command to run the MapReduce job:
```
bin/hadoop jar contrib/streaming/hadoop-streaming-*.jar \
-input myInputDirs \
-output myOutputDir \
-mapper /path/to/mapper.py \
-reducer /path/to/reducer.py
```

Mnemonics and Learning Tricks:
- Remember that Hadoop Streaming is a utility that allows you to create and run Map/Reduce jobs with any executable or script as the mapper and/or the reducer.
- Remember that Hadoop Streaming works by passing data between the Map and Reduce functions via standard input (stdin) and standard output (stdout).
- Remember that the input data is passed to the mapper line by line, and the mapper processes the data and writes the output to stdout.
- Remember that the output of the mapper is then passed to the reducer as input, and the reducer processes the data and writes the final output to stdout.
- Remember that the final output is then written to the Hadoop Distributed File System (HDFS).