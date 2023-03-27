### Informed for the notes of the Unit 2 - PROBLEM SOLVING METHODS in the subject of ARTIFICIAL INTELLIGENCE KCS

In this unit, we will learn about the various problem-solving methods used in the field of Artificial Intelligence. Informed Search is one such method that we will be covering in this unit. Here are the key points that you need to know about Informed Search:

- Informed Search is a search algorithm that uses domain-specific knowledge to guide the search process towards the goal state.
- It is also known as Heuristic Search, as it uses a heuristic function to evaluate the quality of each state and choose the next state to expand.
- The heuristic function is an estimate of the distance between the current state and the goal state. It helps to prioritize the search towards the most promising paths.
- Informed Search algorithms include Best-First Search, A* Search, and Greedy Search.
- Best-First Search is an algorithm that expands the node with the lowest heuristic value. It is similar to Breadth-First Search, but it uses a heuristic function to guide the search.
- A* Search is an algorithm that combines the cost of the path from the start state and the heuristic value of the current state to choose the best next state.
- Greedy Search is an algorithm that chooses the node that is closest to the goal state, based on the heuristic function.
- Informed Search algorithms are more efficient than Uninformed Search algorithms, as they use domain-specific knowledge to guide the search process.
- However, the effectiveness of Informed Search depends on the quality of the heuristic function. A good heuristic function should be admissible and consistent.
- Admissible heuristic function is a function that never overestimates the distance to the goal state.
- Consistent heuristic function is a function that satisfies the triangle inequality. That is, the estimated distance from the current state to the goal state is always less than or equal to the sum of the estimated distance from the current state to the next state and the estimated distance from the next state to the goal state.

In conclusion, Informed Search is a powerful problem-solving method that uses domain-specific knowledge to guide the search process towards the goal state. It is more efficient than Uninformed Search algorithms, but its effectiveness depends on the quality of the heuristic function. Therefore, it is important to choose a good heuristic function that is admissible and consistent.