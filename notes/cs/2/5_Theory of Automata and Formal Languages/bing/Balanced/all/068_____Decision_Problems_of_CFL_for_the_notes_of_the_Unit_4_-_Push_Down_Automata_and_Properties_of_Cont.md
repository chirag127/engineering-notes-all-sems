# Decision Problems of CFL

- Decision problems are questions that can be answered by yes or no, such as whether a given string belongs to a language, or whether a language is empty or infinite.
- Decision problems for CFLs are important because they can help us determine the properties and limitations of CFLs and their corresponding models, such as CFGs and PDAs.
- Some common decision problems for CFLs are:

  - **Membership problem**: Given a CFG G and a string w, decide if w belongs to L(G).
    - This problem can be solved by using a PDA that simulates G and accepts w by empty stack or final state, or by using the CYK algorithm that checks if w can be derived from the start symbol of G.
    - This problem is decidable and has polynomial time complexity.
  - **Emptiness problem**: Given a CFG G, decide if L(G) is empty.
    - This problem can be solved by using a bottom-up search that marks all the symbols that can produce some terminal string, and then checking if the start symbol is marked or not.
    - This problem is decidable and has linear time complexity.
  - **Infiniteness problem**: Given a CFG G, decide if L(G) is infinite.
    - This problem can be solved by using the pumping lemma for CFLs, which states that if L(G) is infinite, then there exists some integer p such that any string w in L(G) with length at least p can be pumped, i.e., written as w = uvxyz such that |vxy| <= p, |vy| > 0, and uv^nxy^nz belongs to L(G) for any n >= 0.
    - This problem is decidable and has polynomial time complexity.
  - **Equivalence problem**: Given two CFGs G1 and G2, decide if L(G1) = L(G2).
    - This problem can be reduced to the emptiness problem by constructing a CFG G such that L(G) = L(G1) symmetric difference L(G2), i.e., the set of strings that belong to either L(G1) or L(G2) but not both, and then checking if L(G) is empty or not.
    - This problem is undecidable, i.e., there is no algorithm that can solve it for all possible inputs. This is because CFLs are not closed under complement, and if this problem were decidable, then we could also decide the complement problem, which is given a CFG G, decide if L(G) is the complement of L(G), i.e., the set of strings that do not belong to L(G).
  - **Containment problem**: Given two CFGs G1 and G2, decide if L(G1) is a subset of L(G2).
    - This problem can be reduced to the emptiness problem by constructing a CFG G such that L(G) = L(G1) intersection L(G2) complement, i.e., the set of strings that belong to L(G1) but not to L(G2), and then checking if L(G) is empty or not.
    - This problem is undecidable, for the same reason as the equivalence problem.