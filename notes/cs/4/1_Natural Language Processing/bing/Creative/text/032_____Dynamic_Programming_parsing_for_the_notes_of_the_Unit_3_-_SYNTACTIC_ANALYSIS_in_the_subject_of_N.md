### Dynamic Programming Parsing

- Dynamic programming parsing is a technique for efficiently parsing natural language sentences using a context-free grammar (CFG) in Chomsky normal form (CNF).
- The idea is to store the results of subproblems in a table or chart and reuse them to solve larger problems, avoiding redundant computations.
- The most common dynamic programming parsing algorithm is the Cocke-Kasami-Younger (CKY) algorithm, which is a bottom-up, chart-based parser.
- The CKY algorithm works as follows:
  - Initialize an n-by-n upper triangular chart, where n is the number of words in the input sentence.
  - For each word i in the sentence, fill the cell (i,i) with the nonterminal symbols that can generate the word according to the grammar rules.
  - For each span of length 2 to n, fill the cell (i,j) with the nonterminal symbols that can generate the substring from word i to word j according to the grammar rules.
  - To fill a cell (i,j), consider all possible splits of the span (i,j) into two subspans (i,k) and (k+1,j), where i < k < j, and check if there is a grammar rule that can combine the nonterminals in the two subspans. If so, add the left-hand side of the rule to the cell (i,j).
  - If the cell (0,n-1) contains the start symbol of the grammar, then the sentence is accepted and a parse tree can be constructed by backtracking the chart. Otherwise, the sentence is rejected.
- The CKY algorithm has a time complexity of O(n^3 * |G|), where n is the length of the sentence and |G| is the size of the grammar. It has a space complexity of O(n^2 * |G|), where n is the length of the sentence and |G| is the size of the grammar.