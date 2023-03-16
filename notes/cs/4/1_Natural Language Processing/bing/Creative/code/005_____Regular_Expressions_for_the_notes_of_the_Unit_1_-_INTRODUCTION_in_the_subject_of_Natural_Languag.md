### Regular Expressions for the notes of the Unit 1 - INTRODUCTION in the subject of Natural Language Processing

- A regular expression (RE) is a language for specifying text search strings.
- RE helps us to match or find other strings or sets of strings, using a specialized syntax held in a pattern.
- RE is very popular among programmers and can be applied in many programming languages like Java, JS, php, C++, etc.
- RE is useful for numerous practical day-to-day tasks that a data scientist encounters.
- RE is one of the key concepts of Natural Language Processing that every NLP expert should be proficient in.
- RE is used in various tasks such as data pre-processing, rule-based information mining systems, pattern matching, text feature engineering, web scraping, data extraction, etc.

#### Examples of Regular Expressions

| Regular Expressions | Regular Set |
| ------------------- | ----------- |
| (0 + 10*) | {0, 1, 10, 100, 1000, 10000, … } |
| (0*10*) | {1, 01, 10, 010, 0010, …} |
| (0 + ε) (1 + ε) | {ε, 0, 1, 01} |
| (a+b)* | It would be set of strings of a’s and b’s |

#### Simple Regular Expressions

- In this section we will see the building blocks for simple regular expressions, along with a selection of linguistic examples.
- A simple regular expression consists of a single character, such as `a`, or a single metacharacter, such as `.`.
- A metacharacter is a symbol that has a special meaning in a regular expression, such as matching any character, or repeating a pattern.
- Some common metacharacters are:

| Metacharacter | Meaning |
| ------------- | ------- |
| . | Matches any single character |
| * | Matches zero or more occurrences of the preceding character or expression |
| + | Matches one or more occurrences of the preceding character or expression |
| ? | Matches zero or one occurrence of the preceding character or expression |
| ^ | Matches the beginning of a string |
| $ | Matches the end of a string |
| [ ] | Matches any one of the characters inside the brackets |
| [^ ] | Matches any one of the characters not inside the brackets |
| ( ) | Groups a subexpression |
| \| | Matches either the expression before or the expression after the symbol |

- Some examples of simple regular expressions and their meanings are:

| Regular Expression | Meaning |
| ------------------ | ------- |
| `a*` | Matches zero or more `a`'s |
| `a+` | Matches one or more `a`'s |
| `a?` | Matches zero or one `a` |
| `a.b` | Matches any three-character string that begins with `a` and ends with `b` |
| `^a` | Matches any string that begins with `a` |
| `a$` | Matches any string that ends with `a` |
| `[abc]` | Matches any one of `a`, `b`, or `c` |
| `[^abc]` | Matches any one of not `a`, not `b`, or not `c` |
| `(ab)+` | Matches one or more occurrences of `ab` |
| `a|b` | Matches either `a` or `b` |