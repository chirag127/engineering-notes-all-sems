### Decision Problems of CFL

- Decision problems are questions that can be answered by yes or no, such as whether a given string belongs to a language, or whether a language is empty or infinite.
- Decision problems for CFLs are important because they can help us determine the properties and limitations of CFLs and their corresponding models, such as CFGs and PDAs.
- Some common decision problems for CFLs are:

  - Membership problem: Given a CFG G and a string w, decide if w belongs to L(G).
    - This problem can be solved by using a PDA that simulates G and accepts w by empty stack or final state.
    - Alternatively, this problem can be solved by using the CYK algorithm, which is a dynamic programming technique that checks if w can be derived from the start symbol of G using the rules of G.
    - The membership problem for CFLs is decidable in polynomial time.

  - Emptiness problem: Given a CFG G, decide if L(G) is empty.
    - This problem can be solved by finding the set of useful symbols of G, which are the symbols that can produce some terminal string through some sequence of rules.
    - If the start symbol of G is not useful, then L(G) is empty. Otherwise, L(G) is nonempty.
    - The emptiness problem for CFLs is decidable in linear time.

  - Infiniteness problem: Given a CFG G, decide if L(G) is infinite.
    - This problem can be solved by using the pumping lemma for CFLs, which states that if L(G) is infinite, then there exists some integer p such that for any string w in L(G) with length at least p, w can be written as w = uvxyz, where |vxy| <= p, |vy| > 0, and for any integer i, u(v^i)x(y^i)z is also in L(G).
    - To decide if L(G) is infinite, we can construct a directed graph where the nodes are the nonterminals of G, and there is an edge from A to B if there is a rule A -> alpha B beta, where alpha and beta are strings of terminals and nonterminals.
    - If the graph contains a cycle, then L(G) is infinite. Otherwise, L(G) is finite.
    - The infiniteness problem for CFLs is decidable in polynomial time.

  - Equivalence problem: Given two CFGs G1 and G2, decide if L(G1) = L(G2).
    - This problem is undecidable for CFLs, because it can be reduced from the halting problem, which is a well-known undecidable problem for Turing machines.
    - The halting problem asks whether a given Turing machine M halts on a given input w.
    - To reduce the halting problem to the equivalence problem, we can construct two CFGs G1 and G2 such that L(G1) = {0^n 1^n | n >= 0} and L(G2) = {0^n 1^n | n >= 0 and M halts on 0^n}.
    - Then, M halts on w if and only if L(G1) = L(G2).
    - Since the halting problem is undecidable, so is the equivalence problem for CFLs.

  - Intersection problem: Given two CFLs L1 and L2, decide if L1 ∩ L2 is empty.
    - This problem is undecidable for CFLs, because it can be reduced from the equivalence problem, which is undecidable for CFLs.
    - To reduce the equivalence problem to the intersection problem, we can construct two CFLs L1 and L2 such that L1 = L(G1) and L2 = L(G2) ∪ {a}, where G1 and G2 are two CFGs and a is a terminal symbol that does not appear in G1 or G2.
    - Then, L(G1) = L(G2) if and only if L1 ∩ L2 = {a}.
    - Since the equivalence problem is undecidable, so is the intersection problem for CFLs.

- However, if one of the languages is regular, then some of the undecidable problems become decidable for CFLs, such as:

  - Intersection problem: Given a CFL L and a regular language R, decide if L ∩ R is empty.
    - This problem can be solved by using the fact that L ∩ R is also a CFL,