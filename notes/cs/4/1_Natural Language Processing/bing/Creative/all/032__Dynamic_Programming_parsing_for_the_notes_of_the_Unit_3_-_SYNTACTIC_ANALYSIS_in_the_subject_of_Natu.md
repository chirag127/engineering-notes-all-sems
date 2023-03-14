### Dynamic Programming parsing for the notes of the Unit 3 - SYNTACTIC ANALYSIS in the subject of Natural Language Processing

- Dynamic programming is a technique to solve complex problems by breaking them down into smaller subproblems and reusing the solutions of the subproblems to avoid repeated computation.
- Dynamic programming parsing is an application of dynamic programming to the problem of syntactic analysis of natural language sentences.
- Syntactic analysis, also known as parsing, is the process of determining the structure and meaning of a sentence by identifying its constituents and their grammatical relations.
- A common way to represent the syntactic structure of a sentence is by using a context-free grammar (CFG), which consists of a set of rules that specify how words and phrases can be combined to form valid sentences.
- A CFG can be used to generate a parse tree, which is a hierarchical representation of the syntactic structure of a sentence, where each node corresponds to a constituent and each branch corresponds to a rule application.
- Dynamic programming parsing algorithms use a bottom-up approach, where they start with the words of the sentence and build larger constituents by applying the rules of the CFG until they reach the start symbol of the grammar, which represents the whole sentence.
- Dynamic programming parsing algorithms use a data structure called a chart, which is a table that stores the partial results of the parsing process, such as the constituents that have been recognized and the rules that have been applied.
- The chart allows the algorithms to avoid recomputing the same constituents multiple times, and to efficiently retrieve the parse trees from the chart once the parsing is complete.
- The chart can be represented as a triangular matrix, where each cell corresponds to a span of words in the sentence, and each entry in a cell corresponds to a constituent that covers that span.
- For example, the chart for the sentence "John likes Mary" with a simple CFG is shown below:

| S |   |   |
|---|---|---|
|   | NP|   |
|   |   | NP|
|John|likes|Mary|

- The chart is filled in a bottom-up manner, starting from the diagonal cells, which correspond to the words of the sentence, and moving up to the upper-right cell, which corresponds to the whole sentence.
- To fill a cell, the algorithm looks at the cells below and to the left of it, and tries to combine the constituents in those cells using the rules of the CFG. If a combination is valid, the algorithm adds the resulting constituent to the current cell, along with a pointer to the cells that were used to form it.
- For example, to fill the cell at row 1 and column 2, which corresponds to the span "John likes", the algorithm looks at the cell at row 1 and column 1, which contains the constituent NP(John), and the cell at row 2 and column 2, which contains the constituent likes. The algorithm then tries to apply the rules of the CFG to combine these constituents. One of the rules is VP -> NP Verb, which means that a verb phrase (VP) can be formed by a noun phrase (NP) followed by a verb. Since NP(John) and likes match this rule, the algorithm adds the constituent VP(NP(John) likes) to the cell at row 1 and column 2, along with a pointer to the cells at row 1 and column 1 and row 2 and column 2. The chart after this step is shown below:

| S |   |   |
|---|---|---|
|   | NP|   |
|   |   | NP|
|John|likes|Mary|
|   | VP |   |

- The algorithm repeats this process for all the cells in the chart, until it reaches the cell at row 1 and column 3, which corresponds to the whole sentence. If this cell contains the start symbol of the grammar, which is S in this case, then the algorithm has successfully parsed the sentence. Otherwise, the algorithm reports a parsing failure, which means that the sentence is not valid according to the grammar.
- To retrieve the parse trees from the chart, the algorithm follows the pointers from the cell that contains the start symbol, and recursively builds the tree by adding the nodes and branches that correspond to the constituents and rules in the chart. For example, the parse tree for the sentence "John likes Mary" is shown below:

```
       S
      / \
     /   \
    NP   VP
   / \   / \
  /   \ /   \
John likes  NP
           /  \
          /    \