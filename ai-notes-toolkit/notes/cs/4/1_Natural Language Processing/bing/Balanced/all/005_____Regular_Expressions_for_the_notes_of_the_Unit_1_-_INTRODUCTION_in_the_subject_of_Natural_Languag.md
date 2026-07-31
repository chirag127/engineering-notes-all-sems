# Regular Expressions for the notes of the Unit 1 - INTRODUCTION in the subject of Natural Language Processing

- A regular expression (RE) is a language for specifying text search strings.
- RE helps us to match or find other strings or sets of strings, using a specialized syntax held in a pattern.
- RE is very popular among programmers and can be applied in many programming languages like Java, JS, php, C++, etc.
- RE is useful for numerous practical day-to-day tasks that a data scientist encounters, such as data pre-processing, rule-based information mining systems, pattern matching, text feature engineering, web scraping, data extraction, etc.
- RE is one of the key concepts of Natural Language Processing that every NLP expert should be proficient in.

## Examples of Regular Expressions

- Regular Expressions | Regular Set
- (0 + 10*) | {0, 1, 10, 100, 1000, 10000, … }
- (0*10*) | {1, 01, 10, 010, 0010, …}
- (0 + ε) (1 + ε) | {ε, 0, 1, 01}
- (a+b)* | It would be set of strings of a’s and b’s

## Simple Regular Expressions

- In this section, we will see the building blocks for simple regular expressions, along with a selection of linguistic examples.
- A simple regular expression consists of one or more of the following components:
  - A literal character, such as a, b, c, etc.
  - A wildcard character, such as ., which matches any single character
  - A character class, such as [a-z], which matches any character in the specified range
  - A negated character class, such as [^a-z], which matches any character not in the specified range
  - A repetition operator, such as *, +, ?, {n}, {n,m}, which specifies how many times the preceding component can be repeated
  - A grouping operator, such as ( ), which groups components together for applying repetition or alternation
  - An alternation operator, such as |, which matches either the component before or after it
  - An anchor, such as ^ or $, which matches the beginning or end of a string, respectively
- Some examples of simple regular expressions and their meanings are:
  - ^a.*b$ | matches any string that starts with a and ends with b
  - [A-Z][a-z]+ | matches any capitalized word
  - [^aeiou] | matches any consonant
  - (a|b)* | matches any string of a's and b's
  - \d{3}-\d{4} | matches any phone number of the form xxx-xxxx