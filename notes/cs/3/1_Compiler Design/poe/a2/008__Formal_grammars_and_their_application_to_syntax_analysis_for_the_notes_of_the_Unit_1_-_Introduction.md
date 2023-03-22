 Here is the content in formal tone without any emojis or external links in Markdown format:

### Formal grammars and their application to syntax analysis for the notes of the Unit 1 - Introduction to Compiler in the subject of Compiler Design:

1. A formal grammar is a set of rules that describe a language. It consists of the following components:
- A finite set of symbols called an alphabet.
- A finite set of production rules.
- A special symbol called the start symbol.

2. The production rules specify how symbols in the language can be combined to form strings (words) of the language. Each rule is of the form:
symbol → string

Where symbol is a symbol in the grammar and string is a sequence of symbols that symbol can be replaced by.

3. The start symbol is the symbol that can generate all strings in the language. The start symbol can be replaced by a string of symbols as per the production rules. Applying production rules recursively on the start symbol leads to all strings of the language.

4. A formal grammar can be used to recognize if a string is in the language or not. This is done using a parsing algorithm that applies production rules on the input string and checks if the start symbol can be derived from the input symbols. If possible, the string is in the language, else it is not. This process is called syntax analysis and is an integral part of a compiler.

5. Certain properties of formal grammars like ambiguity, left-recursion, etc. need to be checked before using the grammar for syntax analysis in a compiler. Appropriate transformations need to be applied to convert a grammar to a suitable normalized form for efficient implementation of the parser.

This concludes the key points on formal grammars and their application to syntax analysis for the given topic. Let me know if you would like me to elaborate on any of the points or modify/add any other content.