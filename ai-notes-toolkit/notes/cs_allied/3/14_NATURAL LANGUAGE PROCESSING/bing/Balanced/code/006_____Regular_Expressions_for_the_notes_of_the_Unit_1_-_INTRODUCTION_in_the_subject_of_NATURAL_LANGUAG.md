### Regular Expressions for the notes of the Unit 1 - INTRODUCTION in the subject of NATURAL LANGUAGE PROCESSING

- A regular expression (RE) is a language for specifying text search strings.
- RE helps us to match or find other strings or sets of strings, using a specialized syntax held in a pattern.
- RE is very popular among programmers and can be applied in many programming languages like Java, JS, php, C++, etc.
- RE is useful for numerous practical day-to-day tasks that a data scientist encounters.
- RE is one of the key concepts of Natural Language Processing that every NLP expert should be proficient in.
- RE is used in various tasks such as data pre-processing, rule-based information mining systems, pattern matching, text feature engineering, web scraping, data extraction, etc.

- Examples of Regular Expressions:

| Regular Expressions | Regular Set |
| ------------------- | ----------- |
| (0 + 10*) | {0, 1, 10, 100, 1000, 10000, … } |
| (0*10*) | {1, 01, 10, 010, 0010, …} |
| (0 + ε) (1 + ε) | {ε, 0, 1, 01} |
| (a+b)* | It would be set of strings of a’s and b’s |

- The syntax of RE consists of the following elements:

| Element | Meaning |
| ------- | ------- |
| a | Matches the character a |
| . | Matches any character |
| [abc] | Matches any character in the set {a, b, c} |
| [a-z] | Matches any character in the range a to z |
| [^abc] | Matches any character not in the set {a, b, c} |
| [^a-z] | Matches any character not in the range a to z |
| a* | Matches zero or more occurrences of a |
| a+ | Matches one or more occurrences of a |
| a? | Matches zero or one occurrence of a |
| a{m} | Matches exactly m occurrences of a |
| a{m,} | Matches at least m occurrences of a |
| a{m,n} | Matches at least m and at most n occurrences of a |
| a|b | Matches either a or b |
| (a) | Matches a and captures it as a group |
| (?:a) | Matches a but does not capture it as a group |
| \n | Matches the nth captured group |
| \a | Matches the character a if it is a metacharacter |
| ^ | Matches the beginning of a string or line |
| $ | Matches the end of a string or line |
| \b | Matches a word boundary |
| \B | Matches a non-word boundary |
| \d | Matches any digit |
| \D | Matches any non-digit |
| \s | Matches any whitespace |
| \S | Matches any non-whitespace |
| \w | Matches any word character |
| \W | Matches any non-word character |