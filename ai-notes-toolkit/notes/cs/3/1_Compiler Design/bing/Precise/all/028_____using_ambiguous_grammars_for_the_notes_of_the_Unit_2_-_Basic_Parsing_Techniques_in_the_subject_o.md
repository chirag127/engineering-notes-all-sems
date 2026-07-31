# Unit 2 - Basic Parsing Techniques: Using Ambiguous Grammars

- An ambiguous grammar is a context-free grammar that generates a sentence for which there are two or more distinct parse trees.
- Ambiguity in a grammar can lead to difficulties in parsing and understanding the meaning of sentences.
- Ambiguity can arise from several sources, including the use of left recursion, the use of right recursion, and the use of multiple productions with the same left-hand side.
- To resolve ambiguity, a grammar can be rewritten to eliminate the sources of ambiguity. This can be done by introducing new non-terminals, rewriting productions, or using precedence and associativity rules.
- Another approach to resolving ambiguity is to use a parser that can handle ambiguous grammars, such as an Earley parser or a GLR parser. These parsers can generate all possible parse trees for a sentence and then use disambiguation rules to select the most likely parse tree.
- It is important to note that not all ambiguous grammars can be rewritten to eliminate ambiguity. In some cases, the ambiguity is inherent in the language being described by the grammar.
- In summary, ambiguous grammars can pose challenges for parsing and understanding sentences, but there are techniques for resolving ambiguity, including rewriting the grammar and using specialized parsers. However, not all ambiguous grammars can be rewritten to eliminate ambiguity.