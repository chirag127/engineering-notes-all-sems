 Here are the notes on Probabilistic CYK for Unit 3 - SYNTACTIC ANALYSIS in Natural Language Processing:

### Probabilistic CYK

- Probabilistic Context Free Grammars (PCFGs) assign probabilities to production rules.
- In Probabilistic CYK, we compute the probability of a sentence being generated from the grammar.
- The algorithm is same as CYK algorithm but we compute probabilities at each step.
- At each step, we consider all possible expansions of the substring and choose the one with the highest probability.
- The final probability of the complete sentence is the product of probabilities of individual expansions.
- This gives us the likelihood of the input sentence being generated from the grammar.
- Higher likelihood indicates better match with the grammar.
- This can be used to select from multiple possible parses of the input or to compare grammars.
- Limitation: The training data should be large enough to get good estimates of probabilities of production rules.
- With limited data, Smoothing techniques are used to handle unseen cases and avoid zero probabilities.

The notes cover the key points about Probabilistic CYK which computes probabilities of input sentences being generated from a Probabilistic Context Free Grammar. The algorithm is similar to standard CYK but calculates probabilities at each step and chooses the highest probability expansion. The final probability of the sentence is the product of individual expansion probabilities. This can be used to compare parses or grammars. Limitations and smoothing techniques are also discussed.