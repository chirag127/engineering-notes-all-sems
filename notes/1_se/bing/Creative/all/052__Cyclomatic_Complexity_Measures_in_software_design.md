##### Cyclomatic Complexity Measures in software design

- Cyclomatic complexity is a software metric used to measure the complexity of a program. It is computed using the control flow graph of the program, which represents the flow of execution among the basic blocks of code.    
- Cyclomatic complexity can be defined as the number of linearly independent paths in the control flow graph, or equivalently, the minimum number of test cases needed to cover all possible paths.   
- Cyclomatic complexity can be calculated using the following formula: M = E - N + 2P, where M is the cyclomatic complexity, E is the number of edges in the graph, N is the number of nodes in the graph, and P is the number of connected components in the graph.  
- Cyclomatic complexity can also be calculated by counting the number of decision points in the code, such as if, while, for, switch, etc., and adding one. For example, a code with no decision points has a cyclomatic complexity of 1, and a code with one if statement has a cyclomatic complexity of 2.  
- Cyclomatic complexity can be used to assess the quality of the code, the risk of errors, the difficulty of testing and maintenance, and the level of modularity and cohesion. Generally, lower cyclomatic complexity is desirable, as it indicates simpler and more readable code.   
- Cyclomatic complexity can also guide the testing process, as it indicates the minimum number of test cases needed to achieve 100% branch coverage. Each independent path in the control flow graph should be tested at least once.   
- Cyclomatic complexity has some limitations, such as not accounting for the data complexity, the nesting level, or the logical complexity of the code. It may also give misleading results for some simple or complex structures. Therefore, it should be used in conjunction with other metrics and human judgment.  
- A common rule of thumb is to keep the cyclomatic complexity below 10, as suggested by McCabe, the inventor of the metric. However, this limit may vary depending on the context, the language, and the coding standards. 

A mnemonic to remember the formula for cyclomatic complexity is: **MEN minus 2P**. 

: https://www.geeksforgeeks.org/cyclomatic-complexity/
: https://learn.microsoft.com/en-us/visualstudio/code-quality/code-metrics-cyclomatic-complexity?view=vs-2022
: https://www.ijert.org/cyclomatic-complexity-in-software-development
: https://www.academia.edu/77224725/Use_and_Analysis_on_Cyclomatic_Complexity_in_Software_Development