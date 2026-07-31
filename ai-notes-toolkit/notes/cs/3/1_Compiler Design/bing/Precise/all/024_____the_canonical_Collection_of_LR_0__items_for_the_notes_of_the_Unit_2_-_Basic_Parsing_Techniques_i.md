# The Canonical Collection of LR(0) Items

- An LR(0) item is a production with a dot at some position on the right side of the production.
- At any point of the parsing process, an LR(0) item indicates how much portion of a production we have seen.
- A collection of sets of LR(0) items is called the Canonical LR(0) collection.
- The Canonical LR(0) collection is used in the construction of SLR functions closure and goto in order to construct a canonical LR(0) collection for a grammar G.
- The collection of LR(0) items is helpful in constructing deterministic finite automata to make parsing decisions.
- In the LR(0), we need to put the reduce node in the entire row.