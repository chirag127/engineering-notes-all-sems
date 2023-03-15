### Finite Automata and Regular Expression

- Finite automata are abstract machines that can recognize patterns in strings and accept or reject them based on some rules .
- Regular expressions are algebraic notations that can describe the language accepted by finite automata . They are composed of symbols, operators and parentheses.
- Regular expressions and finite automata are equivalent in expressive power, meaning that for every regular expression, there exists a finite automaton that accepts the same language, and vice versa   .
- There are two methods to convert a regular expression to a finite automaton:
  - State decomposition method: This method involves breaking down the regular expression into smaller subexpressions and constructing a finite automaton for each subexpression. Then, the subautomata are combined using the rules of union, concatenation and closure .
  - State elimination method: This method involves constructing a nondeterministic finite automaton (NFA) with epsilon transitions for the given regular expression, and then eliminating the states one by one until only the initial and final states remain. The resulting transition between the initial and final states is the regular expression.
- There are two methods to convert a finite automaton to a regular expression:
  - State elimination method: This method involves eliminating the states of the finite automaton one by one, except the initial and final states, and replacing the transitions with regular expressions that represent the paths between the remaining states. The resulting transition between the initial and final states is the regular expression.
  - State labeling method: This method involves labeling each state of the finite automaton with a regular expression that represents the paths from the initial state to that state. Then, the regular expressions are updated using the rules of union, concatenation and closure until only the final state remains. The label of the final state is the regular expression.
- Regular expressions and finite automata are useful tools for modeling and analyzing the syntax and semantics of natural and artificial languages, as well as designing compilers, scanners, parsers, and other applications.

: https://www.tutorialspoint.com/explain-the-relationship-between-finite-automata-and-regular-expression
: https://www.javatpoint.com/automata-regular-expression
: https://www.geeksforgeeks.org/conversion-of-regular-expression-to-finite-automata/
: https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/resources/introduction-finite-automata-regular-expressions/
: https://www.geeksforgeeks.org/designing-finite-automata-from-regular-expression-set-1/
: https://www.geeksforgeeks.org/generating-regular-expression-from-finite-automata/