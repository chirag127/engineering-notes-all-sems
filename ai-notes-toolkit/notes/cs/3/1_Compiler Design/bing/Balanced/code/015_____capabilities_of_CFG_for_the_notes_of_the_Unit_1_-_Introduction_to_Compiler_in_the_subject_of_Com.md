### Capabilities of CFG

A context-free grammar (CFG) is a set of rules that defines a language by specifying how any valid string can be derived from a special symbol called the start symbol. A CFG consists of a set of terminals, a set of non-terminals, a start symbol, and a set of production rules.

Some of the capabilities of CFG are:

- CFG can describe most of the programming languages, such as C, Java, Python, etc.  
- CFG can be used to construct efficient parsers automatically if the grammar is properly written. A parser is a program that analyzes the syntax of a string according to a given grammar.  
- CFG can handle syntactic features such as balanced parentheses, matching begin-end, corresponding if-then-else, etc. These features are not possible to handle by regular expressions or finite automata. 
- CFG can construct suitable grammars for expressions by using the features of associativity and precedence information. For example, the grammar for arithmetic expressions can be written as:

```
E -> E + T | T
T -> T * F | F
F -> (E) | id
```

This grammar ensures that the multiplication operator (*) has higher precedence than the addition operator (+), and that the parentheses can be used to change the order of evaluation.