### Equivalence of Moore and Mealy Machine

- A Moore machine is a finite state machine where the output is determined only by the current state.
- A Mealy machine is a finite state machine where the output is determined by the current state and the input.
- The equivalence of the Moore and Mealy machine means that both the machines produce the same output for the same input.
- A Mealy machine can always be converted to a Moore machine, with the possible addition of extra states .
- A Moore machine can be converted to a Mealy machine by attaching the output of each state to the corresponding input transitions .

#### Conversion from Mealy to Moore Machine

- Step 1: Identify the states that have more than one output associated with them.
- Step 2: Create new states for each distinct output of the original states.
- Step 3: Distribute the incoming and outgoing transitions of the original states among the new states.
- Step 4: Assign the output of each new state as the output of the original state that it represents.
- Step 5: Remove the original states that have been replaced by the new states.

#### Conversion from Moore to Mealy Machine

- Step 1: Identify the output of each state in the Moore machine.
- Step 2: Attach the output of each state to the input transitions that lead to that state.
- Step 3: Remove the output of each state from the state label.
- Step 4: Simplify the Mealy machine by merging any equivalent states.