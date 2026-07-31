### Dynamic Programming Parsing

- Dynamic programming parsing is a technique for efficient parsing of natural language sentences using a context-free grammar (CFG) in Chomsky Normal Form (CNF).
- It is based on the idea of storing and reusing partial results of parsing, rather than recomputing them for every possible combination of words and rules.
- It is also known as chart parsing or tabular parsing, because it uses a data structure called a chart or a table to store the partial results.
- The chart is a two-dimensional matrix, where each cell represents a span of words in the input sentence, and each entry in a cell represents a possible constituent that covers that span.
- The chart is filled in a bottom-up manner, starting from the words and their part-of-speech tags, and applying the grammar rules to combine smaller constituents into larger ones, until the whole sentence is covered by a single constituent.
- The most common algorithm for dynamic programming parsing is the Cocke-Kasami-Younger (CKY) algorithm, which has a time complexity of O(n^3 * |G|), where n is the length of the sentence and |G| is the size of the grammar.
- The CKY algorithm works as follows:

  - Initialize the chart with the words and their part-of-speech tags as the diagonal entries.
  - For each span length from 2 to n, and for each start position from 1 to n - span + 1, do the following:
    - For each possible split point between the start and the end of the span, check if there are two entries in the chart that cover the left and the right subspans, respectively.
    - If there is a grammar rule that can combine the two entries into a larger constituent, add that constituent to the chart cell corresponding to the current span.
  - If the chart cell corresponding to the whole sentence contains the start symbol of the grammar, then the sentence is accepted and parsed. Otherwise, the sentence is rejected.

- The following diagram illustrates the CKY algorithm for parsing the sentence "the dog barks" using a simple CFG in CNF:

| | 1 | 2 | 3 |
| --- | --- | --- | --- |
| 1 | NP -> DT<br>the | S -> NP VP | |
| 2 | | NP -> NN<br>dog | VP -> VBZ |
| 3 | | | VBZ -> barks |

- The chart shows that the sentence can be parsed as S -> NP VP -> NP VBZ -> DT NN VBZ -> the dog barks.