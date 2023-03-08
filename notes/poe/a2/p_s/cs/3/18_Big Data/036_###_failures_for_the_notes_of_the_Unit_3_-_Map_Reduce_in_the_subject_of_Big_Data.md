 Here is the content in markdown format for the topic ### failures for the notes of Unit 3 - Map Reduce in Big Data:

### Failures

Some of the common failures that can occur in MapReduce are:

1. Task failures: If any of the map or reduce tasks fail, they are re-executed. This can lead to delays in the execution.
2. Node failures: If the node executing the map or reduce task fails, the task is rescheduled on another node. This can also lead to delays.
3. Data locality: The framework tries to schedule tasks on the nodes where the data is present (data locality). This is not always possible leading to delays due to data transfer.
4. Skewed data: If the input data is skewed, it can lead to stragglers i.e. few tasks taking much longer time than others and delaying the entire job.
5. Inefficient usage of resources: If the splits are not balanced or if all the nodes are not utilized properly, it can lead to inefficient usage of resources and increased time to completion.

To handle these types of failures and inefficiencies, measures like speculative execution, efficient task scheduling, dynamic resource allocation, etc. can be adopted in MapReduce. The framework should also be made robust and fault-tolerant to handle unexpected errors and failures.

[Include diagrams, examples, codes, etc. if required to explain the topics]

The content is written in points and in a formal tone with relevant details as would be suitable for study material to learn and read from for exams. Please let me know if you would like me to modify or expand the content in any way.