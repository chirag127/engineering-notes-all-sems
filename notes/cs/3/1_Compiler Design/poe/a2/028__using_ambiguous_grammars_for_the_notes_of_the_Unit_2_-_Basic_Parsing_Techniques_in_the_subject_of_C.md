 Here is the content written in Markdown format without any emojis or external links and in a formal tone:

### Using Ambiguous Grammars

- Ambiguous grammars can result in more than one possible parse tree for a given input string. This makes parsing ambiguous grammars challenging.
- Techniques to handle ambiguity:
    - Specify precedence and associativity of operators to resolve shift/reduce conflicts.
    - Use parentheses to resolve ambiguity.
    - Choose one of the possible parse trees arbitrarily. This approach is adopted by some parser generators.
    - Report an error if ambiguity is detected.
- Types of ambiguity:
    - Phrase structure ambiguity: More than one way to group symbols into phrases or constituents. For example, "flying planes" can be parsed as "flying" followed by "planes" or as "flying planes".
    - Scope ambiguity: Ambiguity in determining the scope of operators, quantifiers etc. For example, the string "every boy loves a girl" can be parsed as "every (boy loves a girl)" or as "(every boy) loves a girl".
- Tools like parser generators do not guarantee to detect all ambiguities. It is the responsibility of the grammar designer to write unambiguous grammars. Making grammars unambiguous might require compromising their intuitiveness or simplicity.

The content summarizes the key points about ambiguous grammars and the techniques to handle ambiguity in a formal tone with points and without any emojis or external links as requested. Please let me know if you would like me to modify or expand the answer.