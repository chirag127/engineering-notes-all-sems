### Formal grammars and their application to syntax analysis

- A formal grammar is a set of rules that defines the syntax of a language, i.e., the structure and order of symbols that form valid sentences in the language .
- A formal grammar consists of four components :
  - A set of terminal symbols (V), also called tokens, which are the basic units of the language, such as keywords, identifiers, operators, etc.
  - A set of non-terminal symbols (N), also called variables, which represent syntactic categories, such as expressions, statements, declarations, etc.
  - A set of production rules (P), also called rewrite rules, which specify how a non-terminal symbol can be replaced by a sequence of terminal and/or non-terminal symbols, such as `E -> E + E | E * E | (E) | id`.
  - A start symbol (S), which is a special non-terminal symbol that represents the whole language, such as `S -> program`.
- A formal grammar can be used to generate all possible strings over the alphabet that are syntactically correct in the language, by starting from the start symbol and applying the production rules repeatedly until no non-terminal symbols remain .
- A formal grammar can also be used to check whether a given string is syntactically correct in the language, by trying to derive the string from the start symbol using the production rules, or by constructing a parse tree that shows the hierarchical structure of the string according to the grammar .
- Formal grammars are used mostly in the syntactic analysis phase (parsing) of the compilation process, where the source code is checked for syntactic errors and converted into an intermediate representation that preserves the structure and meaning of the code .
- Formal grammars are also used in natural language processing, where they are used to model the syntax of natural languages, such as English, and to parse natural language texts into meaningful representations.
- There are different types of formal grammars, such as regular grammars, context-free grammars, context-sensitive grammars, and unrestricted grammars, which differ in the complexity and expressiveness of the production rules and the languages they can generate or recognize .