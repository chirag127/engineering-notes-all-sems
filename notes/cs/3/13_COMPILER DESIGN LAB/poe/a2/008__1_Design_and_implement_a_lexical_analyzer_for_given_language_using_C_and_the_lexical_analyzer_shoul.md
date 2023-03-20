 Here is the formal content in Markdown format without any emojis or external links:

### 1.Design and implement a lexical analyzer for given language using C

1.  Lexical analysis is the first phase of a compiler. It breaks up input text into meaningful lexemes (tokens) by removing any whitespace or comments and checking for valid patterns.
2.  For a given programming language, define the tokens and corresponding regular expressions. For example, identifiers can be [a-zA-Z][a-zA-Z0-9]*, numbers can be [0-9]+, etc.
3.  Use flex or implement the scanner manually to match the input characters to the defined tokens and their regular expressions.
4.  The lexical analyzer should ignore redundant characters, whitespace, and comments as those do not contribute to the meaning. Only return the significant lexemes/tokens to the syntax analyzer.
5.  Test the lexical analyzer with sample inputs to ensure it is returning the correct tokens. Handle errors such as unmatched parentheses, identifiers with incorrect characters, etc.
6.  The output of the lexical analyzer is a stream of tokens with their attributes (type, value, line number, etc.) which serve as input to the syntax analyzer.

The above points cover the key steps to design and implement a lexical analyzer for a given programming language using C while ignoring redundant input. The lexical analyzer breaks up the input into meaningful tokens as per the defined patterns for the language.