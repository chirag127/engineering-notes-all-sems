The Viterbi search is an algorithm that finds the most likely sequence of hidden states in a hidden Markov model (HMM) based on a sequence of observed events. It is widely used for speech recognition, where the hidden states are the phonemes or words, and the observed events are the acoustic features.

The following diagram illustrates the basic architecture of a Viterbi search for speech modeling:

```
    +-----------------+     +-----------------+     +-----------------+
    |                 |     |                 |     |                 |
    |  State 1        |     |  State 2        |     |  State 3        |
    |                 |     |                 |     |                 |
    +-----------------+     +-----------------+     +-----------------+
       |       |  \            |       |  \            |       |  \
       |       |   \           |       |   \           |       |   \
       |       |    \          |       |    \          |       |    \
       |       |     \         |       |     \         |       |     \
       |       |      \        |       |      \        |       |      \
       |       |       \       |       |       \       |       |       \
       |       |        \      |       |        \      |       |        \
       |       |         \     |       |         \     |       |         \
       |       |          \    |       |          \    |       |          \
       |       |           \   |       |           \   |       |           \
       |       |            \  |       |            \  |       |            \
       |       |             \ |       |             \ |       |             \
       |       |              \|       |              \|       |              \
    +-----------------+     +-----------------+     +-----------------+     +-----------------+
    |                 |     |                 |     |                 |     |                 |
    |  State 1        |     |  State 2        |     |  State 3        |     |  State 4        |
    |                 |     |                 |     |                 |     |                 |
    +-----------------+     +-----------------+     +-----------------+     +-----------------+
       |       |  \            |       |  \            |       |  \            |       |  \
       |       |   \           |       |   \           |       |   \           |       |   \
       |       |    \          |       |    \          |       |    \          |       |    \
       |       |     \         |       |     \         |       |     \         |       |     \
       |       |      \        |       |      \        |       |      \        |       |      \
       |       |       \       |       |       \       |       |       \       |       |       \
       |       |        \      |       |        \      |       |        \      |       |        \
       |       |         \     |       |         \     |       |         \     |       |         \
       |       |          \    |       |          \    |       |          \    |       |          \
       |       |           \   |       |           \   |       |           \   |       |           \
       |       |            \  |       |            \  |       |            \  |       |            \
       |       |             \ |       |             \ |       |             \ |       |             \
       |       |              \|       |              \|       |              \|       |              \
    +-----------------+     +-----------------+     +-----------------+     +-----------------+
    |                 |     |                 |     |                 |     |                 |
    |  State 1        |     |  State 2        |     |  State 3        |     |  State 4        |
    |                 |     |                 |     |                 |     |                 |
    +-----------------+     +-----------------+     +-----------------+     +-----------------+
       |       |  \            |       |  \            |       |  \            |       |  \
       |       |   \           |       |   \           |       |   \           |       |   \