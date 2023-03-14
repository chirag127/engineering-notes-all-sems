### Dynamic Programming Parsing

Dynamic programming parsing is a technique for efficiently parsing natural language sentences using context-free grammars (CFGs). It is based on the idea of storing and reusing partial results of the parsing process in a table or chart, instead of recomputing them. Dynamic programming parsing can reduce the time complexity of parsing from exponential to polynomial in the length of the input sentence.

There are different variants of dynamic programming parsing, such as the CKY algorithm, the Earley algorithm, and the chart parsing algorithm. They all share the same basic steps:

1. Convert the CFG to Chomsky Normal Form (CNF), which means that every rule has either two nonterminals or one terminal on the right-hand side (RHS).
2. Initialize a table or chart with one cell for each possible span of the input sentence, and fill the cells with the terminals that match the words in the sentence.
3. Apply the bottom-up parsing strategy, which means that for each span of the sentence, starting from the smallest to the largest, try to combine the cells that cover the span with the rules of the CFG that match the RHS of the cells. If a match is found, add the left-hand side (LHS) of the rule to the cell that covers the span.
4. Check if the cell that covers the whole sentence contains the start symbol of the CFG. If yes, the sentence is accepted by the grammar and a parse tree can be constructed by tracing back the rules that were applied. If no, the sentence is rejected by the grammar.

An example of the CKY algorithm applied to the sentence "John likes sushi" using a simple CFG is shown below:

![CKY example](https://courses.engr.illinois.edu/cs447/fa2018/Slides/Lecture09_files/image002.png)

The CFG used in the example is:

```
S -> NP VP
NP -> DT N | N
VP -> V NP | V
DT -> the | a
N -> John | Mary | sushi
V -> likes | eats
```

The CNF of the CFG is:

```
S -> NP VP
NP -> DT N | John | Mary | sushi
VP -> V NP | likes | eats
DT -> the | a
N -> John | Mary | sushi
V -> likes | eats
```

The table is initialized with the terminals that match the words in the sentence:

| John | likes | sushi |
| ---- | ----- | ----- |
| John | likes | sushi |

Then, the bottom-up parsing strategy is applied, starting from the spans of length 1 to the spans of length 3. For each span, the possible combinations of the cells that cover the span with the rules of the CFG are checked. For example, for the span (0, 1), the cell contains John, which matches the RHS of the rule NP -> John, so the LHS NP is added to the cell. Similarly, for the span (1, 2), the cell contains likes, which matches the RHS of the rule VP -> likes, so the LHS VP is added to the cell. The process continues until the table is filled as follows:

| John | likes | sushi |
| ---- | ----- | ----- |
| NP   | VP    | NP    |
|      | S     |       |

Finally, the cell that covers the whole sentence (0, 3) contains the start symbol S, which means that the sentence is accepted by the grammar and a parse tree can be constructed by tracing back the rules that were applied:

![Parse tree](https://courses.engr.illinois.edu/cs447/fa2018/Slides/Lecture09_files/image003.png)

The time complexity of the CKY algorithm is O(n^3 * |G|), where n is the length of the sentence and |G| is the size of the grammar. This is because there are O(n^2) cells in the table, each of which can be filled with O(n) possible combinations of smaller cells, and each combination can be checked against O(|G|) rules of the grammar. The space complexity of the CKY algorithm is O(n^2 * |G|), which is the size of the table.

Some advantages of dynamic programming parsing are:

- It is efficient and guarantees to find the optimal parse (or parses) for a given sentence and grammar, if any.
- It can handle ambiguous grammars and sentences, and produce multiple parses if needed.
- It can be extended to handle probabilistic CFGs, by storing and updating the probabilities of the partial parses in the table, and finding