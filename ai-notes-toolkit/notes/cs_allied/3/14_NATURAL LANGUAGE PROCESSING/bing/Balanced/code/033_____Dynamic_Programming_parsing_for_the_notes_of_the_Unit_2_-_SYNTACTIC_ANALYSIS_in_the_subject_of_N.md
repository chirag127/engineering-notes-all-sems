### Dynamic Programming Parsing

- Dynamic programming parsing is a technique for efficient syntactic analysis of natural language sentences using a context-free grammar (CFG) in Chomsky normal form (CNF).
- It is based on the idea of storing and reusing partial results of the parsing process in a table or chart, rather than recomputing them.
- It is a bottom-up parsing strategy, meaning that it starts from the words (or tokens) of the input sentence and builds larger constituents (or phrases) using the grammar rules.
- It is also a dynamic programming algorithm, meaning that it solves a complex problem by breaking it down into simpler subproblems and solving them optimally.
- The most common dynamic programming parsing algorithm is the Cocke-Kasami-Younger (CKY) algorithm, which has a time complexity of O(n^3 * |G|), where n is the length of the input sentence and |G| is the size of the grammar.
- The CKY algorithm works as follows:

  - Initialize an n x n chart, where each cell (i, j) corresponds to a span of words from i to j in the input sentence.
  - For each word w_i in the input sentence, fill the cell (i, i) with the nonterminal symbols that can generate w_i according to the grammar rules. These are called the preterminal symbols.
  - For each span length l from 2 to n, and for each start position i from 1 to n - l + 1, fill the cell (i, i + l - 1) with the nonterminal symbols that can generate the span from i to i + l - 1 according to the grammar rules. These are called the intermediate symbols.
  - To fill a cell (i, j), consider all possible splits of the span from i to j into two smaller spans: from i to k and from k + 1 to j, where i <= k < j. For each split, check if there is a grammar rule of the form A -> B C, where B is in the cell (i, k) and C is in the cell (k + 1, j). If so, add A to the cell (i, j).
  - The chart is filled in a diagonal fashion, from bottom left to top right, ensuring that the smaller spans are filled before the larger ones.
  - The final cell (1, n) contains the nonterminal symbols that can generate the whole input sentence. If the start symbol of the grammar (usually S) is in this cell, then the sentence is accepted by the grammar and a parse tree can be constructed by tracing back the chart. If not, then the sentence is rejected by the grammar and no parse tree exists.