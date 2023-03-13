The probabilistic CYK algorithm is a parsing algorithm for context-free grammars that finds the most likely parse tree of a given sentence according to production probabilities. It is based on the CYK algorithm, which uses dynamic programming to fill a triangular table with the possible nonterminals that can generate each substring of the input . The probabilistic version of the algorithm also stores the probabilities of each nonterminal in the table, and updates them according to the rules of the grammar and the splitting probabilities of the substrings .

The following diagram illustrates the basic architecture of a probabilistic CYK algorithm in ASCII art:

```
Input: a sentence w = w1 w2 ... wn
Output: the most likely parse tree of w according to a PCFG

Step 1: Initialize the table T with n rows and n columns, where T[i,j] is a set of pairs (A,p) such that A -> wi ... wj with probability p

Step 2: For each i from 1 to n, do:
  For each A such that A -> wi with probability p, do:
    Add (A,p) to T[i,i]

Step 3: For each j from 2 to n, do: (length of the span)
  For each i from j-1 to 1, do: (start of the span)
    For each k from i to j-1, do: (partition of the span)
      For each rule A -> BC with probability q, do:
        If (B,p1) is in T[i,k] and (C,p2) is in T[k+1,j], then:
          Calculate p = p1 * p2 * q (the probability of A -> wi ... wj)
          If (A,p') is already in T[i,j], then:
            Replace (A,p') with (A,p) if p > p' (keep the highest probability)
          Else:
            Add (A,p) to T[i,j]

Step 4: Return the parse tree corresponding to the pair (S,p) in T[1,n], where S is the start symbol of the grammar, and p is the highest probability among all pairs in T[1,n]. If T[1,n] is empty or does not contain S, then return "No parse tree found".
```

: CYK algorithm - Wikipedia
: CYK algorithm - Wikipedia
: Cocke–Younger–Kasami (CYK) Algorithm - GeeksforGeeks