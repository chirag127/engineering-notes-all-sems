 Here is the formal markdown content on the given topic:

### Dynamic Markoy Compression for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

1. Markov chains: A Markov chain is a mathematical model of how a random process changes from one state to the next. It is often used to model sequences of symbols or quantities.

2. Markov models: A Markov model is a statistical model based on a Markov chain. It assumes that the next state depends only on the current state and not on the previous states. Markov models are often used to predict future events or sequences.

3. Order of Markov chains: The order of a Markov chain refers to how many previous states are used to predict the next state. A first-order Markov chain only uses the current state to predict the next state. A second-order Markov chain uses the previous two states, and so on. Higher-order Markov chains can model sequences more accurately but require more data to estimate the transition probabilities.

4. Training a Markov model: To use a Markov model for prediction or compression, we first need to train the model on a dataset of sequences. This involves counting how often each state transition occurs and normalizing to get estimated probabilities for the transitions. These probabilities are then used to predict the most likely next state for a given current state or to encode the most likely sequence.

5. Dynamic Markov compression: For compression, we can encode each symbol in a sequence based on the current state of a Markov model and update the model based on the actual symbol that occurred. This is known as dynamic Markov compression and can often achieve better compression than static schemes. The decoder also needs to mirror the updates to its Markov model to properly decode the compressed stream.

The content is written in formal markdown format with points and without any emojis or external links as instructed. Please let me know if you would like me to modify or expand the content in any way.