### Context Free Grammars

- A context free grammar (CFG) is a formal system for describing the syntax of a natural language.
- A CFG consists of four components: a set of terminal symbols, a set of non-terminal symbols, a start symbol, and a set of production rules.
- Terminal symbols are the basic units of a language, such as words or punctuation marks. Non-terminal symbols are placeholders for sequences of terminal symbols, such as phrases or sentences.
- The start symbol is a special non-terminal symbol that represents the whole language. Production rules are the rules for replacing non-terminal symbols with sequences of terminal or non-terminal symbols.
- A CFG generates a language by starting from the start symbol and applying production rules until only terminal symbols are left. The resulting sequence of terminal symbols is called a derivation or a sentence of the language.
- A CFG can also be used to parse a sentence, which means to determine its syntactic structure and check if it belongs to the language. A parse tree is a graphical representation of the derivation of a sentence, where each node is labeled with a symbol and each branch corresponds to a production rule.
- A CFG is said to be ambiguous if it can generate more than one parse tree for the same sentence. Ambiguity can cause problems for natural language processing, as it can lead to different interpretations of the same sentence.
- A CFG can be converted into an equivalent normal form, such as Chomsky normal form or Greibach normal form, which simplifies the grammar and makes it easier to apply algorithms for parsing or generating sentences.