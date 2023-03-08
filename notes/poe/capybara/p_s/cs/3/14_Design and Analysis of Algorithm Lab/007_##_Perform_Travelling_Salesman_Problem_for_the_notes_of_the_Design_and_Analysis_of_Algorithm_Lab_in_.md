## Perform Travelling Salesman Problem for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

The Travelling Salesman Problem (TSP) is a well-known problem in computer science that involves finding the shortest possible route that visits every city in a given list exactly once and then returns to the starting city. The problem is known to be NP-hard, meaning that it is difficult to solve in a reasonable amount of time for large inputs.

### Algorithm

The following is an algorithm to solve the TSP problem:

1. Generate all possible tours of the cities.
2. Calculate the cost of each tour.
3. Select the tour with the lowest cost.

### Advantages

- The TSP problem is useful in real-world applications such as logistics and transportation planning.
- It can be used to optimize the route of a delivery truck or a salesperson.

### Disadvantages

- The TSP problem is known to be NP-hard, meaning that it is difficult to solve for large inputs.
- The algorithm can be computationally expensive for large input sizes.

### Example

Consider the following set of cities: A, B, C, and D. The distance between each pair of cities is given in the table below:

|   | A | B | C | D |
| - | - | - | - | - |
| A | 0 | 10 | 15 | 20 |
| B | 10 | 0 | 35 | 25 |
| C | 15 | 35 | 0 | 30 |
| D | 20 | 25 | 30 | 0 |

To solve this problem, we can use the algorithm described above. The possible tours are:

- A -> B -> C -> D -> A (cost = 90)
- A -> B -> D -> C -> A (cost = 80)
- A -> C -> B -> D -> A (cost = 95)
- A -> C -> D -> B -> A (cost = 110)
- A -> D -> B -> C -> A (cost = 90)
- A -> D -> C -> B -> A (cost = 105)

The tour with the lowest cost is A -> B -> D -> C -> A (cost = 80).

### Applications

The TSP problem has many applications in real-world scenarios, including:

- Planning the delivery routes for a logistics company.
- Optimizing the route for a salesperson to visit multiple clients in a day.
- Designing the layout of a printed circuit board to minimize the length of the wires.