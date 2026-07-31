
### Context Free grammars for Pushdown Automata

1. A pushdown automaton (PDA) is a type of finite automaton that uses a stack to store information. 
2. A PDA can be used to recognize certain types of languages, known as context-free languages. 
3. A context-free grammar (CFG) is a set of rules that describe how strings of symbols can be generated from a given language. 
4. A CFG consists of a set of non-terminal symbols, a set of terminal symbols, and a set of production rules. 
5. Non-terminal symbols are used to represent strings of symbols that can be generated from the language, while terminal symbols are used to represent strings of symbols that cannot be generated from the language. 
6. Production rules define how a non-terminal symbol can be replaced by a string of non-terminal and terminal symbols. 
7. A CFG can be used to generate strings of symbols that are accepted by a PDA. 
8. To generate a string of symbols accepted by a PDA, a CFG must be constructed such that each of its production rules can be simulated by a series of push and pop operations on the PDA's stack. 
9. A PDA can also be used to determine if a string of symbols is accepted by a CFG. 
10. To determine if a string is accepted by a CFG, a PDA must be constructed such that each of its states can be simulated by a production rule in the CFG.