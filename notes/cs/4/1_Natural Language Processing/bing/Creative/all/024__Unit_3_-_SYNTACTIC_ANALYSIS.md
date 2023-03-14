## Unit 3 - SYNTACTIC ANALYSIS

- Syntactic analysis, also known as parsing, is a process in compiler design where the compiler checks if the source code follows the grammatical rules of the programming language .
- This is typically the second stage of the compilation process, following lexical analysis .
- The main goal of syntactic analysis is to create a parse tree or abstract syntax tree (AST) of the source code, which is a hierarchical representation of the source code that reflects the grammatical structure of the program .
- There are several types of parsing algorithms used in syntactic analysis, including :
  - LL parsing: This is a top-down parsing algorithm that starts with the root of the parse tree and constructs the tree by successively expanding non-terminals. LL parsing is known for its simplicity and ease of implementation.
  - LR parsing: This is a bottom-up parsing algorithm that starts with the leaves of the parse tree and constructs the tree by successively reducing terminals. LR parsing is more powerful than LL parsing and can handle a larger class of grammars.
  - LR (1) parsing: This is a variant of LR parsing that uses lookahead to disambiguate the grammar.
  - LALR parsing: This is a variant of LR parsing that uses a reduced set of lookahead symbols to reduce the number of states in the LR parser.
- Once the parse tree is constructed, the compiler can perform semantic analysis to check if the source code makes sense and follows the semantics of the programming language.
- The parse tree or AST can also be used in the code generation phase of the compiler design to generate intermediate code or machine code.
- The pushdown automata (PDA) is used to design the syntactic analysis phase.
- The grammar for a language consists of production rules.
- Example: Suppose production rules for the grammar of a language are:

```
S -> cAd
A -> bc|a
```

And the input string is “cad”. Now the parser attempts to construct a syntax tree from this grammar for the given input string. It uses the given production rules and applies those as needed to generate the string.

```
    S
   / \
  c   A
     / \
    b   d
```

- Advantages of using syntactic analysis in compiler design include:
  - Structural validation: Syntax analysis allows the compiler to check if the source code follows the grammatical rules of the programming language, which helps to detect and report errors in the source code.
  - Program representation: Syntax analysis provides a parse tree or AST of the source code, which is a useful data structure for further analysis and transformation of the program.
  - Language design: Syntax analysis can help to design and evaluate the syntax of a programming language, by testing if the grammar is unambiguous, consistent, and expressive.
- Disadvantages of using syntactic analysis in compiler design include:
  - Complexity: Syntax analysis can be a complex and time-consuming process, especially for large and complex grammars. Some parsing algorithms may require a lot of memory and computation to construct the parse tree or AST.
  - Error handling: Syntax analysis can be difficult to handle errors gracefully, as some errors may cause the parser to fail or produce incorrect results. Some parsing algorithms may not be able to recover from errors or provide meaningful feedback to the user.
  - Limitations: Syntax analysis can only check the syntactical structure of the source code, but not the semantic meaning or the logical correctness of the program. Some errors or bugs may not be detected by syntax analysis, and may require further analysis or testing.