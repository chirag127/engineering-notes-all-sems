### c) Implementation of Calculator using LEX and YACC

LEX and YACC are tools used for generating lexical analyzers and parsers, respectively. They can be used to implement a calculator by following these steps:

1. Define the grammar for the calculator in YACC. This includes specifying the rules for mathematical expressions, such as the order of operations and the use of parentheses.
2. Write the lexical analyzer in LEX. This involves defining the tokens that the calculator will recognize, such as numbers and operators.
3. Use YACC to generate a parser based on the grammar defined in step 1. This parser will take the input from the user and convert it into a syntax tree.
4. Write the code to evaluate the syntax tree and perform the calculations. This can be done using a recursive function that traverses the tree and performs the appropriate operations.
5. Compile and run the calculator program.

By using LEX and YACC, the implementation of a calculator can be simplified and made more efficient. These tools automate the process of generating the lexical analyzer and parser, allowing the developer to focus on the logic of the calculator itself.