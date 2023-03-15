#### Hadoop Streaming
Hadoop Streaming is a utility that comes with the Hadoop distribution. This utility allows you to create and run Map/Reduce jobs with any executable or script as the mapper and/or the reducer. Here is an example of how to use Hadoop Streaming with Python:

```python
# mapper.py
import sys
for line in sys.stdin:
    line = line.strip()
    words = line.split()
    for word in words:
        print('%s\t%s' % (word, 1))
```

```python
# reducer.py
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

To run the MapReduce job, you would use the following command:

```bash
bin/hadoop jar contrib/streaming/hadoop-streaming-*.jar \
-input myInputDirs \
-output myOutputDir \
-mapper /path/to/mapper.py \
-reducer /path/to/reducer.py
```
