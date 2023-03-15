### Optimization of DFA-Based Pattern Matchers

1. **Important States of an NFA**: The first step in optimizing DFA-based pattern matchers is to identify the important states of the NFA.

2. **Functions Computed From the Syntax Tree**: The next step is to compute certain functions from the syntax tree of the regular expression.

3. **Computing unliable, firstpos, and lastpos**: These functions are used to compute the unliable, firstpos, and lastpos sets for each node in the syntax tree.

4. **Computing followpos**: The followpos set is then computed for each position in the regular expression.

5. **Converting a Regular Expression Directly to a DFA**: One algorithm that can be used to implement and optimize pattern matchers constructed from regular expressions is to construct a DFA directly from a regular expression, without constructing an intermediate NFA.

6. **Minimizing the Number of States of a DFA**: Another algorithm that can be used to optimize DFA-based pattern matchers is to minimize the number of states in the DFA.

These are some of the key points to consider when optimizing DFA-based pattern matchers.