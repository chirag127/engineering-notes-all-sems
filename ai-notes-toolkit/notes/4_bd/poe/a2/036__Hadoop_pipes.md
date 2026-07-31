 Here is the content written in formal tone with points, without emojis or external links, in Markdown format, inside the given header:

#### Hadoop Pipes

- Hadoop Pipes is a SWIG-compatible C++ API for creating MapReduce applications.
- It allows you to create MapReduce applications using any programming language that can produce executable binaries and that can read data from standard input and write to standard output.
- The Map and Reduce tasks are executed as external programs that read input data from standard input and write output data to standard output.
- Hadoop Pipes do not provide features like serialization or data types as in Hadoop Streaming. The developer has to handle I/O formats, data types, and other such details.
- Hadoop Pipes provide only the basic framework and the application logic is entirely handled by user programs. This provides more flexibility but also more responsibility on the developer.
- Hadoop Pipes are useful when:
    - You want to use an unsupported programming language.
    - You want more control over I/O formats and data types.
    - Overhead of Hadoop Streaming is too high for your application.