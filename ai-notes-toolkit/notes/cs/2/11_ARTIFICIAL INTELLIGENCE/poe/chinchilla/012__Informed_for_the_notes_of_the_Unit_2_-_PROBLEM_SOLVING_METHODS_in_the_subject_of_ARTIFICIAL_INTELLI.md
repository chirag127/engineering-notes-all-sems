### Informed for the notes of the Unit 2 - PROBLEM SOLVING METHODS in the subject of ARTIFICIAL INTELLIGENCE KCS

In this unit, we will be discussing the various strategies and techniques used in problem-solving methods in Artificial Intelligence. The focus will be on informed problem-solving methods, which use additional information to guide the search for a solution.

Here are some key points to keep in mind:

- Informed problem-solving methods are also known as heuristic search methods. They use heuristics or rules of thumb to guide the search process towards a more optimal solution.
- Some of the commonly used informed search methods are Best-First Search, A* Search, and Iterative Deepening A* (IDA*).
- Best-First Search is a greedy algorithm that selects the most promising node to expand first based on a heuristic evaluation function. It may not always find the optimal solution but is faster than other informed search methods.
- A* Search is an extension of Best-First Search that incorporates both the cost of the path to a node and the estimated cost to the goal node in its heuristic evaluation function. It is guaranteed to find the optimal solution if certain conditions are met.
- IDA* is a space-efficient variant of A* Search that avoids the memory overhead of storing a fringe of nodes. It iteratively increases the threshold of the heuristic function until a solution is found.
- Informed search methods require an admissible heuristic function, which estimates the distance to the goal node without overestimating it. A consistent heuristic function also ensures that the estimated cost of a node never exceeds the actual cost to reach it.
- Heuristic functions can be derived from problem-specific knowledge or learned from data using machine learning algorithms.
- Informed search methods can be used in a variety of AI applications, such as game playing, route planning, and scheduling.

Overall, informed problem-solving methods are an essential tool in the AI toolkit, enabling us to solve complex problems efficiently and effectively. By understanding the principles and techniques of informed search, we can design better AI systems that can solve real-world problems.