### Predictive Parsers

- Predictive parsers are a type of top-down parsers that do not require backtracking or backup  .
- Predictive parsers can predict which production rule to use by looking at the next input symbol .
- Predictive parsers use a look-ahead pointer to point to the next input symbol.
- Predictive parsers are also known as LL(1) parsers, where L stands for left-to-right scanning of the input, L stands for leftmost derivation, and 1 stands for one symbol of look-ahead .
- Predictive parsers can be implemented by using a stack and a parsing table .
- Predictive parsers can only handle a subset of context-free grammars that are LL(1) grammars .
- Predictive parsers have the advantage of being simple, efficient, and easy to implement.
- Predictive parsers have the disadvantage of being restricted to LL(1) grammars, which may not be expressive enough for some languages .

: https://www.tutorialspoint.com/what-is-a-predictive-parser
: https://t4tutorials.com/predictive-parsing/
: https://www.i2tutorials.com/compiler-design-tutorial/compiler-design-predictive-parsers/
: https://www.geeksforgeeks.org/predictive-parser-in-compiler-design/
: https://www.geeksforgeeks.org/types-of-parsers-in-compiler-design/
: https://www.cs.cmu.edu/~fp/courses/15411-f09/lectures/08-predictive.pdf