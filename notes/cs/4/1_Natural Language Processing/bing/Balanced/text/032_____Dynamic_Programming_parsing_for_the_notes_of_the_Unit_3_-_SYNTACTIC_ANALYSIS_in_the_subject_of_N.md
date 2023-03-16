### Dynamic Programming Parsing

- Dynamic programming parsing is a technique for efficient syntactic analysis of natural language sentences using a context-free grammar (CFG) in Chomsky normal form (CNF).
- The idea is to store the results of subproblems (i.e., smaller constituents) in a table or chart and reuse them to find larger constituents, avoiding redundant computations.
- The most common dynamic programming parsing algorithm is the Cocke-Kasami-Younger (CKY) algorithm, which is a bottom-up, chart-based parser that works as follows:
  - Initialize an n x n chart, where n is the number of words in the sentence, and each cell (i,j) corresponds to the span from word i to word j (inclusive).
  - For each word i, fill the cell (i,i) with the non-terminal symbols that can generate that word according to the grammar rules.
  - For each span length l from 2 to n, and for each start position i from 1 to n-l+1, fill the cell (i,i+l-1) with the non-terminal symbols that can generate the span from word i to word i+l-1 by combining two smaller spans according to the grammar rules. For example, if A -> BC is a grammar rule, and B is in cell (i,k) and C is in cell (k+1,j), then add A to cell (i,j).
  - The chart is filled in a diagonal fashion, starting from the main diagonal and moving upwards and to the right.
  - The final parse tree can be obtained by tracing back the non-terminal symbols from the top-right cell (1,n), which corresponds to the whole sentence. If the start symbol of the grammar is in that cell, then the sentence is accepted by the grammar; otherwise, it is rejected.
- The complexity of the CKY algorithm is O(n^3|G|), where n is the length of the sentence and |G| is the size of the grammar. This is because there are O(n^2) cells to fill, each cell takes O(n) time to check all possible splits, and each split takes O(|G|) time to check all possible rules.
- Dynamic programming parsing can handle ambiguity and produce multiple parse trees for a sentence, but it cannot handle context-sensitive or ungrammatical sentences. It also requires the grammar to be in CNF, which may not be natural or intuitive for some languages.