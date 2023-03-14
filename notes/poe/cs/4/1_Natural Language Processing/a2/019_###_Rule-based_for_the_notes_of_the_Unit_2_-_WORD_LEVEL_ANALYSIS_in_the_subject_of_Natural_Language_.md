 Here is the content in Markdown format:

### Rule-based for the notes of the Unit 2 - WORD LEVEL ANALYSIS in the subject of Natural Language Processing

1. Regular Expressions: Regular expressions are patterns used to match character combinations in strings. They are a powerful mini-language for performing pattern matching in strings. Some common usages of regular expressions are:

- Validating forms: Ensuring email addresses/phone numbers are in the right format.
- Search and replace: Finding and replacing certain patterns of characters with other characters.
- Extracting data: Pulling out certain groups of characters/words from strings.

Advantages:

- Concise way to specify patterns
- Widely used and supported

Disadvantages:

- Can be hard to read/write complex patterns
- Backtracking can lead to poor performance for some patterns

Examples:

- [A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}: Matching an email address
- \d{3}-\d{3}-\d{4}: Matching a phone number in the format 123-456-7890

Applications: Used in text editors, parsing languages, web scraping, etc.

2. Stemming: Stemming is a process of reducing related words to their root/base form. The goal is to conflate the different inflected forms of a word into a single representation. This is useful for tasks like search and clustering.

Examples:

- boats, boating, boated -> boat (remove -s, -ing, -ed)
- better, best -> good

Advantages:

- Increased recall: More related words are matched
- Simplicity: Stemmers are relatively easy to implement

Disadvantages:

- Loss of detail: Related but different words may be conflated (e.g. boats and goats may both stem to boat)
- Ambiguity: Words may stem to the same root, obscuring meaning (e.g. sawing and seeing stem to see)

Applications: Search engines, clustering, indexing, etc.

[Include more points and details if required.]