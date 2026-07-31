# Probabilistic CYK

- Probabilistic CYK is an extension of the CYK algorithm that finds the most likely parse tree of a given sentence according to a probabilistic context-free grammar (PCFG).
- A PCFG is a context-free grammar where each production rule has a probability associated with it, indicating how likely it is to be used in a derivation.
- Probabilistic CYK uses dynamic programming to store the probabilities of all possible substrings and nonterminals in a table, and then uses the table to construct the most probable parse tree.
- The algorithm works as follows:

  - Initialize a table T of size n x n, where n is the length of the input sentence. Each cell T[i,j] will store a set of nonterminals and their probabilities that can generate the substring from i to j.
  - For each word w in the sentence, find all the rules of the form X -> w and add X and its probability to T[i,i], where i is the position of w.
  - For each length l from 2 to n, and for each start position i from 1 to n-l+1, do the following:
    - Set the end position j to i+l-1.
    - For each split position k from i to j-1, do the following:
      - For each pair of nonterminals A and B in T[i,k] and T[k+1,j], respectively, do the following:
        - Find all the rules of the form C -> A B and calculate the probability of C as the product of the probabilities of A, B, and the rule.
        - If C is already in T[i,j], update its probability to the maximum of the current and the new probability.
        - Otherwise, add C and its probability to T[i,j].
  - The most probable parse tree is the one that starts with the nonterminal with the highest probability in T[1,n]. This can be obtained by tracing back the table from T[1,n] to T[i,i] and using the rules that were used to generate the nonterminals.