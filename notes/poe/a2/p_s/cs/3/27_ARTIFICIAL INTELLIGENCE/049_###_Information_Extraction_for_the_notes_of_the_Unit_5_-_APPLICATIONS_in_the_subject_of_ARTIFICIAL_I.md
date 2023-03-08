 Here is the content in markdown format for the given topic:

#### Map Reduce types in Map Reduce

The two main types of Map Reduce are:

1. Map Side Join: In Map Side Join, the join operation is performed within the map function itself. The mapper reads data from multiple inputs and performs the join operation. The benefit of Map Side Join is that it can be faster since the data is joined in parallel. However, it can only be applied if the data is sorted on the join key.
2. Reduce Side Join: In Reduce Side Join, the join operation is performed in the reduce function. The mappers output data for each input and the reducers perform the actual join operation on the data. Reduce Side Join is more general and can handle any type of data but can be slower than Map Side Join due to the added shuffle and sort phases.

Some key points to remember:

- The choice of join type depends on the structure and amount of input data.
- For sorting the data, additional MapReduce jobs may be required.
- The input data to the join operation must be in the same format and join key type.

[Diagrams and examples can be added here to explain the concepts and application of Map Side and Reduce Side Joins]

The advantages and disadvantages can be discussed along with use cases where each join type would be suitable. This covers the major types of joins supported in MapReduce. Please let me know if you would like me to elaborate on any part of this answer further.