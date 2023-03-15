### Interpolation and Backoff for the notes of the Unit 2 - WORD LEVEL ANALYSIS in the subject of Natural Language Processing

In Natural Language Processing, the task of language modeling is to assign probabilities to sequences of words. Interpolation and Backoff are two techniques used to estimate these probabilities.

#### Interpolation
Interpolation is a technique that combines probabilities estimated from multiple sources. It is a weighted average of the probabilities obtained from different sources. The weights are determined based on the performance of each source on a held-out data set.

Mnemonics and Learning Tricks:
- Think of Interpolation as a "blend" of probabilities from multiple sources. Just like how a blend of different ingredients can result in a unique taste, Interpolation blends the probabilities to give a unique probability estimate.

#### Backoff
Backoff is a technique used to estimate probabilities when the probability of a given n-gram is zero. It involves "backing off" to a lower-order n-gram, where the probability estimate is non-zero. For example, if the probability of a trigram is zero, we back off to a bigram or a unigram.

Mnemonics and Learning Tricks:
- Think of Backoff as a "fallback" option when the probability of a given n-gram is zero. Just like how we may have a fallback option when a preferred option is not available, Backoff falls back to a lower-order n-gram when the probability estimate is zero.

#### Interpolation vs. Backoff
Interpolation and Backoff are two complementary techniques used to estimate probabilities in language modeling. Interpolation is used when we have multiple sources of information, and we want to combine them. Backoff is used when we encounter unseen n-grams, and we need to fall back to lower-order n-grams.

Mnemonics and Learning Tricks:
- Think of Interpolation and Backoff as two "helpers" that assist us in estimating probabilities. Interpolation helps us when we have multiple helpers, and we want to combine their efforts. Backoff helps us when a helper is not available, and we need to call upon another helper.