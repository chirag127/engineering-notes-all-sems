# Equivalence of Moore and Mealy Machine

- A Moore machine is a finite state machine where the output depends only on the current state.
- A Mealy machine is a finite state machine where the output depends on the current state and the input.
- The equivalence of the Moore and Mealy machine means that both the machines produce the same output for the same input.
- A Mealy machine can always be converted to a Moore machine, with the possible addition of extra states .
- A Moore machine can also be converted to a Mealy machine, with the possible reduction of states .

## Conversion from Mealy to Moore Machine

- The general method to convert a Mealy machine to a Moore machine is as follows :

  - Step 1: Identify the states that have more than one output associated with them.
  - Step 2: Create new states for each distinct output of the original states.
  - Step 3: Distribute the incoming and outgoing transitions of the original states among the new states.
  - Step 4: Assign the output of each new state according to the original state's output.
  - Step 5: Remove any unreachable or redundant states.

- For example, consider the following Mealy machine:

  ![Mealy machine](https://cstaleem.com/wp-content/uploads/2020/10/Mealy-Machine-1.png)

  - Step 1: The states q1 and q2 have more than one output associated with them.
  - Step 2: We create four new states: q1a, q1b, q2a, and q2b.
  - Step 3: We distribute the transitions as follows:

    - q0 -> q1a on input 0
    - q0 -> q2a on input 1
    - q1a -> q1b on input 0
    - q1a -> q2a on input 1
    - q1b -> q1b on input 0
    - q1b -> q2a on input 1
    - q2a -> q1a on input 0
    - q2a -> q2b on input 1
    - q2b -> q1a on input 0
    - q2b -> q2b on input 1

  - Step 4: We assign the output of each new state as follows:

    - q1a and q2a have output 0
    - q1b and q2b have output 1

  - Step 5: We remove any unreachable or redundant states. In this case, there are none.

  - The resulting Moore machine is:

    ![Moore machine](https://cstaleem.com/wp-content/uploads/2020/10/Moore-Machine-1.png)

## Conversion from Moore to Mealy Machine

- The general method to convert a Moore machine to a Mealy machine is as follows :

  - Step 1: Identify the states that have the same output and are reachable from each other by the same input.
  - Step 2: Merge those states into one state and assign the output to the corresponding transition.
  - Step 3: Remove any unreachable or redundant states.

- For example, consider the following Moore machine:

  ![Moore machine](https://cstaleem.com/wp-content/uploads/2020/10/Moore-Machine-2.png)

  - Step 1: The states q1 and q2 have the same output 0 and are reachable from each other by input 0. The states q3 and q4 have the same output 1 and are reachable from each other by input 1.
  - Step 2: We merge q1 and q2 into one state q12 and assign the output 0 to the transition on input 0. We merge q3 and q4 into one state q34 and assign the output 1 to the transition on input 1.
  - Step 3: We remove any unreachable or redundant states. In this case, there are none.

  - The resulting Mealy machine is:

    ![Mealy machine](https://cstaleem.com/wp-content/uploads/2020/10/Mealy-Machine-2.png)

: https://math.stackexchange.com/questions/268888/my-moore-and-mealy-machines-look-the-same-why