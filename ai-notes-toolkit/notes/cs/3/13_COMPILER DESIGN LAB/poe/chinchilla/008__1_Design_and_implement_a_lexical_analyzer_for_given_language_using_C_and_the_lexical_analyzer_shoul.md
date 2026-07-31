### 1. Design and Implement a Lexical Analyzer for Given Language using C and the Lexical Analyzer should Ignore Redundant

A lexical analyzer is an important component of a compiler that breaks down the source code into a sequence of tokens or lexemes. These tokens are then passed on to the parser for further processing. In this article, we will discuss the design and implementation of a lexical analyzer for a given language using C programming language. The lexical analyzer should also ignore redundant tokens.

Here are the steps to design and implement a lexical analyzer:

1. Define the Tokens: The first step is to define the tokens or lexemes of the language. Tokens are the basic building blocks of the language and represent the smallest unit of meaning. For example, in C language, the tokens include keywords (like if, else, for), identifiers (like variable names), constants (like 1, 2.2, 'c'), operators (like +, -, *, /), and punctuations (like ;, ()). 

2. Write Regular Expressions: Once we have defined the tokens, the next step is to write regular expressions for each token. Regular expressions are patterns that match a specific set of characters. For example, the regular expression for a variable name in C language could be [a-zA-Z][a-zA-Z0-9]*. 

3. Implement the Lexical Analyzer: Now that we have the tokens and regular expressions, we can implement the lexical analyzer. The lexical analyzer reads the input source code character by character and matches the characters against the regular expressions to identify the tokens. If a character does not match any regular expression, it is considered a redundant token and is ignored. The lexical analyzer then returns the sequence of tokens to the parser.

4. Handle Edge Cases: It is important to handle edge cases while implementing the lexical analyzer. For example, if there is a comment in the source code, the lexical analyzer should ignore it. Similarly, if there are whitespace characters between tokens, they should be ignored as well.

In conclusion, designing and implementing a lexical analyzer for a given language using C programming language requires defining the tokens and writing regular expressions for each token. The lexical analyzer should also be able to ignore redundant tokens and handle edge cases like comments and whitespace characters. By following these steps, we can design and implement an efficient lexical analyzer for any programming language.