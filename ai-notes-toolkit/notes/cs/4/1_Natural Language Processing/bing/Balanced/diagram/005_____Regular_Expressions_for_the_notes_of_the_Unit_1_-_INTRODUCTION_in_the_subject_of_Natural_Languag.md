### Regular Expressions for the notes of the Unit 1 - INTRODUCTION in the subject of Natural Language Processing

- A regular expression (RE) is a language for specifying text search strings.
- RE helps us to match or find other strings or sets of strings, using a specialized syntax held in a pattern.
- RE is very popular among programmers and can be applied in many programming languages like Java, JS, php, C++, etc.
- RE is useful for numerous practical day-to-day tasks that a data scientist encounters, such as data pre-processing, rule-based information mining systems, pattern matching, text feature engineering, web scraping, data extraction, etc.
- RE is one of the key concepts of Natural Language Processing that every NLP expert should be proficient in.

#### Examples of Regular Expressions

| Regular Expressions | Regular Set |
| ------------------- | ----------- |
| (0 + 10*) | {0, 1, 10, 100, 1000, 10000, … } |
| (0*10*) | {1, 01, 10, 010, 0010, …} |
| (0 + ε) (1 + ε) | {ε, 0, 1, 01} |
| (a+b)* | It would be set of strings of a’s and b’s |

#### Simple Regular Expressions

- In this section we will see the building blocks for simple regular expressions, along with a selection of linguistic examples.
- A simple regular expression is a single character, such as `a` or `b`.
- A simple regular expression can also be a special character, such as `.` (any character), `^` (beginning of line), `$` (end of line), `\d` (digit), `\w` (word character), `\s` (whitespace), etc.
- A simple regular expression can be modified by a quantifier, such as `*` (zero or more), `+` (one or more), `?` (zero or one), `{n}` (exactly n), `{n,m}` (between n and m), etc.
- A simple regular expression can be combined with other simple regular expressions using operators, such as `|` (or), `()` (grouping), `[]` (character class), etc.

#### Examples of Simple Regular Expressions

| Regular Expressions | Description | Example |
| ------------------- | ----------- | ------- |
| `a*` | Zero or more occurrences of `a` | `""`, `"a"`, `"aa"`, `"aaa"`, etc. |
| `a+` | One or more occurrences of `a` | `"a"`, `"aa"`, `"aaa"`, etc. |
| `a?` | Zero or one occurrence of `a` | `""`, `"a"` |
| `a{3}` | Exactly three occurrences of `a` | `"aaa"` |
| `a{2,4}` | Between two and four occurrences of `a` | `"aa"`, `"aaa"`, `"aaaa"` |
| `a|b` | Either `a` or `b` | `"a"`, `"b"` |
| `(ab)+` | One or more occurrences of `ab` | `"ab"`, `"abab"`, `"ababab"`, etc. |
| `[aeiou]` | Any vowel | `"a"`, `"e"`, `"i"`, `"o"`, `"u"` |
| `[^aeiou]` | Any consonant | `"b"`, `"c"`, `"d"`, etc. |
| `.` | Any character | `"a"`, `"b"`, `"c"`, etc. |
| `^a` | `a` at the beginning of a line | `"a"`, `"ab"`, `"abc"`, etc. |
| `a$` | `a` at the end of a line | `"a"`, `"ba"`, `"cba"`, etc. |
| `\d` | Any digit | `"0"`, `"1"`, `"2"`, etc. |
| `\w` | Any word character | `"a"`, `"b"`, `"c"`, etc. |
| `\s` | Any whitespace | `" "`, `"\t"`, `"\n"`, etc. |