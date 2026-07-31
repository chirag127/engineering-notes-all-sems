### Dynamic Programming Parsing

- Dynamic programming parsing is a technique for efficiently parsing natural language sentences using a context-free grammar (CFG) in Chomsky normal form (CNF).
- It is based on the idea of storing and reusing partial results of the parsing process in a table or chart, rather than recomputing them.
- It is also known as chart parsing or tabular parsing.
- It can reduce the time complexity of parsing from O(n^3 * |G|) to O(n^3), where n is the length of the input sentence and |G| is the size of the grammar.
- There are different variants of dynamic programming parsing, such as the Cocke-Kasami-Younger (CKY) algorithm, the Earley algorithm, and the CYK algorithm.

#### The CKY Algorithm

- The CKY algorithm is a bottom-up dynamic programming parsing algorithm that works on sentences that are in CNF.
- It starts with the words of the sentence and builds larger constituents by applying the grammar rules in a bottom-up fashion.
- It uses a triangular matrix to store the partial results, where each cell (i, j) represents the span of words from i to j in the sentence.
- It fills the matrix in a diagonal order, starting from the bottom-left corner and moving to the top-right corner.
- For each cell (i, j), it checks if there is a grammar rule A -> B C such that B is in cell (i, k) and C is in cell (k, j) for some k between i and j. If so, it adds A to cell (i, j).
- It also checks if there is a grammar rule A -> w such that w is the word at position i in the sentence. If so, it adds A to cell (i, i).
- The algorithm terminates when it reaches the cell (0, n), where n is the length of the sentence.
- If the start symbol of the grammar is in cell (0, n), then the sentence is accepted by the grammar and a parse tree can be constructed by tracing back the matrix.
- If the start symbol is not in cell (0, n), then the sentence is rejected by the grammar and no parse tree exists.

#### Example

- Consider the following CFG in CNF:

S -> NP VP

NP -> Det N

VP -> V NP

VP -> V

Det -> the

Det -> a

N -> dog

N -> cat

V -> barks

V -> chases

- And the following sentence:

the dog barks

- The CKY algorithm would fill the matrix as follows:

|   | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| 0 |   | S |   |   |
| 1 |   |   | NP|   |
| 2 |   |   |   | VP|
| 3 |   |   |   |   |

- The algorithm would start with the diagonal cells (0, 0), (1, 1), and (2, 2), and add the non-terminals that match the words:

|   | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| 0 | Det| S |   |   |
| 1 |   | N | NP|   |
| 2 |   |   | V | VP|
| 3 |   |   |   |   |

- Then, it would move to the next diagonal, and check for rules that combine two adjacent cells:

|   | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| 0 | Det| S | NP|   |
| 1 |   | N | NP|   |
| 2 |   |   | V | VP|
| 3 |   |   |   |   |

- Finally, it would reach the last cell (0, 3), and check for rules that combine three cells:

|   | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| 0 | Det| S | NP| S |
| 1 |   | N | NP|   |
| 2 |   |   | V | VP|
| 3 |   |   |   |   |

- Since the start symbol S is in cell (0, 3), the sentence is accepted by the grammar and a