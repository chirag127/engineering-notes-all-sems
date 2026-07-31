# Myhill-Nerode Theorem

- The Myhill-Nerode theorem is a fundamental result in the theory of regular languages. It provides a necessary and sufficient condition for a language to be regular  .
- The theorem is based on the notion of **equivalence classes** of strings with respect to a language. Two strings are said to be **equivalent** with respect to a language if they can be extended by the same set of strings to form words in the language  .
- Formally, for a language L, we define an equivalence relation ~L on the set of all strings as follows: for any two strings x and y, x ~L y if and only if for all strings z, xz is in L if and only if yz is in L  .
- The equivalence relation ~L partitions the set of all strings into disjoint subsets called **equivalence classes**. Each equivalence class contains all the strings that are equivalent with respect to L. We denote the equivalence class of a string x by [x]L  .
- The Myhill-Nerode theorem states that a language L is regular if and only if it has a **finite** number of equivalence classes, and moreover, that this number is equal to the number of states in the **minimal deterministic finite automaton (DFA)** accepting L  .
- The Myhill-Nerode theorem can be used to prove that a language is regular by showing that it has a finite number of equivalence classes. This can be done by an exhaustive case analysis in which, beginning from the empty string, distinguishing extensions are used to find additional equivalence classes until no more can be found  .
- The Myhill-Nerode theorem can also be used to prove that a language is not regular by showing that it has an **infinite** number of equivalence classes. This can be done by finding an infinite set of strings that are pairwise **distinguishable** with respect to L, meaning that for any two distinct strings x and y in the set, there exists a string z such that xz is in L but yz is not, or vice versa  .
- The Myhill-Nerode theorem can also be used to construct the minimal DFA for a regular language L by taking the equivalence classes of L as the states, the initial state as the equivalence class of the empty string, the final states as the equivalence classes that contain strings in L, and the transition function as the mapping from an equivalence class [x]L and a symbol a to the equivalence class [xa]L  .

: Myhill–Nerode theorem - Wikipedia
: THE MYHILL-NERODE THEOREM - Columbia University
: Basic Theorems in TOC (Myhill nerode theorem) - GeeksforGeeks