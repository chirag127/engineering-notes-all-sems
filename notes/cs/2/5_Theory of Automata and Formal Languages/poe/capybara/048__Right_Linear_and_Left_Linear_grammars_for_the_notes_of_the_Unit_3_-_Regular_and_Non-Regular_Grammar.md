### Right Linear and Left Linear Grammars

Right linear and left linear grammars are two important types of grammars in the study of theory of automata and formal languages. Here are some key points to understand about them:

#### Right Linear Grammar

- A right linear grammar is a type of grammar where all productions are of the form $A \rightarrow aB$ or $A \rightarrow a$, where $A$ and $B$ are non-terminals and $a$ is a terminal symbol.
- In other words, in a right linear grammar, the right-hand side of each production contains at most one non-terminal symbol, and it appears at the end of the string.
- Right linear grammars generate regular languages, which can be recognized by finite automata.
- Examples of right linear grammars include the grammar $S \rightarrow aS | b$ which generates the language $\{a^n b | n \geq 0\}$.

#### Left Linear Grammar

- A left linear grammar is a type of grammar where all productions are of the form $A \rightarrow Ba$ or $A \rightarrow a$, where $A$ and $B$ are non-terminals and $a$ is a terminal symbol.
- In other words, in a left linear grammar, the right-hand side of each production contains at most one non-terminal symbol, and it appears at the beginning of the string.
- Left linear grammars generate regular languages, which can be recognized by finite automata.
- Examples of left linear grammars include the grammar $S \rightarrow Sa | b$ which generates the language $\{ba^n | n \geq 0\}$.

#### Regular Grammars

- A grammar is called regular if it is either a right linear or left linear grammar.
- Regular grammars generate regular languages, which can be recognized by finite automata.
- Regular languages are a proper subset of context-free languages.

#### Non-Regular Grammars

- Any grammar that is not a regular grammar is called a non-regular grammar.
- Non-regular grammars generate non-regular languages, which cannot be recognized by finite automata.
- Examples of non-regular grammars include context-sensitive grammars and unrestricted grammars.

By understanding the concepts of right linear and left linear grammars, as well as regular and non-regular grammars, you will be able to analyze and generate languages in the study of theory of automata and formal languages.