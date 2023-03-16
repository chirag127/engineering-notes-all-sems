### Context Free Grammars

- A **context-free grammar (CFG)** is a list of rules that define the set of all well-formed sentences in a language.
- Each rule has a **left-hand side**, which identifies a syntactic category, and a **right-hand side**, which defines its alternative component parts, reading from left to right.
- For example, the rule `S -> NP VP` means that a sentence (S) can be composed of a noun phrase (NP) followed by a verb phrase (VP).
- A CFG can be used to model the constituent structure of natural language, which is the hierarchical organization of words into phrases and sentences.
- A CFG can also be used to define the high level structure of a programming language, such as the syntax of statements, expressions, and declarations.
- A CFG can be formally defined as a 4-tuple: `G = (N, Σ, R, S)`, where
  - `N` is a finite set of **non-terminal symbols**, which are the syntactic categories that can be expanded by the rules.
  - `Σ` is a finite set of **terminal symbols**, which are the basic units of the language, such as words or tokens.
  - `R` is a finite set of **production rules**, which are of the form `A -> α`, where `A` is a non-terminal symbol and `α` is a string of symbols from `(N ∪ Σ)*`, the Kleene closure of the union of `N` and `Σ`.
  - `S` is a distinguished non-terminal symbol, called the **start symbol**, which represents the whole language.
- A CFG can generate a language, which is the set of all strings that can be derived from the start symbol by applying the rules repeatedly.
- A CFG can also parse a string, which is the process of finding a derivation or a parse tree for the string, if it belongs to the language.
- A CFG is called **context-free** because the production rules can be applied regardless of the surrounding symbols, unlike in a context-sensitive grammar, where the rules depend on the context.
- Natural languages are not strictly context-free, as they have some phenomena that require context-sensitive rules, such as agreement, anaphora, and long-distance dependencies.
- However, CFGs are often used as a simple and convenient approximation of natural languages, as they can capture many of their syntactic patterns and regularities.
- CFGs are also useful for natural language processing (NLP) tasks, such as parsing, generation, translation, and summarization.