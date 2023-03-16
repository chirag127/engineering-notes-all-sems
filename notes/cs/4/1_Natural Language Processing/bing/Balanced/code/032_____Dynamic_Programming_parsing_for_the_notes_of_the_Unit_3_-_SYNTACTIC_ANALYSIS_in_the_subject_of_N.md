### Dynamic Programming Parsing

- Dynamic programming parsing is a technique for efficient parsing of natural language sentences using a context-free grammar (CFG) in Chomsky normal form (CNF).
- It is based on the idea of storing and reusing partial results of the parsing process in a table or chart, rather than recomputing them.
- It is also known as chart parsing or bottom-up parsing, since it starts from the words (the bottom level of the parse tree) and builds larger constituents (the higher levels of the parse tree) using the grammar rules.
- The most common algorithm for dynamic programming parsing is the Cocke-Kasami-Younger (CKY) algorithm, which has a time complexity of O(n^3 * |G|), where n is the length of the input sentence and |G| is the size of the grammar.
- The CKY algorithm works as follows:

  - Initialize an n x n chart, where each cell (i, j) corresponds to a substring of the input sentence from word i to word j (inclusive).
  - For each word i in the sentence, fill the cell (i, i) with the non-terminal symbols that can generate that word according to the grammar rules.
  - For each span length l from 2 to n, and for each start position i from 1 to n - l + 1, fill the cell (i, i + l - 1) with the non-terminal symbols that can generate the substring from word i to word i + l - 1 by combining two smaller constituents from the chart, according to the grammar rules.
  - If the cell (1, n) contains the start symbol of the grammar, then the sentence is accepted and a parse tree can be constructed by tracing back the chart. Otherwise, the sentence is rejected and no parse tree exists.

- An example of the CKY algorithm applied to the sentence "the dog barks" using a simple CFG in CNF is shown below:

  |   | 1  | 2  | 3  |
  |---|----|----|----|
  | 1 | NP | S  |    |
  | 2 |    | V  | VP |
  | 3 |    |    | N  |

  - The grammar rules used are:

    - S -> NP VP
    - NP -> D N
    - VP -> V
    - N -> dog
    - V -> barks
    - D -> the

  - The parse tree is:

    - S
      - NP
        - D
          - the
        - N
          - dog
      - VP
        - V
          - barks