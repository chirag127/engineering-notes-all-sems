A hidden Markov model (HMM) is a statistical model that can be used to describe the probabilistic behavior of a system that has hidden or unobservable states. In speech recognition, an HMM can be used to model the acoustic features of speech signals and the underlying phonetic units that produce them. An HMM consists of the following components:

- A set of N states, denoted by S = {S1, S2, ..., SN}. Each state has an associated probability distribution over the possible observations, denoted by B = {b1, b2, ..., bN}.
- A transition matrix A, where aij is the probability of transitioning from state Si to state Sj.
- An initial state distribution π, where πi is the probability of starting in state Si.

An HMM can be represented graphically as a directed graph, where the nodes are the states and the edges are the transitions. The following diagram illustrates the basic architecture of an HMM:

```
    π1    π2    π3    ...    πN
    |     |     |           |
    v     v     v           v
   S1 --> S2 --> S3 --> ... --> SN
    |     |     |           |
    v     v     v           v
   b1    b2    b3    ...    bN
    |     |     |           |
    v     v     v           v
   O1    O2    O3    ...    ON
```

In the diagram, O1, O2, O3, ..., ON are the observed variables, which are the acoustic features of the speech signal. S1, S2, S3, ..., SN are the hidden variables, which are the phonetic units that generate the speech signal. The transition matrix A and the initial state distribution π are the parameters of the HMM that need to be estimated from the training data. The observation probability distributions B can be either discrete or continuous, depending on the type of features used.

An HMM can be used for speech recognition by performing the following tasks:

- Training: Given a set of speech signals and their corresponding transcriptions, estimate the parameters of the HMM that best fit the data. This can be done using algorithms such as the Baum-Welch algorithm or the Viterbi training algorithm.
- Decoding: Given a new speech signal, find the most likely sequence of hidden states that generated it. This can be done using algorithms such as the Viterbi algorithm or the forward-backward algorithm.
- Evaluation: Given a decoded sequence of hidden states and the true transcription, measure the accuracy of the recognition. This can be done using metrics such as the word error rate (WER) or the phoneme error rate (PER).