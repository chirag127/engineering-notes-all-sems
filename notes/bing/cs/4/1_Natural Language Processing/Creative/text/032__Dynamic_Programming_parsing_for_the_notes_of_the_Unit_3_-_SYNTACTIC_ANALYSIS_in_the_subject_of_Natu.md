### Dynamic Programming Parsing

- Dynamic programming parsing is a technique for efficient parsing of natural language sentences using a context-free grammar (CFG) in Chomsky normal form (CNF).
- The idea is to use a bottom-up approach that builds larger constituents from smaller ones, and stores the intermediate results in a table or chart to avoid recomputation.
- The most common algorithm for dynamic programming parsing is the Cocke-Kasami-Younger (CKY) algorithm, which has a time complexity of O(n^3 * |G|), where n is the length of the input sentence and |G| is the size of the grammar.
- The CKY algorithm works as follows:
  - Initialize an n x n upper triangular matrix, where each cell (i, j) corresponds to a substring of the input sentence from word i to word j (inclusive).
  - For each cell (i, i), fill it with the non-terminal symbols that can generate the word i according to the grammar rules.
  - For each cell (i, j) where i < j, fill it with the non-terminal symbols that can generate the substring from word i to word j by combining two smaller constituents from the cells below it. For example, if cell (i, k) contains A and cell (k+1, j) contains B, and there is a grammar rule S -> A B, then cell (i, j) contains S.
  - The cell (1, n) contains the possible parses for the whole sentence. If it contains the start symbol of the grammar, then the sentence is accepted by the grammar. Otherwise, the sentence is rejected.
  - To recover the parse trees, we can use backpointers that store the information about which cells and rules were used to fill each cell.