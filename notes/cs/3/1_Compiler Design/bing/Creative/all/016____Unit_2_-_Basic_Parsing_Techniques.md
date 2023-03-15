## Unit 2 - Basic Parsing Techniques

Parsing is the process of analyzing the structure and meaning of a sentence or a text, based on a given grammar. Parsing techniques are methods for implementing parsers, which can be divided into two main categories: top-down and bottom-up.

- Top-down parsing techniques start from the root of the parse tree and try to match the input with the grammar rules, expanding the non-terminals into terminals. Examples of top-down parsing techniques are recursive descent parsing, predictive parsing, and LL parsing.
- Bottom-up parsing techniques start from the leaves of the parse tree and try to reduce the input to the start symbol of the grammar, applying the grammar rules in reverse. Examples of bottom-up parsing techniques are shift-reduce parsing, operator-precedence parsing, and LR parsing.

Some of the advantages and disadvantages of top-down and bottom-up parsing techniques are:

- Top-down parsing techniques are easier to implement and understand, but they may encounter left recursion and backtracking problems, which can cause inefficiency or ambiguity.
- Bottom-up parsing techniques can handle a larger class of grammars and avoid left recursion, but they are more complex and difficult to implement and understand, and they may encounter shift-reduce and reduce-reduce conflicts, which can cause ambiguity or error.

Some of the concepts and terms related to parsing techniques are:

- Grammar: A set of rules that define the syntax and structure of a language.
- Terminal: A symbol that represents a basic unit of a language, such as a keyword, an identifier, or a punctuation mark.
- Non-terminal: A symbol that represents a syntactic category or a group of terminals, such as a statement, an expression, or a declaration.
- Production: A rule that specifies how a non-terminal can be replaced by a sequence of terminals and non-terminals, such as S -> NP VP, where S is the start symbol, NP is the noun phrase, and VP is the verb phrase.
- Derivation: A sequence of applications of production rules that generate a sentence or a text from the start symbol, such as S -> NP VP -> Det N VP -> Det N V NP -> The dog barks at the cat.
- Parse tree: A graphical representation of a derivation, where the nodes are the symbols and the edges are the production rules, such as:

```
       S
      / \
     /   \
    NP    VP
   / \   /  \
  /   \ /    \
Det   N V    NP
 |    | |    / \
The  dog barks Det N
               |  |
              at the cat
```

- Ambiguity: A situation where a sentence or a text can have more than one valid parse tree or derivation, such as the sentence "I saw the man with the telescope", which can have two different meanings depending on how the prepositional phrase "with the telescope" is attached to the rest of the sentence.
- Left recursion: A situation where a production rule has the same non-terminal on the left-hand side and the right-hand side, such as A -> Aa, which can cause infinite loops in top-down parsing techniques.
- Backtracking: A situation where a parsing technique has to undo some of the previous steps and try a different alternative, such as when a recursive descent parser encounters a choice point and fails to match the input with the first option, which can cause inefficiency in top-down parsing techniques.
- Shift-reduce conflict: A situation where a bottom-up parsing technique has to decide whether to shift the next input symbol onto the stack or to reduce the top of the stack by applying a production rule, such as when an operator-precedence parser encounters two operators with the same precedence and associativity, which can cause ambiguity or error in bottom-up parsing techniques.
- Reduce-reduce conflict: A situation where a bottom-up parsing technique has to decide which of two or more production rules to apply to reduce the top of the stack, such as when an LR parser encounters two or more rules with the same right-hand side, which can cause ambiguity or error in bottom-up parsing techniques.