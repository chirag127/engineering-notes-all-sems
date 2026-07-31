### Regular Expressions for the notes of the Unit 1 - INTRODUCTION in the subject of Natural Language Processing

- A regular expression (RE) is a language for specifying text search strings.
- RE helps us to match or find other strings or sets of strings, using a specialized syntax held in a pattern.
- RE are useful for numerous practical day-to-day tasks that a data scientist encounters, such as data pre-processing, rule-based information mining systems, pattern matching, text feature engineering, web scraping, data extraction, etc.
- RE can be applied in many programming languages like Java, JS, php, C++, etc.
- RE are based on regular sets, which are sets of strings that can be defined by a finite number of rules.
- Examples of regular sets are:

| Regular Expressions | Regular Set |
| ------------------- | ----------- |
| (0 + 10*) | {0, 1, 10, 100, 1000, 10000, … } |
| (0*10*) | {1, 01, 10, 010, 0010, …} |
| (0 + ε) (1 + ε) | {ε, 0, 1, 01} |
| (a+b)* | It would be set of strings of a’s and b’s |

- RE can be composed of simple symbols, such as letters, digits, or punctuation marks, and operators, such as +, *, ?, |, etc.
- Examples of RE operators are:

| Operator | Meaning |
| -------- | ------- |
| + | One or more occurrences of the preceding expression |
| * | Zero or more occurrences of the preceding expression |
| ? | Zero or one occurrence of the preceding expression |
| | | Alternation (either the expression before or after the operator) |
| () | Grouping (the expression inside the parentheses is treated as a unit) |
| [] | Character class (any one of the characters inside the brackets) |
| [^] | Negated character class (any one of the characters not inside the brackets) |
| . | Any single character (except newline) |
| ^ | Beginning of the string |
| $ | End of the string |
| \ | Escape character (used to indicate that the next character is not to be interpreted literally) |

- RE can be used to perform various tasks on natural language texts, such as:

  - Tokenization: splitting a text into smaller units, such as words, sentences, or phrases.
  - Stemming: reducing a word to its base or root form, such as removing suffixes or prefixes.
  - Lemmatization: finding the canonical or dictionary form of a word, such as finding the verb form of an inflected word.
  - Normalization: transforming a text into a standard or consistent form, such as converting case, spelling, or punctuation.
  - Filtering: removing unwanted or irrelevant parts of a text, such as stopwords, noise, or duplicates.
  - Extraction: identifying and extracting specific information from a text, such as names, dates, numbers, or keywords.
  - Validation: checking if a text conforms to a certain format or pattern, such as email addresses, phone numbers, or URLs.
  - Replacement: substituting parts of a text with other strings, such as correcting errors, anonymizing data, or generating variations.

- RE are powerful and flexible tools for natural language processing, but they also have some limitations, such as:

  - RE are not able to capture the meaning or semantics of natural language, only its surface form.
  - RE are not able to handle complex linguistic phenomena, such as ambiguity, context, or pragmatics.
  - RE are not able to deal with irregular or exceptional cases, such as idioms, slang, or neologisms.
  - RE are not able to learn from data or generalize to new cases, unlike machine learning or deep learning methods.