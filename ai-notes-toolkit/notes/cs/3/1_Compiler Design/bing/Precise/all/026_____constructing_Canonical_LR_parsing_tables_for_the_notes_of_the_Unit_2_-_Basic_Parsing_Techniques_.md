# Constructing Canonical LR Parsing Tables

Canonical LR parsing is a method for constructing LR parsing tables for context-free grammars. It is also known as LR(1) parsing. The method involves the following steps:

1. **Augmenting the grammar**: The first step in constructing a Canonical LR parsing table is to augment the given grammar by adding a new start symbol and a new production rule. The new start symbol is typically denoted by `S'` and the new production rule is of the form `S' -> S`, where `S` is the original start symbol of the grammar.

2. **Constructing the Canonical collection of LR(1) items**: The next step is to construct the Canonical collection of LR(1) items for the augmented grammar. An LR(1) item is a pair consisting of a production rule and a lookahead symbol. The Canonical collection of LR(1) items is a set of sets of LR(1) items, where each set represents a state in the LR parsing table.

3. **Constructing the parsing table**: The final step is to construct the parsing table using the Canonical collection of LR(1) items. The parsing table has two parts: the action table and the goto table. The action table specifies the parser action (shift, reduce, accept, or error) for each state and input symbol. The goto table specifies the next state for each state and non-terminal symbol.

These are the basic steps involved in constructing Canonical LR parsing tables for context-free grammars. It is important to note that not all context-free grammars are suitable for Canonical LR parsing. Some grammars may require more powerful parsing methods, such as LALR or GLR parsing.