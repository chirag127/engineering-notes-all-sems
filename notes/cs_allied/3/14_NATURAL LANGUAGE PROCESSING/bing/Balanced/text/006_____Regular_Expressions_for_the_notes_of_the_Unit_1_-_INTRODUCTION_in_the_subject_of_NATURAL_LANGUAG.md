### Regular Expressions for the notes of the Unit 1 - INTRODUCTION in the subject of NATURAL LANGUAGE PROCESSING

- A regular expression (RE) is a language for specifying text search strings.
- RE helps us to match or find other strings or sets of strings, using a specialized syntax held in a pattern.
- RE is very popular among programmers and can be applied in many programming languages like Java, JS, php, C++, etc.
- RE is useful for numerous practical day-to-day tasks that a data scientist encounters, such as data pre-processing, rule-based information mining systems, pattern matching, text feature engineering, web scraping, data extraction, etc.
- RE is one of the key concepts of Natural Language Processing that every NLP expert should be proficient in.
- RE consists of a set of symbols and operators that define the rules for constructing valid expressions.
- Some of the common symbols and operators in RE are:

| Symbol | Meaning |
| --- | --- |
| . | Matches any single character |
| [ ] | Matches any character(s) inside the brackets |
| [^ ] | Matches any character(s) not inside the brackets |
| * | Matches zero or more occurrences |
| + | Matches one or more occurrences |
| ? | Matches zero or one occurrence |
| | | Matches a choice between the expressions on either side |
| ( ) | Groups the expression inside the parentheses |
| { } | Matches a specific number of occurrences |
| \ | Escapes a special character |

- Examples of RE and their corresponding regular sets are:

| RE | Regular Set |
| --- | --- |
| (0 + 10*) | {0, 1, 10, 100, 1000, 10000, … } |
| (0*10*) | {1, 01, 10, 010, 0010, …} |
| (0 + ε) (1 + ε) | {ε, 0, 1, 01} |
| (a+b)* | It would be set of strings of a’s and b’s such as {ε, a, b, aa, ab, ba, bb, aaa, aab, aba, abb, baa, bab, bba, bbb, …} |

- RE can be used for various NLP tasks, such as:

  - Tokenization: splitting a text into smaller units, such as words or sentences, using RE as delimiters.
  - Stemming: reducing a word to its base or root form, such as removing suffixes or prefixes, using RE as rules.
  - Normalization: transforming a text into a standard or canonical form, such as converting numbers, dates, abbreviations, etc., using RE as patterns.
  - Extraction: retrieving specific information from a text, such as names, entities, keywords, etc., using RE as filters.
  - Validation: checking if a text conforms to a certain format or structure, such as email addresses, phone numbers, URLs, etc., using RE as criteria.