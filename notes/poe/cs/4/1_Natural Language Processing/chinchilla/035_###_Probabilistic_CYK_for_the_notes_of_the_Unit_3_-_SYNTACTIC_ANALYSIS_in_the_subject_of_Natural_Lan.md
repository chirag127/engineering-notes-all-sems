### Probabilistic CYK for the notes of the Unit 3 - SYNTACTIC ANALYSIS in the subject of Natural Language Processing

Probabilistic CYK is a variant of the CYK algorithm that is used for syntactic analysis in natural language processing. It is a bottom-up parsing algorithm that can parse a sentence and generate its parse tree using a probabilistic context-free grammar (PCFG).

The Probabilistic CYK algorithm involves the following steps:

1. Preparation of PCFG: The first step is to prepare a PCFG, which is a context-free grammar where each production rule is associated with a probability. The sum of probabilities of all the production rules for a non-terminal symbol should be one.

2. Initialization: In this step, the algorithm initializes a two-dimensional table with the words of the input sentence. Each cell in the table corresponds to a substring of the sentence and represents the non-terminal symbols that can generate that substring.

3. Filling up the table: The algorithm fills up the table in a bottom-up manner. It starts by filling up the cells that represent substrings of length one. For each cell, it finds all the production rules with the right-hand side equal to the word in that cell and assigns the corresponding left-hand side non-terminal symbol to the cell.

4. Probabilistic parsing: After filling up the table, the algorithm generates the parse tree of the sentence by probabilistically choosing the most probable production rules for each cell. This is done by iterating over the cells of the table in a top-down manner and choosing the production rule with the highest probability for each cell.

5. Backtracking: Once the parse tree is generated, the algorithm performs backtracking to find the path with the highest probability from the root node to each leaf node.

Mnemonics and learning tricks:

- Remember the steps of the Probabilistic CYK algorithm using the acronym IFPBB, where I stands for Initialization, F for Filling up the table, P for Probabilistic parsing, B for Backtracking, and B for Building the parse tree.
- To remember the concept of PCFG, you can think of it as a grammar that assigns probabilities to each production rule, where the sum of probabilities of all the production rules for a non-terminal symbol should be one.

Advantages of Probabilistic CYK:

- It can handle ambiguous sentences and generate multiple parse trees for a sentence, each with a different probability.
- It can handle unseen sentences by assigning probabilities to unseen production rules based on the probabilities of similar production rules.

Disadvantages of Probabilistic CYK:

- It requires a large amount of training data to estimate the probabilities of production rules accurately.
- It is computationally expensive due to the large number of possible parse trees for a sentence.

Example:

Consider the PCFG with the following rules and probabilities:

S -> NP VP (0.6)
S -> VP (0.4)
NP -> Det N (0.4)
NP -> N (0.6)
VP -> V NP (0.8)
VP -> V (0.2)

Now, let's apply the Probabilistic CYK algorithm to parse the sentence "the cat chased the dog":

1. Initialization:

|   | the | cat | chased | the | dog |
|---|---|---|---|---|---|
| 1 | NP(Det) |       |       |       |       |
| 2 |        | NP(N) |       |       |       |
| 3 |        |       | VP(V) |       |       |
| 4 | NP(Det) |       | VP(VP) |       |       |
| 5 |        | NP(N) |       | VP(V) |       |
| 6 |        |       |       | VP(VP) | NP(Det) |

2. Filling up the table:

We can fill up the table by finding all the production rules that can generate a substring and assigning the corresponding non-terminal symbols to the cell. For example, for cell (1,1), we can find all the production rules with the right-hand side equal to "the" and assign the corresponding left-hand side non-terminal symbol to the cell.

3. Probabilistic parsing:

We can generate the parse tree by probabilistically choosing the most probable production rules for each cell. For example, for cell (4,3), we can choose the production rule VP -> V NP with probability 0.8.

4. Backtracking:

We can perform backtracking to find the path with the highest probability from the root node to each leaf node. For example, the parse tree for the sentence "the cat chased the dog" is:

        S(1.44)
       /   \
     NP(0.4) VP(1.0)
    / \     /   \
Det(1.0) N(1.0) V(1.0) NP(0.6)
 |     |     |