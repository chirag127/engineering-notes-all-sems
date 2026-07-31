 Here is the content in markdown format without any emojis or external links and in a formal tone:

### Lexical Phase errors for the notes of the Unit 4 - Symbol Tables in the subject of Compiler Design

1. Unknown symbols: If the input contains symbols that do not belong to the defined vocabulary (set of keywords, identifiers, operators, punctuation symbols) of the language, then lexical error occurs.
2. Illegal character sequences: If the input contains certain character sequences that are not permitted in the language, then lexical error occurs. For example, a floating point constant may contain only digits, decimal point and exponent. Presence of any other character will generate error.
3. String literals: If the string literals are not properly terminated or they contain certain escape sequences that are not defined for that particular language, then lexical error occurs.
4. Premature end of input: If the end of the input is encountered and some more characters were expected to form a valid lexeme, then lexical error occurs.
5. Identifiers: If the identifiers do not conform to the lexical rules regarding their formation, then lexical error occurs. For example, if the identifiers can contain only alphabets and digits, presence of any special symbol will generate error.
6. Keywords: If the reserved words (keywords) of the language are used as identifiers or vice versa, then lexical error occurs.
7. Numeric constants: If the numeric constants do not satisfy the syntactical rules of the language, then lexical error occurs. For example, if only decimal constants are allowed and the input contains hexadecimal constants, error will occur.

The above points cover the key types of lexical errors that can occur during the lexical analysis phase of a compiler. Proper error handling mechanisms should be incorporated to detect and deal with such errors.