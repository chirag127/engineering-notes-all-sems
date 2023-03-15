# Implementation of LR Parsing Tables

LR parsing tables are a two-dimensional array in which each entry represents an action or a goto entry. LR parsing tables are used to guide the parsing process of a given input string based on a grammar. LR parsing tables are constructed by following these steps:

- Generate the canonical collection of LR(1) items for the grammar. An LR(1) item is a production with a dot marking the current position and a lookahead symbol indicating the next input symbol. The canonical collection of LR(1) items is the set of all possible LR(1) items that can be reached from the start symbol by applying the closure and goto operations.
- For each state in the canonical collection, determine the action entries for each terminal symbol and the goto entries for each non-terminal symbol. The action entries can be one of the following: shift, reduce, accept, or error. The goto entries are the state numbers that are reached by applying the goto operation on a non-terminal symbol.
- Fill the LR parsing table with the action and goto entries for each state and symbol. If there is a conflict between two or more entries for the same state and symbol, the grammar is not LR(1) and the table is not valid.

The following example illustrates the construction of an LR parsing table for a simple grammar:

S -> E
E -> E + T | T
T -> T * F | F
F -> ( E ) | id

The canonical collection of LR(1) items for this grammar is:

I0: S -> .E, $
    E -> .E + T, $
    E -> .T, $
    T -> .T * F, $/+
    T -> .F, $/+
    F -> .( E ), $/+
    F -> .id, $/+

I1: S -> E., $
    E -> E. + T, $

I2: E -> E + .T, $
    T -> .T * F, $/+
    T -> .F, $/+
    F -> .( E ), $/+
    F -> .id, $/+

I3: T -> T. * F, $/+
    F -> F. ( E ), $/+

I4: F -> (. E ), $/+
    E -> .E + T, )/+
    E -> .T, )/+
    T -> .T * F, )/+
    T -> .F, )/+
    F -> .( E ), )/+
    F -> .id, )/+

I5: F -> ( E .), $/+
    E -> E. + T, )/+

I6: F -> ( E ) ., $/+

I7: E -> E + T ., $

I8: T -> T * .F, $/+
    F -> .( E ), $/+
    F -> .id, $/+

I9: T -> T * F ., $/+

The LR parsing table for this grammar is:

| State | id | + | * | ( | ) | $ | S | E | T | F |
| ----- | -- | - | - | - | - | - | - | - | - | - |
| 0     | s4 |   |   | s3 |   |   | 1 | 2 | 5 | 6 |
| 1     |    |   |   |   |   | a |   |   |   |   |
| 2     |    | s7|   |   |   | r1|   |   |   |   |
| 3     | s4 |   |   | s3 |   |   |   | 8 | 5 | 6 |
| 4     |    | r6| r6|   | r6| r6|   |   |   |   |
| 5     |    | r3| s9|   | r3| r3|   |   |   |   |
| 6     |    | r5| r5|   | r5| r5|   |   |   |   |
| 7     | s4 |   |   | s3 |   |   |   |   |10 | 6 |
| 8     |    | s7|   |   | s11|   |   |   |   |