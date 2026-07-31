 Here is the markdown content in formal tone without emojis and external links:

### LR parsers for the notes of the Unit 2 - Basic Parsing Techniques in the subject of Compiler Design

1. LR parsers are bottom-up parsers that parse input from Left to Right.
2. They construct a rightmost derivation of the input string.
3. LR parsers use a parsing table called LR(k) parsing table. Here 'k' refers to the number of tokens parsed before deciding which production to use.
4. The parsing table is constructed using the LR(0) items of the grammar. LR(0) items are of the form 'A → α.aβ' where 'α' and 'β' are strings of terminals and non-terminals and 'a' is a terminal or non-terminal.
5. The parsing table has 'state' and 'input symbol' as dimensions. Each entry corresponds to a 'shift' or 'reduce' action.
6. 'Shift' action shifts the input symbol to the stack and moves to the next state. 'Reduce' action pops 'k' symbols from the stack and pushes a non-terminal as per some production.
7. The parsing is successful if there is a sequence of shift and reduce actions that leads to acceptance state. Else, it is a syntax error.
8. LR parsers have deterministic parsing and handle larger class of grammars leading to their wide usage.

The above points summarize the key highlights of LR parsers. Let me know if you would like me to elaborate on any of the points.