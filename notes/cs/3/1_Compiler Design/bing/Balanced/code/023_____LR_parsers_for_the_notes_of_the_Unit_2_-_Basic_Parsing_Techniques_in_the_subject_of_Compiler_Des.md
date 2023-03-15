### LR parsers

LR parsers are a type of bottom-up parsers that analyse deterministic context-free languages in linear time. They read the input from left to right and produce a rightmost derivation in reverse . They are based on the concept of shift-reduce parsing, which involves shifting the input symbols onto a stack and reducing them to grammar productions when possible.

There are several variants of LR parsers, each with different levels of complexity and power:

- SLR (Simple LR) parsers: They use a simplified version of the LR(0) parsing tables, which only consider the current state and the next input symbol. They are easy to construct, but they cannot handle some grammars that are LR(0) or LR(1).
- LALR (Lookahead LR) parsers: They use a compressed version of the LR(1) parsing tables, which also consider a lookahead terminal for each state. They are more powerful than SLR parsers, but they may introduce conflicts or ambiguities in some cases.
- Canonical LR(1) parsers: They use the full LR(1) parsing tables, which have one state for each LR(1) item. They are the most powerful of the deterministic LR parsers, but they are also the most complex and may have a large number of states.
- Minimal LR(1) parsers: They use a reduced version of the LR(1) parsing tables, which eliminate redundant or equivalent states. They have the same power as canonical LR(1) parsers, but they have fewer states and are more efficient.
- GLR (Generalized LR) parsers: They use a nondeterministic version of the LR parsing tables, which allow multiple transitions for the same state and input symbol. They can handle any context-free grammar, including ambiguous ones, but they may require more time and space than deterministic LR parsers.

LR parsers have some advantages over other types of parsers, such as:

- They can handle a large class of grammars, including most programming languages.
- They can detect syntax errors as soon as possible, without requiring backtracking or lookahead.
- They can be easily implemented using tables and a stack, without requiring recursive calls or complex data structures.

LR parsers also have some disadvantages, such as:

- They may require a lot of memory to store the parsing tables, especially for LR(1) parsers.
- They may be difficult to construct by hand, and may require automated tools or algorithms.
- They may not be suitable for natural languages or other grammars that are not deterministic or context-free.

LR parsers are widely used in practice, especially for compiling programming languages. Some examples of LR parsers are:

- Yacc (Yet Another Compiler Compiler): A tool that generates LALR parsers from grammar specifications.
- Bison: A tool that generates LALR, canonical LR(1), or GLR parsers from grammar specifications.
- JavaCC (Java Compiler Compiler): A tool that generates LALR parsers for Java from grammar specifications.

: LR parser - Wikipedia
: Canonical LR parser - Wikipedia
: LR Parser - GeeksforGeeks
: LL vs. LR Parsing | Baeldung on Computer Science