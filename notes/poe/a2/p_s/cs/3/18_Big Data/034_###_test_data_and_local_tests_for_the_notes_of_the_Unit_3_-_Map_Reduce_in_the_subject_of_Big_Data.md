 Here is the content in markdown format:

### Test data and local tests for the notes of the Unit 3 - Map Reduce in the subject of Big Data

1. Test data: To test the Map Reduce programs, you need sample input data which acts as test data. This test data should be in the input format as expected by the Map Reduce program. Some points to consider for preparing test data:
- The test data should have variety and cover different scenarios which the Map Reduce program is expected to handle. For eg. if the MR program is to calculate average, the test data should have values ranging from low to high, some null values etc.
- The test data should be of size big enough to meaningfully test the performance and scalability of the Map Reduce program.
- The test data should follow the input format expected by the MR program, like if input is in form of key-value pairs or if specific delimiters or headers are expected, etc.

2. Local tests: Before deploying the Map Reduce program on the cluster, it is a good practice to test it locally. This helps to:
- Detect and fix any bugs in the code.
- Check if the program is producing correct output for given input.
- Check performance for small data sizes and optimize the code.
- Prepare the program for handling larger data on the cluster by identifying bottlenecks.

Some ways to perform local tests:
- Run the Map Reduce program on small chunks of the actual input data and verify the output.
- Write separate test classes/methods to provide sample input and compare the output with expected output.
- Check for performance by varying data sizes and observing time taken.
- Get debugging info/logs to detect any issues.

[Further details, diagrams, example codes, advantages, disadvantages, applications, etc. can be added here for the topic as bullet points or in paragraphs if required.]