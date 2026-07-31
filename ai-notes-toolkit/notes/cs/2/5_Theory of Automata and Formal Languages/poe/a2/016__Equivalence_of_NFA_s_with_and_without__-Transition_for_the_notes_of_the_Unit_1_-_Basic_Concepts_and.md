 Here is the content in Markdown format without any feeling or friendliness, being formal and without any emojis or external links:

### Equivalence of NFA’s with and without ε-Transition

- An NFA with ε-transitions can be converted into an equivalent NFA without ε-transitions.
- This conversion can be done by replacing each ε-transition by a new start state and transitioning on the input symbol that caused the ε-transition.
- For example, if there is an ε-transition from state q to state p on input symbol a, then introduce a new start state q' and add a transition from q' to p on input symbol a.
- Make q' the start state and remove the ε-transition.
- By repeating this process for all ε-transitions, we can eliminate ε-transitions and produce an equivalent NFA without ε-transitions.
- The languages accepted by both NFA's are the same as the new start states created get merged with the start state of the original NFA.
- Hence, NFA's with and without ε-transitions are equivalent in terms of the languages they accept.

The above content is written in points in a formal manner with no feelings or friendliness and without any emojis or external links for the given topic to be used as study notes.