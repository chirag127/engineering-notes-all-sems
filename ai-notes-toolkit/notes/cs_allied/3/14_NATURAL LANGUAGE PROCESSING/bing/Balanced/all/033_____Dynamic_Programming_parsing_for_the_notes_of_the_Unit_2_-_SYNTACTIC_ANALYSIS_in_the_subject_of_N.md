# Dynamic Programming Parsing

- Dynamic programming parsing is a technique for efficient syntactic analysis of natural language sentences.
- It is based on the idea of storing and reusing partial results of the parsing process, instead of recomputing them.
- It can reduce the time complexity of parsing from exponential to polynomial, depending on the grammar and the input sentence.
- Dynamic programming parsing requires the grammar to be in a restricted form, such as Chomsky Normal Form (CNF), where each rule has at most two symbols on the right-hand side.
- One of the most popular dynamic programming parsing algorithms is the Cocke-Kasami-Younger (CKY) algorithm, which is a bottom-up chart parser that fills a triangular table with the possible constituents for each substring of the input sentence.
- The CKY algorithm works as follows:

  - Initialize the table with the part-of-speech tags of the words in the sentence.
  - For each diagonal of the table, starting from the second one, compute the possible constituents for each cell by applying the grammar rules to the combinations of the cells below and to the left of the current cell.
  - If the cell at the top-right corner of the table contains the start symbol of the grammar, then the sentence is accepted and the table represents the parse forest of the sentence. Otherwise, the sentence is rejected and no parse tree exists.
  - To extract a single parse tree from the table, backtrack from the start symbol to the words, following the grammar rules that were used to fill the table.

- The following example illustrates the CKY algorithm for the sentence "the dog barks" and the grammar:

  - S -> NP VP
  - NP -> DT NN
  - VP -> VBZ
  - DT -> the
  - NN -> dog
  - VBZ -> barks

- The table is filled as follows:

| S |   |   |
|---|---|---|
|   | NP|   |
|   |   | VP|
| DT| NN| VBZ|
|the|dog|barks|

- The sentence is accepted and the parse tree is:

```
  S
 / \
NP  VP
|   |
DT  VBZ
|   |
the barks
 \
  NN
  |
  dog
```