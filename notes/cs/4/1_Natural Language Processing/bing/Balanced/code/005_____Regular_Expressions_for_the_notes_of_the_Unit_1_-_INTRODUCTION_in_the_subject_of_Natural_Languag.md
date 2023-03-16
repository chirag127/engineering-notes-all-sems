### Regular Expressions for the notes of the Unit 1 - INTRODUCTION in the subject of Natural Language Processing

- A regular expression (RE) is a language for specifying text search strings.
- RE helps us to match or find other strings or sets of strings, using a specialized syntax held in a pattern.
- RE is very popular among programmers and can be applied in many programming languages like Java, JS, php, C++, etc.
- RE is useful for numerous practical day-to-day tasks that a data scientist encounters, such as data pre-processing, rule-based information mining systems, pattern matching, text feature engineering, web scraping, data extraction, etc.
- RE is one of the key concepts of Natural Language Processing that every NLP expert should be proficient in.
- Some examples of regular expressions and their corresponding regular sets are:

| Regular Expressions | Regular Set |
| ------------------- | ----------- |
| (0 + 10*) | {0, 1, 10, 100, 1000, 10000, … } |
| (0*10*) | {1, 01, 10, 010, 0010, …} |
| (0 + ε) (1 + ε) | {ε, 0, 1, 01} |
| (a+b)* | It would be set of strings of a’s and b’s |

- The syntax of regular expressions consists of the following elements:

| Element | Description |
| ------- | ----------- |
| Literal characters | They match themselves exactly |
| . | It matches any single character except newline |
| [ ] | It matches any single character in brackets |
| [^ ] | It matches any single character not in brackets |
| ^ | It matches the beginning of a line |
| $ | It matches the end of a line |
| * | It matches 0 or more repetitions of the preceding expression |
| + | It matches 1 or more repetitions of the preceding expression |
| ? | It matches 0 or 1 repetitions of the preceding expression |
| {n} | It matches exactly n repetitions of the preceding expression |
| {n,} | It matches at least n repetitions of the preceding expression |
| {n,m} | It matches at least n and at most m repetitions of the preceding expression |
| a\|b | It matches either a or b |
| ( ) | It groups sub-expressions |
| \ | It escapes special characters |

- Some examples of using regular expressions for natural language processing are:

| Task | Regular Expression | Example |
| ---- | ------------------ | ------- |
| Finding phone numbers | \d{3}-\d{3}-\d{4} | 123-456-7890 |
| Finding email addresses | [\w.-]+@[\w.-]+ | john.doe@gmail.com |
| Finding dates | \d{1,2}/\d{1,2}/\d{2,4} | 12/31/2021 |
| Finding hashtags | #\w+ | #nlp |