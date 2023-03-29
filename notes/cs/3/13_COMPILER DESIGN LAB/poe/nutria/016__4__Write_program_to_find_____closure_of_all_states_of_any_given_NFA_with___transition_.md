
### 4. Write program to find ε – closure of all states of any given NFA with ε transition

* To find the ε-closure of any given state in a NFA with ε transitions, the algorithm must first identify the transitions from the given state to other states with ε transitions. 
* The algorithm should then identify the states that can be reached from the given state by following the ε transitions. 
* This is done by recursively searching for ε-transitions from the given state and any states that can be reached from it. 
* Once the set of states that can be reached from the given state by following ε-transitions is identified, the ε-closure of the given state is the union of the given state and all the states that can be reached from it by following ε-transitions. 
* The algorithm should then repeat the process for each of the states in the ε-closure of the given state, until all the states in the NFA with ε-transitions have been visited. 
* Finally, the algorithm should return the ε-closure of the given state.