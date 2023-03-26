 Here is the content in Markdown format without any emojis or external links:

### Voting protocols for the notes of the Unit 7 - Fault Tolerance in the subject of DISTRIBUTED SYSTEM:

1. Majority Voting: In majority voting, each replica votes and the option that gets majority wins. This can tolerate only minority of faulty replicas. If more than half the replicas are faulty, the result can be wrong.
2. Weighted Majority Voting: Each replica is assigned a weight. The option that gets votes with a weight greater than half the total wins. This can tolerate a larger fraction of faulty replicas by assigning more weight to correct replicas.
3. Consensus: The voting protocol must satisfy two properties:

a) Agreement: No two correct replicas can disagree on the decision value.
b) Validity: If all the initial replica values are the same, then the decided value must be the initial value.

Consensus allows only one decision and is more powerful but harder to achieve than majority voting.

The content is written in a formal tone with points and without any emojis or external links as instructed. Please let me know if you would like me to modify or add any other points.