### BNF notation for the notes of the Unit 1 - Introduction to Compiler in the subject of Compiler Design

- BNF stands for **Backus Naur Form** notation  . It is a form of notation used for specifying the **syntax** of programming languages and other types of computer input .
- The syntax means the **structure of strings** in a certain language. For example, the syntax of a C program is defined by a set of rules that specify how to write valid statements, expressions, declarations, etc.
- BNF notation uses **symbols** and **rules** to define the syntax of a language . The symbols are divided into two categories: **terminals** and **non-terminals**.
- Terminals are the **basic symbols** of the language, such as keywords, operators, identifiers, literals, etc. They are usually written in **lowercase** or enclosed in **quotes**.
- Non-terminals are the **abstract symbols** that represent **syntactic categories** or **constructs** of the language, such as statements, expressions, declarations, etc. They are usually written in **uppercase** or enclosed in **angle brackets**.
- Rules are the **productions** that specify how non-terminals can be **derived** from terminals and other non-terminals . They have the form:

  `NON-TERMINAL ::= ALTERNATIVE1 | ALTERNATIVE2 | ... | ALTERNATIVEN`

  where `::=` means **is defined as**, `|` means **or**, and each alternative is a **sequence** of terminals and non-terminals.

- For example, the following rule defines the syntax of a simple arithmetic expression:

  `EXPR ::= TERM | EXPR "+" TERM | EXPR "-" TERM`

  This means that an expression can be either a term, or an expression followed by a plus sign and a term, or an expression followed by a minus sign and a term.

- BNF notation is a type of **context-free grammar** (CFG), which means that the syntax of a language can be defined **independently** of the context or meaning of the symbols  .
- BNF notation is also a **metasyntax**, which means that it is a **syntax for syntax**. It is used to describe the syntax of other languages, not itself.
- BNF notation has many **variants** and **extensions**, such as **extended BNF** (EBNF), **labeled BNF** (LBNF), **augmented BNF** (ABNF), etc. They introduce additional symbols and conventions to make the notation more **concise**, **expressive**, or **compatible** with different languages .