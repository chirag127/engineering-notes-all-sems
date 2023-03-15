## Unit 2 - Regular Expressions and Languages

- A regular expression is a concise way of describing a set of strings that share a common pattern.
- A regular expression can be used to specify the syntax of a language, such as the format of email addresses, phone numbers, passwords, etc.
- A regular expression can also be used to search for or replace occurrences of a pattern in a text, such as finding all email addresses in a document, or replacing all tabs with spaces.
- A regular expression consists of symbols that represent characters, sets of characters, or operations on sets of characters.
- Some common symbols and their meanings are:

| Symbol | Meaning |
| ------ | ------- |
| a      | The character a |
| [abc]  | Any one of the characters a, b, or c |
| [a-z]  | Any one of the characters from a to z |
| [^a-z] | Any character that is not from a to z |
| .      | Any character except the newline |
| a*     | Zero or more occurrences of a |
| a+     | One or more occurrences of a |
| a?     | Zero or one occurrence of a |
| a{m,n} | Between m and n occurrences of a |
| a|b    | Either a or b |
| (a)    | A group of a |
| ^a     | a at the beginning of a line |
| a$     | a at the end of a line |

- For example, the regular expression `[a-zA-Z]+@[a-zA-Z]+\.(com|edu|org)` matches any email address that consists of one or more letters, followed by an @ sign, followed by one or more letters, followed by a dot, followed by either com, edu, or org.
- A language is a set of strings that are formed from an alphabet, which is a finite set of symbols.
- A language can be defined by a regular expression, which specifies the rules for generating the strings in the language.
- For example, the language defined by the regular expression `a*b*` is the set of all strings that consist of zero or more a's followed by zero or more b's, such as "", "a", "ab", "aaabbb", etc.
- A language can also be defined by a finite automaton, which is a mathematical model of computation that consists of a finite set of states, a finite set of input symbols, a transition function that maps a state and an input symbol to a new state, a start state, and a set of accept states.
- A finite automaton can accept or reject a string by reading it from left to right, and changing its state according to the transition function. If the automaton ends up in an accept state after reading the whole string, it accepts the string. Otherwise, it rejects the string.
- For example, the following finite automaton defines the same language as the regular expression `a*b*`:

![Finite automaton for a*b*](https://i.imgur.com/2QZQ1jJ.png)

- The start state is q0, and the accept states are q0 and q1. The transition function is shown by the arrows labeled with the input symbols. For example, if the automaton is in state q0 and reads an a, it moves to state q1. If it reads a b, it stays in state q0. If it reads any other symbol, it moves to a dead state (not shown) and rejects the string.
- A regular expression and a finite automaton are equivalent ways of defining a language. Any language that can be defined by a regular expression can also be defined by a finite automaton, and vice versa. This is known as the Kleene's theorem, named after the mathematician Stephen Kleene who proved it.
- There are algorithms for converting a regular expression to a finite automaton, and a finite automaton to a regular expression. These algorithms are useful for implementing regular expression engines, such as those used in programming languages, text editors, or search engines.