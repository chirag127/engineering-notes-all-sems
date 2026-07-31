 Here is the content in Markdown format without any emojis or external links and in a formal tone:

### Implementation of LR Parsing Tables

1. Construct the LR(0) items for each production.
- An LR(0) item is of the form X → α.a where X → α is a production and a is a terminal or $ (end-marker).
- All productions of the form S → ε or S → a (where S is the start symbol and a is a terminal) are used to create the LR(0) items S → .$ and S → a.$ respectively.
2. Group the LR(0) items into sets which can have the same follow instances. This is done using the following algorithm:
- Initially, each LR(0) item is in its own set.
- Repeatedly find two sets which have follow instances and merge them.
- Stop when no more merging is possible. At the end, each set will contain LR(0) items which have the same follow possibilities.
3. Construct the LR(0) table. Do the following for each LR(0) item set:
- Choose any LR(0) item (say X → α.a) from the set.
- Check if there exists a production of the form Y → βa where Y → β is already an LR(0) item. If yes, mark the shift action for input symbol a in the entry corresponding to LR(0) item Y → β.
- Similarly, check for reduction productions of the form Y → βa where Y → β and mark the reduce action for the corresponding production.
- Repeat for all other LR(0) items in the set. At the end of this step, we will have the complete LR(0) table with shift and reduce actions marked.