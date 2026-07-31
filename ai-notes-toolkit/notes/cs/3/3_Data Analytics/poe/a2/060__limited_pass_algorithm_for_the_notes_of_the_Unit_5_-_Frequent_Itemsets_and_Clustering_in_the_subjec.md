 Here is the content in markdown format without any emojis or external links as requested:

### Limited Pass Algorithm

- Scan the database only once to find frequent itemsets.
- Candidates are generated on the go. No candidate generation phase.
- Counts of candidates are maintained in a hash table.
- At each step, check if the count of a candidate >= min_support. If yes, it is a frequent itemset.
- If a candidate is frequent, generate new candidates by appending one item at a time and increment their counts.
- Terminate when no new frequent itemset is found.

Advantages:
- Only one scan of database required.
- Less memory required as candidates are generated on the go.
- Fast as less number of candidates are explored.

Limitations:
- May miss some frequent itemsets.
- Difficult to implement.

Note: The above points cover the key aspects of the limited pass algorithm for mining frequent itemsets. The content is written in a formal tone with points and without any emojis or external links as requested. Please let me know if you would like me to elaborate on any of the points or modify the content in any way.