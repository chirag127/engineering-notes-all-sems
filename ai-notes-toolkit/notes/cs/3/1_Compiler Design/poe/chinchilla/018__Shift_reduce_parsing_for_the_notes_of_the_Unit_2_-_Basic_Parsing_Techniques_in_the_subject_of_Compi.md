### Shift Reduce Parsing

Shift Reduce Parsing is a type of bottom-up parsing technique used in Compiler Design. It is also known as LR parsing, where L stands for Left-to-right scanning of the input string, and R stands for Rightmost derivation in reverse order.

The Shift-Reduce parser reads the input string from left to right and reduces the grammar rules from right to left to generate the parse tree. It has two actions, Shift and Reduce, which are performed based on the current state of the parser and the input symbol.

#### Shift Action
- Shift action moves the input symbol to the stack and advances the input pointer to the next symbol.
- Shift action is performed when the parser encounters a terminal symbol or a non-terminal symbol that cannot be reduced further.

#### Reduce Action
- Reduce action replaces a group of symbols on the top of the stack with a non-terminal symbol.
- Reduce action is performed when the parser finds a sequence of symbols on the top of the stack that matches the right-hand side of a grammar rule.

#### Shift-Reduce Conflict
- Shift-Reduce conflict occurs when the parser has to make a decision between Shift and Reduce actions based on the input symbol and the current state of the parser.
- The conflict can be resolved by using a precedence rule or by using a look-ahead symbol to determine the next action.

#### LR Parser
- LR Parser is a type of Shift-Reduce parser that uses a Parsing Table to determine the next action based on the current state of the parser and the input symbol.
- LR Parser is more powerful than LL Parser and can handle a larger class of grammars.

#### Types of LR Parser
- LR(0) Parser: It has no look-ahead symbol and uses only the current state of the parser to determine the next action.
- SLR Parser: It uses a simple look-ahead symbol to resolve Shift-Reduce conflicts and generates a smaller Parsing Table than LR(1) Parser.
- LR(1) Parser: It uses a look-ahead symbol to determine the next action and generates a larger Parsing Table than SLR Parser.
- LALR Parser: It is a compromise between SLR and LR(1) Parser and generates a smaller Parsing Table than LR(1) Parser.

Shift-Reduce Parsing is a widely used parsing technique in Compiler Design and is used in many popular compilers like GCC, Clang, and JavaCC. Understanding the Shift-Reduce Parsing technique and its variants is essential for building efficient and robust compilers.