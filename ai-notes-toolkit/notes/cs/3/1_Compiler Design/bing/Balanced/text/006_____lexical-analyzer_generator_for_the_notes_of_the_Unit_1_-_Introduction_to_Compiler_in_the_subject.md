### Lexical Analyzer Generator

- A lexical analyzer generator is a tool that allows many lexical analyzers to be created with a simple build file.
- A lexical analyzer is a program that reads input, matches the input against a set of regular expressions, and runs the corresponding actions if a regular expression matched.
- A regular expression is a notation that describes a set of strings using characters and operators.
- A lexical analyzer generator takes as input a specification file that contains a list of declarations, rules, and user code.
- A declaration is a statement that provides the generator the context it needs to develop a lexical analyzer, such as the name of the output file, the input character set, the start conditions, and the macro definitions.
- A rule is a pair of a regular expression and an action, which specifies what to do when the input matches the regular expression.
- A user code is a section of code that is copied verbatim to the output file, usually containing the main function, the error handling, and the auxiliary functions.
- A lexical analyzer generator outputs a C or Java program that implements a finite state machine that recognizes the regular expressions in the specification file and executes the actions associated with them.
- A finite state machine is a model of computation that consists of a set of states, a set of input symbols, a transition function that maps a state and an input symbol to a new state, and a set of final states.
- Some examples of lexical analyzer generators are Flex, JFlex, Lex, and ANTLR.