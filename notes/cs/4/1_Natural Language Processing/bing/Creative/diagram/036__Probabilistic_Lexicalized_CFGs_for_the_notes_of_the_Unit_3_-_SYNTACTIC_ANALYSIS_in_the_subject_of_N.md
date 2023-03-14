A probabilistic lexicalized CFG (L-PCFG) is a type of probabilistic context-free grammar (PCFG) that assigns probabilities to the rules based on the lexical heads of the phrases. A lexical head is the word that determines the syntactic category and semantic role of a phrase. For example, in the phrase "the red car", the head is "car" and it determines that the phrase is a noun phrase.

A L-PCFG can be represented as a tuple (N, T, S, R, P, H), where:

- N is a set of non-terminal symbols, such as S, NP, VP, etc.
- T is a set of terminal symbols, such as words or punctuation marks.
- S is the start symbol, usually S.
- R is a set of production rules of the form A -> B C or A -> a, where A, B, C are in N and a is in T.
- P is a function that assigns a probability to each rule, such that for any A in N, the sum of P(A -> alpha) over all possible alpha is 1.
- H is a function that assigns a lexical head to each non-terminal symbol, such that H(A) is in T for any A in N.

A L-PCFG can be used to parse a sentence by finding the most probable derivation tree that generates the sentence from the start symbol. This can be done by using a modified version of the CKY algorithm, which is a bottom-up dynamic programming algorithm that fills a parse table with the probabilities of each possible constituent. The algorithm can be summarized as follows:

- Initialize the parse table with the probabilities of the pre-terminal rules, such as NP -> the, VP -> saw, etc. These probabilities are always 1, since they are deterministic.
- For each span of length 2 or more, from left to right and bottom to top, compute the probabilities of the non-terminal rules that can generate that span, such as S -> NP VP, NP -> NP PP, etc. These probabilities are computed by multiplying the probabilities of the sub-constituents and the rule, and summing over all possible ways to split the span. For example, P(S -> NP VP | NP VP) = P(NP -> NP PP | NP PP) * P(PP -> P NP | P NP) * P(S -> NP VP).
- The probability of the sentence is the probability of the start symbol spanning the whole sentence, which is the top-right cell of the parse table. The most probable parse tree can be obtained by backtracking from that cell and choosing the rule with the highest probability at each step.

A L-PCFG can be learned from a treebank, which is a corpus of sentences annotated with their parse trees. The rule probabilities can be estimated by counting the occurrences of each rule and dividing by the occurrences of the left-hand side symbol. The head function can be defined by using a set of head rules that specify how to find the head of a phrase based on its category and sub-constituents. For example, the head of a noun phrase is usually the rightmost noun, the head of a verb phrase is usually the leftmost verb, etc.

The following diagram illustrates the basic architecture of a L-PCFG:

```
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|  Treebank      |----->|  Rule          |----->|  Parse         |
|                |      |  Extraction    |      |  Table         |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
                         |                |
                         |                |
                         v                v
                    +----------------+      +----------------+
                    |                |      |                |
                    |  Rule          |      |  Head          |
                    |  Probability   |      |  Function      |
                    |  Estimation    |      |                |
                    |                |      |                |
                    +----------------+      +----------------+
```