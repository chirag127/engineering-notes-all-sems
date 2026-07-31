### Myhill-Nerode Theorem

- The Myhill-Nerode theorem is a fundamental result in the theory of regular languages. It provides a necessary and sufficient condition for a language to be regular  .
- The theorem is based on the concept of an equivalence relation on the set of all strings over a given alphabet. The relation is defined as follows: for any language L, two strings x and y are equivalent (denoted by x ~ y) if and only if for any string z, xz belongs to L if and only if yz belongs to L  .
- In other words, x and y are equivalent if they can be extended by the same strings to form words in L. For example, if L is the language of all strings that end with 01, then 0 ~ 10, 1 ~ 11, and 00 ~ 100, but 0 ~/= 1, 10 ~/= 11, and 00 ~/= 01 .
- The equivalence relation ~ partitions the set of all strings into equivalence classes. Each equivalence class contains all the strings that are equivalent to each other. For example, the equivalence class of 0 for the language L above is [0] = {0, 10, 100, 110, ...} .
- The Myhill-Nerode theorem states that a language is regular if and only if it has a finite number of equivalence classes, and moreover, that this number is equal to the number of states in the minimal deterministic finite automaton (DFA) accepting L  .
- The theorem also provides a constructive way to obtain the minimal DFA for a regular language L. The states of the DFA are the equivalence classes of ~, the initial state is the equivalence class of the empty string, the final states are the equivalence classes that contain strings in L, and the transition function is defined by [x]a = [xa], where a is any symbol in the alphabet  .
- The Myhill-Nerode theorem can be used to prove that a language is regular by showing that it has a finite number of equivalence classes. This can be done by an exhaustive case analysis in which, beginning from the empty string, distinguishing extensions are used to find additional equivalence classes until no more can be found  .
- The theorem can also be used to prove that a language is not regular by showing that it has an infinite number of equivalence classes. This can be done by finding an infinite set of strings that are pairwise inequivalent, meaning that for any two strings x and y in the set, there exists a string z such that xz belongs to L but yz does not, or vice versa  .

: Myhill–Nerode theorem - Wikipedia
: THE MYHILL-NERODE THEOREM - Columbia University
: Basic Theorems in TOC (Myhill nerode theorem) - GeeksforGeeks