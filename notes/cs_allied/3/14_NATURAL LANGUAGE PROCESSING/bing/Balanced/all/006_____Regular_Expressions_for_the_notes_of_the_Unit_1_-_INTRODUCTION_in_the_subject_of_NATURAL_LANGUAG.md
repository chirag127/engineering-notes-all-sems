# Regular Expressions for the notes of the Unit 1 - INTRODUCTION in the subject of NATURAL LANGUAGE PROCESSING

- A regular expression (RE) is a language for specifying text search strings.
- RE helps us to match or find other strings or sets of strings, using a specialized syntax held in a pattern.
- RE is very popular among programmers and can be applied in many programming languages like Java, JS, php, C++, etc.
- RE is one of the key concepts of Natural Language Processing that every NLP expert should be proficient in.
- RE is used in various tasks such as data pre-processing, rule-based information mining systems, pattern matching, text feature engineering, web scraping, data extraction, etc.

## Examples of Regular Expressions

- Regular Expressions | Regular Set
- (0 + 10*) | {0, 1, 10, 100, 1000, 10000, … }
- (0*10*) | {1, 01, 10, 010, 0010, …}
- (0 + ε) (1 + ε) | {ε, 0, 1, 01}
- (a+b)* | It would be set of strings of a’s and b’s

## Simple Regular Expressions

- In this section we will see the building blocks for simple regular expressions, along with a selection of linguistic examples.
- A simple regular expression consists of a single character, such as a, or a single metacharacter, such as ^ or $.
- A metacharacter is a character that has a special meaning in a regular expression, such as indicating the beginning or end of a line, or matching any character.
- Some common metacharacters are:

  - ^ : matches the beginning of a line
  - $ : matches the end of a line
  - . : matches any character
  - * : matches zero or more occurrences of the preceding character
  - + : matches one or more occurrences of the preceding character
  - ? : matches zero or one occurrence of the preceding character
  - [ ] : matches any character inside the brackets
  - [^ ] : matches any character not inside the brackets
  - | : matches either the expression before or the expression after
  - ( ) : groups expressions together
  - \ : escapes the following character, if it is a metacharacter

- Some examples of simple regular expressions and their meanings are:

  - ^a : matches any string that starts with a
  - a$ : matches any string that ends with a
  - .a : matches any string that has an a preceded by any character
  - a* : matches any string that has zero or more a's
  - a+ : matches any string that has one or more a's
  - a? : matches any string that has zero or one a
  - [abc] : matches any string that has an a, b, or c
  - [^abc] : matches any string that does not have an a, b, or c
  - a|b : matches any string that has either an a or a b
  - (ab)+ : matches any string that has one or more occurrences of ab