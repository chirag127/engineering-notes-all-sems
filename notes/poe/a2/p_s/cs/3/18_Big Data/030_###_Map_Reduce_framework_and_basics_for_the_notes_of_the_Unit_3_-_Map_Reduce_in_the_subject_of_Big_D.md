 Here is the content in markdown format for the topic ### Map Reduce framework and basics for the notes of the Unit 3 - Map Reduce in the subject of Big Data:

### Map Reduce framework and basics

- Map Reduce is a programming model for processing large data sets with parallel, distributed algorithms on a cluster.
- It consists of two main tasks - Map and Reduce.
- The Map task partitions the input data into smaller chunks which are processed in parallel by multiple machines in the cluster.
- The Reduce task collects and combines the outputs of the Map tasks and performs a summary operation on the results.
- The main advantages of Map Reduce are:
- Scalability - It can handle enormous amounts of data and scale to thousands of nodes in the cluster.
- Fault Tolerance - It is resilient to failures and can handle lost nodes or data. The jobs are re-executed on other nodes.
- Low Cost - It uses commodity hardware and is cost effective.
- Efficient - The processing is parallel and distributed leading to fast execution times.
- The steps in a Map Reduce job are:
1. Input
2. Split into chunks
3. Map (Parallel processing on chunks)
4. Shuffle and Sort
5. Reduce (Summary operation)
6. Output

- Examples of Map Reduce applications are:
- Counting words in a document
- Calculating averages
- Machine Learning algorithms
- Data mining tasks

- The disadvantages of Map Reduce are:
- inflexible - Jobs must conform to the Map and Reduce paradigm.
- Overhead - There is additional time/effort required for splitting and shuffling data.
- Difficult programming - It can be cumbersome to program.

[Include diagrams/images/codes/tables etc. if required to explain the concepts]