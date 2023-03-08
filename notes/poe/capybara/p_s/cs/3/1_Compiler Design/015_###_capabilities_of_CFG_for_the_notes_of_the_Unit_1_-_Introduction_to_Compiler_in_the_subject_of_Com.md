### Capabilities of CFG for the notes of the Unit 1 - Introduction to Compiler in the subject of Compiler Design

Context-free grammars (CFG) are an essential tool in compiler design. CFG is a formalism that describes the syntax of a language. It is used to generate parsers, which are programs that read input code and generate an abstract syntax tree (AST) that represents the code structure. The capabilities of CFG are as follows:

- CFG can describe the syntax of programming languages: CFG is used to describe the syntax of programming languages. It defines the language structure and the rules that govern it. The syntax of programming languages can be described using a set of production rules. For example, the CFG for a simple arithmetic language might include rules for addition, subtraction, multiplication, and division.

- CFG can generate parsers: A parser is a program that reads input code and generates an AST. The parser uses the CFG to recognize the language syntax and build the AST. A parser can be generated automatically from a CFG using parser generators. Parser generators can take a CFG as input and generate a parser in a target programming language.

- CFG can handle recursive structures: CFG can handle recursive structures in a language. For example, a programming language may allow a function to call itself. The CFG for the language can handle this recursive structure by allowing a production rule to refer to itself.

- CFG can handle ambiguous grammars: CFG can handle ambiguous grammars. An ambiguous grammar is a grammar that can generate more than one parse tree for a sentence. In some cases, ambiguity can cause problems when generating code from the AST. However, there are techniques to resolve ambiguity, such as using precedence and associativity rules.

- CFG can handle left-recursive grammars: CFG can handle left-recursive grammars. A left-recursive grammar is a grammar where the left-hand side of a production rule can derive the same non-terminal symbol. Left-recursion can cause problems when generating parsers, but there are techniques to eliminate left-recursion, such as using left-factoring.

- CFG can handle context-sensitive languages: CFG can handle context-sensitive languages. A context-sensitive language is a language whose syntax depends on the context in which it appears. For example, a programming language may allow a variable to be declared before it is used. The CFG for the language can handle the context-sensitive nature of the language by incorporating semantic actions into the production rules.

In conclusion, CFG is an essential tool in compiler design, and it has several capabilities that make it suitable for describing the syntax of programming languages and generating parsers. It can handle recursive structures, ambiguous grammars, left-recursive grammars, and context-sensitive languages. These capabilities make CFG a powerful tool for compiler designers.