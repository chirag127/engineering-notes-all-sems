# Implementation of LR Parsing Tables

LR parsing tables are a two-dimensional array in which each entry represents an action or a goto entry. LR parsing tables are used by LR parsers, which are bottom-up parsers that can handle a large class of context-free grammars. LR parsers use a stack and an input buffer to parse the given string. The stack contains the states and symbols that have been processed so far, and the input buffer contains the remaining symbols to be processed. The parsing table guides the parser to decide which action to take based on the current state and the next input symbol.

There are three types of LR parsers, which differ in the way they construct the parsing table and resolve conflicts:

- Simple LR (SLR) parser: It is the easiest and most cost-effective to implement, but it fails to make a parsing table for some class of grammars. It uses the follow sets of the non-terminals to determine the reduce actions.
- Canonical LR (CLR) parser: It is the most powerful and accurate parser, but it has a large parsing table that may be impractical to store and use. It uses the lookahead sets of the items to determine the reduce actions.
- Lookahead LR (LALR) parser: It is a compromise between SLR and CLR parsers, which can handle a large class of grammars with a smaller parsing table. It merges the states of the CLR parser that have the same core items, and uses the lookahead sets of the merged states to determine the reduce actions.

The following steps are involved in the implementation of LR parsing tables:

- Construct the augmented grammar by adding a new start symbol and a new production.
- Construct the canonical collection of LR(0) items by applying the closure and goto operations on the augmented grammar.
- Construct the action and goto functions based on the LR(0) items and the grammar symbols. The action function maps a state and a terminal symbol to a shift, reduce, accept, or error action. The goto function maps a state and a non-terminal symbol to a new state.
- Construct the parsing table by filling the entries of the action and goto functions. If there is a conflict in any entry, the grammar is not LR parsable by the chosen parser.
- Use the parsing table to parse the given string by following the algorithm of the LR parser. The algorithm repeatedly performs the action indicated by the current state and the next input symbol, until it accepts or rejects the string.

The following is an example of an LR parsing table for the grammar:

S' -> S

S -> CC

C -> cC | d

The grammar is SLR(1) parsable, but not LR(0) parsable.

| State | c | d | $ | S | C |
| ----- | - | - | - | - | - |
| 0 | s3 | s4 | | 1 | 2 |
| 1 | | | accept | | |
| 2 | s3 | s4 | | | 5 |
| 3 | s3 | s4 | | | 6 |
| 4 | r2 | r2 | r2 | | |
| 5 | r1 | r1 | r1 | | |
| 6 | r3 | r3 | r3 | | |

: https://www.tutorialspoint.com/what-is-implementation-of-lr-parsing-tables
: https://www.tutorialspoint.com/what-is-types-of-lr-parser-in-compiler-design
: https://en.wikipedia.org/wiki/LR_parser
: https://www.geeksforgeeks.org/lr-parser/