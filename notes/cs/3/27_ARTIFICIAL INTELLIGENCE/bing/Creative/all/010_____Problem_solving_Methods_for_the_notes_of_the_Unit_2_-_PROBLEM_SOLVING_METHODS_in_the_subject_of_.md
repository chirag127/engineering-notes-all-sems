# Problem Solving Methods for the notes of the Unit 2 - PROBLEM SOLVING METHODS in the subject of ARTIFICIAL INTELLIGENCE KCS

- Problem solving is the process of finding solutions to complex or challenging issues by applying artificial intelligence techniques, such as reasoning, search, optimization, learning, etc.
- Problem solving methods are the strategies or algorithms that are used by problem-solving agents to achieve their goals in a given environment.
- Problem solving methods can be classified into two main categories: search-based and non-search-based methods.

## Search-based methods
- Search-based methods are the most common and widely used problem solving methods in artificial intelligence.
- Search-based methods involve exploring a space of possible solutions (called the search space) and finding the one that satisfies some criteria (called the objective function or the goal test).
- Search-based methods can be further divided into two types: uninformed search and informed search.

### Uninformed search
- Uninformed search methods are also known as blind search or brute-force search methods.
- Uninformed search methods do not use any domain-specific knowledge or heuristics to guide the search process. They only rely on the problem definition and the goal test.
- Uninformed search methods are simple and general, but they can be inefficient and impractical for large or complex search spaces.
- Examples of uninformed search methods are: breadth-first search, depth-first search, uniform-cost search, iterative deepening search, bidirectional search, etc.

### Informed search
- Informed search methods are also known as heuristic search or guided search methods.
- Informed search methods use some domain-specific knowledge or heuristics to estimate the cost or the quality of each solution in the search space. They try to find the solution that has the lowest cost or the highest quality.
- Informed search methods are more efficient and effective than uninformed search methods, but they require more domain knowledge and heuristic design.
- Examples of informed search methods are: greedy search, A* search, hill-climbing search, simulated annealing, genetic algorithms, etc.

## Non-search-based methods
- Non-search-based methods are the problem solving methods that do not involve searching a space of possible solutions, but rather use some other techniques to find or generate solutions.
- Non-search-based methods are usually more specialized and tailored to specific types of problems or domains.
- Non-search-based methods can be further divided into two types: constraint satisfaction and knowledge-based methods.

### Constraint satisfaction
- Constraint satisfaction methods are the problem solving methods that deal with problems that can be formulated as a set of variables, domains, and constraints.
- Variables are the unknowns or the decision variables that need to be assigned values.
- Domains are the sets of possible values that each variable can take.
- Constraints are the rules or the relations that restrict the values of the variables or the combinations of the values.
- Constraint satisfaction methods try to find an assignment of values to the variables that satisfies all the constraints, or report that no such assignment exists.
- Examples of constraint satisfaction methods are: backtracking, forward checking, arc consistency, constraint propagation, local search, etc.

### Knowledge-based methods
- Knowledge-based methods are the problem solving methods that use some form of explicit or implicit knowledge to find or generate solutions.
- Knowledge-based methods can be further divided into two types: logic-based and learning-based methods.

#### Logic-based methods
- Logic-based methods are the problem solving methods that use logic as a formal language to represent and manipulate knowledge.
- Logic-based methods can be further divided into two types: deductive and inductive methods.

##### Deductive methods
- Deductive methods are the problem solving methods that use logic to derive conclusions from given premises or facts.
- Deductive methods are based on the principle of modus ponens: if p implies q, and p is true, then q is true.
- Deductive methods can be further divided into two types: propositional logic and predicate logic.

###### Propositional logic
- Propositional logic is the simplest form of logic that deals with propositions or statements that are either true or false.
- Propositional logic uses symbols (such as p, q, r, etc.) to represent propositions, and operators (such as not, and, or, implies, etc.) to connect propositions.
- Propositional logic can be used to perform logical inference, such as modus ponens, modus tollens, resolution, etc.

###### Predicate logic
- Predicate logic is a more expressive form of logic that deals with predicates or relations that involve objects or entities.
- Predicate logic uses symbols (such as P, Q,