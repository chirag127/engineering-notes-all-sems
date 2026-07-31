# Myhill-Nerode Theorem

- The Myhill-Nerode theorem is a fundamental result in the theory of regular languages. It provides a necessary and sufficient condition for a language to be regular  .
- The theorem is based on the notion of **equivalence classes** of strings with respect to a language. Two strings are said to be **equivalent** with respect to a language if they can be extended by the same set of strings to form words in the language  .
- Formally, for a language L, we define an equivalence relation ~L on the set of all strings as follows:

  - For any two strings x and y, x ~L y if and only if for all strings z, xz is in L if and only if yz is in L  .

- The equivalence relation ~L partitions the set of all strings into disjoint subsets called **equivalence classes**. Each equivalence class contains all the strings that are equivalent to each other with respect to L  .
- The Myhill-Nerode theorem states that:

  - A language L is regular if and only if it has a finite number of equivalence classes under ~L, and moreover, that this number is equal to the number of states in the minimal deterministic finite automaton (DFA) accepting L  .

- The Myhill-Nerode theorem can be used to:

  - Prove that a language L is regular by showing that it has a finite number of equivalence classes under ~L. This can be done by an exhaustive case analysis in which, beginning from the empty string, distinguishing extensions are used to find additional equivalence classes until no more can be found  .
  - Prove that a language L is not regular by showing that it has an infinite number of equivalence classes under ~L. This can be done by finding an infinite set of strings that are pairwise inequivalent with respect to L  .
  - Find the minimal number of states in a DFA that recognizes L by finding the number of equivalence classes under ~L. This can be done by constructing a DFA that has one state for each equivalence class, and transitions that correspond to the extensions that preserve the equivalence  .