### Probabilistic CYK for the notes of the Unit 3 - SYNTACTIC ANALYSIS in the subject of Natural Language Processing

- Probabilistic CYK is an extension of the CYK algorithm that finds the most likely parse tree of a given sentence according to a probabilistic context-free grammar (PCFG).
- A PCFG is a context-free grammar that assigns probabilities to each production rule, such that the sum of the probabilities of all rules with the same left-hand side is 1.
- Probabilistic CYK uses dynamic programming to store the probabilities of all possible substrings and nonterminals in a triangular matrix, similar to the CYK algorithm.
- The algorithm works as follows:
  - For each word in the sentence, find all nonterminals that can generate it with some probability, and store them in the diagonal cells of the matrix.
  - For each substring of length 2 or more, consider all possible ways of splitting it into two parts, and find all nonterminals that can generate the substring by combining the nonterminals of the two parts with some probability, and store them in the upper triangular cells of the matrix.
  - The probability of a nonterminal generating a substring is the product of the probabilities of the production rule and the two parts.
  - The most likely parse tree is the one that maximizes the probability of the start symbol generating the whole sentence, which is stored in the top-right cell of the matrix.
- An example of probabilistic CYK is shown below, using the following PCFG:

```
S -> NP VP  1.0
NP -> Det N  0.8
NP -> N  0.2
VP -> V NP  0.7
VP -> V  0.3
Det -> the  0.6
Det -> a  0.4
N -> dog  0.5
N -> cat  0.3
N -> mouse  0.2
V -> chased  0.6
V -> ate  0.4
```

- The sentence to be parsed is "the dog chased a cat".

```
| S      | 0.03456 |        |        |        |
| NP     | 0.24    | VP     | 0.144  |        |
| Det    | 0.6     | N      | 0.1    | V      | 0.24  | NP     | 0.096  |
| the    | 1.0     | dog    | 1.0    | chased | 1.0   | a      | 1.0    | cat    | 1.0    |
| 0      | 1       | 2      | 3      | 4      | 5     |
```

- The most likely parse tree is:

```
S
 / \
NP  VP
|  /  \
Det V  NP
|  |  /  \
the chased Det N
          |  |
          a  cat
```

- Some possible mnemonics and learning tricks for probabilistic CYK are:

  - Remember that probabilistic CYK is similar to CYK, but with probabilities added to the rules and the matrix cells.
  - Remember that the probability of a nonterminal generating a substring is the product of the probabilities of the rule and the two parts, and that the most likely parse tree is the one that maximizes the probability of the start symbol generating the whole sentence.
  - Remember that the diagonal cells of the matrix store the nonterminals that can generate the single words, and the upper triangular cells store the nonterminals that can generate the substrings of length 2 or more.
  - Remember that the top-right cell of the matrix stores the probability of the start symbol generating the whole sentence, and that the parse tree can be traced back from there by following the splits and the rules that were used.