Hadoop pipes is the name of the C++ interface to Hadoop MapReduce. It uses sockets to communicate with the tasktracker, which runs the map and reduce functions in separate processes. To write code for Hadoop pipes, you need to implement the following classes:

- `Mapper`: This class defines the map function, which takes a key-value pair as input and emits zero or more key-value pairs as output. The key and value types are specified by template parameters.
- `Reducer`: This class defines the reduce function, which takes a key and an iterator over values as input and emits zero or more key-value pairs as output. The key and value types are specified by template parameters.
- `RecordReader`: This class defines how to read input records from a split. It has a `next` method that returns a boolean indicating whether there is more data, and a `getCurrentKey` and `getCurrentValue` method that return the current key and value respectively.
- `RecordWriter`: This class defines how to write output records to a file. It has a `emit` method that takes a key-value pair as input and writes it to the output file.
- `Partitioner`: This class defines how to partition the map output keys among the reducers. It has a `partition` method that takes a key and the number of reducers as input and returns an integer indicating the reducer index for the key.
- `Factory`: This class defines how to create instances of the above classes. It has a `createMapper`, `createReducer`, `createRecordReader`, `createRecordWriter`, and `createPartitioner` method that return pointers to the corresponding classes.

Here is an example of a word count program using Hadoop pipes:

```c++
#include "hadoop/Pipes.hh"
#include "hadoop/TemplateFactory.hh"
#include "hadoop/StringUtils.hh"

class WordCountMapper : public HadoopPipes::Mapper {
public:
  // constructor: does nothing
  WordCountMapper(HadoopPipes::TaskContext& context){}
  
  // map function: receives a line, outputs (word, "1")
  void map(HadoopPipes::MapContext& context) {
    //--- get line of text ---
    std::string line = context.getInputValue();
    
    //--- split it into words ---
    std::vector<std::string> words = HadoopUtils::splitString(line, " ");
    
    //--- emit each word tuple (word, "1") ---
    for(unsigned int i=0; i < words.size(); i++) {
      context.emit(words[i], "1");
    }
  }
};

class WordCountReducer : public HadoopPipes::Reducer {
public:
  // constructor: does nothing
  WordCountReducer(HadoopPipes::TaskContext& context){}
  
  // reduce function: receives a word, counts its occurrences
  void reduce(HadoopPipes::ReduceContext& context) {
    //--- get the word ---
    std::string word = context.getInputKey();
    
    //--- get the iterator of counts ---
    HadoopPipes::Iterator<std::string> counts = context.getValues();
    
    //--- sum them ---
    int sum = 0;
    while(counts.hasMore()) {
      sum += HadoopUtils::toInt(counts.next());
    }
    
    //--- emit the pair (word, sum) ---
    context.emit(word, HadoopUtils::toString(sum));
  }
};

int main(int argc, char *argv[]) {
  // register the mapper and the reducer
  return HadoopPipes::runTask(HadoopPipes::TemplateFactory<WordCountMapper, 
                              WordCountReducer>());
}
```