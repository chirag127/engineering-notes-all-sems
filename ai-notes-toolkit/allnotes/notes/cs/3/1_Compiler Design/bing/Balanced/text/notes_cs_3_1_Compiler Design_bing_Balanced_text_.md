

## Unit 1 - Introduction to Compiler

- A compiler is a program that translates a source program written in a high-level language into a target program written in a low-level language.
- The source program is also called the source code, and the target program is also called the object code or the executable code.
- The process of compilation involves several phases, such as lexical analysis, syntax analysis, semantic analysis, intermediate code generation, code optimization, and code generation.
- The compiler may also perform other tasks, such as error detection, error recovery, symbol table management, and debugging support.
- The main advantages of using a compiler are:
  - The compiler can perform various checks and optimizations on the source code, which can improve the quality and efficiency of the target code.
  - The compiler can generate machine-independent code, which can be executed on different platforms with minimal changes.
  - The compiler can protect the intellectual property of the source code, as the target code is harder to reverse engineer.
  - The compiler can speed up the execution of the program, as the target code is directly executed by the hardware, without the need for an interpreter.
- The main challenges of designing a compiler are:
  - The compiler must conform to the syntax and semantics of the source language and the target language, which may have different features and constraints.
  - The compiler must handle various errors and exceptions that may occur during the compilation process, and report them to the user in a meaningful way.
  - The compiler must balance the trade-offs between the time and space complexity of the compilation process and the quality and efficiency of the target code.
  - The compiler must cope with the evolution and diversity of the source language and the target language, which may require frequent updates and extensions.



### Phases and Passes of Compiler

- A compiler is a software that converts a source program written in a high-level language into a target program written in a low-level language.
- The compilation process involves several steps, which are called phases of the compiler.
- Each phase of the compiler takes input from the previous phase, performs some tasks, and produces output for the next phase.
- The number of times the compiler scans the source program is called the number of passes of the compiler.
- A pass can consist of one or more phases, depending on the design of the compiler.
- The main phases of a compiler are:

  - Lexical analysis: This phase scans the source program and converts it into a sequence of tokens, which are the basic units of the language, such as keywords, identifiers, literals, operators, etc.
  - Syntax analysis: This phase checks the syntactic structure of the source program and builds a parse tree, which represents the hierarchical relationship among the tokens.
  - Semantic analysis: This phase checks the semantic meaning of the source program and performs tasks such as type checking, scope checking, declaration checking, etc. It also annotates the parse tree with additional information, such as types, values, addresses, etc.
  - Intermediate code generation: This phase translates the parse tree into an intermediate representation, which is independent of the source and target languages. The intermediate representation can be in the form of an abstract syntax tree, a three-address code, a quadruple, etc.
  - Code optimization: This phase improves the quality of the intermediate code by applying various techniques, such as constant folding, dead code elimination, loop optimization, etc. The goal is to reduce the execution time and space requirements of the target program.
  - Code generation: This phase converts the optimized intermediate code into the target code, which is specific to the target machine. The target code can be in the form of assembly language, machine code, or bytecode.

- The following diagram shows the phases and passes of a compiler:

Phases and passes of a compiler

- Source: [Passes and Phases of Compiler Design | T4Tutorials.com](https://t4tutorials.com/passes-and-phases-of-compiler-design/)



### Bootstrapping

- Bootstrapping is the process of creating a compiler (or assembler) using the language that it intends to compile (or assemble).
- Bootstrapping is possible because a compiler is just a program that takes some input (source code) and produces some output (target code or executable code).
- Bootstrapping can be done in several ways, such as:
  - Writing an interpreter for the source language in some other language, and then using the interpreter to run the source code of the compiler.
  - Writing a compiler for a subset of the source language in some other language, and then using the compiler to compile the rest of the compiler written in the source language.
  - Writing a cross-compiler that runs on a different platform and produces target code for the desired platform, and then using the cross-compiler to compile the compiler for the desired platform.
  - Using an existing compiler for the source language to compile the compiler, and then replacing the existing compiler with the new compiler.
- Bootstrapping has several advantages, such as:
  - It allows the compiler writer to use the features and abstractions of the source language to implement the compiler, making the development easier and faster.
  - It ensures that the compiler is consistent and compatible with the source language, avoiding errors and discrepancies that may arise from using a different language.
  - It demonstrates the expressiveness and completeness of the source language, showing that it can be used to implement any computable function, including itself.
  - It improves the performance and quality of the compiler, as the compiler can optimize and debug itself using the same techniques that it applies to other programs.



### Finite state machines and regular expressions and their applications to lexical analysis

- Finite state machines (FSMs) are abstract models of computation that can process a finite amount of input and produce a finite amount of output.
- FSMs consist of a set of states, a set of input symbols, a set of output symbols, a transition function that maps a state and an input symbol to a new state, and a start state and a set of final states.
- FSMs can be deterministic (DFA) or nondeterministic (NFA). A DFA has exactly one transition for each state and input symbol, while an NFA can have zero, one, or more transitions for each state and input symbol.
- Regular expressions (REs) are a concise and expressive way of specifying a set of strings, called a regular language. REs use symbols, operators, and parentheses to construct complex patterns from simpler ones.
- REs and FSMs are equivalent in expressive power, meaning that for any RE, there exists an FSM that recognizes the same language, and vice versa. Algorithms exist to convert from one to the other.
- Lexical analysis is the process of breaking down a source code into a sequence of tokens, which are the smallest meaningful units of a language. Tokens can be identifiers, keywords, literals, operators, punctuation, etc.
- Lexical analysis is an application of FSMs, as each token can be recognized by a DFA or an NFA. A lexical analyzer can be implemented as a table-driven or a code-driven FSM, which reads the input character by character and changes its state accordingly.
- REs are useful for specifying the patterns of tokens in a language. A lexical analyzer can be generated automatically from a set of REs, using tools such as Lex or Flex. These tools convert the REs into NFAs, then into DFAs, and then into executable code.



### Optimization of DFA-Based Pattern Matchers

- DFA stands for deterministic finite automaton, which is a model of computation that can recognize regular languages.
- A pattern matcher is a program that can find all occurrences of a given pattern in a text, such as a regular expression or a string.
- A DFA-based pattern matcher can be constructed from a regular expression by applying the following steps:
  - Convert the regular expression to a nondeterministic finite automaton (NFA) using Thompson's construction algorithm.
  - Convert the NFA to a DFA using the subset construction algorithm.
  - Minimize the DFA using Hopcroft's algorithm or a similar technique.
- The advantages of using a DFA-based pattern matcher are:
  - It can scan the text in a single pass, without backtracking or lookahead.
  - It can match multiple patterns simultaneously by using a combined DFA that accepts the union of the patterns.
  - It can be implemented efficiently using a table-driven or a code-driven approach.
- The disadvantages of using a DFA-based pattern matcher are:
  - It may require a large amount of memory to store the transition table or the generated code, especially if the patterns are complex or numerous.
  - It may not support some features of regular expressions, such as capturing groups, backreferences, or lookahead assertions.
- The optimization of DFA-based pattern matchers can be done by applying various techniques, such as:
  - Reducing the size of the transition table by using compression methods, such as row displacement, column displacement, or perfect hashing.
  - Reducing the number of transitions by using character classes, equivalence classes, or transition merging.
  - Reducing the number of states by using state merging, state splitting, or state elimination.
  - Reducing the number of patterns by using pattern simplification, pattern elimination, or pattern grouping.
  - Reducing the complexity of the patterns by using regular expression rewriting, regular expression minimization, or regular expression factorization.



### Implementation of Lexical Analyzers

- Lexical analysis is the first phase of the compiler design, also known as a scanner .
- It converts the high-level input program into a sequence of tokens .
- A token is a meaningful collection of characters in a program, such as keywords, identifiers, literals, operators, etc.
- Lexical analyzer is implemented to scan the entire source code of the program and match the sequence of characters with the pattern of a token.
- Lexical analyzer can be implemented with the deterministic finite automata (DFA), which is a finite state machine that accepts or rejects a string based on the final state it reaches.
- The DFA can be constructed from a regular expression (regex), which is a notation for describing the set of strings that belong to a token.
- The steps to implement a lexical analyzer using DFA are:
  - Define the regex for each token in the language.
  - Convert the regex to a nondeterministic finite automata (NFA), which is a finite state machine that can have multiple transitions for the same input symbol.
  - Convert the NFA to a DFA using the subset construction algorithm, which creates a new state for each subset of NFA states.
  - Minimize the DFA using the partitioning algorithm, which merges the equivalent states that have the same transitions for all input symbols.
  - Generate the transition table for the DFA, which maps each state and input symbol to the next state.
  - Implement the DFA as a program that reads the input character by character and updates the current state according to the transition table.
  - Output the token name and attribute value when the DFA reaches a final state or an error state.
- An example of a lexical analyzer for Java language is given in , which uses the Java code to implement the DFA and the transition table.



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



### LEX compiler

- Lex is a computer program that generates lexical analyzers (\"scanners\" or \"lexers\").
- Lexical analyzers are programs that take a stream of input characters and produce a stream of tokens, which are the basic units of syntax in a programming language.
- Lex is commonly used with the yacc parser generator, which takes a stream of tokens and produces a syntax tree or a parse tree.
- Lex is written in the Lex language, which consists of three sections: definitions, rules, and user subroutines.
- The definitions section contains declarations of variables, constants, regular expressions, and macros that are used in the rules section.
- The rules section contains patterns and actions, which specify what to do when a pattern is matched in the input stream.
- The user subroutines section contains auxiliary functions that are called by the actions in the rules section.
- The function of Lex is as follows:
  - Firstly, the lexical analyzer creates a program lex.l in the Lex language.
  - Then, the Lex compiler runs the lex.l program and produces a C program lex.yy.c, which contains the code for the lexical analyzer. 
  - Finally, the C compiler compiles the lex.yy.c file into an executable file, which can be run on the input stream to produce the output stream of tokens. 
- Lex is the standard lexical analyzer generator on many Unix systems, and an equivalent tool is specified as part of the POSIX standard.
- Lex can be used for various applications, such as text processing, code generation, syntax highlighting, lexical analysis, etc.



### Formal grammars and their application to syntax analysis

- A formal grammar is a set of rules that define the structure and syntax of a language. A grammar consists of four components :
  - A finite set of terminal symbols, denoted by V, that represent the basic units or tokens of the language.
  - A finite set of non-terminal symbols, denoted by N, that represent the syntactic categories or variables of the language.
  - A finite set of production rules, denoted by P, that specify how to form valid sentences or phrases from the terminal and non-terminal symbols.
  - A start symbol, denoted by S, that belongs to N and represents the initial syntactic category of the language.
- A formal grammar can be used to describe the syntax of a programming language, which is the set of rules that determine how a program is written and structured. A grammar can also be used to generate or recognize valid sentences or programs in the language.
- Syntax analysis, also known as parsing, is a process in compiler design where the compiler checks if the source code follows the grammatical rules of the programming language. This is typically the second stage of the compilation process, following lexical analysis, where the source code is divided into tokens.
- Syntax analysis involves two main tasks:
  - Building a parse tree, which is a hierarchical representation of the syntactic structure of the source code, based on the production rules of the grammar.
  - Reporting and handling any syntax errors, which are violations of the grammatical rules of the language, such as missing or extra symbols, mismatched parentheses, etc.
- Syntax analysis can be performed using different algorithms and techniques, depending on the type and complexity of the grammar. There are four main types of formal grammars, classified by the Chomsky hierarchy:
  - Type 0 or unrestricted grammars, which have no restrictions on the form of the production rules. They can generate any recursively enumerable language, which is the most general class of languages that can be recognized by a Turing machine.
  - Type 1 or context-sensitive grammars, which have the restriction that the left-hand side of a production rule must not be shorter than the right-hand side. They can generate any context-sensitive language, which is a subclass of recursively enumerable languages that can be recognized by a linear bounded automaton.
  - Type 2 or context-free grammars, which have the restriction that the left-hand side of a production rule must be a single non-terminal symbol. They can generate any context-free language, which is a subclass of context-sensitive languages that can be recognized by a pushdown automaton. Most programming languages are designed using context-free grammars, as they are easier to parse and understand than more complex grammars.
  - Type 3 or regular grammars, which have the restriction that the right-hand side of a production rule must be either a single terminal symbol, or a single terminal symbol followed by a single non-terminal symbol. They can generate any regular language, which is a subclass of context-free languages that can be recognized by a finite automaton. Regular grammars are often used to describe the lexical structure of a language, such as the keywords, identifiers, operators, etc.



### BNF notation for the notes of the Unit 1 - Introduction to Compiler in the subject of Compiler Design

- BNF stands for **Backus Naur Form** notation . It is a form of notation used for specifying the **syntax** of programming languages and command sets . The syntax means the structure of strings in a certain language.
- BNF is a type of **metasyntax** notation for **context-free grammars** . A metasyntax is a syntax for defining syntaxes. A context-free grammar is a set of rules that describe how to generate strings from a given alphabet .
- BNF was introduced by **John Bakus** and **Peter Naur** in 1960 . It is also known as **Backus Normal Form** or **Backus Naur Form** .
- BNF uses the following symbols and conventions  :
  - **::=** means "is defined as" or "can be replaced by".
  - **< >** enclose **non-terminal symbols**, which are placeholders for syntactic categories or groups of strings.
  - **|** means "or" and separates alternative expansions of a non-terminal symbol.
  - **" "** enclose **terminal symbols**, which are literal symbols or characters that appear in the language.
  - **[ ]** enclose optional parts of a production rule.
  - **{ }** enclose parts of a production rule that can be repeated zero or more times.
  - **( )** are used for grouping symbols or expressions.
  - **;** is used to terminate a production rule.
- For example, the following BNF notation defines the syntax of a simple arithmetic expression language :

```
<expression> ::= <term> | <expression> "+" <term> | <expression> "-" <term>;
<term> ::= <factor> | <term> "*" <factor> | <term> "/" <factor>;
<factor> ::= <number> | "(" <expression> ")";
<number> ::= <digit> | <number> <digit>;
<digit> ::= "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9";
```

- This means that an expression can be a term, or an expression followed by a plus or minus sign and another term. A term can be a factor, or a term followed by a multiplication or division sign and another factor. A factor can be a number, or an expression enclosed in parentheses. A number can be a digit, or a number followed by another digit. A digit can be any of the symbols from 0 to 9.



### Ambiguity

- Ambiguity in grammar is not good for a compiler construction.
- A grammar is ambiguous if it produces more than one parse tree for some sentence.
- An ambiguous grammar or string can have multiple meanings.
- Ambiguity can cause confusion and errors in the syntax analysis and code generation phases of a compiler.
- No method can detect and remove ambiguity automatically, but it can be removed by either re-writing the whole grammar without ambiguity, or by setting and following associativity and precedence constraints.
- Some common sources of ambiguity are:
  - Left recursion: A grammar is left recursive if it has a non-terminal that derives to itself on the left. For example, `A -> Aa | b` is left recursive. Left recursion can cause infinite loops in top-down parsers.
  - Dangling else: A grammar is ambiguous if it has an `if-then-else` statement that can be associated with more than one `if` statement. For example, `if E1 then if E2 then S1 else S2` is ambiguous because the `else` can be matched with either `if`. Dangling else can cause incorrect interpretation of the conditional statements.
- Some methods to eliminate ambiguity are:
  - Removing left recursion: A left recursive grammar can be converted to a right recursive grammar by applying a transformation rule. For example, `A -> Aa | b` can be transformed to `A -> bA'` and `A' -> aA' | ε` where `ε` is the empty string. This eliminates the possibility of infinite loops in top-down parsers.
  - Adding brackets: A grammar can be made unambiguous by adding brackets to indicate the scope of the statements. For example, `if E1 then if E2 then S1 else S2` can be written as `if E1 then { if E2 then S1 else S2 }` or `if E1 then { if E2 then S1 } else S2` depending on the intended meaning. This eliminates the confusion of the dangling else.
  - Using precedence and associativity rules: A grammar can be made unambiguous by defining the order and direction of the operators. For example, `E -> E + E | E * E | id` is ambiguous because it can produce different parse trees for `id + id * id`. This can be resolved by specifying that `*` has higher precedence than `+` and both are left associative. This means that `id + id * id` is equivalent to `id + (id * id)`. This eliminates the ambiguity of the expression.



### YACC for the notes of the Unit 1 - Introduction to Compiler in the subject of Compiler Design

- YACC stands for Yet Another Compiler-Compiler. It is a tool that generates a parser for a given grammar. A parser is a program that analyzes the syntactic structure of a source code and checks if it conforms to the rules of the language.
- YACC is often used with a lexical analyzer tool such as lex, which is used to tokenize the input source code into a stream of tokens. The tokens are then fed to the parser generated by YACC, which builds a parse tree or an abstract syntax tree (AST) representing the logical structure of the code.
- YACC is based on the LALR(1) parsing algorithm, which stands for LookAhead, Left-to-right, Rightmost derivation with 1 lookahead token. This algorithm is efficient and handles most of the grammars used in programming languages.
- YACC takes as input a file that contains three sections: definitions, rules, and user code. The definitions section contains declarations of tokens, variables, and other symbols used in the grammar. The rules section contains the production rules of the grammar, which specify how a non-terminal symbol can be derived from a sequence of terminal and non-terminal symbols. The user code section contains any C code that needs to be executed when a rule is matched by the parser.
- YACC generates a C program that contains the parser, which can be compiled and linked with the lexical analyzer and any other code to form a complete compiler or interpreter for the language. The generated parser uses a stack to keep track of the current state and the symbols that have been parsed so far. It also uses a table-driven approach to determine the next action based on the current state and the lookahead token.
- YACC can handle ambiguous grammars, which are grammars that have more than one possible parse tree for a given input. However, it may report conflicts, which are situations where the parser cannot decide which action to take based on the current state and the lookahead token. There are two types of conflicts: shift-reduce and reduce-reduce. A shift-reduce conflict occurs when the parser can either shift the lookahead token onto the stack or reduce a rule using the symbols on the stack. A reduce-reduce conflict occurs when the parser can reduce more than one rule using the same symbols on the stack. YACC resolves conflicts by choosing the action that appears first in the rules section, but it is advisable to avoid or eliminate conflicts by modifying the grammar or using precedence and associativity declarations.



### The syntactic specification of programming languages

- The syntax of a programming language defines the rules for writing valid programs in that language. It specifies how the symbols, keywords, operators, and punctuation marks of the language can be combined to form expressions, statements, and other syntactic units.
- The syntax of a programming language can be described using various formal methods, such as regular expressions, context-free grammars, and abstract syntax trees. These methods can help to analyze, parse, and generate programs in a systematic and unambiguous way.
- The syntax of a programming language can be broadly divided into three levels:
  - Lexical level: This level determines how characters form tokens, which are the basic components of the source code. Characters belong to one of the five classes of tokens: identifiers, operators, constants, separators, and reserved words.
  - Grammatical level: This level determines how tokens form phrases, which are the syntactic units of the language. Each programming language has its own unique phrasing, which can be defined by a context-free grammar or a similar notation.
  - Contextual level: This level determines the naming conventions and the validity of types, which are the semantic aspects of the language. For example, the contextual level checks if the variables or objects names refer to existing entities, and if the operands and operators are compatible in terms of their types.
- The syntactic specification of a programming language is an important part of its design and implementation, as it affects the readability, expressiveness, and correctness of the programs written in that language. A good syntax should be clear, consistent, concise, and intuitive for the programmers.



### Context Free Grammars

- A context free grammar (CFG) is a set of rules that defines a formal language. A formal language is a set of strings that can be generated by following the rules of the grammar. 
- A CFG consists of four components: a set of terminals, a set of non-terminals, a start symbol, and a set of productions. Terminals are the basic symbols of the language, such as letters, digits, or operators. Non-terminals are placeholders for sequences of terminals or other non-terminals. The start symbol is a special non-terminal that represents the whole language. Productions are rules that specify how to replace a non-terminal with a sequence of terminals and/or non-terminals. 
- A CFG can be written in Backus-Naur form (BNF), which is a notation for specifying grammars. A BNF grammar consists of a series of production rules, each of which has the form:

  `non-terminal ::= sequence`

  where `non-terminal` is a non-terminal symbol, `::=` means "is defined as", and `sequence` is a sequence of terminals and/or non-terminals. For example, the following BNF grammar defines a simple arithmetic language:

  ```
  expr ::= term | expr + term | expr - term
  term ::= factor | term * factor | term / factor
  factor ::= number | ( expr )
  number ::= digit | number digit
  digit ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
  ```

  This grammar can generate strings such as `2 + 3 * (4 - 5)`, `(6 + 7) / 8`, and `9 * 9`. 
- A CFG can also be represented by a parse tree, which is a tree structure that shows how a string is derived from the grammar. The root of the tree is the start symbol, and the leaves are the terminals. Each internal node is a non-terminal, and each branch corresponds to a production. For example, the following parse tree shows how the string `2 + 3 * (4 - 5)` is derived from the grammar above:

  ```
          expr
         / |  \
      expr +  term
      / | \   / | \
    term * factor ( expr )
     |    |      / | \
  factor  |    expr - term
     |    |    / | \   |
  number  |  term + factor
     |    |   |   |   |
   digit  | factor | factor
     |    |   |   |   |
     2    3   (   4   5
  ```

  A parse tree shows the syntactic structure of a string, and can be used to evaluate its meaning or semantics. For example, to evaluate the arithmetic expression `2 + 3 * (4 - 5)`, we can use the order of operations and the parse tree to get:

  ```
  2 + 3 * (4 - 5)
  = 2 + 3 * (-1)    (by evaluating the subtree (expr - term))
  = 2 + (-3)        (by evaluating the subtree term * factor)
  = -1              (by evaluating the subtree expr + term)
  ```

  A parse tree can also be used to translate a string from one language to another, by applying different rules or actions to each node. For example, to translate the arithmetic expression `2 + 3 * (4 - 5)` from infix notation to postfix notation, we can use the following rules:

  - If the node is a terminal, output it.
  - If the node is a non-terminal, visit its children from left to right, and output the node after visiting all its children.

  Applying these rules to the parse tree, we get:

  ```
  2 + 3 * (4 - 5)
  = 2 3 4 5 - * +    (by visiting the nodes in the following order: 2, 3, 4, 5, -, *, +)
  ```

  A parse tree can also be used to check the validity of a string, by verifying that it conforms to the grammar. For example, the string `2 + * 3` is not valid in the arithmetic language, because it does not have a parse tree that matches the grammar. [^1



### Derivation and Parse Trees

- A derivation is a sequence of applications of production rules that transforms the start symbol of a grammar into a string of terminals.
- A parse tree is a hierarchical structure that represents the derivation of the grammar to yield input strings .
- A parse tree has the following properties :
  - The root node of the parse tree has the start symbol of the grammar.
  - The internal nodes of the parse tree are non-terminals of the grammar.
  - The leaf nodes of the parse tree are terminals of the grammar.
  - The order of the children of a node corresponds to the order of the symbols on the right-hand side of the production rule used to derive the node.
  - The inorder traversal of the leaf nodes gives the input string derived from the grammar.
- A parse tree can be constructed from a derivation by following these steps:
  - Start with a single node labeled with the start symbol of the grammar.
  - For each step of the derivation, replace a non-terminal node with a subtree whose root is the non-terminal and whose children are the symbols on the right-hand side of the production rule used.
  - Repeat until all the non-terminal nodes are replaced by terminal nodes.
- A parse tree can also be used to construct a derivation by following these steps:
  - Start with the root node labeled with the start symbol of the grammar.
  - For each non-terminal node, write the production rule that corresponds to its subtree, with the non-terminal on the left-hand side and its children on the right-hand side.
  - Repeat until all the non-terminal nodes are written as production rules.
  - Concatenate the production rules from top to bottom to get the derivation.
- A parse tree is also called a concrete syntax tree, because it directly corresponds to the context-free grammar.
- A parse tree can be simplified by removing unnecessary nodes, such as parentheses, punctuation, or keywords, to get an abstract syntax tree, which corresponds to a simplified or abstract grammar .
- An abstract syntax tree is usually used in compiler design, because it captures the essential structure and meaning of the input string, while ignoring the syntactic details .



### Capabilities of CFG for the notes of the Unit 1 - Introduction to Compiler in the subject of Compiler Design

- CFG stands for Context-Free Grammar, which is a set of recursive rules used to generate patterns of strings.
- CFG is useful to describe most of the programming languages , as it can capture the syntax and structure of the source code.
- An efficient parser can be easily constructed automatically if the grammar is properly written . A parser is a program that analyzes the source code and checks if it conforms to the grammar rules.
- CFG can handle features such as balanced parentheses, matching begin-end, corresponding if-then-else, etc., which are common in programming languages.
- CFG can also construct suitable grammars for expressions, using the features of associativity and precedence information . For example, the grammar can specify that multiplication has higher precedence than addition, and that expressions are evaluated from left to right.
- CFG is not powerful enough to describe all possible languages, as there are some languages that require context-sensitive rules or other mechanisms. For example, the language of palindromes (strings that are the same when reversed) cannot be generated by a CFG.



## Unit 2 - Basic Parsing Techniques

- Parsing is the process of analyzing the syntactic structure of a given input string according to a given grammar.
- A grammar is a set of rules that define the syntax of a language, i.e., how words and symbols can be combined to form valid sentences.
- A parser is a program that implements a parsing algorithm, i.e., a method of applying the grammar rules to the input string and constructing a parse tree or a derivation.
- A parse tree is a hierarchical representation of the syntactic structure of a sentence, where each node corresponds to a grammar rule or a terminal symbol.
- A derivation is a sequence of grammar rule applications that generate a sentence from the start symbol of the grammar.
- There are two main types of parsing techniques: top-down and bottom-up.
- Top-down parsing is a method of parsing that starts from the start symbol of the grammar and tries to match the input string from left to right, using the grammar rules to predict what symbols should come next.
- Bottom-up parsing is a method of parsing that starts from the input string and tries to reduce it to the start symbol of the grammar, using the grammar rules to identify what symbols can be combined together.
- Both top-down and bottom-up parsing can be implemented using recursive or iterative algorithms, and can be enhanced with various techniques such as lookahead, backtracking, memoization, etc.
- Some examples of top-down parsing algorithms are recursive descent, LL(1), and predictive parsing.
- Some examples of bottom-up parsing algorithms are shift-reduce, LR(0), SLR(1), LR(1), and LALR(1) parsing.



### Parsers for the notes of the Unit 2 - Basic Parsing Techniques in the subject of Compiler Design

- A parser is a program that is part of the compiler, and parsing is part of the compiling process.
- Parsing happens during the analysis stage of compilation. In parsing, code is taken from the preprocessor, broken into smaller pieces and analyzed so other software can understand it.
- The parser takes a token string as input and with the help of existing grammar, converts it into the corresponding Intermediate Representation (IR). The parser is also known as Syntax Analyzer.
- There are two main types of parsers: top-down parsers and bottom-up parsers.
- Top-down parsers start from the root of the parse tree and try to match the input with the grammar rules. They use a stack to store the intermediate results and predict the next production to apply.
- Bottom-up parsers start from the leaves of the parse tree and try to reduce the input to the start symbol of the grammar. They use a stack to store the intermediate results and apply the production that matches the top of the stack and the input.
- Top-down parsers can be further classified into recursive descent parsers and predictive parsers.
- Recursive descent parsers are a type of top-down parsers that use recursive functions to implement each non-terminal of the grammar. They may have more than one production to choose from for a single instance of input, which can lead to backtracking.
- Predictive parsers are a type of top-down parsers that use a parsing table to decide which production to apply based on the input and the stack element. They do not require backtracking, but they can only handle a subset of grammars called LL(1) grammars.
- Bottom-up parsers can be further classified into shift-reduce parsers and operator-precedence parsers.
- Shift-reduce parsers are a type of bottom-up parsers that use two operations: shift and reduce. Shift moves the next input symbol to the top of the stack, and reduce applies a production that matches the top of the stack and replaces it with the left-hand side of the production.
- Operator-precedence parsers are a type of bottom-up parsers that use a precedence table to determine the order of operations and operands. They can handle a subset of grammars called operator-precedence grammars, which have no ambiguity and no left recursion.



### Shift reduce parsing

- Shift reduce parsing is a class of efficient, table-driven bottom-up parsing methods for computer languages and other notations formally defined by a grammar.
- The parsing methods most commonly used for parsing programming languages, LR parsing and its variations, are shift-reduce methods.
- Shift reduce parsing uses a stack to hold the grammar and an input tape to hold the string.
- Shift reduce parsing performs the two actions: shift and reduce.
  - Shift: This involves moving symbols from the input buffer onto the stack.
  - Reduce: This involves replacing a handle (a substring that matches the right-hand side of a production rule) on the top of the stack with the corresponding non-terminal symbol (the left-hand side of the production rule).
- The goal of shift reduce parsing is to reduce the input string to the start symbol of the grammar.
- Shift reduce parsing is a type of bottom-up parsing as it generates a parse tree from the leaves (bottom) to the root (up).
- Shift reduce parsing can handle left-recursive grammars, but not right-recursive grammars.
- Shift reduce parsing can detect syntax errors as soon as they occur, but it may not report them until later.
- Shift reduce parsing can be implemented using a finite state machine with a stack.
- Shift reduce parsing can be classified into different types based on the way the parsing table is constructed, such as SLR, LALR, LR, and CLR.



### Operator Precedence Parsing

- Operator precedence parsing is a bottom-up parsing technique that can handle a subset of LR(1) grammars.
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
  - Reduce: If the relation is `>`, the parser pops the symbols from the stack until it finds a handle (a right-hand side of a production) and replaces it with the corresponding left-hand side (a nonterminal). The input pointer does not change.
  - Accept: If the stack contains only the start symbol of the grammar and the input buffer contains only `$`, the parser accepts the input string and terminates.
  - Error: If the relation is ` ` or the stack does not contain a handle, the parser reports an error and terminates.
- Operator precedence parsing is simple and efficient, but it can only handle a limited class of grammars. It also requires the grammar to be unambiguous and have no left recursion.
- Operator precedence parsing is commonly used for parsing expressions involving arithmetic, logical, and bitwise operators, as they have a well-defined precedence and associativity.



### Top-Down Parsing for the Notes of the Unit 2 - Basic Parsing Techniques in the Subject of Compiler Design

- Top-down parsing is a method of parsing the input string provided by the lexical analyzer and generating a parse tree for it using leftmost derivation.
- Top-down parsing starts from the root node (start symbol) and expands it using the grammar productions until all the leaves are terminals that match the input string.
- Top-down parsing can be classified into two types: recursive descent parsing and predictive parsing.
- Recursive descent parsing is a top-down parsing technique that uses a procedure for each non-terminal in the grammar. Each procedure tries to match the input string with the right-hand side of the production for that non-terminal.
- Recursive descent parsing may require backtracking, which means undoing the previous choices and trying other alternatives, if the input string does not match the expected production.
- Predictive parsing is a top-down parsing technique that does not require backtracking. It uses a parsing table and a stack to determine which production to apply next based on the current input symbol and the top of the stack.
- Predictive parsing can only be applied to a special class of grammars called LL(1) grammars, which have the following properties:
  - They are unambiguous, which means there is only one possible parse tree for any input string.
  - They are left-factored, which means there is no common prefix in the right-hand side of any two productions for the same non-terminal.
  - They do not have left recursion, which means there is no production of the form A -> Aα, where A is a non-terminal and α is a string of terminals and non-terminals.



### Predictive Parsers

- A predictive parser is a type of top-down parser that does not require backtracking or backup.
- A predictive parser can predict which production to use by looking at the next input symbol and the current non-terminal.
- A predictive parser is also known as an LL(1) parser, where L stands for left-to-right scanning of the input, L stands for leftmost derivation of the parse tree, and 1 stands for one symbol of lookahead.
- A predictive parser can be implemented by using a stack and a table, where the stack stores the symbols to be matched and the table stores the parsing actions for each pair of stack symbol and input symbol.
- A predictive parser can only handle a subset of context-free grammars, namely those that are LL(1). A grammar is LL(1) if and only if it satisfies two conditions: no left recursion and no ambiguity.
- A left recursive grammar is one that has a production of the form A -> Aα, where A is a non-terminal and α is a string of terminals and non-terminals. A left recursive grammar can cause infinite recursion in a predictive parser.
- An ambiguous grammar is one that has more than one parse tree for some input string. An ambiguous grammar can cause confusion and inconsistency in a predictive parser.
- A grammar can be converted to an equivalent LL(1) grammar by eliminating left recursion and left factoring. Left factoring is a technique of extracting common prefixes from alternative productions of a non-terminal.
- A predictive parser can be constructed by using the following steps:
  - Eliminate left recursion and left factor the grammar if necessary.
  - Compute the FIRST and FOLLOW sets for each non-terminal in the grammar. The FIRST set of a non-terminal is the set of terminals that can begin a string derived from that non-terminal. The FOLLOW set of a non-terminal is the set of terminals that can immediately follow that non-terminal in a derivation.
  - Construct the predictive parsing table by using the following rules:
    - For each production A -> α, if a is in FIRST(α), then add A -> α to the entry M[A, a] in the table, where M is the table and a is a terminal.
    - For each production A -> α, if ε is in FIRST(α), then for each terminal b in FOLLOW(A), add A -> α to the entry M[A, b] in the table.
    - For each production A -> α, if ε is in FIRST(α) and $ is in FOLLOW(A), where $ is the end-of-input marker, then add A -> α to the entry M[A, $] in the table.
  - Simulate the predictive parser by using the following algorithm:
    - Initialize the stack with the start symbol of the grammar and the input with the end-of-input marker.
    - Repeat until the stack is empty or an error occurs:
      - Pop the top symbol X from the stack and read the next input symbol a.
      - If X is a terminal, then match it with a. If they are equal, then continue. If they are not equal, then report an error.
      - If X is a non-terminal, then look up the entry M[X, a] in the table. If it is empty, then report an error. If it contains a production X -> α, then push the symbols of α in reverse order onto the stack. If it contains more than one production, then report an ambiguity error.
    - If the stack is empty and the input is consumed, then report a successful parse. Otherwise, report an error.



### Automatic Construction of Efficient Parsers

- A parser is a program that analyzes the syntactic structure of a given input according to a given grammar.
- A parser can be constructed manually or automatically by using a parser generator tool.
- A parser generator is a program that takes a grammar specification as input and produces a parser program as output.
- A parser generator can also produce a parsing table, which is a data structure that encodes the parsing actions for each state and input symbol.
- There are different types of parsers, such as top-down parsers, bottom-up parsers, and recursive-descent parsers.
- Bottom-up parsers are more powerful and efficient than top-down parsers, as they can handle a larger class of grammars and avoid backtracking.
- LR parsers are a class of bottom-up parsers that use a stack to store the parsing states and a lookahead symbol to decide the next action.
- LR parsers can be divided into four subclasses: SLR, LALR, LR(0), and LR(1), depending on the size and accuracy of the parsing table.
- SLR parsers use the follow sets of the grammar to construct the parsing table, which can be smaller but less precise than LR(1) parsers.
- LALR parsers use the lookahead sets of the grammar to construct the parsing table, which can be more precise but larger than SLR parsers.
- LR(0) parsers use only the items of the grammar to construct the parsing table, which can be the smallest but the least precise of all LR parsers.
- LR(1) parsers use the items and the lookahead symbols of the grammar to construct the parsing table, which can be the most precise but the largest of all LR parsers.
- The canonical collection of LR(0) items is a set of sets of items that represent the possible states of the LR(0) parser.
- The canonical collection of LR(1) items is a set of sets of items that represent the possible states of the LR(1) parser.
- The canonical collection of LR(0) items can be constructed by using the closure and goto operations on the grammar.
- The canonical collection of LR(1) items can be constructed by using the augmented closure and goto operations on the grammar.
- The SLR parsing table can be constructed by using the canonical collection of LR(0) items and the follow sets of the grammar.
- The LR(0) parsing table can be constructed by using the canonical collection of LR(0) items and the conflict resolution rules.
- The LR(1) parsing table can be constructed by using the canonical collection of LR(1) items and the conflict resolution rules.
- The LALR parsing table can be constructed by using the canonical collection of LR(1) items and the merging of compatible states.
- The automatic construction of efficient parsers can be done by using a parser generator tool, such as YACC, which can generate LALR parsers from a grammar specification.
- The automatic construction of efficient parsers can also be done by using an incremental parser, which can handle multiple modifications of the input and epsilon productions in the grammar.



### LR parsers

- LR parsers are a type of **bottom-up parsers** that analyse **deterministic context-free languages** in linear time .
- LR parsers read the input from **left to right** and produce a **rightmost derivation** in reverse .
- LR parsers use a **stack** to store the grammar symbols and a **state transition table** to guide the parsing actions .
- LR parsers can handle a large class of grammars, including **ambiguous grammars** and **left-recursive grammars** .
- LR parsers can detect **syntax errors** as soon as possible .
- There are several variants of LR parsers, such as **SLR**, **LALR**, **Canonical LR**, **Minimal LR**, and **GLR** parsers . They differ in the way they construct the state transition table and the amount of lookahead they use .
- LR parsers are widely used in **compiler construction** and **programming language design** .



### The canonical collection of LR(0) items

- An **LR(0) item** is a production of a grammar G with a dot at some position on the right side of the production .
- The dot indicates how much of the input has been scanned up to a given point in the process of parsing.
- For example, the production `S -> XYZ` yields four items:

  - `S -> .XYZ`
  - `S -> X.YZ`
  - `S -> XY.Z`
  - `S -> XYZ.`

- A **canonical collection of LR(0) items** is a set of sets of LR(0) items that are obtained by applying two functions: **closure** and **goto** .
- The **closure** function takes a set of LR(0) items and adds all the items that can be derived from the given items by following the productions whose left side is the symbol after the dot .
- For example, if the grammar is:

  - `S' -> S`
  - `S -> AB`
  - `A -> aA | b`
  - `B -> c`

  Then the closure of the set `{S' -> .S}` is:

  - `S' -> .S`
  - `S -> .AB`
  - `A -> .aA`
  - `A -> .b`

- The **goto** function takes a set of LR(0) items and a grammar symbol, and returns a new set of LR(0) items that are obtained by moving the dot over the given symbol in the original set .
- For example, using the same grammar as above, the goto of the set `{S' -> .S}` and the symbol `S` is:

  - `S' -> S.`

- The canonical collection of LR(0) items is constructed by starting with the closure of the item `S' -> .S`, where `S'` is a new start symbol, and then applying the goto function recursively on all the symbols that appear after the dot in any item .
- The canonical collection of LR(0) items is used to construct a **DFA** that recognizes the viable prefixes of the grammar, which are the prefixes of right sentential forms that can appear on the stack of a shift-reduce parser .
- The canonical collection of LR(0) items also determines the **action** and **goto** tables of an **LR(0) parser**, which is a bottom-up parser that uses the DFA to decide whether to shift or reduce at each step .
- A grammar is **LR(0)** if the canonical collection of LR(0) items does not contain any **conflicts**, which are situations where the parser has more than one possible action for a given state and input symbol .
- No grammar with **epsilon productions** can be LR(0), because the presence of epsilon productions leads to reduce-reduce conflicts.



### Constructing SLR Parsing Tables

- SLR stands for Simple LR, which is a type of LR parser with small parse tables and a relatively simple parser generator algorithm.
- SLR parsers can perform bottom-up parsing of input strings using one token of lookahead to resolve conflicts .
- SLR parsers can handle a subset of LR(1) grammars, which are grammars that can be parsed by LR parsers with one token of lookahead.
- SLR parsers are similar to LR(0) parsers, except that they use the FOLLOW sets of the non-terminals to determine when to reduce.
- The steps for constructing SLR parsing tables are:
  - Write the augmented grammar, which is the original grammar with a new start symbol and a new production S' -> S, where S is the original start symbol.
  - Find the LR(0) collection of items, which are sets of productions with a dot indicating the current position of the parser. Use the closure and goto functions to generate the items and the transitions between them.
  - Find the FOLLOW sets of the left-hand sides of the productions, which are the sets of terminals that can appear after the non-terminals in the derivations. Use the rules of the FOLLOW algorithm to compute them.
  - Define the action and goto functions in the parsing table, which are the functions that tell the parser what to do (shift, reduce, accept, or error) and what state to go to next. Use the LR(0) items and the FOLLOW sets to fill the table entries.
  - Check for conflicts in the table, which are situations where the parser has more than one possible action for a given state and lookahead symbol. If there are no conflicts, the grammar is SLR(1) and the table is complete. If there are conflicts, the grammar is not SLR(1) and the table cannot be used.



### Constructing Canonical LR Parsing Tables

- A canonical LR parsing table is a table used by a canonical LR parser to determine its parsing actions based on the current state and the next input symbol.
- Canonical LR stands for canonical left-to-right, rightmost derivation, which is a type of bottom-up parsing technique for context-free grammars.
- A canonical LR parser can handle any deterministic context-free grammar without introducing conflicts or ambiguities.
- A canonical LR parsing table consists of two parts: an action table and a goto table.
- The action table specifies the action to be taken for each state and terminal symbol pair. The possible actions are:
  - Shift: move the next input symbol to the top of the stack and advance to the next state.
  - Reduce: pop the symbols corresponding to the right-hand side of a production from the stack, push the left-hand side symbol to the stack, and go to the state indicated by the goto table.
  - Accept: accept the input as a valid sentence of the grammar.
  - Error: report an error and terminate the parsing.
- The goto table specifies the next state to be entered after a reduction for each state and nonterminal symbol pair.
- The canonical LR parsing table is constructed from the canonical collection of LR(1) items, which are augmented productions of the grammar with a dot (.) indicating the position of the parser and a lookahead symbol indicating the next expected input symbol.
- The canonical collection of LR(1) items is obtained by applying two operations: closure and goto.
  - Closure: for each item [A -> α.Bβ, a], where B is a nonterminal symbol, add all the items [B -> .γ, b] to the set, where b is any terminal symbol that can follow B in the derivation of αBβa.
  - Goto: for each item [A -> α.Bβ, a], where B is a symbol (terminal or nonterminal), move the dot past B and obtain the item [A -> αB.β, a]. The goto operation is applied to a set of items and returns a new set of items.
- The algorithm for constructing the canonical LR parsing table is as follows:
  - Input: an augmented grammar G'
  - Output: a canonical LR parsing table
  - Method:
    - Initially construct the set of items C = {I0, I1, I2, ..., In}, where C is the canonical collection of LR(1) items for G'.
    - For each item Ii in C and each terminal symbol a, do the following:
      - If [A -> α.aβ, b] is in Ii, then set action[i, a] to shift goto(Ii, a).
      - If [A -> α., a] is in Ii, then set action[i, a] to reduce A -> α, unless A is the start symbol and a is the end-of-input symbol, in which case set action[i, a] to accept.
      - If action[i, a] is undefined, then set it to error.
    - For each item Ii in C and each nonterminal symbol A, do the following:
      - If goto(Ii, A) is not empty, then set goto[i, A] to goto(Ii, A).
      - If goto[i, A] is undefined, then set it to error.
    - Return the action and goto tables as the canonical LR parsing table.



### Constructing LALR parsing tables

- LALR stands for Lookahead LR, which is a type of bottom-up parser that can handle a large class of grammars.
- LALR parsing tables are constructed from the canonical collection of LR(1) items, which are sets of items that represent the possible states of the parser and the lookahead symbols that determine the next action.
- LR(1) items have the form [A -> α.β, a], where A -> αβ is a production, α and β are strings of grammar symbols, and a is a lookahead symbol.
- To construct the LALR parsing tables, the following steps are followed:
  - Step 1: Compute the canonical collection of LR(1) items by applying the closure and goto operations on the augmented grammar.
  - Step 2: Merge the LR(1) items that have the same core, which is the production and the dot position, but different lookaheads, into a single set of items. This reduces the number of states in the parser and the size of the parsing tables.
  - Step 3: Construct the action and goto tables from the merged sets of items, using the same rules as canonical LR(1) parsing. The action table specifies the shift, reduce, accept, or error action for each state and lookahead symbol, and the goto table specifies the next state for each state and nonterminal symbol.
  - Step 4: Resolve any conflicts that may arise in the action table, either by using precedence and associativity rules, or by modifying the grammar to make it unambiguous. Conflicts occur when more than one action is possible for a given state and lookahead symbol.



### Using ambiguous grammars for the notes of the Unit 2 - Basic Parsing Techniques in the subject of Compiler Design

- A grammar is a set of rules that define the syntax of a language, i.e., how the symbols of the language can be combined to form valid sentences.
- A grammar is ambiguous if it can generate more than one parse tree (or leftmost/rightmost derivation) for the same sentence, i.e., if the sentence has more than one possible interpretation according to the grammar rules.
- Ambiguous grammars are undesirable for compiler design because they can cause conflicts in the parsing process and lead to different meanings for the same program.
- Some examples of ambiguous grammars are:

  - The grammar for arithmetic expressions with + and * operators, where both operators have the same precedence and associativity. For example, the sentence `a+b*c` can be parsed as `(a+b)*c` or `a+(b*c)`.
  - The grammar for if-then-else statements, where the else clause can be associated with the nearest or the farthest if statement. For example, the sentence `if a then if b then c else d` can be parsed as `if a then (if b then c else d)` or `if a then (if b then c) else d`.
  - The grammar for dangling else problem, where the else clause can be associated with any unmatched if statement. For example, the sentence `if a then if b then c; else d;` can be parsed as `if a then (if b then c; else d;)` or `if a then (if b then c;); else d;`.

- To handle ambiguous grammars, we can use one of the following methods:

  - Modify the grammar to make it unambiguous, i.e., to ensure that each sentence has a unique parse tree. For example, we can introduce parentheses to disambiguate arithmetic expressions, or use end-if markers to disambiguate if-then-else statements.
  - Use a parser that can resolve the ambiguity based on some rules, such as precedence and associativity of operators, or the nearest-else rule. For example, we can use an LR parser that can handle shift/reduce or reduce/reduce conflicts in the parsing table of ambiguous grammars.



### An automatic parser generator for the notes of the Unit 2 - Basic Parsing Techniques in the subject of Compiler Design

- A parser is a program that analyzes the syntactic structure of a given input according to a given grammar.
- A parser generator is a tool that takes a grammar as input and automatically generates source code that can parse streams of characters using the grammar.
- A parser generator can save time and effort for compiler developers by automating the tedious and error-prone task of writing a parser by hand.
- A parser generator can also ensure that the generated parser is correct and efficient, as well as consistent with the grammar specification.
- Some examples of parser generators are YACC, ANTLR, LALR, and Exabeam's Auto Parser Generator.
- YACC is a parser generator that produces LALR(1) parsers, which can handle a large class of context-free grammars.
- ANTLR is a parser generator that produces LL(*) parsers, which can handle recursive-descent parsing with arbitrary lookahead.
- LALR is a parser generator that produces LALR(k) parsers, which are a generalization of LALR(1) parsers that can handle more grammars by using more lookahead symbols.
- Exabeam's Auto Parser Generator is a tool that provides security engineers an easy operation for creating, customizing, modifying, and validating parsers for various log sources.
- Basic parsing techniques include top-down parsing and bottom-up parsing, which differ in the direction of the derivation of the input.
- Top-down parsing starts from the start symbol of the grammar and tries to match the input by expanding the nonterminals into terminals.
- Bottom-up parsing starts from the input and tries to reduce the terminals into nonterminals until the start symbol is reached.
- Top-down parsing is easier to implement and understand, but it may encounter left recursion or ambiguity problems.
- Bottom-up parsing is more powerful and can handle a larger class of grammars, but it is more complex and requires more memory and computation.



### Implementation of LR Parsing Tables

- LR parsing tables are a two-dimensional array in which each entry represents an action or a goto entry.
- LR parsing tables are used to guide the LR parser to perform the correct action (shift, reduce, accept or error) based on the current state and the next input symbol.
- LR parsing tables consist of two parts: the action part and the goto part.
  - The action part has columns for lookahead terminal symbols and rows for parser states. It specifies what action the parser should take when it encounters a terminal symbol in the input buffer.
  - The goto part has columns for nonterminal symbols and rows for parser states. It specifies what state the parser should go to after reducing by a production with a nonterminal symbol on the left-hand side.
- LR parsing tables can be constructed by using different algorithms, such as SLR, CLR or LALR.
  - SLR stands for Simple LR, which is the easiest and most cost-effective to implement, but it fails to handle some classes of grammars that have shift-reduce or reduce-reduce conflicts.
  - CLR stands for Canonical LR, which is the most powerful and can handle all LR(k) grammars, but it generates a large number of states and a large parsing table.
  - LALR stands for Lookahead LR, which is a compromise between SLR and CLR, and can handle most of the grammars that CLR can, but with a smaller number of states and a smaller parsing table.
- LR parsing tables can be constructed by using the following steps:
  - Step 1: Construct the augmented grammar by adding a new start symbol and a new production for it.
  - Step 2: Construct the canonical collection of LR(0) items by applying the closure and goto operations on the augmented grammar.
  - Step 3: Construct the action and goto functions based on the LR(0) items and the lookahead symbols.
  - Step 4: Construct the LR parsing table by filling the entries according to the action and goto functions.
  - Step 5: Check for any conflicts in the LR parsing table and resolve them if possible.



## Unit 3 - Syntax-directed Translation

- Syntax-directed translation is a technique for translating the source program into the target program using the syntax and semantic information of the source language.
- Syntax-directed translation can be performed at compile time or at run time, depending on the implementation strategy.
- Syntax-directed translation can be divided into two phases: synthesis and analysis.
  - Synthesis is the process of constructing the target program from the bottom up, using the attributes and actions associated with the grammar rules of the source language.
  - Analysis is the process of checking the validity and meaning of the source program from the top down, using the attributes and actions associated with the grammar symbols of the source language.
- Syntax-directed translation can be implemented using two data structures: syntax trees and annotated parse trees.
  - A syntax tree is a tree representation of the derivation of the source program, where each node corresponds to a grammar symbol and each leaf corresponds to a token.
  - An annotated parse tree is a syntax tree augmented with the attribute values and actions for each node, which are computed during the parsing process.
- Syntax-directed translation can be classified into two types: S-attributed and L-attributed.
  - S-attributed translation is a type of syntax-directed translation where the attribute values depend only on the values of the children nodes or the lexical value of the node itself.
  - L-attributed translation is a type of syntax-directed translation where the attribute values depend on the values of the left siblings, the children nodes, or the lexical value of the node itself.
- Syntax-directed translation can be used for various purposes, such as type checking, intermediate code generation, code optimization, and code generation.



### Syntax-directed Translation schemes for the notes of the Unit 3 - Syntax-directed Translation in the subject of Compiler Design

- Syntax-directed translation is a technique of compiler execution, where the source code translation is totally conducted by the parser, using a context-free grammar and a set of semantic rules or actions  .
- A syntax-directed translation scheme is a notation in which each production of a context-free grammar is associated with a set of semantic rules or actions, and each grammar symbol is associated with a set of attributes .
- Attributes are values that are computed at the nodes of the parse tree or syntax tree by visiting them in some order. Attributes can be classified into two types: synthesized and inherited  .
- Synthesized attributes are attributes that are computed at a node from the attribute values of its children  . For example, the attribute `val` of a node `N` can be computed as `val(N) = val(left child of N) + val(right child of N)`.
- Inherited attributes are attributes that are computed at a node from the attribute values of its parent and siblings  . For example, the attribute `type` of a node `N` can be computed as `type(N) = type(parent of N)`.
- A syntax-directed definition (SDD) is a collection of semantic rules that specify how to compute the attribute values for each grammar symbol . An SDD can be represented by annotating each production with the semantic rules that are executed when that production is used .
- A syntax-directed translation scheme (SDTS) is a context-free grammar where semantic rules are embedded within the right sides of productions . In the parse tree, the order in which actions appear is the order in which they are executed . An SDTS can be converted to an SDD by moving the actions to the end of the productions and assigning the results to attributes.
- A translation scheme can be classified into two types: postfix and prefix. A postfix translation scheme is one where the actions are placed after the grammar symbols in the productions. A prefix translation scheme is one where the actions are placed before the grammar symbols in the productions.
- A postfix translation scheme can be implemented by a bottom-up parser, such as a shift-reduce parser, that executes the actions as soon as the corresponding grammar symbols are popped from the parser stack. A prefix translation scheme can be implemented by a top-down parser, such as a recursive-descent parser, that executes the actions as soon as the corresponding grammar symbols are pushed onto the parser stack.
- A translation scheme can be used to generate intermediate code for the source program by using actions that emit code fragments or instructions . For example, the action `E.code = E1.code || gen('+' || E2.addr)` can be used to generate code for the expression `E -> E1 + E2`, where `E.code` is the code for `E`, `E1.code` is the code for `E1`, `E2.addr` is the address of `E2`, and `gen` is a function that generates a new instruction.



### Implementation of Syntax-Directed Translators

- Syntax-directed translation is a method of compiler implementation where the source language translation is completely driven by the parser.
- A syntax-directed translation scheme is a context-free grammar with attributes and semantic actions associated with the grammar symbols and productions.
- Attributes are values computed at the nodes of the parse tree or syntax tree by visiting them in some order.
- Semantic actions are subroutines that are invoked by the parser at the appropriate time for translation.
- There are two types of attributes: synthesized and inherited.
  - Synthesized attributes are computed from the attributes of the children nodes or the node itself.
  - Inherited attributes are computed from the attributes of the parent node or the siblings nodes.
- There are two types of syntax-directed translation schemes: postfix and prefix.
  - Postfix schemes have semantic actions at the end of the productions.
  - Prefix schemes have semantic actions at the beginning of the productions.
- Syntax-directed translators can be implemented by using one of the following methods:
  - Constructing an explicit parse tree or syntax tree and then traversing it in some order to evaluate the attributes and execute the semantic actions.
  - Evaluating the attributes and executing the semantic actions during parsing without constructing an explicit tree.
  - Using a parser stack to store the attributes and semantic actions and performing them in a postfix order.



### Intermediate code for the notes of the Unit 3 - Syntax-directed Translation in the subject of Compiler Design

- Intermediate code is a form of representation of the source program that is easier to translate into the target machine code.
- Intermediate code eliminates the need of a new full compiler for every unique machine by keeping the analysis portion same for all the compilers. The second part of compiler, synthesis, is changed according to the target machine.
- Intermediate code can be either language-specific (e.g., Bytecode for Java) or language-independent (three-address code).
- The following are commonly used intermediate code representations:
  - Postfix Notation: Also known as reverse Polish notation or suffix notation. The ordinary (infix) way of writing the sum of a and b is with an operator in between: a + b. In postfix notation, the operator follows the operands: a b +. This notation eliminates the need for parentheses and precedence rules.
  - Syntax Trees: A syntax tree is a graphical representation of the abstract syntax of the source program. The leaves of the tree are the operands and the internal nodes are the operators. The order of evaluation is determined by the structure of the tree.
  - Three-address Code: A three-address code is a linearized representation of a syntax tree, where each statement has at most three operands. An operand can be a constant, a variable, a temporary variable, or a pointer to a memory location. A statement can have the form x = y op z, where op is a binary operator, or x = op y, where op is a unary operator, or x = y, where y is assigned to x. A statement can also have the form goto L, where L is a label, or if x goto L, where the control is transferred to L if x is true, or ifFalse x goto L, where the control is transferred to L if x is false, or param x, where x is a parameter for a procedure call, or call p, n, where p is the name of the procedure and n is the number of parameters, or return x, where x is the value returned by the procedure.
- The intermediate code generator takes the output of the syntax analyzer (parse tree or abstract syntax tree) and produces the intermediate code as output.
- The intermediate code generator can use syntax-directed translation to generate the intermediate code. Syntax-directed translation is a method of translating the source program into the intermediate code by attaching semantic rules to the grammar productions. The semantic rules can be either synthesized attributes or inherited attributes. Synthesized attributes are computed from the attributes of the children nodes, while inherited attributes are computed from the attributes of the parent or sibling nodes.
- The intermediate code generator can also use translation schemes to generate the intermediate code. A translation scheme is a context-free grammar with semantic actions embedded within production bodies. The semantic actions are executed whenever the corresponding production is used during the syntax analysis. The semantic actions can generate the intermediate code or manipulate a symbol table.
- The intermediate code generator can also use intermediate representations based on graphs, such as control-flow graphs, data-flow graphs, or dependence graphs. These graphs can capture the flow of control, data, or dependence among the statements of the source program. These graphs can be used for various code optimization techniques.



### Postfix Notation

- Postfix notation is a way of writing expressions where the operator appears after the operands, i.e., the operator between operands is taken out and is attached after operands.
- For example, the infix expression `a * d - (b + c)` can be written in postfix notation as `a d * b c + -`.
- Postfix notation is also known as reverse Polish notation or suffix notation.
- Postfix notation has some advantages over infix notation, such as:
  - It does not require parentheses to specify the order of evaluation.
  - It is easier to parse for a machine, as there is no need to consider operator precedence or associativity.
  - It can be evaluated using a stack data structure, where operands are pushed onto the stack and operators pop and apply to the topmost operands.
- Postfix notation can be used in intermediate code generation in compiler design, as it is a convenient and compact representation of expressions .
- To convert an infix expression to postfix notation, one can use the following algorithm:
  - Scan the infix expression from left to right.
  - If the scanned symbol is an operand, output it.
  - If the scanned symbol is an opening parenthesis, push it onto the stack.
  - If the scanned symbol is a closing parenthesis, pop and output symbols from the stack until an opening parenthesis is encountered. Discard the pair of parentheses.
  - If the scanned symbol is an operator, then:
    - If the stack is empty or the top of the stack is an opening parenthesis, push the operator onto the stack.
    - If the operator has higher precedence than the top of the stack, push the operator onto the stack.
    - If the operator has lower or equal precedence than the top of the stack, pop and output symbols from the stack until the stack is empty or the top of the stack has lower precedence than the operator. Then push the operator onto the stack.
  - After scanning the infix expression, pop and output any remaining symbols from the stack.



### Parse trees and syntax trees

- Parse trees and syntax trees are data structures that represent the syntactic structure of a source code in compiler design.
- A parse tree is generated by the parser, which is a component of the compiler that processes the source code and checks it for syntactic correctness.
- A syntax tree is an abstract or compact representation of a parse tree, which removes some unnecessary details and focuses on the essential information for semantic analysis and code generation.
- The main differences between parse trees and syntax trees are:

  - Parse trees show the complete derivation of the source code according to the grammar rules, while syntax trees only show the relevant syntactic categories and operators.
  - Parse trees include all the tokens and punctuation marks in the source code, while syntax trees omit them and only show the identifiers and literals.
  - Parse trees reflect the precedence and associativity of the operators in the source code, while syntax trees use the tree structure to indicate them.
  - Parse trees are usually larger and more complex than syntax trees, which makes them harder to manipulate and process.

- The main advantages of using syntax trees over parse trees are:

  - Syntax trees are more concise and easier to understand than parse trees, which helps in debugging and optimizing the compiler.
  - Syntax trees are more suitable for semantic analysis and code generation, as they contain only the information that is relevant for these tasks.
  - Syntax trees can be easily transformed and manipulated by applying various rules and algorithms, such as constant folding, dead code elimination, and code optimization.

- An example of a parse tree and a syntax tree for the expression `a + b * c` is shown below:

  - Parse tree:

```
    E
   / \
  E   + T
 / \    / \
T   * F  F  F
|   | |  |  |
a   b c  ( d + e )
```

  - Syntax tree:

```
    +
   / \
  a   *
     / \
    b   c
```



### Three Address Code for the Notes of the Unit 3 - Syntax-directed Translation in the Subject of Compiler Design

- Three address code is a type of intermediate code which is easy to generate and can be easily converted to machine code.
- It makes use of at most three addresses and one operator to represent an expression and the value computed at each instruction is stored in temporary variable generated by compiler.
- The three address code for an expression of the form `A := B op C` is: `t1 := B op C; A := t1` where `t1` is a temporary variable.
- Syntax-directed translation is a method of translating a source program into a target program using the syntax and semantic information of the source language.
- It is based on the idea of attaching semantic actions to the productions of a context-free grammar and executing them during the parsing process.
- Syntax-directed translation can be used to generate intermediate code for various applications, such as arithmetic expressions, infix to postfix conversion, binary to decimal conversion, syntax tree construction, etc.
- There are three ways to represent a three-address code in compiler design: quadruples, triples, and indirect triples.
- Quadruples are a table of four columns, where the first column contains the operator, the second and third columns contain the operands, and the fourth column contains the result.
- Triples are a table of three columns, where the first column contains the operator, the second and third columns contain the operands, and the result is implicitly represented by the row number.
- Indirect triples are a table of two columns, where the first column contains a pointer to the row number of the corresponding triple, and the second column contains the result.
- An example of three-address code representation for the expression `a + b * c + d` is:

| Quadruples | Triples | Indirect Triples |
|------------|---------|------------------|
| * | b | c | t1 | (0) * | b | c | (0) | 0 | t1 |
| + | a | t1 | t2 | (1) + | a | (0) | (1) | 1 | t2 |
| + | t2 | d | t3 | (2) + | (1) | d | (2) | 2 | t3 |

: Types of Three-address codes - GeeksforGeeks
: Intermediate Code Generation in Compiler Design - GeeksforGeeks
: Application of Syntax Directed Translation - GeeksforGeeks
: Three address code in Compiler - GeeksforGeeks



### Quadruples and Triples in Compiler Design

- Quadruples and triples are two ways of representing three-address code in compiler design.
- Three-address code is an intermediate code that is generated by the syntax-directed translation of a source program.
- Three-address code consists of a sequence of statements, each of which has at most one operator and three operands.
- The operands can be constants, variables, or temporary names that hold intermediate results.
- Quadruples and triples are used to store the three-address code in a tabular form, which can be easily manipulated by the compiler for optimization and code generation.

#### Quadruples

- A quadruple is a structure that has four fields: op, arg1, arg2, and result.
- The op field denotes the operator of the statement, such as +, -, *, /, =, etc.
- The arg1 and arg2 fields denote the two operands of the statement, which can be constants, variables, or temporary names.
- The result field denotes the name of the temporary variable that holds the result of the statement.
- For example, the statement x = y + z can be represented by the quadruple:

| op | arg1 | arg2 | result |
|----|------|------|--------|
| +  | y    | z    | t1     |

- And the statement w = x + 1 can be represented by the quadruple:

| op | arg1 | arg2 | result |
|----|------|------|--------|
| +  | x    | 1    | t2     |

- And the statement w = w + 1 can be represented by the quadruple:

| op | arg1 | arg2 | result |
|----|------|------|--------|
| +  | w    | 1    | w      |

- The advantage of quadruples is that they are easy to rearrange for global optimization, as each statement has a unique result name.
- The disadvantage of quadruples is that they may require more space than triples, as they introduce more temporary names.

#### Triples

- A triple is a structure that has three fields: op, arg1, and arg2.
- The op field denotes the operator of the statement, such as +, -, *, /, =, etc.
- The arg1 and arg2 fields denote the two operands of the statement, which can be constants, variables, or temporary names.
- The result of the statement is not stored in a separate field, but rather in the same place as one of the operands.
- For example, the statement x = y + z can be represented by the triple:

| op | arg1 | arg2 |
|----|------|------|
| +  | y    | z    |

- And the statement w = x + 1 can be represented by the triple:

| op | arg1 | arg2 |
|----|------|------|
| +  | x    | 1    |

- And the statement w = w + 1 can be represented by the triple:

| op | arg1 | arg2 |
|----|------|------|
| +  | w    | 1    |

- The advantage of triples is that they save some space compared to quadruples, as they do not introduce extra temporary names.
- The disadvantage of triples is that they are harder to rearrange for global optimization, as the result of a statement may be overwritten by another statement.



### Translation of Assignment Statements

- Translation of assignment statements is a process of generating intermediate code or target code for the assignment statements in a source program.
- Assignment statements are mainly used to assign values to variables or data structures, such as arrays and records.
- The syntax and semantics of assignment statements may vary depending on the source language and the target language.
- A common way to translate assignment statements is to use syntax-directed translation, which is a technique of attaching semantic actions to the grammar rules of a context-free grammar.
- Syntax-directed translation can be implemented by using a parse tree or an abstract syntax tree (AST) to represent the structure and meaning of the source program.
- A parse tree is a tree that shows how a string of tokens is derived from the start symbol of a grammar by applying the grammar rules.
- An abstract syntax tree is a simplified version of a parse tree that omits the unnecessary details and focuses on the essential syntactic constructs of the source program.
- The semantic actions are usually written as code fragments that are executed during the parsing or traversal of the tree.
- The semantic actions can perform various tasks, such as type checking, symbol table management, intermediate code generation, and optimization.
- The intermediate code or target code can be represented in different forms, such as postfix notation, three-address code, quadruples, triples, or indirect triples.
- The choice of the intermediate code or target code representation depends on the characteristics of the source language and the target language, as well as the design goals of the compiler.
- The following example shows how to translate an assignment statement of the form x = y + z, where x, y, and z are integer variables, into three-address code.

```
Grammar rule: S -> id = E
Semantic action: generate (id.place = E.place)

Grammar rule: E -> E1 + E2
Semantic action: t = newtemp()
               generate (t = E1.place + E2.place)
               E.place = t

Grammar rule: E -> id
Semantic action: E.place = id.place
```

- The parse tree and the corresponding three-address code for the assignment statement x = y + z are shown below.

```
          S
        / | \
       /  |  \
      /   |   \
     /    |    \
    /     |     \
   /      |      \
  /       |       \
id        =        E
|                /   \
x               /     \
              E1       E2
             /         /
            /         /
           id        id
           |         |
           y         z

Three-address code:

t1 = y + z
x = t1
```



### Boolean expressions for the notes of the Unit 3 - Syntax-directed Translation in the subject of Compiler Design

- Boolean expressions are expressions that evaluate to either true or false values, such as `x > y`, `a && b`, or `!c`.
- Boolean expressions are used to control the flow of execution of conditional statements, such as `if-else` and `while-do`, and to generate intermediate code for them.
- Syntax-directed translation is a technique to attach semantic actions to the grammar rules of a language and to perform them during parsing.
- Syntax-directed translation can be done by constructing a parse tree or a syntax tree and computing the values of attributes at the nodes of the tree by visiting them in some order, such as depth-first or breadth-first.
- Syntax-directed translation can also be done by embedding the semantic actions within the grammar rules and performing them during parsing, without building an explicit tree. This is called a syntax-directed translation scheme.
- A syntax-directed translation scheme can be used to evaluate the order of semantic rules and to generate intermediate code for boolean expressions and control statements.
- For example, consider the following grammar for boolean expressions:

```
E -> E1 or E2
E -> E1 and E2
E -> not E1
E -> (E1)
E -> true
E -> false
```

- A syntax-directed translation scheme for this grammar can be written as follows, where `||` denotes concatenation, `newlabel()` generates a new label, and `emit()` generates a three-address code:

```
E -> E1 or {E.true = newlabel();
            E.false = E2.false;
            emit('goto' || E.true);
            emit(E1.false || ':');} E2
E -> E1 and {E.true = E2.true;
             E.false = newlabel();
             emit('goto' || E.false);
             emit(E1.true || ':');} E2
E -> not {E.true = E1.false;
          E.false = E1.true;} E1
E -> (E1) {E.true = E1.true;
           E.false = E1.false;}
E -> true {E.true = newlabel();
           E.false = 0;
           emit(E.true || ':');}
E -> false {E.true = 0;
            E.false = newlabel();
            emit(E.false || ':');}
```

- The translation scheme generates intermediate code that uses labels to jump to the true or false branches of the boolean expression, depending on the evaluation of the subexpressions.
- The translation scheme can be extended to handle control statements, such as `if-else` and `while-do`, by using the following grammar rules and semantic actions:

```
S -> if E then S1
S -> if E then S1 else S2
S -> while E do S1

S -> if E then {S.next = newlabel();
                emit('goto' || S.next);
                emit(E.false || ':');} S1
S -> if E then {S.next = newlabel();
                emit('goto' || S.next);
                emit(E.false || ':');} S1 else {emit(E.true || ':');} S2
S -> while {S.begin = newlabel();
            emit(S.begin || ':');} E do {emit('goto' || S.begin);
                                         emit(E.false || ':');
                                         S1.next = S.begin;} S1
```

- The translation scheme generates intermediate code that uses labels to jump to the beginning or the end of the loop, or to the then or else branch of the conditional statement, depending on the evaluation of the boolean expression.



### Statements that alter the flow of control

- Statements that alter the flow of control are the statements that change the flow of execution of statements based on some conditions or iterations.
- Examples of statements that alter the flow of control are if, if-else, switch-case, while-do, for, break, continue, goto, etc.
- Statements that alter the flow of control can be classified into two types: selection statements and iteration statements.
- Selection statements are the statements that choose one of the possible paths of execution based on the value of a Boolean expression. Examples are if, if-else, switch-case, etc.
- Iteration statements are the statements that repeat a block of statements until a certain condition is met. Examples are while-do, for, do-while, etc.
- Statements that alter the flow of control can be represented by a control flow graph (CFG), which is a directed graph that shows the possible paths of execution of a program.
- A CFG consists of nodes and edges, where each node represents a basic block and each edge represents a possible transfer of control between basic blocks.
- A basic block is a sequence of statements such that it can be entered only at the beginning of the block and exited only at the end of the block.
- A CFG can be used to perform data flow analysis, which is a technique to collect information about the possible values of variables at different points in a program.
- Data flow analysis can be used to optimize the code by eliminating redundant computations, dead code, common subexpressions, etc.



### Postfix Translation

- Postfix translation is a technique of generating intermediate code in compiler design that uses a syntax-directed translation scheme with semantic actions at the end of the productions .
- Postfix translation is also known as postfix syntax-directed translation or postfix SDT.
- Postfix translation produces intermediate code in postfix notation, which is a way of writing expressions where the operator appears after the operands.
- Postfix notation is also called reverse Polish notation or RPN.
- Postfix notation has the advantage of being easy to evaluate by a stack machine, as it does not require parentheses or precedence rules.
- Postfix translation can be achieved by factoring the productions to eliminate left recursion and left factoring, and by inserting semantic actions to generate the intermediate code .
- Postfix translation can be implemented by using a bottom-up parser, such as a shift-reduce parser, or by using a top-down parser, such as a recursive-descent parser .
- Postfix translation can be illustrated by the following example :

  - Given the grammar for arithmetic expressions:

    ```
    E → E + T | T
    T → T * F | F
    F → (E) | id
    ```

  - The postfix translation scheme is obtained by factoring the grammar and adding semantic actions:

    ```
    E → TE'
    E' → +TE' {print('+')} | ε
    T → FT'
    T' → *FT' {print('*')} | ε
    F → (E) | id {print(id.lexeme)}
    ```

  - The postfix translation scheme can generate the following intermediate code for the input expression `a * (b + c)`:

    ```
    a
    b
    c
    +
    *
    ```



### Translation with a top down parser

- Translation is the process of mapping a string of symbols from one language to another, such as from source code to machine code.
- A top down parser is a type of parser that constructs a parse tree from the root node (the start symbol of the grammar) to the leaf nodes (the input symbols) by using leftmost derivation.
- A syntax-directed translation (SDT) is a method of translation that uses attributes attached to the nodes of the parse tree to pass information bottom-up and/or top-down.
- A top down parser can perform syntax-directed translation by using the following steps :
  - Define attributes for the non-terminals and terminals of the grammar.
  - Define semantic rules for each production of the grammar, which specify how to compute the attributes of the non-terminals from the attributes of the terminals and/or other non-terminals.
  - Implement the semantic rules as actions in the parser, which are executed when a production is applied during parsing.
  - Use the computed attributes to generate the output of the translation, such as code, intermediate representation, or data structure.
- An example of a top down parser with syntax-directed translation is a simple FTP client, where the parser accepts user commands and uses a syntax tree to store the information about the command and its arguments.
- The advantages of using a top down parser with syntax-directed translation are :
  - It is easy to implement by hand or by using a parser generator tool.
  - It can handle left recursion and left factoring in the grammar by using techniques such as elimination or transformation.
  - It can detect syntax errors early in the input string and report them with meaningful messages.
  - It can perform semantic analysis and translation in one pass, which reduces the memory and time requirements.
- The disadvantages of using a top down parser with syntax-directed translation are :
  - It may require backtracking or lookahead to resolve ambiguity or choose the correct production in the grammar, which can be inefficient or impractical.
  - It may not be able to handle some grammars that are not LL(k), which means that the parser cannot determine the next production to apply by looking at the next k symbols in the input string.
  - It may not be able to perform some types of translation that require more information than the attributes of the current node, such as type checking or code optimization.



### More about translation for the notes of the Unit 3 - Syntax-directed Translation in the subject of Compiler Design

- Syntax-directed translation is a method of compiler implementation where the source language translation is completely driven by the parser.
- It allows the compiler designer to define the generation of intermediate code directly in terms of the syntactic structure of the source language.
- It uses a context-free grammar with attributes and semantic actions associated with the grammar symbols and productions.
- Attributes are the values computed at the nodes of the parse tree or syntax tree, which represent some information about the source program.
- Semantic actions are the subroutines that are executed by the parser at the appropriate time for translation.
- There are two types of attributes: synthesized and inherited.
  - Synthesized attributes are the attributes that are computed at a node from the attribute values of its children.
  - Inherited attributes are the attributes that are computed at a node from the attribute values of its parent and siblings.
- There are two types of syntax-directed translation schemes: postfix and prefix.
  - Postfix schemes are the schemes where the semantic actions are placed at the end of the productions.
  - Prefix schemes are the schemes where the semantic actions are placed at the beginning of the productions.
- Syntax-directed translation can be implemented by either constructing an explicit parse tree or syntax tree and visiting the nodes in some order, or by performing the translation during parsing without building an explicit tree.
- The order of visiting the nodes of the tree depends on the type of attributes and the dependency graph of the attributes.
  - The dependency graph of the attributes is a directed graph that shows the dependencies among the attributes at each node.
  - If the attributes are only synthesized, then the nodes can be visited in a bottom-up order, such as postorder traversal.
  - If the attributes are both synthesized and inherited, then the nodes can be visited in a top-down order, such as preorder traversal, or a mixed order, such as inorder traversal.
- The translation during parsing can be done by using a parser stack that stores the attribute values and semantic actions along with the grammar symbols.
  - The parser stack can be manipulated by the semantic actions to perform the translation.
  - The translation during parsing can be done by either a top-down parser or a bottom-up parser.



### Array references in arithmetic expressions

- An array reference is an expression that refers to an element of an array by specifying its index or subscript.
- An array reference has an l-value, which is the address of the element in memory.
- To compute the l-value of an array reference, the compiler needs to know the base address of the array, the lower and upper bounds of the index, the width of each element, and the order of storage (row-major or column-major).
- The general formula for computing the l-value of an array reference A[i] is:

  - `base + (i - low) * width`
  - where `base` is the base address of the array, `low` is the lower bound of the index, and `width` is the width of each element.

- For multidimensional arrays, the formula is extended by multiplying the index of each dimension by the product of the widths of the lower dimensions, and adding them together. For example, for a two-dimensional array A[i][j], the formula is:

  - `base + (i - low1) * width1 * (high2 - low2 + 1) + (j - low2) * width2`
  - where `low1` and `high1` are the lower and upper bounds of the first dimension, `low2` and `high2` are the lower and upper bounds of the second dimension, `width1` is the width of each row, and `width2` is the width of each element.

- The compiler can generate code to evaluate the l-value of an array reference by using arithmetic instructions and memory operations. For example, for the array reference A[i][j], the compiler can generate the following code:

  - `t1 = i - low1`
  - `t2 = t1 * width1 * (high2 - low2 + 1)`
  - `t3 = j - low2`
  - `t4 = t3 * width2`
  - `t5 = t2 + t4`
  - `t6 = base + t5`
  - `t6` is the l-value of A[i][j]

- The compiler can also optimize the code by using constants and loop-invariant expressions. For example, if `low1`, `low2`, `width1`, `width2`, and `base` are constants, and `i` is loop-invariant, the compiler can generate the following code:

  - `t1 = i - low1`
  - `t2 = t1 * width1 * (high2 - low2 + 1)`
  - `t3 = base - low2 * width2 + t2`
  - `t4 = j - low2`
  - `t5 = t4 * width2`
  - `t6 = t3 + t5`
  - `t6` is the l-value of A[i][j]

- Array references in arithmetic expressions can be used as operands or as targets of assignments. For example, the statement `A[i][j] = B[i] + C[j]` can be translated as:

  - `t1 = i - low1`
  - `t2 = t1 * width1 * (high2 - low2 + 1)`
  - `t3 = base - low2 * width2 + t2`
  - `t4 = j - low2`
  - `t5 = t4 * width2`
  - `t6 = t3 + t5`
  - `t7 = i - lowB`
  - `t8 = t7 * widthB`
  - `t9 = baseB + t8`
  - `t10 = j - lowC`
  - `t11 = t10 * widthC`
  - `t12 = baseC + t11`
  - `t13 = M[t9]`
  - `t14 = M[t12]`
  - `t15 = t13 + t14`
  - `M[t6] = t15`
  - where `M` is the memory array, and `baseB`, `lowB`, and `widthB` are the base address, lower bound, and width of array B, and `baseC`, `lowC`, and `widthC` are the base address, lower bound, and width of array C.



### Procedures call for the notes of the Unit 3 - Syntax-directed Translation in the subject of Compiler Design

- Syntax-directed translation is a method of compiler implementation where the source language translation is completely driven by the parser .
- It allows the compiler designer to define the generation of intermediate code directly in terms of the syntactic structure of the source language.
- It uses a context-free grammar with semantic rules or actions associated with each production and attributes associated with each grammar symbol .
- The semantic rules or actions are executed when the corresponding production is used during parsing .
- The attributes are values computed by the semantic rules or actions and can be used to store information about the source program .
- The attributes can be classified into two types: synthesized and inherited .
- Synthesized attributes are computed at a node from the attribute values of its children .
- Inherited attributes are computed at a node from the attribute values of its parent and siblings .
- The general approach to syntax-directed translation is to construct a parse tree or syntax tree and compute the values of attributes at the nodes of the tree by visiting them in some order.
- In many cases, translation can be done during parsing without building an explicit tree.
- Syntax-directed translation can be used for various tasks in compiler design, such as type checking, intermediate code generation, symbol table management, etc.



### Declarations and Case Statements

Declarations and case statements are two important concepts in compiler design, especially in the intermediate code generation phase. Here are some points to note about them:

- Declarations are statements that provide the information about the name and type of data objects to the programming language translators. For example, `int x;` is a declaration that tells the compiler that `x` is an integer variable.
- Declarations can also specify the storage class, scope, and initial value of the data objects. For example, `static int y = 10;` is a declaration that tells the compiler that `y` is a static integer variable with an initial value of 10.
- As the sequence of declarations in a procedure or block is examined, the compiler can lay out storage for names local to the procedure. For example, the compiler can allocate memory addresses for the variables declared in the procedure or block.
- Case statements are statements that allow the execution of different branches of code based on the value of an expression. For example, `switch (x) { case 1: ...; break; case 2: ...; break; default: ...; break; }` is a case statement that executes different code blocks depending on the value of `x`.
- Case statements can be implemented in different ways by the compiler, such as:
  - By a sequence of conditional goto statements, if the number of cases is small. For example, `if (x == 1) goto L1; if (x == 2) goto L2; goto L3; L1: ...; goto L4; L2: ...; goto L4; L3: ...; L4: ...;` is a possible implementation of the previous case statement using conditional goto statements.
  - By creating a table of pairs, with each pair consisting of a value and a label for the code of the corresponding statement. For example, `table: (1, L1), (2, L2), (default, L3); index = 0; while (index < table.size) { if (x == table[index].value) goto table[index].label; index = index + 1; } goto L3; L1: ...; goto L4; L2: ...; goto L4; L3: ...; L4: ...;` is a possible implementation of the previous case statement using a table of pairs.
  - By using a hash function to map the values to the labels, if the values are sparse. For example, `hash: (1, L1), (2, L2), (default, L3); label = hash(x); goto label; L1: ...; goto L4; L2: ...; goto L4; L3: ...; L4: ...;` is a possible implementation of the previous case statement using a hash function.
- Case statements can also have some restrictions or extensions depending on the programming language. For example, some languages do not allow declarations with initializers inside case statements, while some languages allow multiple values for a single case. For example, `switch (x) { case 1, 2: ...; break; case 3, 4: ...; break; default: ...; break; }` is a possible case statement with multiple values for a single case.



## Unit 4 - Symbol Tables

- A symbol table is a data structure that stores information about the identifiers (symbols) used in a program, such as variables, constants, functions, etc.
- A symbol table is usually implemented as a hash table, a binary search tree, or a linked list, depending on the trade-off between search time and insertion time.
- A symbol table supports the following operations:
  - **insert(symbol, attributes)**: adds a new symbol and its associated attributes to the table, or updates the attributes of an existing symbol.
  - **lookup(symbol)**: returns the attributes of a symbol, or null if the symbol is not in the table.
  - **delete(symbol)**: removes a symbol and its attributes from the table, if it exists.
- A symbol table is used by a compiler or an interpreter to perform various tasks, such as:
  - **lexical analysis**: the process of converting a sequence of characters into a sequence of tokens, each token representing a symbol.
  - **syntax analysis**: the process of checking if the tokens form a valid sentence according to the grammar rules of the language.
  - **semantic analysis**: the process of checking if the tokens have a meaningful interpretation according to the context and the rules of the language.
  - **code generation**: the process of translating the tokens into executable instructions for a target machine or platform.
- A symbol table may have different scopes, depending on the visibility and lifetime of the symbols. For example:
  - **global scope**: the symbols are visible and accessible throughout the entire program.
  - **local scope**: the symbols are visible and accessible only within a specific block or function.
  - **nested scope**: the symbols are visible and accessible within a block or function and its inner blocks or functions.
- A symbol table may have different levels, depending on the abstraction and granularity of the symbols. For example:
  - **source level**: the symbols are the identifiers used in the source code, such as variable names, function names, etc.
  - **intermediate level**: the symbols are the identifiers used in an intermediate representation of the code, such as abstract syntax tree nodes, three-address code instructions, etc.
  - **target level**: the symbols are the identifiers used in the target code, such as registers, memory addresses, labels, etc.



### Data structure for symbol tables

- A symbol table is an important data structure created and maintained by compilers in order to store information about the occurrence of various entities such as variable names, function names, objects, classes, interfaces, etc.  
- A symbol table is used by both the analysis and the synthesis parts of a compiler. 
- A symbol table is a data structure that maps symbols to their attributes, such as name, type, scope, value, etc.   
- A symbol table can be implemented using various data structures, such as arrays, linked lists, hash tables, binary search trees, etc.   
- The choice of data structure for symbol table depends on various factors, such as the number of symbols, the frequency of lookup and insertion operations, the size of the symbol table, the scope of the symbols, etc.   
- A compiler maintains two types of symbol tables: a global symbol table which can be accessed by all the procedures and scope symbol tables that are created for each scope in the program. 
- To determine the scope of a name, symbol tables are arranged in a hierarchical structure as shown in the example below: 

```
Global Symbol Table
|
|---- Scope Symbol Table 1
|     |
|     |---- Scope Symbol Table 2
|     |
|     |---- Scope Symbol Table 3
|
|---- Scope Symbol Table 4
      |
      |---- Scope Symbol Table 5
```

- A symbol table can also be organized in a linear or a nested structure, depending on the language features and the compiler design.  
- A symbol table supports various operations, such as creation, insertion, lookup, deletion, modification, etc.   
- A symbol table is essential for semantic analysis, code generation, and optimization phases of a compiler.



### Representing Scope Information

- Scope is the region of the program where a name (identifier) is valid and can be used to refer to a declared entity.
- A symbol table is a data structure that stores information about the names and their associated entities in a program.
- A symbol table should be able to handle the following tasks related to scope:
  - Insert a name and its attributes into the symbol table when a declaration is encountered.
  - Look up a name and retrieve its attributes when a reference is encountered.
  - Delete a name and its attributes from the symbol table when the scope of the name ends.
- There are different ways to represent scope information in a symbol table, depending on the scoping rules of the language and the structure of the program.
- Some common methods are:
  - Linear list: A single symbol table is used for the entire program. Each entry has a field to indicate the scope of the name. This method is simple but inefficient for large programs with nested scopes.
  - Nested list: A symbol table is created for each scope in the program. Each table has a pointer to its parent table, forming a tree structure. This method allows fast lookup of names in the current scope, but requires traversing the tree to find names in outer scopes.
  - Hash table: A hash function is used to map names to buckets in a symbol table. Each bucket contains a list of entries with the same hash value. Each entry has a field to indicate the scope of the name. This method allows fast insertion and lookup of names, but requires handling of collisions and rehashing when the table grows or shrinks.
  - Stack: A stack of symbol tables is maintained, where each table corresponds to a scope in the program. A new table is pushed onto the stack when a new scope is entered, and popped off the stack when the scope is exited. This method allows easy insertion and deletion of names, but requires searching the stack from top to bottom to find names in outer scopes.



### Run-Time Administration for the notes of the Unit 4 - Symbol Tables in the subject of Compiler Design

- Run-time administration is the process of managing the memory and other resources needed by a program during its execution.
- Run-time administration involves the following tasks:
  - Allocating and de-allocating memory for variables, arrays, records, objects, etc.
  - Maintaining information about the scope and lifetime of variables and procedures.
  - Implementing parameter passing mechanisms and return values for procedures.
  - Handling dynamic memory allocation and garbage collection for heap-allocated objects.
  - Supporting run-time checks and exceptions for errors such as array bounds violation, division by zero, etc.
- Run-time administration is closely related to the design of the symbol table, which is a data structure that stores information about the names and attributes of the entities in a program, such as variables, constants, types, procedures, etc.
- The symbol table is used by the compiler to perform semantic analysis, type checking, code generation, and optimization.
- The symbol table is also used by the run-time system to access and manipulate the entities in the program during execution.
- The symbol table can be organized in different ways, such as linear lists, hash tables, trees, etc.
- The symbol table can also be divided into different levels or scopes, such as global, local, nested, etc.
- The symbol table can also be augmented with additional information, such as offsets, addresses, registers, etc., to facilitate code generation and run-time administration.
- The run-time system can use different techniques to implement run-time administration, such as static allocation, stack allocation, heap allocation, etc.
- Static allocation is the technique of allocating memory for variables and procedures at compile time, based on their size and scope. Static allocation is simple and efficient, but does not support dynamic features such as recursion, dynamic arrays, etc.
- Stack allocation is the technique of allocating memory for variables and procedures at run time, using a data structure called the stack. The stack grows and shrinks as procedures are called and returned, and variables are created and destroyed. Stack allocation supports recursion, local variables, parameter passing, etc., but has limited size and requires stack discipline.
- Heap allocation is the technique of allocating memory for variables and procedures at run time, using a data structure called the heap. The heap is a pool of free memory that can be allocated and de-allocated as needed. Heap allocation supports dynamic features such as dynamic arrays, objects, closures, etc., but requires more memory management and may cause fragmentation and garbage collection issues.



### Implementation of simple stack allocation scheme

- Stack allocation is a runtime storage management technique for the compiler  whereby activation records are pushed and popped onto the stack as activations begin and end by use of predefined routines in the compiler.
- Activation records are data structures that contain information about the execution of a procedure, such as parameters, local variables, return address, etc.
- Stack allocation allows recursive procedures, since each activation of a procedure has its own activation record on the stack.
- Stack allocation is simple and efficient, but it has some limitations, such as:
  - It requires that the lifetime of a procedure activation is nested within the lifetime of its caller, which may not be the case for some languages that allow non-local references or dynamic scoping.
  - It does not support dynamic allocation of variable-length data, such as arrays or strings, within activation records, since the size of the activation record must be known at compile time.
  - It leads to variable-size stack frames, which require both stack and frame pointers to be managed, adding some overhead to the execution.
- To implement stack allocation, the compiler needs to generate code for the following tasks:
  - Allocate space for the activation record on the stack when a procedure is called, by decrementing the stack pointer by the size of the activation record.
  - Store the parameters, return address, and old frame pointer in the activation record, and set the new frame pointer to point to the top of the stack.
  - Access the local variables and parameters within the activation record, by using offsets from the frame pointer.
  - Deallocate space for the activation record on the stack when a procedure returns, by restoring the old frame pointer and incrementing the stack pointer by the size of the activation record.
  - Retrieve the return address and the return value from the activation record, and jump to the caller.



### Storage allocation in block structured language

- A block is a program segment that contains data declarations. There can be nested blocks. Uses dynamic memory allocation.
- A block structured language like ALGOL, and PL/I permit adjustable arrays, i.e., of varying length. Therefore, we cannot store irregular size arrays in between activation records. It can allocate the flexible or variable arrays at one corner of the activation record or above the fixed-size data.
- The storage is allocated sequentially in the stack beginning at one end. Storage should be freed in the reverse order of allocation so that a block of storage being released is always at the top of the stack. A program consists of data and procedures.
- The storage is released when the block is exited. If the block is a procedure that is invoked recursively, the previously allocated storage is pushed down upon entry; the latest allocation of storage is popped up in a recursive procedure when each generation terminates.
- The conventional storage allocation scheme for block structured languages requires the allocation of stack space and the building of a display with each procedure call. Several techniques have been proposed for analyzing the call graph of a program that make it possible to eliminate these operations from many call sequences.
- A new scheme for reducing storage allocation overhead is to use a static analysis of the program to determine the maximum amount of stack space needed by each procedure and to allocate it once at the beginning of the program execution. This scheme also eliminates the need for a display by using static links to access non-local variables.



### Error Detection and Recovery in Compiler Design

- Error detection is the process of locating and reporting any errors in the source program that violate the syntax and semantic rules of the language.
- Error recovery is the ability of the compiler to resume parsing of a program after detecting such errors while the compilation process .
- Errors may occur at various phases of compilation, such as lexical analysis, syntax analysis, semantic analysis, intermediate code generation, optimization, and code generation.
- Errors may be classified into four categories: lexical errors, syntactic errors, semantic errors, and logical errors.
- Lexical errors are caused by invalid characters, misspelled keywords, incorrect identifiers, etc. They are usually detected and reported by the lexical analyzer.
- Syntactic errors are caused by incorrect grammar, mismatched parentheses, missing semicolons, etc. They are usually detected and reported by the syntax analyzer or parser.
- Semantic errors are caused by invalid data types, undeclared variables, type mismatch, etc. They are usually detected and reported by the semantic analyzer or type checker.
- Logical errors are caused by incorrect algorithm, wrong assumptions, faulty logic, etc. They are usually not detected by the compiler, but by the programmer or the user during testing or execution.
- Error recovery strategies are the methods used by the compiler to handle the errors and continue the parsing process. There are mainly five error recovery strategies, which are as follows:
  - Panic mode: This strategy is used by most parsing methods. In this method of discovering the error, the parser discards input symbols one at a time until one of the designated set of synchronizing tokens is found. The synchronizing tokens are usually the delimiters, such as semicolons, commas, etc. This method is simple but may skip a large part of the input and may not report all the errors.
  - Phase level recovery: This strategy is used to confine the errors to a specific phase of the compiler. In this method, the compiler collects all the errors in a phase and reports them together at the end of the phase. This method avoids the cascading of errors from one phase to another, but may not be able to correct the errors within the phase.
  - Error productions: This strategy is used to handle the errors by modifying the grammar of the language. In this method, the compiler adds some error-handling productions to the grammar, which specify the common errors and their corrections. This method can correct the errors and resume the normal parsing, but may increase the complexity of the grammar and the parser.
  - Global correction: This strategy is used to find the minimal changes required to correct the errors in the input. In this method, the compiler uses some heuristics or algorithms to measure the distance between the erroneous input and the closest valid input, and then applies the changes to make the input valid. This method can produce the best correction, but may be very costly and time-consuming.
  - Symbol table: This strategy is used to handle the errors related to the symbol table, which stores the information about the identifiers, constants, types, etc. In this method, the compiler inserts, deletes, or modifies the entries in the symbol table to correct the errors. This method can avoid the semantic errors and generate the correct code, but may affect the scope and binding of the symbols.



### Lexical Phase Errors

- Lexical phase errors are errors that occur during the lexical analysis phase of the compiler, which is responsible for scanning the source code and generating tokens.
- A token is a sequence of characters that matches the pattern of a valid lexical unit, such as a keyword, an identifier, a constant, an operator, etc.
- A lexical error is a sequence of characters that does not match the pattern of any token, and therefore cannot be recognized by the lexical analyzer.
- Some examples of lexical errors are:
  - Invalid characters, such as @, #, $, etc. that are not part of the language syntax.
  - Exceeding the length of identifiers or numeric constants, such as a variable name that is too long or a number that is out of range.
  - Improperly formed strings or comments, such as missing quotes or delimiters, or nested comments.
  - Misspelled keywords, such as `wihle` instead of `while`, or `funtion` instead of `function`.
- Lexical errors can be detected and reported by the lexical analyzer, or by the parser, which is the next phase of the compiler that checks the syntax of the tokens.
- Some possible ways to handle lexical errors are:
  - Ignore the error and continue scanning the next character or token, such as skipping over invalid characters or truncating long identifiers or constants.
  - Replace the error with a valid token, such as correcting the spelling of keywords or inserting missing quotes or delimiters.
  - Insert a special error token into the token stream, such as `ERROR` or `INVALID`, and let the parser handle it later.
  - Abort the compilation process and display an error message, such as `Lexical error: invalid character @ at line 5, column 10`.



### Syntactic Phase Errors

- Syntactic errors are detected during the syntax analysis phase of the compiler, which checks if the input program conforms to the grammar rules of the source language.
- The general syntax errors are:
  - Structural errors: Missing operators, parentheses, semicolons, etc.
  - Mismatch errors: Mismatched data types, number of arguments, etc.
- Error recovery for syntactic phase errors can be done by various methods, such as:
  - Panic mode recovery: In this method, successive characters from the input are removed one at a time until a designated set of synchronizing tokens is found. Synchronizing tokens are delimiters such as `;` or `}`.
  - Phrase level recovery: In this method, the parser performs local correction on the remaining input, such as replacing, inserting, or deleting symbols.
  - Error productions: In this method, the grammar is augmented with special rules that generate erroneous constructs.
  - Global correction: In this method, the parser tries to find a sequence of minimal changes that can make the input string valid.
- Error reporting for syntactic phase errors should be informative and helpful for the user to fix the error. The error message should include the location, the nature, and the possible cause of the error.



### Semantic errors

Semantic errors are errors that arise when a statement used in a program is not meaningful, that is, it does not correspond to the set of rules (semantics) for that language being used. Semantic errors are detected by the semantic analyzer, which is a component of the compiler that checks the source code for meaningfulness and validity. Semantic errors can cause the program to behave incorrectly or produce unexpected results.

Some of the common types of semantic errors are:

- **Type mismatch**: This occurs when the data types of two operands or expressions are not compatible, such as adding a string and an integer. Some compilers can automatically perform type conversion to resolve this error, but others may require explicit type casting by the programmer.
- **Undeclared variables**: This occurs when a variable is used without being declared in the scope of the program. This can cause the compiler to treat the variable as a new identifier or generate an error message.
- **Reserved identifier misuse**: This occurs when a programmer uses a reserved word or symbol as an identifier, such as a variable name or a function name. Reserved words and symbols have special meanings in the language and cannot be used for other purposes.
- **Logic errors**: This occurs when a programmer writes code that fails to communicate its intended purpose, such as using the wrong operator, assigning the wrong value, or using the wrong loop condition. Logic errors are hard to detect by the compiler, because they do not violate the syntax or semantics of the language, but they can cause the program to produce incorrect or unexpected outputs.

To avoid semantic errors, a programmer should follow the rules and conventions of the language, use meaningful and consistent identifiers, declare and initialize variables properly, and test and debug the code carefully. Some of the semantic errors (the static semantic errors) are detected by the compiler, which generates a message indicating the type of error and the position in the source code where the error occurred (notice that the actual error could have occurred before the position signaled by the compiler). However, some semantic errors (the dynamic semantic errors) can only be detected at run time, such as division by zero, array out of bounds, or null pointer dereference. These errors can cause the program to crash or terminate abnormally. Therefore, a programmer should also use exception handling and error checking mechanisms to handle these errors gracefully.



## Unit 5 - Code Generation

- Code generation is the process of translating an intermediate representation of a source program into a target program that can be executed by a machine.
- Code generation can be divided into two phases: instruction selection and instruction scheduling.
- Instruction selection is the task of choosing the appropriate instructions from the target instruction set to implement the operations in the intermediate representation.
- Instruction scheduling is the task of ordering the instructions to optimize the performance of the target program, taking into account the dependencies, latencies, and resource constraints of the target machine.
- Code generation can be performed by different methods, such as template-based, peephole, and graph-based methods.
- Template-based methods use predefined patterns of instructions to match the operations in the intermediate representation and generate the corresponding target code.
- Peephole methods apply local optimizations to a stream of instructions by examining a small window of instructions (called a peephole) and replacing them with more efficient ones.
- Graph-based methods use data structures such as trees or graphs to represent the intermediate representation and the target instruction set, and apply graph algorithms to find the optimal mapping between them.



### Design Issues for Code Generation in Compiler Design

Code generation is the final phase of a compiler, which takes an intermediate representation of the source program and produces an equivalent target program. Code generation involves several design issues, such as:

- **Input to code generator**: The input to the code generator is the intermediate code generated by the front end, along with information in the symbol table that determines the run-time addresses of the data objects denoted by the names in the intermediate representation. The intermediate code can be in various forms, such as abstract syntax trees, three-address code, or stack-machine code. The choice of the intermediate code affects the complexity and efficiency of the code generator.
- **Target program**: The target program is the output of the code generator, which can be either assembly code or machine code. The target program should be correct, meaning that it should preserve the semantics of the source program. The target program should also be efficient, meaning that it should use the resources of the target machine, such as registers, memory, and instructions, in an optimal way. The target program should also be maintainable, meaning that it should be easy to understand and modify by human programmers or debuggers.
- **Instruction selection**: Instruction selection is the process of choosing the appropriate instructions from the target machine's instruction set to implement the operations in the intermediate code. Instruction selection can be done in various ways, such as using a simple one-to-one mapping, using macro expansion, using tree pattern matching, or using dynamic programming. The goal of instruction selection is to minimize the number of instructions and maximize the use of specialized instructions that can perform complex operations in one step.
- **Register allocation**: Register allocation is the process of assigning the temporary variables in the intermediate code to the registers in the target machine. Register allocation can be done in various ways, such as using a simple linear scan, using graph coloring, using linear programming, or using heuristic algorithms. The goal of register allocation is to minimize the number of register spills, which occur when a register is needed for a new variable but all the registers are already occupied and one of them has to be saved to memory and restored later.
- **Instruction ordering**: Instruction ordering is the process of arranging the instructions in the target program in a way that maximizes the performance of the target machine. Instruction ordering can be done in various ways, such as using basic blocks, using trace scheduling, using superblocks, or using hyperblocks. The goal of instruction ordering is to exploit the parallelism and pipelining features of the target machine, such as instruction-level parallelism, branch prediction, loop unrolling, or software pipelining.



### The Target Language for the notes of the Unit 5 - Code Generation in the subject of Compiler Design

- The target language is the language that the compiler generates as output from the source language. It can be machine code, assembly code, or another high-level language.
- The code generation phase of the compiler is responsible for translating the optimized intermediate code into the target language. It may perform some additional optimizations and transformations on the intermediate code to improve the quality and efficiency of the target code.
- The code generation phase typically involves the following tasks:
  - Register allocation: assigning variables and temporary values to registers or memory locations in the target machine.
  - Instruction selection: choosing the appropriate instructions and operands for each operation in the intermediate code.
  - Instruction scheduling: ordering the instructions to maximize the parallelism and minimize the stalls and dependencies in the target machine.
- The code generation phase may use different strategies and algorithms to perform these tasks, depending on the characteristics of the source language, the intermediate code, and the target machine. Some of the common strategies are:
  - Simple code generation: generating one instruction for each operation in the intermediate code, without any optimization or register allocation. This strategy is fast and easy to implement, but produces low-quality and inefficient target code.
  - Peephole optimization: applying local optimizations on a small window of instructions, such as eliminating redundant or unnecessary instructions, replacing expensive instructions with cheaper ones, or rearranging instructions to improve the code layout. This strategy can improve the target code quality and efficiency, but requires a careful design of the peephole rules and patterns.
  - DAG-based code generation: representing the intermediate code as a directed acyclic graph (DAG), where each node is an operation and each edge is a data dependency. This strategy can exploit the common subexpressions and eliminate the redundant computations in the intermediate code, as well as perform instruction selection and register allocation based on the DAG structure and properties. This strategy can produce high-quality and efficient target code, but requires a complex and sophisticated implementation.



### Addresses in the Target Code

- Addresses in the target code are the locations where the values of variables, constants, temporaries, and intermediate results are stored in the memory or registers of the target machine.
- Addresses in the target code can be classified into four categories:
  - Absolute addresses: These are the actual memory locations where the data is stored. For example, `x = 100` means that the value of x is stored at memory location 100.
  - Relative addresses: These are the offsets from a base address, such as the beginning of an activation record or a global data area. For example, `x = B + 4` means that the value of x is stored at four bytes after the base address B.
  - Register addresses: These are the names or numbers of the registers in the target machine. For example, `x = R1` means that the value of x is stored in register R1.
  - Indirect addresses: These are the addresses that point to other addresses where the data is stored. For example, `x = *p` means that the value of x is stored at the address pointed by p.
- Addresses in the target code are generated by the code generator, which is the final phase of the compiler. The code generator takes the optimized intermediate representation as input and produces the target code as output.
- The code generator uses registers to store the operands of the three-address statements, which are a form of intermediate code. The code generator decides the order of operations and the allocation of registers for the three-address statements.
- The code generator also handles the procedure calls and returns, which involve saving and restoring the return addresses, parameters, and local variables in the activation records. The code generator uses the stack pointer and the frame pointer to access the activation records.
- The code generator can perform some optimizations on the target code, such as eliminating redundant instructions, reducing memory accesses, and exploiting the features of the target machine.



### Basic Blocks and Flow Graphs

- A **basic block** is a set of statements that always executes in a sequence one after the other, without any branches or jumps  .
- A basic block has a single entry point and a single exit point. It means the flow of control enters at the beginning and leaves at the end of the block .
- A basic block can be identified by finding the **leaders** of the statements. A leader is the first statement of a basic block.
- The leaders are:
  - The first statement of the program.
  - Any statement that is the target of a jump or branch instruction.
  - Any statement that immediately follows a jump or branch instruction.
- A **flow graph** is a directed graph that represents the flow of control between basic blocks  .
- A flow graph has the following properties:
  - Each node in the graph corresponds to a basic block.
  - There is an edge from node X to node Y if the flow of control can transfer from the end of block X to the beginning of block Y.
  - The initial node has no incoming edges and the final node has no outgoing edges  .
- A flow graph is useful for code optimization and code generation, as it shows the dependencies and the order of execution of the basic blocks .
- An example of a basic block and a flow graph is shown below:

```
// A sequence of three-address code
a = b + c
d = a - b
if d == 0 goto L1
a = a + 1
goto L2
L1: d = b - c
L2: e = a + d
```

```
// The basic blocks are:

B1: a = b + c
    d = a - b
    if d == 0 goto L1

B2: a = a + 1
    goto L2

B3: d = b - c

B4: e = a + d

// The leaders are:

a = b + c // first statement of the program
if d == 0 goto L1 // target of a jump instruction
a = a + 1 // follows a jump instruction
d = b - c // target of a jump instruction
e = a + d // follows a jump instruction
```

```
// The flow graph is:

    B1
   /  \
  /    \
B2      B3
 \     /
  \   /
   B4
```



### Optimization of Basic Blocks

- Optimization is the process of improving the code by consuming fewer resources and delivering high speed.
- Optimization can be applied to the basic blocks after the intermediate code generation phase of the compiler.
- A basic block is a sequence of consecutive statements that has a single entry point and a single exit point.
- Optimization of basic blocks aims to eliminate redundant computations, simplify expressions, and use efficient instructions.
- There are two types of basic block optimizations:
  - Structure preserving transformations: These transformations do not change the structure of the basic block, but only replace some statements with equivalent ones. Examples are common subexpression elimination, copy propagation, dead code elimination, and constant folding.
  - Algebraic transformations: These transformations change the structure of the basic block by applying algebraic laws and identities. Examples are strength reduction, induction variable elimination, and code motion.
- To apply an optimization technique to a basic block, a directed acyclic graph (DAG) can be used. A DAG is a data structure that represents the expressions and dependencies in a basic block. A DAG can help to identify common subexpressions, eliminate redundant computations, and simplify expressions.



### Code Generator for the notes of the Unit 5 - Code Generation in the subject of Compiler Design

- Code generation is the final phase of compilation, where the intermediate representation of the source program is converted into the target program that can be executed by the machine.
- The code generator typically takes an abstract syntax tree or a parse tree as input and produces a linear sequence of instructions, usually in an intermediate language such as three-address code .
- The code generator performs three main tasks to convert the intermediate code into target code:
  - Instruction selection: choosing the appropriate instructions from the target machine's instruction set to implement the operations in the intermediate code.
  - Register allocation: assigning the variables and temporary values in the intermediate code to the available registers in the target machine.
  - Instruction scheduling: ordering the instructions to optimize the performance and reduce the latency of the target program.
- A simple code generator can be implemented using a recursive traversal of the abstract syntax tree, where each node corresponds to an operation or a variable in the intermediate code.
  - For each node, the code generator generates the instructions to evaluate its children and then performs the operation associated with the node.
  - The code generator also keeps track of the registers that are used and freed during the traversal, and uses a register allocation algorithm to assign registers to the variables and temporary values.
  - The code generator can also apply some local optimizations, such as eliminating redundant instructions, constant folding, and peephole optimization, to improve the quality of the target code.



### Code optimization for the notes of the Unit 5 - Code Generation in the subject of Compiler Design

- Code optimization is the process of improving the quality and efficiency of the generated code by applying various techniques at different stages of the compiler.
- Code optimization can be classified into two categories: machine-independent and machine-dependent.
- Machine-independent optimization is applied to the intermediate code and does not depend on the target architecture or instruction set.
- Machine-dependent optimization is applied to the object code and exploits the features and constraints of the target machine.
- Some of the common machine-independent optimization techniques are :
  - Compile time evaluation: evaluating constant expressions and folding them into a single value at compile time.
  - Constant propagation: replacing the use of a variable with its constant value if it is known at compile time.
  - Common subexpression elimination: eliminating redundant computations of the same subexpression and reusing the previously computed value.
  - Code movement: moving invariant code out of loops or conditional blocks to reduce the execution time.
  - Dead code elimination: removing code that does not affect the output or the program behavior, such as unreachable statements or unused variables.
  - Strength reduction: replacing expensive operations with cheaper ones, such as multiplication with addition or division with shift.
- Some of the common machine-dependent optimization techniques are:
  - Instruction selection: choosing the best instruction or sequence of instructions to implement an operation or a statement.
  - Instruction scheduling: reordering the instructions to avoid stalls and improve the utilization of the functional units.
  - Register allocation: assigning the variables and temporary values to the available registers to minimize the memory accesses.
  - Peephole optimization: applying local transformations to a small window of instructions to eliminate or simplify them.
- Code optimization can also be guided by the profile of the program execution, which provides information about the frequency and cost of different parts of the code.
- Profile-guided optimization (PGO) is a technique that uses the profile data to perform more accurate and effective optimizations, such as inlining, loop unrolling, branch prediction, etc.



### Machine-Independent Optimizations

Machine-independent optimizations are techniques that improve the quality of the intermediate code generated by the compiler, without considering the specific features of the target machine. The main goal of these optimizations is to reduce the execution time and/or the code size of the final program.

Some of the common machine-independent optimizations are:

- **Common subexpression elimination**: This technique avoids recomputing the same expression multiple times, by storing the result of the first computation and reusing it later. For example, if the expression `a + b` appears twice in the code, the compiler can generate code to compute it once and store it in a temporary variable, and then use that variable instead of recomputing `a + b` again.
- **Constant folding**: This technique evaluates constant expressions at compile time, and replaces them with their values. For example, if the expression `2 * 3 + 4` appears in the code, the compiler can replace it with `10`, which is the result of the evaluation.
- **Dead code elimination**: This technique removes code that is never executed, or has no effect on the output of the program. For example, if a variable is assigned a value but never used, or if a conditional statement is always true or false, the compiler can eliminate the redundant code.
- **Copy propagation**: This technique replaces the use of a variable with the value of another variable that has the same value. For example, if the statement `x = y` appears in the code, and `x` is used later, the compiler can replace `x` with `y`, which is the same value.
- **Code motion**: This technique moves code that is invariant (does not change) inside a loop, to outside the loop. This reduces the number of times the code is executed, and improves the performance of the loop. For example, if the expression `a + b` is invariant inside a loop, the compiler can move it outside the loop and store it in a temporary variable, and then use that variable inside the loop.



### Loop optimization

- Loop optimization is the process of increasing execution speed and reducing the overheads associated with loops .
- It plays an important role in improving cache performance and making effective use of parallel processing capabilities .
- Loop optimization can be viewed as the application of a sequence of specific loop transformations to the source code or intermediate representation, with each transformation having an associated test for legality.
- Some common loop transformations are  :
  - Loop invariant code motion: moving computations that do not depend on the loop iteration outside of the loop.
  - Loop unrolling: replicating the loop body multiple times to reduce the number of loop iterations and branch instructions.
  - Loop fusion: combining two or more loops that have the same iteration space into one loop to improve locality and reduce loop overheads.
  - Loop fission: splitting a loop into two or more loops that have the same iteration space but perform different computations to improve parallelism and cache utilization.
  - Loop interchange: changing the order of nested loops to improve locality and cache performance.
  - Loop tiling: dividing a loop into smaller subloops that operate on subarrays or submatrices to fit the cache size and improve locality.
  - Loop peeling: executing one or more iterations of a loop before or after the main loop to simplify the loop condition or enable other optimizations.
  - Loop reversal: changing the direction of a loop from increasing to decreasing or vice versa to enable other optimizations or simplify loop bounds.
  - Loop distribution: distributing a loop that performs multiple independent computations into several loops that perform one computation each to improve parallelism and locality.
  - Loop collapsing: transforming a nested loop into a single loop by using a single index variable to improve parallelism and reduce loop overheads.
  - Loop skewing: shifting the iteration space of a nested loop by a constant factor to eliminate or reduce loop-carried dependences and enable parallelization.
  - Loop alignment: aligning the loop iterations with the cache line boundaries to reduce cache misses and improve performance.
  - Loop vectorization: using vector instructions to perform multiple operations in parallel within a loop iteration to exploit data-level parallelism and improve performance.
  - Loop parallelization: using multiple threads or processes to execute different iterations of a loop in parallel to exploit task-level parallelism and improve performance.
- Loop optimization is usually performed by the compiler after analyzing the loop structure, data dependences, and memory access patterns  .
- Loop optimization can have significant impact on the performance, scalability, and energy efficiency of scientific and numerical applications that heavily rely on loops  .



### DAG representation of basic blocks

- A **directed acyclic graph (DAG)** is a graph that has no cycles and has a direction for each edge.
- A **basic block** is a sequence of statements that has a single entry point and a single exit point.
- A DAG can be used to represent the structure and the flow of values of a basic block in a compiler.
- A DAG can also be used to apply optimization techniques to a basic block, such as eliminating common subexpressions, dead code, and redundant calculations.
- To construct a DAG for a basic block, the following steps are followed:
  - The leaves of the DAG are labeled by unique identifiers, which can be variable names or constants.
  - The interior nodes of the DAG are labeled by operators, such as arithmetic, logical, or assignment operators.
  - The edges of the DAG represent the operands of the operators.
  - The order of evaluation of the nodes is determined by the topological sorting of the DAG, which is a linear ordering of the nodes such that for every edge from node u to node v, u comes before v in the ordering.
  - If a node has multiple parents, it means that it is a common subexpression, and it can be computed only once and reused later.
  - If a node has no parents, it means that it is a dead code, and it can be removed from the DAG.
- For example, consider the following basic block:

```c
a = b + c;
d = a - e;
f = b + c;
g = f - e;
```

- The DAG representation of this basic block is:

```
    -     -
   / \   / \
  +   e +   e
 / \   / \
b   c a   f
```

- In this DAG, we can see that:
  - The node labeled by + has two parents, which means that b + c is a common subexpression, and it can be computed only once and stored in a temporary variable, say t1.
  - The node labeled by a has no parents, which means that a = b + c is a dead code, and it can be removed from the DAG.
  - The node labeled by f has no parents, which means that f = b + c is a dead code, and it can be removed from the DAG.
  - The optimized basic block after applying the DAG representation is:

```c
t1 = b + c;
d = t1 - e;
g = t1 - e;
```



### Value Numbers and Algebraic Laws

- Value numbers are a technique for identifying and eliminating redundant computations in a program.
- A value number is a unique identifier assigned to each expression in a basic block, such that two expressions have the same value number if they are guaranteed to have the same value for all possible inputs.
- Value numbers can be computed using a hash-based algorithm or a partitioning algorithm, both of which traverse the dominator tree of the program and use a data structure to store the value numbers of expressions.
- Algebraic laws are rules that describe the properties of mathematical operations, such as commutativity, associativity, distributivity, identity, and inverse.
- Algebraic laws can be used to simplify expressions, rewrite expressions in a canonical form, and detect equivalent expressions.
- Algebraic laws can be applied to expressions before or after assigning value numbers, depending on the optimization goal and the complexity of the laws.
- Some examples of algebraic laws are:

  - x + 0 = x
  - x * 1 = x
  - x + y = y + x
  - x * y = y * x
  - (x + y) + z = x + (y + z)
  - (x * y) * z = x * (y * z)
  - x * (y + z) = x * y + x * z
  - x / x = 1
  - x - x = 0
  - x ^ 0 = 1
  - x ^ 1 = x
  - x ^ -1 = 1 / x



### Global Data-Flow Analysis for the Notes of the Unit 5 - Code Generation in the Subject of Compiler Design

- Global data-flow analysis is a technique to efficiently optimize the code by collecting and distributing information about the program to each block of the flow graph  .
- A flow graph is a representation of the control flow of a program, where each node is a basic block and each edge is a possible transfer of control.
- A basic block is a sequence of instructions that has a single entry point and a single exit point.
- Data-flow analysis is the analysis of the flow of data in the flow graph, i.e., the analysis that determines the information regarding the definition and use of data in the program.
- Data-flow analysis can help perform various optimizations, such as constant propagation, dead code elimination, common subexpression elimination, etc.
- Data-flow analysis can be classified into two types: forward and backward.
  - Forward analysis is when the information flows from the entry of the flow graph to the exit, following the direction of control flow.
  - Backward analysis is when the information flows from the exit of the flow graph to the entry, opposite to the direction of control flow.
- Data-flow analysis can also be classified into two types: local and global.
  - Local analysis is when the information is computed within each basic block, without considering the effects of other blocks.
  - Global analysis is when the information is computed across the basic blocks, taking into account the effects of other blocks.
- Global data-flow analysis requires solving a system of data-flow equations for each program point, which are derived from the data-flow properties of each instruction.
- Data-flow equations can be solved using iterative or non-iterative methods, such as fixed-point iteration, worklist algorithm, etc.
- Data-flow equations can be expressed using data-flow frameworks, which consist of four components: domain, direction, transfer function, and meet operator.
  - Domain is the set of possible values of the data-flow information.
  - Direction is the direction of the data-flow analysis, either forward or backward.
  - Transfer function is the function that computes the output data-flow information from the input data-flow information for each instruction.
  - Meet operator is the operator that combines the data-flow information from different paths for each program point.
- Data-flow frameworks can be categorized into four types: distributive, semi-distributive, non-distributive, and monotone.
  - Distributive frameworks are those where the meet operator distributes over the transfer function, i.e., meet(f(x), f(y)) = f(meet(x, y)) for any x and y in the domain.
  - Semi-distributive frameworks are those where the meet operator distributes over the transfer function for some but not all x and y in the domain.
  - Non-distributive frameworks are those where the meet operator does not distribute over the transfer function for any x and y in the domain.
  - Monotone frameworks are those where the meet operator is monotone, i.e., meet(x, y) ≤ x and meet(x, y) ≤ y for any x and y in the domain, where ≤ is a partial order relation.
- Some examples of global data-flow analysis are:
  - Reaching definitions: a forward, distributive, and monotone framework that computes for each program point the set of definitions that may reach that point.
  - Available expressions: a forward, distributive, and monotone framework that computes for each program point the set of expressions that are available at that point, i.e., they have been computed and not killed along all paths to that point.
  - Live variables: a backward, distributive, and monotone framework that computes for each program point the set of variables that are live at that point, i.e., they are used in some path from that point to the exit.
  - Very busy expressions: a backward, distributive, and monotone framework that computes for each program point the set of expressions that are very busy at that point, i.e., they are used in all paths from that point to the exit and not killed along any path.

