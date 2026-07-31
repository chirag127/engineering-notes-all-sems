# Equivalence of Moore and Mealy Machine

- A Moore machine is a finite state machine where the output depends only on the current state.
- A Mealy machine is a finite state machine where the output depends on the current state and the input.
- The equivalence of the Moore and Mealy machine means that both the machines produce the same output for the same input.
- A Mealy machine can always be converted to a Moore machine, with the possible addition of extra states .
- A Moore machine can be converted to a Mealy machine by attaching the output of each state to the corresponding input transitions.

## Conversion from Moore to Mealy Machine

- To convert a Moore machine to a Mealy machine, follow these steps:
  - For each state in the Moore machine, identify the output associated with it.
  - For each input transition from that state, label the transition with the output of the source state.
  - Remove the output labels from the states and keep only the state names.
  - The resulting machine is a Mealy machine equivalent to the original Moore machine.

## Conversion from Mealy to Moore Machine

- To convert a Mealy machine to a Moore machine, follow these steps:
  - For each state in the Mealy machine, identify the set of outputs that can be produced from that state for different inputs.
  - If the set contains only one output, keep the state as it is and label it with that output.
  - If the set contains more than one output, create a new state for each output and label it with that output.
  - For each input transition from the original state, redirect it to the new state corresponding to the output of that transition.
  - Remove the output labels from the transitions and keep only the input symbols.
  - The resulting machine is a Moore machine equivalent to the original Mealy machine.