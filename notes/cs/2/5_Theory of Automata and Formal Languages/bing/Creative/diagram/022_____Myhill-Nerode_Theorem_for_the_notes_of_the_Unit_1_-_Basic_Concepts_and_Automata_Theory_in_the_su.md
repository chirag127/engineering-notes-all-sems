### Myhill-Nerode Theorem

- The Myhill-Nerode theorem is a fundamental result in the theory of regular languages. It provides a necessary and sufficient condition for a language to be regular  .
- The theorem is based on the concept of **equivalence classes** of strings with respect to a language. Two strings are said to be **equivalent** with respect to a language if they can be extended by the same set of strings to form words in the language  .
- Formally, for a language L, we define an equivalence relation ~L on the set of all strings as follows:

  - For any two strings x and y, x ~L y if and only if for all strings z, xz is in L if and only if yz is in L  .

- The equivalence relation ~L partitions the set of all strings into disjoint subsets called **equivalence classes**. Each equivalence class contains all the strings that are equivalent to each other with respect to L  .
- The Myhill-Nerode theorem states that a language L is regular if and only if it has a **finite** number of equivalence classes, and moreover, that this number is equal to the number of states in the **minimal deterministic finite automaton (DFA)** accepting L  .
- The Myhill-Nerode theorem can be used to show that a language is regular by proving that the number of equivalence classes of L is finite. This can be done by an exhaustive case analysis in which, beginning from the empty string, distinguishing extensions are used to find additional equivalence classes until no more can be found  .
- The Myhill-Nerode theorem can also be used to show that a language is not regular by proving that the number of equivalence classes of L is infinite. This can be done by showing that for any two strings x and y, there exists a string z such that xz is in L but yz is not in L, or vice versa  .
- The Myhill-Nerode theorem can also be used to construct the minimal DFA for a regular language L by taking the equivalence classes of L as the states, the empty string class as the initial state, the classes containing strings in L as the final states, and the transitions defined by the extensions of the strings in each class  .

: Myhill–Nerode theorem - Wikipedia
: THE MYHILL-NERODE THEOREM - Columbia University
: Basic Theorems in TOC (Myhill nerode theorem) - GeeksforGeeks