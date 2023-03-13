### Regular Expressions for the notes of the Unit 1 - INTRODUCTION in the subject of Natural Language Processing

- Regular expressions (RE) are a language for specifying text search strings.
- RE can help us to match or find other strings or sets of strings, using a specialized syntax held in a pattern.
- RE are useful for numerous practical day-to-day tasks that a data scientist encounters, such as data pre-processing, rule-based information mining systems, pattern matching, text feature engineering, web scraping, data extraction, etc.
- RE can be applied in many programming languages like Java, JS, php, C++, etc.
- RE are based on regular sets, which are sets of strings that can be defined by a finite number of rules.
- RE consist of literals (characters that match themselves) and metacharacters (characters that have special meanings and functions).
- Some common metacharacters are:

| Metacharacter | Meaning | Example |
| --- | --- | --- |
| . | Matches any single character except newline | a.c matches abc, a1c, a*c, etc. |
| ^ | Matches the start of the string | ^a matches any string that starts with a |
| $ | Matches the end of the string | a$ matches any string that ends with a |
| * | Matches zero or more occurrences of the preceding character | a* matches any string that contains zero or more a's |
| + | Matches one or more occurrences of the preceding character | a+ matches any string that contains one or more a's |
| ? | Matches zero or one occurrence of the preceding character | a? matches any string that contains zero or one a |
| [ ] | Matches a single character from a set of characters | [a-z] matches any lowercase letter |
| [^ ] | Matches a single character that is not in the set of characters | [^a-z] matches any character that is not a lowercase letter |
| \| | Matches either the expression before or the expression after | a\|b matches either a or b |
| ( ) | Groups a subexpression | (a+b)* matches any string that contains zero or more sequences of a's and b's |
| { } | Specifies the number of repetitions of the preceding character | a{3} matches exactly three a's |
| \ | Escapes the following character | \. matches a literal dot |

- Some examples of regular expressions and their corresponding regular sets are:

| Regular Expressions | Regular Set |
| --- | --- |
| (0 + 10*) | {0, 1, 10, 100, 1000, 10000, … } |
| (0*10*) | {1, 01, 10, 010, 0010, …} |
| (0 + ε) (1 + ε) | {ε, 0, 1, 01} |
| (a+b)* | It would be set of strings of a’s and b’s such as {ε, a, b, aa, ab, ba, bb, aaa, aab, aba, abb, baa, bab, bba, bbb, …} |

- Some mnemonics and learning tricks for regular expressions are:

  - Remember the acronym **DOS** for the three basic operations of regular expressions: **D**isjunction (**\|**), **O**ptionality (**?**) and **S**tar (**\***).
  - Use **[ ]** to match a single character from a range of characters, such as **[a-z]** for lowercase letters, **[0-9]** for digits, **[A-Za-z0-9]** for alphanumeric characters, etc.
  - Use **^** and **$** to anchor your regular expression to the start and end of the string, respectively. This can help you avoid unwanted matches in the middle of the string.
  - Use **\** to escape any metacharacter that you want to match literally, such as **\.** for a dot, **\\** for a backslash, **\*** for a star, etc.
  - Use **( )** to group subexpressions and apply operators to them, such as **(a+b)*c** to match any string that contains zero or more sequences of a's and b's followed by a c.