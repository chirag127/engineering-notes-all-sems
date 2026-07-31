 Here is a formal write-up on the topic "Implementation of Calculator using LEX and YACC" without any emojis or external links:

### c) Implementation of Calculator using LEX and YACC

1. LEX: LEX is a lexical analyzer generator. It is used to generate a program called a lexer that recognizes lexical patterns in text. The input to LEX is a set of regular expressions and C code snippets, and it produces as output a C program that recognizes those patterns.
2. YACC: YACC is a parser generator. It produces a parser, a program that can recognize syntactic patterns in strings. The input to YACC is a context-free grammar of the language it is to recognize, plus C code snippets, and it produces as output a C program that can recognize strings in that language.
3. Combining LEX and YACC: LEX and YACC can be combined to produce a compiler frontend that translates a textual input language into an internal representation that a backend can process further. LEX first breaks up the input into meaningful symbols, and then YACC groups the symbols into meaningful syntactic structures.
4. Calculator in LEX and YACC: To implement a calculator, the following steps can be followed:

a. Write regular expressions in LEX to recognize numbers, operators, parentheses, etc.
b. Write rules in YACC to specify the syntax of expressions. For example, a rule can be <expr> → <term> | <expr> + <term> to specify that an expression contains either a term or a term followed by + followed by another term.
c. Encode actions in YACC to compute the values of expressions. For each rule, C code can be written to evaluate the components of the rule and compute the result.
d. Handle precedence and associativity of operators in YACC. This can be done by assigning different precedences to different operators and using precedence rules.

e. The end result would be a calculator program that can evaluate mathematical expressions entered by a user.