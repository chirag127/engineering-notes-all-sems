 Here is the content in markdown format:

### Big Data Architecture

1. Batch Processing - Data is processed in batches at regular intervals. Examples - Hadoop MapReduce, Pig, Hive.
Pros - Scalable, fault tolerant, inexpensive.
Cons - Latency can be high.

2. Stream Processing - Data is processed as soon as it is received. Examples - Storm, Spark Streaming, Flink.
Pros - Low latency, can handle unbounded data streams.
Cons - More complex to implement, state management can be challenging.

3. Lambda Architecture - Combines both batch and stream processing. Data is processed in batches as well as streams. The outputs are merged to get a single result.
Pros - Leverages both batch and stream processing, provides low latency as well as scalable, fault tolerant processing.
Cons - More complex to implement.

[Include diagrams and examples as needed]

Applications - Fraud detection, recommendation systems, IoT data processing, social media analytics, etc.

Advantages - Scalable, fault tolerant, inexpensive, low latency.
Disadvantages - Complex to implement and manage.

### Optimization of DFA-Based Pattern Matchers for the notes of the Unit 1 - Introduction to Compiler in the subject of Compiler Design

1. Minimize the number of states - Remove unnecessary states and transitions. This reduces the memory required to store the automaton.
2. Remove useless symbols - Remove symbols which do not lead to a state transition. This reduces the number of transitions and checks required.
3. Priority to frequent symbols - Give higher priority to symbols which lead to the most transitions. This can speed up the processing.
4. Lookahead - Use lookahead to predict the next few symbols. This can lead to early state transitions and faster processing.
5. Hardware optimizations - Use specialized hardware and parallelism to speed up the processing.

[Include diagrams and examples as needed]

Advantages - Faster pattern matching, reduced memory and processing requirements.
Disadvantages - Complex to implement, can increase preprocessing time.

Applications - Text editors, compilers, network intrusion detection systems, etc.