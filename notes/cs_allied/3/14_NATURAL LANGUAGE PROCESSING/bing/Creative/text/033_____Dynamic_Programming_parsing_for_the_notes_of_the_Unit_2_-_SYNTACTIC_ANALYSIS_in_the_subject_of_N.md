### Dynamic Programming Parsing

- Dynamic programming parsing is a technique for efficient parsing of natural language sentences using a context-free grammar (CFG) in Chomsky normal form (CNF).
- The idea is to store the results of subproblems (i.e., whether a substring can be derived from a nonterminal symbol) in a table or chart, and reuse them to solve larger problems (i.e., whether the whole sentence can be derived from the start symbol).
- The most common algorithm for dynamic programming parsing is the Cocke-Kasami-Younger (CKY) algorithm, which has a time complexity of O(n^3 * |G|), where n is the length of the sentence and |G| is the size of the grammar.
- The CKY algorithm works as follows:
  - Initialize an n x n upper triangular chart, where each cell (i, j) corresponds to the substring from word i to word j (inclusive) of the input sentence.
  - For each word i, fill the cell (i, i) with the nonterminal symbols that can directly generate that word, according to the grammar rules.
  - For each span length l from 2 to n, and for each start position i from 1 to n - l + 1, fill the cell (i, i + l - 1) with the nonterminal symbols that can generate the substring from word i to word i + l - 1, by applying the following rule: 
    - If A -> BC is a grammar rule, and B is in cell (i, k) and C is in cell (k + 1, i + l - 1) for some k between i and i + l - 1, then add A to cell (i, i + l - 1).
  - Check if the start symbol of the grammar is in the cell (1, n). If yes, then the sentence is accepted by the grammar. If no, then the sentence is rejected by the grammar.
  - Optionally, backtrack from the cell (1, n) to construct a parse tree for the sentence, by following the pointers that indicate which grammar rules and which cells were used to fill each cell.