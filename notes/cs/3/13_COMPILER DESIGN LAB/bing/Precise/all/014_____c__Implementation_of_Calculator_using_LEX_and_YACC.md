### c) Implementation of Calculator using LEX and YACC

LEX and YACC are tools used for generating lexical analyzers and parsers, respectively. They can be used to implement a calculator by following these steps:

1. Define the grammar for the calculator: The first step in implementing a calculator using LEX and YACC is to define the grammar for the calculator. This includes specifying the valid expressions, operators, and operands that the calculator can handle.

2. Write the LEX specification: The next step is to write the LEX specification, which defines the rules for tokenizing the input. This includes specifying the regular expressions for recognizing the different tokens, such as numbers and operators.

3. Write the YACC specification: The YACC specification defines the grammar rules for parsing the input. This includes specifying the production rules for the different expressions and the actions to be taken when a rule is matched.

4. Generate the lexical analyzer and parser: Once the LEX and YACC specifications are written, the lexical analyzer and parser can be generated using the LEX and YACC tools.

5. Write the main program: The final step is to write the main program that uses the generated lexical analyzer and parser to evaluate the expressions entered by the user.

By following these steps, a calculator can be implemented using LEX and YACC. This approach allows for a flexible and modular implementation, as the grammar and parsing rules can be easily modified to support additional features or changes in the calculator's behavior.