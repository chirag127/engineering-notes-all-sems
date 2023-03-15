### LR parsers

- LR parsers are a type of **bottom-up parsers** that analyse **deterministic context-free languages** in linear time .
- LR parsers read the input from **left to right** and produce a **rightmost derivation** in reverse .
- LR parsers use a **stack** to store the grammar symbols and a **state transition table** to guide the parsing actions .
- LR parsers can handle a large class of grammars, including **ambiguous grammars** and **left-recursive grammars** .
- LR parsers can detect **syntax errors** as soon as possible .
- There are several variants of LR parsers, such as **SLR**, **LALR**, **Canonical LR**, **Minimal LR**, and **GLR** parsers . They differ in the way they construct the state transition table and the amount of lookahead they use .
- LR parsers are widely used in **compiler construction** and **programming language design** .