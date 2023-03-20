 Here is the content in markdown format without emojis and external links:

### 2. Implementation of Lexical Analyzer using Lex Tool

1. Lex is a lexical analyzer generator tool. It takes input in the form of specification written in the lexer description language and produces C program to recognize lexical patterns in the input.
2. The lexer description has rules and patterns to identify tokens. A rule contains a regular expression and an action to be performed when the pattern is matched.
3. The lexical analyzer breaks the input into basic units called tokens and passes them to the parser. The tokens are identified using the rules and patterns defined in the lexer description.
4. Lex specification has 3 sections:
    - Definitions section: Macros and regex definitions are specified.
    - Rules section: Pattern rules are defined to identify tokens. Each rule has a regular expression and an action.
    - User subsection: C code to be included in the generated analyzer can be specified.
5. A Lex program is invoked by specifying the input Lex file. It generates a C file which can be compiled and linked to create an executable lexical analyzer.
6. The role of the lexical analyzer is to read the input stream of characters, identify the lexemes using the rules in the specification and return the corresponding tokens to the parser.

The content is written in points and markdown format without external links or emojis as per the instructions. Let me know if you would like me to modify or add any other points.