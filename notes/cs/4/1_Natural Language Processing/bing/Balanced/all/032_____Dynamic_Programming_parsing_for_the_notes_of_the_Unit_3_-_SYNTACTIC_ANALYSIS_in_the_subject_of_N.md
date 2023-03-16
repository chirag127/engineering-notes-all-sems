# Dynamic Programming Parsing

- Dynamic programming parsing is a technique for efficient syntactic analysis of natural language sentences.
- It is based on the idea of storing and reusing partial results of the parsing process, rather than recomputing them.
- It can reduce the time complexity of parsing from exponential to polynomial, depending on the grammar and the input sentence.
- Dynamic programming parsing requires the grammar to be in a restricted form, such as Chomsky Normal Form (CNF), where each rule has at most two symbols on the right-hand side.
- One of the most popular dynamic programming parsing algorithms is the Cocke-Kasami-Younger (CKY) algorithm, which is a bottom-up chart parser that fills a triangular table with the possible constituents for each span of the input sentence.
- The CKY algorithm works as follows:
  - Initialize the table with the part-of-speech tags of the words at the diagonal cells.
  - For each span length from 2 to n, where n is the length of the sentence, iterate over all possible start and end positions of the span.
  - For each span, iterate over all possible split points, and check if there is a grammar rule that can combine the constituents at the left and right subspans.
  - If there is such a rule, add the left-hand side symbol of the rule to the cell corresponding to the span.
  - If the cell at the top-right corner of the table contains the start symbol of the grammar, the sentence is accepted and the table contains the parse tree. Otherwise, the sentence is rejected.
- The CKY algorithm has a time complexity of O(n^3 * |G|), where n is the length of the sentence and |G| is the size of the grammar. It has a space complexity of O(n^2 * |G|), since it stores all possible constituents for each span.