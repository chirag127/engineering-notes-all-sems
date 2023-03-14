A probabilistic context-free grammar (PCFG) is an extension of a context-free grammar (CFG) with a probability for each production rule. The probability of a derivation (parse) is the product of the probabilities of the productions used in that derivation. PCFGs can be used to model the structure of natural languages and other symbol strings.

A PCFG can be defined by a quintuple:

G = (M, T, R, S, P)

where

- M is the set of non-terminal symbols
- T is the set of terminal symbols
- R is the set of production rules
- S is the start symbol
- P is the set of probabilities on production rules

A PCFG can be represented in a Chomsky normal form (CNF), where each production rule has the form:

N -> A B or N -> a

where N, A, and B are non-terminals and a is a terminal. The probabilities of the rules must sum to one for each non-terminal.

A PCFG can be illustrated by a parse tree, which shows the derivation of a string from the start symbol using the production rules. For example, consider the following PCFG:

S -> NP VP [0.9]
S -> VP [0.1]
NP -> Det N [0.8]
NP -> N [0.2]
VP -> V NP [0.5]
VP -> V [0.5]
Det -> the [0.6]
Det -> a [0.4]
N -> dog [0.3]
N -> cat [0.3]
N -> mouse [0.4]
V -> chased [0.4]
V -> ate [0.3]
V -> slept [0.3]

The parse tree for the string "the dog chased a cat" is:

```
       S
      / \
     /   \
    /     \
   NP      VP
  / \     / \
 /   \   /   \
Det   N V    NP
|    |  |   / \
the dog chased Det N
             |  |
             a cat
```

The probability of this parse is:

P(S -> NP VP) * P(NP -> Det N) * P(Det -> the) * P(N -> dog) * P(VP -> V NP) * P(V -> chased) * P(NP -> Det N) * P(Det -> a) * P(N -> cat)

= 0.9 * 0.8 * 0.6 * 0.3 * 0.5 * 0.4 * 0.8 * 0.4 * 0.3

= 0.000995328

This is one possible parse for the string, but there may be others depending on the grammar and the string. PCFGs can be used to find the most likely parse for a given string, or the probability of a string given a grammar. There are various algorithms for parsing PCFGs, such as the CYK algorithm, the Inside-Outside algorithm, or the Viterbi algorithm.