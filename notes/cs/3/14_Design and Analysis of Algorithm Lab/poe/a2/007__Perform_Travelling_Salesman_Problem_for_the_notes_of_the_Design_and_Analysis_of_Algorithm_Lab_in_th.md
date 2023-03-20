 Here is the formal content written in Markdown format on the topic "Perform Travelling Salesman Problem for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System":

## Perform Travelling Salesman Problem

1. The Travelling Salesman Problem (TSP) is a popular optimization problem to find the shortest possible route that visits each city exactly once and returns to the origin city.
2. It is an NP-hard problem as the number of possible routes increases exponentially with the number of cities.
3. The steps to solve TSP are:

- Take the input of the number of cities (N) and the cost matrix of travelling between each pair of cities.
- Initialize the current path as a permutation of cities (1 to N). This is the initial solution.
- While the stopping criterion is not met:
- Select two cities in the current path at random.
- Swap the positions of the cities to get a new path.
- If the new path has a lower cost than the current path then make it the current path.
- Stop and return the current path as the shortest tour for the salesman.

4. The time complexity of this algorithm is O(N^2) since in the worst case the while loop may iterate O(N^2) times before finding the optimal path.
5. Other approaches to solve TSP include Branch and Bound, Dynamic Programming, Genetic Algorithms, etc.

The content does not contain any emojis or external links and is written in formal Markdown format as requested. Please let me know if you would like me to modify or expand the content.