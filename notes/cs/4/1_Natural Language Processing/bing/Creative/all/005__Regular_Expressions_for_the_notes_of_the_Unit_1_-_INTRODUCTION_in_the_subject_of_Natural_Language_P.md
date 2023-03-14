### Regular Expressions for the notes of the Unit 1 - INTRODUCTION in the subject of Natural Language Processing

- Regular expressions (RE) are a language for specifying text search strings. RE help us to match or find other strings or sets of strings, using a specialized syntax held in a pattern .
- RE are very popular among programmers and can be applied in many programming languages like Java, JS, php, C++, etc. RE are useful for numerous practical day-to-day tasks that a data scientist encounters. It is one of the key concepts of Natural Language Processing that every NLP expert should be proficient in.
- RE are used in various tasks such as data pre-processing, rule-based information mining systems, pattern matching, text feature engineering, web scraping, data extraction, etc.
- RE can also handle formatting information, such as dates, email headers, markup tags, etc. RE can refer not just to ordinary characters, but also to formatting information.
- RE can also match sequences of characters, such as words, prefixes, suffixes, etc. RE can use special symbols to indicate the number, position, or type of characters to match.
- Some examples of RE are:

  - (0 + 10*) : This RE matches the regular set {0, 1, 10, 100, 1000, 10000, … }
  - (0*10*) : This RE matches the regular set {1, 01, 10, 010, 0010, …}
  - (0 + ε) (1 + ε) : This RE matches the regular set {ε, 0, 1, 01}
  - (a+b)* : This RE matches the set of strings of a’s and b’s
  - \b[a-z]+ing\b : This RE matches any word ending with ing
  - \d{2}/\d{2}/\d{4} : This RE matches any date in the format dd/mm/yyyy
  - [A-Z][a-z]+@[a-z]+\.(com|edu|org) : This RE matches any email address with the format Name@domain.extension

- A mnemonic to remember the basic syntax of RE is:

  - **M**etacharacters: These are special symbols that have a special meaning in RE, such as ., *, +, ?, ^, $, etc.
  - **A**nchors: These are metacharacters that indicate the position of a match, such as ^ for the beginning of a line, $ for the end of a line, \b for a word boundary, etc.
  - **C**haracter classes: These are metacharacters that specify a set of characters to match, such as [a-z] for any lowercase letter, [0-9] for any digit, [^a-z] for any character except a lowercase letter, etc.
  - **Q**uantifiers: These are metacharacters that specify how many times a character or a group of characters can be repeated, such as * for zero or more times, + for one or more times, ? for zero or one time, {n} for exactly n times, {n,m} for between n and m times, etc.
  - **G**roups: These are metacharacters that group a sequence of characters together, such as ( ) for capturing groups, (?: ) for non-capturing groups, (?= ) for positive lookahead, (?! ) for negative lookahead, etc.
  - **E**scapes: These are metacharacters that escape the special meaning of other metacharacters, such as \ for escaping metacharacters, \w for any word character, \d for any digit, \s for any whitespace, \n for a newline, etc.

- The acronym for the mnemonic is **MACQGE**. You can remember it as **MAC** and **QGE**.