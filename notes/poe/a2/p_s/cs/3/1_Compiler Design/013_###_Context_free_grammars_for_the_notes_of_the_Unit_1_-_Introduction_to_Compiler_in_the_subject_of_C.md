 Here is the content in markdown format:

### Context free grammars for the notes of the Unit 1 - Introduction to Compiler in the subject of Compiler Design

- Context free grammars (CFGs) are a way to represent languages in a very mathematical and precise way using set of rules.
- They are composed of the following components:
	- Alphabet: Set of terminal and non-terminal symbols. Ex: {a, b, S, A, B}
	- Production rules: Rules for replacing a single non-terminal symbol with a string of symbols. Ex: S -> Aa | Bb (where S, A and B are non-terminals and a, b are terminals)
	- Start symbol: Special non-terminal symbol that is the starting point for deriving strings. Ex: S
- Derivation: Process of applying production rules to replace non-terminals with strings of symbols until only terminals remain. Ex: S -> Aa | Bb, A -> a. So, S can derive to a (by replacing S with A and then A with a).
- Language: Set of all terminal strings that can be derived from the start symbol. Ex: {a, b}
- advantages: Mathematical preciseness, ability to prove properties of languages, foundation for compiler design.
- disadvantages: May be difficult to construct CFGs for some languages, can be ambiguity (same input having multiple derivations).
- Applications: Specifying programming languages, compilers, formal language theory, etc.

Detailed explanations and diagrams can be included if required.

### Big Data technology components

The major components of Big Data technology are:

1. HDFS (Hadoop Distributed File System): Distributed file system that stores data on commodity machines, providing fault tolerance and high throughput access.
2. MapReduce: Programming model for large scale data processing. Consists of Map and Reduce functions that process data in a distributed fashion.
3. Hadoop YARN: Resource management platform that schedules resources for processing frameworks running on clusters.
4. NoSQL databases: Non-relational databases like HBase, Cassandra, MongoDB that can handle large volumes and varieties of data.
5. Stream processing: Technologies like Spark Streaming and Flink that can process data in real-time streams.
6. Machine Learning frameworks: Frameworks like Mahout, MLlib that can run machine learning algorithms on large data.
7. Visualization tools: Tools like D3.js, Tableau that can visualize data in intuitive ways.

The components can be combined in various ways to build Big Data processing solutions for a variety of use cases. Diagrams and examples can be included for further clarity.