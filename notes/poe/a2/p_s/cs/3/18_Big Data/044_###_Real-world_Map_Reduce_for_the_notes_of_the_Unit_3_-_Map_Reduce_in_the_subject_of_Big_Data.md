 Here is the content in markdown format for the topic ### Real-world Map Reduce for the notes of the Unit 3 - Map Reduce in the subject of Big Data:

### Real-world Map Reduce

- Map Reduce is a distributed programming model developed by Google to process large data sets in a parallel, reliable and fault-tolerant manner.
- It works by dividing the input into chunks which are processed by multiple nodes in a cluster.
- The Map Reduce framework takes care of distributing the work across the nodes, coordinating the processes and handling failures.
- The computations are expressed as two functions - Map and Reduce.

**Map function**
- The Map function processes the input chunks in parallel and outputs key-value pairs.
- The keys are used to group the outputs of the Map function which are then passed to the Reduce function.
- Example: Mapping words to their frequencies in a document. The words can be the keys and frequencies can be the values.

**Reduce function**
- The Reduce function merges the values for each key.
- It receives the output of the Map function and processes it further to generate the desired output.
- Example: Summing the frequencies of each word to get the total frequency of every word in the document.

**Advantages**
- Scalability - Map Reduce can scale to large clusters and petabytes of data.
- Fault tolerance - It is resilient to failures and can recompute lost work.
- Simplicity - It hides the complexity of distributed processing and makes it easy to parallelize computations.

**Applications**
- Web indexing
- Log processing
- Generating reports
- Data mining
- Machine learning

[You can include diagrams, codes, tables, more advantages, disadvantages and examples here if required.]