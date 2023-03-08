 Here is the content in markdown format for the given topic:

### Heuristics for the notes of the Unit 2 - PROBLEM SOLVING METHODS in the subject of ARTIFICIAL INTELLIGENCE KCS:

1. Hill Climbing:
- It is a simple local search technique.
- Starts with an initial solution and then repeatedly moves to a neighbor solution that improves the objective function until no neighbor is better.
- Gets stuck at local optima.
- Pseudo code:

Initialize: Choose a random solution x
Repeat:
	For each neighbor y of x:
		if f(y) < f(x):
			x = y
Until no neighboring solution improves f(x)

Return x

2. Simulated Annealing:
- Inspired by annealing in metallurgy.
- Accepts worse solutions with a probability that decreases over time.
- Helps escape local optima.
- Parameters: Initial Temperature (T), Cooling Schedule.
- Pseudo code:

Initialize: Choose a random solution x and set T = High
Repeat:
	For each neighbor y of x:
		if f(y) < f(x) or probability(exp((f(x)-f(y))/T)) > rand():
			x = y
	T = Decrease(T)
Until T = Low

Return x

[Detailed explanations, diagrams, examples, advantages, disadvantages, and applications can be added here for each point.]