### Probabilistic CYK for the notes of the Unit 3 - SYNTACTIC ANALYSIS in the subject of Natural Language Processing

- Probabilistic CYK is an extension of the CYK algorithm that finds the most likely parse tree of a given sentence according to a probabilistic context-free grammar (PCFG).
- A PCFG is a context-free grammar that assigns a probability to each production rule, such that the sum of the probabilities of all rules with the same left-hand side is 1.
- The probabilistic CYK algorithm uses dynamic programming to store the probabilities of all possible subtrees that can be generated from a given substring of the input sentence, and then combines them to find the most probable parse tree.
- The algorithm requires the PCFG to be in Chomsky normal form (CNF), which means that every rule has either two non-terminal symbols or one terminal symbol on the right-hand side.
- The algorithm works as follows:

  - Let the input be a string S consisting of n words: w1 ... wn.
  - Let the grammar contain r non-terminal symbols R1 ... Rr, with start symbol R1.
  - Let P[i, j, k] be the probability of the most likely subtree with root Rk that spans from word i to word j in S. Initialize all elements of P to 0.
  - Let back[i, j, k] be a triple that stores the information of how to construct the most likely subtree with root Rk that spans from word i to word j in S. Initialize all elements of back to null.
  - For each i = 1 to n:
    - For each unit production Rk -> wi:
      - Set P[i, i, k] = the probability of the rule Rk -> wi.
      - Set back[i, i, k] = <i, k, null>.
  - For each l = 2 to n (length of the span):
    - For each i = 1 to n - l + 1 (start of the span):
      - Let j = i + l - 1 (end of the span).
      - For each p = i to j - 1 (partition of the span):
        - For each production Ra -> Rb Rc:
          - Let prob = P[i, p, b] * P[p + 1, j, c] * the probability of the rule Ra -> Rb Rc.
          - If prob > P[i, j, a]:
            - Set P[i, j, a] = prob.
            - Set back[i, j, a] = <p, b, c>.
  - If P[1, n, 1] > 0, then S is a member of the language and the most likely parse tree can be constructed by retracing the steps through back.
  - Else, S is not a member of the language.

- Here is an example of the probabilistic CYK algorithm applied to the sentence "a man saw a book" with the following PCFG in CNF:

  - S -> NP VP (0.9)
  - S -> VP (0.1)
  - NP -> Det N (0.8)
  - NP -> N (0.2)
  - VP -> V NP (0.5)
  - VP -> V (0.5)
  - Det -> a (0.6)
  - Det -> the (0.4)
  - N -> man (0.4)
  - N -> book (0.3)
  - N -> telescope (0.3)
  - V -> saw (0.6)
  - V -> ate (0.4)

  - The table P is filled as follows (only showing non-zero values):

    | i\j | 1    | 2    | 3    | 4    |
    | --- | ---- | ---- | ---- | ---- |
    | 1   | Det  | NP   |      | S    |
    |     | 0.6  | 0.48 |      | 0.24 |
    | 2   | N    |      | VP   |      |
    |     | 0.4  |      | 0.12 |      |
    | 3   | V    |      |      | VP   |
    |     | 0.6  |      |      | 0.3  |
    | 4   | N    |      |      |      |
    |     |