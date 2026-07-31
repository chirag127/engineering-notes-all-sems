### Context Free Grammars

- A context-free grammar (CFG) is a list of rules that define the set of all well-formed sentences in a language.
- Each rule has a left-hand side, which identifies a syntactic category, and a right-hand side, which defines its alternative component parts, reading from left to right.
- A syntactic category is a label for a group of words or phrases that have similar grammatical properties, such as noun, verb, adjective, etc.
- A context-free grammar is called so because the rules can be applied regardless of the surrounding context of the words or phrases.
- A context-free grammar can be formally defined as a 4-tuple (V, Σ, R, S), where:
  - V is a finite set of variables or non-terminal symbols, which represent syntactic categories.
  - Σ is a finite set of terminals or lexical symbols, which represent words or tokens in the language.
  - R is a finite set of production rules, which specify how to rewrite a variable as a sequence of variables and terminals.
  - S is a special variable, called the start symbol, which represents the whole sentence or program.
- A context-free grammar can be used to generate or parse sentences or programs in a language by applying the rules recursively, starting from the start symbol.
- A context-free grammar can be represented graphically by a parse tree, which shows the hierarchical structure of a sentence or program and the application of the rules.
- A context-free grammar can be used to model the constituent structure of natural language, which is the way words and phrases are grouped together to form larger units of meaning.
- A context-free grammar can also be used to define the high-level structure of a programming language, which is the way statements and expressions are composed to form a valid program.
- A context-free grammar can capture some, but not all, aspects of natural language syntax, such as word order, agreement, and subordination.
- Natural languages are not strictly context-free, as they have some dependencies and constraints that cannot be expressed by context-free rules, such as pronoun resolution, long-distance dependencies, and cross-serial dependencies.
- To account for these phenomena, some extensions or alternatives to context-free grammars have been proposed, such as context-sensitive grammars, tree-adjoining grammars, and head-driven phrase structure grammars.