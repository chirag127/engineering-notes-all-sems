### Probabilistic CYK

- The probabilistic CYK algorithm is a variant of the CYK algorithm that finds the most likely parse tree for a given sentence and a probabilistic context-free grammar (PCFG).
- A PCFG is a context-free grammar where each production rule has a probability associated with it, indicating how likely it is to be used in a derivation.
- The probabilistic CYK algorithm uses dynamic programming to store the probabilities of all possible subtrees for each substring of the input sentence, and then combines them to find the most probable parse tree.
- The algorithm works as follows:

  - Initialize a table T of size n x n, where n is the length of the input sentence, and fill it with zeros.
  - For each word i in the sentence, find all the nonterminals A that can generate it, and set T[i,i] = P(A -> i), where P(A -> i) is the probability of the production rule A -> i.
  - For each span length j from 2 to n, and for each start position i from 1 to n-j+1, find all the nonterminals A that can generate the substring from i to i+j-1, and set T[i,i+j-1] = max(P(A -> BC) * T[i,k] * T[k+1,i+j-1]), where P(A -> BC) is the probability of the production rule A -> BC, and k ranges from i to i+j-2. This means that we consider all the possible ways to split the substring into two parts, and choose the one that maximizes the probability of the subtree rooted at A.
  - The most probable parse tree for the whole sentence is the one that has the highest probability in T[1,n], and it can be reconstructed by tracing back the splits that were chosen in the previous step.