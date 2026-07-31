 Here is the content written in markdown format for the given topic:

### Deterministic Context free Languages(DCFL)

- A Deterministic Context Free Language(DCFL) is a context free language in which every production rule has either a single variable on the left-hand side or epsilon.
- In DCFL, for each set of symbols on the right-hand side of the production rules, there is at most one set of symbols on the left-hand side.
- DCFL can be recognized by Deterministic Pushdown Automata(DPDA).
- Every Regular Language is a DCFL but the converse is not true. Some examples of DCFL which are not regular are:
    - {a^n b^n | n>=1}
    - {a^i b^j c^k | i,j and k >=0}
- The Pumping Lemma for DCFL states that if L is a DCFL and w is in L such that |w|>=p then there exists u,v,x,y such that:
    - w=uvxy
    - |vxy|<=p
    - For all i>=0, uv^ixy is in L
- Closure properties of DCFL under union, concatenation, Kleene star and homomorphism are same as CF. Inverse homomorphism may change DCFL to a non-DCFL.
- DCFL can be parsed in linear time using Earley's algorithm while a general CFG may require exponential time in the worst case. Hence, DCFL have applications in programming languages where parsing efficiency is desired.

The content is written in points and in a formal tone without any emojis or external links as instructed. Please let me know if you would like me to modify or add anything to the content.