#### Hadoop pipes

- Hadoop pipes is a C++ API that allows developers to write MapReduce applications in C++ and run them on a Hadoop cluster.
- Hadoop pipes uses a binary protocol to communicate between the C++ application and the Java Hadoop framework.
- Hadoop pipes provides a set of classes and methods that implement the MapReduce interface in C++.
- Hadoop pipes also provides some utility classes and functions for common tasks such as reading and writing files, parsing command-line arguments, logging, etc.
- Hadoop pipes requires the C++ application to be compiled and linked with the Hadoop pipes library and the Hadoop native library.
- Hadoop pipes also requires the C++ application to be packaged as a shared object (.so) file and copied to the Hadoop cluster along with the input and output files.
- Hadoop pipes can be used to write MapReduce applications that need to use native libraries or code that are not available or compatible with Java.
- Hadoop pipes can also be used to write MapReduce applications that need to optimize the performance or memory usage of the C++ code.

Some advantages of Hadoop pipes are:

- It allows developers to use their existing C++ skills and tools to write MapReduce applications.
- It can leverage the existing C++ libraries and code that are not available or compatible with Java.
- It can improve the performance or memory usage of the C++ code by avoiding the Java virtual machine overhead.

Some disadvantages of Hadoop pipes are:

- It requires additional steps to compile, link, package, and copy the C++ application to the Hadoop cluster.
- It adds complexity and potential errors to the communication between the C++ application and the Java Hadoop framework.
- It may not be compatible with some Hadoop features or extensions that are specific to Java.

An example of a Hadoop pipes application is:

```cpp
// WordCount.cc
#include "hadoop/Pipes.hh"
#include "hadoop/TemplateFactory.hh"
#include "hadoop/StringUtils.hh"

using namespace std;

// A simple mapper that splits each line into words and emits each word with a count of 1
class WordCountMapper: public HadoopPipes::Mapper {
public:
  // constructor: does nothing
  WordCountMapper(HadoopPipes::TaskContext& context){}
  
  // map function: receives a line, outputs (word, "1")
  void map(HadoopPipes::MapContext& context) {
    // get the input line as a string
    string line = context.getInputValue();
    // split the line into words
    vector<string> words = HadoopUtils::splitString(line, " ");
    // emit each word with a count of 1
    for(unsigned int i=0; i < words.size(); ++i) {
      context.emit(words[i], "1");
    }
  }
};

// A simple reducer that sums the counts for each word and emits each word with its total count
class WordCountReducer: public HadoopPipes::Reducer {
public:
  // constructor: does nothing
  WordCountReducer(HadoopPipes::TaskContext& context){}
  
  // reduce function: receives a word and a list of counts, outputs (word, total count)
  void reduce(HadoopPipes::ReduceContext& context) {
    // get the input word as a string
    string word = context.getInputKey();
    // initialize the sum of counts to zero
    int sum = 0;
    // iterate over the counts and add them to the sum
    while(context.nextValue()) {
      sum += HadoopUtils::toInt(context.getInputValue());
    }
    // emit the word and its total count as strings
    context.emit(word, HadoopUtils::toString(sum));
  }
};

int main(int argc, char *argv[]) {
  // register the mapper and the reducer
  return HadoopPipes::runTask(HadoopPipes::TemplateFactory<WordCountMapper, WordCountReducer>());
}
```

To compile and run this application, the following steps are needed:

- Install the Hadoop pipes library and the Hadoop native library on the development machine.
- Compile the C++ code with the Hadoop pipes library and the Hadoop native library, and create a shared object file named WordCount.so.
- Copy the WordCount.so file, the input file, and the output directory to the Hadoop cluster.
- Run the Hadoop pipes job with the following command:

```bash
hadoop pipes \
  -D hadoop.pipes.java.recordreader=true \
  -D hadoop.pipes.java.recordwriter=true \
  -input input.txt \
  -output output \
  -program WordCount.so
```

Some mnemonics and learning tricks