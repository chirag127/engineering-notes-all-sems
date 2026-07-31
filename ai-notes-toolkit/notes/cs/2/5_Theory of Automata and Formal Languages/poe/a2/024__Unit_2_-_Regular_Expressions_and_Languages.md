 Here is the formal content in Markdown format without any emojis or external links:

## Unit 2 - Regular Expressions and Languages

1. Regular Expressions: Regular Expressions or Regex is a sequence of characters that forms a search pattern. It is used to search and manipulate strings. They are very useful for processing text and validating inputs. Some important concepts in Regex are:

- Metacharacters: Special characters that have a special meaning in a regex. For example, *, +, ?, ., ^, $.
- Quantifiers: Used to specify the number of occurrences of a character/substring. For example, *, +, ?, {n}.
- Character classes: Used to match a set of characters. For example, [abc], [0-9], [a-z].
- Anchors: Used to specify the position of a pattern. For example, ^, $.
- Grouping constructs: Used to group patterns, remember the text caught by parts of a pattern, and have those remembered sections participate in later processing. For example, (), (?:), (?<name>...)

2. Formal Languages: A formal language is a mathematical model for representing strings with a set of rules that govern the structure of strings. They are classified into 4 types:

- Regular Languages: Languages defined by regular expressions. Can be recognized by finite state machines.
- Context-free Languages: Languages defined by context-free grammars. Can be recognized by pushdown automata.
- Context-sensitive Languages: Languages defined by context-sensitive grammars. Can be recognized by linear bounded automata.
- Recursive Languages: Languages that are not context-sensitive languages. Cannot be recognized by Turing machines.