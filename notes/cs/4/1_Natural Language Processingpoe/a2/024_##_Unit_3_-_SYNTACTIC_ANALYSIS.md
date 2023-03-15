 Here is the content in markdown format for Unit 3 - SYNTACTIC ANALYSIS:

## Unit 3 - SYNTACTIC ANALYSIS

Syntactic analysis is the process of analyzing the source code of a program to determine its grammatical structure. It verifies that the input is correctly structured as per the rules of the programming language.

The key steps involved in syntactic analysis are:

1. Lexical analysis - Breaking up the input into meaningful symbols or tokens like identifiers, keywords, operators, literals, etc.

2. Creating a token stream - Arranging the tokens in the same order as they appeared in the input.

3. Writing grammar rules for the programming language - Defining the structure and composition rules for forming valid statements and expressions in the language. These rules are defined using a formal grammar.

4. Creating a parse table or parsing engine - Implementing the grammar rules in a table or engine to use them for syntax analysis.

5. Checking for syntax errors - Applying the grammar rules via the parsing engine to verify that the token stream adheres to the correct structure. Any violations result in syntax errors.

Some key points to remember:

- Syntax analysis is done after lexical analysis.
- Formal grammars like BNF are used to specify syntax rules.
- A parser is constructed to apply the grammar rules on the input and check for errors.
- Syntax errors are caught during compilation and the compiler reports them.
- The program is rejected if there are syntax errors.

Examples of syntax errors:

- Misspelled identifiers or keywords
- Missing semicolons at the end of statements
- Unbalanced parentheses, braces or brackets
- Operands of wrong type for an operator
- Missing operators

Applications of syntax analysis:

- Detecting errors in programming and scripting languages.
- Used in compilers, interpreters and linters to verify syntax.
- Used in software that needs to parse and process language-based input.
- Used in natural language processing to parse sentences and understand structure.

**Mnemonics:**

- "Tokens in a stream, grammar rules supreme" - Remember the key steps.
- "Syntax check's a must, else reject we must" - Syntax analysis is required to detect errors.