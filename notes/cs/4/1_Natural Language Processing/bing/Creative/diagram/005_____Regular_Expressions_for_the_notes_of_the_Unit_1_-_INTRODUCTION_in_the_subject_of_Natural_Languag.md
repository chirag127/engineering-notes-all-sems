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
- A simple regular expression is a single character, such as a, b, 0, 1, etc.
- A simple regular expression can also be a special character, such as ., *, +, ?, etc.
- The special characters have special meanings in regular expressions, as follows:

| Special Character | Meaning |
| ----------------- | ------- |
| . | Matches any single character |
| * | Matches zero or more occurrences of the preceding character |
| + | Matches one or more occurrences of the preceding character |
| ? | Matches zero or one occurrence of the preceding character |
| ^ | Matches the beginning of a string |
| $ | Matches the end of a string |
| [ ] | Matches any one of the characters inside the brackets |
| [^ ] | Matches any one of the characters not inside the brackets |
| ( ) | Groups a subexpression |
| \| | Matches either the expression before or the expression after |

#### Examples of Simple Regular Expressions

- The regular expression `a*` matches any string that consists of zero or more a's, such as "", "a", "aa", "aaa", etc.
- The regular expression `a+` matches any string that consists of one or more a's, such as "a", "aa", "aaa", etc.
- The regular expression `a?` matches any string that consists of zero or one a, such as "", "a".
- The regular expression `^a` matches any string that begins with an a, such as "a", "apple", "ant", etc.
- The regular expression `a$` matches any string that ends with an a, such as "a", "banana", "spa", etc.
- The regular expression `[ab]` matches any string that contains either an a or a b, such as "a", "b", "ab", "ba", "cab", etc.
- The regular expression `[^ab]` matches any string that contains neither an a nor a b, such as "c", "d", "cd", "xyz", etc.
- The regular expression `(ab)+` matches any string that contains one or more occurrences of the substring "ab", such as "ab", "abab", "ababab", etc.
- The regular expression `a|b` matches any string that contains either an a or a b, such as "a", "b", "ab", "ba", "cab", etc.