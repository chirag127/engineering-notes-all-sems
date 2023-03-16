### Context Free Grammars

- A context-free grammar (CFG) is a list of rules that define the set of all well-formed sentences in a language.
- Each rule has a left-hand side, which identifies a syntactic category, and a right-hand side, which defines its alternative component parts, reading from left to right.
- A syntactic category is a label for a group of words or phrases that share some common properties, such as noun, verb, adjective, etc.
- A context-free grammar is called so because the rules can be applied regardless of the surrounding context of the words or phrases.
- A context-free grammar can be formally defined as a 4-tuple (V, Σ, R, S), where:
  - V is a finite set of variables or non-terminals, which represent syntactic categories.
  - Σ is a finite set of terminals, which represent words or symbols in the language.
  - R is a finite set of rules or productions, which have the form A → α, where A ∈ V and α ∈ (V ∪ Σ)*.
  - S ∈ V is a designated start symbol, which represents the whole sentence or program.
- A context-free grammar can be used to generate or parse sentences or programs in a language by applying the rules recursively, starting from the start symbol.
- A context-free grammar can be represented graphically by a parse tree, which shows the hierarchical structure of a sentence or program and the application of the rules.
- A context-free grammar can be used to model the constituent structure of natural language, which is the way words and phrases are grouped together to form larger units of meaning.
- A context-free grammar can also be used to define the high level structure of a programming language, which is the way statements and expressions are composed to form programs.
- A context-free grammar can capture some aspects of natural language syntax, such as word order, agreement, and recursion, but it cannot capture other aspects, such as pronoun reference, ellipsis, and coordination.
- Natural languages are not strictly context-free, but rather mildly context-sensitive, which means they require some additional mechanisms or constraints to account for their syntactic complexity.