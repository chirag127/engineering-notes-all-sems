# 11. Construct a Shift Reduce Parser for a given language.

A shift reduce parser is a type of bottom-up parser that uses a stack and an input buffer to parse a given string. The parser performs two main operations: shift and reduce.

- Shift: The parser moves the next input symbol from the input buffer to the top of the stack.
- Reduce: The parser replaces the topmost symbols on the stack with a non-terminal symbol, according to a production rule in the grammar.

The parser repeats these operations until either the input buffer is empty and the stack contains only the start symbol, or an error occurs. The parser can use a parsing table to decide which operation to perform at each step, based on the current state of the stack and the input buffer.

The following steps describe how to construct a shift reduce parser for a given language:

1. Write the grammar for the language in the form of production rules. The grammar should be unambiguous and free of left recursion and common prefixes.
2. Convert the grammar into an augmented grammar by adding a new start symbol and a new production rule of the form S' -> S, where S is the original start symbol.
3. Construct the canonical collection of LR(0) items for the augmented grammar. An LR(0) item is a production rule with a dot (.) indicating the current position of the parser. The canonical collection is a set of sets of LR(0) items, where each set is called a state and represents a possible configuration of the stack and the input buffer. The canonical collection can be constructed by applying the following rules:

  - Start with the initial state, which contains only the item S' -> .S
  - For each state, if it contains an item of the form A -> a.Bb, where a and b are strings of symbols and B is a non-terminal, then add all the items of the form B -> .c to the same state, where c is any string of symbols that can be derived from B. This is called the closure operation.
  - For each state, if it contains an item of the form A -> a.Bb, where a and b are strings of symbols and B is a non-terminal, then create a new state that contains only the item A -> aB.b and add a transition from the current state to the new state labeled with B. This is called the goto operation.
  - Repeat the closure and goto operations until no new states or transitions can be added.

4. Construct the parsing table for the canonical collection of LR(0) items. The parsing table has two parts: an action table and a goto table. The action table has one row for each state and one column for each terminal symbol and the end-of-input marker ($). The goto table has one row for each state and one column for each non-terminal symbol. The entries in the parsing table are determined by the following rules:

  - For each state, if it contains an item of the form A -> a.b, where a and b are strings of symbols and b is not empty, then the entry in the action table for that state and the first symbol of b is "shift s", where s is the state that can be reached by following the transition labeled with b from the current state. This means that the parser should perform a shift operation and move to state s.
  - For each state, if it contains an item of the form A -> a., where a is a string of symbols, then the entry in the action table for that state and the lookahead symbol (the next input symbol or $) is "reduce r", where r is the number of the production rule A -> a in the grammar. This means that the parser should perform a reduce operation and apply the production rule A -> a.
  - For each state, if it contains the item S' -> S., then the entry in the action table for that state and $ is "accept". This means that the parser should accept the input string as valid.
  - For each state, if it contains an item of the form A -> a.Bb, where a and b are strings of symbols and B is a non-terminal, then the entry in the goto table for that state and B is the state that can be reached by following the transition labeled with B from the current state. This means that the parser should move to that state after performing a reduce operation with a production rule that has B on the right-hand side.
  - For any other entry in the parsing table, leave it blank or mark it as "error". This means that the parser should report an error if it encounters that situation.

5. Use the parsing table to parse a given input string. The parser starts with an empty stack and the input string in the input buffer.