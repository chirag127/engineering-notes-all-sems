
#### Anatomy of a Map Reduce Job Run

1. Map Reduce is a programming model used to process large datasets.
2. It is based on the concept of divide-and-conquer, where a large task is split into smaller tasks that can be processed in parallel.
3. Map Reduce works by splitting the input data into chunks and mapping each chunk to a separate process.
4. The processes are then combined to produce the output.
5. The first step in a Map Reduce job is the Map phase. During this phase, the input data is split into chunks and each chunk is mapped to a separate process.
6. The processes then execute the map function, which processes the data and produces an output.
7. The output of the map phase is then sent to the Reduce phase. During this phase, the outputs of the map phase are collected and combined to produce the output.
8. The Reduce phase is followed by the Cleanup phase, where any temporary files created during the Map Reduce job are removed.
9. Finally, the output of the Map Reduce job is stored in the output file.