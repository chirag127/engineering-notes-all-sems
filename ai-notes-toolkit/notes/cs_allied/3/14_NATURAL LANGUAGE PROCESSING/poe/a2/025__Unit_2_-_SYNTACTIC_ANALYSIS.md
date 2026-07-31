 Here is the content in markdown format without any emojis or external links:

## Unit 2 - SYNTACTIC ANALYSIS

1. Introduction
- Syntax refers to the set of rules that govern the structure of sentences in a language.
- The syntax of a language describes how the words in that language can be combined to form grammatically valid sentences.
- Syntactic analysis is the process of analyzing a sentence to determine its syntactic structure and to ensure that it conforms to the syntactic rules of the language.

2. Context-free Grammars
- Context-free grammars are a formal way to describe the syntax of a language.
- A context-free grammar is defined as a 4-tuple (N, T, P, S) where:
-- N is a finite set of nonterminal symbols.
-- T is a finite set of terminal symbols.
-- P is a finite set of productions of the form A → α where A is a nonterminal and α is a string of terminals and nonterminals.
-- S is a special nonterminal symbol called the start symbol.
- Derivation is a series of applications of productions to rewrite a sentential form into a terminal string. A string is in the language described by the grammar if it can be derived from the start symbol.

3. Parsing
- Parsing is the process of analyzing an input string and constructing a parse tree that represents the syntactic structure of the input.
- There are two main approaches to parsing - top-down parsing and bottom-up parsing.
- In top-down parsing, the parse tree is constructed from the root down. It uses a set of recursive descent rules to match the input to the context-free grammar.
- In bottom-up parsing, the parse tree is constructed from the leaves up. It uses a parse table or parsing stack to determine which production should be used at each step.
- Both approaches have their pros and cons and are used in practice depending on the application.