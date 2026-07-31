### Decision Problems of CFL

- Decision problems are questions that can be answered by yes or no, such as whether a given string belongs to a language, or whether a language is empty or infinite.
- Decision problems for CFLs are important because they can help us determine the properties and limitations of CFLs and their corresponding models, such as CFGs and PDAs.
- Some common decision problems for CFLs are:

  - Membership problem: Given a CFG G and a string w, decide if w belongs to L(G).
    - This problem can be solved by using a PDA that simulates G and accepts w by empty stack or final state, or by using the CYK algorithm that checks if w can be derived from the start symbol of G using a table of subderivations.
    - This problem is decidable and has polynomial time complexity.
  - Emptiness problem: Given a CFG G, decide if L(G) is empty.
    - This problem can be solved by checking if the start symbol of G is useful, i.e., it can produce some terminal string through some sequence of productions.
    - This problem is decidable and has linear time complexity.
  - Infiniteness problem: Given a CFG G, decide if L(G) is infinite.
    - This problem can be solved by checking if G contains a cycle, i.e., a nonterminal symbol that can derive itself through some sequence of productions.
    - This problem is decidable and has linear time complexity.
  - Equivalence problem: Given two CFGs G1 and G2, decide if L(G1) = L(G2).
    - This problem can be reduced to the complement and intersection problems, i.e., checking if L(G1) - L(G2) and L(G2) - L(G1) are both empty, or checking if L(G1) ∩ L(G2) = L(G1) ∪ L(G2).
    - This problem is undecidable, because CFLs are not closed under complement or intersection, and there is no algorithm that can compare two arbitrary CFLs for equality.
  - Containment problem: Given two CFGs G1 and G2, decide if L(G1) ⊆ L(G2).
    - This problem can be reduced to the difference problem, i.e., checking if L(G1) - L(G2) is empty.
    - This problem is undecidable, because CFLs are not closed under difference, and there is no algorithm that can compare two arbitrary CFLs for inclusion.
  - Ambiguity problem: Given a CFG G, decide if G is ambiguous, i.e., there exists some string in L(G) that has more than one leftmost derivation or more than one rightmost derivation.
    - This problem is undecidable, because there is no algorithm that can check all possible strings in L(G) for ambiguity, and there is no general criterion that can determine the ambiguity of a CFG.