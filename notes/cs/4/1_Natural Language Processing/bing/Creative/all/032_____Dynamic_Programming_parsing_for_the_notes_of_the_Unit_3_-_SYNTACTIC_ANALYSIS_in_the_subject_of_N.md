# Dynamic Programming Parsing

- Dynamic programming parsing is a technique for efficient syntactic analysis of natural language sentences.
- It is based on the idea of storing and reusing partial results of the parsing process, rather than recomputing them.
- It can reduce the time complexity of parsing from exponential to polynomial, depending on the grammar and the input sentence.
- Dynamic programming parsing requires the grammar to be in a restricted form, such as Chomsky Normal Form (CNF), where each rule has at most two symbols on the right-hand side.
- One of the most popular dynamic programming parsing algorithms is the Cocke-Kasami-Younger (CKY) algorithm, which is a bottom-up chart parser that fills a triangular matrix with the possible constituents for each span of the input sentence.
- The CKY algorithm works as follows:
  - Initialize the diagonal cells of the matrix with the POS tags of the words in the sentence.
  - For each cell above the diagonal, iterate over all possible splits of the span and check if there is a rule in the grammar that can combine the two subspans into a larger constituent. If so, add that constituent to the cell.
  - The cell at the top right corner of the matrix contains the possible parses for the whole sentence. If it includes the start symbol of the grammar, then the sentence is accepted by the grammar. Otherwise, the sentence is rejected.
  - To recover the parse tree, backtrack from the start symbol to the POS tags, following the rules that were used to fill the matrix.
- An example of the CKY algorithm applied to the sentence "the dog barks" with a simple grammar is shown below:

| S | NP | VP | Det | N | V |
|---|----|----|-----|---|---|
| 3 |    |    |     |   |   |
|   | S  |    |     |   |   |
| 2 |    | VP |     |   |   |
|   |    |    | S   |   |   |
| 1 | NP |    |     | N |   |
|   |    |    |     |   | V |
| 0 |    |    | Det |   |   |
|   | 0  | 1  | 2   | 3 | 4 |
|   | the| dog| barks|   |   |

- The parse tree for the sentence is:

```
  S
 / \
NP VP
| / \
Det N V
| | |
the dog barks
```

- Dynamic programming parsing can handle ambiguity and multiple parses by storing all the possible constituents in each cell of the matrix.
- However, dynamic programming parsing can also suffer from some limitations, such as:
  - It can be memory-intensive, as it requires storing a large matrix for each sentence.
  - It can be inefficient, as it may compute and store constituents that are not part of any valid parse.
  - It can be inaccurate, as it may miss some valid parses due to the grammar being in a restricted form or due to the presence of unknown words or rules.