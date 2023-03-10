 Here is the content in markdown format:

#### CO2 Design Lexical analyser for given language using C and LEX /YACC tools K3, K5

1. Introduction
- A lexical analyser is a tool used to recognise lexemes (tokens) in input data. It breaks up the input into basic symbols (tokens) based on the rules of a language.
- LEX and YACC are tools used to generate lexical analysers and parsers. LEX is used to define patterns to recognise tokens and YACC is used to define grammar rules to build the parser.
- In this task, we have to design a lexical analyser for a given language using C and LEX/YACC tools to recognise the lexemes (tokens) in the input and classify them into different types.

2. Understanding the given language
- First, we need to understand the grammar of the given language and identify the tokens and their types in the language. Some sample inputs in the language will be provided to understand the language.
- Based on the grammar, we have to identify the token patterns and specify the token types like identifier, keyword, operator, integer constant, etc. This will be used to write LEX rules.

3. Writing LEX rules
- LEX rules are written to specify the token patterns. Each rule contains a regular expression pattern to match the token and C code to return the token type.
- For example, to match integers - [0-9]+ { return INT_CONST; }
- Rules can be added to match all the tokens in the given language. Start state and end state of LEX need to be defined.

4. Writing YACC rules
- YACC rules are used to define the grammar of the language in the form of parsing logic. It consists of grammar rules with tokens on LHS and productions on RHS.
- The tokens are separated bypipe (|) symbol to specify options. Precedence and associativity of operators can also be defined. The start symbol of the grammar is specified to start the parsing process.
- The LEX and YACC codes are run through C to generate the lexical analyser which can be used to recognise tokens in input data of the given language.

[Detailed explanations, diagrams, examples and codes can be added here]