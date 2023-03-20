 Here is the content in markdown format without any emojis or external links and in a formal tone:

### Pumping Lemma for CFL

**Pumping Lemma:** For any context-free language L, there exists a constant N such that any string w in L with |w| >= N can be pumped, i.e. there exist strings x, y, z such that:

1. w = xyz
2. |xy| <= N
3. For all i >= 0, xiyiz is in L

* The pumping lemma is used to show that a language is not context-free by assuming it is context-free and reaching a contradiction.
* If we can pump a sufficiently long string w in a language L and get a string not in L, then L cannot be context-free.
* The pumping lemma gives a necessary condition for context-freedom. If a language satisfies the pumping lemma, it must be context-free. The converse is not true.

**Proof:** Let L be a CFL and G = (V, Σ, P, S) be a CFG generating L. Let w be any string in L with |w| >= N, where N is the number of variables in the right-hand side of any production in P. We can write w = xyz such that:

1. |xy| <= N
2. z is as long as possible

Since G generates w, S =>* x1y1z for some x1, y1. But since |xy| <= N, we can repeat the portion xy n times to get a longer string in L: xny1z. So L satisfies the pumping lemma.

**Example:** Show that {a^n b^n c^n | n >= 1} is not a CFL using pumping lemma.
* Assume it is a CFL and take a string w = a^5b^5c^5
* Split: w = xyz, where |xy| <= N
* Then: x = a^i, y = b^j, z = c^k for some i,j,k with i+j+k = 5 and i <= N
* But then wx = a^(i+1)b^(j+1)c^(k+1) which is not in the language (the exponents are not equal)
* Therefore, the assumption was wrong and the language is not a CFL.