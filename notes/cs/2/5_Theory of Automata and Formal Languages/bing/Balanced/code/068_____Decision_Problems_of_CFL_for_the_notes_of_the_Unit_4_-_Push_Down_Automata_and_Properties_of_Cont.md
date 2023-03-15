### Decision Problems of CFL

- Decision problems are questions that can be answered with a yes or no answer.
- Decision problems for CFLs are problems that involve determining some property of a CFL or a CFG.
- Some examples of decision problems for CFLs are:
  - Membership problem: Given a CFG G and a string w, decide if w is in L(G).
  - Emptiness problem: Given a CFG G, decide if L(G) is empty.
  - Finiteness problem: Given a CFG G, decide if L(G) is finite.
  - Equivalence problem: Given two CFGs G1 and G2, decide if L(G1) = L(G2).
  - Containment problem: Given two CFGs G1 and G2, decide if L(G1) is a subset of L(G2).
  - Disjointness problem: Given two CFGs G1 and G2, decide if L(G1) and L(G2) are disjoint.
- Some of these problems are decidable, meaning that there exists an algorithm that can always give a correct answer in a finite amount of time. Some of these problems are undecidable, meaning that no such algorithm exists.
- The following table summarizes the decidability of some common decision problems for CFLs:

| Problem | Decidable or Undecidable | Reason |
| --- | --- | --- |
| Membership | Decidable | Use CYK algorithm or convert CFG to PDA and simulate |
| Emptiness | Decidable | Use bottom-up search to find useful symbols |
| Finiteness | Decidable | Use pumping lemma for CFLs to find a contradiction |
| Equivalence | Undecidable | Reduce from PCP, which is undecidable |
| Containment | Undecidable | Reduce from equivalence problem |
| Disjointness | Undecidable | Reduce from emptiness problem |

- The decidability of these problems has implications for the closure properties of CFLs. For example, if CFLs were closed under intersection, then the equivalence problem would be decidable, which is a contradiction. However, if one of the languages is regular, then the intersection is a CFL.