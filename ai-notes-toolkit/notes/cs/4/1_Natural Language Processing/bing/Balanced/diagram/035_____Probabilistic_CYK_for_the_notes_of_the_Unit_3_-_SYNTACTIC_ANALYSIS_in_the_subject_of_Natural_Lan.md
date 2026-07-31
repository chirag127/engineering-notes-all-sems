### Probabilistic CYK

- The probabilistic CYK algorithm is an extension of the CYK algorithm for parsing sentences with probabilistic context-free grammars (PCFGs).
- PCFGs are context-free grammars that assign probabilities to each production rule, indicating how likely it is to be used in a derivation.
- The probabilistic CYK algorithm finds the most likely parse tree for a given sentence according to the production probabilities, using dynamic programming to avoid redundant computations.
- The algorithm works as follows:

  - Let *n* be the length of the input sentence, and let *X[i,j]* be the probability that the substring from position *i* to *j* can be derived from the nonterminal *X*.
  - Initialize *X[i,i]* to the probability of the rule *X -> w_i*, where *w_i* is the word at position *i*, for all *i* and *X*.
  - For each substring length *l* from 2 to *n*, and for each starting position *i* from 1 to *n-l+1*, do the following:
    - Let *j* be *i+l-1*, the ending position of the substring.
    - For each nonterminal *X*, compute *X[i,j]* as the maximum of the following values, for all possible splits *k* between *i* and *j*:
      - *X[i,j]* = max(*X[i,j]*, *P(X -> Y Z) * Y[i,k] * Z[k+1,j]*), where *P(X -> Y Z)* is the probability of the rule *X -> Y Z*.
  - The final result is *S[1,n]*, the probability that the whole sentence can be derived from the start symbol *S*.
  - To obtain the most likely parse tree, we can backtrack from *S[1,n]* and choose the split *k* that maximizes *X[i,j]* for each nonterminal *X* and substring *[i,j]*.

- The following diagram illustrates the probabilistic CYK algorithm for the sentence "she eats a fish" with a PCFG:

```
| S[1,4] = 0.0027 |         |         |         |
|-----------------|---------|---------|---------|
| NP[1,2] = 0.15  | VP[2,4] = 0.018   |         |         |
|-----------------|-------------------|---------|---------|
| PRP[1,1] = 0.3  | V[2,2] = 0.2      | NP[3,4] = 0.09    |         |
|-----------------|-------------------|-------------------|---------|
| she             | eats              | DT[3,3] = 0.3     | NN[4,4] = 0.3    |
|                 |                   | a                 | fish             |
```

- The most likely parse tree is:

```
S
 / \
NP  VP
|   / \
PRP V  NP
|   |  / \
she eats DT NN
        |  |
        a  fish
```