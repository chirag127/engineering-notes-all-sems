### Informed for the notes of the Unit 2 - PROBLEM SOLVING METHODS in the subject of ARTIFICIAL INTELLIGENCE KCS

Informed search algorithms are used in Artificial Intelligence to solve problems by using domain knowledge. This knowledge helps the algorithm to make informed decisions about which path to take in the search space. In this section, we will learn about the various types of informed search algorithms and how they work.

#### Types of Informed Search Algorithms

1. **Best First Search Algorithm:** This algorithm uses heuristic function to determine which path to take in the search space. The heuristic function is an estimate of the distance from the current node to the goal node. The algorithm selects the node with the lowest heuristic value as the next node to expand. 

2. **A* Search Algorithm:** This algorithm combines the best features of both Breadth First Search and Best First Search algorithms. It uses both the cost to reach the current node and the estimated cost to reach the goal node to evaluate each node. The algorithm selects the node with the lowest total cost as the next node to expand.

3. **Greedy Best First Search Algorithm:** This algorithm is similar to the Best First Search algorithm, but it only considers the heuristic value of each node. It selects the node with the lowest heuristic value as the next node to expand.

#### Advantages and Disadvantages of Informed Search Algorithms

Advantages:
- Informed search algorithms are faster than uninformed search algorithms.
- They use domain knowledge to make informed decisions, which makes them more efficient.

Disadvantages:
- Informed search algorithms may not always find the optimal solution.
- They require domain knowledge to be effective, which may not always be available.

#### Applications of Informed Search Algorithms

Informed search algorithms have various applications in Artificial Intelligence, such as:
- Pathfinding in video games and robotics.
- Planning and scheduling in logistics and transportation.
- Natural Language Processing for text classification and sentiment analysis.

#### Example of Informed Search Algorithm

Let's consider the problem of finding the shortest path between two cities on a map. We can use the A* search algorithm to solve this problem. The algorithm will use the distance between each city and the estimated distance from each city to the destination city to determine the shortest path.

#### Conclusion

Informed search algorithms are an important part of Artificial Intelligence. They use domain knowledge to make informed decisions and find solutions faster than uninformed search algorithms. The different types of informed search algorithms have their advantages and disadvantages, and can be used in various applications.