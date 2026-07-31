# Languages

- In automata theory, a formal language is a set of strings of symbols drawn from a finite alphabet .
- A formal language can be specified either by a set of rules (such as regular expressions or a context-free grammar) that generates the language, or by a formal machine that accepts (recognizes) the language .
- A word is a finite string of symbols from the alphabet.
- A language is a set of words, which may be finite or infinite.
- A formal language is a mathematical object that can be studied using logic and set theory.

## Regular and Non-Regular Grammars

- A grammar is a set of rules that defines how to form words and sentences in a language.
- A grammar consists of four components: a finite set of terminals (symbols that appear in the words of the language), a finite set of nonterminals (symbols that represent syntactic categories), a start symbol (a special nonterminal that denotes the whole sentence), and a finite set of production rules (rules that specify how to replace a nonterminal with a combination of terminals and nonterminals).
- A grammar is said to be regular if all its production rules are of the form A -> a or A -> aB, where A and B are nonterminals and a is a terminal.
- A grammar is said to be non-regular if it has at least one production rule that is not of the form A -> a or A -> aB.
- A regular grammar can generate a regular language, which is a language that can be recognized by a finite automaton .
- A non-regular grammar can generate a non-regular language, which is a language that cannot be recognized by a finite automaton.
- Examples of regular languages are the set of all binary strings that end with 0, the set of all strings over {a,b} that contain an even number of a's, and the set of all strings that match the regular expression (ab)*.
- Examples of non-regular languages are the set of all palindromes over {a,b}, the set of all strings over {a,b} that contain the same number of a's and b's, and the set of all strings that match the context-free grammar S -> aSb | epsilon.
- Regular languages have many applications in computer science, such as lexical analysis, pattern matching, text processing, and network protocols.
- Non-regular languages have applications in natural language processing, compiler design, semantics of programming languages, and logic .