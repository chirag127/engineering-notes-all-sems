 Here is the content in Markdown format:

### Capabilities of CFG

1. CFGs can represent the syntax of all programming languages. Any language can be defined using a CFG.
2. CFGs are machine-independent and can be used to specify the syntax of languages that will be processed by compilers, interpreters, etc.
3. The syntax of a language defined by a CFG can be parsed by writing programs that construct a parse tree for an input string. This forms the basis of syntax-directed compiler design.
4. Ambiguities can be detected in the syntax defined by a CFG. An ambiguous grammar leads to multiple possible parse trees for some input strings which is undesirable.
5. Regular expressions can be converted into CFGs to define the lexical structure of a language. This provides a link between lexical and syntactic analysis.

[Insert diagrams/examples here if required]

Advantages: Precise way to specify syntax. Basis for parser design. Links lexical and syntactic analysis.
Disadvantages: Can be complex for large languages. Ambiguities may exist.
Applications: Specifying programming language syntax. Compiler design.

## Unit 2 - Basic Parsing Techniques

1. Top-down Parsing - Start with the root of the parse tree and expand non-terminals in a top-down fashion. Uses a predictive parsing table/LL(1) grammars.
2. Bottom-up Parsing - Start with input strings and reduce to higher-level structures. Uses LR parsers and handles a larger class of grammars than top-down parsing.
3. Recursive Descent Parsing - A type of top-down parsing with a procedural implementation of grammar rules.
4. LR Parsing - A type of bottom-up parsing using a parsing table to determine the appropriate action based on the current input token and stack top.
5. Operator Precedence Parsing - A technique to handle expressions with ambiguous grammars.

[Diagrams/Examples/Tables here if required]

[Similar advantages/disadvantages and applications as the previous section]