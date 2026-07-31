### Dynamic Programming Parsing

- Dynamic programming parsing is a technique for efficient syntactic analysis of natural language sentences using a context-free grammar (CFG) in Chomsky normal form (CNF).
- It is based on the idea of storing and reusing partial results of the parsing process in a table or chart, rather than recomputing them.
- It is also known as chart parsing or tabular parsing.
- It can handle ambiguous grammars and produce all possible parse trees for a given sentence.
- It has a time complexity of O(n^3 * |G|), where n is the length of the sentence and |G| is the size of the grammar.

#### CKY Parsing Algorithm

- CKY stands for Cocke-Kasami-Younger, the names of the researchers who developed the algorithm independently.
- It is a bottom-up dynamic programming parsing algorithm that starts from the words (terminal symbols) and builds larger constituents (non-terminal symbols) using the grammar rules.
- It requires the grammar to be in CNF, which means that every rule has the form A -> BC or A -> a, where A, B, and C are non-terminals and a is a terminal.
- It uses a triangular matrix or chart to store the partial results, where each cell (i, j) represents the span of words from i to j in the sentence.
- It fills the chart in a diagonal fashion, starting from the cells along the main diagonal (i, i) and moving to the cells above and to the right (i, j) where i < j.
- For each cell (i, j), it checks if there is a rule A -> a that matches the word at position i, and if so, it adds A to the cell.
- Then, it checks if there is a rule A -> BC that matches the combination of two cells below and to the left of the current cell, and if so, it adds A to the cell and records the backpointers to the two cells.
- The algorithm terminates when the cell (0, n) is filled, where n is the length of the sentence.
- If the cell (0, n) contains the start symbol of the grammar, then the sentence is accepted and the parse trees can be extracted by following the backpointers from the cell.
- If the cell (0, n) does not contain the start symbol, then the sentence is rejected and no parse trees are possible.