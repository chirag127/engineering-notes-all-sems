
### Shift Reduce Parsing 
Shift reduce parsing is a type of bottom-up parsing used in compiler design. It is an efficient method of parsing a string of tokens, and is used to determine the syntactic structure of a given input. 

Shift reduce parsers are based on the concept of a stack. The parser reads the input string of tokens from left to right and uses the stack to store symbols that have been read so far. The parser then shifts symbols from the input onto the stack, or reduces symbols from the stack when they match a production rule.

#### Advantages
- It is a simple and efficient method of parsing a string of tokens. 
- It is well suited for the implementation of a parser in a compiler. 
- It is relatively easy to understand and implement.

#### Disadvantages
- It does not always yield the most efficient parse tree. 
- It can be difficult to debug.
- It is not suitable for parsing ambiguous grammars.

#### Examples
A simple example of a shift reduce parser is a calculator that reads in a sequence of tokens representing a mathematical expression and produces a parse tree that can be evaluated to produce a result. 

#### Applications
Shift reduce parsers are used in compilers to parse source code and generate parse trees. They are also used in natural language processing applications such as speech recognition, machine translation and information extraction.