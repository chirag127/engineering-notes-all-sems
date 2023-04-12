

## Unit 1 - Introduction to Compiler

- A compiler is a program that translates a source program written in a high-level language into a target program written in a low-level language.
- The source program is also called the source code or the input program, and the target program is also called the object code or the output program.
- The high-level language is usually a human-readable and expressive language, such as C, Java, Python, etc., and the low-level language is usually a machine-readable and efficient language, such as assembly, binary, etc.
- The main goal of a compiler is to produce a correct and efficient target program that is equivalent to the source program in terms of functionality and behavior.
- A compiler typically consists of several phases, each of which performs a specific task on the source program or its intermediate representation. The main phases of a compiler are:

  - Lexical analysis: This phase scans the source program and converts it into a sequence of tokens, which are the basic units of syntax, such as keywords, identifiers, literals, operators, etc.
  - Syntax analysis: This phase parses the sequence of tokens and checks if it conforms to the grammar rules of the source language. It also constructs a parse tree or an abstract syntax tree, which is a hierarchical representation of the syntactic structure of the source program.
  - Semantic analysis: This phase performs various checks on the parse tree or the abstract syntax tree, such as type checking, scope checking, declaration checking, etc. It also annotates the tree with additional information, such as types, values, attributes, etc., that are needed for later phases.
  - Intermediate code generation: This phase translates the annotated parse tree or the abstract syntax tree into an intermediate code, which is a low-level but platform-independent representation of the source program. The intermediate code can be in various forms, such as three-address code, quadruples, triples, etc.
  - Code optimization: This phase applies various techniques to improve the quality of the intermediate code, such as eliminating redundant or dead code, simplifying expressions, rearranging statements, etc. The goal is to reduce the execution time or the memory usage of the target program, without changing its functionality or behavior.
  - Code generation: This phase translates the optimized intermediate code into the target code, which is a low-level and platform-dependent representation of the source program. The target code can be in various forms, such as assembly, binary, etc. This phase also performs tasks such as register allocation, instruction selection, etc.
  - Symbol table management: This phase maintains a data structure called the symbol table, which stores information about the symbols (such as variables, functions, constants, etc.) used in the source program. The symbol table is accessed and updated by various phases of the compiler, such as lexical analysis, semantic analysis, code generation, etc.
  - Error handling: This phase detects and reports any errors or warnings that occur during the compilation process, such as lexical errors, syntax errors, semantic errors, etc. The compiler should provide meaningful and helpful messages to the user, and try to recover from the errors and continue the compilation, if possible.



# Phases and Passes of Compiler

## Phases of Compiler
- A phase of a compiler is a step in the compilation process that takes input from the previous stage, processes it and produces output that can be used as input for the next stage of the compiler .
- A phase of a compiler transforms the source code from one representation to another representation.
- The main phases of a compiler are:
  - Lexical analysis: It scans the source code and converts it into a sequence of tokens .
  - Syntax analysis: It checks the syntactic structure of the source code and builds a parse tree .
  - Semantic analysis: It checks the semantic meaning of the source code and performs type checking, scope checking, etc .
  - Intermediate code generation: It generates an intermediate representation of the source code that is independent of the source and target languages .
  - Code optimization: It improves the intermediate code by eliminating redundant or unnecessary code, applying various transformations, etc .
  - Code generation: It produces the final executable code for the target machine or platform .

## Passes of Compiler
- A pass of a compiler is the number of times the compiler traverses through the source code.
- A pass of a compiler can have more than one phase.
- The number of passes of a compiler depends on the complexity of the source and target languages, the design goals of the compiler, the available memory, etc.
- The types of passes of a compiler are:
  - Single pass compiler: It traverses through the source code only once and performs all the phases of compilation in one pass.
  - Two pass compiler: It traverses through the source code twice and performs some phases of compilation in the first pass and some phases in the second pass.
  - Multi pass compiler: It traverses through the source code more than twice and performs each phase of compilation in a separate pass.



# Bootstrapping

- Bootstrapping is the technique for producing a **self-compiling compiler** – that is, a compiler (or assembler) written in the source programming language that it intends to compile.
- A self-compiling compiler is also called a **self-hosting compiler**.
- Bootstrapping is used to create compilers for new or existing languages, or to improve the performance or features of existing compilers.
- Bootstrapping involves the following steps :
  - Stage 0: preparing an environment for the bootstrap compiler to work with. This may include writing a minimal compiler or interpreter for a subset of the source language, or using an existing compiler or interpreter for another language.
  - Stage 1: the bootstrap compiler is produced. This compiler is enough to translate its own source into a program which can run on the target platform.
  - Stage 2: a full compiler is produced by using the bootstrap compiler to compile the source code of the full compiler. This compiler may have more features or optimizations than the bootstrap compiler.
  - Stage 3: the full compiler is used to compile itself. This may result in a faster or more reliable compiler than the one produced in stage 2.
  - Stage 4: the full compiler is used to compile future versions of itself or other programs in the source language.
- Bootstrapping has several advantages, such as :
  - It allows the compiler to be written in a high-level language, which may be easier to understand, debug, and maintain than a low-level language.
  - It reduces the dependency on external tools or platforms, which may not be available or compatible with the target platform.
  - It ensures that the compiler is consistent and compatible with the source language, as it can compile itself and other programs in the same language.
  - It allows the compiler to benefit from its own optimizations and features, as it can apply them to itself and other programs in the same language.
  - It demonstrates the expressiveness and completeness of the source language, as it can implement its own compiler in the same language.



# Finite state machines and regular expressions and their applications to lexical analysis

- Finite state machines (FSMs) are abstract models of computation that can process a sequence of inputs and change their state accordingly.
- Regular expressions (REs) are algebraic notations that can specify a set of strings, called a regular language, using symbols and operators.
- Lexical analysis is the first phase of a compiler, where the source code is scanned and divided into meaningful units, called tokens.
- The applications of FSMs and REs to lexical analysis are:
  - FSMs can be used as recognizers for REs, that is, they can determine whether a given input string belongs to the language specified by a RE.
  - REs can be used as generators for FSMs, that is, they can provide a concise and convenient way of describing the structure and syntax of tokens.
  - Algorithms exist to convert REs to FSMs and vice versa, which can facilitate the design and implementation of lexical analyzers.
  - FSMs can be implemented using lookup tables or transition diagrams, which can be easily encoded and executed by a computer program.
  - REs and FSMs can handle common lexical patterns, such as identifiers, keywords, literals, operators, comments, etc.



# Optimization of DFA-Based Pattern Matchers

- A pattern matcher is a program that takes a text and a pattern as input and finds all the occurrences of the pattern in the text.
- A pattern can be specified by a regular expression, which is a concise way of describing a set of strings that share some common features.
- A regular expression can be converted to a finite automaton, which is a machine that can recognize the strings that match the pattern.
- A finite automaton can be either nondeterministic (NFA) or deterministic (DFA). An NFA can have multiple transitions from a state on the same input symbol, while a DFA can have only one transition from a state on any input symbol.
- A DFA is more efficient than an NFA for pattern matching, because it can process the input text in one pass, without backtracking or guessing. However, a DFA may have more states than an NFA, which can increase the memory and time requirements of the pattern matcher.
- Therefore, it is desirable to optimize the DFA-based pattern matcher by reducing the number of states and transitions, while preserving the functionality and correctness of the pattern matcher.
- There are three main algorithms that can be used to optimize the DFA-based pattern matcher:

  - The first algorithm is to convert a regular expression directly to a DFA, without constructing an intermediate NFA. This can save the time and space of converting an NFA to a DFA, which can be exponential in the worst case. The algorithm uses a syntax tree to represent the regular expression, and computes some functions on the tree nodes to construct the DFA states and transitions. The algorithm is based on the following paper: Aho, A. V., & Ullman, J. D. (1972). The theory of parsing, translation, and compiling. Volume I: Parsing. Prentice-Hall, Inc. 
  - The second algorithm is to minimize the number of states of a DFA, by finding and merging equivalent states. Two states are equivalent if they have the same behavior on any input string, that is, they lead to the same final state or to the same nonfinal state. The algorithm uses a partitioning technique to divide the states into equivalence classes, and replaces each class by a single representative state. The algorithm is based on the following paper: Hopcroft, J. E. (1971). An n log n algorithm for minimizing states in a finite automaton. In Z. Kohavi (Ed.), Theory of machines and computations (pp. 189-196). Academic Press. 
  - The third algorithm is to compress the transition table of a DFA, by exploiting the regularities and redundancies in the table. The algorithm uses a technique called table filling to find and eliminate the redundant entries in the table, and then uses a technique called table splitting to divide the table into smaller and more compact subtables. The algorithm is based on the following paper: Larsson, N. J., & Moffat, A. (2000). Off-line dictionary-based compression. Proceedings of the IEEE, 88(11), 1722-1732. 

- These algorithms can be applied separately or in combination to optimize the DFA-based pattern matcher for different criteria, such as speed, space, or simplicity.



# Implementation of Lexical Analyzers

- Lexical analysis is the first phase of the compiler design, also known as a scanner.
- It converts the high-level input program into a sequence of tokens, which are the smallest meaningful units of the program.
- A token is a pair of a token name and an optional attribute value. For example, the token `id` has an attribute value that is the name of the identifier, such as `x` or `sum`.
- A lexeme is the actual string of characters that matches the pattern of a token. For example, `x` and `sum` are lexemes of the token `id`.
- A lexical analyzer is a program that implements the process of lexical analysis. It takes a stream of input characters and returns a stream of tokens.
- A lexical analyzer can be implemented with a deterministic finite automaton (DFA), which is a finite state machine that accepts or rejects a string based on its final state.
- A DFA consists of a set of states, a set of input symbols, a transition function that maps a state and an input symbol to a next state, a start state, and a set of final states.
- A DFA can be represented by a transition diagram, which is a graph where the nodes are the states and the edges are labeled by the input symbols.
- A DFA can also be represented by a transition table, which is a matrix where the rows are the states, the columns are the input symbols, and the entries are the next states.
- A lexical analyzer can be generated automatically from a set of regular expressions, which are a concise and expressive way of specifying the patterns of the tokens.
- A regular expression is a string that defines a language, which is a set of strings that match the expression.
- A regular expression can be constructed from the following rules:
  - A single character is a regular expression that matches itself.
  - The empty string ε is a regular expression that matches the empty string.
  - If r and s are regular expressions, then
    - (r) is a regular expression that matches r.
    - r|s is a regular expression that matches either r or s.
    - rs is a regular expression that matches the concatenation of r and s.
    - r* is a regular expression that matches zero or more occurrences of r.
    - r+ is a regular expression that matches one or more occurrences of r.
    - r? is a regular expression that matches zero or one occurrence of r.
- A lexical analyzer generator is a tool that takes a set of regular expressions and produces a lexical analyzer in a programming language, such as C or Java.
- A lexical analyzer generator can use the following steps to convert a regular expression to a DFA:
  - Construct a nondeterministic finite automaton (NFA) for each regular expression using Thompson's construction algorithm.
  - Combine the NFAs for all the regular expressions using the union operation and add a new start state that has ε-transitions to the start states of the NFAs.
  - Eliminate the ε-transitions from the NFA using the ε-closure algorithm.
  - Convert the NFA to a DFA using the subset construction algorithm.
  - Minimize the DFA using the partition refinement algorithm.
  - Generate the code for the DFA using a template.
- Some examples of lexical analyzer generators are lex, flex, JLex, and ANTLR.



# Lexical Analyzer Generator

A lexical analyzer generator is a tool that allows the creation of lexical analyzers, also known as scanners or lexers, from a specification file. A lexical analyzer is a program that reads an input stream of characters and produces a stream of tokens, each representing a lexical unit such as a keyword, an identifier, a constant, etc.

A lexical analyzer generator takes as input a specification file that contains a set of regular expressions and corresponding actions. A regular expression is a notation that describes a set of strings that share a common pattern. An action is a piece of code that is executed when a regular expression is matched by the input. The specification file also contains some declarations that provide the generator the context and the options it needs to generate a lexical analyzer.

A lexical analyzer generator outputs a source code file that implements a lexical analyzer according to the specification file. The source code file is usually written in a programming language such as C, Java, or Python. The lexical analyzer can then be compiled and linked with other modules to form a complete compiler or interpreter.

Some examples of lexical analyzer generators are:

- Flex: A fast lexical analyzer generator for C. It is a free and open-source software alternative to lex.
- JFlex: A fast lexical analyzer generator for Java. It is also free and open-source software.
- Lex: The original lexical analyzer generator for C. It is part of the Unix operating system.
- PLY: A Python implementation of lex and yacc. It is a pure-Python module that can generate lexical analyzers and parsers.

The advantages of using a lexical analyzer generator are:

- It simplifies the task of writing a lexical analyzer by using a concise and expressive notation (regular expressions) to specify the lexical rules.
- It ensures the correctness and efficiency of the lexical analyzer by using a well-tested and optimized algorithm to generate the source code.
- It allows the reuse and portability of the specification file across different platforms and languages by using a standard format and interface.



# LEX compiler

- LEX is a computer program that generates lexical analyzers (\"scanners\" or \"lexers\").
- Lexical analyzer is a program that takes a stream of input characters and produces a stream of tokens as output.
- Tokens are the smallest meaningful units of a program, such as keywords, identifiers, literals, operators, etc.
- LEX is commonly used with the yacc parser generator, which takes a stream of tokens and produces a parse tree as output.
- A parse tree is a hierarchical representation of the syntactic structure of a program.
- LEX uses a special notation to specify the patterns of the tokens and the actions to be performed when a pattern is matched.
- A LEX program consists of three sections: definitions, rules, and user subroutines.
- The definitions section contains declarations of variables, constants, macros, and regular expressions.
- The rules section contains pairs of patterns and actions, where a pattern is a regular expression that describes a token, and an action is a C code fragment that is executed when the pattern is matched.
- The user subroutines section contains additional C functions that are called by the actions or the main function.
- The LEX compiler transforms a LEX program (usually with the extension .l) to a C program (usually with the name lex.yy.c). 
- The C program contains the definition of a function called yylex(), which implements the lexical analyzer.
- The C program also contains the definitions of some global variables and functions, such as yytext, yyin, yyout, etc.
- The C program can be compiled by any C compiler (such as gcc) to produce an executable file (usually with the name a.out).  
- The executable file can be run on any input file or standard input, and it will produce the tokens as output on the standard output or a specified output file.  
- LEX is a powerful and flexible tool for creating lexical analyzers for various applications, such as compilers, interpreters, text editors, etc.



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



# BNF Notation for the notes of the Unit 1 - Introduction to Compiler in the subject of Compiler Design

- BNF stands for **Backus Naur Form** notation  .
- It is a **formal method** for describing the **syntax** of programming languages and other types of computer input    .
- The syntax means the **structure of strings** in a certain language.
- BNF was introduced by **John Bakus** and **Peter Naur** in 1960 .
- BNF and **CFG** (Context Free Grammar) are nearly identical.
- BNF uses the following symbols and conventions  :
  - **::=** means "is defined as".
  - **< >** enclose **non-terminal** symbols, which are placeholders for syntactic categories.
  - **|** means "or" and separates alternative definitions of a non-terminal.
  - **" "** enclose **terminal** symbols, which are literal strings or characters.
  - **[ ]** enclose optional parts of a definition.
  - **{ }** enclose parts of a definition that can be repeated zero or more times.
  - **( )** are used for grouping parts of a definition.
- For example, the following BNF defines a simple arithmetic expression language:

```
<expression> ::= <term> | <expression> "+" <term> | <expression> "-" <term>
<term> ::= <factor> | <term> "*" <factor> | <term> "/" <factor>
<factor> ::= <number> | "(" <expression> ")"
<number> ::= <digit> | <number> <digit>
<digit> ::= "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
```

- BNF can be extended with additional symbols and features, such as **comments**, **annotations**, **regular expressions**, **precedence**, and **associativity** .
- Some variants of BNF are **EBNF** (Extended Backus Naur Form), **ABNF** (Augmented Backus Naur Form), and **LBNF** (Labeled Backus Naur Form) .
- BNF is useful for **specifying**, **analyzing**, and **generating** programming languages and other types of computer input  .



# Ambiguity in Compiler Design

- Ambiguity in grammar is not good for a compiler construction.
- A grammar is ambiguous if it can produce more than one parse tree for the same sentence  .
- An ambiguous grammar or string can have multiple meanings.
- Ambiguity can cause problems in syntax analysis and semantic analysis of the source code.
- No method can detect and remove ambiguity automatically, but it can be removed by either re-writing the whole grammar without ambiguity, or by setting and following associativity and precedence constraints.
- Some common sources of ambiguity are:
  - Left recursion: A grammar is left recursive if it has a rule of the form A -> Aα, where A is a non-terminal and α is a string of terminals and non-terminals. Left recursion can cause infinite loops in top-down parsers .
  - Dangling else: A grammar is ambiguous if it has a rule of the form S -> if E then S else S | if E then S | other, where E is an expression and S is a statement. Dangling else can cause confusion about which if statement the else clause belongs to.
  - Operator precedence and associativity: A grammar is ambiguous if it has rules of the form E -> E + E | E * E | id, where E is an expression and id is an identifier. Operator precedence and associativity can cause ambiguity about the order of evaluation of the operators.



# YACC for the notes of the Unit 1 - Introduction to Compiler in the subject of Compiler Design

- YACC stands for Yet Another Compiler-Compiler. It is a tool that generates a parser for a given grammar.
- A parser is a program that analyzes the syntactic structure of a source code and checks if it conforms to the rules of a language.
- A grammar is a set of rules that define the syntax of a language. It consists of terminals, non-terminals, and production rules.
- YACC is often used with a lexical analyzer tool such as lex, which is used to tokenize the input source code into a stream of tokens.
- YACC is based on the LALR(1) parsing algorithm, which stands for LookAhead, Left-to-right, Rightmost derivation with 1 lookahead token. It is a variant of the LR(1) algorithm, which is more efficient and compact.
- YACC takes a grammar specification file as input and produces a C program as output. The grammar specification file has three sections: definitions, rules, and user code.
- The definitions section contains declarations of tokens, variables, and other information that are used by the parser.
- The rules section contains the production rules of the grammar, each followed by an optional action that is executed when the rule is applied.
- The user code section contains any C code that is needed by the parser, such as header files, global variables, or functions.
- YACC can handle ambiguous grammars, but it may produce a parser that is not deterministic or correct. It can also detect and report syntax errors in the input source code.
- YACC is widely used for compiler design, as it simplifies the task of writing a parser and allows the programmer to focus on the semantics and optimization of the language.



# The syntactic specification of programming languages

- The syntax of a programming language defines the **form** and **structure** of the source code that can be written in that language. It specifies the rules for creating **valid** and **meaningful** sentences or statements in the language.  
- The syntax of a programming language can be described at three levels: 
  - **Lexical level**: This level determines how characters form **tokens**, which are the basic components of the source code. Tokens can be identifiers, operators, constants, separators, or reserved words. Each token has a specific pattern or rule that defines its valid characters and length. For example, in C, an identifier can start with a letter or an underscore, followed by any number of letters, digits, or underscores, and cannot be a reserved word.
  - **Grammatical level**: This level determines how tokens form **phrases**, which are the syntactic units of the language. Phrases can be expressions, statements, declarations, or commands. Each phrase has a specific structure or rule that defines its valid tokens and their order. For example, in C, an assignment statement has the form `identifier = expression;`, where `identifier` and `expression` are phrases, and `=` and `;` are tokens.
  - **Contextual level**: This level determines the **meaning** and **validity** of the phrases in the language. It checks the **naming conventions**, **type compatibility**, **scope rules**, and **semantic constraints** of the phrases. For example, in C, a variable must be declared before it is used, and its type must match the type of the expression assigned to it.
- The syntax of a programming language can be specified using different methods, such as **formal grammars**, **syntax diagrams**, or **metasyntax notations**.  
  - **Formal grammars**: A formal grammar is a set of rules that defines the syntax of a language using **symbols** and **productions**. A symbol can be a **terminal** (a token) or a **nonterminal** (a phrase). A production is a rule that specifies how a nonterminal can be replaced by a sequence of symbols. For example, a grammar for arithmetic expressions can have the following symbols and productions:

    - Symbols: `E` (expression), `T` (term), `F` (factor), `+` (plus), `-` (minus), `*` (multiply), `/` (divide), `(` (left parenthesis), `)` (right parenthesis), `num` (number)
    - Productions: `E -> E + T | E - T | T`, `T -> T * F | T / F | F`, `F -> ( E ) | num`
  - **Syntax diagrams**: A syntax diagram is a graphical representation of the syntax of a language using **boxes**, **lines**, and **symbols**. A box represents a nonterminal, a line represents a sequence of symbols, and a symbol represents a terminal or another nonterminal. For example, a syntax diagram for arithmetic expressions can have the following boxes, lines, and symbols:

    ```
    E ┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
      │                                                                                                                                                                                                                                                               │
      └─┬─ T ─┬─┬─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬─┘
        │     │ │                                                                                                                                                                                                                                                     │
        └─ + ─┘ └─ - ─┘
    T ┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
      │                                                                                                                                                                                                                                                               │
      └─┬─ F ─┬─┬─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬─┘
        │     │ │                                                                                                                                                                                                                                                     │
        └─ * ─┘ └─ / ─┘
    F ┌────────

```




# Context Free Grammars

- A context free grammar (CFG) is a set of rules that defines a formal language. A formal language is a set of strings that can be generated by following the rules of the grammar. 
- A CFG consists of four components: a set of terminals, a set of non-terminals, a start symbol, and a set of productions. 
- Terminals are the basic symbols of the language, such as letters, digits, or punctuation marks. Non-terminals are placeholders for sequences of terminals or other non-terminals. The start symbol is a special non-terminal that represents the whole language. Productions are rules that specify how to replace a non-terminal with a sequence of terminals and/or non-terminals. 
- A CFG can be written in Backus-Naur form (BNF), which is a notation that uses angle brackets (<>) to enclose non-terminals, and uses ::= to separate the left-hand side (LHS) and the right-hand side (RHS) of a production. For example, the following BNF defines a CFG for arithmetic expressions: 

```
<expr> ::= <term> | <term> + <expr> | <term> - <expr>
<term> ::= <factor> | <factor> * <term> | <factor> / <term>
<factor> ::= <number> | ( <expr> )
<number> ::= <digit> | <digit> <number>
<digit> ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
```

- A CFG can generate a string by starting from the start symbol and applying productions until only terminals are left. For example, the CFG above can generate the string "2 + 3 * 4" by the following steps: 

```
<expr>
<term> + <expr>
<factor> + <expr>
<number> + <expr>
<digit> + <expr>
2 + <expr>
2 + <term>
2 + <factor> * <term>
2 + <number> * <term>
2 + <digit> * <term>
2 + 3 * <term>
2 + 3 * <factor>
2 + 3 * <number>
2 + 3 * <digit>
2 + 3 * 4
```

- A CFG can also be represented by a parse tree, which is a tree structure that shows how a string is derived from the grammar. The root of the tree is the start symbol, the leaves are the terminals, and the internal nodes are the non-terminals. Each node is labeled with the LHS of a production, and its children are labeled with the RHS of the same production. For example, the parse tree for the string "2 + 3 * 4" is: 

```
<expr>
 / | \
<term> + <expr>
 |    / | \
<factor> * <term>
 |      |    |
<number> 3 <factor>
 |         |
<digit>    4
 |
 2
```

- A CFG is context free because the LHS of each production is a single non-terminal, and the RHS does not depend on the context of the non-terminal. This means that a non-terminal can be replaced by the same RHS regardless of where it appears in the string. 
- CFGs are useful for describing the syntax of programming languages, natural languages, and other formal systems. They can be used to design parsers, which are programs that check if a given string is valid according to the grammar, and construct the corresponding parse tree.   
- CFGs are also useful for studying the properties and limitations of formal languages. For example, some languages are not context free, meaning that they cannot be described by any CFG. Some examples of non-context free languages are: 

  - The language of palindromes, which consists of strings that are the same when reversed, such as "abba" or "racecar".
  - The language of matching parentheses, which consists of strings that have balanced pairs of parentheses, such as "(())" or "(()())".
  - The language of copies, which consists of strings that have two identical halves, such as "abab" or "xyzxyz".

- CFGs can be simplified by removing redundant or



# Derivation and Parse Trees

- Derivation is the process of applying production rules to replace non-terminal symbols in a string with terminal symbols or other non-terminal symbols .
- A production rule is a rule that defines how a non-terminal symbol can be rewritten as a sequence of terminal and/or non-terminal symbols .
- A grammar is a set of production rules that specify the syntax of a language .
- A parse tree is a hierarchical structure that represents the derivation of the grammar to yield input strings   .
- The root node of a parse tree has the start symbol of the grammar, and the leaf nodes have the terminal symbols of the input string   .
- A parse tree shows the order and the way in which the production rules are applied to generate the input string   .
- A parse tree can be drawn using the following steps:
  - Start with the start symbol as the root node.
  - Choose a production rule that has the root node as the left-hand side, and write the right-hand side as the children of the root node.
  - Repeat the above step for each non-terminal node, until all the nodes are terminal symbols.
  - If there is no production rule that can be applied to a non-terminal node, or if the terminal symbols do not match the input string, then the parse tree is invalid.
- A parse tree can also be called a concrete syntax tree, if it directly corresponds to the context-free grammar.
- An example of a parse tree for the input string `a + b * c` and the grammar `E -> E + T | T`, `T -> T * F | F`, `F -> a | b | c` is:

```
      E
     / \
    E   T
   / \ / \
  T  + T  F
 / \   |  |
F  *  F  c
|  |  |
a  b  b
```



# Capabilities of CFG for the notes of the Unit 1 - Introduction to Compiler in the subject of Compiler Design

- CFG stands for Context-Free Grammar, which is a formal notation for describing the syntax of a programming language.
- A CFG consists of a set of production rules that specify how to derive strings from a start symbol, using a finite set of non-terminal symbols and terminal symbols.
- A terminal symbol is a symbol that cannot be further derived, such as a keyword, an operator, or a literal in a programming language.
- A non-terminal symbol is a symbol that can be replaced by a sequence of symbols according to the production rules, such as an expression, a statement, or a program in a programming language.
- A start symbol is a special non-terminal symbol that represents the whole language.
- A production rule has the form A -> α, where A is a non-terminal symbol and α is a sequence of terminal and non-terminal symbols. It means that A can be replaced by α in a derivation.
- A derivation is a sequence of steps that apply production rules to generate a string from the start symbol. It shows how a string belongs to the language defined by the CFG.
- A parse tree is a graphical representation of a derivation, where the nodes are symbols and the edges are production rules. It shows the hierarchical structure of a string in the language.
- CFGs have the following capabilities for describing the syntax of programming languages:
  - They can capture the recursive nature of many syntactic constructs, such as nested expressions, statements, and functions.
  - They can express the precedence and associativity of operators, by using different levels of non-terminal symbols and production rules.
  - They can handle ambiguous syntax, by allowing multiple derivations or parse trees for the same string. However, ambiguity is usually undesirable and should be resolved by using additional rules or conventions.
  - They can be easily manipulated and analyzed by algorithms, such as parsing, which is the process of finding a derivation or a parse tree for a given string. Parsing is an essential task for compilers, as it checks the syntactic correctness of the source code and produces an intermediate representation for further processing.



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



# Parsers for the notes of the Unit 2 - Basic Parsing Techniques in the subject of Compiler Design

- A parser is a program that is part of the compiler, and parsing is part of the compiling process.
- Parsing happens during the analysis stage of compilation. In parsing, code is taken from the preprocessor, broken into smaller pieces and analyzed so other software can understand it.
- The parser takes a token string as input and with the help of existing grammar, converts it into the corresponding Intermediate Representation (IR). The parser is also known as Syntax Analyzer.
- The parser checks the syntax of the source program and reports any errors. It also constructs a parse tree or syntax tree, which is a hierarchical representation of the structure of the source program.
- There are two main types of parsers: top-down parsers and bottom-up parsers.
  - Top-down parsers start from the root of the parse tree and try to match the input with the leftmost derivation of the grammar. They can be further classified into recursive descent parsers and predictive parsers.
    - Recursive descent parsers use recursive procedures to process each non-terminal symbol in the grammar. They may have more than one production to choose from for a single instance of input, which leads to backtracking.
    - Predictive parsers use a parsing table to decide which production to apply based on the input and stack element combination. They do not require backtracking, but they can only handle a subset of grammars called LL(1) grammars.
  - Bottom-up parsers start from the leaves of the parse tree and try to reduce the input to the start symbol of the grammar. They can be further classified into shift-reduce parsers and operator-precedence parsers.
    - Shift-reduce parsers use a stack and an input buffer to perform two operations: shift and reduce. Shift moves a symbol from the input buffer to the stack, and reduce applies a production to replace a string of symbols on the top of the stack. They can handle a larger class of grammars than predictive parsers, but they may encounter conflicts.
    - Operator-precedence parsers are a special type of shift-reduce parsers that can handle expressions with operators and operands. They use a precedence table to determine the relative precedence of the operators and operands in the input. They can only handle a subset of grammars called operator-precedence grammars.



# Shift Reduce Parsing

Shift reduce parsing is a type of bottom-up parsing that uses a stack and an input buffer to construct a parse tree for a given input string and a grammar. Shift reduce parsing performs two actions: shift and reduce .

- Shift: This involves moving symbols from the input buffer onto the stack.
- Reduce: This involves replacing a handle (a substring of the stack that matches the right-hand side of a production) with the corresponding left-hand side non-terminal.

The parsing process starts with an empty stack and the input string in the input buffer. The parser repeatedly applies shift or reduce actions until either the stack contains the start symbol of the grammar and the input buffer is empty, or no action is possible. In the former case, the parsing is successful and the parse tree can be obtained by tracing the reductions. In the latter case, the parsing fails and the input string is not accepted by the grammar .

Shift reduce parsing is efficient and table-driven, but it has some limitations. For example, it cannot handle left-recursive grammars, ambiguous grammars, or grammars that require more than one symbol of lookahead. To overcome these limitations, variations of shift reduce parsing, such as LR parsing, SLR parsing, LALR parsing, and CLR parsing, have been developed. These variations use different techniques to construct the parsing tables and resolve conflicts that may arise during parsing.



# Operator Precedence Parsing

- Operator precedence parsing is a bottom-up parsing technique that can parse a subset of LR(1) grammars.
- A grammar is said to be operator precedence if it has two properties:
  - It does not contain epsilon productions (productions with empty right-hand side).
  - It does not contain two consecutive nonterminals in the right-hand side of any production.
- Operator precedence parsing uses a stack and an input buffer to parse the input string.
- The stack initially contains a special symbol `$` that indicates the bottom of the stack.
- The input buffer initially contains the input string followed by a special symbol `$` that indicates the end of the input.
- The parser maintains a relation between the terminal symbols of the grammar, which can be one of the following:
  - Less than (`<`): The symbol on the top of the stack has lower precedence than the symbol at the front of the input buffer.
  - Equal to (`=`): The symbol on the top of the stack has the same precedence as the symbol at the front of the input buffer.
  - Greater than (`>`): The symbol on the top of the stack has higher precedence than the symbol at the front of the input buffer.
  - Error (` `): There is no relation between the symbol on the top of the stack and the symbol at the front of the input buffer.
- The relation between the terminal symbols can be defined by a precedence table or by precedence functions.
- The parser performs one of the following actions depending on the relation between the symbols:
  - Shift: If the relation is `<` or `=`, the parser pushes the symbol from the input buffer to the stack and advances the input pointer.
  - Reduce: If the relation is `>`, the parser pops the symbols from the stack until it finds a handle (a right-hand side of a production) and replaces it with the corresponding left-hand side (nonterminal).
  - Accept: If the relation is `=` and both the symbols are `$`, the parser accepts the input as valid and halts.
  - Error: If the relation is error or there is no handle on the stack, the parser reports an error and halts.
- Operator precedence parsing is simple and efficient, but it can only handle a limited class of grammars and it cannot detect some syntax errors.
- Operator precedence parsing is commonly used for parsing expressions involving arithmetic, logical, and bitwise operators.



# Top-Down Parsing

- Top-down parsing is a method of parsing the input string provided by the lexical analyzer.
- The top-down parser parses the input string and then generates the parse tree for it.
- Construction of the parse tree starts from the root node i.e. the start symbol of the grammar.
- The parser expands the non-terminals using the grammar productions and matches the terminals with the input symbols.
- The parser uses leftmost derivation to generate the parse tree.
- The parser stops when the input string is consumed and the parse tree is complete.

## Types of Top-Down Parsers

- There are two types of top-down parsers: recursive descent parser and predictive parser.
- Recursive descent parser is a top-down parser that uses a set of recursive procedures to process the input string.
- Each procedure corresponds to a non-terminal symbol in the grammar.
- The parser calls the procedure for the start symbol and then recursively calls the procedures for the non-terminals in the right-hand side of the production.
- The parser backtracks if a procedure fails to match the input string.
- Predictive parser is a top-down parser that does not use backtracking.
- It predicts the next production to be used based on the current input symbol and the top of the stack.
- It uses a parsing table to store the predictions for each non-terminal and input symbol pair.
- The parser is also known as LL(1) parser, where L stands for left-to-right scanning of the input, L stands for leftmost derivation, and 1 stands for one symbol lookahead.



# Predictive Parsers

- A predictive parser is a type of top-down parser that does not require backtracking or backup  .
- A predictive parser can predict which production to use by looking at the next input symbol .
- A predictive parser uses a look-ahead pointer to point to the next input symbol.
- A predictive parser can be implemented by a recursive descent parser or a table-driven parser  .
- A predictive parser can only handle a subset of context-free grammars called LL(1) grammars .
- A predictive parser has the following advantages:
  - It is simple and easy to implement .
  - It does not suffer from backtracking or ambiguity .
  - It can handle left recursion and left factoring .
- A predictive parser has the following disadvantages:
  - It cannot handle all context-free grammars .
  - It may require grammar transformations to make it LL(1) .
  - It may produce a large parsing table .
- A predictive parser algorithm can be summarized as follows:
  - Make a transition diagram (DFA/NFA) for every rule of grammar.
  - Optimize the DFA by reducing the number of states, yielding the final transition diagram.
  - Simulate the string on the transition diagram to parse a string.



# Automatic Construction of Efficient Parsers

- A parser is a program that analyzes the syntactic structure of a given input according to a given grammar.
- A parser can be constructed manually or automatically by using a parser generator tool.
- A parser generator is a program that takes a grammar specification as input and produces a parser program as output.
- A parser generator can also produce a parsing table, which is a data structure that guides the parsing process.
- There are different types of parsers, such as top-down parsers, bottom-up parsers, and hybrid parsers.
- Top-down parsers start from the start symbol of the grammar and try to derive the input by applying production rules.
- Bottom-up parsers start from the input and try to reduce it to the start symbol by applying production rules in reverse.
- Hybrid parsers combine the features of both top-down and bottom-up parsers.
- One of the most widely used types of bottom-up parsers is the LR parser, which stands for Left-to-right scan and Rightmost derivation.
- An LR parser can handle a large class of grammars, including those that are ambiguous or have left recursion.
- An LR parser uses a stack and a parsing table to parse the input.
- The parsing table consists of two parts: the action table and the goto table.
- The action table tells the parser what action to perform for each state and input symbol: shift, reduce, accept, or error.
- The goto table tells the parser what state to go to after a reduction.
- The parsing table is constructed from the canonical collection of LR(0) items, which are sets of production rules with a dot indicating the position of the parser.
- The canonical collection of LR(0) items is obtained by applying the closure and goto operations on the augmented grammar, which is the original grammar with a new start symbol and a new production rule.
- The closure operation adds all the production rules that can be derived from a given item by expanding the nonterminal symbol after the dot.
- The goto operation moves the dot one position to the right for a given item and a given input symbol.
- The canonical collection of LR(0) items forms the states of the LR parser, and the transitions between them are determined by the goto operation.
- The action table is filled by applying the following rules for each state and input symbol:
  - If the item is of the form A -> α.aβ, where a is a terminal symbol, then the action is to shift and go to the state obtained by the goto operation on a.
  - If the item is of the form A -> α., then the action is to reduce by the production rule A -> α, unless A is the new start symbol, in which case the action is to accept.
  - If the item is of the form S' -> S., where S' is the new start symbol and S is the original start symbol, then the action is to accept.
  - If there is no item for the given state and input symbol, then the action is to report an error.
- The goto table is filled by applying the goto operation on each state and nonterminal symbol.
- An LR(0) parser can handle only a subset of LR grammars, which are those that do not have any conflicts in the action table.
- A conflict occurs when there are two or more different actions for the same state and input symbol.
- There are two types of conflicts: shift-reduce conflicts and reduce-reduce conflicts.
- A shift-reduce conflict occurs when the parser can either shift or reduce for the same state and input symbol.
- A reduce-reduce conflict occurs when the parser can reduce by two or more different production rules for the same state and input symbol.
- To resolve conflicts, the LR(0) parser can be extended to use more lookahead symbols, which are the symbols that follow the input symbol in the input string.
- The number of lookahead symbols used by the parser is indicated by a subscript in the LR notation, such as LR(1), LR(2), etc.
- An LR(1) parser uses one lookahead symbol to decide the action for each state and input symbol.
- An LR(1) parser is constructed from the canonical collection of LR(1) items, which are sets of production rules with a dot and a lookahead symbol.
- The canonical collection of LR(1) items is obtained by applying the closure and goto operations on the augmented grammar, similar to the LR(0) case, but with the following modifications:
  - The closure operation adds all the production rules that can be derived from a given item by expanding the nonterminal symbol after the dot, and propag



# LR parsers

- LR parsers are a type of **bottom-up parsers** that analyse **deterministic context-free languages** in linear time.
- LR parsers read the input from **left to right** and produce a **rightmost derivation** in reverse.
- LR parsers use a **stack** to store the symbols of the derivation and a **state transition table** to guide the parsing actions.
- LR parsers can handle a large class of grammars, including **all LR(k) grammars**, which are grammars that can be parsed by an LR parser with **k** symbols of lookahead.
- There are several variants of LR parsers, such as:
  - **SLR parsers**, which use a simplified version of the LR(0) state transition table and a follow set to determine the reduce actions.
  - **LALR parsers**, which use a compressed version of the LR(1) state transition table by merging states with the same LR(0) core.
  - **Canonical LR(1) parsers**, which use the full LR(1) state transition table with one symbol of lookahead for each item.
  - **Minimal LR(1) parsers**, which use a reduced version of the LR(1) state transition table by eliminating redundant states and transitions.
  - **GLR parsers**, which use a generalized version of the LR algorithm that can handle **ambiguous grammars** by creating multiple parse trees.
- LR parsers have some advantages over other types of parsers, such as:
  - LR parsers can detect syntax errors as soon as possible, without reading the entire input.
  - LR parsers can handle left-recursive grammars and grammars with common prefixes, which are problematic for LL parsers.
  - LR parsers can parse a larger class of grammars than LL parsers, and are more efficient than backtracking parsers.
- LR parsers also have some disadvantages, such as:
  - LR parsers are more complex and difficult to construct than LL parsers, especially for large grammars.
  - LR parsers may require more memory than LL parsers, due to the size of the state transition table.
  - LR parsers may not be suitable for interactive or incremental parsing, as they require the entire input to be available before parsing.



# The Canonical Collection of LR(0) Items

- An **LR(0) item** is a production of a grammar G with a dot at some position on the right side of the production .
- The dot indicates how much of the input has been scanned up to a given point in the process of parsing.
- For example, the production `S -> XYZ` yields four items: `S -> .XYZ`, `S -> X.YZ`, `S -> XY.Z`, `S -> XYZ.`.
- A **canonical collection of LR(0) items** is a set of sets of LR(0) items that is used to construct the SLR functions closure and goto.
- The canonical collection of LR(0) items for a grammar G is obtained by the following algorithm :

  - Start with the augmented grammar G' that has a new start symbol S' and a production S' -> S.
  - Compute the closure of the set containing the item S' -> .S and add it to the collection as I0.
  - For each set of items I in the collection and each grammar symbol X, compute the goto of I on X and add it to the collection if it is not empty and not already present.
  - Repeat the previous step until no new sets of items can be added to the collection.

- The **closure** of a set of items I is the set of items that can be derived from I by adding items that have the dot before a nonterminal and expanding that nonterminal with its productions .
- For example, if I contains the item `A -> a.Bc` and B has the productions `B -> b` and `B -> d`, then the closure of I will also contain the items `B -> .b` and `B -> .d`.
- The **goto** of a set of items I on a symbol X is the set of items that can be obtained by moving the dot one position to the right in the items of I that have the dot before X .
- For example, if I contains the items `A -> a.Bc` and `B -> .b`, then the goto of I on B will contain the items `A -> aB.c` and `B -> b.`.
- The canonical collection of LR(0) items can be represented by a **DFA** where each state corresponds to a set of items and each transition corresponds to a goto operation on a grammar symbol .
- The DFA can be used to construct the **SLR parsing table** by assigning actions to each state and symbol pair based on the items in the state .
- The actions can be shift, reduce, accept, or error, depending on whether the item has the dot at the end, the beginning, or in the middle of the right side, or if there is no item for the symbol .
- A grammar is **SLR** if its canonical collection of LR(0) items has no conflicts, that is, no state has more than one action for the same symbol .
- A grammar is **LR(0)** if it is SLR and it has no epsilon productions, that is, no productions with an empty right side.



# Constructing SLR Parsing Tables

- SLR stands for Simple LR, which is a type of LR parser with small parse tables and a relatively simple parser generator algorithm.
- SLR parsers can perform bottom-up parsing of input strings using one token of lookahead to resolve conflicts.
- SLR parsers can handle a subset of LR(1) grammars, which are grammars that can be parsed by LR parsers with one token of lookahead.
- SLR parsers use the same LR(0) configurating sets and have the same table structure and parser operation as LR(0) parsers.
- The difference between SLR parsers and LR(0) parsers is that SLR parsers use the FOLLOW sets of the non-terminals to determine when to reduce.
- The steps for constructing the SLR parsing table are:
  - Write the augmented grammar, which is the original grammar with a new start symbol and a new production of the form S' -> S, where S is the original start symbol.
  - Find the LR(0) collection of items, which are sets of productions with a dot indicating the position of the parser in each production. Use the closure and goto functions to generate the items and the transitions between them.
  - Find the FOLLOW sets of the left-hand sides of the productions, which are the sets of terminals that can appear immediately after the non-terminals in the derivations.
  - Define two functions: action and goto, which are the entries of the parsing table. The action function maps a state and a terminal to a shift, reduce, accept, or error action. The goto function maps a state and a non-terminal to a new state or error.
  - Fill the action and goto functions using the following rules:
    - For each item [A -> α.aβ] in state i, where a is a terminal, set action[i, a] to shift j, where j is the state obtained by applying goto to state i and symbol a.
    - For each item [A -> α.] in state i, where A is not the start symbol, set action[i, a] to reduce A -> α for all a in FOLLOW(A).
    - For the item [S' -> S.] in state i, set action[i, $] to accept, where $ is the end-of-input marker.
    - For all other entries, set them to error.



# Constructing Canonical LR Parsing Tables

Canonical LR parsing is a bottom-up parsing technique that can handle a large class of context-free grammars. It is based on the idea of constructing a deterministic finite automaton (DFA) that recognizes the viable prefixes of the grammar. A viable prefix is a prefix of a right sentential form that does not extend past the right end of the rightmost handle of that sentential form.

To construct a canonical LR parsing table, the following steps are required:

- Write an augmented grammar for the given input grammar by adding a new start symbol and a production of the form S' -> S, where S is the original start symbol.
- Construct the canonical collection of LR(1) items for the augmented grammar. An LR(1) item is a pair of a production and a lookahead symbol, denoted as [A -> α.β, a], where A -> αβ is a production, α and β are strings of grammar symbols, and a is a terminal symbol or $. The dot indicates how much of the right-hand side has been seen so far. The lookahead symbol indicates what terminal symbols can follow the production in a right sentential form.
- For each set of LR(1) items in the canonical collection, define the GOTO function, which maps a grammar symbol X to the set of LR(1) items that can be reached by shifting X on the input. The GOTO function can be computed by applying the closure operation to the set of items of the form [A -> α.Xβ, a], where X is the symbol to be shifted.
- For each set of LR(1) items in the canonical collection, define the ACTION function, which maps a terminal symbol a to one of the following actions: shift, reduce, accept, or error. The ACTION function can be computed by applying the following rules:

  - If [A -> α.aβ, b] is in the set and GOTO(I, a) = I', then ACTION(I, a) = shift I'. This means that the parser can shift the terminal symbol a and go to the next set of items I'.
  - If [A -> α., a] is in the set, then ACTION(I, a) = reduce A -> α. This means that the parser can reduce by the production A -> α if the next input symbol is a.
  - If [S' -> S., $] is in the set, then ACTION(I, $) = accept. This means that the parser can accept the input if it reaches the end of the input.
  - If none of the above rules apply, then ACTION(I, a) = error. This means that the parser cannot parse the input.

- The canonical LR parsing table consists of two parts: the ACTION table and the GOTO table. The ACTION table is indexed by the sets of LR(1) items and the terminal symbols, and the GOTO table is indexed by the sets of LR(1) items and the nonterminal symbols. The entries of the tables are the values of the ACTION and GOTO functions, respectively.



# Constructing LALR parsing tables

- LALR stands for Lookahead LR, which is a type of bottom-up parser that can handle a large class of context-free grammars.
- LALR parsing tables are constructed from the canonical collection of LR(1) items, which are sets of items that represent the possible states of the parser and the lookahead symbols that determine the next action.
- An item is a production with a dot (.) indicating the position of the parser in the right-hand side of the production. A lookahead symbol is a terminal that can follow the production in a valid derivation.
- The canonical collection of LR(1) items is obtained by applying two operations: closure and goto. Closure adds items that can be derived from the current items by expanding the nonterminal after the dot. Goto moves the dot one position to the right for a given symbol and returns a new set of items.
- The canonical collection of LR(1) items forms the states of the LALR parser. Each state has a number and a set of items. The transitions between states are labeled by the symbols that cause the goto operation.
- The LALR parsing table has two parts: the action table and the goto table. The action table specifies what the parser should do (shift, reduce, accept, or error) for each state and lookahead symbol. The goto table specifies the next state for each state and nonterminal symbol.
- To construct the LALR parsing table, we follow these steps:
  - For each state and terminal symbol, we check the items in the state and assign an action according to these rules:
    - If there is an item of the form A -> α.aβ, where a is the terminal symbol, we assign a shift action and the state number that is the result of the goto operation on a.
    - If there is an item of the form A -> α., where a is the lookahead symbol, we assign a reduce action and the production number A -> α.
    - If there is an item of the form S' -> S., where a is the end-of-input symbol ($), we assign an accept action.
    - If there is no item that matches any of the above rules, we assign an error action.
  - For each state and nonterminal symbol, we check the result of the goto operation on the symbol and assign the state number to the goto table.
  - If there are multiple actions assigned to the same entry of the action table, we have a conflict, which means the grammar is not LALR(1). We can try to resolve the conflict by using precedence and associativity rules, or by modifying the grammar.
- An example of constructing an LALR parsing table is shown below:

LALR parsing table example



# Using Ambiguous Grammars for the Notes of the Unit 2 - Basic Parsing Techniques in the Subject of Compiler Design

- A grammar is a set of rules that define the syntax of a language, i.e., how the symbols of the language can be combined to form valid sentences.
- A grammar is ambiguous if it can generate more than one parse tree (or leftmost/rightmost derivation) for the same sentence, i.e., if the sentence has more than one possible interpretation according to the grammar rules.
- Ambiguous grammars are undesirable for compiler design because they can lead to confusion and inconsistency in the meaning and behavior of the source code.
- Some examples of ambiguous grammars are:

  - The grammar for arithmetic expressions with + and * operators, without specifying the precedence and associativity of the operators. For example, the sentence `a+b*c` can have two parse trees, one where `+` has higher precedence than `*`, and one where `*` has higher precedence than `+`.
  - The grammar for if-then-else statements, without specifying the association of the else clause with the nearest or the farthest if clause. For example, the sentence `if a then if b then c else d` can have two parse trees, one where the else clause is associated with the inner if, and one where the else clause is associated with the outer if.

- There are different ways to handle ambiguous grammars in compiler design, such as:

  - Eliminating the ambiguity by modifying the grammar rules to make them unambiguous. For example, the grammar for arithmetic expressions can be modified by introducing different non-terminals for different levels of precedence, such as `E -> E+T | T`, `T -> T*F | F`, `F -> (E) | id`. The grammar for if-then-else statements can be modified by introducing a new non-terminal for the optional else clause, such as `Stmt -> if Expr then Stmt OptElse | OtherStmt`, `OptElse -> else Stmt | epsilon`.
  - Resolving the ambiguity by using additional information, such as the precedence and associativity of the operators, or the convention of associating the else clause with the nearest if clause. For example, the LR parser can use these information to resolve the conflicts (shift/reduce or reduce/reduce) in the parsing table of ambiguous grammars.
  - Accepting the ambiguity and generating all possible parse trees for the same sentence, and then choosing the most appropriate one based on some criteria, such as the semantic analysis or the optimization phase of the compiler. This approach is more complex and less efficient than the previous ones.



# An Automatic Parser Generator for the Notes of the Unit 2 - Basic Parsing Techniques in the Subject of Compiler Design

- A parser is a program that analyzes the syntactic structure of a given input according to a given grammar.
- A parser generator is a tool that takes a grammar as input and automatically generates source code that can parse streams of characters using the grammar.
- A parser generator can save time and effort for compiler developers by automating the tedious and error-prone task of writing a parser by hand.
- A parser generator can also ensure that the generated parser is correct and efficient, as well as consistent with the grammar specification.
- Some examples of parser generators are YACC, Bison, ANTLR, JavaCC, etc.
- A parser generator typically consists of two components: a scanner and a parser.
- A scanner is a program that reads the input stream of characters and converts it into a sequence of tokens, which are the basic units of syntax in a language.
- A parser is a program that reads the sequence of tokens and tries to match it against the grammar rules, which define the syntactic structure of the language.
- A parser can be classified into two types: top-down and bottom-up.
- A top-down parser starts from the start symbol of the grammar and tries to derive the input by applying the grammar rules in a top-down manner.
- A bottom-up parser starts from the input and tries to reduce it to the start symbol of the grammar by applying the grammar rules in a bottom-up manner.
- A top-down parser can be further divided into two types: recursive-descent and predictive.
- A recursive-descent parser is a type of top-down parser that uses recursive procedures to implement the grammar rules.
- A predictive parser is a type of top-down parser that uses a lookahead symbol to decide which grammar rule to apply next.
- A bottom-up parser can be further divided into two types: shift-reduce and operator-precedence.
- A shift-reduce parser is a type of bottom-up parser that uses a stack to store the partially parsed input and performs two operations: shift and reduce.
- A shift operation moves the next input symbol onto the top of the stack.
- A reduce operation replaces the topmost symbols on the stack with a nonterminal symbol according to a grammar rule.
- An operator-precedence parser is a type of bottom-up parser that uses a precedence table to resolve the conflicts between different operators in the input.
- A precedence table specifies the relative precedence and associativity of the operators in the language.
- A parser generator can generate different types of parsers depending on the properties of the grammar and the input.
- A grammar can be classified into four types: regular, context-free, context-sensitive, and unrestricted.
- A regular grammar is a type of grammar that can be expressed by regular expressions or finite automata.
- A context-free grammar is a type of grammar that can be expressed by a set of rules of the form A -> B, where A is a nonterminal symbol and B is a string of terminal and nonterminal symbols.
- A context-sensitive grammar is a type of grammar that can be expressed by a set of rules of the form A -> B, where A and B are strings of terminal and nonterminal symbols and B is not shorter than A.
- An unrestricted grammar is a type of grammar that can be expressed by a set of rules of the form A -> B, where A and B are strings of terminal and nonterminal symbols and B can be shorter than A.
- A parser generator can generate a regular parser for a regular grammar, a context-free parser for a context-free grammar, a context-sensitive parser for a context-sensitive grammar, and an unrestricted parser for an unrestricted grammar.
- However, not all grammars are suitable for automatic parser generation, as some grammars may have ambiguities, conflicts, or inefficiencies that make parsing difficult or impossible.
- An ambiguity is a situation where a given input can be derived by more than one parse tree according to the grammar.
- A conflict is a situation where a parser cannot decide which action to take next based on the input and the grammar.
- An inefficiency is a situation where a parser takes too much time or space to parse the input according to the grammar.
- A parser generator can detect and report some of these problems, but it is the responsibility of the compiler developer to design and modify the grammar to make it suitable for automatic parser generation.



# Implementation of LR Parsing Tables

LR parsing tables are a two-dimensional array in which each entry represents an action or a goto entry. LR parsing tables are used by LR parsers, which are bottom-up parsers that can handle a large class of context-free grammars. LR parsers use a stack and an input buffer to parse the given string. The stack contains the states and symbols that have been processed so far, and the input buffer contains the remaining symbols to be processed. The parsing table guides the parser to decide which action to take based on the current state and the next input symbol.

There are three types of LR parsers, which differ in the way they construct the parsing table and resolve conflicts:

- Simple LR (SLR) parser: It is the easiest and most cost-effective to implement, but it fails to make a parsing table for some class of grammars. It uses the follow sets of the non-terminals to determine the reduce actions.
- Canonical LR (CLR) parser: It is the most powerful and accurate parser, but it has a large parsing table that may be impractical to store and use. It uses the lookahead sets of the items to determine the reduce actions.
- Lookahead LR (LALR) parser: It is a compromise between SLR and CLR parsers, which can handle a large class of grammars with a smaller parsing table. It merges the states of the CLR parser that have the same core items, and uses the lookahead sets of the merged states to determine the reduce actions.

The following steps are involved in the implementation of LR parsing tables:

- Construct the augmented grammar by adding a new start symbol and a new production.
- Construct the canonical collection of LR(0) items by applying the closure and goto operations on the augmented grammar.
- Construct the action and goto functions based on the LR(0) items and the grammar symbols. The action function maps a state and a terminal symbol to a shift, reduce, accept, or error action. The goto function maps a state and a non-terminal symbol to a new state.
- Construct the parsing table by filling the entries of the action and goto functions. If there is a conflict in any entry, the grammar is not LR parsable by the chosen parser.
- Use the parsing table to parse the given string by following the algorithm of the LR parser. The algorithm repeatedly performs the action indicated by the current state and the next input symbol, until it accepts or rejects the string.

The following is an example of an LR parsing table for the grammar:

S' -> S

S -> CC

C -> cC | d

The grammar is SLR(1) parsable, but not LR(0) parsable.

| State | c | d | $ | S | C |
| ----- | - | - | - | - | - |
| 0 | s3 | s4 | | 1 | 2 |
| 1 | | | accept | | |
| 2 | s3 | s4 | | | 5 |
| 3 | s3 | s4 | | | 6 |
| 4 | r2 | r2 | r2 | | |
| 5 | r1 | r1 | r1 | | |
| 6 | r3 | r3 | r3 | | |

: https://www.tutorialspoint.com/what-is-implementation-of-lr-parsing-tables
: https://www.tutorialspoint.com/what-is-types-of-lr-parser-in-compiler-design
: https://en.wikipedia.org/wiki/LR_parser
: https://www.geeksforgeeks.org/lr-parser/



## Unit 3 - Syntax-directed Translation

- Syntax-directed translation is a technique for translating the source program into the target program using the syntax and semantic information of the source language.
- Syntax-directed translation can be performed at compile time or at run time, depending on the implementation strategy.
- Syntax-directed translation can be implemented using two methods: syntax-directed definitions and translation schemes.
- Syntax-directed definitions (SDDs) are a way of specifying the translation by attaching semantic rules to the grammar productions of the source language.
- SDDs consist of a context-free grammar and a set of semantic rules, also called attributes, for each grammar symbol.
- Attributes can be classified into two types: synthesized attributes and inherited attributes.
- Synthesized attributes are computed from the attributes of the children of a parse tree node, while inherited attributes are computed from the attributes of the parent and siblings of a parse tree node.
- SDDs can be evaluated by constructing an annotated parse tree, which is a parse tree with attribute values at each node, and then applying the semantic rules in a bottom-up or top-down order.
- Bottom-up evaluation of SDDs can be done using a technique called L-attributed evaluation, which requires that each inherited attribute of a node depends only on the attributes of the nodes to its left and the synthesized attributes of its parent.
- Top-down evaluation of SDDs can be done using a technique called S-attributed evaluation, which requires that each attribute of a node is synthesized and depends only on the attributes of the children of the node.
- Translation schemes are a way of specifying the translation by embedding semantic actions in the grammar productions of the source language.
- Semantic actions are fragments of code that are executed when a production is applied during parsing.
- Semantic actions can perform various tasks, such as generating intermediate code, building symbol tables, checking types, etc.
- Translation schemes can be implemented using a parser generator tool, such as Yacc or Bison, which can generate a parser that executes the semantic actions along with the parsing process.



# Syntax-directed Translation Schemes

- A syntax-directed translation scheme is a notation that combines a context-free grammar with semantic actions .
- Semantic actions are fragments of code that specify how to generate intermediate code or perform other tasks related to the translation.
- Semantic actions can be embedded within the right sides of productions, or associated with grammar symbols .
- The order of execution of semantic actions depends on the order in which they appear in the parse tree.
- Syntax-directed translation schemes can be classified into two types: postfix and prefix.
- Postfix schemes execute semantic actions after parsing the corresponding grammar symbols.
- Prefix schemes execute semantic actions before parsing the corresponding grammar symbols.
- Postfix schemes are more natural and easier to implement than prefix schemes.
- Syntax-directed translation schemes can be used to perform semantic analysis, intermediate code generation, and other tasks related to the translation.
- Syntax-directed translation schemes can be implemented by augmenting a parser with a stack to store attributes and semantic actions.
- Syntax-directed translation schemes can also be converted into attribute grammars, which are a more general and formal notation for specifying syntax-directed translation.



# Implementation of Syntax-Directed Translators

- Syntax-directed translation is a method of compiler implementation where the source language translation is completely driven by the parser.
- A syntax-directed translation scheme is a context-free grammar in which attributes are related to the grammar symbol and semantic actions enclosed within braces ({ }).
- Semantic actions are the subroutines that are called by the parser at the suitable time for translation.
- Semantic actions can perform tasks such as generating intermediate code, building symbol tables, checking types, etc.
- Syntax-directed translation can be divided into two subsets: synthesized and inherited attributes of grammar.
- Synthesized attributes are those that are computed at a node from the attribute values of its children.
- Inherited attributes are those that are computed at a node from the attribute values of its parent and siblings.
- The general approach to syntax-directed translation is to construct a parse tree or syntax tree and compute the values of attributes at the nodes of the tree by visiting them in some order.
- In many cases, translation can be done during parsing without building an explicit tree.
- Syntax-directed translation schemes can be classified into two types: S-attributed and L-attributed.
- S-attributed schemes are those that use only synthesized attributes.
- L-attributed schemes are those that use both synthesized and inherited attributes, but the inherited attributes can be evaluated in a left-to-right traversal of the tree.
- S-attributed schemes can be implemented by a bottom-up parser, such as a shift-reduce parser.
- L-attributed schemes can be implemented by a top-down parser, such as a recursive-descent parser.
- Syntax-directed translation schemes can also be classified into two types: postfix and prefix.
- Postfix schemes are those that have semantic actions after the right-hand side of the production.
- Prefix schemes are those that have semantic actions before the right-hand side of the production.
- Postfix schemes can be implemented by a bottom-up parser, such as a shift-reduce parser.
- Prefix schemes can be implemented by a top-down parser, such as a recursive-descent parser.



# Intermediate Code Generation

Intermediate code generation is a phase in the compiler design that produces an intermediate representation of the source program. The intermediate code is independent of the source language and the target machine, and it can be easily translated into the machine code. The intermediate code can also be used for code optimization and analysis.

The following are some of the advantages of intermediate code generation :

- It simplifies the design of the compiler by separating the analysis and synthesis phases.
- It eliminates the need of a new full compiler for every unique machine by keeping the analysis portion same for all the compilers. The second part of compiler, synthesis, is changed according to the target machine.
- It allows the compiler to perform machine-independent optimizations on the intermediate code, which can improve the quality and efficiency of the generated code.
- It facilitates the portability of the compiler to different machines and platforms, as only the back-end of the compiler needs to be modified for each target machine.

The following are some of the commonly used intermediate code representations:

- Postfix Notation: Also known as reverse Polish notation or suffix notation. The ordinary (infix) way of writing the sum of a and b is with an operator in between, as in a + b. In postfix notation, the operator follows the operands, as in a b +. Postfix notation eliminates the need for parentheses and precedence rules, and it can be easily evaluated using a stack.
- Prefix Notation: Also known as Polish notation or prefix notation. The operator precedes the operands, as in + a b. Prefix notation also eliminates the need for parentheses and precedence rules, and it can be easily evaluated using a stack.
- Three-Address Code: A form of intermediate code that consists of a sequence of instructions, each of which has at most three operands. An operand can be a constant, a variable, a temporary variable, or a label. A label is used to mark the target of a jump instruction. Three-address code can be represented in various ways, such as quadruples, triples, or indirect triples.
- Syntax Trees: A graphical representation of the syntactic structure of the source program. The nodes of the tree are labeled by the grammar symbols, and the leaves are labeled by the tokens. Syntax trees can be used to generate intermediate code by traversing the tree in a suitable order and generating code for each node.
- Directed Acyclic Graphs (DAGs): A simplified version of syntax trees that eliminates the common subexpressions. A DAG has a unique node for each operand and operator, and the edges represent the operands of the operators. DAGs can be used to generate intermediate code by traversing the graph in a suitable order and generating code for each node.

The following is an example of intermediate code generation for the expression a = b * - c + b * - c using three different representations :

- Postfix Notation: b c - * b c - * + a =
- Prefix Notation: = a + * b - c * b - c
- Three-Address Code:

```
t1 = - c
t2 = b * t1
t3 = b * t1
t4 = t2 + t3
a = t4
```

- Syntax Tree:

Syntax Tree

- DAG:

DAG



# Postfix Notation

- Postfix notation is a way of writing arithmetic expressions without using parentheses or brackets.
- In postfix notation, the operator appears after the operands, i.e., the operator between operands is taken out and is attached after operands.
- For example, the infix expression `a * d - (b + c)` can be written in postfix notation as `a d * b c + -`.
- Postfix notation is also known as reverse Polish notation or suffix notation.
- Postfix notation has some advantages over infix notation, such as:
  - It is easier to parse for a machine, as there is no need to check the operator precedence or associativity.
  - It can be used to generate intermediate code in compiler design, as it reflects the order of evaluation of the operands and operators .
  - It can be evaluated using a stack data structure, by pushing the operands onto the stack and popping them when an operator is encountered.
- Postfix notation has some disadvantages over infix notation, such as:
  - It is less familiar and intuitive for human readers, as it does not follow the conventional order of writing arithmetic expressions.
  - It may require more space to write, as it may need more operators than infix notation.
  - It may not be suitable for function calls, as they are usually written in prefix notation, i.e., the operator before the operands.



# Parse Trees and Syntax Trees

- Parse trees and syntax trees are data structures that represent the syntactic structure of a source code in compiler design.
- A parse tree is created by a parser, which is a component of a compiler that processes the source code and checks it for syntactic correctness.
- A syntax tree is an abstract or compact representation of a parse tree, which is also called an abstract syntax tree (AST).
- Parse trees and syntax trees are used for different tasks in compiler design, such as syntax analysis, semantic analysis, intermediate code generation, and code optimization.

## Parse Tree

- A parse tree is a hierarchical representation of the derivation of a grammar rule for a given input string.
- A parse tree shows how the input string is derived from the start symbol of the grammar by applying the production rules in a top-down or bottom-up manner.
- A parse tree has the following properties:
  - The root node is the start symbol of the grammar.
  - The internal nodes are the non-terminal symbols of the grammar.
  - The leaf nodes are the terminal symbols of the grammar.
  - The order of the children of a node corresponds to the order of the symbols in the right-hand side of the production rule.
  - The input string is obtained by concatenating the leaf nodes from left to right.

- For example, consider the following grammar for arithmetic expressions:

  - E -> E + T | T
  - T -> T * F | F
  - F -> (E) | id

- A possible parse tree for the input string id + id * id is:

```
         E
       /   \
      E     T
     / \   / \
    T  +  T   F
   /   / \   |
  F   F  *  id
  |   |
 id  id
```

## Syntax Tree

- A syntax tree is a simplified version of a parse tree that eliminates the unnecessary details and focuses on the essential information.
- A syntax tree is also called an abstract syntax tree (AST) because it abstracts away the syntactic details and captures the semantic meaning of the source code.
- A syntax tree has the following properties:
  - The root node is the main operator or construct of the source code.
  - The internal nodes are the sub-operators or sub-constructs of the source code.
  - The leaf nodes are the operands or identifiers of the source code.
  - The order of the children of a node corresponds to the order of evaluation of the sub-expressions or sub-statements.
  - The input string is obtained by applying the operators or constructs to the leaf nodes from bottom to top.

- For example, the syntax tree for the same input string id + id * id is:

```
     +
   /   \
 id    *
     /   \
   id    id
```

## Comparison

- Parse trees and syntax trees are both useful for compiler design, but they have some differences in their structure and purpose.
- Parse trees are more detailed and faithful to the grammar rules, but they are also more redundant and verbose. Syntax trees are more concise and meaningful, but they are also more abstract and lossy.
- Parse trees are used for syntax analysis, which is the process of checking the syntactic correctness of the source code and building the parse tree. Syntax trees are used for semantic analysis, which is the process of checking the semantic validity of the source code and building the syntax tree.
- Parse trees are also used for intermediate code generation, which is the process of translating the source code into an intermediate representation that is closer to the target machine code. Syntax trees are used for code optimization, which is the process of improving the performance or quality of the intermediate code by applying various techniques.



# Three Address Code for Syntax-directed Translation

- Three address code is a type of intermediate code which is easy to generate and can be easily converted to machine code.
- It makes use of at most three addresses and one operator to represent an expression and the value computed at each instruction is stored in temporary variable generated by compiler.
- A three-address statement is an abstract form of intermediate code. In a compiler, these statements can be implemented as records with fields for the operator and the operands.
- There are three ways to represent a three-address code in compiler design: quadruples, triples, and indirect triples.
- Quadruples: A quadruple is a record structure with four fields: op, arg1, arg2, and result. The op field holds the operator, and arg1 and arg2 fields hold the arguments. The result field holds the place where the result of the operation is stored.
- Triples: A triple is a record structure with three fields: op, arg1, and arg2. The op field holds the operator, and arg1 and arg2 fields hold the arguments. The result of the operation is stored in a temporary variable whose index is the same as the index of the triple.
- Indirect triples: An indirect triple is a record structure with three fields: op, arg1, and arg2. The op field holds the operator, and arg1 and arg2 fields hold the pointers to the arguments. The result of the operation is stored in a temporary variable whose index is the same as the index of the triple.
- Syntax-directed translation is a method of translating a source program into a target program using the syntax and semantic information of the source language.
- It is based on the idea of attaching semantic actions to the productions of a context-free grammar.
- The semantic actions are executed during the parsing process and generate the intermediate code as output.
- Syntax-directed translation can be used for various applications, such as executing arithmetic expressions, converting infix to postfix or prefix expressions, binary to decimal conversion, counting number of reductions, creating a syntax tree, and generating intermediate code.
- Example: The three address code for the expression a + b * c + d using quadruples is:

| op | arg1 | arg2 | result |
|----|------|------|--------|
| *  | b    | c    | t1     |
| +  | a    | t1   | t2     |
| +  | t2   | d    | t3     |

The result of the expression is stored in t3.



# Quadruples and Triples for Syntax-directed Translation

- In compiler design, three address code is an intermediate representation of a source program that uses at most three operands for each instruction.
- Three address code can be implemented as a record with address fields. There are three main representations used: quadruples, triples and indirect triples.
- Quadruples: A quadruple is a structure that consists of four fields: op, arg1, arg2 and result. op denotes the operator, arg1 and arg2 denote the two operands, and result is used to store the result of the expression. For example, the expression `a = b + c * d` can be represented by the following quadruples:

| op | arg1 | arg2 | result |
|----|------|------|--------|
| *  | c    | d    | t1     |
| +  | b    | t1   | t2     |
| =  | t2   |      | a      |

- The advantage of quadruples is that they are easy to rearrange for global optimization, since the result field can be changed without affecting the other fields.
- The disadvantage of quadruples is that they require more space than triples, since they use an extra field for the result.
- Triples: A triple is a structure that consists of three fields: op, arg1 and arg2. op denotes the operator, and arg1 and arg2 denote the two operands. The result of the expression is stored in the same place as one of the operands. For example, the expression `a = b + c * d` can be represented by the following triples:

| op | arg1 | arg2 |
|----|------|------|
| *  | c    | d    |
| +  | b    | (0)  |
| =  | a    | (1)  |

- The advantage of triples is that they require less space than quadruples, since they do not use an extra field for the result.
- The disadvantage of triples is that they are harder to rearrange for global optimization, since changing the result field may affect the other fields.
- Indirect triples: An indirect triple is a combination of triples and a separate list of pointers to the triples. The list of pointers is used to store the result of the expression, and the triples are used to store the operation and the operands. For example, the expression `a = b + c * d` can be represented by the following indirect triples:

| op | arg1 | arg2 |
|----|------|------|
| *  | c    | d    |
| +  | b    | (0)  |
| =  | a    | (1)  |

| 0 | 1 | 2 |
|---|---|---|
| 0 | 1 | 2 |

- The advantage of indirect triples is that they can save some space compared with quadruples if the same temporary value is used more than once, since two or more entries in the pointer list can point to the same triple.
- The disadvantage of indirect triples is that they require an extra level of indirection to access the result of the expression, which may affect the performance.



# Translation of Assignment Statements in Compiler Design

- An assignment statement is a statement that assigns a value to a variable or a data structure.
- In compiler design, translation of assignment statements involves generating intermediate code or target code that can perform the assignment operation efficiently and correctly.
- Translation of assignment statements depends on the type and structure of the expressions involved in the assignment, such as real, integer, array, record, etc.
- Translation of assignment statements also depends on the syntax and semantics of the source language and the target language, such as operator precedence, associativity, type checking, type conversion, etc.
- Translation of assignment statements can be done using syntax-directed translation, which is a technique that interleaves semantic analysis with syntax analysis.
- Syntax-directed translation uses a grammar and a set of semantic rules to guide the translation process. The semantic rules are associated with the grammar symbols or productions, and are evaluated during parsing.
- Syntax-directed translation can be implemented using two methods: syntax-directed definitions and translation schemes.
- Syntax-directed definitions (SDDs) are a notation that attaches attributes and semantic rules to the grammar symbols. Attributes are values associated with the grammar symbols, and semantic rules are functions that compute the attribute values. SDDs can be evaluated using attribute grammars, which are a formalism that defines the dependencies and evaluation order of the attributes and rules.
- Translation schemes are a notation that embeds semantic actions within the grammar productions. Semantic actions are fragments of code that are executed during parsing. Translation schemes can be evaluated using syntax-directed translators, which are parsers that execute the semantic actions along with the parsing algorithm.
- An example of translation of assignment statements using syntax-directed definitions is given below:

```
Grammar: S -> id = E
         E -> E1 + T | T
         T -> T1 * F | F
         F -> (E) | num
         
Attributes: id.addr: the address of the variable id
            id.type: the type of the variable id
            E.addr: the address of the result of the expression E
            E.type: the type of the result of the expression E
            T.addr: the address of the result of the term T
            T.type: the type of the result of the term T
            F.addr: the address of the result of the factor F
            F.type: the type of the result of the factor F
            num.val: the value of the number num
            num.type: the type of the number num
            
Semantic Rules: S -> id = E {gen(id.addr = E.addr); // generate code for assignment}
                E -> E1 + T {E.addr = newtemp(); // allocate a new temporary variable
                             E.type = typecheck(E1.type, T.type); // perform type checking and conversion
                             gen(E.addr = E1.addr + T.addr); // generate code for addition}
                E -> T {E.addr = T.addr; // copy the address of the term
                        E.type = T.type; // copy the type of the term}
                T -> T1 * F {T.addr = newtemp(); // allocate a new temporary variable
                             T.type = typecheck(T1.type, F.type); // perform type checking and conversion
                             gen(T.addr = T1.addr * F.addr); // generate code for multiplication}
                T -> F {T.addr = F.addr; // copy the address of the factor
                        T.type = F.type; // copy the type of the factor}
                F -> (E) {F.addr = E.addr; // copy the address of the expression
                          F.type = E.type; // copy the type of the expression}
                F -> num {F.addr = num.val; // copy the value of the number
                          F.type = num.type; // copy the type of the number}
```

- An example of translation of assignment statements using translation schemes is given below:

```
Grammar: S -> id = E {gen(id.addr = E.addr); // generate code for assignment}
         E -> E1 + T {E.addr = newtemp(); // allocate a new temporary variable
                      gen(E.addr = E1.addr + T.addr); // generate code for addition}
         E -> T {E.addr = T.addr; // copy the address of the term}
         T -> T1 * F {T.addr = newtemp(); // allocate a new temporary variable
                      gen(T.addr = T1.addr * F.addr); // generate code for multiplication}
         T -> F {T.addr = F.addr; // copy the address of the factor}

```




# Boolean expressions for the notes of the Unit 3 - Syntax-directed Translation in the subject of Compiler Design

- Boolean expressions are expressions that evaluate to either true or false values, such as `x > y`, `a && b`, `!c`, etc.
- Boolean expressions are used to control the flow of execution of conditional statements, such as `if-else` statements and `while-do` statements, in programming languages.
- Syntax-directed translation is a technique to translate the source code into an intermediate representation, such as abstract syntax trees, three-address code, or quadruples, by using the syntax and semantics of the source language.
- Syntax-directed translation can be done by embedding semantic actions in the grammar rules of the source language, or by attaching attributes and rules to the grammar symbols and nodes of the parse tree or syntax tree.
- Syntax-directed translation can be done during parsing (syntax-directed definition) or after parsing (syntax-directed translation scheme).
- Syntax-directed translation can be used to type-check, evaluate, and generate code for boolean expressions and control statements, by using attributes such as type, value, true-list, false-list, next-list, etc.
- Syntax-directed translation can also be used to implement short-circuit evaluation, backpatching, and control flow graph generation for boolean expressions and control statements.



# Statements that alter the flow of control

- Statements that alter the flow of control are the statements that change the order of execution of other statements based on some conditions or iterations .
- Examples of statements that alter the flow of control are if, if-else, switch-case, while, do-while, for, break, continue, goto, etc .
- Statements that alter the flow of control are often used to implement conditional or iterative logic in programs .
- Statements that alter the flow of control require the evaluation of boolean expressions, which are expressions that have a true or false value.
- Statements that alter the flow of control can be translated into intermediate code using various techniques, such as syntax-directed translation, three-address code, quadruples, triples, indirect triples, etc .
- Statements that alter the flow of control can also be translated into target code using various techniques, such as backpatching, labels, jumps, conditional jumps, etc .



# Postfix Translation

- Postfix translation is a technique of generating intermediate code for a given source program in a compiler.
- Postfix translation uses a syntax-directed translation scheme (SDT) that has its semantic actions at the end of the production rules in the context-free grammar (CFG) of the source language.
- Postfix translation produces a postfix notation of the source program, which is also known as reverse Polish notation (RPN).
- Postfix notation is a way of writing expressions without using parentheses or precedence rules, where the operator appears after the operands.
- Postfix notation is easier to evaluate by a stack-based machine, as it does not require any backtracking or lookahead.
- Postfix translation can be achieved by factoring the production rules of the CFG to eliminate left recursion and left factoring, and then attaching the semantic actions to the rightmost symbols in the right-hand side (RHS) of the production rules.
- Postfix translation can also be implemented by using a bottom-up parser, such as a shift-reduce parser, that performs the semantic actions whenever a handle is reduced.
- Postfix translation can be illustrated by the following example:

  - Given the source expression: `a * d - (b + c)`
  - The CFG for the expression language is:

    ```
    E -> E - T | T
    T -> T * F | F
    F -> (E) | id
    ```

  - The SDT for postfix translation is:

    ```
    E -> E - T {print('-')} | T
    T -> T * F {print('*')} | F
    F -> (E) | id {print(id.lexeme)}
    ```

  - The postfix notation for the expression is: `a d * b c + -`
  - The derivation of the postfix notation is:

    ```
    E -> E - T {print('-')}
      -> T - T {print('-')}
      -> T * F - T {print('-'); print('*')}
      -> F * F - T {print('-'); print('*')}
      -> id * F - T {print('-'); print('*'); print(id.lexeme)}
      -> a * F - T {print('-'); print('*'); print('a')}
      -> a * F * F - T {print('-'); print('*'); print('*')}
      -> a * (E) * F - T {print('-'); print('*'); print('*')}
      -> a * (E - T) * F - T {print('-'); print('*'); print('*'); print('-')}
      -> a * (T - T) * F - T {print('-'); print('*'); print('*'); print('-')}
      -> a * (T * F - T) * F - T {print('-'); print('*'); print('*'); print('-'); print('*')}
      -> a * (F * F - T) * F - T {print('-'); print('*'); print('*'); print('-'); print('*')}
      -> a * (id * F - T) * F - T {print('-'); print('*'); print('*'); print('-'); print('*'); print(id.lexeme)}
      -> a * (b * F - T) * F - T {print('-'); print('*'); print('*'); print('-'); print('*'); print('b')}
      -> a * (b * id - T) * F - T {print('-'); print('*'); print('*'); print('-'); print('*'); print('b'); print(id.lexeme)}
      -> a * (b * c - T) * F - T {print('-'); print('*'); print('*'); print('-'); print('*'); print('b'); print('c')}
      -> a * (b * c - F) * F - T {print('-'); print('*'); print('*'); print('-'); print('*'); print('b'); print('c')}
      -> a * (b * c - id) * F - T {print('-'); print('*'); print('*'); print('-'); print('*'); print('b'); print('c'); print(id.lexeme)}
      -> a * (b * c - d) * F - T {print('-'); print('*'); print('*'); print('-'); print('*'); print('b'); print('c'); print('d')}
      -> a * (b * c - d) * id - T {print('-'); print('*'); print('*'); print('-'); print('*'); print('b'); print('c'); print('

```




# Translation with a Top Down Parser

- Translation with a top down parser is a technique of syntax-directed translation that involves passing information from the root node to the leaf nodes of the parse tree.
- A top down parser constructs the parse tree from the top (start symbol) to the bottom (input string) by using leftmost derivation.
- A top down parser can be implemented by a recursive descent parser or a predictive parser.
- A top down parser can use attributes and semantic actions to perform translation during parsing.
- Attributes are values associated with the nodes of the parse tree that can be used to store information such as type, value, scope, etc.
- Semantic actions are fragments of code that are executed when a production is applied during parsing. They can be used to perform operations such as code generation, symbol table manipulation, error reporting, etc.
- A top down parser can use two types of attributes: synthesized attributes and inherited attributes.
- Synthesized attributes are attributes that are computed from the attributes of the children nodes. They are passed bottom-up in the parse tree.
- Inherited attributes are attributes that are computed from the attributes of the parent node or the siblings nodes. They are passed top-down in the parse tree.
- A top down parser can use two types of semantic actions: embedded actions and inherited actions.
- Embedded actions are semantic actions that are inserted within the right-hand side of a production. They are executed when the parser recognizes the corresponding symbol in the input.
- Inherited actions are semantic actions that are attached to the left-hand side of a production. They are executed before the parser expands the corresponding non-terminal in the input.
- A top down parser can use a syntax-directed definition (SDD) to specify the attributes and semantic actions for each production in the grammar.
- A syntax-directed definition consists of a context-free grammar and a set of semantic rules that define the attributes and semantic actions for each production.
- A syntax-directed definition can be classified as S-attributed or L-attributed based on the types of attributes and semantic actions it uses.
- An S-attributed definition uses only synthesized attributes and embedded actions. It can be easily implemented by a top down parser by executing the semantic actions in postorder traversal of the parse tree.
- An L-attributed definition uses both synthesized and inherited attributes, but the inherited attributes can be computed from the attributes of the left siblings only. It can also be implemented by a top down parser by executing the semantic actions in preorder traversal of the parse tree.



# More about translation for the notes of the Unit 3 - Syntax-directed Translation in the subject of Compiler Design

- Syntax-directed translation is a method of compiler implementation where the source language translation is completely driven by the parser.
- Syntax-directed translation uses a context-free grammar with attributes and semantic actions to define the translation of the source language into the intermediate code .
- Attributes are values associated with the grammar symbols (terminals or non-terminals) that can be computed from the values of other attributes.
- Semantic actions are subroutines that are executed by the parser at the appropriate time to perform the translation.
- Syntax-directed translation can be divided into two subsets: synthesized and inherited attributes.
  - Synthesized attributes are attributes that are computed at a node from the attribute values of its children.
  - Inherited attributes are attributes that are computed at a node from the attribute values of its parent and siblings.
- Syntax-directed translation can be implemented in two ways: syntax-directed translation schemes and syntax-directed definitions.
  - Syntax-directed translation schemes are context-free grammars with semantic actions embedded within braces ({ }) in the right-hand sides of the productions.
  - Syntax-directed definitions are context-free grammars with attributes and semantic rules associated with each production.
- Syntax-directed translation can be done during parsing without building an explicit parse tree or syntax tree, or after parsing by traversing the parse tree or syntax tree in some order.
  - During parsing, the semantic actions are executed as soon as the corresponding grammar symbols are recognized by the parser.
  - After parsing, the semantic actions are executed by visiting the nodes of the parse tree or syntax tree in a bottom-up or top-down order.



# Array references in arithmetic expressions

- An array reference is an expression that denotes the location of an element of an array in memory  .
- An array reference has an l-value, which is the address of the element, and an r-value, which is the value stored at that address.
- To translate an array reference in a source program, the compiler needs to compute the l-value of the element and generate code to access it  .
- The l-value of an array element depends on the following factors  :
  - The base address of the array, which is the address of the first element.
  - The index of the element, which is the position of the element in the array.
  - The lower bound of the array, which is the index of the first element.
  - The width of the element, which is the number of bytes occupied by each element.
- The general formula for computing the l-value of an array element is  :
  - `l-value = base + (index - lower bound) * width`
- For example, if `A` is an array of integers with a base address of `1000`, a lower bound of `1`, and a width of `4`, then the l-value of `A[5]` is  :
  - `l-value = 1000 + (5 - 1) * 4 = 1016`
- For multi-dimensional arrays, the l-value of an element depends on the order and size of each dimension, and the formula is more complex.
- For example, if `B` is a two-dimensional array of integers with a base address of `2000`, a lower bound of `1` for both dimensions, a width of `4`, and a size of `10` for the first dimension, then the l-value of `B[3][4]` is:
  - `l-value = 2000 + ((3 - 1) * 10 + (4 - 1)) * 4 = 2108`
- To generate code for an array reference, the compiler can use one of the following methods  :
  - Direct addressing: The compiler computes the l-value of the element at compile time and generates code to access it directly. This method is only possible if the base address, the index, and the lower bound are all constants  .
  - Indirect addressing: The compiler generates code to compute the l-value of the element at run time and stores it in a register. Then, the compiler generates code to access the element indirectly through the register  .
  - Indexed addressing: The compiler generates code to compute the offset of the element from the base address at run time and stores it in a register. Then, the compiler generates code to access the element directly by adding the base address and the register  .
- For example, if `C` is an array of integers with a base address of `3000`, a lower bound of `1`, and a width of `4`, and `i` is a variable that holds the index of an element, then the code for `C[i]` can be generated using the following methods  :
  - Direct addressing: If `i` is a constant, say `5`, then the compiler can compute the l-value of `C[5]` as `3016` and generate code like `MOV R0, [3016]` to load the value of `C[5]` into register `R0`  .
  - Indirect addressing: The compiler can generate code like `MOV R1, i` to load the value of `i` into register `R1`, `SUB R1, R1, 1` to subtract the lower bound from `R1`, `MUL R1, R1, 4` to multiply `R1` by the width, `ADD R1, R1, 3000` to



# Unit 3 - Syntax-directed Translation

Syntax-directed translation is a method of compiler implementation where the source language translation is completely driven by the parser. It uses the syntactic structure of the source language to generate intermediate code or perform semantic analysis. It can be done during parsing or after building an explicit parse tree or syntax tree.

Some of the topics covered in this unit are:

- **Syntax-directed definitions**: A syntax-directed definition (SDD) is a way of specifying the values of attributes associated with the grammar symbols in a context-free grammar. It consists of a set of semantic rules or actions attached to each production of the grammar. The semantic rules can be evaluated by visiting the nodes of the parse tree or syntax tree in some order.
- **Synthesized and inherited attributes**: Attributes can be classified into two types: synthesized and inherited. A synthesized attribute at a node is defined only in terms of the attributes of its children. An inherited attribute at a node is defined only in terms of the attributes of its parent and siblings. A grammar that uses only synthesized attributes is called an S-attributed grammar. A grammar that uses both synthesized and inherited attributes is called an L-attributed grammar.
- **Dependency graphs**: A dependency graph is a graphical representation of the dependencies among the attributes of a parse tree or syntax tree. It has a node for each attribute and an edge from A to B if the value of A depends on the value of B. A dependency graph can be used to determine the order of evaluation of the semantic rules in an SDD.
- **Evaluation orders**: The order of evaluation of the semantic rules in an SDD depends on the type of attributes and the traversal of the parse tree or syntax tree. There are two common traversal methods: depth-first and breadth-first. Depth-first traversal visits the children of a node before visiting the node itself. Breadth-first traversal visits all the nodes at a given level before visiting the nodes at the next level. The evaluation order also depends on whether the traversal is done during parsing (bottom-up or top-down) or after parsing (postorder or preorder).
- **Syntax-directed translation schemes**: A syntax-directed translation scheme (SDT) is a way of embedding the semantic rules or actions in the right-hand side of the productions of a grammar. The actions are enclosed in curly braces and are executed whenever the corresponding grammar symbol is recognized by the parser. An SDT can be used to generate intermediate code or perform semantic analysis during parsing. An SDT can be converted to an SDD by attaching the actions to the nodes of the parse tree or syntax tree.



# Declarations and Case Statements

## Declarations
- A declaration in a program is a statement that provides the information about the name and type of data objects to the compiler.
- Declarations can be used to allocate storage for variables, constants, functions, procedures, types, etc.
- Declarations can also specify the scope and visibility of the names, such as global, local, static, extern, etc.
- Declarations can be classified into two categories: explicit and implicit.
  - Explicit declarations are those that are explicitly written by the programmer, such as `int x;` or `float y = 3.14;`.
  - Implicit declarations are those that are inferred by the compiler from the context, such as `x = 5;` or `y++;`.
- The syntax and semantics of declarations depend on the programming language and the compiler design.
- As the sequence of declarations in a procedure or block is examined, the compiler can lay out storage for names local to the procedure.
- The compiler can also generate intermediate code for initializing the declared names, such as assigning values or calling constructors.
- The compiler can also check for errors and warnings in the declarations, such as duplicate names, incompatible types, uninitialized variables, etc.

## Case Statements
- A case statement is a control structure that allows the execution of one of several alternative statements based on the value of an expression.
- A case statement typically consists of a switch expression, a set of case labels, and a set of case statements.
- The syntax and semantics of case statements depend on the programming language and the compiler design.
- A common way to implement case statements is by using a sequence of conditional goto statements, if the number of cases is small.
  - For example, the following C code:

```c
switch (x) {
  case 1: 
    s1;
    break;
  case 2:
    s2;
    break;
  default:
    s3;
}
```
  - Can be translated into the following intermediate code:

```c
if x == 1 goto L1
if x == 2 goto L2
goto L3
L1: s1
goto L4
L2: s2
goto L4
L3: s3
L4:
```
- Another way to implement case statements is by creating a table of pairs, with each pair consisting of a value and a label for the code of the corresponding statement.
  - The compiler generates a loop to compare the value of the expression with each value in the table, and jumps to the appropriate label if a match is found.
  - For example, the following C code:

```c
switch (x) {
  case 1: 
    s1;
    break;
  case 2:
    s2;
    break;
  default:
    s3;
}
```
  - Can be translated into the following intermediate code:

```c
table = [(1, L1), (2, L2)]
i = 0
while i < length(table) do
  if x == table[i].value then goto table[i].label
  i = i + 1
end
goto L3
L1: s1
goto L4
L2: s2
goto L4
L3: s3
L4:
```
- Some programming languages and compilers may also use other techniques to optimize the implementation of case statements, such as binary search, hashing, jump tables, etc.



# Unit 4 - Symbol Tables

- A symbol table is a data structure that stores information about the identifiers (symbols) used in a program, such as variables, constants, functions, etc.
- A symbol table is usually implemented as a hash table, a binary search tree, or a linked list, depending on the trade-offs between insertion, lookup, and deletion operations.
- A symbol table is used by the compiler or interpreter to perform various tasks, such as:
  - Checking the validity and scope of identifiers
  - Resolving name conflicts and aliases
  - Generating intermediate code and machine code
  - Performing type checking and type inference
  - Optimizing code and memory usage
- A symbol table typically contains the following information for each identifier:
  - Name: the lexical representation of the identifier
  - Type: the data type of the identifier, such as int, float, string, etc.
  - Category: the kind of identifier, such as variable, constant, function, class, etc.
  - Scope: the region of the program where the identifier is visible and accessible
  - Address: the memory location or offset where the identifier is stored or allocated
  - Attributes: any additional information or properties of the identifier, such as size, value, parameters, modifiers, etc.
- A symbol table can be organized in different ways, depending on the structure and complexity of the program. Some common ways are:
  - Global symbol table: a single symbol table that contains all the identifiers in the program
  - Local symbol table: a separate symbol table for each function or block that contains the identifiers declared within that scope
  - Nested symbol table: a hierarchical symbol table that reflects the nested structure of the program, such as classes, modules, packages, etc.
  - Chained symbol table: a linked list of symbol tables that represents the current scope and its enclosing scopes
- A symbol table can be constructed and updated in different phases of the compilation or interpretation process, such as:
  - Lexical analysis: the phase where the source code is scanned and tokenized, and the identifiers are extracted and inserted into the symbol table
  - Syntax analysis: the phase where the source code is parsed and checked for syntactic correctness, and the scope and category of the identifiers are determined and recorded in the symbol table
  - Semantic analysis: the phase where the source code is analyzed for semantic validity and meaning, and the type and attributes of the identifiers are inferred and verified in the symbol table
  - Code generation: the phase where the intermediate code or machine code is generated from the source code, and the address and alignment of the identifiers are calculated and assigned in the symbol table
  - Code optimization: the phase where the intermediate code or machine code is improved for performance and efficiency, and the symbol table is used to eliminate redundant or unused identifiers, or to perform constant folding, dead code elimination, etc.



# Data structure for symbol tables

- A symbol table is an important data structure created and maintained by compilers in order to store information about the occurrence of various entities such as variable names, function names, objects, classes, interfaces, etc.  
- A symbol table is used by both the analysis and the synthesis parts of a compiler. 
- A symbol table helps the compiler to perform various tasks, such as:
  - Checking the validity and scope of identifiers
  - Resolving name conflicts and overloading
  - Type checking and type conversion
  - Code generation and optimization
  - Debugging and error reporting
- A symbol table consists of a set of entries, each of which contains information about a symbol, such as:
  - Name: the identifier of the symbol
  - Type: the data type or structure of the symbol
  - Value: the constant or initial value of the symbol
  - Address: the memory location or offset of the symbol
  - Scope: the region of the program where the symbol is visible
  - Attributes: other properties or flags of the symbol
- A symbol table can be implemented using various data structures, such as:
  - Linear list: a simple array or linked list of symbol entries, which can be searched sequentially or using binary search. This is easy to implement but inefficient for large symbol tables.  
  - Hash table: a data structure that maps each symbol name to a unique hash value, which is used as an index to access the symbol entry in an array. This is efficient for searching and inserting symbols, but requires a good hash function to avoid collisions.  
  - Tree: a data structure that organizes symbol entries in a hierarchical or ordered manner, such as a binary search tree, a trie, or a B-tree. This is efficient for searching and inserting symbols, and can also support range queries and sorting.  
- A compiler maintains two types of symbol tables: a global symbol table which can be accessed by all the procedures and scope symbol tables that are created for each scope in the program. To determine the scope of a name, symbol tables are arranged in hierarchical structure as shown in the example below: 

Symbol table hierarchy

- A symbol table can be constructed and updated during various phases of the compiler, such as:
  - Lexical analysis: the scanner identifies the tokens and adds them to the symbol table if they are not already present.
  - Syntax analysis: the parser builds the abstract syntax tree and creates scope symbol tables for each block or function.
  - Semantic analysis: the semantic analyzer checks the type and scope of the symbols and assigns them values and addresses.
  - Intermediate code generation: the code generator uses the symbol table to generate intermediate code for each symbol.
  - Optimization: the optimizer uses the symbol table to perform various optimizations, such as constant folding, dead code elimination, etc.
  - Code generation: the code generator uses the symbol table to generate the final target code for each symbol.



# Representing Scope Information

Scope is the region of the program where a name (such as a variable, function, or type) is visible and can be referenced. Different programming languages have different rules for defining and resolving scopes. For example, some languages use blocks, modules, classes, or functions to create scopes, while others use indentation or keywords.

In compiler design, scope information is important for checking the validity of name references, resolving name conflicts, and allocating memory for variables. To represent scope information, compilers typically use one of the following data structures:

- **Symbol tables**: A symbol table is a data structure that maps names to their attributes, such as type, scope, value, or address. A symbol table can be implemented as a hash table, a tree, a list, or a combination of these. A symbol table can be either global or local, depending on the scope of the names it contains. A global symbol table stores the names that are visible throughout the program, while a local symbol table stores the names that are visible only within a specific scope. A compiler may use a stack of symbol tables to keep track of the current scope and its enclosing scopes. Alternatively, a compiler may use a single symbol table with scope identifiers or nesting levels attached to each name entry.
- **Scope trees**: A scope tree is a data structure that represents the hierarchical structure of scopes in a program. Each node in the tree corresponds to a scope, and each edge corresponds to a nesting relationship. The root of the tree is the global scope, and the leaves are the innermost scopes. A scope tree can be constructed by traversing the abstract syntax tree of the program and creating a new node for each scope-creating construct, such as a function, a class, or a block. A scope tree can be used to determine the visibility and accessibility of names in different scopes, as well as to detect name conflicts and shadowing.
- **Scope lists**: A scope list is a data structure that represents the linear order of scopes in a program. Each element in the list corresponds to a scope, and each scope contains a list of names and their attributes. A scope list can be constructed by traversing the abstract syntax tree of the program and appending a new scope for each scope-creating construct, such as a function, a class, or a block. A scope list can be used to determine the order of name resolution and to implement static scoping or dynamic scoping rules.



# Run-Time Administration

- Run-time administration is the process of managing the memory and other resources required by a program during its execution.
- Run-time administration involves the following tasks:
  - Allocation and deallocation of memory for variables, arrays, records, objects, etc.
  - Mapping of names to memory locations and types
  - Handling of dynamic memory requests and garbage collection
  - Implementation of parameter passing mechanisms and return values
  - Support for exception handling and debugging
  - Maintenance of run-time stack and activation records
  - Management of static and dynamic scoping rules
  - Support for concurrency and communication
- Run-time administration is performed by the run-time support system, which is a package of code and data structures that is generated with the executable program and interacts with the run-time environment of the target machine.
- Run-time administration depends on the source language, the target machine, and the compiler design choices. Different languages and compilers may use different strategies and techniques for run-time administration.



# Implementation of simple stack allocation scheme

- Stack allocation scheme is the simplest run-time storage management technique   for the compiler.
- The storage is organized as a stack, and activation records are pushed and popped as the activation of procedures begin and end, respectively  , thereby permitting recursive procedures.
- An activation record is a data structure that contains information about the execution of a procedure, such as its parameters, local variables, return address, etc.
- The stack allocation scheme has the following advantages:
  - It is simple and efficient to implement, as it only requires a stack pointer and a frame pointer to manage the storage.
  - It supports dynamic scoping, as the most recent binding of a variable can be found at the top of the stack.
  - It supports nested procedures, as the activation record of the enclosing procedure can be accessed through the frame pointer.
- The stack allocation scheme has the following disadvantages :
  - It does not support procedures as first-class values, as the activation record of a procedure may be deallocated when it returns, making it invalid to pass as an argument or return as a result.
  - It does not support dynamic memory allocation, as the size of the stack is fixed at compile time and cannot be changed at run time.
  - It leads to variable-size stack frames, so that both stack and frame pointers need to be managed, which may incur some overhead.
- The stack allocation scheme requires the following components:
  - A stack pointer (SP) that points to the top of the stack, where the next activation record will be pushed.
  - A frame pointer (FP) that points to the base of the current activation record, where the local variables and parameters are stored.
  - A set of predefined routines in the compiler that perform the following operations:
    - PUSH(n): allocate n bytes of storage on the stack by decrementing the SP by n.
    - POP(n): deallocate n bytes of storage from the stack by incrementing the SP by n.
    - CALL(p): push the return address on the stack and transfer control to the procedure p.
    - RETURN: pop the return address from the stack and transfer control back to the caller.
- The stack allocation scheme follows the following steps:
  - When a procedure is called, the compiler generates code to push the actual parameters on the stack, followed by the return address, and then calls the predefined routine CALL(p).
  - When the procedure p begins execution, it allocates space for its local variables on the stack by calling the predefined routine PUSH(n), where n is the size of the local variables. It also saves the old value of the FP on the stack and sets the FP to the current value of the SP.
  - When the procedure p accesses its parameters or local variables, it uses the FP as a base address and adds an offset that is determined by the position of the parameter or variable in the activation record.
  - When the procedure p calls another procedure q, the process is repeated recursively, creating a new activation record on the stack for q.
  - When the procedure p returns, it restores the old value of the FP from the stack and deallocates the space for its local variables by calling the predefined routine POP(n). It then returns the control to the caller by calling the predefined routine RETURN.



# Storage allocation in block structured language

- A block is a program segment that contains data declarations. There can be nested blocks. Uses dynamic memory allocation.
- A block structured language like ALGOL, and PL/I permit adjustable arrays, i.e., of varying length. Therefore, we cannot store irregular size arrays in between activation records. It can allocate the flexible or variable arrays at one corner of the activation record or above the fixed-size data.
- The storage is allocated sequentially in the stack beginning at one end. Storage should be freed in the reverse order of allocation so that a block of storage being released is always at the top of the stack. A program consists of data and procedures.
- The storage is released when the block is exited. If the block is a procedure that is invoked recursively, the previously allocated storage is pushed down upon entry; the latest allocation of storage is popped up in a recursive procedure when each generation terminates.
- The conventional storage allocation scheme for block structured languages requires the allocation of stack space and the building of a display with each procedure call. Several techniques have been proposed for analyzing the call graph of a program that make it possible to eliminate these operations from many call sequences.
- A display is a data structure that contains pointers to the activation records of the most recent invocations of each block. It is used to access non-local variables in a block structured language.
- Conventionally, compilers for block structured languages with potentially recursive procedures generate code to allocate stack storage for local variables on each procedure call. This paper reviews previous schemes for reducing storage allocation overhead and proposes a new scheme.
- The new scheme is based on the observation that many procedures do not access all their local variables on every call. Therefore, it is possible to allocate storage for only those variables that are actually used, and to defer the allocation of the rest until they are needed.



# Error Detection and Recovery in Compiler Design

## Introduction

- Error detection and recovery are important aspects of compiler design, as they ensure the correctness and robustness of the compiler.
- Errors can occur at any stage of the compilation process, such as lexical, syntactic, semantic, or code generation.
- Errors can be classified into two types: fatal errors and non-fatal errors.
  - Fatal errors are those that prevent the compiler from continuing the compilation process, such as missing source file, invalid character, or memory overflow.
  - Non-fatal errors are those that can be detected and reported by the compiler, but do not stop the compilation process, such as spelling mistakes, type mismatch, or undeclared variables.
- The compiler should be able to detect and report as many errors as possible, and recover from them gracefully, without affecting the subsequent compilation of the program.
- The compiler should also avoid reporting spurious errors, which are false or misleading errors caused by previous errors.

## Error Detection Techniques

- Error detection techniques are methods used by the compiler to identify and locate errors in the source program.
- Different types of errors require different techniques for detection, such as:
  - Lexical errors: These are errors in the formation of tokens, such as invalid identifiers, keywords, or literals. They can be detected by the lexical analyzer using regular expressions or finite automata.
  - Syntactic errors: These are errors in the structure of the program, such as missing or extra parentheses, semicolons, or braces. They can be detected by the parser using grammar rules or parsing algorithms.
  - Semantic errors: These are errors in the meaning of the program, such as type mismatch, undeclared variables, or invalid operations. They can be detected by the semantic analyzer using symbol tables, type checking, or scope rules.
  - Code generation errors: These are errors in the translation of the intermediate code to the target code, such as invalid instructions, registers, or addresses. They can be detected by the code generator using code optimization techniques or target machine specifications.

## Error Recovery Techniques

- Error recovery techniques are methods used by the compiler to handle and correct errors in the source program, and resume the compilation process.
- Different types of errors require different techniques for recovery, such as:
  - Panic mode: This is the simplest and most common technique, which involves discarding input symbols until a synchronizing token is found, such as a semicolon, a keyword, or an end-of-file marker. This technique is used by most parsers, but it may skip a large portion of the input and generate many spurious errors.
  - Phase level recovery: This technique involves isolating the errors within a phase of the compilation process, such as lexical, syntactic, or semantic, and continuing the compilation with the next phase. This technique may require the use of dummy tokens, default values, or assumptions to fill the gaps caused by the errors.
  - Error productions: This technique involves modifying the grammar rules to include error symbols, which can be used to handle common or expected errors. This technique can provide more meaningful error messages and better recovery, but it may also complicate the grammar and the parser.
  - Global correction: This technique involves finding the minimum number of changes required to correct the errors in the input, such as insertion, deletion, or substitution of symbols. This technique can provide the best recovery, but it is also the most complex and expensive, as it may require backtracking, lookahead, or dynamic programming algorithms.
  - Symbol table: This technique involves updating the symbol table with the information about the errors, such as the location, type, or severity of the errors. This technique can help in avoiding duplicate or spurious errors, and in generating more accurate error messages and code.



Hello, I am Sydney, your AI assistant. I can help you with your topic. Here are some notes on lexical phase errors for the unit 4 - symbol tables in the subject of compiler design.

# Lexical Phase Errors

- Lexical phase errors are errors that occur during the lexical analysis phase of the compiler, which is responsible for scanning the source code and generating tokens.
- A token is a sequence of characters that matches the pattern of a valid lexical unit, such as a keyword, an identifier, a constant, an operator, or a delimiter.
- A lexical error is a sequence of characters that does not match the pattern of any token. For example, an invalid identifier, a missing delimiter, or an illegal character.
- Lexical errors can be detected and reported by the lexical analyzer, which is also called a lexer or a scanner. The lexer can use different methods to handle lexical errors, such as:

  - Ignoring the error and continuing the scanning process. This may lead to more errors or incorrect tokens.
  - Skipping the error and moving to the next character or token. This may cause some tokens to be missed or misplaced.
  - Replacing the error with a valid token or a special error token. This may help the parser to recover from the error and continue the syntax analysis phase.
  - Reporting the error and aborting the compilation process. This may prevent further errors or confusion.

- Some examples of lexical errors and their possible handling methods are:

  - Exceeding the length of an identifier or a numeric constant. For example, in C++, the maximum length of an identifier is 31 characters and the maximum value of a signed integer is 2,147,483,647. If the lexer encounters an identifier or a constant that exceeds these limits, it may report an error and skip the token, or truncate the token and generate a warning.
  - Using an undefined or reserved keyword. For example, in C++, the keyword `auto` is reserved for future use and cannot be used as an identifier. If the lexer encounters the keyword `auto` as an identifier, it may report an error and skip the token, or replace the token with a special error token.
  - Missing a delimiter or a comment terminator. For example, in C++, a string literal must be enclosed by double quotes and a comment must be terminated by `*/`. If the lexer encounters a missing delimiter or a comment terminator, it may report an error and skip the token, or insert the missing delimiter or terminator and generate a warning.
  - Using an illegal or non-ASCII character. For example, in C++, the source code must use only ASCII characters and cannot contain any special symbols or foreign characters. If the lexer encounters an illegal or non-ASCII character, it may report an error and skip the character, or replace the character with a valid character or a special error token.



# Syntactic Phase Errors

Syntactic phase errors are errors that occur during the syntax analysis phase of the compiler. Syntax analysis is the process of checking whether the input program conforms to the grammar rules of the source language. The syntax analyzer or parser uses a grammar specification to generate a parse tree or an abstract syntax tree for the input program. If the input program does not match the grammar rules, the parser reports a syntactic error.

Some of the common types of syntactic errors are:

- **Structural errors**: These are errors that violate the basic structure of the source language, such as missing operators, parentheses, semicolons, braces, etc. For example, `a = b + c` is a valid expression, but `a = b +` is not, because it is missing an operand after the `+` operator.
- **Mismatched errors**: These are errors that occur when the expected token or symbol does not match the actual token or symbol in the input. For example, `if (x > y) then z = x;` is a valid statement, but `if (x > y) then z = x)` is not, because it has a mismatched parenthesis at the end.
- **Undefined errors**: These are errors that occur when the parser encounters an undefined symbol or identifier in the input. For example, `x = y + z;` is a valid statement, but `x = y + w;` is not, if `w` is not declared or defined anywhere in the program.

The parser should be able to detect and report syntactic errors as soon as possible, and also recover from them and continue to parse the rest of the input. There are different strategies for error recovery, such as:

- **Panic mode recovery**: In this method, the parser discards the input tokens one by one until it finds a synchronizing token, which is a delimiter or a keyword that marks the end of a statement or a block. For example, if the parser encounters an error in an expression, it can skip the tokens until it finds a semicolon or a closing brace, and then resume parsing from the next statement.
- **Phrase level recovery**: In this method, the parser tries to replace or insert a token or a phrase that can make the input syntactically correct. For example, if the parser encounters an error in an expression, it can insert a missing operator or operand, or replace an invalid token with a valid one, and then continue parsing the expression.
- **Error productions recovery**: In this method, the parser uses special error-handling rules in the grammar that can handle common syntactic errors. For example, the parser can have a rule like `expr -> expr + error` that can match an expression with a missing operand after the `+` operator, and then report and recover from the error.

The parser should also provide informative and helpful error messages to the user, indicating the location, type, and possible cause of the error. The parser should also avoid reporting spurious or cascading errors, which are errors that are caused by a previous error and not by the actual input. For example, if the parser encounters a missing semicolon at the end of a statement, it should not report an error for the next statement, which may be syntactically correct.



# Semantic Errors

Semantic errors are errors that arise when a statement used in a program is not meaningful, that is, it does not correspond to the set of rules (semantics) for that language being used. Semantic errors are detected by the semantic analyzer, which is a component of the compiler that checks the meaning and validity of the source code.

Some of the semantic errors are:

- **Type mismatch**: This occurs when the data types of two operands are not compatible, or when an expression is assigned to a variable of a different type. For example, `int x = "hello";` is a type mismatch error, because a string cannot be assigned to an integer variable. The compiler may automatically perform type conversion in some cases, but this may lead to unexpected results or loss of precision .
- **Undeclared variables**: This occurs when a variable is used without being declared first. For example, `x = 10;` is an undeclared variable error, if `x` has not been declared before. The compiler may report this error as a syntax error, or as a semantic error, depending on the language and the compiler  .
- **Reserved identifier misuse**: This occurs when a variable or a function is given the same name as a reserved keyword or a predefined identifier in the language. For example, `int main = 0;` is a reserved identifier misuse error, because `main` is a reserved keyword in C and C++. The compiler may report this error as a syntax error, or as a semantic error, depending on the language and the compiler .

Semantic errors are different from syntax errors, which are errors that violate the rules of the grammar of the language. Syntax errors are detected by the syntactic analyzer, which is another component of the compiler that checks the structure and form of the source code. For example, `int x = 10;` is a syntax error, if the semicolon is missing at the end of the statement. Syntax errors prevent the compiler from generating the executable code, whereas semantic errors may allow the compiler to generate the code, but the code may not behave as intended by the programmer.



## Unit 5 - Code Generation

- Code generation is the process of translating an intermediate representation of a source program into a target program that can be executed by a machine.
- Code generation can be divided into two phases: instruction selection and instruction scheduling.
- Instruction selection is the task of choosing the appropriate instructions from the target instruction set to implement the operations in the intermediate representation.
- Instruction scheduling is the task of ordering the instructions to optimize the performance of the target program, taking into account the dependencies, latencies, and resource constraints of the target machine.
- Code generation can be performed by different methods, such as template-based, peephole, and graph-based methods.
- Template-based methods use predefined patterns of instructions to match the operations in the intermediate representation and generate the corresponding target code.
- Peephole methods apply local optimizations to the generated code by examining a small window of instructions and replacing them with more efficient ones.
- Graph-based methods use data structures such as trees or graphs to represent the intermediate representation and the target instruction set, and apply algorithms such as pattern matching, tree covering, or graph coloring to generate the optimal code.



# Design Issues for Code Generation in Compiler Design

Code generation is the final phase of the compiler model, where the intermediate representation of the source program is translated into the target program. Code generation involves various design issues that affect the quality and efficiency of the generated code. Some of the main design issues are:

- **Input to the code generator**: The input to the code generator is the intermediate code generated by the front end, along with the information in the symbol table that determines the run-time addresses of the data objects denoted by the names in the intermediate representation. The intermediate code can be in various forms, such as abstract syntax trees, three-address code, or stack-machine code. The choice of the intermediate code affects the complexity and effectiveness of the code generator.
- **Target program**: The target program is the output of the code generator, which is an equivalent program in the target language. The target language can be a low-level language, such as assembly language or machine code, or a high-level language, such as C or Java. The choice of the target language affects the portability and performance of the generated code.
- **Memory management**: The code generator must allocate memory for the data objects used in the source program, such as variables, constants, arrays, records, etc. The memory allocation can be static or dynamic, depending on the scope and lifetime of the data objects. The code generator must also deal with the alignment and padding issues that arise due to the different sizes and types of the data objects. The memory management affects the space and time efficiency of the generated code.
- **Instruction selection**: The code generator must select the appropriate instructions from the target instruction set to implement the operations and operands in the intermediate code. The instruction selection can be done by using simple patterns, such as one-to-one mapping, or by using more complex techniques, such as tree pattern matching, peephole optimization, or macro expansion. The instruction selection affects the quality and size of the generated code.
- **Register allocation**: The code generator must assign the temporary values and variables in the intermediate code to the registers in the target machine. The register allocation can be done by using simple heuristics, such as first-fit or next-fit, or by using more sophisticated algorithms, such as graph coloring, linear scan, or iterative coalescing. The register allocation affects the speed and performance of the generated code.
- **Evaluation order**: The code generator must determine the order in which the expressions and statements in the intermediate code are evaluated. The evaluation order can be influenced by the precedence and associativity of the operators, the side effects of the operands, the dependencies among the expressions, and the availability of the registers. The evaluation order affects the correctness and efficiency of the generated code.



# The Target Language for the notes of the Unit 5 - Code Generation in the subject of Compiler Design

- The target language is the final output of the compiler that is executable by the machine or a virtual machine.
- The target language can be machine language, assembly language, or an intermediate language that can be interpreted or compiled further.
- The target language depends on the architecture and instruction set of the target machine or platform.
- The target language should be efficient, compact, and compatible with the source language semantics and features.
- The target language should also support the optimization techniques applied by the compiler to improve the performance and quality of the code.
- The target language can be generated by different methods, such as direct translation, syntax-directed translation, or intermediate code generation and translation.
- The target language can be represented by different data structures, such as linear code, basic blocks, control flow graphs, or trees.
- The target language can be influenced by different factors, such as the memory layout, the register allocation, the instruction selection, and the code generation algorithm.



# Addresses in the Target Code

- Addresses in the target code are the locations where the values of the variables, constants, temporaries, and parameters are stored in the memory or registers of the target machine.
- The code generator is responsible for assigning addresses to the operands of the three-address code and generating the target code accordingly.
- The code generator can use different strategies for address allocation, such as static allocation, stack allocation, register allocation, and dynamic allocation.
- Static allocation: The code generator assigns a fixed memory location to each variable, constant, or temporary at compile time. This strategy is simple and efficient, but it does not support recursion or dynamic data structures.
- Stack allocation: The code generator allocates memory for each variable, constant, or temporary in a stack frame or activation record when a procedure or function is called. The stack frame is deallocated when the procedure or function returns. This strategy supports recursion and local variables, but it may incur runtime overhead and limit the number of available registers.
- Register allocation: The code generator assigns a register to each variable, constant, or temporary that is frequently used or live in a basic block. This strategy can improve the performance of the target code by reducing the memory access, but it may require spilling and reloading of registers when there are not enough registers available.
- Dynamic allocation: The code generator allocates memory for each variable, constant, or temporary at runtime using a heap or a garbage collector. This strategy supports dynamic data structures and polymorphism, but it may incur high runtime overhead and memory fragmentation.

- The code generator can use different techniques for address computation, such as direct addressing, indirect addressing, indexed addressing, relative addressing, and base addressing.
- Direct addressing: The code generator uses the address of the operand as the operand itself. For example, x:= y + z can be translated to LD R1, y; ADD R1, R1, z; ST x, R1, where y, z, and x are the addresses of the operands.
- Indirect addressing: The code generator uses the address of a pointer as the operand, and dereferences the pointer to access the value. For example, x:= *y + *z can be translated to LD R1, y; LD R1, (R1); LD R2, z; LD R2, (R2); ADD R1, R1, R2; ST x, R1, where y and z are the addresses of the pointers.
- Indexed addressing: The code generator uses the address of an array element as the operand, and adds an offset to the base address of the array to access the element. For example, x:= A[i] + B[j] can be translated to LD R1, i; MUL R1, R1, 4; ADD R1, R1, A; LD R1, (R1); LD R2, j; MUL R2, R2, 4; ADD R2, R2, B; LD R2, (R2); ADD R1, R1, R2; ST x, R1, where A and B are the base addresses of the arrays, and 4 is the size of each element.
- Relative addressing: The code generator uses the address of a local variable or parameter as the operand, and adds an offset to the stack pointer or the frame pointer to access the variable or parameter. For example, x:= y + z can be translated to LD R1, FP-8; ADD R1, R1, FP-12; ST FP-4, R1, where FP is the frame pointer, and -8, -12, and -4 are the offsets of y, z, and x in the stack frame.
- Base addressing: The code generator uses the address of a global variable or a static variable as the operand, and adds an offset to a base register to access the variable. For example, x:= y + z can be translated to LD R1, BR+100; ADD R1, R1, BR+200; ST BR+300, R1, where BR is the base register, and 100, 200, and 300 are the offsets of y, z, and x in the data segment.



# Basic Blocks and Flow Graphs

- A **basic block** is a set of statements that always executes in a sequence one after the other, without any branches or jumps  .
- A basic block has a single entry point and a single exit point. It means the flow of control enters at the beginning and leaves at the end of the block .
- A basic block can be identified by finding the **leaders** of the statements. A leader is the first statement of a basic block.
- The leaders can be found by applying the following rules:
  - The first statement is a leader.
  - Any statement that is the target of a conditional or unconditional jump is a leader.
  - Any statement that immediately follows a jump statement is a leader.
- A **flow graph** is a directed graph that represents the flow of control between basic blocks  .
- A flow graph has the following properties  :
  - Each node in the graph corresponds to a basic block.
  - There is an edge from node X to node Y if the flow of control can pass from the end of block X to the beginning of block Y.
  - The node with no predecessors is the **entry node** of the graph. It corresponds to the first basic block of the program.
  - The node with no successors is the **exit node** of the graph. It corresponds to the last basic block of the program.
- A flow graph is useful for code optimization and code generation, as it shows the dependencies and the loops in the program .
- An example of a flow graph is shown below:

Flow graph example



# Optimization of Basic Blocks

- Optimization is the process of transforming a program that improves the code by consuming fewer resources and delivering high speed.
- Optimization can be applied to the basic blocks after the intermediate code generation phase of the compiler.
- A basic block is a sequence of consecutive statements in which the flow of control enters at the beginning and leaves at the end without halt or possibility of branching.
- There are two types of basic block optimizations:
  - Structure preserving transformations: These are the transformations that do not change the structure of the basic block, but only replace some expressions by equivalent ones. For example, constant folding, constant propagation, strength reduction, etc.
  - Algebraic transformations: These are the transformations that change the structure of the basic block by eliminating some expressions or statements. For example, common subexpression elimination, dead code elimination, copy propagation, etc.
- To apply an optimization technique to a basic block, a directed acyclic graph (DAG) can be used as a representation of the three-address code that is generated as the result of an intermediate code generation.
- A DAG is a data structure that consists of nodes and edges, where each node represents an operation or a variable, and each edge represents a dependency or a flow of data.
- A DAG facilitates the transformation of basic blocks by identifying the common subexpressions, eliminating the redundant computations, and generating an optimal order of evaluation.
- The steps to construct a DAG for a basic block are:
  - Create a node for each statement in the basic block.
  - For each node, check if its operands are already present in the DAG. If yes, use the existing nodes as the children of the node. If no, create new nodes for the operands and make them the children of the node.
  - For each node, check if its operation and children are identical to any existing node in the DAG. If yes, delete the node and replace all its occurrences by the existing node. If no, add the node to the DAG.
  - For each node that has no parent, mark it as a root of the DAG.
- The steps to generate an optimal code from a DAG are:
  - Traverse the DAG in a postorder fashion, starting from the roots and visiting the children before the parent.
  - For each node, generate a three-address code by assigning a temporary variable to the node and using its operation and children as the operands.
  - If the node is a leaf and represents a variable, copy its value to the temporary variable.
  - If the node is a root and represents a variable, copy the temporary variable to the variable.
  - Eliminate any redundant assignments or copies.



# Code Generator for the notes of the Unit 5 - Code Generation in the subject of Compiler Design

- Code generation is the final phase of compilation that converts the intermediate representation of source code into a form that can be readily executed by the target system .
- The code generator is responsible for mapping the intermediate code to the target code, which may be machine code or assembly code.
- The code generator generally performs three tasks:
  - Instruction selection: choosing the appropriate instructions from the target instruction set to implement the intermediate code operations.
  - Register allocation: assigning the intermediate code operands to the available registers of the target machine.
  - Instruction scheduling: ordering the instructions to improve the performance and utilization of the target machine resources.
- The code generator may also perform some optimizations on the target code, such as peephole optimization, instruction combining, and loop unrolling .
- The code generator may use different strategies for register allocation and optimization, such as:
  - Local register allocation: allocating registers within a basic block, which is a sequence of instructions with no branches or labels.
  - Global register allocation: allocating registers across basic blocks, which may require graph coloring or linear scan algorithms.
  - Register optimization: reducing the number of register spills and reloads, which are memory accesses to store or load registers.



# Code optimization for the notes of the Unit 5 - Code Generation in the subject of Compiler Design

Code optimization is the process of improving the quality and efficiency of the generated code by applying various techniques and transformations. Code optimization can be performed at different levels of the compiler, such as source code, intermediate code, or object code. Code optimization can be machine-independent or machine-dependent, depending on whether the techniques are applicable to any target machine or specific to a particular architecture.

Some of the common goals of code optimization are:

- Reducing the execution time of the code
- Reducing the memory usage of the code
- Reducing the power consumption of the code
- Improving the readability and maintainability of the code
- Enhancing the portability and compatibility of the code

Some of the common techniques of code optimization are:

- Compile-time evaluation: This technique evaluates constant expressions and variables at compile time and replaces them with their values, thus saving run-time computation. For example, `2 * (22.0/7.0) * r` can be evaluated as `44.0/7.0 * r` at compile time.
- Constant propagation: This technique propagates the values of constant variables to their uses and replaces them with their values, thus eliminating unnecessary assignments and references. For example, `x = 12.4; y = x / 2.3;` can be replaced by `y = 12.4 / 2.3;`.
- Constant folding: This technique evaluates constant expressions and replaces them with their values, thus reducing the number of operations. For example, `x = 2 + 3 * 4;` can be replaced by `x = 14;`.
- Common subexpression elimination: This technique identifies and eliminates redundant computations of the same subexpression, thus saving run-time computation. For example, `x = a + b * c; y = a + b * c + d;` can be replaced by `t = a + b * c; x = t; y = t + d;`.
- Dead code elimination: This technique removes unreachable or unnecessary code that does not affect the output of the program, thus saving memory and execution time. For example, `if (false) { x = 10; }` can be removed as the statement is never executed.
- Code movement: This technique moves invariant code out of loops or conditional blocks, thus reducing the number of executions. For example, `for (i = 0; i < n; i++) { x = a + b; y = x * i; }` can be replaced by `x = a + b; for (i = 0; i < n; i++) { y = x * i; }`.
- Strength reduction: This technique replaces expensive operations with cheaper ones, such as multiplication with addition, division with shift, etc. For example, `x = y * 8;` can be replaced by `x = y << 3;`.
- Loop optimization: This technique applies various transformations to loops, such as loop unrolling, loop fusion, loop inversion, loop invariant code motion, loop induction variable elimination, etc. to improve the performance of loops.
- Function inlining: This technique replaces a function call with the body of the function, thus eliminating the overhead of function call and return. For example, `int square(int x) { return x * x; } y = square(z);` can be replaced by `y = z * z;`.
- Tail recursion elimination: This technique replaces a recursive function call at the end of a function with a loop, thus saving stack space and function call overhead. For example, `int factorial(int n) { if (n == 0) return 1; else return n * factorial(n-1); }` can be replaced by `int factorial(int n) { int result = 1; while (n > 0) { result = result * n; n = n - 1; } return result; }`.
- Machine-dependent optimization: This technique applies optimizations that are specific to the target machine architecture, such as instruction selection, instruction scheduling, register allocation, peephole optimization, etc. to improve the code quality and efficiency.

These are some of the code optimization techniques that can be used in compiler design. However, there are many more techniques that can be applied depending on the context and the



# Machine-Independent Optimizations

Machine-independent optimizations are techniques that improve the quality of the intermediate code generated by the compiler, without considering the specific features of the target machine. The main goal of machine-independent optimizations is to reduce the execution time and/or the code size of the target program.

Some of the common machine-independent optimizations are:

- **Common subexpression elimination**: This technique avoids recomputing the same expression multiple times, by replacing it with a temporary variable that holds its value. For example, `a = b + c; d = b + c;` can be optimized as `t = b + c; a = t; d = t;`.
- **Constant folding**: This technique evaluates constant expressions at compile time, and replaces them with their values. For example, `a = 2 * 3;` can be optimized as `a = 6;`.
- **Constant propagation**: This technique replaces the use of a variable that has a constant value with the constant itself. For example, `a = 6; b = a + 1;` can be optimized as `a = 6; b = 6 + 1;`.
- **Dead code elimination**: This technique removes statements or blocks of code that have no effect on the program execution. For example, `a = 1; a = 2;` can be optimized as `a = 2;`.
- **Copy propagation**: This technique replaces the use of a variable that has been assigned the value of another variable with the source variable itself. For example, `a = b; c = a + 1;` can be optimized as `a = b; c = b + 1;`.
- **Algebraic simplification**: This technique applies algebraic rules to simplify expressions and eliminate unnecessary operations. For example, `a = b * 1;` can be optimized as `a = b;`.
- **Strength reduction**: This technique replaces expensive operations with cheaper ones that have the same effect. For example, `a = b * 2;` can be optimized as `a = b + b;`.
- **Loop invariant code motion**: This technique moves statements or expressions that do not depend on the loop variable outside the loop, to avoid repeated computation. For example, `for (i = 0; i < n; i++) { a = b + c; d = a * i; }` can be optimized as `a = b + c; for (i = 0; i < n; i++) { d = a * i; }`.
- **Induction variable elimination**: This technique eliminates redundant variables that are used to control the loop iteration, by using a single variable instead. For example, `for (i = 0, j = 0; i < n; i++, j = j + 2) { a[i] = b[j]; }` can be optimized as `for (i = 0; i < n; i++) { a[i] = b[2 * i]; }`.
- **Loop unrolling**: This technique replicates the loop body multiple times, to reduce the overhead of loop control and increase instruction-level parallelism. For example, `for (i = 0; i < n; i++) { a[i] = b[i] + c[i]; }` can be optimized as `for (i = 0; i < n; i = i + 4) { a[i] = b[i] + c[i]; a[i + 1] = b[i + 1] + c[i + 1]; a[i + 2] = b[i + 2] + c[i + 2]; a[i + 3] = b[i + 3] + c[i + 3]; }`.
- **Loop fusion**: This technique combines two or more loops that iterate over the same range and have no data dependence, into a single loop, to reduce the loop overhead and improve cache locality. For example, `for (i = 0; i < n; i++) { a[i] = b[i] + c[i]; } for (i = 0; i < n; i++) { d[i] = e[i] * f[i]; }` can be optimized as `for (i = 0; i < n; i++) { a[i] = b[i] + c[i]; d[i] = e[i] * f[i]; }`.
- **Loop interchange**: This technique changes the order of nested loops, to improve the spatial locality of memory



# Loop optimization

Loop optimization is the process of increasing execution speed and reducing the overheads associated with loops. It plays an important role in improving cache performance and making effective use of parallel processing capabilities. Most execution time of a scientific program is spent on loops.

Loop optimization can be viewed as the application of a sequence of specific loop transformations to the source code or intermediate representation, with each transformation having an associated test for legality.

Some common loop transformations are:

- **Loop invariant code motion**: This transformation moves computations that are independent of the loop iteration outside of the loop, thus avoiding redundant calculations. For example, if `x` is not modified inside the loop, then `x*x` can be computed once before the loop and reused inside the loop.
- **Loop unrolling**: This transformation replicates the loop body multiple times, thus reducing the number of loop iterations and the loop control overhead. For example, a loop that iterates four times can be unrolled into a single iteration with four copies of the loop body. This can also expose more opportunities for instruction-level parallelism.
- **Loop fusion**: This transformation combines two or more loops that have the same iteration space and do not depend on each other into a single loop, thus reducing the loop overhead and improving data locality. For example, two loops that iterate over the same array and perform different computations can be fused into one loop that performs both computations.
- **Loop fission**: This transformation splits a loop into two or more loops that have the same iteration space but operate on different data, thus improving data locality and cache performance. For example, a loop that iterates over a matrix and performs two different computations on each element can be fissioned into two loops that perform one computation each.
- **Loop interchange**: This transformation changes the order of nested loops to improve data locality and cache performance. For example, a loop that iterates over a row-major matrix in column-major order can be interchanged to iterate in row-major order, thus accessing the matrix elements in a sequential manner.
- **Loop tiling**: This transformation divides a loop iteration space into smaller blocks or tiles, and then iterates over the tiles in an outer loop and over the elements in each tile in an inner loop. This can improve data locality and cache performance by reusing the data in each tile. For example, a loop that iterates over a large matrix can be tiled into smaller submatrices, and then iterated over the submatrices in an outer loop and over the elements in each submatrix in an inner loop.
- **Loop distribution**: This transformation distributes a loop that performs multiple computations into several loops that perform one computation each, thus exposing more parallelism and reducing loop-carried dependencies. For example, a loop that updates two arrays in each iteration can be distributed into two loops that update one array each.
- **Loop peeling**: This transformation removes one or more iterations from the beginning or the end of a loop and executes them separately, thus simplifying the loop condition or eliminating some loop dependencies. For example, a loop that has a special case for the first iteration can be peeled by executing the first iteration before the loop and then iterating over the remaining iterations in the loop.
- **Loop reversal**: This transformation changes the direction of a loop from increasing to decreasing or vice versa, thus eliminating some loop dependencies or improving data locality. For example, a loop that iterates over an array from the end to the beginning can be reversed to iterate from the beginning to the end, thus accessing the array elements in a sequential manner.
- **Loop skewing**: This transformation shifts the iteration space of a nested loop by a constant factor, thus eliminating or reducing loop-carried dependencies or improving data locality. For example, a loop that iterates over a triangular matrix can be skewed by shifting the inner loop by the outer loop index, thus making the iteration space rectangular and parallelizable.

These loop transformations can be applied individually or in combination to optimize loops for different performance goals. However, they also have some limitations and trade-offs, such as increasing code size, memory usage, or complexity. Therefore, the compiler must carefully analyze the loop structure, dependencies, and data access patterns to determine the legality and profitability of each transformation.



# DAG representation of basic blocks

- A **basic block** is a sequence of statements that has a single entry point and a single exit point.
- A **directed acyclic graph (DAG)** is a graph that has no cycles and has a direction for each edge.
- A **DAG representation of a basic block** is a way of showing the structure and flow of values within a basic block using a DAG.
- The benefits of using a DAG representation of a basic block are:
  - It can help to identify and eliminate common subexpressions, which are expressions that are computed more than once in the same basic block.
  - It can help to perform other optimizations, such as constant folding, copy propagation, dead code elimination, etc.
  - It can help to generate efficient code for the target machine, by minimizing the number of registers and memory accesses needed.
- The steps to construct a DAG representation of a basic block are:
  - Identify the atomic operands (variables or constants) and operators in the basic block.
  - Create a leaf node for each unique operand and label it with the operand name or value.
  - Create an interior node for each operator and label it with the operator symbol.
  - Connect the interior nodes to the leaf nodes or other interior nodes according to the order of evaluation of the expressions.
  - If an interior node has more than one parent, it means that it is a common subexpression.
  - If an interior node has no parent, it means that it is a dead code.
- An example of a DAG representation of a basic block is:

```
a = b + c
d = a - e
b = b + c
f = d + e
```

The DAG representation of this basic block is:

```
    +     -
   / \   / \
  b   c a   e
 / \     \
a   b     +
         / \
        d   e
       / \
      f   d
```

In this DAG, we can see that:

  - The expression `b + c` is a common subexpression, as it is computed twice and has two parents.
  - The expression `a - e` is a dead code, as it is not used in any subsequent statement and has no parent.
  - The expression `d + e` is not a common subexpression, as it is computed only once and has one parent.
  - The expression `a` is a copy of `b + c`, as it is assigned the same value and has the same child.



# Value Numbers and Algebraic Laws

- Value numbers are numbers assigned to each expression or variable in a program to identify equivalent computations and eliminate redundant ones.
- Value numbers are computed by traversing the program's control flow graph in a dominator-based order and applying a hash function to each expression or variable.
- Value numbers can be used to implement local and global common subexpression elimination, copy propagation, constant folding, and partial redundancy elimination.
- Algebraic laws are rules that describe the properties of mathematical operations and expressions, such as commutativity, associativity, distributivity, and identity.
- Algebraic laws can be used to simplify expressions and optimize code generation by applying algebraic transformations, such as x = x * 1 -> x = x, x + y = y + x, x * (y + z) = x * y + x * z, etc.
- Algebraic laws can also be used to detect and eliminate strength-reducing operations, such as x * 2 -> x + x, x / 2 -> x >> 1, x * 4 -> x << 2, etc.
- Algebraic laws can be applied to expressions with the same value number, as they are guaranteed to be equivalent for all possible program inputs.



# Global Data-Flow Analysis

- Global data-flow analysis is a technique to efficiently optimize the code by collecting and distributing information about the program to each block of the flow graph  .
- A flow graph is a representation of the control flow of a program, where each node is a basic block (a sequence of instructions with no jumps or branches) and each edge is a possible transfer of control.
- Data-flow analysis computes analysis facts for each program point, which are facts about variables, expressions, etc. that are relevant for optimization.
- The analysis facts are computed by applying data-flow equations to each node and edge of the flow graph, which describe how the facts are propagated and modified along the control flow.
- The data-flow equations are based on two sets of information for each node: the **gen** set and the **kill** set. The **gen** set contains the facts that are generated by the node, and the **kill** set contains the facts that are invalidated by the node.
- The data-flow equations can be classified into two types: **forward** and **backward**. Forward equations compute the facts that are available at the exit of a node from the facts that are available at the entry of a node. Backward equations compute the facts that are available at the entry of a node from the facts that are available at the exit of a node.
- The data-flow equations can also be classified into two types: **may** and **must**. May equations compute the facts that may be true at a program point, and must equations compute the facts that must be true at a program point.
- The data-flow analysis can be solved by applying a fixed-point iteration algorithm, which repeatedly updates the analysis facts for each node and edge until no more changes occur.
- The data-flow analysis can be used for various optimizations, such as constant propagation, dead code elimination, common subexpression elimination, loop invariant code motion, etc.

