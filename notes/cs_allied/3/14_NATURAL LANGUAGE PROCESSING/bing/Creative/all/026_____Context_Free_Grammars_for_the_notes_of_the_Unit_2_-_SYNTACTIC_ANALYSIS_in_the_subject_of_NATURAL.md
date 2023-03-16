# Context Free Grammars

- A **context-free grammar (CFG)** is a list of rules that define the set of all well-formed sentences in a language.
- Each rule has a **left-hand side**, which identifies a syntactic category, and a **right-hand side**, which defines its alternative component parts, reading from left to right.
- A CFG consists of four components: a set of **terminal symbols**, a set of **non-terminal symbols**, a set of **production rules**, and a **start symbol**.
- A **terminal symbol** is a symbol that cannot be further decomposed into smaller units, such as a word or a punctuation mark.
- A **non-terminal symbol** is a symbol that can be replaced by a sequence of terminal or non-terminal symbols, according to the production rules.
- A **production rule** is a rule that specifies how a non-terminal symbol can be rewritten as a sequence of terminal or non-terminal symbols.
- A **start symbol** is a special non-terminal symbol that represents the whole sentence or utterance.
- A CFG can be used to generate or parse sentences in a language, by applying the production rules recursively, starting from the start symbol.
- A CFG can be represented by a **parse tree**, which is a graphical representation of the syntactic structure of a sentence, where each node corresponds to a non-terminal symbol, and each leaf corresponds to a terminal symbol.
- A CFG can also be represented by a **Backus-Naur form (BNF)**, which is a notation for expressing production rules in a concise and readable way.
- A CFG is called **context-free** because the production rules do not depend on the surrounding symbols or the position in the sentence.
- A CFG can model the constituent structure of natural language, but it cannot capture some of the more complex syntactic phenomena, such as agreement, long-distance dependencies, or word order variations .
- Therefore, natural languages are not strictly context-free, but rather **mildly context-sensitive**, which means that they require some additional mechanisms or constraints to account for their syntactic complexity.
- Some examples of mildly context-sensitive grammars are **tree-adjoining grammars**, **combinatory categorial grammars**, or **head-driven phrase structure grammars**.