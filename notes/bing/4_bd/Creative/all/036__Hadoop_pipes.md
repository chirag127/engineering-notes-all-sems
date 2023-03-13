#### Hadoop pipes

- Hadoop pipes is the name of the C++ interface to Hadoop MapReduce  .
- Unlike Streaming, which uses standard input and output to communicate with the map and reduce code, Pipes uses sockets as the channel over which the tasktracker communicates with the process running the C++ map or reduce function  . JNI is not used.
- Hadoop pipes provides a SWIG-compatible C++ API to implement MapReduce applications (non JNI™ based).
- The MapReduce framework operates exclusively on <key, value> pairs, that is, the framework views the input to the job as a set of <key, value> pairs and produces a set of <key, value> pairs as the output of the job, conceivably of different types.
- To run Hadoop pipes, the C++ code needs to be compiled and linked with the pipes libraries . The pipes libraries are provided by the Hadoop distribution.
- A Hadoop pipes application consists of a driver class, a mapper class, and a reducer class. The driver class is responsible for configuring the job and submitting it to the cluster. The mapper class implements the map function, which takes a <key, value> pair as input and emits zero or more <key, value> pairs as output. The reducer class implements the reduce function, which takes a <key, list of values> pair as input and emits zero or more <key, value> pairs as output.
- Hadoop pipes provides a set of abstract classes and interfaces that the C++ code needs to inherit and implement. These include:
  - HadoopPipes::Mapper: The abstract base class for the mapper. It has a virtual method map, which takes a HadoopPipes::MapContext object as a parameter. The MapContext object provides methods to access the input key and value, emit output key and value pairs, and report progress and status.
  - HadoopPipes::Reducer: The abstract base class for the reducer. It has a virtual method reduce, which takes a HadoopPipes::ReduceContext object as a parameter. The ReduceContext object provides methods to access the input key and list of values, emit output key and value pairs, and report progress and status.
  - HadoopPipes::Factory: The interface for creating mapper and reducer objects. It has two pure virtual methods, createMapper and createReducer, which take a HadoopPipes::TaskContext object as a parameter and return a pointer to a HadoopPipes::Mapper or HadoopPipes::Reducer object respectively.
  - HadoopPipes::TaskContext: The abstract base class for the context objects. It provides methods to access the configuration, the counters, and the task type.
  - HadoopPipes::MapContext and HadoopPipes::ReduceContext: The subclasses of HadoopPipes::TaskContext that provide additional methods specific to the map and reduce tasks.

- A simple example of a Hadoop pipes application that performs word count is shown below:

```cpp
// WordCount.cc
#include "hadoop/Pipes.hh"
#include "hadoop/TemplateFactory.hh"
#include "hadoop/StringUtils.hh"

class WordCountMapper : public HadoopPipes::Mapper {
public:
  // constructor: does nothing
  WordCountMapper(HadoopPipes::TaskContext& context){}
  // map function: receives a line, outputs (word,"1")
  // to reducer
  void map(HadoopPipes::MapContext& context) {
    //--- get line of text ---
    std::string line = context.getInputValue();
    //--- split it into words ---
    std::vector< std::string > words =
      HadoopUtils::splitString( line, " " );
    //--- emit each word tuple (word, "1" ) ---
    for(unsigned int i=0; i < words.size(); ++i) {
      context.emit(words[i], "1");
    }
  }
};

class WordCountReducer : public HadoopPipes::Reducer {
public:
  // constructor: does nothing
  WordCountReducer(HadoopPipes::TaskContext& context){}
  // reduce function
  void reduce(HadoopPipes::ReduceContext& context) {
    int count = 0