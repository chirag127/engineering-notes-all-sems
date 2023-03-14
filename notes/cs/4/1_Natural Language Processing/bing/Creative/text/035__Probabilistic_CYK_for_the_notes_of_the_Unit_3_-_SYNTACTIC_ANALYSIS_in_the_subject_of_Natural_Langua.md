### Probabilistic CYK

- Probabilistic CYK is an extension of the Cocke–Younger–Kasami (CYK) algorithm for parsing sentences with probabilistic context-free grammars (PCFGs).
- PCFGs are context-free grammars that assign probabilities to each production rule, indicating how likely it is to be used in generating a sentence.
- Probabilistic CYK uses dynamic programming to find the most likely parse tree of a given sentence according to the production probabilities.
- The algorithm requires the grammar to be in Chomsky normal form (CNF), which means that every rule has either two non-terminal symbols or one terminal symbol on the right-hand side.
- The algorithm works as follows:

  - Let the input be a string of length n: a1 ... an.
  - Let the grammar contain r non-terminal symbols R1 ... Rr, with start symbol R1.
  - Let P[n, n, r] be an array of probabilities. Initialize all elements of P to 0.
  - Let back[n, n, r] be an array of backpointers. Initialize all elements of back to null.
  - For each s = 1 to n:
    - For each unit production Rv → as:
      - Set P[1, s, v] = the probability of the production.
      - Set back[1, s, v] = as.
  - For each l = 2 to n (length of span):
    - For each s = 1 to n - l + 1 (start of span):
      - For each p = 1 to l - 1 (partition of span):
        - For each production Ra → Rb Rc:
          - If P[p, s, b] > 0 and P[l - p, s + p, c] > 0:
            - Let prob = the probability of the production times P[p, s, b] times P[l - p, s + p, c].
            - If prob > P[l, s, a]:
              - Set P[l, s, a] = prob.
              - Set back[l, s, a] = <p, b, c>.
  - If P[n, 1, 1] > 0, then the sentence is in the language and the most likely parse tree can be constructed by following the backpointers from back[n, 1, 1].
  - Otherwise, the sentence is not in the language.