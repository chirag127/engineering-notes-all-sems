# Formal grammars and their application to syntax analysis

- A **formal grammar** is a set of rules that defines the syntax of a language, i.e. the structure and order of symbols that form valid sentences in the language .
- A formal grammar consists of four components :
  - A set of **terminals** or **tokens**, denoted by V, which are the basic symbols of the language, such as keywords, identifiers, operators, etc.
  - A set of **non-terminals** or **variables**, denoted by N, which are placeholders for sequences of terminals or other non-terminals, such as expressions, statements, declarations, etc.
  - A set of **productions** or **rules**, denoted by P, which specify how non-terminals can be replaced by sequences of terminals and non-terminals, such as E -> E + E | E * E | (E) | id, where E is a non-terminal and +, *, (, ), and id are terminals.
  - A **start symbol** or **axiom**, denoted by S, which is a special non-terminal that represents the whole language, such as S -> program | statement | expression.
- A formal grammar can be used to generate or derive sentences in the language by starting from the start symbol and applying the productions repeatedly until only terminals are left.
- A formal grammar can also be used to analyze or parse sentences in the language by checking if they can be derived from the start symbol using the productions .
- Syntax analysis or parsing is the process of verifying the syntactic correctness of a sentence in the language using a formal grammar .
- Syntax analysis is typically the second phase of the compilation process, following lexical analysis, where the source code is converted into a sequence of tokens.
- Syntax analysis can be performed by different types of parsers, such as top-down parsers, bottom-up parsers, recursive-descent parsers, etc., depending on the type and complexity of the formal grammar.
- Syntax analysis is concerned with the structure, not the meaning, of the sentences in the language. Semantic analysis is a later phase of the compilation process where the meaning and validity of the sentences are checked .
- Syntax analysis is important for compiler design because it helps to detect and report syntactic errors in the source code, to construct a parse tree or an abstract syntax tree that represents the syntactic structure of the source code, and to facilitate the subsequent phases of the compilation process, such as semantic analysis, code generation, and optimization.